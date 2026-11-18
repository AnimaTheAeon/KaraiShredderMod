import pefile,capstone,sys,re
pe=pefile.PE('game/TMNTSF.exe',fast_load=True); IB=pe.OPTIONAL_HEADER.ImageBase
data=open('game/TMNTSF.exe','rb').read()
def off2va(o):
    for s in pe.sections:
        if s.PointerToRawData<=o<s.PointerToRawData+s.SizeOfRawData: return IB+s.VirtualAddress+o-s.PointerToRawData
def va2off(v):
    r=v-IB
    for s in pe.sections:
        if s.VirtualAddress<=r<s.VirtualAddress+max(s.Misc_VirtualSize,s.SizeOfRawData): return s.PointerToRawData+r-s.VirtualAddress
def cstr(v):
    o=va2off(v)
    if o is None: return None
    e=data.find(b'\0',o); s=data[o:e]
    if len(s)>=3 and all(32<=c<127 for c in s): return s.decode()
md=capstone.Cs(capstone.CS_ARCH_X86,capstone.CS_MODE_64); md.detail=False
start=int(sys.argv[1],16); n=int(sys.argv[2],16); va=off2va(start)
for i in md.disasm(data[start:start+n],va):
    extra=''
    m=re.search(r'\[rip ([+-]) (0x[0-9a-f]+)\]',i.op_str)
    if m:
        t=i.address+i.size+(int(m.group(2),16)*(1 if m.group(1)=='+' else -1))
        s=cstr(t); extra='  ; %s %s'%(hex(t), repr(s) if s else '')
    if len(sys.argv)>3 and not extra and 'cmp' not in i.mnemonic and 'call' not in i.mnemonic and not i.mnemonic.startswith('j'): continue
    print(hex(i.address),i.mnemonic,i.op_str,extra)
