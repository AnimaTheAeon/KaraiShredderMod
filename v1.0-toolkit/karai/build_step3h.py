# Step 3h: speed up Karai's tool animation nodes (all map to her boss ShurikenThrow clip, which has a long windup)
import sys,struct
sys.path.insert(0,'/home/claude/work/tools')
from cffrec import Rec
src,out,spd=sys.argv[1],sys.argv[2],float(sys.argv[3])
r=Rec.load(open(src,'rb').read()); I=r.inst; P=dict(r.ptrs)
cs=lambda a: bytes(I[a:I.find(b'\0',a)]).decode('latin1')
G=[struct.unpack_from('<I',s,0)[0] for s in r.syms if s[8:s.find(b'\0',8)]==b'*KaraiAnimGraphTuning*'][0]
n=0
for x,t in sorted(P.items()):
    if G<=x<0x16900 and cs(t).endswith('ShurikenThrow.anim') and x-0x18 in P and cs(P[x-0x18]).startswith('tool_'):
        assert abs(struct.unpack_from('<f',I,x+8)[0]-1.0)<1e-6
        struct.pack_into('<f',I,x+8,spd); n+=1; print(cs(P[x-0x18]))
assert n==16, n
open(out,'wb').write(r.save()); print('nodes',n,'speed',spd)
