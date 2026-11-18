import re,sys
want={int(x,16) for x in sys.argv[1:]}
cur=None; prev=None; hits={}
pat=re.compile(r'\[rip ([+-]) 0x([0-9a-f]+)\]')
lines=open('/home/claude/full.dis')
buf=[]
for l in lines:
    if l.startswith('F '): cur=l[2:].strip(); prev=None; continue
    sp=l.split(' ',1)
    if len(sp)<2: continue
    a=int(sp[0],16)
    if prev:
        pa,pins=prev; m=pat.search(pins)
        if m:
            t=a+(1 if m[1]=='+' else -1)*int(m[2],16)
            if t in want: hits.setdefault(hex(t),[]).append((cur,hex(pa),pins.strip()))
    prev=(a,sp[1])
for k,v in hits.items():
    print(k,len(v))
    for x in v[:60]: print('  ',x)
