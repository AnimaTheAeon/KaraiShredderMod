# Step 3t data: Karai-only red copies of Alopex's Inspiration CharSelect entries + Karai cards +0x108/+0x110
import sys,struct
sys.path.insert(0,'/home/claude/work/tools')
from cffrec import Rec
def sym_chunk(off,typ,name):
    b=struct.pack('<II',off,typ)+name.encode()+b'\0'; return b+b'\0'*((-len(b))%8)
ps_src,ps_out,ca_src,ca_out=sys.argv[1:5]
r=Rec.load(open(ps_src,'rb').read()); I=r.inst
def addstr(s):
    I.extend(b'\0'*((-len(I))%8)); a=len(I); I.extend(s.encode()+b'\0'); return a
syms={s[8:s.find(b'\0',8)].decode():struct.unpack_from('<II',s,0) for s in r.syms}
atl=addstr('build://Boss_Karai.atlas'); new={}
for k in (1,2):
    o,typ=syms['*PowerSelect_BroPower_Alopex_00%d_CharSelect*'%k]; n=0x90
    I.extend(b'\0'*((-len(I))%16)); c=len(I); I.extend(I[o:o+n])
    for x,t in [p for p in list(r.ptrs) if o<=p[0]<o+n]: r.ptrs.append((x-o+c, t-o+c if o<=t<o+n else t))
    sp=addstr('karai_insp%d'%k)
    r.ptrs=[(x,(atl if x==c+0x60 else sp if x==c+0x68 else t)) for x,t in r.ptrs]
    name='*PowerSelect_BroPower_Karai_00%d_CharSelect*'%k
    r.syms.append(sym_chunk(c,typ,name)); new[k]=name
I.extend(b'\0'*((-len(I))%16)); r.ptrs.sort()
data=r.save(); open(ps_out,'wb').write(data)
r2=Rec.load(data); J=bytes(r2.inst); D=dict(r2.ptrs); g=lambda a: J[D[a]:J.find(b'\0',D[a])].decode()
for s in r2.syms:
    nm=s[8:s.find(b'\0',8)].decode()
    if 'Karai' in nm: o=struct.unpack_from('<I',s,0)[0]; print(nm,[g(o+q) for q in (0,0x38,0x40,0x60,0x68)])
rc=Rec.load(open(ca_src,'rb').read()); K=rc.inst
def addk(s):
    K.extend(b'\0'*((-len(K))%8)); a=len(K); K.extend(s.encode()+b'\0'); return a
ka={1:addk(new[1]),2:addk(new[2])}; K.extend(b'\0'*((-len(K))%16))
cards=[struct.unpack_from('<I',s,0)[0] for s in rc.syms if s[8:s.find(b'\0',8)].startswith(b'*Karai_HeroData')]
idx={x:i for i,(x,t) in enumerate(rc.ptrs)}
for cd in cards:
    rc.ptrs[idx[cd+0x108]]=(cd+0x108,ka[1]); rc.ptrs[idx[cd+0x110]]=(cd+0x110,ka[2])
rc.ptrs.sort(); open(ca_out,'wb').write(rc.save()); print('cards',len(cards))
