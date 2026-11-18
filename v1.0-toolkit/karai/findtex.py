import sys,glob,struct,os
sys.path.insert(0,'/home/claude/work/tools')
from texdec import decode
from PIL import Image
import numpy as np
key=None
cands=[]
for p in sorted(glob.glob('/home/claude/ovh/*.bin'))+sorted(glob.glob('/home/claude/pre_*/*.bin'))+sorted(glob.glob('/home/claude/pc/*.bin'))+sorted(glob.glob('/home/claude/pre_Junkyard/*.bin')):
    d=open(p,'rb').read()
    if len(d)<200 or d[:4] in (b'CFF0',b'RSC0',b'UIML',b'DXBC',b'// p'): continue
    try:
        mips,one,fmt,w,h,ns=struct.unpack_from('<IIIIII',d,4)
    except: continue
    if one!=1 or fmt not in (2,4,17,18,20) or not (1<=ns<=200) or w<128 or h<128: continue
    try: r=decode(d)
    except Exception as e: continue
    if not r: continue
    im=r[0]; a=np.asarray(im.convert('RGB').resize((32,32))).astype(float)
    # Karai: crimson red + dark navy hair, pale skin
    red=((a[...,0]>150)&(a[...,1]<70)&(a[...,2]<80)).mean()
    navy=((a[...,2]>a[...,0]+20)&(a[...,0]<90)&(a[...,2]<160)).mean()
    cands.append((red*navy,red,navy,p,w,h,ns,fmt))
cands.sort(reverse=True)
for c in cands[:16]: print('%.3f %.2f %.2f %s %dx%d spr=%d fmt=%d'%c)
