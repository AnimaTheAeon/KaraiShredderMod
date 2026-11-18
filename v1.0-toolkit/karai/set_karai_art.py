import sys,struct
sys.path.insert(0,'/home/claude/work/tools')
from cffrec import Rec
r=Rec.load(open(sys.argv[1],'rb').read()); I=r.inst
def align(a=16): I.extend(b'\0'*((-len(I))%a))
def addstr(s): align(8); a=len(I); I.extend(s.encode()+b'\0'); return a
def setptr(a,t):
    for k,(x,y) in enumerate(r.ptrs):
        if x==a: r.ptrs[k]=(a,t); return
    raise KeyError(hex(a))
cards=[struct.unpack_from('<I',s,0)[0] for s in r.syms if s[8:s.find(b'\0',8)].startswith(b'*Karai_HeroData')]
hud=addstr('Boss_Karai.atlas:karai_hud'); sel=addstr('Boss_Karai.atlas:karai_select')
for c in cards: setptr(c+0x70,hud); setptr(c+0xc8,sel)
align(16); r.ptrs.sort(); data=r.save(); open(sys.argv[2],'wb').write(data)
r2=Rec.load(data); D=dict(r2.ptrs); J=bytes(r2.inst); cs=lambda a: J[a:J.find(b'\0',a)].decode()
print(len(cards),[ (cs(D[c+0x70]),cs(D[c+0x98]),cs(D[c+0xc8])) for c in cards][:1])
