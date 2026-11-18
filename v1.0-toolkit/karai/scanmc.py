import pefile,capstone,re,sys,bisect
from capstone.x86 import X86_OP_MEM
pe=pefile.PE('/home/claude/game/TMNTSF.exe',fast_load=True); IB=pe.OPTIONAL_HEADER.ImageBase
pe.parse_data_directories(directories=[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_EXCEPTION']])
data=open('/home/claude/game/TMNTSF.exe','rb').read()
fs=sorted(set((IB+e.struct.BeginAddress,IB+e.struct.EndAddress) for e in pe.DIRECTORY_ENTRY_EXCEPTION))
lo,hi=int(sys.argv[1],16),int(sys.argv[2],16)
dlo,dhi=int(sys.argv[3],16),int(sys.argv[4],16)
md=capstone.Cs(capstone.CS_ARCH_X86,capstone.CS_MODE_64); md.detail=True
off=lambda v: v-0x140001000+0x400
for a,b in fs:
    if not(lo<=a<hi): continue
    for i in md.disasm(data[off(a):off(b)],a):
        for op in i.operands:
            if op.type==X86_OP_MEM:
                base=i.reg_name(op.mem.base) if op.mem.base else ''
                if base in ('rsp','rip',''): continue
                if dlo<=op.mem.disp<dhi:
                    print('%x %x %s %s'%(a,i.address,i.mnemonic,i.op_str))
