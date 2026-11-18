# Step 3x (exe, on top of L26 exe): give hero Karai's Cleave real hero special damage, like Raph/Mikey/Donnie.
# Only while HFLAG is set (i.e. when building "Karai_HeroCleave"; the boss's "Karai_Cleave" never sets it):
#  * damage block (builder rbp+0x370): damage := fn 0x1406adf48 (hero stat 0x1a = special damage, as Raph/Mikey/Don),
#    enemy difficulty multiplier (rbp+0x380, fn 0x1406ae34c) cleared, category flags 0x2000 -> 0x2004 (Raph's value)
#  * slash effect damage (rbp+0x880): := fn 0x14088ba70 (hero stat 0x1d, as Raph's special effect / Leo's special),
#    enemy multiplier (rbp+0x890, fn 0x1406ae28c) cleared
#  * the step-3v/3w xmm7 multiplier goes back to 1.0 (that value was not the damage)
import sys, struct, pefile, capstone
src, dst = sys.argv[1], sys.argv[2]
d = bytearray(open(src, 'rb').read())
pe = pefile.PE(data=bytes(d), fast_load=True); IB = pe.OPTIONAL_HEADER.ImageBase
md = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_64)
def off(va):
    r = va - IB
    for s in pe.sections:
        if s.VirtualAddress <= r < s.VirtualAddress + max(s.Misc_VirtualSize, s.SizeOfRawData):
            return s.PointerToRawData + r - s.VirtualAddress
    raise ValueError(hex(va))
def get(va, n): return bytes(d[off(va):off(va)+n])
def put(va, b): d[off(va):off(va)+len(b)] = b
def rel(end, target): return struct.pack('<i', target - end)

HFLAG = 0x14186f900; MULT = 0x14186f910
CAVE_A = 0x14186fa40; CAVE_B = 0x14186fa80; END = 0x14186fb00
HERO_SPECIAL_DMG = 0x1406adf48; HERO_SPECIAL_FX_DMG = 0x14088ba70
SITE_A = 0x1409fd6a1; BACK_A = 0x1409fd6ac
SITE_B = 0x1409fd919; BACK_B = 0x1409fd920; ONMELEE = 0x1411c1628

# --- sanity: step-3v/3w pieces present, target bytes as expected, cave area empty ---
assert get(0x1409fd309, 5)[0] == 0xe9 and get(0x14186f920, 16) == b'Karai_HeroCleave'
assert struct.unpack('<f', get(MULT, 4))[0] in (3.0, 60.0)
assert get(SITE_A, 11) == bytes.fromhex('48c785c003000000200000')
assert get(SITE_B, 3) == bytes.fromhex('488d0d') and SITE_B + 7 + struct.unpack('<i', get(SITE_B + 3, 4))[0] == ONMELEE
assert get(ONMELEE, 13) == b'OnMeleeAction'
for f, stat in ((HERO_SPECIAL_DMG, 0x1a), (HERO_SPECIAL_FX_DMG, 0x1d)):
    ins = list(md.disasm(get(f, 0x20), f)); assert any(i.mnemonic == 'mov' and i.op_str == 'dl, 0x%x' % stat for i in ins), hex(f)
assert all(b == 0 for b in get(CAVE_A, END - CAVE_A))

put(MULT, struct.pack('<f', 1.0))

# cave A: original flags store, then hero-only damage block rewrite
c = bytearray(bytes.fromhex('48c785c003000000200000'))          # mov qword [rbp+0x3c0],0x2000
c += b'\x80\x3d' + rel(CAVE_A + len(c) + 7, HFLAG) + b'\x00'    # cmp byte [HFLAG],0
j = len(c); c += b'\x74\x00'                                     # je done
c += b'\x48\x8d\x05' + rel(CAVE_A + len(c) + 7, HERO_SPECIAL_DMG)  # lea rax,[special dmg fn]
c += bytes.fromhex('48898570030000')                             # mov [rbp+0x370],rax
c += bytes.fromhex('c6857803000004')                             # mov byte [rbp+0x378],4
c += bytes.fromhex('c6858803000000')                             # mov byte [rbp+0x388],0
c += bytes.fromhex('48c785c003000004200000')                     # mov qword [rbp+0x3c0],0x2004
c[j + 1] = len(c) - (j + 2)
c += b'\xe9' + rel(CAVE_A + len(c) + 5, BACK_A)
assert CAVE_A + len(c) <= CAVE_B; put(CAVE_A, c)
put(SITE_A, b'\xe9' + rel(SITE_A + 5, CAVE_A) + b'\x90' * 6)

# cave B: hero-only slash-effect damage rewrite, then the original lea rcx,"OnMeleeAction"
c = bytearray(b'\x80\x3d' + rel(CAVE_B + 7, HFLAG) + b'\x00')
j = len(c); c += b'\x74\x00'
c += b'\x48\x8d\x05' + rel(CAVE_B + len(c) + 7, HERO_SPECIAL_FX_DMG)
c += bytes.fromhex('48898580080000')                             # mov [rbp+0x880],rax
c += bytes.fromhex('c6858808000004')                             # mov byte [rbp+0x888],4
c += bytes.fromhex('c6859808000000')                             # mov byte [rbp+0x898],0
c[j + 1] = len(c) - (j + 2)
c += b'\x48\x8d\x0d' + rel(CAVE_B + len(c) + 7, ONMELEE)        # lea rcx,[OnMeleeAction]
c += b'\xe9' + rel(CAVE_B + len(c) + 5, BACK_B)
assert CAVE_B + len(c) <= END; put(CAVE_B, c)
put(SITE_B, b'\xe9' + rel(SITE_B + 5, CAVE_B) + b'\x90\x90')

pe2 = pefile.PE(data=bytes(d)); oh = pe.OPTIONAL_HEADER.get_file_offset()
struct.pack_into('<I', d, oh + 64, pe2.generate_checksum())
open(dst, 'wb').write(d); print('ok')
