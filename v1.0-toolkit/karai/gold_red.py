import numpy as np, cv2
from PIL import Image, ImageFilter
G=np.array(Image.open('/home/claude/s3v/gold_special.png').convert('RGBA')).astype(np.float32)
rgb=G[...,:3]; a=G[...,3]
hsv=cv2.cvtColor(G[...,:3].astype(np.uint8),cv2.COLOR_RGB2HSV).astype(np.float32)
V=hsv[...,2]/255; S=hsv[...,1]/255
gold=(S>0.35)&(V>0.35)
yy,xx=np.mgrid[0:250,0:250]
hilt=(xx>184)&(yy<128)&(yy>85)&(xx-yy>60)
flame=(yy>150)|((yy>132)&(xx>140)&(xx<185))
def gmap(v,stops):
    xs=[s[0] for s in stops]; out=np.zeros(v.shape+(3,),np.float32)
    for c in range(3): out[...,c]=np.interp(v,xs,[s[1][c] for s in stops])
    return out
RED=[(0.0,(55,0,8)),(0.5,(135,4,16)),(0.8,(192,12,24)),(0.95,(228,34,40)),(1.0,(255,105,90))]
STEEL=[(0.0,(70,80,100)),(0.5,(130,145,170)),(0.8,(180,192,212)),(0.95,(232,238,248)),(1.0,(255,255,255))]
HILT=[(0.0,(30,0,4)),(0.6,(110,4,14)),(1.0,(190,24,32))]
Y=(0.3*rgb[...,0]+0.59*rgb[...,1]+0.11*rgb[...,2])/255
lo,hi=np.percentile(Y[gold],2),np.percentile(Y[gold],99)
VN=np.clip((Y-lo)/(hi-lo),0,1)
print(np.percentile(VN[gold],[10,25,50,75,90]))
def make(blade_steel):
    o=G.copy(); v=VN
    col=gmap(v,RED)
    if blade_steel:
        st=gmap(v,STEEL); w=np.clip((yy-112)/45+np.clip((xx-150)/60,0,1)*0.6,0,1)[...,None]; m=gold&~hilt; col[m]=(st*(1-w)+col*w)[m]
    hc=gmap(v,HILT); col[hilt]=hc[hilt]
    o[...,:3]=np.where(gold[...,None],col,rgb)
    im=Image.fromarray(o.clip(0,255).astype(np.uint8))
    al=np.array(im)[...,3]
    g=np.array(Image.fromarray(al).filter(ImageFilter.GaussianBlur(8))).astype(np.float32)
    glow=np.zeros((250,250,4),np.uint8); glow[...,0]=225; glow[...,1]=20; glow[...,2]=30; glow[...,3]=np.clip(g*1.2,0,200).astype(np.uint8)
    base=Image.fromarray(glow); base.alpha_composite(im); return base
A=make(False); B=make(True)
A.save('/home/claude/s3v/special_red_A.png'); B.save('/home/claude/s3v/special_red_B.png')
K=Image.open('/home/claude/s3j/karai_katana.png').convert('RGBA')
bg=Image.new('RGBA',(1060,290),(30,38,66,255))
for i,x in enumerate([Image.open('/home/claude/s3v/gold_special.png').convert('RGBA'),A,B,K]): bg.alpha_composite(x,(10+i*262,20))
bg.convert('RGB').save('/home/claude/vid/special_red_opts.png')
