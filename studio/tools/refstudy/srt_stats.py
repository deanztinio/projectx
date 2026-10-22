#!/usr/bin/env python3
# usage: srt_stats.py <file.srt> <outdir>
import re, sys, json, statistics as st, os
src, outdir = sys.argv[1], sys.argv[2]
os.makedirs(outdir, exist_ok=True)
txt = open(src, encoding="utf-8-sig").read()
blocks = re.split(r"\n\s*\n", txt.strip())
def ts(s):
    h, m, rest = s.split(":"); sec, ms = rest.split(",")
    return int(h)*3600 + int(m)*60 + int(sec) + int(ms)/1000
segs = []
for b in blocks:
    lines = b.strip().splitlines()
    if len(lines) < 3: continue
    a, z = [x.strip() for x in lines[1].split("-->")]
    t = " ".join(lines[2:]).strip()
    t = t.replace("(Transcribed by TurboScribe. Go Unlimited to remove this message.)", "").strip()
    segs.append({"start": ts(a), "end": ts(z), "text": t})
# gaps
for i, s in enumerate(segs):
    s["gap_after"] = round(segs[i+1]["start"] - s["end"], 3) if i+1 < len(segs) else None
words_total = sum(len(s["text"].split()) for s in segs)
speech = sum(s["end"] - s["start"] for s in segs)
span = segs[-1]["end"] - segs[0]["start"]
gaps = [s["gap_after"] for s in segs if s["gap_after"] is not None]
# sentences: join text with segment timing, split at . ? !
sents, cur, cur_start = [], [], None
for s in segs:
    parts = re.split(r"(?<=[.?!])\s+", s["text"])
    n = len(parts)
    for j, p in enumerate(parts):
        if not p: continue
        if cur_start is None:
            # approximate start inside the segment by word position
            wbefore = sum(len(x.split()) for x in parts[:j]); wall = max(1, len(s["text"].split()))
            cur_start = s["start"] + (s["end"] - s["start"]) * wbefore / wall
        cur.append(p)
        if re.search(r"[.?!][\"')\]]?$", p):
            wupto = sum(len(x.split()) for x in parts[:j+1]); wall = max(1, len(s["text"].split()))
            end = s["start"] + (s["end"] - s["start"]) * wupto / wall
            sents.append({"start": round(cur_start, 2), "end": round(end, 2), "text": " ".join(cur)})
            cur, cur_start = [], None
if cur: sents.append({"start": round(cur_start, 2), "end": round(segs[-1]["end"], 2), "text": " ".join(cur)})
for i, s in enumerate(sents):
    s["words"] = len(s["text"].split())
    s["dur"] = round(s["end"] - s["start"], 2)
    s["wpm"] = round(s["words"] / max(0.1, s["dur"]) * 60)
    s["pause_after"] = round(sents[i+1]["start"] - s["end"], 2) if i+1 < len(sents) else None
wl = [s["words"] for s in sents]
pa = [s["pause_after"] for s in sents if s["pause_after"] is not None]
summary = {
  "segments": len(segs), "words": words_total, "first_word": segs[0]["start"], "last_word": segs[-1]["end"],
  "speech_span_s": round(span, 1), "wpm_over_span": round(words_total / span * 60, 1),
  "wpm_while_talking": round(words_total / speech * 60, 1),
  "sentences": len(sents), "sentence_words_mean": round(st.mean(wl), 1), "sentence_words_median": st.median(wl),
  "sentence_words_p10_p90": [sorted(wl)[len(wl)//10], sorted(wl)[len(wl)*9//10]], "sentence_words_max": max(wl),
  "pause_after_sentence_mean": round(st.mean(pa), 2), "pause_after_sentence_median": round(st.median(pa), 2),
  "pauses_over_1s": sum(1 for p in pa if p >= 1.0), "pauses_over_2s": sum(1 for p in pa if p >= 2.0),
  "gap_between_segments_median": round(st.median(gaps), 2),
}
json.dump({"summary": summary, "sentences": sents, "segments": segs}, open(os.path.join(outdir, "srt_analysis.json"), "w"), indent=1)
with open(os.path.join(outdir, "transcript_timed.md"), "w") as f:
    for s in sents:
        m, sec = divmod(s["start"], 60)
        f.write(f"[{int(m):02d}:{sec:05.2f}] ({s['words']}w {s['dur']}s pause {s['pause_after']}) {s['text']}\n")
print(json.dumps(summary, indent=1))
