import sys, struct
sys.path.insert(0, '/home/claude/work/tools')
from texdec import decode
from PIL import Image
d = open('/home/claude/ovh/070a475246230d1f.bin', 'rb').read()
mips, one, fmt, w, h, ns = struct.unpack_from('<IIIIII', d, 4)
print(mips, fmt, w, h, ns, [struct.unpack_from('<IHHHH', d, 0x1c + 12 * i) for i in range(ns)])
im = decode(d)[0]
bg = Image.new('RGBA', im.size, (70, 70, 70, 255)); bg.alpha_composite(im)
bg.convert('RGB').resize((512, 512)).save('/home/claude/keyart.png')
