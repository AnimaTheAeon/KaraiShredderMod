import xxhash,mmh3,struct
M32=0xffffffff; M64=2**64-1
def mix(a,b,c):
    a=(a-b-c)&M32; a^=c>>13
    b=(b-c-a)&M32; b^=(a<<8)&M32
    c=(c-a-b)&M32; c^=b>>13
    a=(a-b-c)&M32; a^=c>>12
    b=(b-c-a)&M32; b^=(a<<16)&M32
    c=(c-a-b)&M32; c^=b>>5
    a=(a-b-c)&M32; a^=c>>3
    b=(b-c-a)&M32; b^=(a<<10)&M32
    c=(c-a-b)&M32; c^=b>>15
    return a,b,c
def lookup2(k,initval=0):
    a=b=0x9e3779b9; c=initval; n=len(k); L=n; i=0
    while L>=12:
        a=(a+struct.unpack_from('<I',k,i)[0])&M32; b=(b+struct.unpack_from('<I',k,i+4)[0])&M32; c=(c+struct.unpack_from('<I',k,i+8)[0])&M32
        a,b,c=mix(a,b,c); i+=12; L-=12
    c=(c+n)&M32; r=k[i:]
    sh=[(2,10,24),(2,9,16),(2,8,8),(1,7,24),(1,6,16),(1,5,8),(1,4,0),(0,3,24),(0,2,16),(0,1,8),(0,0,0)]
    abc=[a,b,c]
    for idx,pos,s in sh:
        if L>pos:
            abc[idx if idx!=2 else 2]=(abc[idx]+(r[pos]<<s))&M32
    # note: for c, byte 8 is not added (c low byte reserved for length) -> pos 10,9,8 shift 24,16,8
    a,b,c=mix(*abc); return c
def fnv1a64(b):
    h=0xcbf29ce484222325
    for x in b: h=((h^x)*0x100000001b3)&M64
    return h
def fnv1a32(b):
    h=0x811c9dc5
    for x in b: h=((h^x)*0x1000193)&M32
    return h
def allh(b):
    out={}
    out['xxh64']=xxhash.xxh64_intdigest(b); out['xxh3']=xxhash.xxh3_64_intdigest(b)
    out['mmh3_64a']=mmh3.hash64(b,signed=False)[0]; out['mmh3_64b']=mmh3.hash64(b,signed=False)[1]
    out['fnv1a64']=fnv1a64(b)
    l0=lookup2(b,0); l1=lookup2(b,0x12345678)
    out['lk']=(l0<<32)|l1; out['lk_r']=(l1<<32)|l0
    out['fnv32x2']=(fnv1a32(b)<<32)
    return out
