# Grow Boss_Karai.atlas (karai_0 dialogue portrait, 1024x1024 BC3) to 1024x2048 and add two new sprites:
#   karai_select : 360x480 framed card for the character-select thumbnail
#   karai_hud    : 256x256 round HUD portrait (teal ring, same style as the turtles')
import sys, struct, numpy as np, etcpak, texture2ddecoder
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, '/home/claude/work/tools')
from cff import lookup2
src, hudpng, out, preview = sys.argv[1:5]
d = open(src, 'rb').read()
size, mips, one, fmt, W, H, ns = struct.unpack_from('<IIIIIII', d, 0)
assert (fmt, W, H, ns) == (4, 1024, 1024, 1) and size == len(d)
spr0 = d[0x1c:0x28]
hl = 0x1c + 12 * ns
art = Image.frombytes('RGBA', (W, H), texture2ddecoder.decode_bc3(d[hl:hl + W * H], W, H), 'raw', 'BGRA').transpose(Image.FLIP_TOP_BOTTOM)

# ---- select card 360x480: same tilted/skewed card shape as the other heroes' AvatarSelect thumbnails ----
CW, CH = 360, 480
S = 2                                                     # supersample for smooth edges
FW, FH = 340 * S, 456 * S                                 # flat card before warping
B = 9 * S                                                 # light outer border, like the others
bust = art.crop((530, 190, 530 + 240, 190 + 320)).resize((FW - 2 * B, FH - 2 * B), Image.LANCZOS)
g = np.zeros((FH - 2 * B, FW - 2 * B, 4), np.uint8)
yy = np.linspace(0, 1, FH - 2 * B)[:, None]
g[..., 0] = (120 + 70 * (1 - yy)).astype(np.uint8); g[..., 1] = (18 + 10 * (1 - yy)).astype(np.uint8); g[..., 2] = (34 + 18 * (1 - yy)).astype(np.uint8); g[..., 3] = 255
inner = Image.fromarray(g, 'RGBA')
hd = ImageDraw.Draw(inner)
for y in range(0, FH - 2 * B, 14 * S):
    for x in range((y // (14 * S)) % 2 * 7 * S, FW - 2 * B, 14 * S):
        r = (1.5 + 2.5 * (y / (FH - 2 * B))) * S
        hd.ellipse([x - r, y - r, x + r, y + r], fill=(90, 10, 24, 255))
inner.alpha_composite(bust)
flat = Image.new('RGBA', (FW, FH), (245, 240, 232, 255))
flat.paste(inner, (B, B))
ImageDraw.Draw(flat).rectangle([B - 3 * S // 2, B - 3 * S // 2, FW - B + 3 * S // 2 - 1, FH - B + 3 * S // 2 - 1], outline=(20, 18, 22, 255), width=3 * S // 2 + 1)
# target quad (measured from the in-game Leo/Alopex thumbnails, normalised): TL(0,0) TR(.963,.059) BR(1,1) BL(.079,.987)
mx, my = 5 * S, 4 * S; QW, QH = CW * S - 2 * mx, CH * S - 2 * my
Q = [(mx + nx * QW, my + ny * QH) for nx, ny in [(0, 0), (.963, .059), (1, 1), (.079, .987)]]
# perspective coeffs mapping output pixel -> flat-card pixel
src = [(0, 0), (FW, 0), (FW, FH), (0, FH)]
A = []; bb = []
for (x, y), (u, v) in zip(Q, src):
    A.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); bb.append(u)
    A.append([0, 0, 0, x, y, 1, -v * x, -v * y]); bb.append(v)
coef = np.linalg.solve(np.array(A, float), np.array(bb, float))
big = flat.transform((CW * S, CH * S), Image.PERSPECTIVE, tuple(coef), Image.BICUBIC)
mask = Image.new('L', (CW * S, CH * S), 0); ImageDraw.Draw(mask).polygon(Q, fill=255)
big.putalpha(Image.fromarray(np.minimum(np.asarray(big.getchannel('A')), np.asarray(mask))))
card = big.resize((CW, CH), Image.LANCZOS)

# ---- big select art 1000x888: centred like the other heroes (their centroid ~350-450, Karai's was 733) ----
# scale 1.1 about her bottom-centre, move her centre to x~430, fade the hard right edge of the source art
SC, CX0, CX1 = 1.10, 733.0, 430.0
src0 = art.crop((0, 0, 1000, 888))
bigw, bigh = int(1000 * SC), int(888 * SC)
sc = src0.resize((bigw, bigh), Image.LANCZOS)
ox = int(round(CX1 - CX0 * SC)); oy = 888 - bigh
bigart = Image.new('RGBA', (1000, 888), (0, 0, 0, 0)); bigart.alpha_composite(sc.crop((max(0, -ox), max(0, -oy), max(0, -ox) + 1000, max(0, -oy) + 888)), (max(0, ox), max(0, oy)))
edge = ox + bigw                     # where the source's cut right edge now sits
fa = np.asarray(bigart).copy(); ramp = np.clip((edge - np.arange(1000)) / 70.0, 0, 1)
fa[..., 3] = (fa[..., 3] * ramp[None, :]).astype(np.uint8); bigart = Image.fromarray(fa, 'RGBA')
print('big art: offset', ox, 'right edge', edge)

# ---- HUD round portrait 256x256 (from the old mod's art) ----
hud = Image.open(hudpng).convert('RGBA').resize((256, 256), Image.LANCZOS)

# ---- new 1024x2048 canvas ----
NW, NH = 2048, 2048
canvas = Image.new('RGBA', (NW, NH), (0, 0, 0, 0))
canvas.paste(art, (0, 0))
SEL = (16, 1040, CW, CH); HUD = (400, 1040, 256, 256)
BIG = (1024, 0, 1000, 888); SPC = (1024, 900, 250, 250); KUN = (1290, 900, 200, 200); DSH = (1500, 900, 250, 250)
HUDS = [('karai_special_hud',(1024,1160,250,250)),('karai_dash_hud',(1290,1160,250,250)),('karai_kunai_hud',(1550,1160,200,200)),('karai_insp1',(1780,900,200,200)),('karai_insp2',(1780,1160,200,200)),('karai_katana',(1024,1420,250,250))]   # in-run HUD versions with a baked ring
dash = Image.open('/home/claude/s3j/karai_dash_red.png').convert('RGBA')   # old Karai dash art, cyan streaks turned red
kunai = Image.open('/home/claude/s3j/karai_kunai.png').convert('RGBA')   # Alopex's Kunai tool icon recoloured crimson
special = Image.open('/home/claude/s3j/karai_special.png').convert('RGBA')   # Leo's special icon recoloured crimson
canvas.paste(card, SEL[:2]); canvas.paste(hud, HUD[:2]); canvas.paste(bigart, BIG[:2]); canvas.paste(special, SPC[:2]); canvas.paste(kunai, KUN[:2]); canvas.paste(dash, DSH[:2])
for _n,_r in HUDS: canvas.paste(Image.open('/home/claude/s3j/%s.png' % _n).convert('RGBA'), _r[:2])

def levels(w, h):
    lv = []
    while True:
        lv.append((w, h))
        if w == 1 and h == 1: break
        w = max(1, w // 2); h = max(1, h // 2)
    return lv
LV = levels(NW, NH)
blob = bytearray()
for i, (w, h) in enumerate(LV):
    img = canvas if i == 0 else canvas.resize((w, h), Image.BOX)
    st = np.array(img.transpose(Image.FLIP_TOP_BOTTOM))
    pw, ph = max(4, (w + 3) // 4 * 4), max(4, (h + 3) // 4 * 4)
    if (pw, ph) != (w, h):
        pad = np.zeros((ph, pw, 4), np.uint8); pad[:h, :w] = st; st = pad
    blob += etcpak.compress_bc3(np.ascontiguousarray(st).tobytes(), pw, ph)
sprites = [spr0,
           struct.pack('<IHHHH', lookup2(b'karai_select', 0x12345678), *SEL),
           struct.pack('<IHHHH', lookup2(b'karai_hud', 0x12345678), *HUD),
           struct.pack('<IHHHH', lookup2(b'karai_big', 0x12345678), *BIG),
           struct.pack('<IHHHH', lookup2(b'karai_special', 0x12345678), *SPC),
           struct.pack('<IHHHH', lookup2(b'karai_kunai', 0x12345678), *KUN),
           struct.pack('<IHHHH', lookup2(b'karai_dash', 0x12345678), *DSH)] + [struct.pack('<IHHHH', lookup2(_n.encode(), 0x12345678), *_r) for _n,_r in HUDS]
hdr = bytearray(d[:0x1c]) + b''.join(sprites)
total = len(hdr) + len(blob)
struct.pack_into('<IIIIIII', hdr, 0, total, len(LV), one, fmt, NW, NH, len(sprites))
data = bytes(hdr) + bytes(blob)
assert len(data) == total
open(out, 'wb').write(data)
# preview: decode back
px = texture2ddecoder.decode_bc3(data[len(hdr):len(hdr) + NW * NH], NW, NH)
back = Image.frombytes('RGBA', (NW, NH), px, 'raw', 'BGRA').transpose(Image.FLIP_TOP_BOTTOM)
pv = Image.new('RGBA', (NW, NH), (60, 60, 60, 255)); pv.alpha_composite(back)
pv.convert('RGB').resize((1024, 1024)).save(preview)
back.crop((BIG[0], BIG[1], BIG[0] + 1000, BIG[1] + 888)).save(preview.replace('.png', '_big.png'))
back.crop((SEL[0], SEL[1], SEL[0] + CW, SEL[1] + CH)).save(preview.replace('.png', '_card.png'))
print('ok', total, 'mips', len(LV), 'karai_select', hex(lookup2(b'karai_select', 0x12345678)), 'karai_hud', hex(lookup2(b'karai_hud', 0x12345678)))
