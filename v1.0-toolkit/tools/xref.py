import pefile,struct,re,functools
P='/mnt/user-data/outputs/TMNTSF.exe.original-backup'
pe=pefile.PE(P,fast_load=True); D=pe.__data__; BASE=pe.OPTIONAL_HEADER.ImageBase
T=[s for s in pe.sections if s.Name.startswith(b'.text')][0]; T0=T.PointerToRawData; TV=T.VirtualAddress; TB=D[T0:T0+T.SizeOfRawData]
import numpy as np
_tb=np.frombuffer(TB,dtype=np.uint8)
def va_of_off(o): return BASE+pe.get_rva_from_offset(o)
def str_va(s):
    b=s.encode()+b'\0'; res=[]
    for m in re.finditer(re.escape(b),D):
        if m.start()==0 or D[m.start()-1]==0: res.append(va_of_off(m.start()))
    return res
@functools.lru_cache(None)
def _cands():
    idx=np.nonzero((_tb[1:-6]==0x8d)&((_tb[:-7]==0x48)|(_tb[:-7]==0x4c)))[0]
    disp=np.frombuffer(TB,dtype=np.uint8)
    d32=np.array([struct.unpack_from('<i',TB,i+3)[0] for i in idx],dtype=np.int64)
    tgt=TV+idx+7+d32
    return idx,tgt
def lea_refs(va):
    idx,tgt=_cands(); rva=va-BASE
    return [BASE+TV+int(i) for i in idx[tgt==rva]]
import bisect as _bis
_P=[s for s in pe.sections if s.Name.startswith(b'.pdata')][0]
_pd=D[_P.PointerToRawData:_P.PointerToRawData+_P.Misc_VirtualSize]
FUNCS=sorted({struct.unpack_from('<I',_pd,i)[0] for i in range(0,len(_pd)-11,12) if struct.unpack_from('<I',_pd,i)[0]})
FEND={}
for i in range(0,len(_pd)-11,12):
    b,e,u=struct.unpack_from('<III',_pd,i)
    if b: FEND[b]=max(FEND.get(b,0),e)
def func_of(va):
    r=va-BASE; i=_bis.bisect_right(FUNCS,r)-1; return BASE+FUNCS[i]
def call_refs(target):
    tb=_tb; idx=np.nonzero(tb[:-5]==0xe8)[0]
    d=np.frombuffer(TB[1:],dtype=np.uint8)
    disp=np.array([0]*len(idx),dtype=np.int64)
    raw=np.lib.stride_tricks.sliding_window_view(_tb,5)[idx][:,1:].copy().view('<i4').ravel().astype(np.int64)
    t=BASE+TV+idx+5+raw; return [BASE+TV+int(i) for i in idx[t==target]]
def ptr_refs(target):
    p=struct.pack('<Q',target); return [va_of_off(m.start()) for m in re.finditer(re.escape(p),D)]
