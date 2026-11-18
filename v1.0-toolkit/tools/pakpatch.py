import struct,zlib,shutil
def patch_pak(src,dst,repl):
    shutil.copyfile(src,dst)
    with open(dst,'r+b') as f:
        hd=bytearray(f.read(32)); cnt,=struct.unpack_from('<I',hd,8); t,=struct.unpack_from('<Q',hd,16)
        f.seek(t); dirb=bytearray(f.read(cnt*32)); end=t
        for i in range(cnt):
            h,off,cs,al,us,z,fl=struct.unpack_from('<QIIIIII',dirb,i*32)
            if h not in repl: continue
            raw=repl[h]; c=zlib.compress(raw,9)
            if len(c)<=al: f.seek(off); f.write(c+b'\0'*(al-len(c))); noff,nal=off,al
            else: nal=(len(c)+0xfff)&~0xfff; noff=end; f.seek(noff); f.write(c+b'\0'*(nal-len(c))); end+=nal
            struct.pack_into('<QIIIIII',dirb,i*32,h,noff,len(c),nal,len(raw),z,fl)
        f.seek(end); f.write(dirb); f.truncate(); struct.pack_into('<Q',hd,16,end); f.seek(0); f.write(hd)
