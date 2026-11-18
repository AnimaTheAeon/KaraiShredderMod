import numpy as np, cv2
from PIL import Image, ImageFilter
F=np.array(Image.open('/home/claude/s3v/front_raw.png').convert('RGBA'))
def recol(F,blade_tint):
    o=F.copy(); hsv=cv2.cvtColor(F[...,:3],cv2.COLOR_RGB2HSV).astype(np.float32)
    h,s,v=hsv[...,0],hsv[...,1],hsv[...,2]
    yy,xx=np.mgrid[0:250,0:250]
    hilt=(xx<72)&(yy>184)&(h>75)&(h<110)&(s>60)          # cyan wrap
    nh=h.copy(); ns=s.copy(); nv=v.copy()
    nh[hilt]=178; ns[hilt]=np.clip(s[hilt]*1.25,0,255); nv[hilt]=np.clip(v[hilt]*1.05,0,255)
    if blade_tint:
        bl=(~hilt)&(h>95)&(h<130)&(s>40)               # blue accents on blade
        nh[bl]=178; ns[bl]=np.clip(s[bl]*1.1,0,255); nv[bl]=v[bl]*0.9
    hsv2=np.stack([nh,ns,nv],-1).astype(np.uint8)
    o[...,:3]=cv2.cvtColor(hsv2,cv2.COLOR_HSV2RGB); return o
def aura(o):
    im=Image.fromarray(o); sc=0.88; n=int(250*sc)
    im=im.resize((n,n),Image.LANCZOS); c=Image.new('RGBA',(250,250),(0,0,0,0)); c.alpha_composite(im,((250-n)//2,(250-n)//2))
    a=np.array(c)[...,3].astype(np.float32)
    g1=np.array(Image.fromarray(a.astype(np.uint8)).filter(ImageFilter.GaussianBlur(9))).astype(np.float32)
    g2=np.array(Image.fromarray(a.astype(np.uint8)).filter(ImageFilter.GaussianBlur(3))).astype(np.float32)
    glow=np.zeros((250,250,4),np.uint8)
    al=np.clip(g1*1.3+g2*0.7,0,220)
    glow[...,0]=225; glow[...,1]=20; glow[...,2]=30; glow[...,3]=al.astype(np.uint8)
    base=Image.fromarray(glow); base.alpha_composite(c); return base
A=aura(recol(F,False)); B=aura(recol(F,True))
A.save('/home/claude/s3v/katana_leo_A.png'); B.save('/home/claude/s3v/katana_leo_B.png')
L=Image.open('/home/claude/s3v/attack_leo.png').convert('RGBA')
bg=Image.new('RGBA',(790,270),(30,38,66,255))
for i,x in enumerate([L,A,B]): bg.alpha_composite(x,(10+i*260,10))
bg.save('/home/claude/vid/katana_leo_options.png')
