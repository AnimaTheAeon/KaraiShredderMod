import sys,struct
sys.path.insert(0,'/home/claude/work/tools')
from cffrec import Rec
H={'Leo':'5ce5356c8aced125','Raph':'0e2ff051f6d864af','Don':'acc845ffeafb1213','Mikey':'3a041441f8385576','Casey':'5635aea195a4e11c','Metal':'458f5abb8371dc4c','Alopex':'1fe99fc5fb80dd9e','Slash':'7151a2967ae0d393'}
recs={}
for k,h in H.items():
    r=Rec.load(open('ovh/%s.bin'%h,'rb').read()); recs[k]=r
    syms=[]
    for s in r.syms:
        # parse (off,typehash,name)
        i=0
        while i+8<=len(s):
            off,th=struct.unpack_from('<II',s,i); j=s.find(b'\0',i+8)
            if j<0: break
            nm=s[i+8:j]; 
            if not nm.startswith(b'*'): break
            syms.append((off,hex(th),nm.decode())); i=(j+1+3)&~3
    print(k,len(r.inst),syms)
