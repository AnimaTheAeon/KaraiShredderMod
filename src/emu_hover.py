import os
import sys, struct; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unicorn import *; from unicorn.x86_const import *
from pe import PE
def run(path, base, ebx, rnd):
    p=PE(path); delta=base-p.base; mu=Uc(UC_ARCH_X86,UC_MODE_64)
    size=(max(v+max(vs,ps) for v,vs,_,ps,_ in p.secs)+0xfff)&~0xfff; mu.mem_map(base,size)
    for v,vs,o,ps,n in p.secs: mu.mem_write(base+v,p.d[o:o+ps])
    FAKE=0x20000000; mu.mem_map(FAKE,0x1000); mu.mem_write(FAKE,b'\xb8'+struct.pack('<I',rnd)+b'\xc3')   # mov eax,rnd; ret
    mu.mem_write(0x140f6c550+delta,struct.pack('<Q',FAKE))
    STK=0x10000000; mu.mem_map(STK,0x100000); mu.reg_write(UC_X86_REG_RSP,STK+0x80000)
    mu.reg_write(UC_X86_REG_RBX,ebx); mu.reg_write(UC_X86_REG_RDI,0x5151)
    out={}
    def h(uc,a,s,u):
        if a-delta==0x140655ca0: out['rdi']=uc.reg_read(UC_X86_REG_RDI); uc.emu_stop()
    mu.hook_add(UC_HOOK_CODE,h); mu.emu_start(0x140655bb1+delta,0,count=200)
    r=out.get('rdi')
    if r is None: return 'did not reach 0x140655ca0'
    if r==0x5151: return 'default (rdi untouched)'
    s=bytes(mu.mem_read(r,90)).split(b'\0')[0].decode(); return s.split('/')[-1]
OUT=sys.argv[1] if len(sys.argv)>1 else 'out'
for path in [os.path.join(OUT,'TMNTSF_karai.exe'),os.path.join(OUT,'TMNTSF_both.exe')]:
    for base in (0x140000000,0x7ff6a1230000):
        print(path,hex(base))
        for ebx in (0,1,2,3):
            res=[run(path,base,ebx,r) for r in range(12)] if ebx in (1,2) else [run(path,base,ebx,0)]
            print('   ebx=%d:'%ebx, res if len(set(res))>1 else res[0])
