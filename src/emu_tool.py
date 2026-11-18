import os
import sys, struct; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unicorn import *; from unicorn.x86_const import *
from pe import PE
def fnv(s):
    h=0x811c9dc5
    for c in s.encode(): h=((h^c)*0x1000193)&0xffffffff
    return h
H={n:fnv(n) for n in ['*Karai_Hero*','*Shredder_Hero*','*CaseyJones_Hero*','*Raphael*','*Alopex*','*Karai*','*Shredder*',
   'BuffMarker_Ability_Common_005_Heckle','BuffMarker_Ability_Common_007_Kunai','BuffMarker_Ability_Common_002_Hook','BuffMarker_Ability_Ninja_001_SmokeBomb',
   '*PowerSelect_Ability_Common_005_Heckle*','*PowerSelect_Ability_Common_007_Kunai_Karai*','*PowerSelect_Ability_Common_002_Hook*','*PowerSelect_Ability_Ninja_001_SmokeBomb_Shredder*','*PowerSelect_Ability_Common_007_Kunai*',
   'tool','tool_common_5','tool_common_7','tool_common_2','tool_ninja_1','Buff_Whatever','dash','*AllBuffs*']}
R={v:k for k,v in H.items()}
nm=lambda v: R.get(v,hex(v))
class Img:
    def __init__(s,path,base):
        s.p=PE(path); s.delta=base-s.p.base; s.mu=Uc(UC_ARCH_X86,UC_MODE_64)
        size=(max(v+max(vs,ps) for v,vs,_,ps,_ in s.p.secs)+0xfff)&~0xfff; s.mu.mem_map(base,size)
        for v,vs,o,ps,n in s.p.secs: s.mu.mem_write(base+v,s.p.d[o:o+ps])
        s.mu.mem_map(0x10000000,0x200000)
    def run_a(s,actor,buff,ps):
        mu=s.mu; D=0x10100000; ENT=D; ACT=D+0x1000
        mu.mem_write(ENT,b'\0'*0x200); mu.mem_write(ENT+0x78,struct.pack('<I',actor))
        mu.mem_write(ACT,b'\0'*0x200); mu.mem_write(ACT+0x70,struct.pack('<II',buff,ps))
        rsp=0x10080000; mu.reg_write(UC_X86_REG_RSP,rsp); mu.reg_write(UC_X86_REG_RBX,ENT); mu.reg_write(UC_X86_REG_R14,ACT)
        mu.reg_write(UC_X86_REG_RDX,H['*AllBuffs*']); mu.reg_write(UC_X86_REG_RSI,0x5151); mu.reg_write(UC_X86_REG_RDI,0x5252)
        mu.mem_write(0x140d06f6c+s.delta,b'\xc3'); seen={}
        def h(uc,a,sz,u):
            if a-s.delta==0x140d06f6c: seen['ecx']=uc.reg_read(UC_X86_REG_ECX); seen['edx']=uc.reg_read(UC_X86_REG_EDX); seen['rsp_al']=(uc.reg_read(UC_X86_REG_RSP)+8)%16
            if a-s.delta==0x140cded98: uc.emu_stop()
        hk=mu.hook_add(UC_HOOK_CODE,h); mu.emu_start(0x140cded8f+s.delta,0,count=200); mu.hook_del(hk)
        end=mu.reg_read(UC_X86_REG_RIP)-s.delta
        b2,p2=struct.unpack('<II',bytes(mu.mem_read(ACT+0x70,8)))
        ok_regs=mu.reg_read(UC_X86_REG_RBX)==ENT and mu.reg_read(UC_X86_REG_R14)==ACT and mu.reg_read(UC_X86_REG_RSI)==0x5151 and mu.reg_read(UC_X86_REG_RDI)==0x5252 and mu.reg_read(UC_X86_REG_RSP)==rsp
        return end==0x140cded98, seen.get('ecx'), seen.get('edx')==H['*AllBuffs*'], b2, p2, ok_regs, seen.get('rsp_al')
    def run_b(s,actor,src,dst,null_owner=False):
        mu=s.mu; D=0x10100000; ENT=D+0x2000; CFG=D+0x3000
        mu.mem_write(ENT,b'\0'*0x200); mu.mem_write(ENT+0x78,struct.pack('<I',actor))
        mu.mem_write(CFG,b'\0'*0x40); mu.mem_write(CFG+0x10,struct.pack('<II',src,dst))
        rsp=0x10080000; mu.mem_write(rsp,b'\0'*0x100); mu.mem_write(rsp+0x20,struct.pack('<Q',0 if null_owner else ENT+0x28))
        mu.reg_write(UC_X86_REG_RSP,rsp); mu.reg_write(UC_X86_REG_R8,CFG); mu.reg_write(UC_X86_REG_RBX,0x6161)
        def h(uc,a,sz,u):
            if a-s.delta==0x140d0cb96: uc.emu_stop()
        hk=mu.hook_add(UC_HOOK_CODE,h); mu.emu_start(0x140d0cb8e+s.delta,0,count=200); mu.hook_del(hk)
        end=mu.reg_read(UC_X86_REG_RIP)-s.delta
        return end==0x140d0cb96, mu.reg_read(UC_X86_REG_R8D), mu.reg_read(UC_X86_REG_R9D), mu.reg_read(UC_X86_REG_RSP)==rsp and mu.reg_read(UC_X86_REG_RBX)==0x6161
A_CASES=[('*Karai_Hero*','BuffMarker_Ability_Common_005_Heckle','*PowerSelect_Ability_Common_005_Heckle*'),
         ('*Karai_Hero*','BuffMarker_Ability_Common_005_Heckle','*PowerSelect_Ability_Common_007_Kunai*'),
         ('*Karai_Hero*','BuffMarker_Ability_Common_007_Kunai','*PowerSelect_Ability_Common_007_Kunai*'),
         ('*Karai_Hero*','Buff_Whatever','*PowerSelect_Ability_Common_005_Heckle*'),
         ('*Karai_Hero*','BuffMarker_Ability_Common_002_Hook','*PowerSelect_Ability_Common_002_Hook*'),
         ('*Shredder_Hero*','BuffMarker_Ability_Common_002_Hook','*PowerSelect_Ability_Common_002_Hook*'),
         ('*Shredder_Hero*','BuffMarker_Ability_Common_005_Heckle','*PowerSelect_Ability_Common_005_Heckle*'),
         ('*Shredder_Hero*','Buff_Whatever','*PowerSelect_Ability_Common_002_Hook*'),
         ('*CaseyJones_Hero*','BuffMarker_Ability_Common_005_Heckle','*PowerSelect_Ability_Common_005_Heckle*'),
         ('*Raphael*','BuffMarker_Ability_Common_002_Hook','*PowerSelect_Ability_Common_002_Hook*'),
         ('*Alopex*','BuffMarker_Ability_Common_007_Kunai','*PowerSelect_Ability_Common_007_Kunai*'),
         ('*Karai*','BuffMarker_Ability_Common_005_Heckle','*PowerSelect_Ability_Common_005_Heckle*'),
         ('*Shredder*','BuffMarker_Ability_Common_002_Hook','*PowerSelect_Ability_Common_002_Hook*')]
B_CASES=[('*Karai_Hero*','tool','tool_common_7',False),('*Karai_Hero*','tool','tool_common_5',False),('*Karai_Hero*','dash','tool_common_7',False),
         ('*Karai_Hero*','tool','tool_common_7',True),('*Shredder_Hero*','tool','tool_ninja_1',False),('*Shredder_Hero*','tool','tool_common_2',False),
         ('*Shredder_Hero*','dash','tool_ninja_1',False),('*Shredder_Hero*','tool','tool_common_7',False),('*Karai_Hero*','tool','tool_ninja_1',False),
         ('*Alopex*','tool','tool_common_7',False),('*CaseyJones_Hero*','tool','tool_common_5',False),('*Raphael*','tool','tool_common_2',False),
         ('*Karai*','tool','tool_common_7',False),('*Shredder*','tool','tool_ninja_1',False)]
def expect_a(build,actor,buff,ps):
    k = build in ('karai','both') and actor=='*Karai_Hero*'
    s = build in ('shredder','both') and actor=='*Shredder_Hero*'
    if k and buff=='BuffMarker_Ability_Common_005_Heckle':
        return 'BuffMarker_Ability_Common_007_Kunai', ('*PowerSelect_Ability_Common_007_Kunai_Karai*' if ps=='*PowerSelect_Ability_Common_005_Heckle*' else ps)
    if s and buff=='BuffMarker_Ability_Common_002_Hook':
        return 'BuffMarker_Ability_Ninja_001_SmokeBomb', ('*PowerSelect_Ability_Ninja_001_SmokeBomb_Shredder*' if ps=='*PowerSelect_Ability_Common_002_Hook*' else ps)
    return buff, ps
def expect_b(build,actor,src,dst,null):
    if null or src!='tool': return src,dst
    if build in ('karai','both') and actor=='*Karai_Hero*' and dst=='tool_common_7': return src,'tool_common_5'
    if build in ('shredder','both') and actor=='*Shredder_Hero*' and dst=='tool_ninja_1': return src,'tool_common_2'
    return src,dst
total=fail=0
OUT=sys.argv[1] if len(sys.argv)>1 else 'out'
for path,build in [(os.path.join(OUT,'TMNTSF_karai.exe'),'karai'),(os.path.join(OUT,'TMNTSF_shredder.exe'),'shredder'),(os.path.join(OUT,'TMNTSF_both.exe'),'both')]:
    for base in (0x140000000,0x7ff6a1230000):
        im=Img(path,base)
        for actor,buff,ps in A_CASES:
            done,ecx,edx_ok,b2,p2,regs,al=im.run_a(H[actor],H[buff],H[ps])
            eb,ep=expect_a(build,actor,buff,ps)
            ok=done and edx_ok and regs and al==0 and nm(ecx)==eb and nm(b2)==eb and nm(p2)==ep
            total+=1; fail+=not ok
            if not ok or base==0x140000000 and build=='both': print(('PASS' if ok else 'FAIL'),build,hex(base),'A',actor,'|',buff,'->',nm(ecx),'| PS ->',nm(p2))
        for actor,src,dst,null in B_CASES:
            done,r8,r9,regs=im.run_b(H[actor],H[src],H[dst],null)
            es,ed=expect_b(build,actor,src,dst,null)
            ok=done and regs and nm(r8)==es and nm(r9)==ed
            total+=1; fail+=not ok
            if not ok or base==0x140000000 and build=='both': print(('PASS' if ok else 'FAIL'),build,hex(base),'B',actor,src,dst,'null' if null else '','->',nm(r9))
print('\n%d checks, %d failed'%(total,fail))
