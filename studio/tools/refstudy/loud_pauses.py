#!/usr/bin/env python3
# usage: loud_pauses.py <ebur128.log> <srt_analysis.json>
import sys, re, json, numpy as np
T, M, S = [], [], []
for line in open(sys.argv[1]):
    m = re.search(r"t:\s*([\d.]+)\s+TARGET.*?M:\s*(-?[\d.]+|-inf)\s+S:\s*(-?[\d.]+|-inf)", line)
    if m:
        T.append(float(m.group(1))); M.append(float(m.group(2)) if m.group(2) != "-inf" else -70); S.append(float(m.group(3)) if m.group(3) != "-inf" else -70)
T, M, S = map(np.array, (T, M, S))
sents = json.load(open(sys.argv[2]))["sentences"]
speech = np.zeros_like(T, bool)
for s in sents: speech |= (T >= s["start"]) & (T <= s["end"])
print(f"momentary loudness while talking: median {np.median(M[speech]):.1f} LUFS")
print(f"momentary loudness in gaps (no talking): median {np.median(M[~speech]):.1f} LUFS")
print("long pauses (>=3 s): pause start, length, M during pause (median / max), M in 3 s of speech before")
for i, s in enumerate(sents[:-1]):
    p = s["pause_after"]
    if p and p >= 3:
        a, b = s["end"] + 0.3, sents[i+1]["start"] - 0.1
        w = (T >= a) & (T <= b); pre = (T >= s["end"] - 3) & (T <= s["end"])
        print(f"  {int(s['end']//60)}:{s['end']%60:05.2f}  {p:4.1f}s  pause M {np.median(M[w]):6.1f} / {M[w].max():6.1f}   speech-before M {np.median(M[pre]):6.1f}   '{s['text'][-45:]}'")
