# Step 3a: Casey fully original again; Karai (slot 8) gets her own actor reps, anim graph, card text/art.
# in: step-1 Casey record (v10 + Karai actor/cards), original Casey record, v10 anim graph record
import sys, struct
sys.path.insert(0, '/home/claude/work/tools')
from cffrec import Rec
slot9, orig, graph, out = sys.argv[1:5]
r = Rec.load(open(slot9, 'rb').read()); o = Rec.load(open(orig, 'rb').read()); g = Rec.load(open(graph, 'rb').read())
I = r.inst; n = len(o.inst)
def align(a=16): I.extend(b'\0' * ((-len(I)) % a))
def addstr(s): align(8); a = len(I); I.extend(s.encode() + b'\0'); return a
def P(): return dict(r.ptrs)
def setptr(a, t):
    for k, (x, y) in enumerate(r.ptrs):
        if x == a: r.ptrs[k] = (a, t); return
    r.ptrs.append((a, t))
def cs(a): return bytes(I[a:I.find(b'\0', a)]).decode('latin1')
def sym(off, th, name):
    b = struct.pack('<II', off, th) + name.encode() + b'\0'; b += b'\0' * ((-(len(b) + 8)) % 8)
    r.syms.append(b); r.order.append(b'SYMB')
def find_sym(name):
    for s in r.syms:
        if s[8:s.find(b'\0', 8)] == name.encode(): return struct.unpack_from('<I', s, 0)[0]
    raise KeyError(name)

# --- a) Casey back to original (bytes + the one changed pointer) ---
I[0:n] = o.inst[0:n]
Po = dict(o.ptrs)
for k, (a, t) in enumerate(r.ptrs):
    if a < n and Po.get(a) != t: r.ptrs[k] = (a, Po[a])
assert {a: t for a, t in r.ptrs if a < n} == Po

KACT = find_sym('*Karai_Hero*')
KCARDS = [find_sym('*Karai_HeroData*'), find_sym('*Karai_HeroData_Skin_Samurai*'), find_sym('*Karai_HeroData_Skin_TrenchCoat*')]
EMPTY = Po[0x2F8 + 0x08]
assert cs(EMPTY) == ''

# --- d) Karai anim graph: append v10 Casey graph under a new name ---
align(16); B = len(I); I.extend(g.inst)
r.ptrs += [(a + B, t + B) for a, t in g.ptrs]
sym(B, 0x97524006, '*KaraiAnimGraphTuning*')

# --- c) Karai actor reps (clone Casey's 3, Karai model + Karai graph) ---
s_mesh = addstr('build://Characters/NPCs/Karai/Model/Karai.mesh')
s_skel = addstr('build://Characters/NPCs/Karai/Model/Karai.skeleton')
s_graph = addstr('*KaraiAnimGraphTuning*')
rep_names = []
for src, suf in ((0x0, 'Default'), (0x58, 'Samurai'), (0xb0, 'TrenchCoat')):
    align(16); a = len(I); I.extend(I[src:src + 88])
    for x, t in [p for p in list(r.ptrs) if src <= p[0] < src + 88]: r.ptrs.append((x - src + a, t))
    setptr(a + 0x00, s_mesh); setptr(a + 0x08, s_skel); setptr(a + 0x18, s_graph)
    nm = '*Karai_ActorRep_%s*' % suf; sym(a, 0x79c1c4a8, nm); rep_names.append(nm)

# --- Karai actor: own HUD name key ---
s_name = addstr('UI_CHARACTER_NAME_06')          # "Karai" (used by her dialogue speaker entry)
setptr(KACT + 0x1e0, s_name)

# --- e) Karai cards: name, art, tool, reps; blank Casey-only texts ---
s_art = addstr('Boss_Karai.atlas:karai_0')
s_tool = addstr('*PowerSelect_Ability_Common_007_Kunai*')
for c, rn in zip(KCARDS, rep_names):
    setptr(c + 0x28, addstr(rn))
    setptr(c + 0x60, s_name)
    for f in (0x68, 0xf0, 0xf8): setptr(c + f, EMPTY)   # description / special name / special desc (no Karai text exists yet)
    for f in (0x70, 0x98, 0xc8): setptr(c + f, s_art)    # HUD portrait, select art, select thumbnail
    setptr(c + 0x100, s_tool)
align(16)
r.ptrs.sort()
data = r.save(); open(out, 'wb').write(data)
# verify
r2 = Rec.load(data); assert bytes(r2.inst) == bytes(I) and r2.ptrs == r.ptrs
D = dict(r2.ptrs); J = bytes(r2.inst); c2 = lambda a: J[a:J.find(b'\0', a)].decode('latin1')
print('ok', len(data), 'graph at', hex(B))
for nm in ('*CaseyJones_HeroData*', '*Karai_HeroData*'):
    c = [struct.unpack_from('<I', s, 0)[0] for s in r2.syms if s[8:s.find(b'\0', 8)] == nm.encode()][0]
    print(nm, [c2(D[c + f]) for f in (0x10, 0x20, 0x28, 0x60, 0x68, 0x70, 0x98, 0xc8, 0x100)], struct.unpack_from('<I', J, c + 0x18)[0])
for rep in [s for s in r2.syms if b'ActorRep' in s]:
    a = struct.unpack_from('<I', rep, 0)[0]; print(rep[8:rep.find(b'\0', 8)], c2(D[a]), c2(D[a + 0x18]))
print('casey actor scale', struct.unpack_from('<f', J, 0x108 + 0x54)[0], 'karai actor scale', struct.unpack_from('<f', J, KACT + 0x54)[0],
      'casey list', hex(D[0x108 + 0x138]), 'karai list', hex(D[KACT + 0x138]), 'karai name', c2(D[KACT + 0x1e0]))
