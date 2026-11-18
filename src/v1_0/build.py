"""Build a v1.0 version (karai, shredder or both) from the original game files + the readable sources.

Usage: python build.py <folder with the 4 original game files> <folder with the release .kpatch files> <karai|shredder|both> <out folder>

What comes from where:
  TMNTSF.exe      original + source/<version>/exe.asm (assembled with keystone)
  overhead.pak2   original + source/<version>/record_*.rec (each record rebuilt and re-encrypted)
                  + the texture atlases listed in manifest.json, taken from the release patch: their new
                    sprites are recoloured / resized game art, so the pixels are not stored in this repo.
                    `python ../decode_patch.py <original overhead.pak2> <patch> --png=out` exports them to look at.
                  + Karai only: older development copies of entries left between the live ones (the game never
                    reads them; manifest.json lists each one), also copied from the release so the SHA-1 matches.
  default.pak2    original + source/<version>/layout_*.json
  dupes.pak2      original + source/<version>/banter_additions.json
Every result is checked against the released v1.0 SHA-1. The .kpatch files written to <out> are also
compared with the released ones (an exe patch may group its byte ranges differently; the file it makes is identical).
"""
import os, sys, json, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
import kpatch, pak, asmfile, recfile, uimlfile
from gen_source import PATCHES, LAYOUT, BANTER

sha = lambda b: hashlib.sha1(b).hexdigest().upper()
ORIG = {'TMNTSF.exe': 'DF59708EC2F3B0A469CF7C8C0D2934510D42FE96', 'overhead.pak2': 'AD67E867B815A7D262EB7BD58B9B205ADA6C7EC7',
        'dupes.pak2': '8816893AB016B4CF57552C8BB064024C7F0B8206', 'default.pak2': 'F55E73ABC9C31C1427A1031DD1AF7A2C3B29F32C'}
WANT = {'karai': {'TMNTSF.exe': '6D55D5E09E7CDA4E4B1154C3D65E6F0499CBB49C', 'overhead.pak2': '357213F9D34C3AD1FC39403E98D96AEAC65AAE77',
                  'dupes.pak2': '454D6AD99D22E0A93F5049A3E9B989A2F9B6A488', 'default.pak2': '19221B21CCA8A4017A125C981609058D6664F5A1'},
        'shredder': {'TMNTSF.exe': '93EEA03FBD722384A754CDA5B996E8E0178A3FA3', 'overhead.pak2': '234F44EC85099C6434ED5C58ACC28683345A042E',
                     'dupes.pak2': '660F2BCC9D3766B82A5EB685BE062DE606EACA6B', 'default.pak2': '5DA2CD2F4402070306BECD2D32335F2D469DEE02'},
        'both': {'TMNTSF.exe': '614F75438D9B5A8C04FCB752753DF555C2597821', 'overhead.pak2': '668968C34823723CA3AA9053C7B55DEFE463A036',
                 'dupes.pak2': 'C42581F6B1CCC52DBC82F96DB55BF7C0461F34DE', 'default.pak2': '52ED1D8B85CBAB21BA62713201B6BB0E7E8837FD'}}

def place(orig, rep, lay, rel):
    """Write the rebuilt entries into overhead.pak2 at the positions the release used (manifest overhead_layout).
    Entries that fit stay in their original slot; moved entries go to their recorded offset. Leftover older
    copies between them (Karai only; the game never reads them) are copied from the release patch."""
    import struct, zlib
    d0, E = pak.read_dir(orig); E = [list(e) for e in E]; idx = {e[0]: i for i, e in enumerate(E)}
    b = bytearray(orig[:d0]) + bytearray(lay['directory_offset'] - d0)
    for k, data in rep.items():
        e = E[idx[k]]; c = zlib.compress(data, 9); ks = '%016x' % k
        if ks in lay['moved']: e[1], e[3] = lay['moved'][ks]
        assert len(c) <= e[3], 'entry %s does not fit its slot' % ks
        b[e[1]:e[1] + e[3]] = c + bytes(e[3] - len(c)); e[2] = len(c); e[4] = len(data)
    for a, z, what in lay['stale_blocks_from_release']:
        assert not any(b[a:z]), 'stale block overlaps a live entry'
        b[a:z] = rel[a:z]
    d1 = len(b); assert d1 == lay['directory_offset']
    for e in E: b += struct.pack('<QIIIIII', *e)
    struct.pack_into('<Q', b, 0x10, d1)
    return bytes(b)

def main(orig_dir, rel_dir, ver, out):
    SRC = os.path.join(HERE, 'source', ver); os.makedirs(out, exist_ok=True)
    man = json.load(open(os.path.join(SRC, 'manifest.json')))
    orig = {}
    for f, h in ORIG.items():
        orig[f] = open(os.path.join(orig_dir, f), 'rb').read()
        assert sha(orig[f]) == h, '%s is not the original Steam file' % f
    res = {}
    res['TMNTSF.exe'], ni, nr = asmfile.assemble(orig['TMNTSF.exe'], os.path.join(SRC, 'exe.asm'))
    print('%s exe: %d instructions assembled, %d raw lines (data / exact encodings)' % (ver, ni, nr))
    o = orig['overhead.pak2']; rep = {}
    rel_over = kpatch.apply(o, os.path.join(rel_dir, PATCHES[ver]['overhead.pak2']))
    for ks in man['overhead_order']:
        k = int(ks, 16)
        if ks in man['records']: rep[k] = recfile.build(pak.get(o, k), os.path.join(SRC, 'record_%s.rec' % ks))
        else: rep[k] = pak.get(rel_over, k)
    res['overhead.pak2'] = place(o, rep, man['overhead_layout'], rel_over)
    o = orig['default.pak2']
    res['default.pak2'] = pak.edit(o, replace={LAYOUT: uimlfile.build(pak.get(o, LAYOUT), os.path.join(SRC, 'layout_%016x.json' % LAYOUT))})
    o = orig['dupes.pak2']; j = json.loads(pak.get(o, BANTER))
    for sec, d in json.load(open(os.path.join(SRC, 'banter_additions.json')))['add'].items():
        for k in d: assert k not in j[sec], 'already present: %s' % k
        j[sec].update(d)
    res['dupes.pak2'] = pak.edit(o, replace={BANTER: json.dumps(j, separators=(',', ':'), ensure_ascii=False).encode()})
    ok = True
    for f in ('TMNTSF.exe', 'overhead.pak2', 'dupes.pak2', 'default.pak2'):
        data = res[f]; want = WANT[ver][f]; pname = PATCHES[ver][f]
        kp = kpatch.make(orig[f], data); open(os.path.join(out, pname), 'wb').write(kp)
        same_patch = kp == open(os.path.join(rel_dir, pname), 'rb').read()
        good = sha(data) == want; ok &= good
        print('  %-14s %s  %s   (.kpatch byte-identical to the release: %s)' % (f, sha(data), 'OK, same as release' if good else 'MISMATCH (want %s)' % want,
              'yes' if same_patch else 'no; byte ranges grouped differently, same resulting file' if good else 'no'))
    if not ok: sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 5: print(__doc__); sys.exit(1)
    main(*sys.argv[1:])
