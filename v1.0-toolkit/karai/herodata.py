import sys,struct
sys.path.insert(0,'/home/claude/work/tools')
from cffrec import Rec
H={'Leo':('5ce5356c8aced125',1256),'Raph':('0e2ff051f6d864af',1256),'Don':('acc845ffeafb1213',1256),'Mikey':('3a041441f8385576',1256),'Casey':('5635aea195a4e11c',760),'Metal':('458f5abb8371dc4c',760),'Alopex':('1fe99fc5fb80dd9e',2248),'Slash':('7151a2967ae0d393',1752)}
def s_at(inst,o):
    e=inst.find(b'\0',o); return inst[o:e].decode('latin1')
rows={}
for k,(h,base) in H.items():
    r=Rec.load(open('ovh/%s.bin'%h,'rb').read()); P=dict(r.ptrs); inst=bytes(r.inst)
    row=[]
    for off in range(0,280,4):
        a=base+off
        if a in P:
            t=P[a]; s=s_at(inst,t)
            row.append(('P',s[:48] if s and s.isprintable() else '->%x'%t))
        elif a-4 in P: row.append(('',''))
        else:
            v=struct.unpack_from('<I',inst,a)[0]; f=struct.unpack_from('<f',inst,a)[0]
            row.append(('v','%d/%.3g'%(v,f) if v and abs(f)>1e-4 and abs(f)<1e6 else str(v) if v<100000 else hex(v)))
    rows[k]=row
for i in range(70):
    vals=[rows[k][i][1] for k in H]
    if any(vals) and len(set(vals))>=1:
        print('%03x'%(i*4),' | '.join('%-22s'%v[:22] for v in vals))
