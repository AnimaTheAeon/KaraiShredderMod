import os
import sys, re; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pe import PE
def strat(p,va):
    o=p.off(va)
    if o is None: return None
    s=p.d[o:o+80]; z=s.find(b'\0')
    t=s[:z] if z>=0 else s
    if len(t)>=3 and all(32<=c<127 for c in t): return t.decode()
def ann(p,i):
    m=re.search(r'\[rip ([+-]) 0x([0-9a-f]+)\]',i.op_str)
    x=''
    if m:
        t=i.address+i.size+(int(m.group(2),16)*(1 if m.group(1)=='+' else -1))
        s=strat(p,t); x=' ; %#x'%t+(' "%s"'%s if s else '')
    return x
def show(path,va,n=200,stop=True):
    p=PE(path)
    for i in p.dis(va,n,stop):
        print('%x: %-8s %s%s'%(i.address,i.mnemonic,i.op_str,ann(p,i)))
if __name__=='__main__':
    show(sys.argv[1],int(sys.argv[2],16),int(sys.argv[3]) if len(sys.argv)>3 else 200, len(sys.argv)<=4)
