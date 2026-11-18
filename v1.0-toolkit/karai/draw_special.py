import sys, math, numpy as np
sys.path.insert(0,'/home/claude/work')
from PIL import Image, ImageDraw, ImageFilter
from draw_katana import katana
S=4; W=250*S
def crescent(dr,c,r,th,a0,a1,col,out=(12,8,12,255),ow=4):
    pts_o=[(c[0]+r*math.cos(t),c[1]+r*math.sin(t)) for t in np.linspace(a0,a1,60)]
    pts_i=[(c[0]+(r-th*math.sin((t-a0)/(a1-a0)*math.pi))*math.cos(t),c[1]+(r-th*math.sin((t-a0)/(a1-a0)*math.pi))*math.sin(t)) for t in np.linspace(a0,a1,60)]
    poly=[(x*S,y*S) for x,y in pts_o+pts_i[::-1]]
    dr.polygon(poly,fill=out); dr.line(poly+[poly[0]],fill=out,width=ow*S,joint='curve'); dr.polygon(poly,fill=col)
def star(dr,c,r,col,out=(12,8,12,255)):
    pts=[]
    for i in range(8):
        a=i*math.pi/4-math.pi/2; rr=r if i%2==0 else r*0.32
        pts.append(((c[0]+rr*math.cos(a))*S,(c[1]+rr*math.sin(a))*S))
    dr.polygon(pts,fill=out); dr.line(pts+[pts[0]],fill=out,width=3*S); dr.polygon(pts,fill=col)
im=Image.new('RGBA',(W,W),(0,0,0,0)); dr=ImageDraw.Draw(im)
# one sweeping slash trail behind the blade (the tip's swing path), crimson with a dark inner band
C=(64,206)
crescent(dr,C,178,46,math.radians(-100),math.radians(-5),(150,8,18,255))
crescent(dr,C,178,26,math.radians(-96),math.radians(-9),(222,30,38,255),ow=0)
crescent(dr,C,178,9,math.radians(-92),math.radians(-14),(255,120,110,255),ow=0)
crescent(dr,C,128,22,math.radians(-88),math.radians(-18),(40,10,14,255))
im=im.resize((250,250),Image.LANCZOS)
k=katana(250).rotate(-6,resample=Image.BICUBIC,center=(125,125))
im.alpha_composite(k)
d2=Image.new('RGBA',(W,W),(0,0,0,0)); dd=ImageDraw.Draw(d2)
star(dd,(226,44),20,(255,226,170,255)); star(dd,(232,170),14,(255,226,170,255))
im.alpha_composite(d2.resize((250,250),Image.LANCZOS))
im.save('/home/claude/s3j/karai_special_v2.png')
leo=Image.open('/home/claude/s3j/hud2_20.png').convert('RGBA'); kat=Image.open('/home/claude/s3j/karai_katana.png')
bg=Image.new('RGBA',(780,260),(30,40,70,255)); bg.alpha_composite(leo,(0,5)); bg.alpha_composite(im,(265,5)); bg.alpha_composite(kat,(530,5)); bg.convert('RGB').save('/home/claude/vid/special_v2.png')
