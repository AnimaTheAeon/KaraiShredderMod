import pefile,struct,re,sys
pe=pefile.PE('/home/claude/game/TMNTSF.exe',fast_load=True); IB=pe.OPTIONAL_HEADER.ImageBase
def rd(va,n): return pe.get_data(va-IB,n)
def f32(va): return struct.unpack('<f',rd(va,4))[0]
def func(start):
    out=[]; p=False
    for l in open('/home/claude/full.dis'):
        if l.startswith('F '):
            if p: break
            p = l.strip()=='F %x'%start; continue
        if p: out.append(l.rstrip())
    return out
def annot(lines):
    for l in lines:
        a,ins=l.split(' ',1); a=int(a,16); note=''
        m=re.search(r'\[rip ([+-]) 0x([0-9a-f]+)\]',ins)
        if m:
            # need instruction length: next line address
            pass
        yield a,ins
if __name__=='__main__':
    L=func(int(sys.argv[1],16)); addrs=[int(l.split(' ',1)[0],16) for l in L]
    for i,l in enumerate(L):
        a,ins=l.split(' ',1); a=int(a,16); note=''
        m=re.search(r'\[rip ([+-]) 0x([0-9a-f]+)\]',ins)
        if m and i+1<len(addrs):
            t=addrs[i+1]+(1 if m[1]=='+' else -1)*int(m[2],16)
            try:
                if 'movss' in ins or 'addss' in ins or 'mulss' in ins or 'subss' in ins or 'comiss' in ins or 'maxss' in ins or 'minss' in ins: note='  ; [%x]=%g'%(t,f32(t))
                elif 'lea' in ins:
                    b=rd(t,48); s=b.split(b'\0')[0]
                    note='  ; %x "%s"'%(t,s.decode('latin1')) if len(s)>2 and all(32<=c<127 for c in s) else '  ; %x'%t
                else: note='  ; %x'%t
            except Exception: note='  ; %x'%t
        m=re.search(r'dword ptr \[.*\], 0x([0-9a-f]{8})$',ins)
        if m and int(m[1],16)>0x3c000000: note+='  ; =%g'%struct.unpack('<f',struct.pack('<I',int(m[1],16)))[0]
        print('%x %s%s'%(a,ins,note))
