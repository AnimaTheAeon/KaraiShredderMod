# Step 3q: Kunai via input swap again (spawn hook removed in exe), and custom HUD icons for Karai via ability-slot
# fields +0x18 (atlas name, used as build://<x>.atlas), +0x20/+0x28 (sprite names) read by the HUD icon chooser 0x140683650.
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
P=dict(r.ptrs); cs=lambda a: bytes(I[a:I.find(b'\0',a)]).decode('latin1')
act={s[8:s.find(b'\0',8)]:struct.unpack_from('<I',s,0)[0] for s in r.syms}
KACT=act[b'*Karai_Hero*']; CACT=act[b'*CaseyJones_Hero*']
def slots(a):
    l=P[a+0x138]; out=[]; k=0
    while l+8*k in P: out.append((l+8*k,P[l+8*k])); k+=1
    return out
casey=set(s for _,s in slots(CACT)); allstarts=sorted(set(s for _,s in slots(KACT))|casey)
def size(s):
    nx=[x for x in allstarts if x>s]; n=(nx[0]-s) if nx else 0x158; return n if 0x150<=n<=0x200 else 0x158
def clone(s):
    n=size(s); align(16); c=len(I); I.extend(I[s:s+n])
    for x,t in [p for p in list(r.ptrs) if s<=p[0]<s+n]: r.ptrs.append((x-s+c, t-s+c if s<=t<s+n else t))
    return c
ATL=addstr('Boss_Karai')
SPR={k:addstr(k) for k in ('karai_special','karai_dash','karai_kunai')}
INP={k:addstr(k) for k in ('tool_common_5','tool_common_7')}
done=[]
for li,s in slots(KACT):
    n=cs(P[s]); want=None
    if n=='Karai_Cleave': want=('karai_special',None)
    elif n=='Mobility_001_Dash': want=('karai_dash',None)
    elif n=='Ability_Common_007_Kunai': want=('karai_kunai','tool_common_5')    # Kunai answers the Heckle marker's input
    elif n=='Ability_Common_005_Heckle': want=('karai_kunai','tool_common_7')
    if not want: continue
    if s in casey: c=clone(s); setptr(li,c); s2=c; tag='cloned'
    else: s2=s; tag='own'
    setptr(s2+0x18,ATL); setptr(s2+0x20,SPR[want[0]]); setptr(s2+0x28,SPR[want[0]])
    if want[1]: setptr(s2+8,INP[want[1]])
    done.append((n,tag,want))
align(16); r.ptrs.sort()
data=r.save(); open(out,'wb').write(data)
r2=Rec.load(data); J=bytes(r2.inst); D=dict(r2.ptrs); g=lambda a: J[D[a]:J.find(b'\0',D[a])].decode() if a in D else None
def show(a):
    l=D[a+0x138]; k=0; o=[]
    while l+8*k in D:
        s=D[l+8*k]; n=g(s)
        if n in ('Karai_Cleave','Mobility_001_Dash','Ability_Common_007_Kunai','Ability_Common_005_Heckle'): o.append((n,g(s+8),g(s+0x18),g(s+0x20)))
        k+=1
    return o
for d in done: print(d)
print('KARAI',show(KACT)); print('CASEY',show(CACT))
