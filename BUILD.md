# How to build

You build the release from **your own copy of the game files**. Nothing from the game is stored in this repo.

## 1. What you need

- **Windows, macOS or Linux with Python 3.10+.** Install the packages:

  ```
  pip install pefile capstone keystone-engine unicorn numpy scipy pillow texture2ddecoder etcpak
  ```
- **The original, unmodded game files** (Steam: right-click the game > Properties > Installed Files >
  Verify integrity). Check their SHA-1:

  | File | SHA-1 |
  |---|---|
  | `TMNTSF.exe` | `DF59708EC2F3B0A469CF7C8C0D2934510D42FE96` |
  | `PackData\overhead.pak2` | `AD67E867B815A7D262EB7BD58B9B205ADA6C7EC7` |
  | `PackData\dupes.pak2` | `8816893AB016B4CF57552C8BB064024C7F0B8206` |
  | `PackData\default.pak2` | `F55E73ABC9C31C1427A1031DD1AF7A2C3B29F32C` |
  | `PackData\_PreloadRooftops_.pak2` | read only, never changed |

- **The v1.0 base patches** from the mod download, the `*_v1.0.kpatch` files plus `dupes_*`,
  `default_*` and `overhead_karai.kpatch`. See "The v1.0 base" below.

## 2. Build the exe (v1.0.4 = v1.0.3 code)

```
python src/build_exe.py "<game>\TMNTSF.exe" "<folder with exe_*_v1.0.kpatch>" out
```

For each build (karai, shredder, both) this:
1. applies `exe_<build>_v1.0.kpatch` to the original exe;
2. runs `patch_tvswap.py`, which adds the lair-TV swap rule for the new hero(es);
3. runs `patch_hover.py` (Karai and Both only), which makes Karai say 1 of 6 lines on the select screen;
4. runs `patch_tool.py`, which gives Karai and Shredder their real tool markers (Kunai and Smoke Bomb);
5. checks the SHA-1 and writes `out/exe_<build>.kpatch`.

Each patch script asserts that its target bytes are the original instructions and that its cave is empty
before it writes anything.

## 3. Build overhead.pak2 (v1.0.4 purple cape)

```
python src/build_cape.py "<game>\PackData\overhead.pak2" "<game>\PackData\_PreloadRooftops_.pak2" "<folder with overhead_*_v1.0.kpatch>" out
```

This copies Shredder's model, material and texture out of `_PreloadRooftops_.pak2`, recolours the cape
purple, adds the copies to `overhead.pak2` under new names, and points only the playable Shredder at
them. Boss Shredder still uses the untouched originals. It writes `out/overhead_shredder.kpatch` and
`out/overhead_both.kpatch` and checks the SHA-1s.

## 4. Expected results

Both scripts stop with an error if anything differs.

| Output | SHA-1 of the patched file |
|---|---|
| exe karai | `29DCD292306BE1D7E13A98964702070B51A24561` |
| exe shredder | `0E7EAAC827CFD9F24358AC40641143D74EFC9F2B` |
| exe both | `F314C68894E000C0ECB1F8CB879FC9564FCB4C2A` |
| overhead shredder | `0530B24F31DE3C2A97850553EF9178BCCC655BBA` |
| overhead both | `0FFFBF831174EA9DF810FCF3C7FCBCA5893663FD` |

The `.kpatch` files these scripts produce are byte-identical to the ones in the v1.0.4 download.

## 5. Make the release folder

Copy into one folder:
- `installer/*`;
- the five `.kpatch` files from `out/`;
- the unchanged v1.0 patches: `overhead_karai`, `dupes_*`, `default_*`;
- the older-version patches the installer uses to update or remove old installs:
  `exe_*_v1.0*.kpatch` and `overhead_{shredder,both}_v1.0.kpatch`.

Zip it.

## 6. Tests

- `python src/emu_tool.py out` and `python src/emu_hover.py out` run the new exe hooks in the
  Unicorn emulator for every hero, the bosses, and right and wrong inputs.
- `python src/emu.py out/TMNTSF_both.exe` checks the lair-TV hook.

## The v1.0 base

v1.0 built the characters themselves:
- new hero, card, animation and model records;
- select-screen art;
- the 9th/10th slot code;
- the voice rules.

It was built over several sessions:
- **The original toolkit** is in [`v1.0-toolkit/`](v1.0-toolkit/), as it was written. It covers the pak2
  reader and writer, the CFF0 record decrypter and editor, the boss-to-hero ability transplant, the
  texture patcher and the Karai v4 record build.
- **The later v1.0 build scripts** aren't in this repo. `docs/HISTORY.md`, `docs/FORMATS.md` and
  `docs/KARAI_MOD_NOTES.md` describe what they change and how.
- **The v1.0 patches** are in the Nexus download. Every change after v1.0 is rebuilt from source here.

The patch format is plain: each range lists its offset, the new bytes and the original bytes, so
`src/kpatch.py` can inspect or reverse any patch.
