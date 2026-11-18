"""Decode a .kpatch into a readable report: what exactly it changes in the game file.

Usage:
  python decode_patch.py <original game file> <file.kpatch> [report.txt]

The original file must be the unmodded Steam file the patch was made from (the script checks the
patch's recorded old size). The kind of file is detected automatically:

  TMNTSF.exe  - PE header / section changes, then every changed code site disassembled
                (original vs patched), then every new code block ("cave") disassembled with labels,
                and the data the caves use (strings, numbers).
  *.pak2      - which archive entries change or are added, and for each one:
                CFF0 game-data records: new symbols, every new field (pointers resolved to strings),
                and any byte changed inside the original record;
                textures: size change and the sprite list (new / moved sprites);
                the voice-line database (JSON): every added or changed criterion, response and rule;
                UIML layouts and anything else: changed ranges as hex with readable strings.

Nothing is written back to the game file.
"""
import os, sys, struct, json, zlib, re, hashlib, io
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import kpatch

out = io.StringIO()
def w(s=''): out.write(s + '\n')

# ----------------------------------------------------------------------------------------- helpers
def hexrows(b, base=0, width=16, indent='    '):
    for i in range(0, len(b), width):
        ch = b[i:i + width]
        asc = ''.join(chr(c) if 32 <= c < 127 else '.' for c in ch)
        w('%s%08x  %-*s  %s' % (indent, base + i, width * 3, ch.hex(' '), asc))

def cstr_at(b, o, maxlen=200):
    if o < 0 or o >= len(b): return None
    e = b.find(b'\0', o, o + maxlen)
    if e <= o: return None
    s = b[o:e]
    if all(32 <= c < 127 for c in s): return s.decode()
    return None

def ranges_merged(R, gap=32):
    """kpatch ranges -> merged (start, end) spans."""
    sp = []
    for off, new, old in sorted(R, key=lambda r: r[0]):
        if sp and off <= sp[-1][1] + gap: sp[-1][1] = max(sp[-1][1], off + len(new))
        else: sp.append([off, off + len(new)])
    return sp

# ============================================================================================ EXE
# Original-game functions and globals the mod's code calls or reads (names from the reverse engineering, docs/FORMATS.md)
KNOWN = {
    0x1415f6b90: 'behavior registry list head (name -> factory)', 0x14055c6f8: 'registry init (list -> map)',
    0x140534f30: 'std::string assign', 0x140f6c550: 'rand (import)',
    0x140cd3160: 'AddBuff', 0x140cded04: 'ActionApplyBuff::Execute', 0x140d06f6c: 'buff definition lookup',
    0x140d0cb44: 'BB_SwapAbilityAlias handler', 0x14053df00: 'set damage value',
    0x1406adf2c: 'hero stat fn 0x18 (combo damage)', 0x1406adf48: 'hero stat fn 0x1a (special damage)',
    0x14088ba70: 'hero stat fn 0x1d (special effect damage)', 0x140cf62fc: 'set timed phase (seconds)',
    0x140683650: 'HUD ability-button chooser', 0x1406b2200: 'make actor condition', 0x1406b19a4: 'actor condition eval',
    0x14084aab8: 'level logic: NewRule', 0x140cf6cc8: 'level logic: response-trigger param',
    0x140a7a8bc: 'level logic: swap player hero action', 0x1409d0b30: 'level logic: add actions to rule', 0x140ce011c: 'destroy temp',
    0x140883de8: 'factory Raphael_Attack_Chain', 0x140884028: 'factory Raphael_Attack_Chain1', 0x140884f04: 'factory Raphael_Attack_Chain2',
    0x140885e08: 'factory Raphael_Attack_Chain3', 0x140886d90: 'factory Raphael_Attack_Chain4', 0x14088863c: 'factory Raphael_DashAttack',
    0x140b5bb74: 'factory Boss_Shredder_SpinKick', 0x140b5eccc: 'factory Shredder_Leap_Attack', 0x140ab5680: 'factory Ability_Ninja_001_SmokeBomb',
}
def decode_exe(orig, new, R, collect=None):
    import pefile, capstone
    po = pefile.PE(data=orig, fast_load=True); pn = pefile.PE(data=new, fast_load=True)
    IB = pn.OPTIONAL_HEADER.ImageBase
    md = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_64); md.detail = True

    def secs(p):
        return [(s.Name.rstrip(b'\0').decode(), s.VirtualAddress, s.Misc_VirtualSize, s.PointerToRawData,
                 s.SizeOfRawData, s.Characteristics) for s in p.sections]
    SO, SN = secs(po), secs(pn)
    def off2va(off, S):
        for n, va, vs, ro, rs, ch in S:
            if ro <= off < ro + rs: return IB + va + off - ro, n
        return None, None
    def va2off(va, S, data_len):
        r = va - IB
        for n, sva, vs, ro, rs, ch in S:
            if sva <= r < sva + max(vs, rs):
                o = ro + r - sva
                return o if r - sva < rs else None
        return None

    w('=' * 100); w('PE HEADER'); w('=' * 100)
    for fld in ('SizeOfImage', 'CheckSum', 'SizeOfCode', 'SizeOfInitializedData'):
        a, b = getattr(po.OPTIONAL_HEADER, fld), getattr(pn.OPTIONAL_HEADER, fld)
        if a != b: w('  OptionalHeader.%-22s %#x -> %#x' % (fld, a, b))
    if po.FILE_HEADER.NumberOfSections != pn.FILE_HEADER.NumberOfSections:
        w('  FileHeader.NumberOfSections        %d -> %d' % (po.FILE_HEADER.NumberOfSections, pn.FILE_HEADER.NumberOfSections))
    for i, nm in enumerate(('EXPORT', 'IMPORT', 'RESOURCE', 'EXCEPTION', 'SECURITY', 'BASERELOC')):
        a = po.OPTIONAL_HEADER.DATA_DIRECTORY[i]; b = pn.OPTIONAL_HEADER.DATA_DIRECTORY[i]
        if (a.VirtualAddress, a.Size) != (b.VirtualAddress, b.Size):
            w('  DataDirectory[%s]  (%#x, %#x) -> (%#x, %#x)%s' % (nm, a.VirtualAddress, a.Size, b.VirtualAddress, b.Size,
              '   (Authenticode signature block dropped: a patched exe can no longer carry the original signature)' if nm == 'SECURITY' else ''))
    w(); w('  Sections (name, RVA, virtual size, file offset, file size, flags):')
    old = {s[0]: s for s in SO}
    for s in SN:
        o = old.get(s[0])
        tag = 'NEW ' if o is None else ('CHG ' if o != s else '    ')
        w('   %s%-9s %#9x %#9x %#9x %#9x %#010x' % (tag, *s))
        if o is not None and o != s:
            w('        was  %#9x %#9x %#9x %#9x %#010x' % o[1:])
    if len(new) != len(orig):
        w(); w('  File size %d -> %d bytes (the old file ends with data past the last section, e.g. the signature)' % (len(orig), len(new)))

    # classify changed bytes
    newsec = {s[0] for s in SN} - {s[0] for s in SO}
    text = [s for s in SO if s[0] == '.text'][0]
    text_old_end = IB + text[1] + text[2]
    sites, cave_spans, other = [], [], []
    for a, b in ranges_merged(R, gap=8):
        va, sn = off2va(a, SN)
        if va is None: other.append((a, b)); continue
        if sn in newsec: cave_spans.append((va, va + (b - a)))
        elif sn == '.text' and va >= text_old_end: cave_spans.append((va, va + (b - a)))
        elif sn == '.text' and va + (b - a) > text_old_end:
            sites.append((va, text_old_end, a)); cave_spans.append((text_old_end, va + (b - a)))
        else: sites.append((va, va + (b - a), a)) if sn == '.text' else other.append((a, b))

    def dis_range(data_S, data, start, end, maxn=400):
        o = va2off(start, data_S, len(data))
        if o is None: return []
        res = []
        for ins in md.disasm(bytes(data[o:o + (end - start) + 16]), start):
            if ins.address >= end or len(res) >= maxn: break
            res.append(ins)
        return res

    # function starts from .pdata (original exe) to align disassembly
    import bisect
    pd = po.OPTIONAL_HEADER.DATA_DIRECTORY[3]
    po_ = pefile.PE(data=orig, fast_load=True)
    fstarts = []
    pdo = va2off(IB + pd.VirtualAddress, SO, len(orig))
    for k in range(pd.Size // 12):
        b0, e0, u = struct.unpack_from('<III', orig, pdo + 12 * k); fstarts.append(IB + b0)
    fstarts.sort()

    def aligned_start(va):
        i = bisect.bisect_right(fstarts, va) - 1
        s = fstarts[i] if i >= 0 else va
        if va - s > 0x4000: s = va
        last = s
        for ins in dis_range(SO, orig, s, va + 1, maxn=100000):
            if ins.address > va: break
            last = ins.address
        return last

    def fmt(ins, data, S, names):
        txt = '%s %s' % (ins.mnemonic, ins.op_str)
        note = ''
        tgt = None
        if ins.mnemonic.startswith('j') or ins.mnemonic == 'call':
            try: tgt = int(ins.op_str, 16)
            except ValueError: pass
        m = re.search(r'\[rip ([+-]) (0x[0-9a-f]+)\]', ins.op_str)
        if m:
            tgt = ins.address + ins.size + (int(m.group(2), 16) * (1 if m.group(1) == '+' else -1))
            txt = txt.replace(m.group(0), '[%#x]' % tgt)
        if tgt is not None:
            if tgt in names: note = names[tgt]
            elif tgt in KNOWN: note = KNOWN[tgt]
            else:
                o = va2off(tgt, S, len(data))
                s = cstr_at(data, o) if o is not None else None
                if s and len(s) >= 3: note = repr(s)
                elif o is not None and ('xmm' in ins.op_str or 'dword' in ins.op_str) and ins.mnemonic.startswith(('movss', 'mulss', 'addss', 'comiss', 'ucomiss', 'divss', 'subss')):
                    note = 'float %g' % struct.unpack_from('<f', data, o)[0]
        return '%-60s %s' % (txt, ('; ' + note) if note else '')

    # ---- cave code: recursive descent from every branch / call / lea target that lands in a cave
    in_cave = lambda va: any(a <= va < b for a, b in cave_spans)
    entries = set()
    for va, end, off in sites:
        for ins in dis_range(SN, new, aligned_start(va), end + 16):
            for g in ins.operands if ins.operands else []:
                pass
            t = None
            if ins.mnemonic.startswith('j') or ins.mnemonic == 'call':
                try: t = int(ins.op_str, 16)
                except ValueError: t = None
            m = re.search(r'\[rip ([+-]) (0x[0-9a-f]+)\]', ins.op_str)
            if m: t = ins.address + ins.size + (int(m.group(2), 16) * (1 if m.group(1) == '+' else -1))
            if t is not None and in_cave(t): entries.add(t)
    code = {}          # va -> ins
    data_refs = set()
    work = sorted(entries)
    def plausible(va):
        """Is a lea target code (a function pointer the cave installs) rather than data?"""
        o = va2off(va, SN, len(new))
        if o is None: return False
        if new[o] in (0, 0xcc): return False
        s = cstr_at(new, o)
        if s is not None and len(s) >= 2: return False
        n = 0
        for ins in md.disasm(bytes(new[o:o + 96]), va):
            if ins.bytes[:2] == b'\0\0' or ins.mnemonic in ('outsd', 'insd', 'outsb', 'insb', 'in', 'out', 'sldt', 'hlt'): return False
            n += 1
            if ins.mnemonic in ('ret', 'jmp') or n >= 8: return True
        return False
    seen = set()
    while work:
        va = work.pop()
        if va in seen or not in_cave(va): continue
        seen.add(va)
        o = va2off(va, SN, len(new))
        if o is None: continue
        for ins in md.disasm(bytes(new[o:o + 0x2000]), va):
            if ins.address in code: break
            if not in_cave(ins.address): break
            code[ins.address] = ins
            t = None
            if ins.mnemonic.startswith('j') or ins.mnemonic == 'call':
                try: t = int(ins.op_str, 16)
                except ValueError: t = None
                if t is not None and in_cave(t): work.append(t)
            m = re.search(r'\[rip ([+-]) (0x[0-9a-f]+)\]', ins.op_str)
            if m:
                t2 = ins.address + ins.size + (int(m.group(2), 16) * (1 if m.group(1) == '+' else -1))
                if in_cave(t2):
                    if ins.mnemonic == 'lea' and plausible(t2) and t2 % 4 == 0: work.append(t2)
                    else: data_refs.add(t2)
            if ins.mnemonic in ('ret', 'jmp', 'int3', 'ud2'): break
    # labels
    labels = {}
    for ins in code.values():
        if ins.mnemonic.startswith('j') or ins.mnemonic == 'call':
            try:
                t = int(ins.op_str, 16)
                if t in code: labels.setdefault(t, 'L_%x' % t)
            except ValueError: pass
    for e in entries: labels[e] = 'ENTRY_%x' % e
    names = dict(labels)
    if collect is not None:
        collect.update(sites=sites, cave_spans=cave_spans, code=code, labels=labels, other=other, SO=SO, SN=SN, IB=IB,
                       va2off=va2off, off2va=off2va, aligned_start=aligned_start, dis_range=dis_range, md=md)

    w(); w('=' * 100); w('CHANGED CODE SITES IN THE ORIGINAL GAME CODE (.text): %d' % len(sites)); w('=' * 100)
    w('Each site shows the original instructions, then the patched bytes. A patched site is usually a jump into')
    w('new code (a "cave", listed in the next part), or a constant/branch change.')
    for va, end, off in sites:
        s0 = aligned_start(va)
        ol = dis_range(SO, orig, s0, end)
        oend = max((i.address + i.size for i in ol), default=end)
        nl = dis_range(SN, new, s0, max(end, oend))
        w(); w('-- site %#x .. %#x (%d bytes changed)' % (va, end, end - va))
        w('   original:')
        for i in ol: w('     %x: %-24s %s' % (i.address, i.bytes.hex(), fmt(i, orig, SO, {})))
        w('   patched:')
        for i in nl: w('     %x: %-24s %s' % (i.address, i.bytes.hex(), fmt(i, new, SN, names)))

    w(); w('=' * 100); w('NEW CODE (caves) %s' % ', '.join('%#x..%#x' % s for s in cave_spans)); w('=' * 100)
    w('Disassembled by following every jump/call/lea from the changed sites. Bytes that are not reached as')
    w('code are listed afterwards as data (strings, numbers, tables).')
    last = None
    for a in sorted(code):
        ins = code[a]
        if last is not None and a != last: w('     ...')
        if a in labels: w(); w('%s:' % labels[a])
        w('     %x: %-24s %s' % (a, ins.bytes.hex(), fmt(ins, new, SN, names)))
        last = a + ins.size
    # data
    covered = set()
    for a, ins in code.items(): covered.update(range(a, a + ins.size))
    w(); w('=' * 100); w('DATA IN THE NEW SECTIONS (everything not decoded as code above)'); w('=' * 100)
    for a, b in cave_spans:
        va = a
        while va < b:
            if va in covered: va += 1; continue
            st = va
            while va < b and va not in covered: va += 1
            o = va2off(st, SN, len(new)); blob = new[o:o + (va - st)] if o is not None else b''
            if not blob.strip(b'\0\xcc'): continue
            # trim padding
            lead = len(blob) - len(blob.lstrip(b'\0\xcc')); blob2 = blob.strip(b'\0\xcc'); st2 = st + lead
            w(); w('-- %#x .. %#x (%d bytes)%s' % (st2, st2 + len(blob2), len(blob2), '   <- referenced by code' if any(st2 <= r < st2 + len(blob2) for r in data_refs) else ''))
            strs = [(m.start(), m.group().decode()) for m in re.finditer(rb'[\x20-\x7e]{4,}', blob2)]
            u16 = [(m.start(), m.group().decode('utf-16le')) for m in re.finditer(rb'(?:[\x20-\x7e]\x00){4,}', blob2)]
            for p, s in strs: w('     string  %#x: %r' % (st2 + p, s))
            for p, s in u16: w('     utf-16  %#x: %r' % (st2 + p, s))
            if len(blob2) <= 64 and not strs:
                fl = [struct.unpack_from('<f', blob2, k)[0] for k in range(0, len(blob2) - 3, 4)]
                if fl and all(abs(x) < 1e6 for x in fl): w('     as floats: %s' % ', '.join('%g' % x for x in fl))
            hexrows(blob2[:2048], st2, indent='     ')
            if len(blob2) > 2048: w('     ... (%d more bytes)' % (len(blob2) - 2048))
    if other:
        w(); w('=' * 100); w('OTHER CHANGED BYTES (headers, data sections)'); w('=' * 100)
        for a, b in other:
            va, sn = off2va(a, SN)
            w('-- file offset %#x..%#x  %s' % (a, b, ('%s VA %#x' % (sn, va)) if va else 'PE header / end of file'))
            ob = orig[a:b] if a < len(orig) else b''
            w('   old:'); hexrows(ob[:256], a)
            w('   new:'); hexrows(new[a:b][:256], a)

# =========================================================================================== PAK2
def decode_pak(orig, new, R, name):
    import pak
    from cff import load as cffload
    from hashes import lookup2
    d0, E0 = pak.read_dir(orig); d1, E1 = pak.read_dir(new)
    M0 = {e[0]: e for e in E0}; M1 = {e[0]: e for e in E1}
    changed = [k for k in M1 if k in M0 and bytes(orig[M0[k][1]:M0[k][1] + M0[k][2]]) != bytes(new[M1[k][1]:M1[k][1] + M1[k][2]])]
    added = [k for k in M1 if k not in M0]
    removed = [k for k in M0 if k not in M1]
    w('=' * 100); w('ARCHIVE %s: %d entries -> %d. Changed: %d, added: %d, removed: %d' % (name, len(E0), len(E1), len(changed), len(added), len(removed)))
    w('=' * 100)
    w('All other entries are byte-identical (compared compressed, in place or moved).')
    for k in changed: w('  changed %016x  %d -> %d bytes' % (k, M0[k][4], M1[k][4]))
    for k in added: w('  added   %016x  %d bytes' % (k, M1[k][4]))
    # sprite names we can resolve: every string in the changed/added entries
    cand = set()
    for k in changed + added:
        t = pak.get(new, k)
        if b'CFF0' in t[:40]:
            try: t = cffload(t)['inst']
            except Exception: pass
        for m in re.finditer(rb'[A-Za-z0-9_]{3,64}', t): cand.add(m.group().decode())
    cand |= set(EXTRA_SPRITE_NAMES)
    sprite_name = {lookup2(c.lower().encode(), 0x12345678): c for c in cand}
    for k in changed + added:
        a = pak.get(orig, k) if k in M0 else None; b = pak.get(new, k)
        w(); w('#' * 100); w('ENTRY %016x  (%s)' % (k, 'changed' if a is not None else 'new')); w('#' * 100)
        decode_entry(a, b, sprite_name, cffload)

def is_texture(t):
    if len(t) < 0x1c: return False
    sz, mips, one, fmt, wd, ht = struct.unpack_from('<6I', t, 0)
    return sz == len(t) and one == 1 and fmt in (2, 4, 17, 18, 20) and 0 < wd <= 8192

def decode_entry(a, b, sprite_name, cffload):
    raw = b[32:] if b[:4] == b'RSC0' else b
    if raw[:4] == b'CFF0':
        from cff import parse as cffparse
        if any(t == b'DEF0' for t, _ in cffparse(b)[2]): return decode_cff(a, b, cffload)
        return decode_material(a, b, cffparse)
    if b[:4] == b'RSC0' and b[0x26:0x27] == b'/':
        e = b.find(b'\0', 0x26)
        w('RSC0 model (mesh) resource, %d bytes. Material path stored in it: %r' % (len(b), b[0x26:e].decode()))
        w('The game finds the material by key = lookup8(MD5(that path without the leading /).upper()). See docs/FORMATS.md.')
        if a is None: w('New entry. Every byte other than that path is a copy of an existing game mesh (see build_cape.py).')
        return
    if is_texture(b): return decode_tex(a, b, sprite_name)
    if b[:1] == b'{':
        try: return decode_json(a, b)
        except ValueError: pass
    if b[:5] == b'UIML!':
        try: return decode_uiml(a, b)
        except Exception as ex: w('UIML layout (could not parse: %s); showing bytes.' % ex)
    # generic: changed ranges
    if a is None:
        w('New data, %d bytes. Readable strings:' % len(b))
        for m in re.finditer(rb'[\x20-\x7e]{6,}', b): w('    %#x %r' % (m.start(), m.group().decode()))
        return
    L = max(len(a), len(b)); A = a.ljust(L, b'\0'); B = b.ljust(L, b'\0')
    i = 0; spans = []
    while i < L:
        if A[i] != B[i]:
            j = i
            while j < L and (A[j] != B[j] or any(A[x] != B[x] for x in range(j, min(L, j + 16)))): j += 1
            spans.append((i, j)); i = j
        else: i += 1
    w('%d changed span(s). Size %d -> %d.' % (len(spans), len(a), len(b)))
    for s, e in spans:
        w(); w('  span %#x..%#x' % (s, e))
        w('  old:'); hexrows(a[max(0, s - 16):e + 16][:1024], max(0, s - 16))
        w('  new:'); hexrows(b[max(0, s - 16):e + 16][:1024], max(0, s - 16))
        for m in re.finditer(rb'[\x20-\x7e]{4,}', b[s:e]): w('    new string %#x %r' % (s + m.start(), m.group().decode()))

def decode_material(a, b, cffparse):
    wrap, hdr, ch = cffparse(b)
    w('CFF0 material ("shadergraph") record, not encrypted. Chunks: %s' % ', '.join(t.decode('latin1') for t, _ in ch))
    gb = re.findall(rb'[0-9A-F]{32}', b)
    w('Texture GUIDs it uses (key = lookup8(GUID)):')
    for g in sorted(set(gb)): w('  %s  x%d' % (g.decode(), gb.count(g)))
    if a is not None and len(a) == len(b):
        w('Bytes changed vs original: %d' % sum(1 for i in range(len(a)) if a[i] != b[i]))

def decode_cff(a, b, cffload):
    rb = cffload(b); ra = cffload(a) if a is not None else None
    Ib = rb['inst']; Pb = dict(rb['ptrs'])
    w('CFF0 game-data record (decrypted with key index %d). Data %d bytes, %d pointers, %d symbols.' % (rb['key'], len(Ib), len(Pb), len(rb['syms'])))
    if ra is not None:
        Ia = ra['inst']; Pa = dict(ra['ptrs'])
        n = len(Ia)
        diff = [i for i in range(min(n, len(Ib))) if Ia[i] != Ib[i]]
        w('Original record: %d bytes, %d pointers, %d symbols.' % (n, len(Pa), len(ra['syms'])))
        w('Bytes changed inside the original part: %d. Original pointers changed: %d. Added after the original part: %d bytes.'
          % (len(diff), sum(1 for k, v in Pa.items() if Pb.get(k) != v), max(0, len(Ib) - n)))
        if diff:
            osyms = sorted(ra['syms'])
            def owner(off):
                best = None
                for so, th, nm in osyms:
                    if so <= off: best = (nm, off - so)
                return best
            groups = ranges_merged([(d, b'x', b'x') for d in diff], gap=8)
            w(); w('Changes inside the original part:')
            for s, e in groups:
                ow = owner(s)
                w('  %#x..%#x  (in %s +%#x)' % (s, e, ow[0], ow[1]) if ow else '  %#x..%#x' % (s, e))
                w('     old: %s' % Ia[s:e].hex(' ')); w('     new: %s' % Ib[s:e].hex(' '))
        changed_ptrs = [(k, Pa.get(k), v) for k, v in sorted(Pb.items()) if k < n and Pa.get(k) != v]
        if changed_ptrs:
            w(); w('Pointers inside the original part that now point somewhere else:')
            for k, o_, v in changed_ptrs:
                w('  slot %#x: %s -> %#x %s' % (k, ('%#x' % o_) if o_ is not None else 'none', v, repr(cstr_at(Ib, v) or '')))
        start = n
    else:
        start = 0
    syms = sorted(rb['syms']); newsyms = [s for s in syms if s[0] >= start or (ra is not None and s[2] not in {x[2] for x in ra['syms']})]
    w(); w('New symbols (%d):' % len(newsyms))
    for so, th, nm in newsyms: w('  %#08x  type %#010x  %s' % (so, th, nm))
    if len(Ib) > start:
        w(); w('Added data, every 8-byte field (pointers resolved; strings shown once at their own address):')
        symat = {so: nm for so, th, nm in syms}
        strings = set(v for v in Pb.values())
        o = start
        while o < len(Ib):
            if o in symat: w(); w('  ---- %s ----' % symat[o])
            s = cstr_at(Ib, o)
            if s is not None and o in strings:
                w('  %#08x  string %r' % (o, s)); o = (o + len(s) + 1 + 7) & ~7; continue
            q = Ib[o:o + 8]
            if o in Pb:
                t = Pb[o]; ts = cstr_at(Ib, t)
                w('  %#08x  -> %#x %s' % (o, t, repr(ts) if ts is not None else ('(%s)' % symat[t] if t in symat else '')))
            elif q != b'\0' * 8:
                u = struct.unpack('<2I', q.ljust(8, b'\0')); f = struct.unpack('<2f', q.ljust(8, b'\0'))
                ff = ', '.join('%g' % x for x in f if x == x and 1e-6 < abs(x) < 1e7)
                w('  %#08x  %s   u32 %#x %#x%s' % (o, q.hex(' '), u[0], u[1], ('   f32 ' + ff) if ff else ''))
            o += 8

def decode_tex(a, b, sprite_name):
    def info(t):
        sz, mips, one, fmt, wd, ht, ns = struct.unpack_from('<7I', t, 0)
        sp = [struct.unpack_from('<I4H', t, 0x1c + 12 * i) for i in range(ns)]
        return dict(fmt={2: 'BC1', 4: 'BC3'}.get(fmt, fmt), w=wd, h=ht, mips=mips, sprites=sp)
    ib = info(b); ia = info(a) if a is not None else None
    w('Texture %s %dx%d, %d mips, %d sprites.' % (ib['fmt'], ib['w'], ib['h'], ib['mips'], len(ib['sprites'])))
    if ia: w('Was %s %dx%d, %d mips, %d sprites.' % (ia['fmt'], ia['w'], ia['h'], ia['mips'], len(ia['sprites'])))
    old = {s[0]: s[1:] for s in (ia['sprites'] if ia else [])}
    w('Sprites (hash, x, y, w, h, name if known):')
    for h, x, y, ww, hh in ib['sprites']:
        tag = 'new ' if h not in old else ('moved' if old[h] != (x, y, ww, hh) else '     ')
        w('  %s %#010x  %5d %5d %5d %5d  %s' % (tag, h, x, y, ww, hh, sprite_name.get(h, '')))
    if ia is not None and ia['w'] == ib['w'] and ia['h'] == ib['h']:
        n = sum(1 for i in range(len(a)) if a[i] != b[i]) if len(a) == len(b) else None
        if n is not None: w('Pixel bytes changed: %d of %d.' % (n, len(b)))
    w('Pixels are recoloured / resized copies of game art (see docs/HISTORY.md). Use --png to export before/after images.')
    if PNG_DIR: export_png(a, b)

def export_png(a, b):
    try:
        import texture2ddecoder
        from PIL import Image
    except ImportError: w('(--png needs texture2ddecoder and pillow)'); return
    def img(t):
        sz, mips, one, fmt, wd, ht = struct.unpack_from('<6I', t, 0)
        bs = 16 if fmt == 4 else 8
        tot = sum(max(1, (wd >> m) // 4) * max(1, (ht >> m) // 4) * bs for m in range(mips))
        d = t[len(t) - tot:]
        px = texture2ddecoder.decode_bc3(d, wd, ht) if fmt == 4 else texture2ddecoder.decode_bc1(d, wd, ht)
        return Image.frombytes('RGBA', (wd, ht), px, 'raw', 'BGRA').transpose(Image.FLIP_TOP_BOTTOM)
    os.makedirs(PNG_DIR, exist_ok=True)
    tag = hashlib.sha1(b).hexdigest()[:8]
    img(b).save(os.path.join(PNG_DIR, 'tex_%s_new.png' % tag))
    if a is not None: img(a).save(os.path.join(PNG_DIR, 'tex_%s_old.png' % tag))
    w('PNG written to %s (tex_%s_*.png)' % (PNG_DIR, tag))

def uiml_parse(d):
    """UIML: 'UIML!', u32 BE id, u8 index width, count, count x u32 name hashes, then the root element.
    Element: u8 type, u8 len + name, u8 attr count + (u8 attr id, u8 len, text)..., u8 prop count +
    (u8 prop id, element)..., u16 BE child count, children."""
    assert d[:5] == b'UIML!' and d[9] == 1
    cnt = d[10]; o = 11 + 4 * cnt
    def el(o):
        t = d[o]; o += 1; nl = d[o]; nm = d[o + 1:o + 1 + nl].decode('latin1'); o += 1 + nl
        at = []
        for _ in range(d[o - 0] if False else 0): pass
        ac = d[o]; o += 1
        for _ in range(ac):
            i, l = d[o], d[o + 1]; at.append((i, d[o + 2:o + 2 + l].decode('latin1'))); o += 2 + l
        pc = d[o]; o += 1; props = []
        for _ in range(pc):
            i = d[o]; o += 1; e, o = el(o); props.append((i, e))
        nc = (d[o] << 8) | d[o + 1]; o += 2; kids = []
        for _ in range(nc):
            e, o = el(o); kids.append(e)
        return dict(type=t, name=nm, attrs=at, props=props, kids=kids), o
    root, end = el(o)
    assert end == len(d), 'parse ended at %#x of %#x' % (end, len(d))
    return root

def uiml_lines(e, depth=0, out=None):
    out = [] if out is None else out
    out.append('%s<%#04x %s> %s' % ('  ' * depth, e['type'], e['name'] or '', ' '.join('%d=%r' % a for a in e['attrs'])))
    for i, p in e['props']:
        out.append('%s  [prop %d]' % ('  ' * depth, i)); uiml_lines(p, depth + 2, out)
    for k in e['kids']: uiml_lines(k, depth + 1, out)
    return out

def decode_uiml(a, b):
    import difflib
    nb = uiml_lines(uiml_parse(b))
    w('UIML layout (binary UI markup), parsed as a tree: %d elements.' % len(nb))
    if a is None:
        for l in nb: w('  ' + l)
        return
    na = uiml_lines(uiml_parse(a))
    w('Before: %d elements. Lines starting with + were added, - removed (unified diff of the element tree):' % len(na))
    for l in difflib.unified_diff(na, nb, 'original', 'patched', n=2, lineterm=''): w('  ' + l)

def decode_json(a, b):
    jb = json.loads(b); ja = json.loads(a) if a is not None else {}
    w('JSON document (the voice-line / banter database: criteria, responses, rules).')
    for sec in jb:
        if not isinstance(jb[sec], dict): continue
        A = ja.get(sec, {}); B = jb[sec]
        add = [k for k in B if k not in A]; chg = [k for k in B if k in A and A[k] != B[k]]; rem = [k for k in A if k not in B]
        w(); w('[%s] %d -> %d entries: %d added, %d changed, %d removed' % (sec, len(A), len(B), len(add), len(chg), len(rem)))
        for k in chg:
            w('  CHANGED %s' % k); w('     old: %s' % json.dumps(A[k], sort_keys=True)); w('     new: %s' % json.dumps(B[k], sort_keys=True))
        for k in add: w('  ADDED %s: %s' % (k, json.dumps(B[k], sort_keys=True)))
        for k in rem: w('  REMOVED %s' % k)

# =========================================================================================== main
PNG_DIR = None
# sprite names used only by the mod's exe code (the HUD tool icon), so they're not in any record
EXTRA_SPRITE_NAMES = ['shredder_0', 'karai_0', 'shredder_smoke_hud', 'karai_kunai_hud', 'shredder_dash_hud', 'karai_dash_hud', 'karai_special_hud', 'shredder_special_hud']
def main(orig_path, patch_path, report=None):
    orig = open(orig_path, 'rb').read()
    o_sz, n_sz, R = kpatch.parse(patch_path)
    if len(orig) != o_sz: sys.exit('This patch was made from a %d-byte file, but %s is %d bytes. Use the original game file.' % (o_sz, orig_path, len(orig)))
    for off, new, old in R:
        cur = orig[off:off + len(old)].ljust(len(old), b'\0')
        if cur != old: sys.exit('The original file does not match the patch at offset %#x. Use the unmodded game file.' % off)
    new = kpatch.apply(orig, patch_path)
    w('Patch:    %s' % os.path.basename(patch_path))
    w('Applied to: %s  (SHA-1 %s, %d bytes)' % (os.path.basename(orig_path), hashlib.sha1(orig).hexdigest().upper(), len(orig)))
    w('Result:   SHA-1 %s, %d bytes' % (hashlib.sha1(new).hexdigest().upper(), len(new)))
    w('Ranges in patch: %d, bytes written: %d' % (len(R), sum(len(r[1]) for r in R)))
    w()
    if orig[:2] == b'MZ': decode_exe(orig, new, R)
    elif orig[:4] == b'PAK2': decode_pak(orig, new, R, os.path.basename(orig_path))
    else: w('Unknown file type.')
    txt = out.getvalue()
    if report: open(report, 'w', encoding='utf-8').write(txt); print('wrote', report, len(txt.splitlines()), 'lines')
    else: sys.stdout.write(txt)

if __name__ == '__main__':
    args = [x for x in sys.argv[1:] if not x.startswith('--png')]
    for x in sys.argv[1:]:
        if x.startswith('--png'): PNG_DIR = x.split('=', 1)[1] if '=' in x else 'png'
    if len(args) not in (2, 3): print(__doc__); sys.exit(1)
    main(*args)
