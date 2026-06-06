from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

W, H = 1200, 800
DEEP = (13, 11, 26)
CARD = (31, 24, 48)
ACCENT = (139, 26, 74)
GOLD = (201, 150, 58)
BLUSH = (232, 160, 176)
MUTED = (154, 138, 170)

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

def load_font(names, size):
    for n in names:
        for base in (r"C:\Windows\Fonts", ""):
            p = os.path.join(base, n) if base else n
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()

serif = lambda s: load_font(["georgiab.ttf", "georgia.ttf", "times.ttf"], s)
sans  = lambda s: load_font(["segoeui.ttf", "arial.ttf"], s)

def heart(draw, cx, cy, size, color):
    # two top lobes + bottom point, filled
    r = size / 2
    draw.pieslice([cx - size, cy - r, cx, cy + r], 180, 360, fill=color)
    draw.pieslice([cx, cy - r, cx + size, cy + r], 180, 360, fill=color)
    draw.polygon([(cx - size, cy), (cx + size, cy), (cx, cy + size * 1.15)], fill=color)

def make(n, label_top, label_main):
    # diagonal gradient deep -> card
    col = Image.new("RGB", (1, H))
    for y in range(H):
        col.putpixel((0, y), lerp(DEEP, CARD, (y / H) ** 1.1))
    img = col.resize((W, H))

    # soft radial glow (accent->blush) upper-center
    glow = Image.new("L", (W, H), 0)
    gd = ImageDraw.Draw(glow)
    gx, gy, gr = int(W * 0.5), int(H * 0.42), int(H * 0.6)
    gd.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], fill=70)
    glow = glow.filter(ImageFilter.GaussianBlur(120))
    glow_col = Image.new("RGB", (W, H), lerp(ACCENT, BLUSH, 0.35))
    img = Image.composite(glow_col, img, glow)

    # vignette
    vig = Image.new("L", (W, H), 0)
    vd = ImageDraw.Draw(vig)
    vd.ellipse([-W * 0.25, -H * 0.25, W * 1.25, H * 1.25], fill=255)
    vig = vig.filter(ImageFilter.GaussianBlur(180))
    dark = Image.new("RGB", (W, H), DEEP)
    img = Image.composite(img, dark, vig)

    d = ImageDraw.Draw(img, "RGBA")
    # thin inner frame
    m = 54
    d.rounded_rectangle([m, m, W - m, H - m], radius=18, outline=(201, 150, 58, 90), width=2)

    # subtle large heart watermark
    heart(d, W // 2, int(H * 0.34), 64, (232, 160, 176, 38))

    # texts
    f_top = sans(22)
    f_main = serif(74)
    f_sub = sans(26)

    def center(text, font, y, fill):
        bb = d.textbbox((0, 0), text, font=font)
        tw = bb[2] - bb[0]
        d.text(((W - tw) / 2, y), text, font=font, fill=fill)

    center(label_top, f_top, int(H * 0.45), (201, 150, 58, 235))
    center(label_main, f_main, int(H * 0.515), (232, 224, 240, 255))
    center("photos/moment%d.jpg" % n, f_sub, int(H * 0.66), (154, 138, 170, 220))

    out = "photos/moment%d.jpg" % n
    img.save(out, "JPEG", quality=88)
    print("wrote", out)

for i in range(1, 7):
    make(i, "MOMENT %d" % i, "Add your photo here")
print("done")
