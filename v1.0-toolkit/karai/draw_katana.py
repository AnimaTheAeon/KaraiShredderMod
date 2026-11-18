# Draw a single katana icon (chunky cartoon style, thick dark outline), red/black theme.
import numpy as np, math
from PIL import Image, ImageDraw
def bez(p0,p1,p2,n=90):
    return [((1-t)**2*p0[0]+2*(1-t)*t*p1[0]+t*t*p2[0], (1-t)**2*p0[1]+2*(1-t)*t*p1[1]+t*t*p2[1]) for t in np.linspace(0,1,n)]
def normals(pts):
    out=[]
    for i in range(len(pts)):
        a=pts[max(i-1,0)]; b=pts[min(i+1,len(pts)-1)]; dx,dy=b[0]-a[0],b[1]-a[1]; L=math.hypot(dx,dy) or 1
        out.append((-dy/L,dx/L))
    return out
def ellipse_pts(c,ax1,r1,r2,n=60):
    ux,uy=ax1; vx,vy=-uy,ux
    return [(c[0]+ux*r1*math.cos(t)+vx*r2*math.sin(t), c[1]+uy*r1*math.cos(t)+vy*r2*math.sin(t)) for t in np.linspace(0,2*math.pi,n)]
def katana(size=250,S=4,steel=(168,176,190),edge=(246,248,252),wrap=(200,18,28),grip=(26,18,22),guard=(34,28,34)):
    W=size*S; im=Image.new('RGBA',(W,W),(0,0,0,0)); dr=ImageDraw.Draw(im)
    P=lambda pts:[(x*S,y*S) for x,y in pts]
    OUT=(12,8,12,255); ow=5
    G=(84,160); TIP=(218,24)
    spine=bez(G,(158,112),TIP); N=normals(spine); n=len(spine); ts=np.linspace(0,1,n)
    w=[21*(1-0.25*t) if t<0.9 else 21*(1-0.25*t)*max(0.02,1-(t-0.9)/0.1) for t in ts]
    back=[(x+nx*wi*0.45,y+ny*wi*0.45) for (x,y),(nx,ny),wi in zip(spine,N,w)]
    cut=[(x-nx*wi*0.55,y-ny*wi*0.55) for (x,y),(nx,ny),wi in zip(spine,N,w)]
    # outline = draw polygon then thick line around
    poly=back+cut[::-1]
    dr.polygon(P(poly),fill=OUT); dr.line(P(poly+[poly[0]]),fill=OUT,width=ow*S,joint='curve')
    dr.polygon(P(poly),fill=steel+(255,))
    # cutting-edge highlight band and spine shade
    hl=[(x-nx*wi*0.30,y-ny*wi*0.30) for (x,y),(nx,ny),wi in zip(spine,N,w)][2:-6]
    dr.line(P(hl),fill=edge+(255,),width=int(4*S))
    sh=[(x+nx*wi*0.25,y+ny*wi*0.25) for (x,y),(nx,ny),wi in zip(spine,N,w)][2:-10]
    dr.line(P(sh),fill=(110,116,132,255),width=int(3*S))
    # blade direction at guard
    d=(spine[3][0]-spine[0][0],spine[3][1]-spine[0][1]); L=math.hypot(*d); d=(d[0]/L,d[1]/L); nrm=(-d[1],d[0])
    # habaki collar (red-gold) just above guard
    hc=(G[0]+d[0]*6,G[1]+d[1]*6)
    hab=ellipse_pts(hc,nrm,10,5); dr.polygon(P(hab),fill=OUT); dr.polygon(P(ellipse_pts(hc,nrm,7.5,3)),fill=(150,24,30,255))
    # tsuba: ellipse across the blade
    gc=(G[0]-d[0]*3,G[1]-d[1]*3)
    dr.polygon(P(ellipse_pts(gc,nrm,27,9)),fill=OUT)
    dr.polygon(P(ellipse_pts(gc,nrm,22.5,5.5)),fill=guard+(255,))
    dr.line(P(ellipse_pts(gc,nrm,16,2.5)),fill=(96,88,96,255),width=int(2*S))
    # handle
    a=(gc[0]-d[0]*8,gc[1]-d[1]*8); b=(a[0]-d[0]*62,a[1]-d[1]*62); hw=12
    c=lambda p,t,o:(p[0]-d[0]*t+nrm[0]*o, p[1]-d[1]*t+nrm[1]*o)
    hp=[c(a,0,hw),c(a,62,hw),c(a,62,-hw),c(a,0,-hw)]
    dr.polygon(P(hp),fill=OUT); dr.line(P(hp+[hp[0]]),fill=OUT,width=ow*S)
    hw2=hw-2.5; dr.polygon(P([c(a,0,hw2),c(a,62,hw2),c(a,62,-hw2),c(a,0,-hw2)]),fill=grip+(255,))
    k=6
    for i in range(k):
        t0=(i+0.12)/k*62; t1=(i+0.88)/k*62; tm=(t0+t1)/2
        dr.polygon(P([c(a,t0,0),c(a,tm,hw2-0.3),c(a,t1,0),c(a,tm,-hw2+0.3)]),fill=wrap+(255,))
    # pommel cap
    pc=c(a,64,0); dr.polygon(P(ellipse_pts(pc,nrm,12,7)),fill=OUT); dr.polygon(P(ellipse_pts(pc,nrm,8,3.5)),fill=(140,20,26,255))
    return im.resize((size,size),Image.LANCZOS)
if __name__=='__main__':
    k=katana(); k.save('/home/claude/s3j/karai_katana.png')
    ref=Image.open('/home/claude/s3j/hud2_12.png').convert('RGBA')
    bg=Image.new('RGBA',(520,260),(30,40,70,255)); bg.alpha_composite(ref,(0,5)); bg.alpha_composite(k,(265,5)); bg.convert('RGB').save('/home/claude/vid/katana_draw.png')
