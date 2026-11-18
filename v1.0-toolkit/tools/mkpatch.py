import struct,hashlib,numpy as np,sys
def mkpatch(old_path,new_path,out_path,gap=256):
    a=open(old_path,'rb').read(); b=open(new_path,'rb').read()
    L=max(len(a),len(b)); A=np.zeros(L,np.uint8); B=np.zeros(L,np.uint8)
    A[:len(a)]=np.frombuffer(a,np.uint8); B[:len(b)]=np.frombuffer(b,np.uint8)
    d=np.nonzero(A!=B)[0]; rng=[]
    if len(d):
        s=p=int(d[0])
        for x in d[1:]:
            x=int(x)
            if x-p>gap: rng.append((s,p+1)); s=x
            p=x
        rng.append((s,p+1))
    with open(out_path,'wb') as f:
        f.write(b'KPAT'+struct.pack('<QQI',len(a),len(b),len(rng)))
        for s,e in rng:
            f.write(struct.pack('<QI',s,e-s)); f.write(B[s:e].tobytes()); f.write(A[s:e].tobytes())
    return len(rng),sum(e-s for s,e in rng),hashlib.sha1(a).hexdigest().upper(),hashlib.sha1(b).hexdigest().upper()
def apply(path_bytes,patch,reverse=False):
    d=bytearray(path_bytes); p=open(patch,'rb').read(); o,n,c=struct.unpack_from('<QQI',p,4); i=24
    for _ in range(c):
        s,l=struct.unpack_from('<QI',p,i); i+=12; new=p[i:i+l]; old=p[i+l:i+2*l]; i+=2*l
        src=old if reverse else new
        if len(d)<s+l: d+=b'\0'*(s+l-len(d))
        d[s:s+l]=src
    t=(o if reverse else n)
    if len(d)<t: d+=b'\0'*(t-len(d))
    del d[t:]
    return bytes(d)
