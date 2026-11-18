# Patch reports

One plain-text report for each `.kpatch` in the current download, made with
`python src/decode_patch.py <original game file> <patch>`.

| Report | Patch | Game file |
|---|---|---|
| `exe_<build>.txt` | `exe_<build>.kpatch` | `TMNTSF.exe` |
| `overhead_<build>.txt` | `overhead_<build>.kpatch` | `PackData\overhead.pak2` |
| `dupes_<build>.txt` | `dupes_<build>.kpatch` | `PackData\dupes.pak2` |
| `default_<build>.txt` | `default_<build>.kpatch` | `PackData\default.pak2` |

`<build>` is `karai`, `shredder` or `both`. Run the decoder yourself on the download to check that a
report matches. Add `--png=folder` to also save the art that changed as images.
