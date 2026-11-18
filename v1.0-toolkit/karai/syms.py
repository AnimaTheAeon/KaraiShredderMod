import sys,os,glob,re
sys.path.insert(0,'/home/claude/work/tools')
from cffrec import Rec
out=open(sys.argv[2],'w')
for p in sorted(glob.glob(sys.argv[1]+'/*.bin')):
    d=open(p,'rb').read()
    if not (d[:4]==b'CFF0' or (d[:4]==b'RSC0' and d[32:36]==b'CFF0')): continue
    try: r=Rec.load(d)
    except: continue
    names=[]
    for s in r.syms: names+= [m.decode() for m in re.findall(rb'\*[A-Za-z0-9_:\.]+\*',s)]
    strs=[]
    if hasattr(r,'inst'): strs=[m.decode() for m in re.findall(rb'[ -~]{6,}',bytes(r.inst))]
    out.write('%s\tSYM:%s\n'%(os.path.basename(p)[:-4],' '.join(names[:60])))
    for s in strs: out.write('%s\tSTR:%s\n'%(os.path.basename(p)[:-4],s))
