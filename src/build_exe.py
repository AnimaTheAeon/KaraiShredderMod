"""Build the v1.0.4 TMNTSF.exe for all three mod versions (Karai / Shredder / Both).

The v1.0.4 exe is the same as v1.0.3. Steps, starting from the v1.0 mod exe:
  1. patch_tvswap.py  - lair TV hero swap for Karai / Shredder (+ swap voice line)   [v1.0.1/1.0.2]
  2. patch_hover.py   - Karai says 1 of 6 lines on the select screen (Karai, Both)   [v1.0.2]
  3. patch_tool.py    - Karai/Shredder own their real tool marker (Kunai/Smoke Bomb)  [v1.0.3]

Usage:
  python build_exe.py <original TMNTSF.exe> <folder with exe_*_v1.0.kpatch> <out folder>
Writes out/TMNTSF_<build>.exe and out/exe_<build>.kpatch and checks every SHA-1.
"""
import os, sys, hashlib, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import kpatch

ORIG_SHA = 'DF59708EC2F3B0A469CF7C8C0D2934510D42FE96'
WANT = {'karai': '29DCD292306BE1D7E13A98964702070B51A24561',
        'shredder': '0E7EAAC827CFD9F24358AC40641143D74EFC9F2B',
        'both': 'F314C68894E000C0ECB1F8CB879FC9564FCB4C2A'}
# free space in the mod's own .karai/.shred section for each build: (TV-swap cave, tool cave)
CAVES = {'karai': (0x14186fc00, 0x14186fea0), 'shredder': (0x141870800, 0x141870900), 'both': (0x141872800, 0x141872900)}
sha = lambda b: hashlib.sha1(b).hexdigest().upper()

def run(*a): subprocess.run([sys.executable, *a], check=True)

def main(orig_path, v10_dir, out):
    os.makedirs(out, exist_ok=True)
    orig = open(orig_path, 'rb').read()
    assert sha(orig) == ORIG_SHA, 'not the original Steam TMNTSF.exe (SHA-1 %s)' % sha(orig)
    for b in ('karai', 'shredder', 'both'):
        step = lambda n: os.path.join(out, f'_{b}_{n}.exe')
        open(step(0), 'wb').write(kpatch.apply(orig, os.path.join(v10_dir, f'exe_{b}_v1.0.kpatch')))
        run(os.path.join(HERE, 'patch_tvswap.py'), step(0), step(1), hex(CAVES[b][0]), b); cur = step(1)
        if b in ('karai', 'both'):
            run(os.path.join(HERE, 'patch_hover.py'), cur, step(2)); cur = step(2)
        final = os.path.join(out, f'TMNTSF_{b}.exe')
        run(os.path.join(HERE, 'patch_tool.py'), cur, final, hex(CAVES[b][1]), b)
        data = open(final, 'rb').read()
        assert sha(data) == WANT[b], f'{b}: got {sha(data)}, expected {WANT[b]}'
        open(os.path.join(out, f'exe_{b}.kpatch'), 'wb').write(kpatch.make(orig, data))
        for n in range(3):
            if os.path.exists(step(n)): os.remove(step(n))
        print(f'OK {b}: {sha(data)}')

if __name__ == '__main__':
    if len(sys.argv) != 4: print(__doc__); sys.exit(1)
    main(*sys.argv[1:])
