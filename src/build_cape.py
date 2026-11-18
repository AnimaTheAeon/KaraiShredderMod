"""v1.0.4: playable Shredder gets his own purple-cape model. Boss Shredder is not touched.

How the game finds files (see docs/FORMATS.md):
  pak key = lookup8(MD5(asset path).hexdigest().upper())   e.g. 'Characters/NPCs/Shredder/Model/Shredder.mesh'
  texture key = lookup8(texture GUID)                      (materials name textures by a 32-char hex GUID)
Chain: hero ActorRep -> Shredder.mesh (_PreloadRooftops_.pak2) -> its material (...shadergraph, Rooftops)
       -> diffuse texture GUID 346BC2D4B607C70507101824F448B834 (Rooftops).

What this builds (overhead.pak2, Shredder and Both versions only):
  1. hero record 0e2ff051f6d864af: mesh path '.../Shredder.mesh' -> '.../ShredHro.mesh' (same length, re-encrypted)
  2. new entry: copy of the mesh whose material path says 'ShredHro.' instead of 'Shredder.'
  3. new entry: copy of the material with the diffuse GUID swapped for a new one
  4. new entry: the diffuse texture with the cape re-coloured purple (only the BC1 blocks on the cape change)

Usage:
  python build_cape.py <original overhead.pak2> <original _PreloadRooftops_.pak2> <folder with overhead_*_v1.0.kpatch> <out folder>
"""
import os, sys, hashlib, struct
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import pak, kpatch, tex
from cff import parse, dec, enc
from l8 import lookup8

sha = lambda b: hashlib.sha1(b).hexdigest().upper()
key = lambda path: lookup8(hashlib.md5(path.encode()).hexdigest().upper().encode())
ORIG_OVERHEAD = 'AD67E867B815A7D262EB7BD58B9B205ADA6C7EC7'
V10 = {'shredder': '234F44EC85099C6434ED5C58ACC28683345A042E', 'both': '668968C34823723CA3AA9053C7B55DEFE463A036'}
WANT = {'shredder': '0530B24F31DE3C2A97850553EF9178BCCC655BBA', 'both': '0FFFBF831174EA9DF810FCF3C7FCBCA5893663FD'}

HERO_RECORD = 0x0e2ff051f6d864af
MESH_KEY, MAT_KEY, TEX_KEY = 0x9704bb740b27ef99, 0xace9ec120f6ea44e, 0xb6fbab2ec679b8f5
OLD_MESH_REF = b'build://Characters/NPCs/Shredder/Model/Shredder.mesh'
NEW_MESH_REF = b'build://Characters/NPCs/Shredder/Model/ShredHro.mesh'
OLD_MAT = b'/Characters/NPCs/Shredder/Model/Shredder.ShredderCharacterShader_REBIRTH_CHARACTER_SHADER.shadergraph'
NEW_MAT = b'/Characters/NPCs/Shredder/Model/ShredHro.ShredderCharacterShader_REBIRTH_CHARACTER_SHADER.shadergraph'
OLD_GUID = b'346BC2D4B607C70507101824F448B834'
NEW_GUID = hashlib.md5(b'Characters/NPCs/Shredder/Model/ShredHro_Purple_BaseColor').hexdigest().upper().encode()

def edit_hero_record(raw):
    """Swap the mesh path inside the encrypted INST chunk of the hero record (same length)."""
    wrap, hdr, ch = parse(raw); k = [b for t, b in ch if t == b'DEF0'][0][1]
    i = (32 if wrap else 0) + 0x40
    while True:
        tag = raw[i:i + 4]; ln = struct.unpack_from('<I', raw, i + 4)[0]
        if tag == b'INST': break
        i += ln
    plain = dec(raw[i + 8:i + ln], k)
    assert plain.count(OLD_MESH_REF) == 1, 'hero mesh path not found exactly once'
    new = enc(plain.replace(OLD_MESH_REF, NEW_MESH_REF), k)
    return raw[:i + 8] + new + raw[i + ln:]

def new_files(rooftops):
    mesh = pak.get(rooftops, MESH_KEY); mat = pak.get(rooftops, MAT_KEY); t = pak.get(rooftops, TEX_KEY)
    assert mesh.count(OLD_MAT) == 1 and mat.count(OLD_GUID) > 0
    mesh2 = mesh.replace(OLD_MAT, NEW_MAT); mat2 = mat.replace(OLD_GUID, NEW_GUID)
    t2, _ = tex.build(t)
    return {key(NEW_MESH_REF[8:].decode()): mesh2, key(NEW_MAT[1:].decode()): mat2, lookup8(NEW_GUID): t2}

def main(orig_overhead, rooftops_path, v10_dir, out):
    os.makedirs(out, exist_ok=True)
    orig = open(orig_overhead, 'rb').read(); assert sha(orig) == ORIG_OVERHEAD, 'not the original overhead.pak2'
    rooftops = open(rooftops_path, 'rb').read()
    add = new_files(rooftops)
    for b in ('shredder', 'both'):
        base = kpatch.apply(orig, os.path.join(v10_dir, f'overhead_{b}_v1.0.kpatch')); assert sha(base) == V10[b]
        rec = edit_hero_record(pak.get(base, HERO_RECORD))
        new = pak.edit(base, replace={HERO_RECORD: rec}, add=add)
        assert sha(new) == WANT[b], f'{b}: got {sha(new)}, expected {WANT[b]}'
        open(os.path.join(out, f'overhead_{b}.pak2'), 'wb').write(new)
        open(os.path.join(out, f'overhead_{b}.kpatch'), 'wb').write(kpatch.make(orig, new))
        print(f'OK overhead {b}: {sha(new)}')

if __name__ == '__main__':
    if len(sys.argv) != 5: print(__doc__); sys.exit(1)
    main(*sys.argv[1:])
