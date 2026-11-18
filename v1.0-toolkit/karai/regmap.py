import struct,pefile,numpy as np,capstone,bisect,sys,json
pe=pefile.PE('/home/claude/game/TMNTSF.exe',fast_load=True); IB=pe.OPTIONAL_HEADER.ImageBase
pe.parse_data_directories(directories=[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_EXCEPTION']])
d=open('/home/claude/game/TMNTSF.exe','rb').read()
fs=sorted(set((IB+e.struct.BeginAddress,IB+e.struct.EndAddress) for e in pe.DIRECTORY_ENTRY_EXCEPTION)); st=[f[0] for f in fs]
def fn(v):
    i=bisect.bisect_right(st,v)-1; return fs[i] if i>=0 and fs[i][0]<=v<fs[i][1] else None
def va2off(v):
    r=v-IB
    for s in pe.sections:
        if s.VirtualAddress<=r<s.VirtualAddress+s.SizeOfRawData: return s.PointerToRawData+r-s.VirtualAddress
def off2va(o):
    for s in pe.sections:
        if s.PointerToRawData<=o<s.PointerToRawData+s.SizeOfRawData: return IB+s.VirtualAddress+o-s.PointerToRawData
ds=[s for s in pe.sections if s.Name.startswith(b'.data')][0]
q=np.frombuffer(d[ds.PointerToRawData:ds.PointerToRawData+ds.SizeOfRawData],dtype=np.uint64)
reg={}
for i in np.flatnonzero((q>=0x140f6b000)&(q<0x1413fd000)):
    if i+1>=len(q): continue
    f=int(q[i+1])
    if not (0x140001000<=f<0x140f6b000) or fn(f) is None or fn(f)[0]!=f: continue
    o=va2off(int(q[i])); s=d[o:d.find(b'\0',o)]
    if 3<len(s)<80 and all(32<c<127 for c in s): reg[s.decode()]=f
md=capstone.Cs(capstone.CS_ARCH_X86,capstone.CS_MODE_64)
def callees(f):
    a,b=fn(f); out=set()
    for i in md.disasm(d[va2off(a):va2off(b)],a):
        if i.mnemonic in('call','jmp') and i.op_str.startswith('0x'):
            t=int(i.op_str,16)
            if not (a<=t<b): out.add(t)
    return out
sites=[int(x,16) for x in sys.argv[1:]]
sitef={fn(s)[0]:s for s in sites}
res={}
for name,f in reg.items():
    lvl1=callees(f)
    hit=[sitef[x] for x in lvl1 if x in sitef]
    if not hit:
        for c in lvl1:
            if fn(c) and fn(c)[1]-fn(c)[0]<0x8000:
                for c2 in callees(c):
                    if c2 in sitef: hit.append(sitef[c2])
    if f in sitef: hit.append(sitef[f])
    for h in hit: res.setdefault(hex(h),[]).append(name)
print(len(reg),'registry names')
for k,v in res.items(): print(k,v)
json.dump(reg,open('/home/claude/registry.json','w'))
