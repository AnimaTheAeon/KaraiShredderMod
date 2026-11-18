# map global -> fact-name from static-init stubs (lea rdx,'str' ... mov dword [rip+g],ecx ; ret)
import pefile,struct,re,capstone,pickle
pe=pefile.PE('game/TMNTSF.exe',fast_load=True); IB=pe.OPTIONAL_HEADER.ImageBase
data=open('game/TMNTSF.exe','rb').read()
text=[s for s in pe.sections if s.Name.startswith(b'.text')][0]
t0=text.PointerToRawData; t1=t0+text.SizeOfRawData; tva=IB+text.VirtualAddress-t0
def va2off(v):
    r=v-IB
    for s in pe.sections:
        if s.VirtualAddress<=r<s.VirtualAddress+s.SizeOfRawData: return s.PointerToRawData+r-s.VirtualAddress
md=capstone.Cs(capstone.CS_ARCH_X86,capstone.CS_MODE_64)
G={}
for m in re.finditer(rb'\x48\x8d\x15(....)\xb9\xc5\x9d\x1c\x81',data[t0:t1],re.S):
    i=m.start()+t0; sva=tva+i+7+struct.unpack('<i',m.group(1))[0]; o=va2off(sva)
    if o is None: continue
    s=data[o:data.find(b'\0',o)]
    for ins in md.disasm(data[i:i+0x40],tva+i):
        if ins.mnemonic=='mov' and ins.op_str.startswith('dword ptr [rip') and ins.op_str.endswith('ecx'):
            G[ins.address+ins.size+int(ins.op_str.split('+ ')[1].split(']')[0],16)]=s.decode('latin1'); break
        if ins.mnemonic=='ret': break
pickle.dump(G,open('/home/claude/gmap.pkl','wb')); print(len(G))
