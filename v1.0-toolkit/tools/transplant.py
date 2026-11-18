import sys,struct,re,json
sys.path.insert(0,'/home/claude/tools')
from cffrec import Rec
def cstr(b,o):
    e=b.find(b'\0',o); return b[o:e].decode('latin1')
def align(buf,a=16):
    buf+=b'\0'*((-len(buf))%a)
def add_string(r,s):
    align(r.inst,8); o=len(r.inst); r.inst+=s.encode()+b'\0'; return o
def put_inplace(r,off,old,new):
    assert r.inst[off:off+len(old)]==old.encode() and r.inst[off+len(old)]==0 and len(new)<=len(old)
    r.inst[off:off+len(old)+1]=new.encode()+b'\0'*(len(old)-len(new)+1)
def build(casey_raw,karai_raw,moves,drop):
    C=Rec.load(casey_raw); K=Rec.load(karai_raw)
    # 1) model + skeleton -> Karai (in place, as in the working build)
    for m in list(re.finditer(rb'build://Characters/NPCs/CaseyJones/Model/(CaseyJones(?:_Samurai|_Trenchcoat)?)\.(mesh|skeleton)\x00',bytes(C.inst))):
        put_inplace(C,m.start(),m.group()[:-1].decode(),'build://Characters/NPCs/Karai/Model/Karai.'+m.group(2).decode())
    # 2) append Karai data
    align(C.inst,16); B=len(C.inst); C.inst+=K.inst
    C.ptrs+= [(a+B,b+B) for a,b in K.ptrs]
    P=dict(C.ptrs); KP=dict(K.ptrs)
    # Karai slots by name (in shifted space)
    klist=KP[0x138]; kslots={}
    k=0
    while klist+8*k in KP:
        s=KP[klist+8*k]; kslots[cstr(K.inst,KP[s])]=s+B; k+=1
    # Casey list
    hero=0x108; clist=P[hero+0x138]; cs=[]; k=0
    while clist+8*k in P:
        s=P[clist+8*k]; cs.append((cstr(C.inst,P[s]),s)); k+=1
    newlist=[s for n,s in cs if n not in drop]
    # 3) wire Karai moves to hero inputs
    pi={a:i for i,(a,b) in enumerate(C.ptrs)}
    for kname,inp in moves:
        s=kslots[kname]
        so=add_string(C,inp)
        C.ptrs[pi[s+8]]=(s+8,so)          # repoint slot input string
        newlist.append(s)
    # 4) write new NULL-terminated list and repoint hero+0x138
    align(C.inst,8); L=len(C.inst)
    for i,s in enumerate(newlist):
        C.inst+=b'\0'*8; C.ptrs.append((L+8*i,s))
    C.inst+=b'\0'*8
    C.ptrs[pi[hero+0x138]]=(hero+0x138,L)
    align(C.inst,16)
    return C,[n for n,s in cs if n not in drop]
