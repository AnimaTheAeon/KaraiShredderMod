import struct
M=0xffffffff
KEYS=[0x6e0da13b,0x50daa98f,0x2d5ffa4f,0x56c6c3eb,0xcad31ddd,0x4f7be6a,0xd5c4e961,0x7fe2ef92,0xccbb8a6d,0x19b6875b,0x433b604c,0xba7b1ee4,0x9dea872e,0xa8c2e10a,0xed30a2ff,0x16a8f9a4]
def mix(a,b,c):
    a=(a-b-c)&M;a^=c>>13; b=(b-c-a)&M;b^=(a<<8)&M; c=(c-a-b)&M;c^=b>>13
    a=(a-b-c)&M;a^=c>>12; b=(b-c-a)&M;b^=(a<<16)&M; c=(c-a-b)&M;c^=b>>5
    a=(a-b-c)&M;a^=c>>3;  b=(b-c-a)&M;b^=(a<<10)&M; c=(c-a-b)&M;c^=b>>15
    return a,b,c
def lookup2(k,init):
    a=b=0x9e3779b9;c=init;L=len(k);i=0
    while L-i>=12:
        a=(a+struct.unpack_from('<I',k,i)[0])&M;b=(b+struct.unpack_from('<I',k,i+4)[0])&M;c=(c+struct.unpack_from('<I',k,i+8)[0])&M
        a,b,c=mix(a,b,c);i+=12
    c=(c+len(k))&M; r=k[i:]
    for j,ch in enumerate(r):
        if j<4: a=(a+(ch<<(8*j)))&M
        elif j<8: b=(b+(ch<<(8*(j-4))))&M
        else: c=(c+(ch<<(8*(j-7))))&M
    return mix(a,b,c)[2]
def crypt(buf,key,decrypt=True):
    n=len(buf); h=lookup2(struct.pack('<I',key),n); prev=n; out=bytearray(buf)
    for i in range(0,n//4*4,4):
        w=struct.unpack_from('<I',buf,i)[0]
        if decrypt:
            p=(((prev<<1)|(prev>>31))&M)^w^h; prev=w
        else:
            p=(((prev<<1)|(prev>>31))&M)^w^h; prev=p   # p is ciphertext
        struct.pack_into('<I',out,i,p)
    return bytes(out)
def inst(d):
    i=d.find(b'INST'); n=struct.unpack_from('<I',d,i+4)[0]; return i, d[i+8:i+n]
import collections
def decrypt_auto(buf):
    n=len(buf); prev=n; raw=[]
    for i in range(0,n//4*4,4):
        w=struct.unpack_from('<I',buf,i)[0]; raw.append((((prev<<1)|(prev>>31))&M)^w); prev=w
    h=collections.Counter(raw).most_common(1)[0][0]
    out=bytearray(buf)
    for k,x in enumerate(raw): struct.pack_into('<I',out,k*4,x^h)
    return bytes(out),h
def encrypt_with(plain,h):
    n=len(plain); prev=n; out=bytearray(plain)
    for i in range(0,n//4*4,4):
        p=struct.unpack_from('<I',plain,i)[0]; c=(((prev<<1)|(prev>>31))&M)^p^h
        struct.pack_into('<I',out,i,c); prev=c
    return bytes(out)
def decrypt_with(buf,h):
    n=len(buf); prev=n; out=bytearray(buf)
    for i in range(0,n//4*4,4):
        w=struct.unpack_from('<I',buf,i)[0]; struct.pack_into('<I',out,i,(((prev<<1)|(prev>>31))&M)^w^h); prev=w
    return bytes(out)
