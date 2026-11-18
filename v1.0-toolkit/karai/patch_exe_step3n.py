# Step 3n: give Karai the real Kunai starting tool.
# Hero spawn steps (built in 0x140a07e0c) are "if HasBuff(Buff_<Hero>_LifetimeBuff) -> give tool marker".
# Their condition objects use vtable 0x1411b0648 {dtor 0x14091324c, eval 0x140910670}.
#  - Alopex's step (Kunai): eval becomes  orig || isKarai(entity)
#  - Casey's step  (Heckle): eval becomes  orig && !isKarai(entity)
# isKarai(entity) = HeroData lookup 0x1406a6570(entity+0x1c8) -> card, card+0x78 (slot) == 8.
# All absolute addresses (vtables) are written at runtime (ASLR).
import sys,struct,pefile,capstone
src,dst=sys.argv[1],sys.argv[2]
pe=pefile.PE(src,fast_load=True); IB=pe.OPTIONAL_HEADER.ImageBase; d=bytearray(open(src,'rb').read())
def off(va): return pe.get_offset_from_rva(va-IB)
ORIG_EVAL=0x140910670; LOOKUP=0x1406a6570; VT=0x1411b0648
CODE=0x14186f200; KVA=0x14186f408; KVC=0x14186f428; END=0x14186f440
assert not any(d[off(CODE):off(END)]), 'cave not empty'
SITES={'A':(0x140a08587,bytes.fromhex('4c8bc848894500'),0x140a0858e,KVA),      # Alopex: mov r9,rax; mov [rbp],rax
       'C':(0x140a08737,bytes.fromhex('4c8bc8488945e0'),0x140a0873e,KVC)}      # Casey : mov r9,rax; mov [rbp-0x20],rax
for k,(a,ob,_,_) in SITES.items(): assert bytes(d[off(a):off(a)+7])==ob,(k,d[off(a):off(a)+7].hex())
c=bytearray(); fix=[]   # (pos_of_rel32, target_va)
def rel(op,tgt): c.extend(op); c.extend(b'\0\0\0\0'); fix.append((len(c)-4,tgt))
lab={}
# --- isKarai(rcx=entity) -> al
lab['isK']=len(c)
c+=b'\x48\x83\xec\x28'                       # sub rsp,0x28
c+=b'\x48\x81\xc1'+struct.pack('<I',0x1c8)    # add rcx,0x1c8
rel(b'\xe8',LOOKUP)                           # call lookup
c+=b'\x48\x85\xc0'                            # test rax,rax
c+=b'\x74\x0c'                                # jz no (+12)
c+=b'\x83\x78\x78\x08'                        # cmp dword [rax+0x78],8
c+=b'\x0f\x94\xc0'                            # sete al
c+=b'\x48\x83\xc4\x28\xc3'                    # add rsp,0x28; ret
c+=b'\x31\xc0\x48\x83\xc4\x28\xc3'            # no: xor eax,eax; add rsp,0x28; ret
# --- evalA: orig || isKarai
lab['evA']=len(c)
c+=b'\x53\x48\x83\xec\x20\x48\x89\xd3'        # push rbx; sub rsp,0x20; mov rbx,rdx
rel(b'\xe8',ORIG_EVAL)
c+=b'\x84\xc0\x75\x0e'                        # test al,al; jnz done(+14)
c+=b'\x48\x8b\x0b\x48\x85\xc9\x74\x06'        # mov rcx,[rbx]; test rcx,rcx; jz done(+6)
isk1=len(c); c+=b'\xe8\0\0\0\0'               # call isKarai
c+=b'\x90'
c+=b'\x48\x83\xc4\x20\x5b\xc3'                # done: add rsp,0x20; pop rbx; ret
# --- evalC: orig && !isKarai
lab['evC']=len(c)
c+=b'\x53\x48\x83\xec\x20\x48\x89\xd3'
rel(b'\xe8',ORIG_EVAL)
c+=b'\x84\xc0\x74\x13'                        # test al,al; jz done(+19)
c+=b'\x48\x8b\x0b\x48\x85\xc9\x74\x09'        # mov rcx,[rbx]; test rcx,rcx; jz yes(+9)
isk2=len(c); c+=b'\xe8\0\0\0\0'               # call isKarai
c+=b'\x34\x01'                                # xor al,1
c+=b'\xeb\x02'                                # jmp done
c+=b'\xb0\x01'                                # yes: mov al,1
c+=b'\x48\x83\xc4\x20\x5b\xc3'                # done
for p in (isk1,isk2): struct.pack_into('<i',c,p+1,lab['isK']-(p+5))
# --- site caves
for k,(a,ob,back,KV) in SITES.items():
    lab['site'+k]=len(c)
    c+=ob                                                         # replay mov r9,rax; mov [rbp..],rax
    c+=b'\x48\x8b\x15'; c+=b'\0'*4; fix.append((len(c)-4,VT-8))   # mov rdx,[rip+VT-8]  (RTTI)
    c+=b'\x48\x89\x15'; c+=b'\0'*4; fix.append((len(c)-4,KV-8))   # mov [rip+KV-8],rdx
    c+=b'\x48\x8b\x15'; c+=b'\0'*4; fix.append((len(c)-4,VT))     # mov rdx,[rip+VT]    (dtor)
    c+=b'\x48\x89\x15'; c+=b'\0'*4; fix.append((len(c)-4,KV))     # mov [rip+KV],rdx
    c+=b'\x48\x8d\x15'; c+=b'\0'*4; fix.append((len(c)-4,('L','ev'+k)))  # lea rdx,[rip+evalX]
    c+=b'\x48\x89\x15'; c+=b'\0'*4; fix.append((len(c)-4,KV+8))   # mov [rip+KV+8],rdx
    c+=b'\x48\x8b\x08'                                            # mov rcx,[rax]   (heap condition object)
    c+=b'\x48\x8d\x15'; c+=b'\0'*4; fix.append((len(c)-4,KV))     # lea rdx,[rip+KV]
    c+=b'\x48\x89\x11'                                            # mov [rcx],rdx   (swap vtable)
    rel(b'\xe9',back)
for p,t in fix:
    tv=CODE+lab[t[1]] if isinstance(t,tuple) else t
    struct.pack_into('<i',c,p,tv-(CODE+p+4))
assert CODE+len(c)<KVA-8, hex(CODE+len(c))
d[off(CODE):off(CODE)+len(c)]=c
for k,(a,ob,back,KV) in SITES.items():
    o=off(a); d[o:o+7]=b'\xe9'+struct.pack('<i',CODE+lab['site'+k]-(a+5))+b'\x90\x90'
open(dst,'wb').write(d)
md=capstone.Cs(capstone.CS_ARCH_X86,capstone.CS_MODE_64)
for i in md.disasm(bytes(c),CODE): print(hex(i.address),i.mnemonic,i.op_str)
print({k:hex(CODE+v) for k,v in lab.items()})
