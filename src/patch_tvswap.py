"""v1.0.1 fix: hub TV hero swap for Karai / Shredder.

The home-lair level logic builder (0x140a8f2a2) adds one rule per hero:
    rule = NewRule(ctx=rsi, "*Hero*")              ; 0x14084aab8, listens for FNV("*Hero*")
    trig = ResponseTriggerParam(rbp+0x4a8, {FNV("TurtleSwap_X"), 1})  ; 0x140cf6cc8 (LB_ResponseTrigger)
    act  = SwapLocalPlayerTo(rbp-0x40, FNV("*Hero*"))                 ; 0x140a7a8bc (LB_BehaviorList)
    AddActions(rule, act, trig)                    ; 0x1409d0b30
    Destroy(rbp-0x40)                              ; 0x140ce011c
The TV (SelectCharacterMC -> 0x1405dad58) fires FNV(HeroData+0x20 actor name).
Karai/Shredder had no rule, so nothing listened.  We hook right after Slash's rule
(0x140a8ff26, 'lea rdx,[rip->0x141692658]', 7 bytes) and add the same rule for the
mod heroes.  The response trigger uses a new name (TurtleSwap_Karai / _Shredder)
that no banter rule uses, so no voice line plays and nothing else changes.

Usage: python3 patch_tvswap.py in.exe out.exe <cave_va_hex> karai|shredder|both
"""
import os
import sys, struct
from keystone import Ks, KS_ARCH_X86, KS_MODE_64
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pe import PE

HOOK = 0x140a8ff26
HOOK_ORIG = bytes.fromhex('488d152b27c000')        # lea rdx, [rip+0xc0272b] -> 0x141692658
RET = 0x140a8ff2d
LEA_TARGET = 0x141692658
F_NEWRULE, F_TRIG, F_SWAP, F_ADD, F_DESTROY = 0x14084aab8, 0x140cf6cc8, 0x140a7a8bc, 0x1409d0b30, 0x140ce011c

def fnv(s):
    h = 0x811c9dc5
    for c in s.encode(): h = ((h ^ c) * 0x1000193) & 0xffffffff
    return h

HEROES = {'karai': ('*Karai_Hero*', 'TurtleSwap_Casey'),     # v1.0.2: fire Casey's swap concept; the .KaraiMod clones (KaraiExists) answer it
          'shredder': ('*Shredder_Hero*', 'TurtleSwap_Casey')}  # .ShredderMod clones (ShredderHeroExists) answer it

def lea_rdx_rip(at, target):
    return b'\x48\x8d\x15' + struct.pack('<i', target - (at + 7))

def assemble(cave, heroes, name_addrs):
    """returns machine code; rip-relative LEAs encoded by hand, the rest via keystone"""
    ks = Ks(KS_ARCH_X86, KS_MODE_64)
    out = bytearray()
    def emit(line):
        enc, _ = ks.asm(line, cave + len(out)); out.extend(bytes(enc))
    for k, (actor, trig) in enumerate(heroes):
        emit('mov rcx, rsi')
        out.extend(lea_rdx_rip(cave + len(out), name_addrs[k]))
        emit(f'call {F_NEWRULE:#x}')
        emit('mov r12, rax')
        emit(f'mov dword ptr [rbp - 0x80], {fnv(trig):#x}')
        emit('mov byte ptr [rbp - 0x78], 1')
        emit('lea rdx, [rbp - 0x80]')
        emit('lea rcx, [rbp + 0x4a8]')
        emit(f'call {F_TRIG:#x}')
        emit('mov rbx, rax')
        emit(f'mov edx, {fnv(actor):#x}')
        emit('lea rcx, [rbp - 0x40]')
        emit(f'call {F_SWAP:#x}')
        emit('mov r8, rbx')
        emit('mov rdx, rax')
        emit('mov rcx, r12')
        emit(f'call {F_ADD:#x}')
        emit('lea rcx, [rbp - 0x40]')
        emit(f'call {F_DESTROY:#x}')
    out.extend(lea_rdx_rip(cave + len(out), LEA_TARGET))   # replayed original instruction
    emit(f'jmp {RET:#x}')
    return bytes(out)

def build(src, dst, cave, which):
    heroes = [HEROES[h] for h in (['karai', 'shredder'] if which == 'both' else [which])]
    p = PE(src); d = bytearray(p.d)
    ho = p.off(HOOK)
    assert bytes(d[ho:ho + 7]) == HOOK_ORIG, 'hook site not original'
    size = len(assemble(cave, heroes, [cave] * len(heroes)))
    nbase = cave + ((size + 15) & ~15); names = b''; addrs = []
    for actor, _t in heroes:
        addrs.append(nbase + len(names)); names += actor.encode() + b'\0'
    code = assemble(cave, heroes, addrs)
    assert len(code) == size
    blob = code.ljust(nbase - cave, b'\xcc') + names
    co = p.off(cave)
    assert co is not None and all(b == 0 for b in d[co:co + len(blob) + 16]), 'cave area not free'
    d[co:co + len(blob)] = blob
    d[ho:ho + 7] = b'\xe9' + struct.pack('<i', cave - (HOOK + 5)) + b'\x90\x90'
    open(dst, 'wb').write(d)
    print(f'{dst}: cave {cave:#x}, code {len(code)} bytes, names at {nbase:#x}; heroes {[h[0] for h in heroes]}')

if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2], int(sys.argv[3], 16), sys.argv[4])
