"""Readable patch source for the exe: write it from a patched exe, and assemble it back.

File format (one statement per line, ';' starts a comment):
  size <n>                 final file size in bytes
  file <offset> <hex>      raw bytes at a file offset (PE header fields, section table)
  org <va>                 following lines are placed at this virtual address
      <instruction>        x86-64 assembly (Intel syntax, as capstone prints it); assembled with keystone
      .bytes <hex>         raw bytes (data, or an instruction whose exact encoding keystone would pick
                           differently; the comment then shows the instruction)
"""
import os, sys, re, struct
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(HERE))

def _secs(data):
    import pefile
    p = pefile.PE(data=bytes(data), fast_load=True)
    return p.OPTIONAL_HEADER.ImageBase, [(s.VirtualAddress, max(s.Misc_VirtualSize, s.SizeOfRawData), s.PointerToRawData, s.SizeOfRawData) for s in p.sections]

def _va2off(IB, S, va):
    r = va - IB
    for sva, vs, ro, rs in S:
        if sva <= r < sva + vs and r - sva < rs: return ro + r - sva
    raise ValueError('VA %#x is not backed by file data' % va)

def write_source(orig, new, R, path, title):
    """Emit the source file for patch R (orig -> new)."""
    import decode_patch as D
    from keystone import Ks, KS_ARCH_X86, KS_MODE_64
    ks = Ks(KS_ARCH_X86, KS_MODE_64)
    info = {}
    D.decode_exe(orig, new, R, collect=info)
    IB, SN = info['IB'], info['SN']
    md = info['md']
    lines = ['; %s' % title,
             '; Generated from the released patch by gen_source.py, then checked: build.py assembles this file',
             '; back onto the original TMNTSF.exe and must reproduce the released exe byte for byte.',
             '', 'size %d' % len(new), '']
    def asm_ok(ins):
        txt = '%s %s' % (ins.mnemonic, ins.op_str)
        try:
            enc, _ = ks.asm(txt, ins.address); return bytes(enc) == bytes(ins.bytes)
        except Exception: return False
    S2_ = [(x[1], max(x[2], x[4]), x[3], x[4]) for x in SN]
    def note(ins):
        m = re.search(r'\[rip ([+-]) (0x[0-9a-f]+)\]', ins.op_str); t = None
        if m: t = ins.address + ins.size + int(m.group(2), 16) * (1 if m.group(1) == '+' else -1)
        elif ins.mnemonic.startswith('j') or ins.mnemonic == 'call':
            try: t = int(ins.op_str, 16)
            except ValueError: t = None
        if t is None: return ''
        if t in D.KNOWN: return '  -> %#x %s' % (t, D.KNOWN[t])
        try:
            o = _va2off(IB, S2_, t); st = D.cstr_at(new, o)
            if st and len(st) >= 3: return '  -> %#x %r' % (t, st)
        except ValueError: pass
        return '  -> %#x' % t if m else ''
    def emit_ins(ins):
        txt = ('%s %s' % (ins.mnemonic, ins.op_str)).strip()
        if asm_ok(ins): lines.append('    %-60s ; %x%s' % (txt, ins.address, note(ins)))
        else: lines.append('    .bytes %-52s ; %x  %s  (exact original encoding)%s' % (bytes(ins.bytes).hex(), ins.address, txt, note(ins)))
    def emit_data(va, blob):
        for i in range(0, len(blob), 16):
            ch = blob[i:i + 16]; asc = ''.join(chr(c) if 32 <= c < 127 else '.' for c in ch)
            lines.append('    .bytes %-52s ; %x  %s' % (ch.hex(), va + i, asc))
    # 1. bytes outside code: headers, section table, other sections
    lines.append('; ---- PE header, section table and other non-code bytes')
    for a, b in info['other']:
        lines.append('file %#x %s' % (a, new[a:b].hex()))
    # 2. changed sites in the original code: whole instructions covering each changed range
    lines.append(''); lines.append('; ---- changed instructions inside the original game code')
    for va, end, off in info['sites']:
        s0 = info['aligned_start'](va)
        ins_list = []
        for ins in md.disasm(bytes(new[_va2off(IB, [(x[1], max(x[2], x[4]), x[3], x[4]) for x in SN], s0):][:end - s0 + 32]), s0):
            if ins.address >= end: break
            ins_list.append(ins)
        if not ins_list or ins_list[-1].address + ins_list[-1].size < end:
            raise SystemExit('could not cover site %#x' % va)
        lines.append(''); lines.append('org %#x' % ins_list[0].address)
        for ins in ins_list: emit_ins(ins)
    # 3. caves: code where the analysis found code, data elsewhere
    code = info['code']
    S2 = [(x[1], max(x[2], x[4]), x[3], x[4]) for x in SN]
    lines.append(''); lines.append('; ---- new code and data (caves)')
    for a, b in info['cave_spans']:
        lines.append(''); lines.append('org %#x' % a)
        va = a
        while va < b:
            if va in code:
                ins = code[va]
                if va in info['labels']: lines.append('  ; %s' % info['labels'][va])
                emit_ins(ins); va += ins.size
            else:
                st = va
                while va < b and va not in code: va += 1
                o = _va2off(IB, S2, st); emit_data(st, new[o:o + (va - st)])
    open(path, 'w').write('\n'.join(lines) + '\n')
    return path

def assemble(orig, path):
    """Apply a source file to the original exe bytes; returns the patched exe."""
    from keystone import Ks, KS_ARCH_X86, KS_MODE_64
    ks = Ks(KS_ARCH_X86, KS_MODE_64)
    d = bytearray(orig); va = None; layout = None; n_ins = 0; n_raw = 0
    for ln, raw in enumerate(open(path), 1):
        line = raw.split(';', 1)[0].strip()
        if not line: continue
        try:
            if line.startswith('size '):
                n = int(line.split()[1])
                if n < len(d): del d[n:]
                else: d.extend(b'\0' * (n - len(d)))
            elif line.startswith('file '):
                _, off, hx = line.split(); off = int(off, 16); b = bytes.fromhex(hx)
                if off + len(b) > len(d): d.extend(b'\0' * (off + len(b) - len(d)))
                d[off:off + len(b)] = b; layout = None
            elif line.startswith('org '):
                va = int(line.split()[1], 16)
                if layout is None: layout = _secs(d)
            elif line.startswith('.bytes '):
                b = bytes.fromhex(line.split()[1]); o = _va2off(*layout, va); d[o:o + len(b)] = b; va += len(b); n_raw += 1
            else:
                enc, _ = ks.asm(line, va); b = bytes(enc); o = _va2off(*layout, va); d[o:o + len(b)] = b; va += len(b); n_ins += 1
        except Exception as ex:
            raise SystemExit('%s line %d: %s  (%s)' % (path, ln, raw.rstrip(), ex))
    return bytes(d), n_ins, n_raw
