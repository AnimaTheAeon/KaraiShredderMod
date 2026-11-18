import pefile,struct,sys,re,numpy as np,capstone
pe=pefile.PE('game/TMNTSF.exe',fast_load=True); IB=pe.OPTIONAL_HEADER.ImageBase
data=open('game/TMNTSF.exe','rb').read()
text=[s for s in pe.sections if s.Name.startswith(b'.text')][0]
t0=text.PointerToRawData; t1=t0+text.SizeOfRawData; tva=IB+text.VirtualAddress-t0
md=capstone.Cs(capstone.CS_ARCH_X86,capstone.CS_MODE_64)
def globals_for(name):
    out=set()
    for m in re.finditer(re.escape(name.encode())+b'\0',data):
        if data[m.start()-1]!=0: continue
        sva=None
        for s in pe.sections:
            if s.PointerToRawData<=m.start()<s.PointerToRawData+s.SizeOfRawData: sva=IB+s.VirtualAddress+m.start()-s.PointerToRawData
        for mm in re.finditer(rb'[\x48\x4c]\x8d[\x05\x0d\x15\x1d\x25\x2d\x35\x3d]',data[t0:t1]):
            i=mm.start()+t0; disp=struct.unpack_from('<i',data,i+3)[0]
            if tva+i+7+disp==sva:
                for ins in md.disasm(data[i:i+0x40],tva+i):
                    if ins.mnemonic=='mov' and ins.op_str.startswith('dword ptr [rip'):
                        out.add(ins.address+ins.size+int(ins.op_str.split('+ ')[1].split(']')[0],16)); break
    return out
arr=np.frombuffer(data[t0:t1],dtype=np.uint8)
n=len(arr)-4
disp=(arr[:n].astype(np.int64)|arr[1:n+1].astype(np.int64)<<8|arr[2:n+2].astype(np.int64)<<16|arr[3:n+3].astype(np.int64)<<24)
disp=np.where(disp>=2**31,disp-2**32,disp)
base=tva+t0+np.arange(n)+4
for name in sys.argv[1:]:
    G=globals_for(name); print(name,len(G))
    hits=set()
    for extra in (0,1,4):
        tg=base+extra+disp
        idx=np.nonzero(np.isin(tg,list(G)))[0]
        for i in idx:
            for L in range(5,11):
                s=t0+i+4+extra-L
                ins=list(md.disasm(data[s:t0+i+4+extra],tva+s))
                if len(ins)==1 and ins[0].size==L and 'rip' in ins[0].op_str and not ins[0].op_str.startswith('dword ptr [rip') :
                    hits.add((ins[0].address,ins[0].mnemonic+' '+ins[0].op_str))
    for h in sorted(hits)[:30]: print(' ',hex(h[0]),h[1])
