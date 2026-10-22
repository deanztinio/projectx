#!/usr/bin/env python3
# usage: script_stats.py <srt_analysis.json> <chapter starts "m:ss=Title" ...>
import sys, json, re, collections
d = json.load(open(sys.argv[1])); sents = d["sentences"]
chs = []
for a in sys.argv[2:]:
    t, name = a.split("=", 1); m, s = t.split(":"); chs.append((int(m) * 60 + float(s), name))
chs.sort()
def chap(t):
    c = chs[0][1]
    for s, n in chs:
        if t >= s - 0.5: c = n
    return c
by = collections.OrderedDict((n, []) for _, n in chs)
for s in sents: by[chap(s["start"])].append(s)
print("| chapter | start | length | sentences | words | wpm (span) | avg words/sentence |")
print("|---|---|---|---|---|---|---|")
ends = [s for s, _ in chs[1:]] + [sents[-1]["end"]]
for (st, n), en in zip(chs, ends):
    ss = by[n]; w = sum(x["words"] for x in ss); L = en - st
    print(f"| {n} | {int(st//60)}:{st%60:04.1f} | {L:.0f} s | {len(ss)} | {w} | {w / L * 60:.0f} | {w / max(1, len(ss)):.1f} |")
txt = " ".join(s["text"] for s in sents)
starts = collections.Counter()
for s in sents:
    w = s["text"].split()
    k = " ".join(w[:2]) if w[0] in ("In", "By", "During", "After", "Around", "Between", "Over") else w[0].strip(",")
    starts[k] += 1
print("\nmost common sentence openers:", starts.most_common(14))
dates = re.findall(r"\b\d{3,4}\b|\b\d{1,2}(?:st|nd|rd|th) centur|\bmillenni", txt)
print("date/number mentions:", len(dates), "=", round(len(dates) / (sents[-1]["end"] / 60), 1), "per minute")
print("questions:", txt.count("?"), "| exclamations:", txt.count("!"), "| em dashes:", txt.count("—"))
print("first person we/our/us:", len(re.findall(r"\b(we|our|us)\b", txt, re.I)), "| 'you':", len(re.findall(r"\byou\b", txt, re.I)))
short = [s["text"] for s in sents if s["words"] <= 6]
print("short lines (<=6 words):", len(short), "e.g.", short[:12])
