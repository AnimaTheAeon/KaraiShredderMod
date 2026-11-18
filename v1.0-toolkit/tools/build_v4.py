import sys,json,struct,re
sys.path.insert(0,'/home/claude/tools')
from cffrec import Rec
from transplant import build, add_string, put_inplace, align
def cs(I,o): e=I.find(b'\0',o); return I[o:e].decode('latin1')
drop={'CaseyJones_Special'}
moves=[('Karai_Cleave','special')]
craw=open('/home/claude/out/overhead/5635aea195a4e11c.bin','rb').read()
C,_=build(craw,open('/home/claude/out/overhead/1c12a84b01339d4c.bin','rb').read(),moves,drop)
P=dict(C.ptrs); I=C.inst
# locate the hero's new slots
L=P[0x108+0x138]; k=0; slot={}
while L+8*k in P: s=P[L+8*k]; slot[cs(I,P[s])]=s; k+=1
# reference values from Casey's original slots (same offsets in the original part of the record)
O=Rec.load(craw); OP=dict(O.ptrs); OL=OP[0x108+0x138]; k=0; oslot={}
while OL+8*k in OP: s=OP[OL+8*k]; oslot[cs(O.inst,OP[s])]=s; k+=1
def copy_fields(dst,src_rec,src,ranges):
    for a,b in ranges: I[dst+a:dst+b]=src_rec.inst[src+a:src+b]
chain=oslot['CaseyJones_Attack_Chain1']; spec=oslot['CaseyJones_Special']
for n in ():
    copy_fields(slot[n],O,chain,[(0x48,0x60),(0xe0,0xe8),(0xf8,0x100)])
copy_fields(slot['Karai_Cleave'],O,spec,[(0x48,0x60),(0xe0,0xe8),(0xf8,0x100)])
# starting tool: Heckle -> Kunai (in place, shorter)
for m in re.finditer(rb'\*PowerSelect_Ability_Common_005_Heckle\*\x00',bytes(I)):
    put_inplace(C,m.start(),'*PowerSelect_Ability_Common_005_Heckle*','*PowerSelect_Ability_Common_007_Kunai*')
hero=C.save()
# ---- anim graph: v1 + cloned nodes for boss slot names
A=Rec.load(open('/home/claude/out/overhead/84e188b8ea515d94.bin','rb').read())
for a,o,n in json.load(open('/home/claude/animplan.json')):
    assert A.inst[a:a+len(o)]==o.encode(); A.inst[a:a+len(o)+1]=n.encode()+b'\0'*(len(o)-len(n)+1)
AP=dict(A.ptrs); arr=AP[0x8]; nodes=[]; k=0
while arr+8*k in AP: nodes.append(AP[arr+8*k]); k+=1
have={cs(A.inst,AP[n]) for n in nodes}
tmpl=[n for n in nodes if cs(A.inst,AP[n])=='attack_combo1'][0]
loop_tmpl=[n for n in nodes if cs(A.inst,AP[n])=='ability_dash'][0]
amap=json.load(open('/home/claude/karai_animmap.json'))
added=[]
for name,path in amap.items():
    if name in have or name.startswith('Karai_'): continue
    t=loop_tmpl if name.endswith('_loop') else tmpl
    align(A.inst,16); N=len(A.inst); A.inst+=A.inst[t:t+0x40]
    for a,b in list(A.ptrs):
        if t<=a<t+0x40: A.ptrs.append((a-t+N,b))
    pi={a:i for i,(a,b) in enumerate(A.ptrs)}
    so=add_string(A,name); po=add_string(A,path)
    A.ptrs[pi[N]]=(N,so); A.ptrs[pi[N+0x18]]=(N+0x18,po)
    nodes.append(N); added.append(name)
align(A.inst,8); NA=len(A.inst)
for i,n in enumerate(nodes): A.inst+=b'\0'*8; A.ptrs.append((NA+8*i,n))
A.inst+=b'\0'*8
pi={a:i for i,(a,b) in enumerate(A.ptrs)}; A.ptrs[pi[0x8]]=(0x8,NA); align(A.inst,16)
graph=A.save()
open('/home/claude/mod/5635aea195a4e11c.bin','wb').write(hero); open('/home/claude/mod/84e188b8ea515d94.bin','wb').write(graph)
# verify
R=Rec.load(graph); RP=dict(R.ptrs); a=RP[0x8]; k=0; names=[]
while a+8*k in RP: n=RP[a+8*k]; names.append((cs(R.inst,RP[n]),cs(R.inst,RP[n+0x18]).split('/')[-1])); k+=1
print('anim nodes',len(names),'added',added)
H=Rec.load(hero); HP=dict(H.ptrs); print('tool kunai present', b'*PowerSelect_Ability_Common_007_Kunai*' in H.inst)
for n in ('Karai_Cleave',):
    s=slot[n]; print(n, struct.unpack_from('<ff',H.inst,s+0x50), H.inst[s+0xe4:s+0xe8].hex(), H.inst[s+0xf8:s+0xfa].hex())
