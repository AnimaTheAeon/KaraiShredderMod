import struct
from cff import KEYS,lookup2,decrypt_with,encrypt_with
def _chunks(d):
    i=0x40; out=[]
    while i+8<=len(d):
        tag=d[i:i+4]; n=struct.unpack_from('<I',d,i+4)[0]
        if n<8 or not tag.isalnum(): break
        out.append((tag,i,n)); i+=n
    return out
class Rec:
    @classmethod
    def load(cls,raw):
        r=cls(); r.wrap=None; d=raw
        if d[:4]==b'RSC0': r.wrap=d[:32]; d=d[32:]
        r.hdr=bytearray(d[:0x40]); r.order=[]; r.syms=[]; r.extra=[]
        for tag,i,n in _chunks(d):
            body=d[i+8:i+n]; r.order.append(tag)
            if tag==b'DEF0': r.def0=body
            elif tag==b'INST':
                r.keyidx=r.def0[1]
                r.inst=bytearray(decrypt_with(body,lookup2(struct.pack('<I',KEYS[r.keyidx]),len(body))))
            elif tag==b'PTCH':
                cnt=struct.unpack_from('<I',body,0)[0]; r.ptch_hdr=body[4:8]
                r.ptrs=[struct.unpack_from('<II',body,8+k*8) for k in range(cnt)]
                r.ptch_pad=len(body)-(8+cnt*8)
            elif tag==b'SYMB': r.syms.append(body)
            else: r.extra.append((tag,body))
        r.tail=d[sum(n for _,_,n in _chunks(d))+0x40:]
        return r
    def _chunk(self,tag,body):
        return tag+struct.pack('<I',len(body)+8)+body
    def save(self):
        n=len(self.inst)
        enc=encrypt_with(bytes(self.inst),lookup2(struct.pack('<I',KEYS[self.keyidx]),n))
        pt=struct.pack('<I',len(self.ptrs))+self.ptch_hdr+b''.join(struct.pack('<II',a,b) for a,b in self.ptrs)
        pt+=b'\0'*((-(len(pt)+8))%16) if self.ptch_pad else b''
        out=b''
        for tag in self.order:
            if tag==b'DEF0': out+=self._chunk(tag,self.def0)
            elif tag==b'INST': out+=self._chunk(tag,enc)
            elif tag==b'PTCH': out+=self._chunk(tag,pt)
        for s in self.syms: out+=self._chunk(b'SYMB',s)
        for t,b in self.extra: out+=self._chunk(t,b)
        hdr=bytearray(self.hdr); body=bytes(hdr[:0x40])+out+self.tail
        struct.pack_into('<I',hdr,4,len(body)); body=bytes(hdr)+out+self.tail
        if self.wrap:
            w=bytearray(self.wrap); struct.pack_into('<II',w,4,len(body),len(body)); return bytes(w)+body
        return body
