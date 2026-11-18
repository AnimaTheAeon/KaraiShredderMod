import struct,zlib
def fnv1a32(b,h=0x811c9dc5):
    for c in b: h=((h^c)*0x01000193)&0xffffffff
    return h
def write_pak(path,stem,entries,level=9):
    """entries: list of (hash64, raw_bytes)"""
    body=bytearray(); dirs=[]; off=0x1000
    for h,raw in entries:
        c=zlib.compress(raw,level); al=(len(c)+0xfff)&~0xfff
        dirs.append(struct.pack('<QIIIIII',h,off,len(c),al,len(raw),0,0x1000000))
        body+=c+b'\0'*(al-len(c)); off+=al
    hdr=bytearray(0x1000); hdr[0:4]=b'PAK2'; hdr[4:8]=bytes([1,0,1,0])
    struct.pack_into('<IIQI',hdr,8,len(entries),0,off,fnv1a32(stem.lower().encode()))
    open(path,'wb').write(bytes(hdr)+bytes(body)+b''.join(dirs))
