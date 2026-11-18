import struct,zlib
def read_dir(b):
    cnt=struct.unpack_from('<I',b,8)[0]; diroff=struct.unpack_from('<Q',b,0x10)[0]
    ents=[list(struct.unpack_from('<QIIIIII',b,diroff+32*i)) for i in range(cnt)]
    return diroff,ents
def get(b,key):
    diroff,ents=read_dir(b)
    for e in ents:
        if e[0]==key:
            raw=bytes(b[e[1]:e[1]+e[2]])
            return zlib.decompress(raw) if e[6]&0x01000000 else raw
    return None
def edit(b,replace={},add={}):
    """replace: key->uncompressed bytes (existing entry); add: key->uncompressed bytes (new entry).
    In-place when the new compressed data fits the entry's aligned slot; otherwise appended before the directory."""
    b=bytearray(b); diroff,ents=read_dir(b); idx={e[0]:i for i,e in enumerate(ents)}
    for k in add: assert k not in idx, 'key exists %016x'%k
    tail=diroff  # first free byte for appends (directory gets rewritten after)
    appended=[]
    for k,data in replace.items():
        e=ents[idx[k]]; c=zlib.compress(data,9)
        if len(c)<=e[3]:
            b[e[1]:e[1]+e[3]]=c+b'\0'*(e[3]-len(c)); e[2]=len(c); e[4]=len(data)
        else:
            appended.append(('rep',k,data,c))
    for k,data in add.items(): appended.append(('add',k,data,zlib.compress(data,9)))
    del b[diroff:]
    for kind,k,data,c in appended:
        off=len(b); al=(len(c)+0xfff)&~0xfff
        b+=c+b'\0'*(al-len(c))
        if kind=='rep':
            e=ents[idx[k]]; e[1]=off; e[2]=len(c); e[3]=al; e[4]=len(data)
        else:
            ents.append([k,off,len(c),al,len(data),0,0x01000000])
    assert len(b)%0x1000==0
    newdir=len(b)
    for e in ents: b+=struct.pack('<QIIIIII',*e)
    struct.pack_into('<I',b,8,len(ents)); struct.pack_into('<Q',b,0x10,newdir)
    assert newdir<2**32
    return bytes(b)
