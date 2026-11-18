import sys,pefile,capstone
src,dst=sys.argv[1],sys.argv[2]
d=bytearray(open(src,'rb').read())
pe=pefile.PE(src,fast_load=True); IB=pe.OPTIONAL_HEADER.ImageBase
def off(va):
    r=va-IB
    for s in pe.sections:
        if s.VirtualAddress<=r<s.VirtualAddress+s.Misc_VirtualSize: return s.PointerToRawData+r-s.VirtualAddress
md=capstone.Cs(capstone.CS_ARCH_X86,capstone.CS_MODE_64)
# (VA, expected disassembly before, old bytes, new bytes)
P=[
 (0x1406a6761,'mov ebx, 0xd0',              'bbd0000000',            'bb00010000'),
 (0x14054e720,'mov edx, 0xd0',              'bad0000000',            'ba00010000'),
 (0x1406a67fd,'mov r12d, 8',                '41bc08000000',          '41bc09000000'),
 (0x1406a67db,'mov dword ptr [rsi + 0xa8], r15d', None, None),
 (0x1406a682b,'mov eax, dword ptr [rsi + 0xa8]',  None, None),
 (0x1406a6831,'mov dword ptr [rsi + rax*4 + 0xb0], r15d', None, None),
 (0x1406a6839,'inc dword ptr [rsi + 0xa8]', None, None),
 (0x1406a683f,'cmp dword ptr [rsi + 0xa8], r12d', None, None),
 (0x1406a6c51,'mov dword ptr [rsi + rcx*4 + 0xb0], eax', None, None),
 (0x1406a66b7,'cmp dword ptr [rcx + 0xa8], 0', None, None),
 (0x1406a66c3,'add dword ptr [rcx + 0xa8], -1', None, None),
]
for va,asm,old,new in P:
    o=off(va); ins=next(md.disasm(bytes(d[o:o+16]),va))
    got='%s %s'%(ins.mnemonic,ins.op_str)
    assert got==asm,(hex(va),got,asm)
    b=bytearray(d[o:o+ins.size])
    if old is None:
        # displacement 0xa8 -> 0xb8, 0xb0 -> 0xbc (disp32 little endian)
        for a,n in ((b'\xa8\x00\x00\x00',b'\xb8\x00\x00\x00'),(b'\xb0\x00\x00\x00',b'\xbc\x00\x00\x00')):
            i=b.find(a)
            if i>0: b[i:i+4]=n; break
        else: raise SystemExit('no disp in %x'%va)
    else:
        assert b.hex()==old,(hex(va),b.hex()); b=bytearray.fromhex(new)
    d[o:o+len(b)]=b
    print(hex(va),got,'->','%s %s'%next(((i.mnemonic,i.op_str) for i in md.disasm(bytes(b),va))))
open(dst,'wb').write(d)
