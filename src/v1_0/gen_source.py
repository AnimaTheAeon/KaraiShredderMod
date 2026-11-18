"""Turn the released v1.0 patches back into readable source, for each version (karai, shredder, both).

Why this exists: Karai's v1.0 build scripts survive (v1.0-toolkit/), but they ran as a long chain of
development steps, and the scripts that built Shredder (and the combined "Both" build) were lost. The
released v1.0 patches are the exact record of what was built, so this script decodes each one into source
a person can read and check:

  source/<version>/exe.asm             every changed instruction and all new code, as x86-64 assembly
  source/<version>/record_<key>.rec    what was appended to each encrypted game-data record
  source/<version>/layout_<key>.json   the elements inserted into the select-screen layout
  source/<version>/banter_additions.json  the voice-line criteria, responses and rules that were added
  source/<version>/manifest.json       the order entries are written, and which textures come from the release

build.py rebuilds the four v1.0 files from the ORIGINAL game files plus these sources and checks every
SHA-1 against the release. Textures are the one thing not turned into source: their new sprites are
recoloured/resized game art, so build.py takes them from the release patch (decode_patch.py --png shows them).

Usage: python gen_source.py <folder with the 4 original game files> <folder with the release .kpatch files> <karai|shredder|both>
"""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
import kpatch, pak, asmfile, recfile, uimlfile

PATCHES = {'karai': {'TMNTSF.exe': 'exe_karai_v1.0.kpatch', 'overhead.pak2': 'overhead_karai.kpatch',
                     'dupes.pak2': 'dupes_karai.kpatch', 'default.pak2': 'default_karai.kpatch'},
           'shredder': {'TMNTSF.exe': 'exe_shredder_v1.0.kpatch', 'overhead.pak2': 'overhead_shredder_v1.0.kpatch',
                        'dupes.pak2': 'dupes_shredder.kpatch', 'default.pak2': 'default_shredder.kpatch'},
           'both': {'TMNTSF.exe': 'exe_both_v1.0.kpatch', 'overhead.pak2': 'overhead_both_v1.0.kpatch',
                    'dupes.pak2': 'dupes_both.kpatch', 'default.pak2': 'default_both.kpatch'}}
LAYOUT = 0x07398c8c3a145269
BANTER = 0x19cff664ab3fd994

def is_texture(t):
    import struct
    if len(t) < 0x1c: return False
    sz, mips, one, fmt, wd, ht = struct.unpack_from('<6I', t, 0)
    return sz == len(t) and one == 1 and fmt in (2, 4) and 0 < wd <= 8192

def changed_entries(o, n):
    d0, E0 = pak.read_dir(o); d1, E1 = pak.read_dir(n); M0 = {e[0]: e for e in E0}
    ch = [e for e in E1 if e[0] in M0 and bytes(o[M0[e[0]][1]:M0[e[0]][1] + M0[e[0]][2]]) != bytes(n[e[1]:e[1] + e[2]])]
    assert all(e[0] in M0 for e in E1), 'v1.0 adds no new entries'
    # write order: entries rewritten in place first (any order), then the ones appended, by their new offset
    inplace = [e[0] for e in ch if e[1] == M0[e[0]][1]]
    moved = [e[0] for e in sorted(ch, key=lambda e: e[1]) if e[1] != M0[e[0]][1]]
    return inplace + moved

def describe_stream(raw):
    """what a leftover zlib stream holds, in words"""
    import struct, zlib
    d = zlib.decompressobj(); x = d.decompress(raw); n = len(raw) - len(d.unused_data)
    if x[:4] == b'CFF0': what = 'an older copy of a game-data record (%d bytes)' % len(x)
    elif is_texture(x):
        wd, ht = struct.unpack_from('<II', x, 16); what = 'an older copy of a %dx%d art atlas' % (wd, ht)
    else: what = 'unknown data (%d bytes)' % len(x)
    return n, what

def layout(o, n):
    """Where the release put each moved entry, where its directory is, and what fills the space between.
    Karai v1.0 was built in many appended steps, so its overhead.pak2 still holds older copies of entries
    the directory no longer points at (the game never reads them). They are listed here so the rebuild can
    put them back from the release patch and match it byte for byte."""
    d0, E0 = pak.read_dir(o); d1, E1 = pak.read_dir(n); M0 = {e[0]: e for e in E0}
    moved = {('%016x' % e[0]): [e[1], e[3]] for e in E1 if e[1] != M0[e[0]][1]}
    live = sorted((e[1], e[1] + e[2]) for e in E1 if e[1] >= d0)
    stale, pos = [], d0
    for a, b in live + [(d1, d1)]:
        p = pos
        while p < a:
            q = n.find(b'\x78\xda', p, a)
            if q < 0: assert not any(n[p:a]); break
            assert not any(n[p:q]); ln, what = describe_stream(n[q:a]); stale.append([q, q + ln, what]); p = q + ln
        pos = max(pos, b)
    return {'directory_offset': d1, 'moved': moved, 'stale_blocks_from_release': stale}

def main(orig_dir, rel_dir, ver):
    out = os.path.join(HERE, 'source', ver); os.makedirs(out, exist_ok=True)
    O = lambda f: open(os.path.join(orig_dir, f), 'rb').read()
    P = lambda f: os.path.join(rel_dir, PATCHES[ver][f])
    man = {'version': ver, 'patches': PATCHES[ver], 'overhead_order': [], 'records': [], 'textures_from_release': []}
    # exe
    o = O('TMNTSF.exe'); _, _, R = kpatch.parse(P('TMNTSF.exe')); n = kpatch.apply(o, P('TMNTSF.exe'))
    asmfile.write_source(o, n, R, os.path.join(out, 'exe.asm'), 'v1.0 %s: TMNTSF.exe changes' % ver)
    # overhead
    o = O('overhead.pak2'); n = kpatch.apply(o, P('overhead.pak2'))
    man['overhead_layout'] = layout(o, n)
    for k in changed_entries(o, n):
        a, b = pak.get(o, k), pak.get(n, k)
        man['overhead_order'].append('%016x' % k)
        if is_texture(b): man['textures_from_release'].append('%016x' % k); continue
        recfile.write_source(k, a, b, os.path.join(out, 'record_%016x.rec' % k), 'v1.0 %s: record %016x' % (ver, k))
        man['records'].append('%016x' % k)
    # layout
    o = O('default.pak2'); n = kpatch.apply(o, P('default.pak2'))
    assert changed_entries(o, n) == [LAYOUT]
    uimlfile.write_source(pak.get(o, LAYOUT), pak.get(n, LAYOUT), os.path.join(out, 'layout_%016x.json' % LAYOUT),
                          'v1.0 %s: select-screen layout insertions.' % ver)
    # banter
    o = O('dupes.pak2'); n = kpatch.apply(o, P('dupes.pak2'))
    assert changed_entries(o, n) == [BANTER]
    ja, jb = json.loads(pak.get(o, BANTER)), json.loads(pak.get(n, BANTER)); add = {}
    for sec in jb:
        if isinstance(jb[sec], dict):
            assert list(jb[sec])[:len(ja[sec])] == list(ja[sec]), 'order changed'
            assert all(ja[sec][k] == jb[sec][k] for k in ja[sec]), 'an original %s entry changed' % sec
            add[sec] = {k: v for k, v in jb[sec].items() if k not in ja[sec]}
        else: assert ja[sec] == jb[sec]
    json.dump({'comment': 'v1.0 %s: voice-line database entries added; nothing original is changed. Each rule is a copy of a '
                          'Casey rule renamed with .KaraiMod / .ShredderMod, spoken by Karai_Hero / Shredder_Hero, with '
                          'Casey facts swapped for that hero\'s facts and that hero\'s voice lines.' % ver, 'add': add},
              open(os.path.join(out, 'banter_additions.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump(man, open(os.path.join(out, 'manifest.json'), 'w'), indent=1)
    print('%s: sources written to %s' % (ver, out))

if __name__ == '__main__':
    if len(sys.argv) != 4: print(__doc__); sys.exit(1)
    main(*sys.argv[1:])
