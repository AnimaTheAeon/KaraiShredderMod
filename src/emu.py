import os
import sys, struct; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unicorn import *; from unicorn.x86_const import *
from pe import PE
STUBS={0x14084aab8:'NewRule',0x140cf6cc8:'TrigParam',0x140a7a8bc:'SwapAction',0x1409d0b30:'AddActions',0x140ce011c:'Destroy'}
def run(path, base):
    p=PE(path); delta=base-p.base
    mu=Uc(UC_ARCH_X86,UC_MODE_64)
    size=(max(v+max(vs,ps) for v,vs,_,ps,_ in p.secs)+0xfff)&~0xfff
    mu.mem_map(base,size)
    for v,vs,o,ps,n in p.secs: mu.mem_write(base+v,p.d[o:o+ps])
    for f in STUBS: mu.mem_write(f+delta,b'\xc3')
    STK=0x10000000; mu.mem_map(STK,0x100000)
    rsp=STK+0x80000; rbp=STK+0x40000; RSI=0x5150A0
    mu.reg_write(UC_X86_REG_RSP,rsp); mu.reg_write(UC_X86_REG_RBP,rbp); mu.reg_write(UC_X86_REG_RSI,RSI)
    for r in (UC_X86_REG_RBX,UC_X86_REG_R12,UC_X86_REG_R13,UC_X86_REG_R14,UC_X86_REG_R15,UC_X86_REG_RDI): mu.reg_write(r,0xdead0000+r)
    log=[]; ret_counter=[0x7000]
    def hook(uc,addr,size,ud):
        a=addr-delta
        if a in STUBS:
            R=lambda r: uc.reg_read(r)
            ent=dict(fn=STUBS[a],rcx=R(UC_X86_REG_RCX),rdx=R(UC_X86_REG_RDX),r8=R(UC_X86_REG_R8),rsp_mod16=(R(UC_X86_REG_RSP)+8)%16)
            if a==0x14084aab8: ent['str']=bytes(uc.mem_read(ent['rdx'],20)).split(b'\0')[0].decode()
            if a==0x140cf6cc8: ent['param']=struct.unpack('<IB',bytes(uc.mem_read(ent['rdx'],5)))
            log.append(ent)
            ret_counter[0]+=0x10
            rv={0x14084aab8:0x11110000+ret_counter[0],0x140cf6cc8:ent['rcx'],0x140a7a8bc:ent['rcx']}.get(a,0)
            uc.reg_write(UC_X86_REG_RAX,rv)
        if a==0x140a8ff2d: uc.emu_stop()
    mu.hook_add(UC_HOOK_CODE,hook)
    mu.emu_start(0x140a8ff26+delta,0,count=500)
    end=mu.reg_read(UC_X86_REG_RIP)-delta
    return dict(end=hex(end),rdx=hex(mu.reg_read(UC_X86_REG_RDX)-delta),rsp_ok=mu.reg_read(UC_X86_REG_RSP)==rsp,
                rsi_ok=mu.reg_read(UC_X86_REG_RSI)==RSI,rbp_ok=mu.reg_read(UC_X86_REG_RBP)==rbp,
                rdi_ok=mu.reg_read(UC_X86_REG_RDI)==0xdead0000+UC_X86_REG_RDI,
                r13_ok=mu.reg_read(UC_X86_REG_R13)==0xdead0000+UC_X86_REG_R13,
                r14_ok=mu.reg_read(UC_X86_REG_R14)==0xdead0000+UC_X86_REG_R14,
                r15_ok=mu.reg_read(UC_X86_REG_R15)==0xdead0000+UC_X86_REG_R15), log, rbp
if __name__=='__main__':
    for path in sys.argv[1:]:
        for base in (0x140000000, 0x7ff6a1230000):
            st,log,rbp=run(path,base)
            print(path, hex(base), st)
            for e in log:
                x={k:(hex(v) if isinstance(v,int) and k in('rcx','rdx','r8') else v) for k,v in e.items()}
                if 'rcx' in e and e['rcx']-rbp in (-0x40,0x4a8,-0x80): x['rcx']='rbp%+#x'%(e['rcx']-rbp)
                if 'rdx' in e and e['rdx']-rbp in (-0x80,): x['rdx']='rbp-0x80'
                print('   ',x)
