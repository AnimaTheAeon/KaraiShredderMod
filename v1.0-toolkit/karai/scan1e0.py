import pefile,capstone,bisect
pe=pefile.PE('/home/claude/game/TMNTSF.exe',fast_load=True); IB=pe.OPTIONAL_HEADER.ImageBase
pe.parse_data_directories(directories=[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_EXCEPTION']])
d=open('/home/claude/game/TMNTSF.exe','rb').read()
fs=sorted(set((IB+e.struct.BeginAddress,IB+e.struct.EndAddress) for e in pe.DIRECTORY_ENTRY_EXCEPTION))
off=lambda v: v-0x140001000+0x400
md=capstone.Cs(capstone.CS_ARCH_X86,capstone.CS_MODE_64)
import re
pat=re.compile(rb'\x8b[\x40-\x7f\x80-\xbf]\xe0\x01\x00\x00|\x8b[\x80-\xbf]\xe0\x01\x00\x00')
for a,b in fs:
    if b-a>0x6000: continue
    code=d[off(a):off(b)]
    if b'\xe0\x01\x00\x00' not in code: continue
    calls=b''
    has_lookup=False; loads=[]
    for i in md.disasm(code,a):
        if i.mnemonic=='call' and i.op_str in ('0x140da452c','0x140da4598'): has_lookup=True
        if i.mnemonic=='mov' and 'dword ptr' in i.op_str and '+ 0x1e0]' in i.op_str and i.op_str.split(',')[0].strip().startswith(('e','r')) and 'ptr' not in i.op_str.split(',')[0]: loads.append(hex(i.address))
    if has_lookup and loads: print(hex(a),loads[:3])
