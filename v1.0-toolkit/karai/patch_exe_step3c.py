# Step 3b: Karai-only combo sounds/effects/grunts. Applied on top of the step-3a exe.
# Adds a new RWX section ".karai" holding: a "building Karai" flag, stub factories, new registry nodes,
# Karai string table, and per-site caves that swap Casey strings for Karai strings while the flag is set.
import sys, struct, pefile, capstone, keystone
src, dst = sys.argv[1], sys.argv[2]
d = bytearray(open(src, 'rb').read())
pe = pefile.PE(data=bytes(d), fast_load=True); IB = pe.OPTIONAL_HEADER.ImageBase
md = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_64); md.detail = True
ks = keystone.Ks(keystone.KS_ARCH_X86, keystone.KS_MODE_64)
def off(va):
    r = va - IB
    for s in pe.sections:
        if s.VirtualAddress <= r < s.VirtualAddress + max(s.Misc_VirtualSize, s.SizeOfRawData):
            return s.PointerToRawData + r - s.VirtualAddress
    raise ValueError(hex(va))
def ins_at(va): o = off(va); return next(md.disasm(bytes(d[o:o+16]), va))
def asm(code, va): enc, _ = ks.asm(code, va); return bytes(enc)
def cstr_at(va): o = off(va); return bytes(d[o:d.index(b'\0', o)]).decode()

# ---------- new section ----------
assert pe.FILE_HEADER.NumberOfSections == 8
SEC_VA = IB + pe.OPTIONAL_HEADER.SizeOfImage            # 0x14186e000
SEC_SIZE = 0x2000
sec = bytearray(SEC_SIZE)
cur = [0]
def place(b, align=16):
    cur[0] = (cur[0] + align - 1) & ~(align - 1); a = cur[0]; sec[a:a+len(b)] = b; cur[0] += len(b); return SEC_VA + a
FLAG = place(b'\0' * 16)
HEAD = 0x1415f6b90                                     # behaviour-registry list head
# Karai replacement strings
KS = {
 'name1': 'CKarai_Attack_Chain1', 'name2': 'CKarai_Attack_Chain2', 'name3': 'CKarai_Attack_Chain3', 'nameD': 'CKarai_DashAttack',
 'hover': 'event:/VO/BOSSES/KARAI/BANTER_KAR_GLOBAL_DASHPREP_001',
 'pfx1': 'build://Effects/Characters/Turtles/Leonardo/BasicAttacks/Leonardo_Attack_01/Leonardo_Attack_01.pfx',
 'pfx2': 'build://Effects/Characters/Turtles/Leonardo/BasicAttacks/Leonardo_Attack_02/Leonardo_Attack_02.pfx',
 'pfx3': 'build://Effects/Characters/Turtles/Leonardo/BasicAttacks/Leonardo_Attack_03/Leonardo_Attack_03.pfx',
 'pfx4': 'build://Effects/Characters/Enemies/Karai/Karai_Dash_Slash/Karai_Dash_Slash.pfx',
 'light': 'event:/Combat/BOSSES/Karai/Combat_Karai_Attack_Light',
 'heavy': 'event:/Combat/BOSSES/Karai/Combat_Karai_Attack_Heavy_01',
 'leap': 'event:/Combat/BOSSES/Karai/Combat_Karai_Dash_Prep_01',
 'hurt': 'event:/Combat/BOSSES/Karai/Exertions_Karai_DamageTaken',
}
KSVA = {k: place(v.encode() + b'\0', 8) for k, v in KS.items()}
# swap sites: (va, expected casey string, karai key)
SITES = [
 (0x140b368dd, 'CaseyJones_Attack_Chain1', 'name1'), (0x140b36933, 'CaseyJones_Attack_Chain2', 'name2'),
 (0x140b36982, 'CaseyJones_Attack_Chain3', 'name3'), (0x140b369d1, 'CaseyJones_DashAttack', 'nameD'),
 (0x140b3710b, 'CaseyJones_Attack_01.pfx', 'pfx1'), (0x140b37d58, 'CaseyJones_Attack_02.pfx', 'pfx2'),
 (0x140b38a88, 'CaseyJones_Attack_03.pfx', 'pfx3'), (0x140b39a8a, 'CaseyJones_Attack_04.pfx', 'pfx4'),
 (0x140b371be, 'Abi_Plr_CJ_Basic_Attack_Light_Play', 'light'), (0x140b37e0c, 'Abi_Plr_CJ_Basic_Attack_Light_Play', 'light'),
 (0x140b398de, 'Abi_Plr_CJ_Basic_Attack_Light_Play', 'light'), (0x140b388df, 'Abi_Plr_CJ_Basic_Attack_Heavy_Impact_Play', 'heavy'),
 (0x140b38b39, 'Abi_Plr_CJ_Basic_Attack_Heavy_Leap_Play', 'leap'),
 (0x140a05bb8, 'Exertion_Casey_Stunned', 'hurt'), (0x140a06994, 'Exertion_Casey_Damage_Taken', 'hurt'),
]
log = []
for va, want, key in SITES:
    i = ins_at(va)
    assert i.mnemonic == 'lea' and i.size == 7 and 'rip' in i.op_str, (hex(va), i.op_str)
    reg = i.op_str.split(',')[0]
    tgt = va + 7 + struct.unpack_from('<i', d, off(va) + 3)[0]
    assert cstr_at(tgt).endswith(want), (hex(va), cstr_at(tgt), want)
    cave_va = SEC_VA + ((cur[0] + 15) & ~15)
    c = bytearray(b'\x9c')                                          # pushfq
    c += bytes(d[off(va):off(va)+3]); c += b'\0\0\0\0'; lea1 = len(c) - 4   # lea reg,[rip+casey]
    c += b'\x80\x3d' + b'\0\0\0\0' + b'\x00'; cmpd = len(c) - 5           # cmp byte [rip+FLAG],0
    c += b'\x74\x07'                                                 # je +7 (skip next lea)
    c += bytes(d[off(va):off(va)+3]); c += b'\0\0\0\0'; lea2 = len(c) - 4   # lea reg,[rip+karai]
    c += b'\x9d'                                                     # popfq
    c += b'\xe9\0\0\0\0'; jmpd = len(c) - 4                          # jmp back
    a = place(bytes(c))
    struct.pack_into('<i', sec, a - SEC_VA + lea1, tgt - (a + lea1 + 4))
    struct.pack_into('<i', sec, a - SEC_VA + cmpd, FLAG - (a + cmpd + 5))
    struct.pack_into('<i', sec, a - SEC_VA + lea2, KSVA[key] - (a + lea2 + 4))
    struct.pack_into('<i', sec, a - SEC_VA + jmpd, (va + 7) - (a + jmpd + 4))
    o = off(va); d[o:o+7] = b'\xe9' + struct.pack('<i', a - (va + 5)) + b'\x90\x90'
    log.append('hook %x %s -> %s' % (va, want, KS[key][-45:]))

# ---------- stub factories + registry nodes ----------
NEW = [('CKarai_Attack_Chain', 0x140b36894), ('CKarai_Attack_Chain1', 0x140b36a54), ('CKarai_Attack_Chain2', 0x140b376fc),
       ('CKarai_Attack_Chain3', 0x140b38338), ('CKarai_DashAttack', 0x140b39280),
       ('Karai_Hit_Reaction', 0x140a06590), ('Karai_Stun', 0x140a057b4)]
nodes = []
for name, fac in NEW:
    nva = place(name.encode() + b'\0', 8)
    s = SEC_VA + ((cur[0] + 15) & ~15)
    c = bytearray(b'\x48\x83\xec\x28')                               # sub rsp,0x28
    c += b'\xc6\x05' + b'\0\0\0\0' + b'\x01'; f1 = len(c) - 5          # mov byte [rip+FLAG],1
    c += b'\xe8\0\0\0\0'; cl = len(c) - 4                            # call factory
    c += b'\xc6\x05' + b'\0\0\0\0' + b'\x00'; f2 = len(c) - 5          # mov byte [rip+FLAG],0
    c += b'\x48\x83\xc4\x28\xc3'                                     # add rsp,0x28; ret
    a = place(bytes(c))
    struct.pack_into('<i', sec, a - SEC_VA + f1, FLAG - (a + f1 + 5))
    struct.pack_into('<i', sec, a - SEC_VA + cl, fac - (a + cl + 4))
    struct.pack_into('<i', sec, a - SEC_VA + f2, FLAG - (a + f2 + 5))
    node = place(b'\0' * 24, 16)
    nodes.append((node, nva, a))
    log.append('register %s -> stub %x -> %x' % (name, a, fac))
# init routine: push nodes onto the registry list, then continue into the step-2 cave (table copy + atexit)
CAVE1 = 0x140f6ac80
init = SEC_VA + ((cur[0] + 15) & ~15)
c = bytearray()
def rip(instr_len_before_disp, target, here):
    return struct.pack('<i', target - (here + instr_len_before_disp + 4))
for node, nva, stub in nodes:
    for src_va, field in ((nva, 0), (stub, 8)):
        here = init + len(c); c += b'\x48\x8d\x05' + rip(3, src_va, here)          # lea rax,[rip+x]
        here = init + len(c); c += b'\x48\x89\x05' + rip(3, node + field, here)    # mov [rip+node+field],rax
    here = init + len(c); c += b'\x48\x8b\x05' + rip(3, HEAD, here)                # mov rax,[rip+HEAD]
    here = init + len(c); c += b'\x48\x89\x05' + rip(3, node + 16, here)           # mov [rip+node+16],rax
    here = init + len(c); c += b'\x48\x8d\x05' + rip(3, node, here)                # lea rax,[rip+node]
    here = init + len(c); c += b'\x48\x89\x05' + rip(3, HEAD, here)                # mov [rip+HEAD],rax
here = init + len(c); c += b'\xe9' + struct.pack('<i', CAVE1 - (here + 5))         # jmp step-2 cave
assert place(bytes(c)) == init
HOOK1 = 0x1400d3a72
i = ins_at(HOOK1); assert i.mnemonic == 'jmp' and int(i.op_str, 16) == CAVE1, i.op_str
o = off(HOOK1); d[o:o+5] = b'\xe9' + struct.pack('<i', init - (HOOK1 + 5))
log.append('init %x (%d nodes), section used 0x%x bytes' % (init, len(nodes), cur[0]))
assert cur[0] <= SEC_SIZE


# ---------- select-screen hover voice for slot 8 (was falling through to Leo) ----------
HV = 0x140655bb1
i1 = ins_at(HV); i2 = ins_at(HV + 3)
assert (i1.mnemonic, i1.op_str) == ('cmp', 'ebx, 1') and i2.mnemonic == 'jne' and int(i2.op_str, 16) == 0x140655ca0, (i1.op_str, i2.op_str)
hv = SEC_VA + ((cur[0] + 15) & ~15)
c = bytearray(b'\x83\xfb\x01')                       # cmp ebx,1
c += b'\x0f\x85\0\0\0\0'; j1 = len(c) - 4             # jne 0x140655ca0 (no sound)
c += b'\x48\x8d\x3d\0\0\0\0'; l1 = len(c) - 4         # lea rdi,[rip+karai hover]
c += b'\xe9\0\0\0\0'; j2 = len(c) - 4                 # jmp 0x140655ca0 (play it)
a = place(bytes(c))
struct.pack_into('<i', sec, a - SEC_VA + j1, 0x140655ca0 - (a + j1 + 4))
struct.pack_into('<i', sec, a - SEC_VA + l1, KSVA['hover'] - (a + l1 + 4))
struct.pack_into('<i', sec, a - SEC_VA + j2, 0x140655ca0 - (a + j2 + 4))
o = off(HV); d[o:o+9] = b'\xe9' + struct.pack('<i', a - (HV + 5)) + b'\x90' * 4
log.append('hover hook %x -> %x' % (HV, a))

# ---------- add the section (drop the now-invalid Authenticode signature overlay) ----------
sd = pe.OPTIONAL_HEADER.DATA_DIRECTORY[4]
raw = sd.VirtualAddress if sd.Size else len(d)
assert raw % 0x200 == 0
d = d[:raw]
hdr_off = pe.sections[-1].get_file_offset() + 0x28
assert all(b == 0 for b in d[hdr_off:hdr_off+0x28])
d[hdr_off:hdr_off+0x28] = struct.pack('<8sIIIIIIHHI', b'.karai\0\0', SEC_SIZE, SEC_VA - IB, SEC_SIZE, raw, 0, 0, 0, 0, 0xE0000020)
d += sec
fh = pe.FILE_HEADER.get_file_offset(); struct.pack_into('<H', d, fh + 2, 9)
oh = pe.OPTIONAL_HEADER.get_file_offset()
struct.pack_into('<I', d, oh + 56, (SEC_VA - IB) + SEC_SIZE)                  # SizeOfImage
dd = oh + 112 + 4 * 8; struct.pack_into('<II', d, dd, 0, 0)                   # security directory -> none
pe2 = pefile.PE(data=bytes(d)); struct.pack_into('<I', d, oh + 64, pe2.generate_checksum())
open(dst, 'wb').write(d)
print('\n'.join(log))
