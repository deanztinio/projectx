#!/usr/bin/env python3
# usage: font_compare2.py <ref_png> <out_png> <text> <tracking_em> <list of family:weight:style ...> [--feat onum,smcp]
import sys, glob
from PIL import Image, ImageDraw, ImageFont
args = sys.argv[1:]
feats = None
if "--feat" in args:
    i = args.index("--feat"); feats = args[i+1].split(","); args = args[:i] + args[i+2:]
ref, out, text, track = args[0], args[1], args[2], float(args[3])
specs = args[4:]
refim = Image.open(ref).convert("RGB")
W = refim.width
rows = [refim]
for sp in specs:
    fam, w, st = sp.split(":")
    p = glob.glob(f"/home/user/work/fonts/x/fontsource-{fam}-*/package/files/{fam}-latin-{w}-{st}.woff")
    if not p: print("missing", sp); continue
    font = ImageFont.truetype(p[0], 120, layout_engine=ImageFont.Layout.RAQM)
    tmp = Image.new("RGB", (4000, 220), (40, 40, 40)); d = ImageDraw.Draw(tmp); x = 10
    for ch in text:
        d.text((x, 20), ch, font=font, fill=(240, 235, 225), features=feats)
        x += font.getlength(ch, features=feats) + track * 120
    bbox = tmp.getbbox() if False else None
    # crop to ink
    import numpy as np
    a = np.asarray(tmp).mean(axis=2) > 80
    ys, xs = np.where(a)
    tmp = tmp.crop((max(0, xs.min() - 4), max(0, ys.min() - 4), xs.max() + 4, ys.max() + 4))
    r = W / tmp.width
    tmp = tmp.resize((W, int(tmp.height * r)))
    ImageDraw.Draw(tmp).text((W - 260, 2), sp, fill=(255, 220, 0))
    rows.append(tmp)
H = sum(r.height for r in rows)
sheet = Image.new("RGB", (W, H)); y = 0
for r in rows: sheet.paste(r, (0, y)); y += r.height
sheet.save(out); print("ok")
