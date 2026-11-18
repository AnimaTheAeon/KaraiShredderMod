import pefile,capstone,bisect,struct,sys,re
pe=pefile.PE('/home/claude/game/TMNTSF.exe',fast_load=True); IB=pe.OPTIONAL_HEADER.ImageBase
pe.parse_data_directories(directories=[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_EXCEPTION']])
d=open('/home/claude/game/TMNTSF.exe','rb').read()
fs=sorted(set((IB+e.struct.BeginAddress,IB+e.struct.EndAddress) for e in pe.DIRECTORY_ENTRY_EXCEPTION)); st=[f[0] for f in fs]
off=lambda v: v-0x140001000+0x400
def fn(v):
    i=bisect.bisect_right(st,v)-1; return fs[i] if fs[i][0]<=v<fs[i][1] else None
md=capstone.Cs(capstone.CS_ARCH_X86,capstone.CS_MODE_64)
targets=[int(x,16) for x in sys.argv[1:]]
tf=set(targets)
print('getter funcs',[hex(x) for x in tf])
t=[s for s in pe.sections if s.Name.startswith(b'.text')][0]; t0=t.PointerToRawData; tva=IB+t.VirtualAddress
callers=set()
for m in re.finditer(rb'\xe8',d[t0:t0+t.Misc_VirtualSize]):
    i=t0+m.start(); dd=struct.unpack_from('<i',d,i+1)[0]; tg=tva+m.start()+5+dd
    if tg in tf:
        f=fn(tva+m.start())
        if f: callers.add(f)
for a,b in sorted(callers):
    hits=[]
    for i in md.disasm(d[off(a):off(b)],a):
        if '+ 0x1e0]' in i.op_str or '+ 0x1e4]' in i.op_str or '+ 0x1e8]' in i.op_str: hits.append('%x %s %s'%(i.address,i.mnemonic,i.op_str))
    if hits: print(hex(a),hits[:4])
