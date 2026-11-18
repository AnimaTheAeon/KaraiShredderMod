# Copy Raph's four UI colour sets (+0x78,+0x88,+0xB4,+0xD0; 4 floats each) onto Karai's HeroData cards
import sys,struct
sys.path.insert(0,'/home/claude/work/tools')
from cffrec import Rec
raph=Rec.load(open('/home/claude/ovh/0e2ff051f6d864af.bin','rb').read()).inst; RB=1256
r=Rec.load(open(sys.argv[1],'rb').read()); I=r.inst
cards=[struct.unpack_from('<I',s,0)[0] for s in r.syms if s[8:s.find(b'\0',8)].startswith(b'*Karai_HeroData')]
for c in cards:
    for o in (0x78,0x88,0xB4,0xD0): I[c+o:c+o+16]=raph[RB+o:RB+o+16]
data=r.save(); open(sys.argv[2],'wb').write(data)
J=Rec.load(data).inst
for c in cards: print(hex(c),[tuple(round(x,3) for x in struct.unpack_from('<4f',J,c+o)) for o in (0x78,0x88,0xB4,0xD0)])
