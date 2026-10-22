#!/usr/bin/env python3
# usage: palette.py <frames_dir> <out_dir> <sec:label> ...   -> k-means palette per frame + swatch sheet
import sys, os, numpy as np
from PIL import Image, ImageDraw
from sklearn.cluster import KMeans
fd, od = sys.argv[1], sys.argv[2]
rows = []
for spec in sys.argv[3:]:
    s, label = spec.split(":", 1); s = int(s)
    im = Image.open(f"{fd}/{s+1:04d}.jpg").convert("RGB").resize((320, 180))
    px = np.asarray(im).reshape(-1, 3).astype(float)
    km = KMeans(n_clusters=7, n_init=4, random_state=0).fit(px)
    cnt = np.bincount(km.labels_, minlength=7); order = np.argsort(-cnt)
    cols = [(tuple(int(v) for v in km.cluster_centers_[i]), cnt[i] / cnt.sum()) for i in order]
    rows.append((s, label, im, cols))
    print(f"{s//60}:{s%60:02d} {label}: " + "  ".join(f"#{c[0]:02x}{c[1]:02x}{c[2]:02x} {p*100:.0f}%" for c, p in cols))
W, H = 320 + 7 * 120, 180
sheet = Image.new("RGB", (W, H * len(rows)), (0, 0, 0)); d = ImageDraw.Draw(sheet)
for i, (s, label, im, cols) in enumerate(rows):
    y = i * H; sheet.paste(im, (0, y))
    for j, (c, p) in enumerate(cols):
        x = 320 + j * 120; d.rectangle([x, y, x + 119, y + H - 1], fill=c)
        d.text((x + 4, y + 4), f"#{c[0]:02x}{c[1]:02x}{c[2]:02x}\n{p*100:.0f}%", fill=(255, 255, 255) if sum(c) < 380 else (0, 0, 0))
    d.text((4, y + 4), f"{s//60}:{s%60:02d} {label}", fill=(255, 255, 0))
sheet.save(f"{od}/palette_sheet.png")
