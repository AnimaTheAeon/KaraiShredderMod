# Step 3o: Karai-only Kunai PowerSelect with a red icon.
#  - PowerSelect record 3d50408ab841b670: clone *PowerSelect_Ability_Common_007_Kunai* (0x90 bytes) as
#    *PowerSelect_Ability_Common_007_Kunai_Karai*, icon -> build://Boss_Karai.atlas : karai_kunai
#  - Casey record: Karai cards +0x100 (starting tool) -> the new PowerSelect
import sys,struct
sys.path.insert(0,'/home/claude/work/tools')
from cffrec import Rec
def sym_chunk(off,typ,name):
    b=struct.pack('<II',off,typ)+name.encode()+b'\0'; return b+b'\0'*((-len(b))%8)
ps_src,ps_out,ca_src,ca_out=sys.argv[1:5]
NEW='*PowerSelect_Ability_Common_007_Kunai_Karai*'
r=Rec.load(open(ps_src,'rb').read()); I=r.inst; P=dict(r.ptrs)
src=[struct.unpack_from('<II',s,0) for s in r.syms if s[8:s.find(b'\0',8)]==b'*PowerSelect_Ability_Common_007_Kunai*'][0]
o,typ=src; n=0x90
def addstr(s):
    I.extend(b'\0'*((-len(I))%8)); a=len(I); I.extend(s.encode()+b'\0'); return a
I.extend(b'\0'*((-len(I))%16)); c=len(I); I.extend(I[o:o+n])
for x,t in [p for p in list(r.ptrs) if o<=p[0]<o+n]:
    r.ptrs.append((x-o+c, t-o+c if o<=t<o+n else t))
at=addstr('build://Boss_Karai.atlas'); sp=addstr('karai_kunai'); I.extend(b'\0'*((-len(I))%16))
r.ptrs=[(x,(at if x==c+0x60 else sp if x==c+0x68 else t)) for x,t in r.ptrs]
r.ptrs.sort(); r.syms.append(sym_chunk(c,typ,NEW))
data=r.save(); open(ps_out,'wb').write(data)
r2=Rec.load(data); J=bytes(r2.inst); D=dict(r2.ptrs); g=lambda a: J[D[a]:J.find(b'\0',D[a])].decode()
print('clone',hex(c),[g(c+k) for k in (0,0x38,0x40,0x60,0x68)], 'syms',len(r2.syms))
# Karai cards
rc=Rec.load(open(ca_src,'rb').read()); K=rc.inst
K.extend(b'\0'*((-len(K))%8)); a=len(K); K.extend(NEW.encode()+b'\0'); K.extend(b'\0'*((-len(K))%16))
cards=[struct.unpack_from('<I',s,0)[0] for s in rc.syms if s[8:s.find(b'\0',8)].startswith(b'*Karai_HeroData')]
old=[]
for cd in cards:
    i=[j for j,(x,y) in enumerate(rc.ptrs) if x==cd+0x100][0]; old.append(bytes(K[rc.ptrs[i][1]:K.find(b'\0',rc.ptrs[i][1])])); rc.ptrs[i]=(cd+0x100,a)
rc.ptrs.sort(); open(ca_out,'wb').write(rc.save()); print('cards',len(cards),'was',old[0])
