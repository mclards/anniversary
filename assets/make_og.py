from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
W, H = 1200, 630
DEEP=(13,11,26); CARD=(31,24,48); ACCENT=(139,26,74); GOLD=(201,150,58); BLUSH=(232,160,176); MUTED=(154,138,170)
def lerp(a,b,t): return tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3))
def load_font(names,size):
    for n in names:
        try: return ImageFont.truetype(os.path.join(r"C:\Windows\Fonts",n),size)
        except Exception: continue
    return ImageFont.load_default()
serif=lambda s: load_font(["georgiai.ttf","georgia.ttf","timesi.ttf"],s)
serifb=lambda s: load_font(["georgiab.ttf","georgia.ttf"],s)
sans=lambda s: load_font(["segoeui.ttf","arial.ttf"],s)
def heart(d,cx,cy,size,color):
    r=size/2
    d.pieslice([cx-size,cy-r,cx,cy+r],180,360,fill=color)
    d.pieslice([cx,cy-r,cx+size,cy+r],180,360,fill=color)
    d.polygon([(cx-size,cy),(cx+size,cy),(cx,cy+size*1.15)],fill=color)
col=Image.new("RGB",(1,H))
for y in range(H): col.putpixel((0,y),lerp(DEEP,CARD,(y/H)**1.1))
img=col.resize((W,H))
glow=Image.new("L",(W,H),0); gd=ImageDraw.Draw(glow)
gr=int(H*0.7); gd.ellipse([W//2-gr,int(H*0.4)-gr,W//2+gr,int(H*0.4)+gr],fill=80)
glow=glow.filter(ImageFilter.GaussianBlur(130))
img=Image.composite(Image.new("RGB",(W,H),lerp(ACCENT,BLUSH,0.4)),img,glow)
d=ImageDraw.Draw(img,"RGBA")
heart(d,W//2,150,30,(139,26,74,255))
def center(text,font,y,fill):
    bb=d.textbbox((0,0),text,font=font); tw=bb[2]-bb[0]
    d.text(((W-tw)/2,y),text,font=font,fill=fill)
center("For you, Baby.",serifb(86),215,(232,160,176,255))
center("365 araw. Isang taon. Patungo sa ating habang-buhay.",serif(31),333,(232,224,240,235))
center("STILL CHOOSING YOU, BABY JEZEL  •  JUNE 2026",sans(22),470,(201,150,58,235))
img.save("assets/og-image.jpg","JPEG",quality=90)
print("wrote assets/og-image.jpg")
