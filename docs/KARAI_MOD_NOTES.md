# TMNT: Splintered Fate — Playable Karai Mod: Complete Notes

**Purpose:** hand this file to Claude in a new chat to pick the project back up with full context.
The companion zip `KaraiMod_tools.zip` holds the Python tools, the edited records and textures, and the build scripts. Upload it alongside this file if you want Claude to rebuild or extend anything.

---

## 0. TL;DR / current state (as of 2026-11-16)

- **Goal:** make Karai playable in TMNT: Splintered Fate (Steam PC). She takes over **Casey Jones's** character slot. The long-term idea is a brand-new 9th slot.
- **Status: WORKING and confirmed in-game by the user**:
  - Karai model, skeleton and animations replace Casey's.
  - She moves and lunges while attacking like the turtles (it uses Casey's hero combo code).
  - Combo swings show Leonardo's katana slash effects. The finisher shows Karai's fire-ring "Dash_Slash" effect.
  - Combo animations are sped up 1.4–1.5× so swings line up with hits. The user says they now "match/work".
  - Her special is Karai's boss **Cleave**. The starting tool is **Kunai** (Casey's was Heckle).
  - Karai combat sounds and exertions (grunts) are in, and weapon swing audio works.
  - In-run chatter: all 581 Casey banter lines are repointed to Karai boss voice lines (taunts/yells). Confirmed working.
  - She is 0.88 scale, slightly smaller than default, to match the turtles.
  - Character art (select screen, cards) shows Karai.
  - The round HUD and run-summary portrait is Karai (default, Trenchcoat and Samurai skins).
  - The HUD dash icon is a running Karai.
- **Game path:** `C:\Program Files (x86)\Steam\steamapps\common\Teenage Mutant Ninja Turtles Splintered Fate`
- **To undo everything:** close the game and run `RESTORE_EVERYTHING.bat` in the game folder. It restores the exe, overhead.pak2 and dupes.pak2 from backups and moves the old mod paks aside. Steam "Verify integrity" also works.

### Files currently installed (modified)

| File | Version | SHA1 |
|---|---|---|
| `TMNTSF.exe` | karai v6 | `698557e0f693c3c18cbc2db4d09cc58dd5caf5a7` |
| `PackData\overhead.pak2` | karai v10 (395,891,392 bytes) | `2a933cf03227b5f3ac5b6d504143db698d99ac61` |
| `PackData\dupes.pak2` | voice-patched (419,108,288 bytes) | `B63183F3AA6A5A8B810C98D2DD17CF85253CB440` |
| `PackData\0KaraiMod.pak2`, `PackData\~~KaraiMod.pak2` | old experiment, harmless (the game ignores them) | |

### Backups in the game folder (originals)

| Backup | Original SHA1 |
|---|---|
| `TMNTSF.exe.original-backup` | `df59708ec2f3b0a469cf7c8c0d2934510d42fe96` |
| `overhead.pak2.original-backup` (395,055,808 bytes) | `ad67e867b815a7d262eb7bd58b9b205ada6c7ec7` |
| `dupes.pak2.original-backup` (418,850,240 bytes) | `8816893ab016b4cf57552c8bb064024c7f0b8206` (created by APPLY_KARAI_VOICE.bat) |

### One-click installer (the main way to install or uninstall now)
`KaraiMod.bat` sits in the game folder next to the `KaraiMod\` folder (`KaraiMod.ps1`, `exe.kpatch`, `overhead.kpatch`, `dupes.kpatch`, `README.txt`). The same package is in `KaraiMod_Installer.zip` (~13 MB).
- The menu offers **1. Install, 2. Uninstall, 3. Exit**. It finds the game automatically: its own parent folder, the default Steam path, other Steam libraries listed in `libraryfolders.vdf`, or it asks for the path. It refuses to run while `TMNTSF` is running.
- **Install:** SHA1-checks each file. Original files get backed up to `*.original-backup` and then patched; already-modded files are skipped. An unknown version (e.g. the game was updated) aborts without changing anything. Each file is verified after patching and auto-restored from backup if the check fails.
- **Uninstall:** reverse-applies the patch (the original bytes are stored in the .kpatch) or copies the backup back, then verifies the original SHA1.
- **.kpatch format:** `'KPAT'`, u64 old size, u64 new size, u32 range count, then for each range: u64 offset, u32 length, new bytes[length], old bytes[length]. Forward: write the new bytes, then truncate or extend to the new size. Reverse: write the old bytes, then truncate to the old size. Built by `tools/mkpatch.py` (`mkpatch(old, new, out)`).
- **To ship a new mod version:** rebuild the modded files, regenerate the 3 kpatches against the originals, and update the `Mod` SHA1s in the `$Files` table in KaraiMod.ps1.

### Scripts in the game folder

- `RESTORE_EVERYTHING.bat`: full undo (checks that the game is closed, restores the three files, verifies with `fc /b`).
- `APPLY_KARAI_VOICE.bat` plus `KaraiMod_patch\apply_karai_voice.ps1`, `dupes_header.bin`, `dupes_tail.bin`: patch dupes.pak2 in place. It backs up first, verifies the SHA1 afterwards and auto-restores if the check fails. It was needed because dupes.pak2 is larger than the 400 MB per-file limit for pushing files to the PC. Re-run it after a Steam verify or update.
- Older and obsolete: `RESTORE_ORIGINAL_EXE.bat`, `ENABLE_KARAI_MOD.bat`, `DISABLE_KARAI_MOD.bat`, `USE_KARAI_VOICE.bat`, `USE_KARAI_TEST_CASEY_SLOT.bat`, `TMNTSF_karai_voice.exe`, `TMNTSF_test_karai_in_casey_slot.exe`.
- Note: `scskiller.*` files (cfg, db, keys, log, csv, bin) also appeared in the game folder. **We did not create them.** They come from some other tool, so check what they are.

**A Steam update or "Verify integrity" will wipe the mod.** Reinstall from the saved outputs (overhead v10, exe v6), then re-run APPLY_KARAI_VOICE.bat. If the game itself updates, the record and texture hashes or offsets may change, and the exe string patches would need redoing against the new exe.

---

## 1. Engine and file formats (reverse-engineered)

- **Developer and engine:** Super Evil Megacorp ("SEMC"), proprietary engine (internal project name "Rebirth", "Nuo" framework). Source paths look like `C:\SEMC\Rebirth_Stab\Projects\Rebirth\Assets\...`.
- **Exe:** `TMNTSF.exe` (24,848,200 bytes), x64, **no SteamStub DRM**, so it is patchable directly. Audio is FMOD Studio (`fmod.dll`, `fmodstudio.dll`).
- **Data:** everything is in `PackData\*.pak2`: `overhead`, `dupes`, `direct`, `default`, `_PreloadCommon_`, `_PreloadDocks_`, `_PreloadJunkyard_`, `_PreloadRooftops_`, `_PreloadSewers_`, `_PreloadStreets_`.

### 1.1 PAK2 archive format

```
0x00 'PAK2'
0x04 01 00 01 00
0x08 u32 entry count
0x0C u32 0
0x10 u64 directory offset
0x18 u32 FNV-1a32(lowercase pak stem, e.g. "overhead")  -- a pak ID, not a checksum
... header padded to 0x1000
entries: zlib-compressed, each 4 KB (0x1000) aligned
directory: count × 32 bytes:
  u64 hash, u32 offset, u32 compressed size, u32 aligned size, u32 uncompressed size, u32 0, u32 flags (0x01000000 = zlib)
```

- Entry names are **64-bit hashes of unknown function**. Brute force with FNV-64, MD5 and SHA1 of paths (`build://...`) found nothing, so we always identify files by content.
- The directory is **not** sorted by hash.
- **Extra paks are ignored when they duplicate entries.** Dropping `0KaraiMod.pak2` or `~~KaraiMod.pak2` into PackData did nothing: the copy in the original pak wins. **So the mod must patch the original paks in place.**
- Patching method (`pakpatch.py`): if the new compressed data fits the entry's aligned slot, overwrite it in place. Otherwise, append it before the directory, move the directory to the end and update the dir offset at 0x10.

### 1.2 What's inside the paks

| Magic | Count | What |
|---|---|---|
| `RSC0` | ~8166 | 32-byte wrapper. Inside: CFF0 records (mostly shaders in dupes), anims (`01 00 00 00`, 30.0 fps, frame count) and other data |
| `// p` and `DXBC` | 4104 each | shader source and compiled bytecode |
| texture (no magic) | ~2057 BC plus 255 WebP | see 1.4 |
| `CFF0` | 440 (overhead) | encrypted game-data records (heroes, abilities, anim graphs, narrative...) |
| `UIML` | 118 | UI markup (binary). References like `build://HudImages:portrait_casey` and `build://MenuImages.atlas` |
| JSON | some | e.g. the **narrative/banter database** (dupes `19cff664ab3fd994`) |
| `direct.pak2` | | stored uncompressed: Ogg, MP3, RIFF and FMOD banks (audio) |

### 1.3 CFF0 records (encrypted game data)

```
0x00 'CFF0', header 0x40 bytes (u32 at +4 = total length)
chunks: tag(4) + u32 length (incl. 8-byte header) + body
  DEF0  byte [1] = key index (0..15)
  INST  encrypted record data (the actual struct blob)
  PTCH  u32 count, u32 ?, then (u32 ptr_offset, u32 target) pairs = relocation table.
        Pointer slots inside INST are stored as 0; PTCH says where each points.
  SYMB  (u32 offset, u32 typehash, '*SymbolName*' string), the exported symbols
Some records are wrapped in a 32-byte RSC0 header (sizes at +4 and +8).
```

**Cipher (cracked):** a per-dword stream with a Bob Jenkins lookup2 key.
```
KEYS = [0x6e0da13b,0x50daa98f,0x2d5ffa4f,0x56c6c3eb,0xcad31ddd,0x04f7be6a,0xd5c4e961,0x7fe2ef92,
        0xccbb8a6d,0x19b6875b,0x433b604c,0xba7b1ee4,0x9dea872e,0xa8c2e10a,0xed30a2ff,0x16a8f9a4]
n = len(INST);  h = lookup2(pack('<I', KEYS[DEF0[1]]), initval=n)
prev = n
for each u32 word c:   plain = rol(prev,1) ^ c ^ h ;  prev = c      (decrypt)
encrypt:               c = rol(prev,1) ^ plain ^ h ; prev = c
```
`cffrec.py` (`Rec.load(raw)` / `Rec.save()`) round-trips byte-exactly on all 439 overhead records. To edit a record, decrypt it, modify `inst` and `ptrs`, append new data at the end (keeping alignment), add PTCH entries for new pointers, then save.

**Symbol IDs** are compile-time FNV-1a32 of the full `"*Name*"` string, including the stars (e.g. `*CaseyJones_Hero*` = `0xc94d7a6e`). That's why patching roster **strings** in the exe did nothing: the code compares precomputed hashes.

### 1.4 Textures

```
0x00 u16 magic/varies (0x5598 BC3, 0xaae0 BC1 seen)
0x04 u32 mip count
0x08 u32 1
0x0C u32 format: 2 = BC1, 4 = BC3, 17/18/20 = WebP-compressed (RIFF/WEBP blob at 0x2C, length at 0x28)
0x10 u32 width, 0x14 u32 height
0x18 u32 SPRITE COUNT  (NOT depth! 1 for normal textures)
0x1C sprite table: count × 12 bytes = u32 name-hash, u16 x, u16 y, u16 w, u16 h  (coords in upright image space)
then mip data (header length = file size − sum of mip sizes)
```
- Pixel data is stored **vertically flipped**.
- Decode with `texture2ddecoder` (decode_bc1 or decode_bc3, which output BGRA). Encode with `etcpak.compress_bc3`, which expects **RGBA**. Mixing these up gives a red/blue swap.
- Sprite-name hash function: **unknown**. FNV, lookup2, CRC, murmur and xxhash were tried and none matched. Sprites were found by template-matching screenshots instead.
- Atlases are named in data as `Atlas.atlas:sprite`, e.g. `HudImages.atlas:portrait_casey`.
- **Gotcha that cost time:** an early decoder required the field at 0x18 to be 1, which silently skipped every multi-sprite atlas. Don't filter on it.

### 1.5 Anim files (RSC0)
At +32 in the RSC0: u32 1, f32 duration (s), u32 3, u32 size, f32 30.0 (fps), u32 frame count, then u32 track/bone count... Mapping from anim path to pak entry is unknown (hashed), so durations weren't matched to specific anims.

---

## 2. Game data structures that matter

### 2.1 Key records (overhead.pak2 entry hashes)

| Hash | What |
|---|---|
| `5635aea195a4e11c` | **Casey hero record** (`*CaseyJones_HeroData*`, `*CaseyJones_Hero*`, ActorReps, skins, portrait strings). **Modified.** |
| `84e188b8ea515d94` | **CaseyJonesAnimGraphTuning** (anim node table). **Modified.** |
| `1c12a84b01339d4c` | **Boss_Karai** record. The source of Karai's moves; read-only. |
| `b8a951520e937281` | Narrative record with 88 `event:/VO/ALLIES/CASEY/...` pointers. We repointed them to Karai, but **this had no audible effect**. The real banter comes from the JSON DB (2.6). |
| `5ce5356c8aced125`, `acc845ffeafb1213` (Don), `458f5abb8371dc4c` (Metalhead), `7151a2967ae0d393` (Slash), `1fe99fc5fb80dd9e` (Alopex), `0e2ff051f6d864af` (Raph), `3a041441f8385576` (Mikey) | other hero records |

### 2.2 Hero / actor struct offsets
- Hero actor type `0x2419fb6c` is the **same type as Boss_Karai**, so boss data can be grafted into the hero.
- Within the Casey record, the hero struct sits at INST offset `0x108`.
  - `hero+0x54`: **visual scale** (turtles 1.0, Casey 1.05, Metalhead 0.95). **Set to 0.88.**
  - `hero+0x108`: move speed (5.3). `hero+0x140`: health. Both untouched and available for balancing.
  - `hero+0x138`: **ability slot list** (NULL-terminated pointer array).
- **Ability slot:** +0x00 name, +0x08 input string (`primary`, `primary_2`, `special`, `dash`, `tool`...), +0x50 cooldown, plus fields 0x48–0x60, 0xE0–0xE8 and 0xF8–0x100 (copied from Casey's special onto Karai_Cleave to make it behave as a hero special).
- **ActorRep:** +0x00 mesh path, +0x08 skeleton path. Casey's mesh and skeleton strings (default, Samurai, Trenchcoat) now point to `build://Characters/NPCs/Karai/Model/Karai.mesh` and `.skeleton`.

### 2.3 How moves work (important finding)
- Move **behavior is C++ code**, not data. There's a registry of **2870** behavior factories in `.data` (`{name ptr, factory fn}`), e.g. `Abilities_CaseyJones.cpp` builds Casey's moves.
- Behavior pieces are requested by FNV-1a32 of the type name, e.g. `AB_LockMovement 0x8149e69d`, **`AB_Dash 0xd25eb241` (the hero lunge-forward on attacks)**, `AB_LockAbilities 0x360f10c6`, `BB_ScaleActor 0x1d6b7e45`.
- **Boss attacks lack AB_Dash**, which is why Karai "stood still while swinging" when she used her boss attacks. **The fix:** keep **Casey's hero combo code** (it lunges like the turtles) and play **Karai's animations** on it.
- Renaming slots to Leonardo's names did nothing, because Leo's code expects his partner slots.

### 2.4 Anim graph tuning record
- `root+8`: node array (NULL-terminated pointers). Node = 0x40 bytes: +0x00 name, +0x08 flags (01 = loop), +0x18 `.anim` path, **+0x20 f32 playback speed** (default 1.0; the game itself uses 1.2 and 2.0 in places), +0x2C f32 (usually 1.0; 99.0 or 9.0 on shuriken storm, possibly a loop count).
- Boss abilities look up nodes **by name**. We cloned 24 extra nodes into Casey's graph for the boss slot names (basicAttack, finishers, cleave, dash_*, parry_*, kunai_*, smokebomb_*...). Without them, boss moves didn't animate (v3 bug).
- **Casey to Karai anim mapping** (main ones):
  - Combo1 → `Karai_Default_Attack1` (**speed 1.5**)
  - Combo2 → `Attack1_Finisher1` (**speed 1.5**)
  - Combo3 → `Attack1_Finisher2` (**speed 1.4**)
  - Attack_Dash → `Dash_Slash`
  - Attack_Special → `Cleave`
  - Dash → `Dash_Loop`, Dash_End → `Dash_End`, Jump → `Dash_Start`
  - Idle → `Idle_InCombat`
  - Run, Run_Start and Run_180 → `Run`
  - Death → `Death`
  - Tool_ShurikenStorm → `ShurikenThrow`
  - Narrative and cinematic → `Idle_OutOfCombat`
  - Level exit ascend/portal → `SmokeBomb_Disappear`
- Available Karai anims (all `build://Characters/NPCs/Karai/Anims/`): Attack1, Attack1_Finisher1/2, BombShower, Cleave, DashCut_Attack/Loop/Start, Dash_End/Loop/Slash/Start, Death, Enrage, FlameWave, HitReaction, Idle_InCombat, Idle_OutOfCombat, KunaiStorm, Parry_Attack/Loop/Start, Run, ShurikenThrow, Karai_SmokeBomb_Disappear/Reappear.

### 2.5 Exe string patches (sound and effects are runtime path strings in .rdata)

Patched in place: the new string plus NUL padding to the old length. **File offsets** in TMNTSF.exe:

| Offset | Original (Casey) | Now |
|---|---|---|
| 0x11d2400 | `.../CaseyJones_Attack_01.pfx` | `build://Effects/Characters/Turtles/Leonardo/BasicAttacks/Leonardo_Attack_01/Leonardo_Attack_01.pfx` (v6) |
| 0x11d2320 | `.../CaseyJones_Attack_02.pfx` | `...Leonardo_Attack_02.pfx` (v6) |
| 0x11d2240 | `.../CaseyJones_Attack_03.pfx` | `...Leonardo_Attack_03.pfx` (v6) |
| 0x11d2b60 | `.../CaseyJones_Attack_04.pfx` | `build://Effects/Characters/Enemies/Karai/Karai_Dash_Slash/Karai_Dash_Slash.pfx` |
| 0x11d2390 | `Abi_Plr_CJ_Basic_Attack_Light_Play` | `event:/Combat/BOSSES/Karai/Combat_Karai_Attack_Light` |
| 0x11d22b0 | `Abi_Plr_CJ_Basic_Attack_Heavy_Impact_Play` | `event:/Combat/BOSSES/Karai/Combat_Karai_Attack_Heavy_01` |
| 0x11d21d0 | `Abi_Plr_CJ_Basic_Attack_Heavy_Leap_Play` | `event:/Combat/BOSSES/Karai/Combat_Karai_Dash_Prep_01` |
| 0x11b2720 | `Exertion_Casey_Dash` | `event:/Combat/BOSSES/Karai/Exertions_Karai_Shuriken` |
| 0x11d0eb0 | `Exertion_Casey_Throw` | `event:/Combat/BOSSES/Karai/Exertions_Karai_Shuriken` |
| 0x11c12d0 | `Exertion_Casey_Damage_Taken` | `event:/Combat/BOSSES/Karai/Exertions_Karai_DamageTaken` |
| 0x11c1570 | `Exertion_Casey_Stunned` | `event:/Combat/BOSSES/Karai/Exertions_Karai_DamageTaken` |

(Original Casey sound paths are under `event:/Combat/Abilities/Abilities_Player/Abi_Player_Casey_Jones/`.)
- In v5 the attacks 1–3 used Karai's boss pfx (`Karai_Attack_First/Second/Uppercut.pfx`). They **never appeared** during player combos (likely timed for the boss windup and cancelled by the next combo step). Only the finisher showed, so Leo's slashes replaced them in v6.
- Other Karai pfx available: `Karai_Attack_AOE`, `*_OnSword` variants, `Karai_Cleave`, `Karai_Dash`, `Karai_Dash_Uppercut`, `Karai_Enraged_Dash`, `Karai_Persistent_EyeTrails`, `Karai_Persistent_OnHead_AngryEyes`, `Karai_Persistent_OnSword`.
- The exe also lists atlases as `build://HudImages.atlas`, `build://DialogueImages.atlas`, etc.

### 2.6 Voice / banter (what finally worked)
- **Banter database = JSON in `dupes.pak2`, entry `19cff664ab3fd994`** (3.4 MB, keys: `files`, `criteria`, `events`, `responses` (2499), `rules` (2493)). Each response has `lines[]` of `{type:"vo", resource:"event:/VO/...", caption, delay, followup, volume}`.
- We replaced every `event:/VO/ALLIES/CASEY/...` resource (**581 unique lines**) with Karai boss lines, cycling through 71 (`event:/VO/BOSSES/KARAI/...`: NAR_BOSS_KARAI_*, BANTER_KAR_GLOBAL_DASHPREP / SUMMONADDS / TELEPORTPREP, ENRAGE arrays, DEATH and DEFEAT arrays...). Captions were swapped to the matching Karai caption keys.
- The JSON recompressed 669 bytes larger than its slot, so it was appended. The patch only touches pak header bytes 0–31 and everything from offset 418,799,616 to the end.

### 2.7 Art (textures replaced, all in overhead.pak2)

Source art: the official in-game Karai key art, texture `070a475246230d1f` (1024², BC3), already shipped with the game.

| Hash | What | Change |
|---|---|---|
| `0caddfc86e5b6901`, `1454e0837d499dbb`, `2aa89f6d7ddd5c1d`, `cd9444a99a103375`, `d54a9465f1df3857`, `ddde66a2eab40c54` | big Casey character art (select screen, cards) | Karai art scaled to 0.8× Casey's height, bottom-aligned, centered, full mips, BC3 |
| `7a66e24950374ffc` | **HudImages atlas** (2048², 120+ sprites: hero round portraits, HUD icons, bars) | sprite at (774,0) 256², hash `0x641ef2d8` = `portrait_casey`, now a Karai face in the teal ring on a dark-crimson background |
| `ac037af5cd094fd9` | **HudImages_2 atlas** (ability icons: dash runners, attack swooshes, weapons) | sprite at (756,0) 250², hash `0x302eaae6` = Casey dash, now a running Karai with cyan streaks |
| `d4f281b526b4f58c` | Trenchcoat skin sheet (`SkinSet0x`) | round Casey portrait at (258,823), hash `0x5a50c850`, now Karai |
| `96f496f5f7bc04d8` | Samurai skin sheet | round Casey portrait at (258,823), hash `0xa9590ec8`, now Karai |

- Ring geometry of round portraits (256²): black 0–3 px, teal 4–11, black 12–15, art disc radius ≈113.
- **Not yet replaced (possible next step):**
  - In `ac037af5cd094fd9`: sprite at (756,252) hash `0x8778821f` (Casey's blue hockey-swoosh attack icon, the "E" key), the hockey-stick weapon icon, and the Casey tool icon.
  - `Multiplayer.atlas:AvatarSelect_Casey` and `Frame_Ink_Casey`.
  - `Hero_CaseyAction.atlas:casey_2`.
  - The skin "cards" (rectangular Casey cards in the skin sheets).
  - `CaseyJones_Skin01/02.atlas`.
- Casey's sprite refs from the hero record: `HudImages.atlas:portrait_casey`, `Hero_CaseyAction.atlas:casey_2`, `Multiplayer.atlas:Frame_Ink_Casey`, `Multiplayer.atlas:AvatarSelect_Casey`, `HudImages_2.atlas:Attack_Casey`, `HudImages_2.atlas:Special_Casey`, `SkinSet01/02.atlas:CaseyJones_Skin0x_Button/_Icon/_Weapon`, `CaseyJones_Skin01/02.atlas:CaseyJones`.
- Patching method (`texpatch.py`): decode mip0, paste the sprite, then **re-encode only the touched 4×4 blocks in each mip** (downscaled with BOX). The rest of the atlas stays bit-identical.

---

## 3. Build history (what was tried, what failed, why)

1. **Exe roster string patch** (`*Slash_Hero*` or `*CaseyJones_Hero*` → `*Boss_Karai*`): no effect, because IDs are compile-time hashes.
2. **Extra mod pak** (`0KaraiMod.pak2` / `~~KaraiMod.pak2`): ignored. Switched to patching overhead.pak2 in place.
3. A swap .bat failed because the game was running. All bats now check `tasklist` and verify with `fc`.
4. **v1–v2: model and skeleton swap** in the Casey record, plus the Casey anim graph pointed at Karai anims. She loaded and animated, but Casey's moves and special remained.
5. **CFF0 cipher cracked** and the record editor built (`cffrec.py`, byte-exact). `decrypt_auto` sometimes picked the wrong seed, so the exact seed is now derived from the DEF0 key index.
6. **v3: transplanted the Boss_Karai INST and PTCH into the Casey record**, rewired slots to hero inputs, and set the special to Karai_Cleave. Boss moves didn't animate, because the hero graph lacked the boss node names.
7. **v4: cloned 24 boss-named anim nodes** into Casey's graph. Animations and grunts worked, but she **stood still** while attacking (boss attacks lack AB_Dash).
8. **Reverse-engineered the behavior registry** (2870 factories, code-built moves, AB_Dash hash).
9. **v5: Casey's hero combo code with Karai anims**, the Cleave special, the Kunai tool and the exe sound/pfx patches. She moved while swinging. The user then asked for her taunts.
10. Narrative CFF record repointed to Karai VO: **no audible effect** (wrong place).
11. Scale 0.88, and big character art replaced (encode bug: red/blue swap; fixed with RGBA for etcpak; art first too big, scaled to 0.8×).
12. **overhead v9: HUD portrait and dash icon** (found by template matching once the atlas-decode bug was fixed).
13. **exe v6, overhead v10, dupes patch:** Leo slash pfx on combos 1–3, combo anim speed ×1.4–1.5 and the **banter JSON** voice swap. **The user confirmed audio and swings work.**

Other gotchas: a background loop ran away on a wrong count field. `dis.py` shadowed a stdlib module (renamed to `disx.py`). Large file pushes to the PC failed (HTTP 404/400) until they went through "send file to chat, then commit by fileUuid". The per-file push limit is 400 MB, so dupes needed the in-place patch script.

---

## 4. Tooling (in KaraiMod_tools.zip → `tools/`)

| Script | Purpose |
|---|---|
| `pak2.py` | `entries(path)` yields (hash, data). CLI: `python pak2.py in.pak2 outdir` |
| `pakw.py` | `write_pak(path, stem, entries)`: new pak; `fnv1a32` |
| `pakpatch.py` | `patch_pak(src, dst, {hash: newbytes})`: in-place or append |
| `cff.py` | KEYS, `lookup2`, `decrypt_with`, `encrypt_with`, `decrypt_auto` |
| `cffrec.py` | `Rec.load(raw)` → `.inst` (bytearray), `.ptrs` [(off, target)], `.syms`; `Rec.save()` |
| `cffparse.py`, `rtti.py` | record and RTTI exploration helpers |
| `transplant.py` | `build(casey_raw, karai_raw, moves, drop)`: graft Karai data into the Casey record; `add_string`, `put_inplace`, `align` |
| `build_v4.py` | builds the hero record and anim graph (the v4/v5 logic; v10 then set node speeds at +0x20) |
| `texdec.py` | `decode(bytes)` → (PIL RGBA upright, info) for BC1, BC3 and WebP |
| `texpatch.py` | `patch_bc3(texbytes, [(img, x, y)])`: block-level re-encode per mip |
| `xref.py`, `disx.py` | PE helpers for TMNTSF.exe (string VAs, lea/call/pointer xrefs, function bounds via .pdata, capstone disassembly). Expect the original exe at `/mnt/user-data/outputs/TMNTSF.exe.original-backup` (edit the path) |

Python deps: `pefile capstone numpy pillow texture2ddecoder etcpak opencv-python-headless`.

Also in the zip:
- `mod/`: final records (`5635aea195a4e11c.bin` hero, `84e188b8ea515d94_v10.bin` anim graph, `b8a951520e937281.bin` narrative).
- `modtex/`: all 10 replaced textures.
- `vo/19cff664ab3fd994.bin`: the patched banter JSON.
- `animplan.json` and `karai_animmap.json`: anim mappings.
- `karai_vo.json`: the Karai VO list.
- `hud/`: the portrait and dash art PNGs.

**How to rebuild overhead from the original:** extract the original overhead, then `patch_pak(original, out, {hash: bytes})` for all replaced entries:
- the 3 records: hero, the **v10** anim graph, narrative
- the 10 textures

The game folder is a remote-device connected folder. To patch on the PC: send the file to chat, then commit it to the device path by fileUuid. Files over 400 MB need an in-place patch script like `apply_karai_voice.ps1`.

---

## 5. Ideas / next steps (not done)

- Replace the remaining Casey icons: the "E" attack swoosh, weapon icons, multiplayer avatar and frame, the `Hero_CaseyAction` card, the skin cards.
- **Balance:** health (`hero+0x140`), move speed (`hero+0x108`), Cleave cooldown (slot +0x50).
- Tune combo anim speeds (node +0x20) if swings feel off. Possibly use Karai's own `*_OnSword` pfx as an additional trail.
- Name and description text: the character still says "Casey" in menus (`UI_CHARACTER_NAME_15` and `UI_CHARACTER_DESCRIPTION_15` localization keys). The localization files haven't been located yet.
- Character-select voice and other non-banter Casey VO.
- **A true 9th character slot** (instead of replacing Casey): would require code changes (roster IDs are compile-time hashes), so it's much harder. The DLC heroes (Alopex, Metalhead, Slash, Casey) are the reference for how a hero is defined.
- Shredder: same approach, with his boss record as the donor.
