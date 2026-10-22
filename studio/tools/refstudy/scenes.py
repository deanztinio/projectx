#!/usr/bin/env python3
# usage: scenes.py <scene.txt> <outdir> [threshold]
import sys, re, json, statistics as st, os
f, outdir = sys.argv[1], sys.argv[2]
thr = float(sys.argv[3]) if len(sys.argv) > 3 else 0.3
t, scores, cur = [], [], None
for line in open(f):
    m = re.search(r"pts_time:([\d.]+)", line)
    if m: cur = float(m.group(1)); continue
    m = re.search(r"lavfi.scene_score=([\d.]+)", line)
    if m and cur is not None: t.append(cur); scores.append(float(m.group(1)))
dur = t[-1]
def cuts_at(th, min_gap=0.25):
    out, last = [], -9
    for ti, s in zip(t, scores):
        if s >= th and ti - last >= min_gap: out.append(ti); last = ti
    return out
res = {}
for th in (0.15, 0.2, 0.3, 0.4, 0.5):
    c = cuts_at(th)
    b = [0] + c + [dur]
    L = [b[i+1] - b[i] for i in range(len(b)-1)]
    res[th] = {"cuts": len(c), "mean_shot": round(st.mean(L), 2), "median_shot": round(st.median(L), 2)}
c = cuts_at(thr)
json.dump({"duration": dur, "threshold": thr, "cuts": c, "by_threshold": res}, open(os.path.join(outdir, "cuts.json"), "w"), indent=1)
# per-minute cut counts at chosen threshold
pm = {}
for x in c: pm[int(x // 60)] = pm.get(int(x // 60), 0) + 1
print(json.dumps(res, indent=1)); print("per minute @", thr, [pm.get(i, 0) for i in range(int(dur // 60) + 1)])
# also print gradual-transition candidates: runs of moderately elevated scores (crossfades)
runs, start, acc = [], None, 0
for ti, s in zip(t, scores):
    if 0.04 <= s < thr:
        if start is None: start, acc = ti, 0
        acc += s
    else:
        if start is not None and ti - start >= 0.3 and acc > 0.5: runs.append((round(start, 2), round(ti - start, 2), round(acc, 2)))
        start = None
print("gradual transitions (start, len, summed score):", len(runs)); print(runs[:80])
