# Step 3t: Karai gets Alopex's Inspirations (bro powers) in a run.
# HeroDataModel 0x1406ac960 builds per-hero steps "if <actor hash var> == *Hero* -> Buff_BroPower_<Hero>_001/002".
# Alopex's condition object (vtable 0x141165940 {dtor 0x1406b16c0, eval 0x1406b19a4}) gets a copied vtable whose eval is
#   orig(this,ctx) || value(this+0x30, ctx) == FNV('*Karai_Hero*')   (value resolver 0x1406b2580, the actor-hash side)
import sys,struct,pefile,capstone
src,dst=sys.argv[1],sys.argv[2]
pe=pefile.PE(src,fast_load=True); IB=pe.OPTIONAL_HEADER.ImageBase; d=bytearray(open(src,'rb').read())
def off(va): return pe.get_offset_from_rva(va-IB)
def fnv(s):
    h=0x811c9dc5
    for c in s.encode(): h=((h^c)*0x1000193)&0xffffffff
    return h
SITE=0x1406acbdc; BACK=0x1406acbe6; VT=0x141165940; ORIG=0x1406b19a4; RES=0x1406b2580
ob=bytes(d[off(SITE):off(SITE)+10]); assert ob==bytes.fromhex('4c8bc8448875b8')+ob[7:10] or True
md=capstone.Cs(capstone.CS_ARCH_X86,capstone.CS_MODE_64)
ins=list(md.disasm(ob,SITE)); print([(hex(i.address),i.mnemonic,i.op_str,i.size) for i in ins])
n=0; keep=b''
for i in ins:
    keep+=bytes(i.bytes); n+=i.size
    if n>=5: break
assert ins[0].mnemonic=='mov' and ins[0].op_str=='r9, rax' and 'rbp' in ins[1].op_str and n<=10
BACK=SITE+n
CODE=0x14186f700; KV=0x14186f7e8; END=0x14186f800
assert not any(d[off(CODE):off(END)])
c=bytearray(); fx=[]
def rip(op,t): c.extend(op); c.extend(b'\0'*4); fx.append((len(c)-4,t))
lab={}
lab['ev']=len(c)
c+=bytes.fromhex('53564883ec38')                    # push rbx; push rsi; sub rsp,0x38
c+=bytes.fromhex('4889cb4889d6')                    # mov rbx,rcx; mov rsi,rdx
rip(b'\xe8',ORIG)                                   # call orig eval
c+=bytes.fromhex('84c0'); c+=b'\x75\x00'; jnz=len(c)-1          # test al,al; jnz done
c+=bytes.fromhex('488d4b30')                        # lea rcx,[rbx+0x30]
c+=bytes.fromhex('488d542420')                      # lea rdx,[rsp+0x20]
c+=bytes.fromhex('4989f0')                          # mov r8,rsi
c+=bytes.fromhex('4531c9')                          # xor r9d,r9d
c+=bytes.fromhex('48c744242000000000')              # mov qword [rsp+0x20],0
rip(b'\xe8',RES)                                    # call resolver
c+=bytes.fromhex('817c2420')+struct.pack('<I',fnv('*Karai_Hero*'))   # cmp dword [rsp+0x20],K
c+=bytes.fromhex('0f94c0')                          # sete al
done=len(c); c[jnz]=(done-(jnz+1))&0xff
c+=bytes.fromhex('4883c4385e5bc3')                  # add rsp,0x38; pop rsi; pop rbx; ret
lab['site']=len(c)
c+=keep                                             # replay mov r9,rax; mov byte [rbp+..],r14b
c+=bytes.fromhex('488b08')                          # mov rcx,[rax]  (condition object)
rip(b'\x48\x8b\x15',VT-8); rip(b'\x48\x89\x15',KV-8)
rip(b'\x48\x8b\x15',VT);   rip(b'\x48\x89\x15',KV)
rip(b'\x48\x8d\x15',('L','ev')); rip(b'\x48\x89\x15',KV+8)
rip(b'\x48\x8d\x15',KV); c+=bytes.fromhex('488911')   # lea rdx,KV; mov [rcx],rdx
rip(b'\xe9',BACK)
for p,t in fx:
    tv=CODE+lab[t[1]] if isinstance(t,tuple) else t
    struct.pack_into('<i',c,p,tv-(CODE+p+4))
assert CODE+len(c)<=KV-8
d[off(CODE):off(CODE)+len(c)]=c
o=off(SITE); d[o:o+n]=b'\xe9'+struct.pack('<i',CODE+lab['site']-(SITE+5))+b'\x90'*(n-5)
open(dst,'wb').write(d)
for i in md.disasm(bytes(c),CODE): print(hex(i.address),i.mnemonic,i.op_str)
o=off(SITE); print([(hex(i.address),i.mnemonic,i.op_str) for i in md.disasm(bytes(d[o:o+14]),SITE)][:3])
