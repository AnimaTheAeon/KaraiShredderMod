import struct,sys
def apply(src,patch,dst,reverse=False):
    d=bytearray(open(src,'rb').read()); p=open(patch,'rb').read()
    assert p[:4]==b'KPAT'; old,new,cnt=struct.unpack_from('<QQI',p,4); i=24
    for _ in range(cnt):
        off,ln=struct.unpack_from('<QI',p,i); i+=12
        nb=p[i:i+ln]; i+=ln; ob=p[i:i+ln]; i+=ln
        b=ob if reverse else nb
        if off+ln>len(d): d.extend(b'\0'*(off+ln-len(d)))
        d[off:off+ln]=b
    sz=old if reverse else new; del d[sz:]
    if len(d)<sz: d.extend(b'\0'*(sz-len(d)))
    open(dst,'wb').write(d)
def mk(old,new,out,gap=64):
    a=open(old,'rb').read(); b=open(new,'rb').read(); n=max(len(a),len(b))
    A=a.ljust(n,b'\0'); B=b.ljust(n,b'\0')
    import numpy as np
    x=np.frombuffer(A,np.uint8)!=np.frombuffer(B,np.uint8)
    idx=np.flatnonzero(x); ranges=[]
    if len(idx):
        s=idx[0]; e=idx[0]
        for k in idx[1:]:
            if k-e>gap: ranges.append((s,e+1)); s=k
            e=k
        ranges.append((s,e+1))
    out_b=bytearray(b'KPAT'+struct.pack('<QQI',len(a),len(b),len(ranges)))
    for s,e in ranges: out_b+=struct.pack('<QI',s,e-s)+B[s:e]+A[s:e]
    open(out,'wb').write(out_b); return len(ranges)
if __name__=='__main__':
    apply(sys.argv[1],sys.argv[2],sys.argv[3])
