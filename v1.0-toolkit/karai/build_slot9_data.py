# Adds a separate hero "Karai" (slot 8) into the Casey record: own actor symbol + 3 HeroData cards.
import sys,struct
sys.path.insert(0,'/home/claude/work/tools')
from cffrec import Rec
HERO_T=0x2419fb6c; HD_T=0xc01a1612
def sym_chunk(off,th,name):
    b=struct.pack('<II',off,th)+name.encode()+b'\0'
    b+=b'\0'*((-(len(b)+8))%8); return b
def build(src,dst):
    r=Rec.load(open(src,'rb').read()); I=r.inst
    def align(a=16): I.extend(b'\0'*((-len(I))%a))
    def addstr(s): align(8); o=len(I); I.extend(s.encode()+b'\0'); return o
    def clone(start,size):
        align(16); new=len(I); I.extend(I[start:start+size])
        for a,t in [p for p in r.ptrs if start<=p[0]<start+size]:
            r.ptrs.append((a-start+new,t))
        return new
    P=lambda: dict(r.ptrs)
    def setptr(a,t):
        for i,(x,y) in enumerate(r.ptrs):
            if x==a: r.ptrs[i]=(a,t); return
        r.ptrs.append((a,t))
    ACT=0x108; HDS=[(0x2F8,''),(0x410,'_Skin_Samurai'),(0x528,'_Skin_TrenchCoat')]
    act=clone(ACT,496)
    s_hero=addstr('*Karai_Hero*'); s_short=addstr('Karai')
    empty=P()[0x2F8+0x08]   # empty string Casey already uses
    newhd=[]
    for base,suf in HDS:
        h=clone(base,280); s_id=addstr('*Karai_HeroData%s*'%suf)
        setptr(h+0x00,s_id); setptr(h+0x10,s_short); setptr(h+0x20,s_hero)
        setptr(h+0x40,empty)
        struct.pack_into('<I',I,h+0x18,8)     # slot index 8 (9th hero)
        struct.pack_into('<I',I,h+0x30,0)     # DLC index: base game
        struct.pack_into('<I',I,h+0x34,0)
        newhd.append((h,suf))
    align(16)
    r.syms.append(sym_chunk(act,HERO_T,'*Karai_Hero*'))
    for h,suf in newhd: r.syms.append(sym_chunk(h,HD_T,'*Karai_HeroData%s*'%suf))
    r.order+= [b'SYMB']*4
    r.ptrs.sort()
    out=r.save(); open(dst,'wb').write(out)
    # verify round trip
    r2=Rec.load(out); assert bytes(r2.inst)==bytes(I) and len(r2.ptrs)==len(r.ptrs)
    print('ok',len(out),'actor at',hex(act),'cards',[hex(h) for h,_ in newhd])
build(sys.argv[1],sys.argv[2])
