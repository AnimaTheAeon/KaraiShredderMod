# Step 2: 9th portrait on the select screen. Applied on top of the step-1 exe.
import sys, struct, pefile, capstone
src, dst = sys.argv[1], sys.argv[2]
d = bytearray(open(src, 'rb').read())
pe = pefile.PE(data=bytes(d), fast_load=True); IB = pe.OPTIONAL_HEADER.ImageBase
md = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_64); md.detail = True
def off(va):
    r = va - IB
    for s in pe.sections:
        if s.VirtualAddress <= r < s.VirtualAddress + max(s.Misc_VirtualSize, s.SizeOfRawData):
            return s.PointerToRawData + r - s.VirtualAddress
    raise ValueError(hex(va))
def ins_at(va):
    o = off(va); return next(md.disasm(bytes(d[o:o+16]), va))
def txt(i): return '%s %s' % (i.mnemonic, i.op_str)
log = []

# ---------- A. new homes: table in .data tail, cave in .text tail ----------
secs = {s.Name.rstrip(b'\0'): s for s in pe.sections}
data_s, text_s = secs[b'.data'], secs[b'.text']
assert data_s.Misc_VirtualSize == 0x2b30e0 and text_s.Misc_VirtualSize == 0xf69c7e
OLD_TBL, TBL_SIZE8 = 0x1414cc890, 8 * 0xe0
NEW_TBL = IB + ((data_s.VirtualAddress + data_s.Misc_VirtualSize + 0xf) & ~0xf)      # 0x1416b00e0
assert NEW_TBL + 9 * 0xe0 <= IB + data_s.VirtualAddress + 0x2b4000
CAVE = IB + ((text_s.VirtualAddress + text_s.Misc_VirtualSize + 0xf) & ~0xf)        # 0x140f6ac80
CAVE_END = IB + text_s.VirtualAddress + text_s.SizeOfRawData
assert all(b == 0 for b in d[off(CAVE):off(CAVE_END-1)+1])
# grow section VirtualSizes (header fields) so the new bytes are mapped
def set_vsize(sec, v):
    struct.pack_into('<I', d, sec.get_file_offset() + 8, v)
set_vsize(data_s, 0x2b4000)          # .pdata starts at RVA 0x16b1000 = .data RVA + 0x2b4000
set_vsize(text_s, text_s.SizeOfRawData)
DELTA = NEW_TBL - OLD_TBL

# ---------- B. retarget every rip-relative reference to the old table ----------
import numpy as np
t0 = text_s.PointerToRawData; n = text_s.Misc_VirtualSize; tva = IB + text_s.VirtualAddress
arr = np.frombuffer(bytes(d[t0:t0+n+8]), dtype=np.uint8)
disp = (arr[:-7].astype(np.int64) | (arr[1:-6].astype(np.int64) << 8) | (arr[2:-5].astype(np.int64) << 16) | (arr[3:-4].astype(np.int64) << 24))
disp = np.where(disp >= 2**31, disp - 2**32, disp)
pos = np.arange(len(disp)); fixed = set()
for k in (0, 1, 4):
    tgt = tva + pos + 4 + k + disp
    for i in np.flatnonzero((tgt >= OLD_TBL) & (tgt < OLD_TBL + TBL_SIZE8)):
        end = int(i) + 4 + k
        for L in range(5, 12):
            s = end - L
            ins = list(md.disasm(bytes(d[t0+s:t0+end]), tva + s))
            if len(ins) == 1 and ins[0].size == L and ins[0].disp_offset == L - 4 - k and 'rip' in ins[0].op_str:
                do = t0 + s + ins[0].disp_offset
                if do in fixed: break
                if k and ins[0].imm_offset == 0: break
                t = tva + end + int(disp[i])
                assert OLD_TBL <= t < OLD_TBL + TBL_SIZE8
                struct.pack_into('<i', d, do, int(disp[i]) + DELTA); fixed.add(do)
                break
log.append('table refs retargeted: %d' % len(fixed))

# ---------- C. cave: copy the 9th table entry (7 short SSO strings) at startup ----------
names = ['SP8', 'SP8/Lit', 'SP8/Used', 'SP8/Locked', 'SP8/Image', 'SP8/HeroColor', 'SP8/Glow']
tmpl = b''.join(n.encode().ljust(16, b'\0') + struct.pack('<QQ', len(n), 15) for n in names)
assert len(tmpl) == 0xe0
code = bytearray(); cva = CAVE
def emit(b): code.extend(b)
def rel32(at_va, target): return struct.pack('<i', target - (at_va + 4))
TMPL_VA = CAVE + 0x80
HOOK1 = 0x1400d3a72            # jmp 0x140e1ab5c  (tail of the table's static initializer)
i = ins_at(HOOK1); assert txt(i) == 'jmp 0x140e1ab5c', txt(i)
emit(b'\x56\x57\x51')                                   # push rsi; push rdi; push rcx
emit(b'\x48\x8d\x35'); emit(rel32(cva+len(code), TMPL_VA))        # lea rsi,[rip+tmpl]
emit(b'\x48\x8d\x3d'); emit(rel32(cva+len(code), NEW_TBL + 8*0xe0))  # lea rdi,[rip+tbl8]
emit(b'\xb9' + struct.pack('<I', 0xe0))                 # mov ecx,0xe0
emit(b'\xf3\xa4')                                       # rep movsb
emit(b'\x59\x5f\x5e')                                   # pop rcx; pop rdi; pop rsi
emit(b'\xe9'); emit(rel32(cva+len(code), 0x140e1ab5c))  # jmp atexit
CAVE2 = cva + len(code)
# ---------- D. cave 2: progression-unlock bit for slot 8 ----------
HOOK2 = 0x14064fe17
a = ins_at(HOOK2); b_ = ins_at(HOOK2 + a.size)
assert txt(a) == 'mov al, byte ptr [rbp + 0x30]' and txt(b_) == 'mov byte ptr [rbx + 0x16c], al'
emit(bytes(d[off(HOOK2):off(HOOK2)+a.size+b_.size]))   # original two instructions
emit(b'\xc6\x83\x6d\x01\x00\x00\x01')                   # mov byte [rbx+0x16d],1  (Karai: no progression lock)
emit(b'\xe9'); emit(rel32(cva+len(code), HOOK2 + a.size + b_.size))
assert cva + len(code) <= TMPL_VA
o = off(CAVE); d[o:o+len(code)] = code
o = off(TMPL_VA); d[o:o+len(tmpl)] = tmpl
assert TMPL_VA + len(tmpl) <= CAVE_END
# hooks
o = off(HOOK1); d[o:o+5] = b'\xe9' + rel32(HOOK1+1, CAVE)
o = off(HOOK2); d[o:o+9] = b'\xe9' + rel32(HOOK2+1, CAVE2) + b'\x90'*4
log.append('caves at %x (%d bytes code) + template %x' % (CAVE, len(code), TMPL_VA))

# ---------- E. select-controller fields 0xE0..0x10B move up by 0x18 (room for entry 9) ----------
SHIFT = [0x14064fa4a,0x14064fa51,0x14064fa58,0x14064fa5f,0x14064fa66,0x14064fa6d,0x14064fcf2,0x14064fcfb,
 0x14064fe59,0x14064feeb,0x14064ff48,0x14064ffb7,0x14065000b,0x140650b0d,0x140650b63,0x140650c68,0x140650c75,
 0x140650cf6,0x140650d29,0x140650e98,0x140650eb8,0x14065114c,0x14065115b,0x14065126a,0x140651279,0x1406512ca,
 0x140651302,0x140651399,0x1406513a8,0x140651557,0x1406515a5,0x14065199a,0x140651f94,0x1406520e7,0x14065268c,
 0x1406526c9,0x1406526e5,0x140652993,0x1406529a0,0x140652ced,0x140652d09]
for va in SHIFT:
    i = ins_at(va)
    assert i.disp_offset and 0xe0 <= struct.unpack_from('<i', d, off(va)+i.disp_offset)[0] < 0x10c, (hex(va), txt(i))
    do = off(va) + i.disp_offset
    old = struct.unpack_from('<i', d, do)[0]
    # disp must be a 32-bit field (not followed by the next instruction)
    assert i.disp_offset + 4 <= i.size
    struct.pack_into('<i', d, do, old + 0x18)
    log.append('shift %x  %s -> %s' % (va, txt(i), txt(ins_at(va))))

# ---------- F. loops: 8 heroes -> 9 ----------
LOOPS = {0x14064fe29:'lea edi, [rax + 8]', 0x14065002b:'cmp esi, 8', 0x1406515be:'cmp r14d, 8',
 0x140651aea:'mov ecx, 8', 0x140651b7d:'cmp ecx, 8', 0x1406529d3:'cmp r9d, 8',
 0x140653d53:'cmp r14d, 8', 0x140654920:'cmp ebp, 8', 0x140655915:'cmp r15d, 8'}
for va, want in LOOPS.items():
    i = ins_at(va); assert txt(i) == want, (hex(va), txt(i), want)
    o = off(va)
    if i.imm_offset: d[o + i.imm_offset] = 9
    else: d[o + i.disp_offset] = 9          # lea edi,[rax+8] (disp8)
    log.append('loop %x %s -> %s' % (va, want, txt(ins_at(va))))
open(dst, 'wb').write(d)
print('\n'.join(log))
