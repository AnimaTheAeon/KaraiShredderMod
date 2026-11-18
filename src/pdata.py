import os
import sys, struct, bisect; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pe import PE
_c={}
def funcs(path):
    if path in _c: return _c[path]
    p=PE(path); pe=p.pe; d=pe.OPTIONAL_HEADER.DATA_DIRECTORY[3]
    o=p.off(p.base+d.VirtualAddress); n=d.Size//12; F=[]
    for i in range(n):
        b,e,u=struct.unpack_from('<III',p.d,o+12*i)
        if b: F.append((p.base+b,p.base+e))
    F.sort(); _c[path]=(F,[f[0] for f in F]); return _c[path]
def func_of(path,va):
    F,S=funcs(path); i=bisect.bisect_right(S,va)-1
    if i>=0 and F[i][0]<=va<F[i][1]: return F[i]
    return None
