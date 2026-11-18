import numpy as np, cv2
from PIL import Image, ImageFilter
G=np.array(Image.open('/home/claude/s3v/gold_special.png').convert('RGBA')).astype(np.float32)
rgb=G[...,:3]
hsv=cv2.cvtColor(rgb.astype(np.uint8),cv2.COLOR_RGB2HSV).astype(np.float32)
S=hsv[...,1]/255; V=hsv[...,2]/255
gold=(S>0.3)&(V>0.35)&(G[...,3]>40)
core=((hsv[...,1]>90)&(hsv[...,2]>120)&(G[...,3]>128)).astype(np.uint8)
n,lab,st,cen=cv2.connectedComponentsWithStats(core,connectivity=4)
big=[i for i in range(1,n) if st[i,4]>100]
# grow labels into anti-aliased gold pixels
L=np.where(np.isin(lab,big),lab,0).astype(np.int32)
for _ in range(3):
    for i in big:
        g=cv2.dilate((L==i).astype(np.uint8),np.ones((3,3),np.uint8))>0
        L[(L==0)&g&gold]=i
sword=L==3; handle=L==2
yy,xx=np.mgrid[0:250,0:250]
Y=(0.3*rgb[...,0]+0.59*rgb[...,1]+0.11*rgb[...,2])/255
lo,hi=np.percentile(Y[gold],2),np.percentile(Y[gold],99); VN=np.clip((Y-lo)/(hi-lo),0,1)
def gmap(v,stops):
    xs=[s[0] for s in stops]; out=np.zeros(v.shape+(3,),np.float32)
    for c in range(3): out[...,c]=np.interp(v,xs,[s[1][c] for s in stops])
    return out
RED=[(0.0,(55,0,8)),(0.5,(135,4,16)),(0.8,(192,12,24)),(0.95,(228,34,40)),(1.0,(255,105,90))]
WHITE=[(0.0,(95,102,118)),(0.5,(160,168,182)),(0.8,(200,206,218)),(0.95,(232,236,242)),(1.0,(250,251,253))]
HILT=[(0.0,(30,0,4)),(0.6,(105,4,14)),(1.0,(175,22,30))]
col=gmap(VN,RED)
w=np.clip((176-xx)/(176-65),0,1)[...,None]**0.9       # 0 at blade tip (white) -> 1 near guard (red)
blade=gmap(VN,WHITE)*(1-w)+col*w
guard=sword&(xx>=176)
m=sword&~guard; col[m]=blade[m]
h=gmap(VN,HILT); col[guard|handle]=h[guard|handle]
o=G.copy(); o[...,:3]=np.where(gold[...,None],col,rgb)
im=Image.fromarray(o.clip(0,255).astype(np.uint8))
al=np.array(im)[...,3]
g=np.array(Image.fromarray(al).filter(ImageFilter.GaussianBlur(8))).astype(np.float32)
glow=np.zeros((250,250,4),np.uint8); glow[...,0]=225; glow[...,1]=20; glow[...,2]=30; glow[...,3]=np.clip(g*1.2,0,200).astype(np.uint8)
base=Image.fromarray(glow); base.alpha_composite(im); base.save('/home/claude/s3v/special_red_D.png')
bg=Image.new('RGBA',(1060,540),(30,38,66,255))
bg.alpha_composite(Image.open('/home/claude/s3v/special_red_C.png').resize((500,500),Image.LANCZOS),(20,20))
bg.alpha_composite(base.resize((500,500),Image.LANCZOS),(540,20))
bg.convert('RGB').save('/home/claude/vid/special_CD.png')
