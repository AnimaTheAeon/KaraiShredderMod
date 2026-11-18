import struct,re
from xref import *
def vtables_of(classname):
    out=[]
    for m in re.finditer(re.escape(classname.encode())+b'\x00',D):
        td_rva=pe.get_rva_from_offset(m.start()-16)
        for x in re.finditer(re.escape(struct.pack('<I',td_rva)),D):
            h=x.start()
            if struct.unpack_from('<I',D,h-12)[0]==1:
                col=va_of_off(h-12)
                for mm in re.finditer(re.escape(struct.pack('<Q',col)),D): out.append(va_of_off(mm.start())+8)
    return out
