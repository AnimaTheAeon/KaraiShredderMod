"""KPAT apply/make. Format: 'KPAT', u64 old, u64 new, u32 n, then n x (u64 off, u32 len, new[len], old[len]).
apply(fwd) writes new then truncates/zero-extends to new size (like PowerShell SetLength)."""
import struct, sys
def parse(p):
    d=open(p,'rb').read(); assert d[:4]==b'KPAT'
    o,n,c=struct.unpack_from('<QQI',d,4); p=24; R=[]
    for _ in range(c):
        off,l=struct.unpack_from('<QI',d,p); p+=12; R.append((off,d[p:p+l],d[p+l:p+2*l])); p+=2*l
    return o,n,R
def apply(data,patch,reverse=False):
    o,n,R=parse(patch); b=bytearray(data); want=o if reverse else n
    for off,new,old in R:
        src=old if reverse else new
        if len(b)<off+len(src): b.extend(b'\0'*(off+len(src)-len(b)))
        b[off:off+len(src)]=src
    if len(b)<want: b.extend(b'\0'*(want-len(b)))
    del b[want:]; return bytes(b)
def make(a,b,gap=16):
    R=[]; L=max(len(a),len(b)); A=a.ljust(L,b'\0'); B=b.ljust(L,b'\0'); i=0
    while i<L:
        if A[i]!=B[i]:
            j=i
            while j<L:
                if A[j]!=B[j]: j+=1; continue
                k=j
                while k<L and k-j<gap and A[k]==B[k]: k+=1
                if k<L and k-j<gap: j=k; continue
                break
            R.append((i,B[i:j],A[i:j])); i=j
        else: i+=1
    out=bytearray(b'KPAT'+struct.pack('<QQI',len(a),len(b),len(R)))
    for off,new,old in R: out+=struct.pack('<QI',off,len(new))+new+old
    return bytes(out)
if __name__=='__main__':
    cmd,src,patch,dst=sys.argv[1:5]
    open(dst,'wb').write(apply(open(src,'rb').read(),patch,cmd=='rev'))
