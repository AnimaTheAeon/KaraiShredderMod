import pefile,capstone,sys
pe=pefile.PE('game/TMNTSF.exe',fast_load=True)
def off2va(o):
    for s in pe.sections:
        if s.PointerToRawData<=o<s.PointerToRawData+s.SizeOfRawData: return pe.OPTIONAL_HEADER.ImageBase+s.VirtualAddress+o-s.PointerToRawData,s.Name
for o in [0x591850,0x65c250]: print(hex(o),[hex(off2va(o)[0]),off2va(o)[1]])
md=capstone.Cs(capstone.CS_ARCH_X86,capstone.CS_MODE_64)
data=open('game/TMNTSF.exe','rb').read()
start=int(sys.argv[1],16); n=int(sys.argv[2],16)
va,_=off2va(start)
for i in md.disasm(data[start:start+n],va): print(hex(i.address),i.mnemonic,i.op_str)
