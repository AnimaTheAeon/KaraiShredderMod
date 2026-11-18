import os
import sys, numpy as np; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pe import PE
_cache={}
def xrefs(path,target,extra=(0,1,4)):
    """rip-relative references to target: disp32 at k with next-ip = k+4+extra (extra=imm bytes after disp)"""
    if path not in _cache:
        p=PE(path); v,vs,o,ps=p.sec('.text'); b=np.frombuffer(p.d[o:o+ps],dtype=np.uint8)
        n=len(b)-4; d=(b[:n].astype(np.int64)|(b[1:n+1].astype(np.int64)<<8)|(b[2:n+2].astype(np.int64)<<16)|(b[3:n+3].astype(np.int64)<<24))
        d=np.where(d>=2**31,d-2**32,d); _cache[path]=(p,v,d)
    p,v,d=_cache[path]; vas=v+np.arange(len(d))
    res=set()
    for e in extra:
        res.update((vas[np.nonzero(vas+4+e+d==target)[0]]).tolist())
    return sorted(res)
def func_start(p,va,maxback=0x4000):
    """walk back to a likely function start: after int3/cc padding"""
    o=p.off(va)
    for k in range(o,o-maxback,-1):
        if p.d[k-1]==0xcc and p.d[k]!=0xcc: return p.va(k)
if __name__=='__main__':
    p=PE(sys.argv[1])
    for a in sys.argv[2:]:
        t=int(a,16); r=xrefs(sys.argv[1],t)
        print(a,[(hex(x),hex(func_start(p,x) or 0)) for x in r])
