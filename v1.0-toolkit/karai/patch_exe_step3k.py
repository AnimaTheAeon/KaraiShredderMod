# Step 3k: custom localized strings for Karai.
# Hooks the localization lookup 0x14074278c (ecx = FNV1a hash of the key) so Karai's new keys
# return our own UTF-16 string objects {u32 len, pad, u16* chars} instead of the empty string.
import sys,struct,pefile
src,dst=sys.argv[1],sys.argv[2]
pe=pefile.PE(src,fast_load=True); IB=pe.OPTIONAL_HEADER.ImageBase; d=bytearray(open(src,'rb').read())
def off(va): return pe.get_offset_from_rva(va-IB)
def fnv(s):
    h=0x811c9dc5
    for c in s.encode(): h=((h^c)*0x1000193)&0xffffffff
    return h
TEXT={
 'UI_CHARACTER_DESCRIPTION_KARAI':"The Foot Clan's deadliest kunoichi, trained by the Shredder himself. Karai fights with swift, precise blade work and never misses an opening.",
 'SPECIAL_ATTACK_KARAI_NAME':"Cleave",
 'SPECIAL_ATTACK_KARAI_DESC':"Unleash a sweeping sword strike that cuts through every enemy in front of you.",
}
FN=0x14074278c; BACK=0x140742794
ORIG=bytes.fromhex('405348 83ec20 8bd9'.replace(' ',''))
assert bytes(d[off(FN):off(FN)+8])==ORIG, d[off(FN):off(FN)+8].hex()
CODE=0x14186ee00; OBJ=0x14186ef00; STR=0x14186ef80; END=0x141870000
assert not any(d[off(CODE):off(CODE)+(END-CODE)]), 'cave area not empty'
objs={}; sp=STR
for k,(key,txt) in enumerate(TEXT.items()):
    u=txt.encode('utf-16-le')+b'\0\0'
    d[off(sp):off(sp)+len(u)]=u
    o=OBJ+0x10*k; struct.pack_into('<IIQ',d,off(o),len(txt),0,0); objs[key]=(o,sp)   # chars ptr filled at runtime (ASLR)
    sp=(sp+len(u)+15)&~15
assert sp<END
c=bytearray(); fx=[]
for key in TEXT:
    c+=b'\x81\xf9'+struct.pack('<I',fnv(key)); c+=b'\x0f\x84\0\0\0\0'; fx.append((len(c)-4,key))
c+=ORIG; c+=b'\xe9\0\0\0\0'; jb=len(c)-4
ret={}
for key in TEXT:
    o,sp_=objs[key]; ret[key]=len(c)
    c+=b'\x48\x8d\x05\0\0\0\0'; struct.pack_into('<i',c,len(c)-4,sp_-(CODE+len(c)))          # lea rax,[rip+chars]
    c+=b'\x48\x89\x05\0\0\0\0'; struct.pack_into('<i',c,len(c)-4,(o+8)-(CODE+len(c)))       # mov [rip+obj+8],rax
    c+=b'\x48\x8d\x05\0\0\0\0'; struct.pack_into('<i',c,len(c)-4,o-(CODE+len(c)))           # lea rax,[rip+obj]
    c+=b'\xc3'
for p,key in fx: struct.pack_into('<i',c,p,ret[key]-(p+4))
struct.pack_into('<i',c,jb,BACK-(CODE+jb+4))
assert CODE+len(c)<OBJ
d[off(CODE):off(CODE)+len(c)]=c
o=off(FN); d[o:o+8]=b'\xe9'+struct.pack('<i',CODE-(FN+5))+b'\x90'*3
open(dst,'wb').write(d)
import capstone
md=capstone.Cs(capstone.CS_ARCH_X86,capstone.CS_MODE_64)
for i in md.disasm(bytes(c),CODE): print(hex(i.address),i.mnemonic,i.op_str)
for k,v in objs.items(): print(k,hex(fnv(k)),hex(v[0]),hex(v[1]))
