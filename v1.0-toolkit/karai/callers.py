import pefile,struct,sys,re
pe=pefile.PE('game/TMNTSF.exe',fast_load=True); IB=pe.OPTIONAL_HEADER.ImageBase
pe.parse_data_directories(directories=[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_EXCEPTION']])
data=open('game/TMNTSF.exe','rb').read()
text=[s for s in pe.sections if s.Name.startswith(b'.text')][0]
t0=text.PointerToRawData; t1=t0+text.SizeOfRawData; tva=IB+text.VirtualAddress-t0
funcs=sorted((IB+e.struct.BeginAddress,IB+e.struct.EndAddress) for e in pe.DIRECTORY_ENTRY_EXCEPTION)
import bisect
starts=[f[0] for f in funcs]
def fn(va):
    i=bisect.bisect_right(starts,va)-1; return funcs[i] if i>=0 and funcs[i][0]<=va<funcs[i][1] else None
for a in sys.argv[1:]:
    va=int(a,16); f=fn(va); print('addr',a,'in func',[hex(x) for x in f] if f else None)
    tgt=f[0] if f else va
    for m in re.finditer(rb'\xe8',data[t0:t1]):
        i=t0+m.start(); d=struct.unpack_from('<i',data,i+1)[0]
        if tva+i+5+d==tgt: 
            c=tva+i; g=fn(c); print('  call from',hex(c),'func',hex(g[0]) if g else None)
