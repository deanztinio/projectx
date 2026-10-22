#!/usr/bin/env python3
import sys, json, numpy as np
d = json.load(open(sys.argv[1])); fps = d["fps"]; S = d["samples"]
t = np.array([s["t"] for s in S])
ok = np.array(["scale" in s and s.get("inl", 0) >= 30 for s in S])
scale = np.array([s.get("scale", 1.0) for s in S]); tx = np.array([s.get("tx", 0.0) for s in S]); ty = np.array([s.get("ty", 0.0) for s in S])
diff = np.array([s.get("diff", 0.0) for s in S])
zoom_ps = (scale ** fps - 1) * 100          # % per second
pan_ps = np.hypot(tx, ty) * fps            # px/s at 1920 wide
cut = diff > 25
valid = ok & ~cut
z = zoom_ps[valid]; p = pan_ps[valid]
still = valid & (np.abs(zoom_ps) < 0.15) & (pan_ps < 4) & (diff < 0.6)
print(f"valid samples {valid.sum()}/{len(S)}")
print(f"zoom %/s: median |z| {np.median(np.abs(z)):.2f}, p75 {np.percentile(np.abs(z),75):.2f}, p95 {np.percentile(np.abs(z),95):.2f}; push-in share {np.mean(z>0.15)*100:.0f}%, pull-out share {np.mean(z<-0.15)*100:.0f}%")
print(f"pan px/s (1920 frame): median {np.median(p):.1f}, p75 {np.percentile(p,75):.1f}, p95 {np.percentile(p,95):.1f}")
print(f"camera moving (|zoom|>0.15%/s or pan>4px/s): {np.mean((np.abs(z)>0.15)|(p>4))*100:.0f}% of valid time")
# longest stretch of 'still' samples (no camera move AND little pixel change)
runs, cur = [], 0
for i, s in enumerate(still):
    if s: cur += 1
    else:
        if cur: runs.append((cur / fps, t[i - cur])); cur = 0
runs.sort(reverse=True)
print("total truly-still time %.1f s (%.1f%%)" % (still.sum() / fps, still.mean() * 100))
print("longest still stretches (s, start):", [(round(a, 2), f"{int(b//60)}:{b%60:04.1f}") for a, b in runs[:8]])
# mean abs frame difference (overall liveliness) per minute
pm = [round(float(np.mean(diff[(t >= m*60) & (t < (m+1)*60)])), 2) for m in range(int(t[-1]//60)+1)]
print("mean frame diff per minute:", pm)
