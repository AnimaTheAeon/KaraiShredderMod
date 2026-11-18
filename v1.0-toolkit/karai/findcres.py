import sys,glob,struct,numpy as np,cv2
sys.path.insert(0,'/home/claude/work/tools')
from texdec import decode
from PIL import Image
t=np.array(Image.open('/home/claude/s3v/e_shot.png').convert('RGB')).astype(np.float32)
def ymask(a):
    r,g,b=a[...,0],a[...,1],a[...,2]
    return ((r>200)&(g>180)&(b<120)).astype(np.float32)
tm=ymask(t)[20:95,25:100]   # crescent area
res=[]
files=sorted(glob.glob('/home/claude/ovh/*.bin'))+sorted(glob.glob('/home/claude/direct/*.bin'))
for p in files:
    d=open(p,'rb').read()
    if len(d)<1000: continue
    try: r=decode(d)
    except Exception: continue
    if not r: continue
    im=np.array(r[0].convert('RGBA')).astype(np.float32)
    a=im[...,3:]/255; m=ymask(im[...,:3])*(a[...,0]>0.5)
    if m.mean()<0.002: continue
    best=(0,)
    for s in (0.25,0.3,0.35,0.4,0.5,0.6,0.75,1.0):
        mm=cv2.resize(m,None,fx=s,fy=s,interpolation=cv2.INTER_AREA)
        if mm.shape[0]<tm.shape[0] or mm.shape[1]<tm.shape[1]: continue
        cc=cv2.matchTemplate(mm,tm,cv2.TM_CCOEFF_NORMED); cc[~np.isfinite(cc)]=0
        pm=cv2.blur(mm,(tm.shape[1],tm.shape[0]))[tm.shape[0]//2:tm.shape[0]//2+cc.shape[0],tm.shape[1]//2:tm.shape[1]//2+cc.shape[1]]
        tmean=tm.mean(); cc[(pm<tmean*0.6)|(pm>tmean*1.5)]=0
        _,mx,_,loc=cv2.minMaxLoc(cc)
        if mx>best[0]: best=(mx,s,(int(loc[0]/s),int(loc[1]/s)))
    res.append((best,p,im.shape))
res.sort(key=lambda x:-x[0][0])
for r in res[:8]: print(r)
