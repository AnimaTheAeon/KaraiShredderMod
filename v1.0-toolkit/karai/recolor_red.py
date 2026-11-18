# recolour cool/green hues of a game icon to an aggressive crimson; keeps warm sparkles
import sys,numpy as np
from PIL import Image
def recolor(img, lo, hi, target=358, spread=0.08, satmul=1.45, satadd=0.18, valmul=0.86):
    a=np.asarray(img.convert('RGBA')).astype(float)/255; rgb=a[...,:3]; A=a[...,3]
    mx=rgb.max(-1); mn=rgb.min(-1); dl=mx-mn; r,g,b=rgb[...,0],rgb[...,1],rgb[...,2]
    hue=np.zeros_like(mx); m=dl>1e-6
    hr=(mx==r)&m; hg=(mx==g)&m&~hr; hb=m&~hr&~hg
    hue[hr]=((g-b)[hr]/dl[hr])%6; hue[hg]=((b-r)[hg]/dl[hg])+2; hue[hb]=((r-g)[hb]/dl[hb])+4; hue*=60
    sat=np.where(mx>0,dl/np.maximum(mx,1e-6),0)
    sel=(hue>lo)&(hue<hi)&(sat>0.12)
    mid=(lo+hi)/2
    nh=np.where(sel,(target+(hue-mid)*spread)%360,hue)
    ns=np.where(sel,np.minimum(1,sat*satmul+satadd),sat)
    nv=np.where(sel,mx*valmul,mx)
    H=nh/60; C=nv*ns; X=C*(1-np.abs(H%2-1)); z=np.zeros_like(C); idx=np.floor(H).astype(int)%6
    out=np.zeros_like(rgb)
    for k,(R,G,B) in enumerate([(C,X,z),(X,C,z),(z,C,X),(z,X,C),(X,z,C),(C,z,X)]):
        mk=idx==k; out[...,0][mk]=R[mk]; out[...,1][mk]=G[mk]; out[...,2][mk]=B[mk]
    out+=(nv-C)[...,None]
    return Image.fromarray((np.clip(np.dstack([out,A]),0,1)*255).astype(np.uint8),'RGBA')
