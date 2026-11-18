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

## `karai/`: the rest of the Karai v1.0 build
These scripts are as written, with the same hard-coded sandbox paths.

| Scripts | What they do |
|---|---|
| `build_slot9_data.py`, `build_step3a`…`3t.py` | Karai's hero, cards, actor reps, animation graph and moves, step by step, in Casey's record |
| `patch_exe_slot9.py`, `patch_exe_step2`…`3x.py` | the exe changes: 9th slot (hero model, select-screen table and loops), Karai's move hooks, banter facts, hover voice, text, HUD, Inspirations, and the hero-only Cleave damage and timing |
| `build_layout9.py`, `build_layout_banner.py` | the select-screen layout (UIML) for the 9th slot |
| `build_karai_atlas.py`, `set_karai_*.py`, `recolor_red.py`, `leo_*.py`, `gold_red*.py`, `draw_*.py`, `keyart.py` | Karai's select art and icons, recoloured from game art |
| `kpatch.py`, `sim_installer.py` | patch maker and the installer rehearsal from that period |
| `annot.py`, `fulldis.py`, `fdis.py`, `xr.py`, `callers.py`, `ripref.py`, `rangeref.py`, `leascan.py`, `leastr.py`, `regmap.py`, `scanmc.py`, `trackmc.py`, `dis_at.py`, … | the analysis helpers used to find each hook site |

## Not here
- **The Shredder v1.0 builders** (`sf.py`, `recedit.py`, `build_shred_data/atlas/banter/exe.py`) were lost.
  Their output is kept as readable source in [`src/v1_0/source/`](../src/v1_0/source/) (for Karai, Shredder
  and Both), and `src/v1_0/build.py` rebuilds the v1.0 files from it exactly. See BUILD.md, "The v1.0 base".
- **Game data.** Records and textures pulled from the paks are not included. Extract them from your own
  game files with the tools above.
