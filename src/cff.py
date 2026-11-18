import os
import struct,sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hashes import lookup2
KEYS=[0x6e0da13b,0x50daa98f,0x2d5ffa4f,0x56c6c3eb,0xcad31ddd,0x04f7be6a,0xd5c4e961,0x7fe2ef92,0xccbb8a6d,0x19b6875b,0x433b604c,0xba7b1ee4,0x9dea872e,0xa8c2e10a,0xed30a2ff,0x16a8f9a4]
M=0xffffffff
rol=lambda x:((x<<1)|(x>>31))&M
def parse(raw):
    wrap=None
    if raw[:4]==b'RSC0': wrap=raw[:32]; raw=raw[32:]
    assert raw[:4]==b'CFF0'
    hdr=raw[:0x40]; i=0x40; ch=[]
    while i<len(raw):
        tag=raw[i:i+4]; ln=struct.unpack_from('<I',raw,i+4)[0]; ch.append([tag,raw[i+8:i+ln]]); i+=ln
        if ln==0: break
    return wrap,hdr,ch
def dec(body,key):
    n=len(body); h=lookup2(struct.pack('<I',KEYS[key]),n); prev=n; out=bytearray(body)
    for j in range(0,n-n%4,4):
        c=struct.unpack_from('<I',body,j)[0]; struct.pack_into('<I',out,j,rol(prev)^c^h); prev=c
    return bytes(out)
def enc(plain,key):
    n=len(plain); h=lookup2(struct.pack('<I',KEYS[key]),n); prev=n; out=bytearray(plain)
    for j in range(0,n-n%4,4):
        p=struct.unpack_from('<I',plain,j)[0]; c=rol(prev)^p^h; struct.pack_into('<I',out,j,c); prev=c
    return bytes(out)
def load(raw):
    wrap,hdr,ch=parse(raw); d={t:b for t,b in ch}; key=d[b'DEF0'][1]
    inst=dec(d[b'INST'],key)
    pt=d.get(b'PTCH',b''); ptrs=[]
    if pt:
        cnt=struct.unpack_from('<I',pt,0)[0]; ptrs=[struct.unpack_from('<II',pt,8+8*k) for k in range(cnt)]
    syms=[]
    for t,sy in ch:
        if t!=b'SYMB': continue
        off,th=struct.unpack_from('<II',sy,0); e=sy.find(b'\0',8); syms.append((off,th,sy[8:e].decode('latin1')))
    return dict(wrap=wrap,hdr=hdr,chunks=ch,key=key,inst=inst,ptrs=ptrs,syms=syms)
