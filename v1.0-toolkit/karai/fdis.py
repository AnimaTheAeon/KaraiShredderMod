import pefile,capstone,sys,struct,re,bisect
pe=pefile.PE('/home/claude/game/TMNTSF.exe',fast_load=True); IB=pe.OPTIONAL_HEADER.ImageBase
pe.parse_data_directories(directories=[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_EXCEPTION']])
d=open('/home/claude/game/TMNTSF.exe','rb').read()
fs=sorted(set((IB+e.struct.BeginAddress,IB+e.struct.EndAddress) for e in pe.DIRECTORY_ENTRY_EXCEPTION)); st=[f[0] for f in fs]
def va2off(v):
    r=v-IB
    for s in pe.sections:
        if s.VirtualAddress<=r<s.VirtualAddress+max(s.Misc_VirtualSize,s.SizeOfRawData): return s.PointerToRawData+r-s.VirtualAddress
def cstr(v):
    o=va2off(v)
    if o is None: return None
    e=d.find(b'\0',o); s=d[o:e]
    return s.decode() if 3<=len(s)<200 and all(32<=c<127 for c in s) else None
md=capstone.Cs(capstone.CS_ARCH_X86,capstone.CS_MODE_64)
va=int(sys.argv[1],16); f=fs[bisect.bisect_right(st,va)-1]
for i in md.disasm(d[va2off(f[0]):va2off(f[1])],f[0]):
    ex=''
    m=re.search(r'\[rip ([+-]) (0x[0-9a-f]+)\]',i.op_str)
    if m:
        t=i.address+i.size+int(m.group(2),16)*(1 if m.group(1)=='+' else -1); s=cstr(t)
        if s: ex=repr(s)
        elif 'xmm' in i.op_str or 'ss' in i.mnemonic: ex='f=%.4g'%struct.unpack_from('<f',d,va2off(t))[0]
    m2=re.search(r', (0x[0-9a-f]{8})$',i.op_str)
    if m2 and 'dword' in i.op_str:
        f32=struct.unpack('<f',struct.pack('<I',int(m2.group(1),16)))[0]
        if 1e-3<abs(f32)<1e6: ex+=' f=%.4g'%f32
    print(hex(i.address),i.mnemonic,i.op_str,ex)
