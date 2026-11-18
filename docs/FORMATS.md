# Game file formats (reverse-engineered)

These notes are for TMNT: Splintered Fate (Super Evil Megacorp), PC/Steam, exe SHA-1 `DF59708E…`.
Every address below is for that build. The exe is x64 and DYNAMIC_BASE (ASLR), so mod code uses
rip-relative addressing only.

## pak2 archives (`PackData\*.pak2`)
- **Header:**
  - `'PAK2'`, `01000100`, u32 entry count, 0;
  - u64 directory offset @0x10;
  - u32 FNV-1a32 of the lowercase pak name @0x18;
  - padded to 0x1000.
- **Entries:** zlib-compressed and 4 KB aligned.
- **Directory:** at the end, 32 bytes per entry: u64 key, u32 offset, u32 compressed size, u32 aligned size, u32 size, 0, flags (0x01000000 = zlib).
- **Extra pak files are ignored by the game**, so the mod patches the original paks in place.
  - A changed entry that fits its slot is rewritten in place.
  - Otherwise it is appended before the directory, and the directory is rewritten at the end.
  - See `src/pak.py`.

## Entry keys
- **Key** = `lookup8( MD5(asset path).hexdigest().upper() )`.
  - lookup8 is Bob Jenkins' 64-bit hash with level `0x123456789abcdeff` (exe 0x140742c50, called from 0x140d730b0).
  - The asset path has no `build://` and no leading `/`, and is case-sensitive.
  - Example: `Characters/NPCs/Shredder/Model/Shredder.mesh`.
- **Textures** are named by a 32-character uppercase hex GUID inside materials. Their key is `lookup8(GUID)`.

## CFF0 records (encrypted game data: heroes, abilities, animation graphs, materials…)
- **Layout:** 0x40-byte header, then chunks:
  - `DEF0`: byte 1 = key index;
  - `INST`: the encrypted struct data;
  - `PTCH`: pointer fixups;
  - `SYMB`: offset, type hash, `*Name*`.
  - Some records are wrapped in a 32-byte `RSC0` header.
- **Cipher:** a per-dword stream.
  - `h = lookup2(pack('<I', KEYS[idx]), initval=len)`, `prev = len`.
  - Decrypt: `p = rol(prev,1) ^ c ^ h; prev = c`.
  - The keys are in `src/cff.py`.
- **Symbol IDs** are FNV-1a32 of `"*Name*"`. Atlas sprite IDs are `lookup2(lowercase name, 0x12345678)`.
- **Materials** (`…shadergraph`) keep their texture GUIDs in plain text inside `SHD0` chunks.

## Textures
- **Header:** u32 total size, mips, 1, format (2 = BC1, 4 = BC3), width, height, sprite count, then 12-byte sprites.
- **Mips:** stored at the end of the file, rows bottom-up.
- `src/tex.py` decodes and re-encodes only the 4×4 blocks it changes, so every other block stays bit-identical.

## Models
A hero's ActorRep holds a `build://….mesh` path. The mesh file (RSC0) lists its material path(s) at 0x26.
The material lists its texture GUIDs. The v1.0.4 cape follows this chain; see `src/build_cape.py`.

## .kpatch
- **Header:** `'KPAT'`, u64 old size, u64 new size, u32 range count.
- **Each range:** u64 offset, u32 length, new bytes, old bytes.
- **Forward:** write the new bytes, then set the file length to the new size.
- **Reverse:** write the old bytes, then set the length to the old size.
