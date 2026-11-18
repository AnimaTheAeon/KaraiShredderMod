import pefile, struct, capstone, bisect
class PE:
    def __init__(s,p):
        s.pe=pefile.PE(p,fast_load=True); s.d=open(p,'rb').read(); s.base=s.pe.OPTIONAL_HEADER.ImageBase
        s.secs=[(x.VirtualAddress,x.Misc_VirtualSize,x.PointerToRawData,x.SizeOfRawData,x.Name.rstrip(b'\0').decode()) for x in s.pe.sections]
        s.md=capstone.Cs(capstone.CS_ARCH_X86,capstone.CS_MODE_64); s.md.detail=False
    def off(s,va):
        r=va-s.base
        for v,vs,p,ps,n in s.secs:
            if v<=r<v+max(vs,ps): return p+r-v
    def va(s,off):
        for v,vs,p,ps,n in s.secs:
            if p<=off<p+ps: return s.base+v+off-p
    def sec(s,name):
        for v,vs,p,ps,n in s.secs:
            if n==name: return s.base+v,vs,p,ps
    def q(s,va): return struct.unpack_from('<Q',s.d,s.off(va))[0]
    def u32(s,va): return struct.unpack_from('<I',s.d,s.off(va))[0]
    def dis(s,va,n=200,stop_ret=False):
        o=s.off(va); out=[]
        for i in s.md.disasm(s.d[o:o+n*15],va):
            out.append(i)
            if len(out)>=n or (stop_ret and i.mnemonic in('ret','int3') ): break
        return out
    def rtti_vtables(s,name):
        """name like '.?AVFoo@Bar@@' -> list of vtable VAs"""
        i=s.d.find(name.encode()+b'\0'); td=s.va(i-0x10)-s.base
        res=[]; rd=s.sec('.rdata'); o=rd[2]; e=o+rd[3]
        # COL: sig(1) off cdoff tdRVA chRVA selfRVA
        k=o
        while True:
            k=s.d.find(struct.pack('<I',td),k,e)
            if k<0: break
            if (k-12)%4==0 and struct.unpack_from('<I',s.d,k-12)[0]==1:
                colva=s.va(k-12); col=struct.pack('<Q',colva)
                j=o
                while True:
                    j=s.d.find(col,j,e)
                    if j<0: break
                    res.append(s.va(j+8)); j+=8
            k+=4
        return res
