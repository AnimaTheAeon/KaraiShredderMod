import pefile,capstone,sys
from capstone.x86 import X86_OP_MEM,X86_OP_REG
pe=pefile.PE('/home/claude/game/TMNTSF.exe',fast_load=True); IB=pe.OPTIONAL_HEADER.ImageBase
pe.parse_data_directories(directories=[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_EXCEPTION']])
data=open('/home/claude/game/TMNTSF.exe','rb').read()
fs=sorted(set((IB+e.struct.BeginAddress,IB+e.struct.EndAddress) for e in pe.DIRECTORY_ENTRY_EXCEPTION))
md=capstone.Cs(capstone.CS_ARCH_X86,capstone.CS_MODE_64); md.detail=True
off=lambda v: v-0x140001000+0x400
VOL={'rax','rcx','rdx','r8','r9','r10','r11'}
def full(r):
    m={'ecx':'rcx','eax':'rax','edx':'rdx','ebx':'rbx','esi':'rsi','edi':'rdi','r8d':'r8','r9d':'r9','r10d':'r10','r11d':'r11','r12d':'r12','r13d':'r13','r14d':'r14','r15d':'r15'}
    return m.get(r,r)
lo,hi=int(sys.argv[1],16),int(sys.argv[2],16)
init=sys.argv[3] # 'rcx' MC this, or 'vc' (rcx is VC; MC = [VC+0x180])
for a,b in fs:
    if not(lo<=a<hi): continue
    mc=set(['rcx']) if init=='rcx' else set(); vc=set(['rcx']) if init=='vc' else set()
    for i in md.disasm(data[off(a):off(b)],a):
        ops=i.operands
        # report memory accesses via mc regs
        for op in ops:
            if op.type==X86_OP_MEM and op.mem.base and full(i.reg_name(op.mem.base)) in mc and (0xe0<=op.mem.disp<0x10c):
                print('%x %x %-6s %s'%(a,i.address,i.mnemonic,i.op_str))
        if i.mnemonic=='call':
            mc-=VOL; vc-=VOL; continue
        if len(ops)==2 and ops[0].type==X86_OP_REG:
            dst=full(i.reg_name(ops[0].reg))
            src=ops[1]
            newmc=newvc=False
            if i.mnemonic=='mov' and src.type==X86_OP_REG:
                s=full(i.reg_name(src.reg)); newmc=s in mc; newvc=s in vc
            elif i.mnemonic=='mov' and src.type==X86_OP_MEM and src.mem.base and full(i.reg_name(src.mem.base)) in vc and src.mem.disp==0x180:
                newmc=True
            if i.mnemonic in('mov','lea','xor','add','sub','movzx','movsxd','and','or','imul','pop','shl','shr','inc','dec','neg','cmovne','cmove','sbb','setne','sete','movsx') or i.mnemonic.startswith('cmov'):
                if i.mnemonic in ('mov',) or not (i.mnemonic in ('add','sub','and','or','xor','inc','dec','shl','shr','neg','sbb') and dst in mc and False):
                    mc.discard(dst); vc.discard(dst)
                if newmc: mc.add(dst)
                if newvc: vc.add(dst)
