import numpy as np, cv2
from PIL import Image, ImageDraw
src=Image.open('/home/claude/s3j/hud2_20.png').convert('RGBA'); A=np.array(src).astype(np.float32)
W=250
def poly(pts,w=None):
    m=Image.new('L',(W,W),0); d=ImageDraw.Draw(m)
    if w: d.line(pts,fill=255,width=w,joint='curve')
    else: d.polygon(pts,fill=255)
    return np.array(m)>0
# back sword (handle right, tip upper-left)
back = poly([(2,86),(40,104),(78,124),(112,134),(150,140),(175,142),(176,174),(150,174),(110,175),(80,172),(66,164),(50,144),(20,108),(2,92)])
back|= poly([(170,132),(202,132),(204,182),(170,182)])          # tsuba
back|= poly([(196,139),(228,141),(228,158),(196,160)])          # handle/pommel
# front sword (handle top, tip lower-right) to protect
front= poly([(62,70),(102,70),(98,92),(112,130),(140,170),(170,198),(205,230),(190,232),(150,212),(110,180),(88,150),(76,110),(72,90)])
# stars (peach/orange) protect
r,g,b,a=[A[...,i] for i in range(4)]
star=(r>200)&(g>120)&(b<200)&(r-b>40)&(a>100)
star=cv2.dilate(star.astype(np.uint8),np.ones((3,3),np.uint8))>0
mask=back&~front&~star
np.save('/tmp/mask.npy',mask)
# preview mask
ov=src.copy(); o=np.array(ov); o[mask]=[255,0,0,255]; o[front&back]=[0,255,0,255]
bg=Image.new('RGBA',(W,W),(30,38,66,255)); bg.alpha_composite(Image.fromarray(o)); bg.resize((750,750),Image.NEAREST).save('/home/claude/vid/leo_mask.png')
