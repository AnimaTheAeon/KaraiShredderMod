# Version history

## v1.0: the characters
- **Karai:** slot 9 (alone or with Shredder).
  - Built on Casey's hero record, data appended so Casey's own bytes stay the same.
  - New hero, cards, model reference and animation graph using Karai's boss animations with Casey's combo code.
  - Cleave special (hero-only damage hooks; boss Karai's Cleave unchanged); Kunai tool.
  - Select art and icons recoloured from game art; voice rules cloned from Casey's with Karai's boss lines.
- **Shredder:** slot 9 alone, or 10 with Karai.
  - Built on Raph's hero record the same way.
  - Spinning Heel special, Smoke Bomb tool, Leonardo's Inspirations, purple select art, Shredder's own voice lines.
  - Boss Shredder's record is untouched.
- **Exe:** a new code section with hooks that check the hero's ID first, so the bosses and the other heroes run the original code. It also has the 9/10-slot select-screen code.
- **default.pak2:** select-screen layout for the extra slot(s).
- **dupes.pak2:** the voice-line rule database.

## v1.0.1: lair TV swap (`patch_tvswap.py`)
The lair's level logic only had swap rules for the original heroes. The patch adds the same rule for Karai and Shredder.

## v1.0.2: voice lines (`patch_tvswap.py`, `patch_hover.py`)
- Swapping at the TV fires Casey's swap event, which the mod's cloned Karai/Shredder rules answer, so they say a line.
- Karai says 1 of 6 lines on the select screen.

## v1.0.3: real tools (`patch_tool.py`)
Karai and Shredder now own their real tool markers, Kunai and Smoke Bomb. Upgrade offers show the right name and icon, and upgrades make the right tool stronger.

## v1.0.4: purple cape (`build_cape.py`)
The playable Shredder gets his own copy of the model, material and texture, with the cape recoloured purple. Boss Shredder keeps the original red files.
