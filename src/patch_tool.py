"""v1.0.3: Karai / Shredder own their real tool marker (fixes "Heckle"/"Hook" upgrade offers and tool levels).

How tools work (orig exe VAs):
- Lifetime buff rule: has Buff_<Hero>_LifetimeBuff -> AB_ApplyBuff(spec: marker hash, +0xD8 PowerSelect hash).
  Karai is built on Casey -> Heckle marker; Shredder on Raph -> Hook marker.
- Every buff application ends in ActionApplyBuff::Execute (0x140cded04, the only caller of AddBuff
  0x140cd3160).  Action +0x58 = target handle (resolved into rbx = entity), +0x70 = buff hash,
  +0x74 = PowerSelect hash (stored on the new buff instance).
- Each tool marker carries BB_SwapAbilityAlias "tool" -> "tool_common_N"; its handler 0x140d0cb44 queues
  ActionSwapAbilityAlias(owner, r8d=FNV("tool"), r9d=FNV(input)).  The ability slot with that input runs.
- The mod's data swapped slot inputs so the borrowed marker fires the new hero's tool:
  Karai: Kunai slot input tool_common_5;   Shredder: SmokeBomb slot input tool_common_2.

Fix (gated on entity+0x78 == FNV("*Karai_Hero*") / FNV("*Shredder_Hero*")):
 A) 0x140cded8f (mov ecx,[r14+0x70]; call 0x140d06f6c):
      Karai:    Heckle marker -> Kunai marker,     Heckle PS -> *PowerSelect_Ability_Common_007_Kunai_Karai*
      Shredder: Hook marker   -> SmokeBomb marker, Hook PS   -> *PowerSelect_Ability_Ninja_001_SmokeBomb_Shredder*
      (written back into the action, then the original lookup call)
 B) 0x140d0cb8e (mov r9d,[r8+0x14]; mov r8d,[r8+0x10]), alias source "tool" only, one way:
      Karai:    tool_common_7 -> tool_common_5   (Kunai marker reaches her Kunai slot)
      Shredder: tool_ninja_1  -> tool_common_2   (SmokeBomb marker reaches his SmokeBomb slot)
    The input each hero actually fires is unchanged from v1.0.2; an old Heckle/Hook marker still works.
Usage: python3 patch_tool.py in.exe out.exe <cave_va_hex> karai|shredder|both
"""
import os
import sys, struct
from keystone import Ks, KS_ARCH_X86, KS_MODE_64
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pe import PE

def fnv(s):
    h = 0x811c9dc5
    for c in s.encode(): h = ((h ^ c) * 0x1000193) & 0xffffffff
    return h

A_SITE, A_ORIG, A_RET, A_CALL = 0x140cded8f, bytes.fromhex('418b4e70e8d4810200'), 0x140cded98, 0x140d06f6c
B_SITE, B_ORIG, B_RET = 0x140d0cb8e, bytes.fromhex('458b4814458b4010'), 0x140d0cb96

HEROES = {
    'karai': dict(actor=fnv('*Karai_Hero*'),
                  m_from=fnv('BuffMarker_Ability_Common_005_Heckle'), m_to=fnv('BuffMarker_Ability_Common_007_Kunai'),
                  ps_from=fnv('*PowerSelect_Ability_Common_005_Heckle*'), ps_to=fnv('*PowerSelect_Ability_Common_007_Kunai_Karai*'),
                  in_from=fnv('tool_common_7'), in_to=fnv('tool_common_5')),
    'shredder': dict(actor=fnv('*Shredder_Hero*'),
                  m_from=fnv('BuffMarker_Ability_Common_002_Hook'), m_to=fnv('BuffMarker_Ability_Ninja_001_SmokeBomb'),
                  ps_from=fnv('*PowerSelect_Ability_Common_002_Hook*'), ps_to=fnv('*PowerSelect_Ability_Ninja_001_SmokeBomb_Shredder*'),
                  in_from=fnv('tool_ninja_1'), in_to=fnv('tool_common_2')),
}
TOOL = fnv('tool')

def asm_lines(lines, base):
    """assemble with labels: two passes via keystone (labels are local, ending with ':')"""
    ks = Ks(KS_ARCH_X86, KS_MODE_64)
    enc, _ = ks.asm('\n'.join(lines), base)
    return bytes(enc)

def cave_a(hs):
    L = ['mov ecx, dword ptr [r14 + 0x70]', 'mov eax, dword ptr [rbx + 0x78]']
    for i, h in enumerate(hs):
        L += [f'cmp eax, {h["actor"]:#x}', f'jne a_next{i}',
              f'cmp ecx, {h["m_from"]:#x}', 'jne a_go',
              f'mov ecx, {h["m_to"]:#x}', 'mov dword ptr [r14 + 0x70], ecx',
              f'cmp dword ptr [r14 + 0x74], {h["ps_from"]:#x}', 'jne a_go',
              f'mov dword ptr [r14 + 0x74], {h["ps_to"]:#x}', 'jmp a_go',
              f'a_next{i}:']
    L += ['a_go:', f'call {A_CALL:#x}', f'jmp {A_RET:#x}']
    return L

def cave_b(hs):
    L = ['mov r9d, dword ptr [r8 + 0x14]', 'mov r8d, dword ptr [r8 + 0x10]',
         f'cmp r8d, {TOOL:#x}', 'jne b_back',
         'mov rax, qword ptr [rsp + 0x20]', 'test rax, rax', 'je b_back',
         'mov eax, dword ptr [rax + 0x50]']          # handle = entity+0x28, so entity+0x78 = handle+0x50
    for i, h in enumerate(hs):
        L += [f'cmp eax, {h["actor"]:#x}', f'jne b_next{i}',
              f'cmp r9d, {h["in_from"]:#x}', 'jne b_back',
              f'mov r9d, {h["in_to"]:#x}', 'jmp b_back',
              f'b_next{i}:']
    L += ['b_back:', f'jmp {B_RET:#x}']
    return L

def build(src, dst, cave, which):
    hs = [HEROES[h] for h in (['karai', 'shredder'] if which == 'both' else [which])]
    p = PE(src); d = bytearray(p.d)
    ao, bo = p.off(A_SITE), p.off(B_SITE)
    assert bytes(d[ao:ao + len(A_ORIG)]) == A_ORIG, 'hook A site not original'
    assert bytes(d[bo:bo + len(B_ORIG)]) == B_ORIG, 'hook B site not original'
    ca = asm_lines(cave_a(hs), cave)
    b_at = cave + ((len(ca) + 15) & ~15)
    cb = asm_lines(cave_b(hs), b_at)
    blob = ca.ljust(b_at - cave, b'\xcc') + cb
    co = p.off(cave)
    assert co is not None and all(x == 0 for x in d[co:co + len(blob) + 16]), 'cave area not free'
    d[co:co + len(blob)] = blob
    d[ao:ao + len(A_ORIG)] = (b'\xe9' + struct.pack('<i', cave - (A_SITE + 5))).ljust(len(A_ORIG), b'\x90')
    d[bo:bo + len(B_ORIG)] = (b'\xe9' + struct.pack('<i', b_at - (B_SITE + 5))).ljust(len(B_ORIG), b'\x90')
    open(dst, 'wb').write(d)
    print(f'{dst}: cave A {cave:#x} ({len(ca)} B), cave B {b_at:#x} ({len(cb)} B), ends {cave+len(blob):#x}; heroes {which}')
    return cave, b_at

if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2], int(sys.argv[3], 16), sys.argv[4])
