import struct,glob,os,sys
def fnv(s):
    h=0x811c9dc5
    for c in s.encode(): h=((h^c)*0x01000193)&0xffffffff
    return h
names=[]
for base in ['Leonardo','Raphael','Donatello','Michelangelo','Alopex','Slash_Hero','Metalhead_Hero','CaseyJones_Hero','Slash','Metalhead','CaseyJones']:
    for suf in ['','_HeroData','_Tutorial','_Narrative']:
        names.append('*%s%s*'%(base,suf))
hs={fnv(n):n for n in names}
print('CaseyJones_Hero check',hex(fnv('*CaseyJones_Hero*')))
files=glob.glob('ovh_dec/*.bin')+glob.glob('dflt_dec/*.bin')
hits={}
for p in files:
    d=open(p,'rb').read()
    for h,n in hs.items():
        k=struct.pack('<I',h); i=d.find(k)
        while i!=-1:
            hits.setdefault(n,[]).append((os.path.basename(p)[:-4],i)); i=d.find(k,i+1)
for n in names:
    if n in hits: print(n, hits[n][:12])
exe=open('game/TMNTSF.exe','rb').read()
print('--- exe')
for h,n in hs.items():
    k=struct.pack('<I',h); c=exe.count(k)
    if c: 
        offs=[];i=exe.find(k)
        while i!=-1 and len(offs)<10: offs.append(hex(i)); i=exe.find(k,i+1)
        print(n,hex(h),c,offs)
