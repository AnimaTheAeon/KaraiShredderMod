import pefile,struct,sys,re,bisect,capstone
pe=pefile.PE('game/TMNTSF.exe',fast_load=True); IB=pe.OPTIONAL_HEADER.ImageBase
pe.parse_data_directories(directories=[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_EXCEPTION']])
data=open('game/TMNTSF.exe','rb').read()
text=[s for s in pe.sections if s.Name.startswith(b'.text')][0]
t0=text.PointerToRawData; t1=t0+text.SizeOfRawData; tva=IB+text.VirtualAddress-t0
funcs=sorted(set((IB+e.struct.BeginAddress,IB+e.struct.EndAddress) for e in pe.DIRECTORY_ENTRY_EXCEPTION)); starts=[f[0] for f in funcs]
def fn(va):
    i=bisect.bisect_right(starts,va)-1; return funcs[i] if i>=0 and funcs[i][0]<=va<funcs[i][1] else None
md=capstone.Cs(capstone.CS_ARCH_X86,capstone.CS_MODE_64)
target=int(sys.argv[1],16)
# scan for disp32 such that address of next-instr + disp == target, instr lengths 6..10
seen=set()
for L in range(6,11):
  for dpos in range(2,L-3):
    pass
arr=data[t0:t1]
for i in range(0,len(arr)-4):
    d=struct.unpack_from('<i',arr,i)[0]
    # assume disp at end-ish: candidate instr end in i+4..i+5 (imm8) .. i+8 (imm32)
    for extra in (0,1,4):
        end=i+4+extra
        if tva+t0+end+d==target:
            # try decode from end-L
            for L in range(5,12):
                s=end-L
                if s<0: continue
                ins=list(md.disasm(arr[s:end],tva+t0+s))
                if ins and ins[0].size==L and len(ins)==1 and 'rip' in ins[0].op_str:
                    a=ins[0].address
                    if a in seen: continue
                    seen.add(a); f=fn(a)
                    print(hex(a),ins[0].mnemonic,ins[0].op_str,'func',hex(f[0]) if f else None)
