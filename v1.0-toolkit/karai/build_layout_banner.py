# Add a 9th child (Karai, index 8) to the STACK_ONE bound to TurtleCharacter that holds the Window_Banner_<Hero> images: a copy of Raph's (red)
import sys
d=bytearray(open(sys.argv[1],'rb').read())
exec(open('/home/claude/work/build_layout9.py').read().split('# locate the HORIZONTAL')[0].split('d=bytearray')[0])
def parse_elem(o, d=d):
    t=d[o]; o+=1; nl=d[o]; o+=1+nl; ac=d[o]; o+=1; attrs=[]
    for _ in range(ac):
        aid=d[o]; ln=d[o+1]; attrs.append((aid,o+2,ln)); o+=2+ln
    c2=d[o]; o+=1
    for _ in range(c2): o+=1; o=parse_elem(o,d)[0]
    nch=(d[o]<<8)|d[o+1]; o+=2; kids=[]
    for _ in range(nch):
        e=parse_elem(o,d); kids.append((o,e)); o=e[0]
    return (o,t,attrs,kids)
i=d.find(b'Window_Banner_Mike')
# walk back to find the STACK_ONE element containing it: try candidate starts whose parse covers i with 8 banner kids
best=None
for s in range(i-1, i-400, -1):
    try: e=parse_elem(s)
    except Exception: continue
    end,t,attrs,kids=e
    if end>i and len(kids)==8 and all(b'Window_Banner_' in bytes(d[k[0]:k[1][0]]) for k in kids): best=(s,e); break
assert best, 'stack not found'
s,(end,t,attrs,kids)=best
print('stack at %x type %x kids %d'%(s,t,len(kids)), [bytes(d[k[0]:k[1][0]]).split(b'Window_Banner_')[1][:6] for k in kids])
raph=[k for k in kids if b'Window_Banner_Raph' in bytes(d[k[0]:k[1][0]])][0]
el=bytes(d[raph[0]:raph[1][0]]).replace(b'\r\x04true',b'\r\x05false')   # same visibility default as the non-first children
out=d[:end]+el+d[end:]
fc=kids[0][0]; assert (out[fc-2]<<8|out[fc-1])==8
out[fc-2:fc]=bytes([0,9])
e2=parse_elem(s,out); print('new kids',len(e2[3]),'added',len(el))
# sanity: whole document still parses from root
r=parse_elem(0,out) if out[0]!=0x55 else None
open(sys.argv[2],'wb').write(out)
