# Karai + Shredder: playable characters for TMNT: Splintered Fate

This is the source for the **Karai + Shredder** mod (Nexus Mods). It adds Karai and Shredder to the
character select screen as new characters: slot 9 for one of them, or 9 and 10 for both. The 8 normal
heroes stay as they are, and boss Karai and boss Shredder are not changed.

**Game:** TMNT: Splintered Fate, PC / Steam, the build with `TMNTSF.exe` SHA-1
`DF59708EC2F3B0A469CF7C8C0D2934510D42FE96`. Single-player only.

## What the mod is (and isn't)

- **There is no compiled program.** The installer is a plain-text PowerShell script,
  [`installer/KaraiShredderMod.ps1`](installer/KaraiShredderMod.ps1), started by
  [`installer/Install.bat`](installer/Install.bat). You can read every line of it.
- **The rest of the download is `.kpatch` data files.** Each one is a list of byte ranges:
  offset, new bytes, old bytes. The installer applies them to four game files and checks the
  SHA-1 before and after:

  | File | What changes |
  |---|---|
  | `TMNTSF.exe` | small code hooks for the new characters |
  | `PackData\overhead.pak2` | character data, art, and Shredder's purple-cape model |
  | `PackData\dupes.pak2` | voice-line rules |
  | `PackData\default.pak2` | select-screen layout |

- Every patch also stores the old bytes, so uninstalling puts the files back exactly.
  The installer also keeps `*.original-backup` copies, and it backs up your saves before it changes anything.
- The patches contain only bytes that come from the game itself, rearranged or recoloured.
  No outside art or sound is added. For that reason the `.kpatch` files are **not** in this repo:
  they're generated from your own game files (see BUILD.md) and shipped in the Nexus download.

## Repo layout

| Path | What it is |
|---|---|
| `installer/` | Install.bat, KaraiShredderMod.ps1 (install, switch, uninstall), README.txt (shipped in the zip) |
| `src/build_exe.py` | builds the v1.0.4 `TMNTSF.exe` for Karai, Shredder and Both, and their `exe_*.kpatch` |
| `src/patch_tvswap.py`, `patch_hover.py`, `patch_tool.py` | the exe changes made after v1.0 (lair TV swap, Karai hover lines, real tool markers) |
| `src/build_cape.py` | builds the v1.0.4 `overhead.pak2` (Shredder's purple cape) and `overhead_*.kpatch` |
| `src/kpatch.py` | makes and applies `.kpatch` files (same format the installer reads) |
| `src/pak.py`, `cff.py`, `tex.py`, `l8.py`, `hashes.py` | game file formats: pak2 archives, encrypted data records, BC1 textures, hashes |
| `src/pe.py`, `disx.py`, `xref.py`, `pdata.py` | exe inspection (disassembly, cross-references) |
| `src/emu*.py` | Unicorn emulation tests for the exe hooks |
| `docs/FORMATS.md` | the reverse-engineered file formats |
| `docs/HISTORY.md` | what each version changed |

See **[BUILD.md](BUILD.md)** for step-by-step build instructions.
