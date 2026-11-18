import struct,re
def chunks(d):
    i=0x40; out=[]
    while i+8<=len(d):
        tag=d[i:i+4]; n=struct.unpack_from('<I',d,i+4)[0]
        if n<8 or not tag.isalnum(): break
        out.append((tag.decode(),i,n)); i+=n
    return out
def syms(d):
    res=[]
    for tag,i,n in chunks(d):
        if tag=='SYMB':
            body=d[i+8:i+n]; m=re.search(rb'\*([A-Za-z0-9_]+)\*',body)
            res.append((i,body[:m.start()].hex() if m else body[:16].hex(), m.group(1).decode() if m else None))
    return res
def load(f):
    d=open(f,'rb').read(); ch={t:(i,n) for t,i,n in chunks(d)}
    i,n=ch['INST']; inst=d[i+8:i+n]
    pi,pn=ch['PTCH']; p=d[pi+8:pi+pn]; cnt=struct.unpack_from('<I',p,0)[0]
    ptr={}
    for k in range(cnt):
        a,b=struct.unpack_from('<II',p,8+k*8); ptr[a]=b
    return d,inst,ptr
def cstr(inst,o):
    e=inst.find(b'\0',o); s=inst[o:e]
    return s.decode('latin1') if 0<len(s)<200 and all(32<=c<127 for c in s) else None
