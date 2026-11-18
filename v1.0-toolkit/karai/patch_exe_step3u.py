# Step 3u (exe): hero-only Cleave damage boost.
# Registers a new behaviour "Karai_HeroCleave" whose stub factory sets HFLAG, calls the boss Cleave factory
# (0x1409fe5c8), then clears HFLAG. Inside the Cleave builder, the one site that loads the hit damage (4.5)
# for the normal variant multiplies it by MULT only while HFLAG is set. Boss Karai keeps calling
# "Karai_Cleave" (flag clear) -> exactly the original value. Only Karai's hero record is renamed to use the new behaviour.
import sys, struct, pefile, capstone
src, dst, mult = sys.argv[1], sys.argv[2], float(sys.argv[3])
d = bytearray(open(src, 'rb').read())
pe = pefile.PE(data=bytes(d), fast_load=True); IB = pe.OPTIONAL_HEADER.ImageBase
md = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_64)
def off(va):
    r = va - IB
    for s in pe.sections:
        if s.VirtualAddress <= r < s.VirtualAddress + max(s.Misc_VirtualSize, s.SizeOfRawData):
            return s.PointerToRawData + r - s.VirtualAddress
    raise ValueError(hex(va))
def ins_at(va): o = off(va); return next(md.disasm(bytes(d[o:o+16]), va))
def put(va, b): o = off(va); d[o:o+len(b)] = b
def rel(here_end, target): return struct.pack('<i', target - here_end)

BASE = 0x14186f900; END = 0x14186fa80
assert all(b == 0 for b in d[off(0x14186f800):off(0x14186ffff)+1]), 'target area not empty'
HFLAG = BASE            # runtime byte
MULT  = BASE + 0x10     # float
NAME  = BASE + 0x20     # "Karai_HeroCleave"
NODE  = BASE + 0x40     # 24-byte registry node, filled at runtime (no absolute pointers on disk)
STUB  = BASE + 0x60
DCAVE = BASE + 0xa0
INIT  = BASE + 0xe0
HEAD  = 0x1415f6b90; CAVE1 = 0x140f6ac80; FACT = 0x1409fe5c8
SITE  = 0x1409fd309; BACK = 0x1409fd311; DMG = 0x14126e148
INITJ = 0x14186e8b8

# --- sanity checks on the original code ---
i = ins_at(SITE); assert i.mnemonic == 'movss' and i.op_str.startswith('xmm7') and i.size == 8, i.op_str
assert SITE + 8 + struct.unpack_from('<i', d, off(SITE) + 4)[0] == DMG
assert struct.unpack('<f', bytes(d[off(DMG):off(DMG)+4]))[0] == 4.5
assert ins_at(BACK).mnemonic == 'movaps'
i = ins_at(INITJ); assert i.mnemonic == 'jmp' and int(i.op_str, 16) == CAVE1, i.op_str
assert bytes(d[off(FACT):off(FACT)+4]) == bytes.fromhex('4883ec28')

put(MULT, struct.pack('<f', mult))
put(NAME, b'Karai_HeroCleave\0')

# stub factory
c = bytearray(b'\x48\x83\xec\x28')
c += b'\xc6\x05' + rel(STUB + len(c) + 7, HFLAG) + b'\x01'
c += b'\xe8' + rel(STUB + len(c) + 5, FACT)
c += b'\xc6\x05' + rel(STUB + len(c) + 7, HFLAG) + b'\x00'
c += b'\x48\x83\xc4\x28\xc3'
assert len(c) <= DCAVE - STUB; put(STUB, c)

# damage cave: movss xmm7,[4.5]; cmp byte [HFLAG],0; je done; mulss xmm7,[MULT]; done: jmp BACK
c = bytearray(b'\xf3\x0f\x10\x3d' + rel(DCAVE + 8, DMG))
c += b'\x80\x3d' + rel(DCAVE + len(c) + 7, HFLAG) + b'\x00'
c += b'\x74\x08'
c += b'\xf3\x0f\x59\x3d' + rel(DCAVE + len(c) + 8, MULT)
c += b'\xe9' + rel(DCAVE + len(c) + 5, BACK)
assert len(c) <= INIT - DCAVE; put(DCAVE, c)
put(SITE, b'\xe9' + rel(SITE + 5, DCAVE) + b'\x90\x90\x90')

# init: fill node at runtime and push it on the registry list, then continue to the original step-2 cave
c = bytearray()
def emit(op, target): c.extend(op + rel(INIT + len(c) + len(op) + 4, target))
emit(b'\x48\x8d\x05', NAME); emit(b'\x48\x89\x05', NODE)
emit(b'\x48\x8d\x05', STUB); emit(b'\x48\x89\x05', NODE + 8)
emit(b'\x48\x8b\x05', HEAD); emit(b'\x48\x89\x05', NODE + 16)
emit(b'\x48\x8d\x05', NODE); emit(b'\x48\x89\x05', HEAD)
c += b'\xe9' + rel(INIT + len(c) + 5, CAVE1)
assert INIT + len(c) <= END; put(INIT, c)
put(INITJ, b'\xe9' + rel(INITJ + 5, INIT))

pe2 = pefile.PE(data=bytes(d)); oh = pe.OPTIONAL_HEADER.get_file_offset()
struct.pack_into('<I', d, oh + 64, pe2.generate_checksum())
open(dst, 'wb').write(d)
print('ok stub %x dcave %x init %x mult %g' % (STUB, DCAVE, INIT, mult))
