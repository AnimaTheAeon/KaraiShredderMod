# Step 3f: slot 8 (Karai) sets her own banter facts: KaraiVariantId, KaraiVariantIsSkin, KaraiExists, KaraiIsDead, KaraiIsHost.
# Copies Casey's case (0x14072e69d..0x14072e765) of the fact switch into the .karai section with relocated rip/branch targets.
import sys,struct,pefile,capstone
src,dst=sys.argv[1],sys.argv[2]
pe=pefile.PE(src,fast_load=True); IB=pe.OPTIONAL_HEADER.ImageBase; d=bytearray(open(src,'rb').read())
def off(va): return pe.get_offset_from_rva(va-IB)
md=capstone.Cs(capstone.CS_ARCH_X86,capstone.CS_MODE_64); md.detail=True
def fnv(s):
    h=0x811c9dc5
    for c in s.encode(): h=((h^c)*0x1000193)&0xffffffff
    return h
SW=0x14072e3e4; SLASH=0x14072e3ec; NONE=0x14072ea8d
B0,B1=0x14072e69d,0x14072e765
CODE=0x14186ea00; GL=0x14186ec00
assert bytes(d[off(SW):off(SW)+8])==bytes.fromhex('3bc30f85a1060000'), d[off(SW):off(SW)+8].hex()
assert not any(d[off(CODE):off(CODE)+0x300]), 'cave not empty'
FACTS={0x141658a1c:'KaraiVariantId',0x141658e58:'KaraiVariantIsSkin',0x141658bb4:'KaraiExists',0x141658bd4:'KaraiIsDead',0x1416591ac:'KaraiIsHost'}
gaddr={}
for k,(t,n) in enumerate(FACTS.items()):
    gaddr[t]=GL+4*k; struct.pack_into('<I',d,off(GL+4*k),fnv(n))
c=bytearray()
c+=b'\x3b\xc3'+b'\x0f\x84'+b'\0'*4; fix=[(len(c)-4,SLASH)]          # cmp eax,ebx ; je slash
c+=b'\x83\xf8\x02'+b'\x0f\x85'+b'\0'*4; fix.append((len(c)-4,NONE))  # cmp eax,2 ; jne none
blk=bytes(d[off(B0):off(B1)]); base=len(c); c+=blk
used=set()
for ins in md.disasm(blk,B0):
    rel=ins.address-B0+base
    for opnd in ins.operands:
        if opnd.type==capstone.x86.X86_OP_MEM and opnd.mem.base==capstone.x86.X86_REG_RIP:
            tgt=ins.address+ins.size+opnd.mem.disp
            if tgt in gaddr: tgt=gaddr[tgt]; used.add(tgt)
            fix.append((rel+ins.disp_offset,tgt,ins.size-ins.disp_offset-4))
    if ins.group(capstone.CS_GRP_JUMP) or ins.group(capstone.CS_GRP_CALL):
        tgt=ins.operands[0].imm
        if not (B0<=tgt<B1):
            assert ins.size>=5, ins
            fix.append((rel+ins.size-4,tgt,0))
assert len(used)==5, used
for f in fix:
    p,t=f[0],f[1]; tail=f[2] if len(f)>2 else 0
    struct.pack_into('<i',c,p,t-(CODE+p+4+tail))
d[off(CODE):off(CODE)+len(c)]=c
o=off(SW); d[o:o+8]=b'\xe9'+struct.pack('<i',CODE-(SW+5))+b'\x90'*3
open(dst,'wb').write(d)
for ins in md.disasm(bytes(c),CODE): print(hex(ins.address),ins.mnemonic,ins.op_str)
print('facts',{hex(v):n for v,n in zip(gaddr.values(),FACTS.values())})
