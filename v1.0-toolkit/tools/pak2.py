import struct,zlib,sys,os
def entries(path):
    with open(path,'rb') as f: d=f.read()
    cnt=struct.unpack_from('<I',d,8)[0]; toff=struct.unpack_from('<Q',d,16)[0]
    for i in range(cnt):
        h,off,cs,al,us,z,fl=struct.unpack_from('<QIIIIII',d,toff+i*32)
        raw=d[off:off+cs]
        try: data=zlib.decompress(raw) if fl>>24 else raw
        except Exception as e: data=raw
        yield h,data
if __name__=='__main__':
    src,dst=sys.argv[1],sys.argv[2]; os.makedirs(dst,exist_ok=True)
    for h,data in entries(src):
        open(os.path.join(dst,'%016x.bin'%h),'wb').write(data)
