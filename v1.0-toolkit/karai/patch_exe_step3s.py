# Step 3r: HUD icon fixes for Karai.
#  (a) dash fallback style 'abilitybutton_rebirth_dash' (no frame) -> 'abilitybutton_rebirth_dash_raph' (framed, red)
#  (b) at HUD chooser entry (0x140683667: mov r14,[rdx+0x38]; mov [rsp+0x28],r14): if the hero is Karai
#      ([entity+0x78]==FNV('*Karai_Hero*'), entity = 0x14056bd48(rbp+0x10)) and the descriptor name is
#      'Ability_Common_007_Kunai', swap r14 for a fake descriptor (copy of the first 0x40 bytes) whose
#      +0x18/+0x20/+0x28 = 'Boss_Karai' / 'karai_kunai' / 'karai_kunai'. All pointers are written at runtime (ASLR).
import sys,struct,pefile,capstone,re
src,dst=sys.argv[1],sys.argv[2]
pe=pefile.PE(src,fast_load=True); IB=pe.OPTIONAL_HEADER.ImageBase; d=bytearray(open(src,'rb').read())
def off(va): return pe.get_offset_from_rva(va-IB)
def va_of_str(s):
    for m in re.finditer(re.escape(s.encode())+b'\0',d):
        if d[m.start()-1]==0:
            for sec in pe.sections:
                if sec.PointerToRawData<=m.start()<sec.PointerToRawData+sec.SizeOfRawData: return IB+sec.VirtualAddress+m.start()-sec.PointerToRawData
def fnv(s):
    h=0x811c9dc5
    for c in s.encode(): h=((h^c)*0x1000193)&0xffffffff
    return h
# (a) Karai's fallback button styles -> a style name that does not exist (draws nothing; the custom
#     Boss_Karai icon from the slot fields then shows alone, with its own baked-in ring)
FALLBACKS=[0x140683ba4,0x140683fd6,0x140683b00]   # dash fallback, special fallback, unmatched-ability fallback
for a in FALLBACKS: assert bytes(d[off(a):off(a)+3])==b'\x48\x8d\x15', hex(a)
# (b)
SITE=0x140683667; BACK=0x140683670
assert bytes(d[off(SITE):off(SITE)+9])==bytes.fromhex('4c8b72384c89742428'), d[off(SITE):off(SITE)+9].hex()
CODE=0x14186f480; DATA=0x14186f600; FAKE=DATA; S_NAME=DATA+0x40; S_ATL=DATA+0x60; S_SPR=DATA+0x70; S_FN=DATA+0x80; S_NONE=DATA+0xA0; END=DATA+0xC8
assert not any(d[off(CODE):off(END)])
for a,s in ((S_NAME,'Ability_Common_007_Kunai'),(S_ATL,'Boss_Karai'),(S_SPR,'karai_kunai_hud'),(S_FN,'Ability_Karai_Kunai'),(S_NONE,'abilitybutton_rebirth_karai_none')): b=s.encode()+b'\0'; d[off(a):off(a)+len(b)]=b
c=bytearray(); fx=[]
def rip(op,tgt): c.extend(op); c.extend(b'\0'*4); fx.append((len(c)-4,tgt))
c+=bytes.fromhex('4c8b7238')                     # mov r14,[rdx+0x38]
c+=bytes.fromhex('4d85f6'); c+=b'\x0f\x84'; c+=b'\0'*4; j_out1=len(c)-4      # test r14,r14 ; jz out
c+=bytes.fromhex('4989d2')                        # mov r10,rdx (keep rdx)
# strcmp([r14], S_NAME)
c+=bytes.fromhex('498b06')                        # mov rax,[r14]
c+=bytes.fromhex('4885c0'); c+=b'\x0f\x84'; c+=b'\0'*4; j_out2=len(c)-4      # test rax,rax ; jz out
rip(b'\x48\x8d\x0d',S_NAME)                       # lea rcx,[rip+S_NAME]
loop=len(c)
c+=bytes.fromhex('448a00')                        # mov r8b,[rax]
c+=bytes.fromhex('443a01')                        # cmp r8b,[rcx]
c+=b'\x0f\x85'; c+=b'\0'*4; j_out3=len(c)-4       # jne out
c+=bytes.fromhex('4584c0'); c+=b'\x74\x08'        # test r8b,r8b ; jz match (+8)
c+=bytes.fromhex('48ffc0')                        # inc rax
c+=bytes.fromhex('48ffc1')                        # inc rcx
c+=b'\xeb'; c+=bytes([(loop-(len(c)+1))&0xff])    # jmp loop
# match: is the hero Karai?
c+=bytes.fromhex('488d4d10')                      # lea rcx,[rbp+0x10]
c+=b'\xe8'; c+=b'\0'*4; fx.append((len(c)-4,0x14056bd48))   # call handle->entity
c+=bytes.fromhex('4885c0'); c+=b'\x74\x5c'; j_out4=len(c)-1  # test rax,rax ; jz out (patched below)
c+=bytes.fromhex('817878')+struct.pack('<I',fnv('*Karai_Hero*'))   # cmp dword [rax+0x78],K
c+=b'\x75\x00'; j_out5=len(c)-1                   # jne out (patched below)
# build fake descriptor: copy 0x40 bytes from r14, then set icon fields
rip(b'\x48\x8d\x0d',FAKE)                         # lea rcx,[rip+FAKE]
for q in range(0,0x40,8):
    c+=bytes.fromhex('498b46')+bytes([q])         # mov rax,[r14+q]
    c+=bytes.fromhex('488941')+bytes([q])         # mov [rcx+q],rax
rip(b'\x48\x8d\x05',S_ATL); c+=bytes.fromhex('48894118')   # lea rax,atl ; mov [rcx+0x18],rax
rip(b'\x48\x8d\x05',S_SPR); c+=bytes.fromhex('48894120')   # lea rax,spr ; mov [rcx+0x20],rax
c+=bytes.fromhex('48894128')                               # mov [rcx+0x28],rax
rip(b'\x48\x8d\x05',S_FN); c+=bytes.fromhex('488901')     # name -> unmatched, so no green style
c+=bytes.fromhex('4989ce')                                 # mov r14,rcx
out=len(c)
c+=bytes.fromhex('4c89d2')                        # mov rdx,r10   (harmless if r10 unset on early-out paths: see below)
c+=bytes.fromhex('4c89742428')                    # mov [rsp+0x28],r14
c+=b'\xe9'; c+=b'\0'*4; fx.append((len(c)-4,BACK))
# early-outs before r10 was saved must skip 'mov rdx,r10'
out_nor10=out+3
for p,tgt in ((j_out1,out_nor10),(j_out2,out),(j_out3,out)): struct.pack_into('<i',c,p,tgt-(p+4))
c[j_out4]=(out-(j_out4+1))&0xff; c[j_out5]=(out-(j_out5+1))&0xff
assert 0<out-(j_out4+1)<128 and 0<out-(j_out5+1)<128
for p,t in fx: struct.pack_into('<i',c,p,t-(CODE+p+4))
assert CODE+len(c)<DATA
d[off(CODE):off(CODE)+len(c)]=c
for a in FALLBACKS: struct.pack_into('<i',d,off(a)+3,S_NONE-(a+7))
o=off(SITE); d[o:o+9]=b'\xe9'+struct.pack('<i',CODE-(SITE+5))+b'\x90'*4
open(dst,'wb').write(d)
md=capstone.Cs(capstone.CS_ARCH_X86,capstone.CS_MODE_64)
ins=list(md.disasm(bytes(c),CODE)); starts={i.address for i in ins}
for i in ins: print(hex(i.address),i.mnemonic,i.op_str)
bad=[i for i in ins if (i.mnemonic.startswith('j')) and CODE<=int(i.op_str,16)<CODE+len(c) and int(i.op_str,16) not in starts]
print('bad',bad)
