# Karai default card: select-screen ink splash (+0xA8) -> Raph's red Frame_Ink_Raph (skins keep their skin backgrounds)
import sys,struct
sys.path.insert(0,'/home/claude/work/tools')
from cffrec import Rec
r=Rec.load(open(sys.argv[1],'rb').read()); I=r.inst
I.extend(b'\0'*((-len(I))%8)); a=len(I); I.extend(b'Multiplayer.atlas:Frame_Ink_Raph\0'); I.extend(b'\0'*((-len(I))%16))
c=[struct.unpack_from('<I',s,0)[0] for s in r.syms if s[8:s.find(b'\0',8)]==b'*Karai_HeroData*'][0]
k=[i for i,(x,y) in enumerate(r.ptrs) if x==c+0xA8][0]; r.ptrs[k]=(c+0xA8,a); r.ptrs.sort()
data=r.save(); open(sys.argv[2],'wb').write(data)
r2=Rec.load(data); J=bytes(r2.inst); t=dict(r2.ptrs)[c+0xA8]; print(J[t:J.find(b'\0',t)])
