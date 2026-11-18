import struct,io,os,texture2ddecoder
from PIL import Image
def _ds(w,h,mips,bpb):
    s=0
    for i in range(mips): s+=max(1,(w+3)//4)*max(1,(h+3)//4)*bpb; w=max(1,w//2); h=max(1,h//2)
    return s
def decode(d):
    """returns (PIL RGBA upright, info) or None"""
    if len(d)<48: return None
    mips,one,fmt,w,h,dep=struct.unpack_from('<IIIIII',d,4)
    if not(one==1 and 1<=mips<=13 and 4<=w<=8192 and 4<=h<=8192): return None
    if fmt in (17,18,20):
        if d[0x2c:0x30]!=b'RIFF': return None
        ln=struct.unpack_from('<I',d,0x28)[0]; im=Image.open(io.BytesIO(d[0x2c:0x2c+ln])); im=im.convert('RGBA')
        return im.transpose(Image.FLIP_TOP_BOTTOM),('webp',fmt,0x2c)
    if fmt in (2,4):
        bpb=8 if fmt==2 else 16; hl=len(d)-_ds(w,h,mips,bpb)
        if not(40<=hl<8192): return None
        n=(w*h//2) if fmt==2 else w*h
        px=(texture2ddecoder.decode_bc1 if fmt==2 else texture2ddecoder.decode_bc3)(d[hl:hl+n],w,h)
        return Image.frombytes('RGBA',(w,h),px,'raw','BGRA').transpose(Image.FLIP_TOP_BOTTOM),('bc',fmt,hl)
    return None
