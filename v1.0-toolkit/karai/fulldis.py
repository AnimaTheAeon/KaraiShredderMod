import pefile,capstone,struct
pe=pefile.PE('game/TMNTSF.exe'); IB=pe.OPTIONAL_HEADER.ImageBase
data=open('game/TMNTSF.exe','rb').read()
md=capstone.Cs(capstone.CS_ARCH_X86,capstone.CS_MODE_64); md.skipdata=True
pd=pe.OPTIONAL_HEADER.DATA_DIRECTORY[3]; o=pe.get_offset_from_rva(pd.VirtualAddress)
funcs=sorted(set(struct.unpack_from('<II',data,o+i*12)[:2] for i in range(pd.Size//12)))
out=open('full.dis','w')
for b,e in funcs:
    fo=pe.get_offset_from_rva(b)
    out.write('F %x\n'%(IB+b))
    for a,s,m,op in md.disasm_lite(data[fo:fo+(e-b)],IB+b):
        out.write('%x %s %s\n'%(a,m,op))
print(len(funcs))
