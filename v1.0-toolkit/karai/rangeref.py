import pefile,numpy as np,sys,capstone,bisect
pe=pefile.PE('/home/claude/game/TMNTSF.exe',fast_load=True); IB=pe.OPTIONAL_HEADER.ImageBase
pe.parse_data_directories(directories=[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_EXCEPTION']])
data=open('/home/claude/game/TMNTSF.exe','rb').read()
t=[s for s in pe.sections if s.Name.startswith(b'.text')][0]
t0=t.PointerToRawData; n=t.Misc_VirtualSize; tva=IB+t.VirtualAddress
lo=int(sys.argv[1],16); hi=int(sys.argv[2],16)
arr=np.frombuffer(data[t0:t0+n+8],dtype=np.uint8)
d=(arr[:-7].astype(np.int64)|(arr[1:-6].astype(np.int64)<<8)|(arr[2:-5].astype(np.int64)<<16)|(arr[3:-4].astype(np.int64)<<24))
d=np.where(d>=2**31,d-2**32,d)
pos=np.arange(len(d))
funcs=sorted(set((IB+e.struct.BeginAddress,IB+e.struct.EndAddress) for e in pe.DIRECTORY_ENTRY_EXCEPTION)); starts=[f[0] for f in funcs]
def fn(va):
    i=bisect.bisect_right(starts,va)-1; return funcs[i][0] if i>=0 and funcs[i][0]<=va<funcs[i][1] else None
md=capstone.Cs(capstone.CS_ARCH_X86,capstone.CS_MODE_64)
seen=set()
for k in (0,1,2,4):
    tgt=tva+pos+4+k+d
    for i in np.flatnonzero((tgt>=lo)&(tgt<hi)):
        end=int(i)+4+k
        for L in range(5,12):
            s=end-L
            if s<0: continue
            ins=list(md.disasm(data[t0+s:t0+end],tva+s))
            if len(ins)==1 and ins[0].size==L and 'rip' in ins[0].op_str:
                a=ins[0].address
                if a in seen: break
                seen.add(a); target=tva+end+int(d[i])
                print(hex(a),hex(target),ins[0].mnemonic,ins[0].op_str,'func',hex(fn(a)) if fn(a) else None); break
