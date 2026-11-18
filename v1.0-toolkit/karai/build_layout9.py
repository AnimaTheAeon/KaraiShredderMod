import sys
d=bytearray(open(sys.argv[1],'rb').read())
def parse_elem(o):
    """returns end offset of element at o (index width 1)"""
    t=d[o]; o+=1
    nl=d[o]; o+=1+nl
    ac=d[o]; o+=1
    attrs=[]
    for _ in range(ac):
        aid=d[o]; ln=d[o+1]; attrs.append((aid,o+2,ln)); o+=2+ln
    c2=d[o]; o+=1
    for _ in range(c2):
        o+=1                     # property index
        e=parse_elem(o); o=e[0]  # property value element
    nch=(d[o]<<8)|d[o+1]; o+=2
    kids=[]
    for _ in range(nch):
        e=parse_elem(o); kids.append((o,e)); o=e[0] if isinstance(e,tuple) else e
    return (o,t,attrs,kids)
# locate the HORIZONTAL stack holding the portraits: find wrapper of SelectorPortrait_0
p0=d.find(b'SelectorPortrait_0')
stack=d.rfind(b'\x36\x00\x05',0,p0)
end,t,attrs,kids=parse_elem(stack)
print('stack type %x at %x, %d children, ends %x'%(t,stack,len(kids),end))
names=[]
for ko,ke in kids:
    s=bytes(d[ko:ke[0]]); i=s.find(b'SelectorPortrait_'); names.append((ko,ke[0],s[i:i+18] if i>=0 else b'-'))
for n in names: print(hex(n[0]),hex(n[1]),n[2])
w7=[n for n in names if n[2]==b'SelectorPortrait_7'][0]
el=bytearray(d[w7[0]:w7[1]])
# rebuild button attrs
_,wt,_,wk=parse_elem(w7[0]); bo=wk[0][0]; _,bt,battrs,_=parse_elem(bo)
newattrs=[]
for aid,ao,ln in battrs:
    v=bytes(d[ao:ao+ln])
    if v==b'7': v=b'8'
    elif v==b'SelectorPortrait_7': v=b'SP8'
    elif v.startswith(b'#') and len(v)==7: v=b'#b02a3a'
    elif v.startswith(b'build://Multiplayer:AvatarSelect_'): v=b'build://Multiplayer:AvatarSelect_Casey'
    newattrs.append(bytes([aid,len(v)])+v)
btn=bytes([bt,0,len(newattrs)])+b''.join(newattrs)+b'\x00\x00\x00'
wrap=bytes(d[w7[0]:bo])+btn
assert d[w7[0]:bo]==b'\x31\x00\x00\x00\x00\x01'
out=d[:w7[1]]+wrap+d[w7[1]:]
# bump child count (u16 BE right before first child)
fc=kids[0][0]; assert (out[fc-2]<<8|out[fc-1])==len(kids)
out[fc-2:fc]=bytes([(len(kids)+1)>>8,(len(kids)+1)&0xff])
open(sys.argv[2],'wb').write(out)
# verify reparse
d=out; e2,_,_,k2=parse_elem(stack); print('new children',len(k2),'stack end shift',e2-end, 'added',len(wrap))
print(wrap)
