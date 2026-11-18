import sys,struct
sys.path.insert(0,'/home/claude/work/tools')
from cffrec import Rec
src,out=sys.argv[1:3]
r=Rec.load(open(src,'rb').read()); I=r.inst
def align(a=16): I.extend(b'\0'*((-len(I))%a))
def addstr(s): align(8); a=len(I); I.extend(s.encode()+b'\0'); return a
def setptr(a,t):
    for k,(x,y) in enumerate(r.ptrs):
        if x==a: r.ptrs[k]=(a,t); return
    r.ptrs.append((a,t))
cs=lambda a: bytes(I[a:I.find(b'\0',a)]).decode('latin1')
KACT=[struct.unpack_from('<I',s,0)[0] for s in r.syms if s[8:s.find(b'\0',8)]==b'*Karai_Hero*'][0]
P=dict(r.ptrs)
# Kunai/tool fix: actor's own name
setptr(KACT+0x1d8, addstr('Karai_Hero'))
# clone moves with Karai names
REN={'CaseyJones_Attack_Chain':'CKarai_Attack_Chain','CaseyJones_Attack_Chain1':'CKarai_Attack_Chain1','CaseyJones_Attack_Chain2':'CKarai_Attack_Chain2',
     'CaseyJones_Attack_Chain3':'CKarai_Attack_Chain3','CaseyJones_DashAttack':'CKarai_DashAttack','Turtle_Hit_Reaction':'Karai_Hit_Reaction','Turtle_Stun':'Karai_Stun'}
lst=P[KACT+0x138]; k=0; done=[]
while lst+8*k in P:
    s=P[lst+8*k]; nm=cs(P[s])
    if nm in REN:
        align(16); c=len(I); I.extend(I[s:s+0x150])
        for x,t in [p for p in list(r.ptrs) if s<=p[0]<s+0x150]: r.ptrs.append((x-s+c,t))
        setptr(c, addstr(REN[nm]))           # new name -> new registry entry; input (+8) unchanged
        setptr(lst+8*k, c); done.append(nm)
    k+=1
assert sorted(done)==sorted(REN), done
align(16); r.ptrs.sort()
data=r.save(); open(out,'wb').write(data)
r2=Rec.load(data); D=dict(r2.ptrs); J=bytes(r2.inst); c2=lambda a: J[a:J.find(b'\0',a)].decode('latin1')
lst=D[KACT+0x138]; k=0; names=[]
while lst+8*k in D: s=D[lst+8*k]; names.append((c2(D[s]), c2(D[s+8]) if s+8 in D else '')); k+=1
print('ok',len(data),'actor name',c2(D[KACT+0x1d8]))
print([n for n in names if n[0].startswith(('Karai','CKarai')) or 'Turtle_' in n[0]])
# Casey untouched?
cl=D[0x108+0x138]; print('casey first combo', c2(D[D[cl+8*14]]))
