# Karai cards: description (+0x68), special name (+0xF0), special description (+0xF8) -> custom keys served by the exe hook
import sys,struct
sys.path.insert(0,'/home/claude/work/tools')
from cffrec import Rec
r=Rec.load(open(sys.argv[1],'rb').read()); I=r.inst
def addstr(s):
    I.extend(b'\0'*((-len(I))%8)); a=len(I); I.extend(s.encode()+b'\0'); return a
def setptr(a,t):
    for k,(x,y) in enumerate(r.ptrs):
        if x==a: r.ptrs[k]=(a,t); return
    r.ptrs.append((a,t))
K={0x68:addstr('UI_CHARACTER_DESCRIPTION_KARAI'),0xf0:addstr('SPECIAL_ATTACK_KARAI_NAME'),0xf8:addstr('SPECIAL_ATTACK_KARAI_DESC')}
I.extend(b'\0'*((-len(I))%16))
cards=[struct.unpack_from('<I',s,0)[0] for s in r.syms if s[8:s.find(b'\0',8)].startswith(b'*Karai_HeroData')]
for c in cards:
    for o,a in K.items(): setptr(c+o,a)
r.ptrs.sort(); data=r.save(); open(sys.argv[2],'wb').write(data)
r2=Rec.load(data); J=bytes(r2.inst); D=dict(r2.ptrs)
print(len(cards),[[J[D[c+o]:J.find(b'\0',D[c+o])].decode() for o in K] for c in cards][0])
