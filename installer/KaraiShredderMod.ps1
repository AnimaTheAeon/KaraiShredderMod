# Karai + Shredder Mod for TMNT: Splintered Fate - installer / uninstaller
# Every option goes straight from the original game files to the chosen version (one patch per file),
# and every patch can be run backwards, so uninstall works even without the backup copies.
$ErrorActionPreference = 'Stop'
$Host.UI.RawUI.WindowTitle = 'Karai + Shredder Mod - TMNT: Splintered Fate'
$Here = $PSScriptRoot
$ModVersion = '1.0.4'

# ---------- the 4 game files this mod changes ----------
# Orig = SHA1 of the unmodded Steam file. For each version: SHA1 after patching + the patch that gets there from Orig.
# Old = files from older mod versions (SHA1, patch from Orig, version). They are recognised so they can be removed or updated.
$Files = @(
  @{ Name='Game program (TMNTSF.exe)';     Rel='TMNTSF.exe';             Backup='TMNTSF.exe.original-backup';
     Orig='DF59708EC2F3B0A469CF7C8C0D2934510D42FE96';
     Karai=@('29DCD292306BE1D7E13A98964702070B51A24561','exe_karai.kpatch');
     Shredder=@('0E7EAAC827CFD9F24358AC40641143D74EFC9F2B','exe_shredder.kpatch');
     Both=@('F314C68894E000C0ECB1F8CB879FC9564FCB4C2A','exe_both.kpatch');
     Old=@( @('6D55D5E09E7CDA4E4B1154C3D65E6F0499CBB49C','exe_karai_v1.0.kpatch','Karai'),
            @('93EEA03FBD722384A754CDA5B996E8E0178A3FA3','exe_shredder_v1.0.kpatch','Shredder'),
            @('614F75438D9B5A8C04FCB752753DF555C2597821','exe_both_v1.0.kpatch','Both'),
            @('55EC81F8823CBCDB54F1472923438F79F04F9D96','exe_karai_v1.0.1.kpatch','Karai'),
            @('EFA936BED4C3D2730C3CBF8AB4F4388F2C0AAEEC','exe_shredder_v1.0.1.kpatch','Shredder'),
            @('49A00D2F6FE6434CAF8F34DEFD66A75F233FB736','exe_both_v1.0.1.kpatch','Both'),
            @('AC6E45EE40B5F76510F5ADE38B3823C0BF641F74','exe_karai_v1.0.2.kpatch','Karai'),
            @('575E4B407E5D44FA2EF98E0D097905F65437E0D9','exe_shredder_v1.0.2.kpatch','Shredder'),
            @('54ED395CFB3F7F57F0FC40DC5498AC41D290A116','exe_both_v1.0.2.kpatch','Both') ) },
  @{ Name='Main data (overhead.pak2)';     Rel='PackData\overhead.pak2'; Backup='overhead.pak2.original-backup';
     Orig='AD67E867B815A7D262EB7BD58B9B205ADA6C7EC7';
     Karai=@('357213F9D34C3AD1FC39403E98D96AEAC65AAE77','overhead_karai.kpatch');
     Shredder=@('0530B24F31DE3C2A97850553EF9178BCCC655BBA','overhead_shredder.kpatch');
     Both=@('0FFFBF831174EA9DF810FCF3C7FCBCA5893663FD','overhead_both.kpatch');
     Old=@( @('234F44EC85099C6434ED5C58ACC28683345A042E','overhead_shredder_v1.0.kpatch','Shredder'),
            @('668968C34823723CA3AA9053C7B55DEFE463A036','overhead_both_v1.0.kpatch','Both') ) },
  @{ Name='Voice lines data (dupes.pak2)'; Rel='PackData\dupes.pak2';    Backup='dupes.pak2.original-backup';
     Orig='8816893AB016B4CF57552C8BB064024C7F0B8206';
     Karai=@('454D6AD99D22E0A93F5049A3E9B989A2F9B6A488','dupes_karai.kpatch');
     Shredder=@('660F2BCC9D3766B82A5EB685BE062DE606EACA6B','dupes_shredder.kpatch');
     Both=@('C42581F6B1CCC52DBC82F96DB55BF7C0461F34DE','dupes_both.kpatch') },
  @{ Name='Menu layouts (default.pak2)';   Rel='PackData\default.pak2';  Backup='default.pak2.original-backup';
     Orig='F55E73ABC9C31C1427A1031DD1AF7A2C3B29F32C';
     Karai=@('19221B21CCA8A4017A125C981609058D6664F5A1','default_karai.kpatch');
     Shredder=@('5DA2CD2F4402070306BECD2D32335F2D469DEE02','default_shredder.kpatch');
     Both=@('52ED1D8B85CBAB21BA62713201B6BB0E7E8837FD','default_both.kpatch') }
)
$Versions = @('Karai','Shredder','Both')
$VersionText = @{ Karai='Karai (9th character)'; Shredder='Shredder (9th character)'; Both='Karai (9th) + Shredder (10th)'; Original='the original game (no mod)' }

function Say($msg, $color='Gray') { Write-Host $msg -ForegroundColor $color }
function Get-Sha1($path) { (Get-FileHash -LiteralPath $path -Algorithm SHA1).Hash }
function Game-Running { [bool](Get-Process -Name TMNTSF -ErrorAction SilentlyContinue) }

# ---------- find the game ----------
function Find-Game {
  $cands = @( (Split-Path -Parent $Here), $Here,
    'C:\Program Files (x86)\Steam\steamapps\common\Teenage Mutant Ninja Turtles Splintered Fate',
    'C:\Program Files\Steam\steamapps\common\Teenage Mutant Ninja Turtles Splintered Fate' )
  foreach ($vdf in 'C:\Program Files (x86)\Steam\steamapps\libraryfolders.vdf','C:\Program Files\Steam\steamapps\libraryfolders.vdf') {
    if (Test-Path $vdf) {
      foreach ($m in [regex]::Matches((Get-Content $vdf -Raw), '"path"\s+"([^"]+)"')) {
        $cands += (Join-Path ($m.Groups[1].Value -replace '\\\\','\') 'steamapps\common\Teenage Mutant Ninja Turtles Splintered Fate')
      }
    }
  }
  foreach ($c in $cands) { if ($c -and (Test-Path (Join-Path $c 'TMNTSF.exe')) -and (Test-Path (Join-Path $c 'PackData'))) { return $c } }
  Say "I couldn't find the game folder automatically." Yellow
  while ($true) {
    $p = (Read-Host 'Paste the game folder path (the one with TMNTSF.exe), or press Enter to cancel').Trim('"',' ')
    if (-not $p) { return $null }
    if ((Test-Path (Join-Path $p 'TMNTSF.exe')) -and (Test-Path (Join-Path $p 'PackData'))) { return $p }
    Say 'TMNTSF.exe and the PackData folder are not in that folder. Try again.' Red
  }
}

# ---------- apply a .kpatch forward or backwards ----------
# Format: 'KPAT', u64 old size, u64 new size, u32 count, then per range: u64 offset, u32 length, new bytes, old bytes.
function Apply-KPatch($target, $patchFile, [bool]$reverse) {
  if (-not (Test-Path -LiteralPath $patchFile)) { throw "Patch file missing: $(Split-Path -Leaf $patchFile). Re-extract the mod download." }
  $br = New-Object IO.BinaryReader([IO.File]::OpenRead($patchFile))
  try {
    $magic = [Text.Encoding]::ASCII.GetString($br.ReadBytes(4))
    if ($magic -ne 'KPAT') { throw "Bad patch file: $(Split-Path -Leaf $patchFile)" }
    $oldSize = $br.ReadUInt64(); $newSize = $br.ReadUInt64(); $count = $br.ReadUInt32()
    $fs = [IO.File]::Open($target, 'Open', 'ReadWrite', 'None')
    try {
      for ($i = 0; $i -lt $count; $i++) {
        $off = [int64]$br.ReadUInt64(); $len = [int]$br.ReadUInt32()
        $new = $br.ReadBytes($len); $old = $br.ReadBytes($len)
        $src = if ($reverse) { $old } else { $new }
        [void]$fs.Seek($off, 'Begin'); $fs.Write($src, 0, $len)
      }
      if ($reverse) { $fs.SetLength([int64]$oldSize) } else { $fs.SetLength([int64]$newSize) }
    } finally { $fs.Close() }
  } finally { $br.Close() }
}

# ---------- what is each file right now? ----------
function State-Of($f, $sha) {
  if ($sha -eq $f.Orig) { return 'Original' }
  foreach ($v in $Versions) { if ($sha -eq $f[$v][0]) { return $v } }
  if ($f.Old) { for ($i = 0; $i -lt $f.Old.Count; $i++) { if ($sha -eq $f.Old[$i][0]) { return "Old:$i" } } }
  return 'Unknown'
}

function Backup-Ok($game, $f) {
  $bak = Join-Path $game $f.Backup
  return (Test-Path -LiteralPath $bak) -and ((Get-Sha1 $bak) -eq $f.Orig)
}

function Scan($game) {
  Say "`nChecking your game files (the big ones take a few seconds each)..." Cyan
  $scan = @()
  foreach ($f in $Files) {
    $path = Join-Path $game $f.Rel
    if (-not (Test-Path -LiteralPath $path)) { Say "  MISSING: $($f.Rel)" Red; return $null }
    $sha = Get-Sha1 $path
    $scan += @{ F=$f; Path=$path; Sha=$sha; State=(State-Of $f $sha); BakOk=(Backup-Ok $game $f) }
  }
  return ,$scan
}

function State-Text($s) {
  if ($s.State -eq 'Unknown') { return 'not recognised' }
  if ($s.State -like 'Old:*') { return "$($VersionText[$s.F.Old[[int]$s.State.Substring(4)][2]]) - older mod version (pick it again to update)" }
  return $VersionText[$s.State]
}

function Overall($scan) {
  $states = @($scan | ForEach-Object { $_.State } | Select-Object -Unique)
  if ($states.Count -eq 1) { return $states[0] }
  return 'Mixed'
}

# ---------- put one file back to the original ----------
function To-Original($s, $game) {
  $f = $s.F
  if ($s.State -eq 'Original') { return }
  $patch = $null
  if ($Versions -contains $s.State) { $patch = $f[$s.State][1] }
  elseif ($s.State -like 'Old:*') { $patch = $f.Old[[int]$s.State.Substring(4)][1] }
  if ($patch) {
    try {
      Apply-KPatch $s.Path (Join-Path $Here $patch) $true
      if ((Get-Sha1 $s.Path) -eq $f.Orig) { return }
      Say "  $($f.Name): reverse patch didn't give the original, using the backup copy instead..." Yellow
    } catch {
      if (-not $s.BakOk) { throw }
      Say "  $($f.Name): $($_.Exception.Message) Using the backup copy instead..." Yellow
    }
  }
  if (-not $s.BakOk) { throw "can't restore $($f.Rel): no valid backup" }
  Copy-Item -LiteralPath (Join-Path $game $f.Backup) -Destination $s.Path -Force
  if ((Get-Sha1 $s.Path) -ne $f.Orig) { throw "restore check failed for $($f.Rel)" }
}

# ---------- install a version ----------
function Install-Version($game, $target) {
  $scan = Scan $game; if ($null -eq $scan) { return $false }
  # Pre-flight: refuse before touching anything if any file is unrecognised and has no good backup
  foreach ($s in $scan) {
    if ($s.State -eq 'Unknown' -and -not $s.BakOk) {
      Say "  $($s.F.Name): this is a version the mod doesn't recognise, so nothing was changed." Red
      Say '  The game was probably updated by Steam. This mod only works with the game version it was made for.' Yellow
      Say '  (Steam > right-click the game > Properties > Installed Files > Verify integrity gets you back to the original.)' Yellow
      return $false
    }
  }
  if (@($scan | Where-Object { $_.State -ne $target }).Count -eq 0) { Say "`nNothing to do - $($VersionText[$target]) is already installed." Green; return $true }
  # Disk space for the backup copies we still need to make
  $need = 0; foreach ($s in $scan) { if (-not $s.BakOk -and $s.State -ne $target) { $need += (Get-Item -LiteralPath $s.Path).Length } }
  if ($need -gt 0) {
    $drive = (Get-Item -LiteralPath $game).PSDrive
    if ($drive -and $drive.Free -lt ($need + 200MB)) { Say "  Not enough free disk space for the safety backups (need about $([math]::Round(($need+200MB)/1GB,1)) GB)." Red; return $false }
  }
  Say "`nBacking up your saves first..." Cyan; Backup-Saves
  foreach ($s in $scan) {
    $f = $s.F
    if ($s.State -eq $target) { Say "  $($f.Name): already right" Green; continue }
    try {
      if ($s.State -ne 'Original') { Say "  $($f.Name): removing the old version first ..." Gray; To-Original $s $game; $s.State = 'Original' }
      if (-not $s.BakOk) {
        Say "  Backing up the original $($f.Rel) ..." Gray
        Copy-Item -LiteralPath $s.Path -Destination (Join-Path $game $f.Backup) -Force
        if ((Get-Sha1 (Join-Path $game $f.Backup)) -ne $f.Orig) { throw 'backup check failed' }
        $s.BakOk = $true
      }
      Say "  $($f.Name): installing ..." Gray
      Apply-KPatch $s.Path (Join-Path $Here $f[$target][1]) $false
      if ((Get-Sha1 $s.Path) -ne $f[$target][0]) { throw 'check failed after patching' }
      Say "  OK: $($f.Name)" Green
    } catch {
      Say "  Problem with $($f.Name): $($_.Exception.Message)" Red
      Say '  Putting every file back to the original so the game still works...' Yellow
      [void](Uninstall-All $game $true)
      return $false
    }
  }
  Say "`nDONE! $($VersionText[$target]) is installed." Green
  return $true
}

# ---------- uninstall ----------
function Uninstall-All($game, [bool]$quiet) {
  $scan = Scan $game; if ($null -eq $scan) { return $false }
  foreach ($s in $scan) {
    if ($s.State -eq 'Unknown' -and -not $s.BakOk) {
      Say "  $($s.F.Name): this is a version the mod doesn't recognise and there's no backup, so it was left alone." Red
      Say '  (Steam > right-click the game > Properties > Installed Files > Verify integrity restores it.)' Yellow
      return $false
    }
  }
  $ok = $true
  foreach ($s in $scan) {
    try { To-Original $s $game; Say "  OK: $($s.F.Name) is original" Green }
    catch { Say "  Problem with $($s.F.Name): $($_.Exception.Message)" Red; $ok = $false }
  }
  if (-not $ok) { Say "`nSome files could not be restored. Use Steam's Verify integrity to fix them." Yellow; return $false }
  # Everything is verified original: the backup copies are no longer needed
  foreach ($f in $Files) {
    $bak = Join-Path $game $f.Backup
    if (Test-Path -LiteralPath $bak) { Remove-Item -LiteralPath $bak -Force }
  }
  if (-not $quiet) { Say "`nDONE! The game is back to 100% original, and the backup copies were removed." Green }
  return $true
}

# ---------- save backup ----------
function Backup-Saves {
  $save = Join-Path $env:APPDATA 'TMNTSF'
  if (-not (Test-Path $save)) { Say "  (No save folder found at $save - nothing to back up.)" DarkGray; return }
  $dst = Join-Path $env:APPDATA ('TMNTSF_save_backup_' + (Get-Date -Format 'yyyy-MM-dd_HH-mm-ss'))
  Copy-Item -LiteralPath $save -Destination $dst -Recurse -Force
  Say "  Saves backed up to: $dst" Green
}

# ---------- menu ----------
$game = Find-Game
if (-not $game) { Say 'Cancelled.'; exit }

while ($true) {
  Clear-Host
  Say '==============================================' Red
  Say "   KARAI + SHREDDER MOD v$ModVersion  -  TMNT: Splintered Fate" White
  Say '==============================================' Red
  Say "Game folder: $game" DarkGray
  Say ''
  Say '  1. Install Karai (9th character)'
  Say '  2. Install Shredder (9th character)'
  Say '  3. Install both: Karai 9th + Shredder 10th'
  Say '  4. Uninstall (back to the 100% original game)'
  Say '  5. Show what is installed right now'
  Say '  6. Exit'
  Say ''
  Say '  You can switch between 1, 2 and 3 at any time; the old version is removed first.' DarkGray
  Say ''
  $c = Read-Host 'Choose 1-6'
  if ($c -eq '6') { break }
  if ('1','2','3','4','5' -notcontains $c) { continue }
  if ($c -ne '5' -and (Game-Running)) { Say "`nSplintered Fate is running. Quit the game first, then choose again." Yellow; Read-Host 'Press Enter'; continue }
  $finished = $false
  try {
    switch ($c) {
      '1' { [void](Install-Version $game 'Karai'); $finished = $true }
      '2' { [void](Install-Version $game 'Shredder'); $finished = $true }
      '3' { [void](Install-Version $game 'Both'); $finished = $true }
      '4' { [void](Uninstall-All $game $false); $finished = $true }
      '5' {
        $scan = Scan $game
        if ($scan) {
          foreach ($s in $scan) { Say ("  {0}: {1}" -f $s.F.Name, (State-Text $s)) }
          $o = Overall $scan
          if ($VersionText.ContainsKey($o)) { Say "`nInstalled: $($VersionText[$o])" Green }
          elseif (@($scan | Where-Object { $_.State -like 'Old:*' }).Count -gt 0) { Say "`nAn older version of the mod is installed. Pick the same option again (1, 2 or 3) to update it to v$ModVersion." Yellow }
          else { Say "`nThe files don't all match one version. Pick 1-4 to fix that." Yellow }
        }
      }
    }
  } catch [UnauthorizedAccessException] {
    Say "`nWindows blocked writing to the game folder. Close this window, right-click Install.bat and choose 'Run as administrator'." Yellow
  } catch {
    Say "`nSomething went wrong: $($_.Exception.Message)" Red
  }
  if ($finished) { Read-Host "`nPress Enter to close this window"; break }
  Read-Host "`nPress Enter to go back to the menu"
}
