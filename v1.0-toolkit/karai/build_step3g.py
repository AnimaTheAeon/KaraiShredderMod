# Step 3g: Karai's own copies of the Heckle/Kunai tool slots with inputs swapped,
# so her starting tool marker (Heckle, from Casey's lifetime buff) fires the Kunai ability.
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
lst=P[KACT+0x138]; slots=[]; k=0
while lst+8*k in P: slots.append(P[lst+8*k]); k+=1
starts=sorted(set(slots))
def size(s):
    nxt=[x for x in starts if x>s]; return (nxt[0]-s) if nxt else 0x158
SW={'Ability_Common_005_Heckle':'tool_common_7','Ability_Common_007_Kunai':'tool_common_5'}
done=[]
for k,s in enumerate(slots):
    nm=cs(P[s])
    if nm in SW:
        n=size(s); assert 0x150<=n<=0x200, hex(n)
        align(16); c=len(I); I.extend(I[s:s+n])
        for x,t in [p for p in list(r.ptrs) if s<=p[0]<s+n]:
            r.ptrs.append((x-s+c, t-s+c if s<=t<s+n else t))
        setptr(c+8, addstr(SW[nm]))
        setptr(lst+8*k, c); done.append((nm,hex(n)))
print(done); assert len(done)==2
align(16); r.ptrs.sort()
data=r.save(); open(out,'wb').write(data)
r2=Rec.load(data); D=dict(r2.ptrs); J=bytes(r2.inst); c2=lambda a: J[a:J.find(b'\0',a)].decode('latin1')
for who,act in (('Karai',KACT),('Casey',0x108)):
    l=D[act+0x138]; k=0; o=[]
    while l+8*k in D:
        s=D[l+8*k]; nm=c2(D[s])
        if 'Heckle' in nm or 'Kunai' in nm: o.append((nm,c2(D[s+8]),hex(s)))
        k+=1
    print(who,o)
