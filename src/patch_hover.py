"""v1.0.2: Karai select-screen hover plays 1 of 6 random Karai lines (like Shredder's rand-of-4).
Old Karai hover cave 0x14186e8c0 (entry kept; Shredder's hover else-path and the .text hook jump here)
-> jmp 0x14186fd00.  New code: ebx==1 ? rdi = lines[rand()%6] : default path; jmp 0x140655ca0.
Lines table = int32 offsets relative to the table (no absolute pointers, ASLR-safe)."""
import os
import sys, struct
from keystone import Ks, KS_ARCH_X86, KS_MODE_64
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pe import PE
OLD = 0x14186e8c0
OLD_BYTES = bytes.fromhex('83fb010f85d773defe488d3da0f7ffffe9cb73defe')
NEW = 0x14186fd00
BACK = 0x140655ca0
RAND_SLOT = 0x140f6c550
LINES = ['event:/VO/BOSSES/KARAI/BANTER_KAR_GLOBAL_DASHPREP_001',
         'event:/VO/BOSSES/KARAI/BANTER_KAR_GLOBAL_DASHPREP_002',
         'event:/VO/BOSSES/KARAI/BANTER_KAR_GLOBAL_DASHPREP_003',
         'event:/VO/BOSSES/KARAI/BANTER_KAR_GLOBAL_TELEPORTPREP_001',
         'event:/VO/BOSSES/KARAI/BANTER_KAR_GLOBAL_TELEPORTPREP_002',
         'event:/VO/BOSSES/KARAI/BANTER_KAR_GLOBAL_TELEPORTPREP_003']
def build(src, dst):
    p = PE(src); d = bytearray(p.d); ks = Ks(KS_ARCH_X86, KS_MODE_64)
    oo = p.off(OLD); assert bytes(d[oo:oo + len(OLD_BYTES)]) == OLD_BYTES, 'old Karai hover cave not as expected'
    def code(table):
        out = bytearray()
        def e(s): enc, _ = ks.asm(s, NEW + len(out)); out.extend(bytes(enc))
        e('cmp ebx, 1'); e(f'jne {BACK:#x}')
        out.extend(b'\xff\x15' + struct.pack('<i', RAND_SLOT - (NEW + len(out) + 6)))   # call [rip->rand]
        e('xor edx, edx'); e(f'mov ecx, {len(LINES)}'); e('div ecx')
        out.extend(b'\x48\x8d\x0d' + struct.pack('<i', table - (NEW + len(out) + 7)))   # lea rcx,[rip->table]
        e('movsxd rax, dword ptr [rcx + rdx*4]'); e('lea rdi, [rcx + rax]'); e(f'jmp {BACK:#x}')
        return bytes(out)
    n = len(code(NEW + 0x80)); table = NEW + ((n + 15) & ~15)
    strs = b''; offs = []
    sbase = table + 4 * len(LINES)
    for s in LINES: offs.append(sbase + len(strs) - table); strs += s.encode() + b'\0'
    c = code(table); assert len(c) == n
    blob = c.ljust(table - NEW, b'\xcc') + b''.join(struct.pack('<i', o) for o in offs) + strs
    no = p.off(NEW); assert all(b == 0 for b in d[no:no + len(blob) + 16]), 'new area not free'
    d[no:no + len(blob)] = blob
    jmp = b'\xe9' + struct.pack('<i', NEW - (OLD + 5))
    d[oo:oo + len(OLD_BYTES)] = jmp.ljust(len(OLD_BYTES), b'\xcc')
    open(dst, 'wb').write(d)
    print(f'{dst}: hover code {n} bytes at {NEW:#x}, table {table:#x}, {len(LINES)} lines, blob ends {NEW+len(blob):#x}')
if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2])
