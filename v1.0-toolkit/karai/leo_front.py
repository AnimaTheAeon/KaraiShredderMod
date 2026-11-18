import numpy as np, cv2, colorsys
from PIL import Image, ImageDraw, ImageFilter
src=Image.open('/home/claude/s3v/attack_leo.png').convert('RGBA'); A=np.array(src)
W=250
m=Image.new('L',(W,W),0); d=ImageDraw.Draw(m)
blade=[(197,13),(204,17),(206,40),(205,95),(190,106),(160,132),(135,155),(115,175),(100,190),(84,178),(80,168),(96,153),(107,146),(118,137),(129,125),(150,100),(170,74),(186,48),(192,30)]
tsuba=[(57,158),(80,151),(103,198),(103,212),(84,218),(60,176)]
handle=[(28,206),(66,183),(78,196),(80,208),(34,226)]
for p in (blade,tsuba,handle): d.polygon(p,fill=255)
keep=np.array(m)>0
np.save('/tmp/keep.npy',keep)
o=A.copy(); o[~keep & (A[...,3]>0)]=[255,0,0,255]
bg=Image.new('RGBA',(W,W),(30,38,66,255)); bg.alpha_composite(Image.fromarray(o)); bg.resize((750,750),Image.NEAREST).save('/home/claude/vid/al_mask.png')
hsv=cv2.cvtColor(A[...,:3],cv2.COLOR_RGB2HSV)
dark=(hsv[...,2]<70)&(A[...,3]>0)
grow=cv2.dilate(keep.astype(np.uint8),cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(9,9)))>0
k2=keep|(grow&dark)
out=A.copy(); out[...,3]=np.where(k2,A[...,3],0)
Image.fromarray(out).save('/home/claude/s3v/front_raw.png')
bg=Image.new('RGBA',(W,W),(30,38,66,255)); bg.alpha_composite(Image.fromarray(out)); bg.resize((750,750),Image.NEAREST).save('/home/claude/vid/al_front.png')
