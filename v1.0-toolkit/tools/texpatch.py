import struct,etcpak,texture2ddecoder,numpy as np
from PIL import Image
def levels(w,h,mips):
    out=[];o=0
    for i in range(mips):
        bw,bh=max(1,(w+3)//4),max(1,(h+3)//4); out.append((w,h,o,bw,bh)); o+=bw*bh*16; w=max(1,w//2); h=max(1,h//2)
    return out
def patch_bc3(d,sprites):
    """d: texture bytes (fmt 4). sprites: list of (upright_rgba_img, x, y). Re-encodes only touched blocks per mip."""
    d=bytearray(d); mips,one,fmt,W,H=struct.unpack_from('<IIIII',d,4); assert fmt==4
    lv=levels(W,H,mips); hl=len(d)-(lv[-1][2]+lv[-1][3]*lv[-1][4]*16)
    # full mip0 upright
    px=texture2ddecoder.decode_bc3(bytes(d[hl:hl+W*H]),W,H)
    full=Image.frombytes('RGBA',(W,H),px,'raw','BGRA').transpose(Image.FLIP_TOP_BOTTOM)
    for im,x,y in sprites: full.paste(im,(x,y))
    for (w,h,o,bw,bh),i in zip(lv,range(mips)):
        sc=W//w
        img=full if i==0 else full.resize((w,h),Image.BOX)
        st=np.array(img.transpose(Image.FLIP_TOP_BOTTOM))  # stored orientation RGBA
        for im,x,y in sprites:
            x0=(x//sc)//4*4; x1=min(w,-(-((x+im.width)//sc+1)//4)*4)
            ys0=h-((y+im.height)//sc+1); ys1=h-(y//sc)
            y0=max(0,ys0)//4*4; y1=min(h,-(-ys1//4)*4)
            if x1<=x0 or y1<=y0 or w<4 or h<4: continue
            reg=np.ascontiguousarray(st[y0:y1,x0:x1])
            enc=etcpak.compress_bc3(reg.tobytes(),x1-x0,y1-y0)
            rb=(x1-x0)//4
            for by in range((y1-y0)//4):
                dst=hl+o+((y0//4+by)*bw+x0//4)*16
                d[dst:dst+rb*16]=enc[by*rb*16:(by+1)*rb*16]
    return bytes(d)
