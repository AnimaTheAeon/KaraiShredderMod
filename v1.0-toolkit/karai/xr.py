import pefile,struct,sys,re
pe=pefile.PE('game/TMNTSF.exe',fast_load=True); IB=pe.OPTIONAL_HEADER.ImageBase
data=open('game/TMNTSF.exe','rb').read()
text=[s for s in pe.sections if s.Name.startswith(b'.text')][0]
def off2va(o):
    for s in pe.sections:
        if s.PointerToRawData<=o<s.PointerToRawData+s.SizeOfRawData: return IB+s.VirtualAddress+o-s.PointerToRawData
targets={}
for name in sys.argv[1:]:
    for m in re.finditer(re.escape(name.encode())+b'\0',data):
        if data[m.start()-1]==0: targets[off2va(m.start())]=name
print({hex(k):v for k,v in targets.items()})
t0=text.PointerToRawData; t1=t0+text.SizeOfRawData; tva=IB+text.VirtualAddress-t0
pat=re.compile(rb'[\x48\x4c]\x8d[\x05\x0d\x15\x1d\x25\x2d\x35\x3d]',re.S)
for m in pat.finditer(data,t0,t1):
    i=m.start(); disp=struct.unpack_from('<i',data,i+3)[0]; t=tva+i+7+disp
    if t in targets: print(targets[t], 'lea at', hex(tva+i), 'fileoff',hex(i))
# also pointer tables (8-byte absolute)
for k,v in targets.items():
    p=struct.pack('<Q',k); j=data.find(p)
    while j!=-1: print(v,'ptr at fileoff',hex(j),hex(off2va(j))); j=data.find(p,j+1)
