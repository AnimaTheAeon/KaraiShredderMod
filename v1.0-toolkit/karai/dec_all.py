import sys,os,glob
sys.path.insert(0,'/home/claude/work/tools')
from cffrec import Rec
src,dst=sys.argv[1],sys.argv[2]; os.makedirs(dst,exist_ok=True); n=0
for p in glob.glob(src+'/*.bin'):
    d=open(p,'rb').read()
    if d[:4]==b'CFF0' or (d[:4]==b'RSC0' and d[32:36]==b'CFF0'):
        try:
            r=Rec.load(d); open(os.path.join(dst,os.path.basename(p)),'wb').write(bytes(r.inst)); n+=1
        except Exception as e: print('fail',p,e)
print(n)
