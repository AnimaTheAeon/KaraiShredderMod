# v1.0 toolkit: the original Karai tools

These are the first tools used to build Karai, kept **as they were written**. They still have the
original sandbox paths (`/home/claude/...`) hard-coded at the top.

| File | What it does |
|---|---|
| `tools/pak2.py`, `pakw.py`, `pakpatch.py` | read pak2 archives, write them, and patch an entry in place or append it |
| `tools/cff.py`, `cffparse.py`, `cffrec.py` | decrypt and parse CFF0 game-data records, and edit and re-save them byte-exactly |
| `tools/transplant.py` | copies a boss's ability data into a hero record and rewires it to hero inputs |
| `tools/build_v4.py` | the Karai record build at stage v4: Casey record + Karai moves, anims remapped with `maps/` |
| `tools/texdec.py`, `texpatch.py` | decode BC textures and paste a sprite, re-encoding only the touched blocks |
| `tools/xref.py`, `disx.py`, `rtti.py`, `old_dis_helper.txt` | exe cross-reference, disassembly and RTTI helpers |
| `tools/mkpatch.py` | an early patch maker (the release uses `src/kpatch.py`) |
| `maps/animplan.json` | which Casey animation slots point to which Karai animation |
| `maps/karai_animmap.json` | Casey to Karai animation name map |
| `maps/karai_vo.json` | the Karai boss voice events used for her lines |

`docs/KARAI_MOD_NOTES.md` is the build log from that period: what was tried, what failed and why.

## Not here
- **The later v1.0 builders.** Karai's step-3 record, art and slot-9 exe scripts, and the Shredder
  builders, were made in later sessions that aren't in this archive. `docs/HISTORY.md` and
  `docs/FORMATS.md` describe what they change.
- **Game data.** Records and textures pulled from the paks are not included. Extract them from your own
  game files with the tools above.
