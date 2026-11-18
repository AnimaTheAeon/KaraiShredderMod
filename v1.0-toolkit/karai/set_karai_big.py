# point all Karai HeroData cards' big select art (+0x98) at Boss_Karai.atlas:karai_big
import sys,struct
sys.path.insert(0,'/home/claude/work/tools')
from cffrec import Rec
r=Rec.load(open(sys.argv[1],'rb').read()); I=r.inst
I.extend(b'\0'*((-len(I))%8)); a=len(I); I.extend(b'Boss_Karai.atlas:karai_big\0'); I.extend(b'\0'*((-len(I))%16))
cards=[struct.unpack_from('<I',s,0)[0] for s in r.syms if s[8:s.find(b'\0',8)].startswith(b'*Karai_HeroData')]
for c in cards:
    k=[i for i,(x,y) in enumerate(r.ptrs) if x==c+0x98][0]; r.ptrs[k]=(c+0x98,a)
r.ptrs.sort(); data=r.save(); open(sys.argv[2],'wb').write(data)
r2=Rec.load(data); J=bytes(r2.inst); D=dict(r2.ptrs)
print(len(cards),[J[D[c+0x98]:J.find(b'\0',D[c+0x98])] for c in cards])
