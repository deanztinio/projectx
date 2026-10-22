#!/usr/bin/env python3
# usage: grok.py <out_basename> <prompt_file> [model]
import json, sys, urllib.request, time
out, pf = sys.argv[1], sys.argv[2]
model = sys.argv[3] if len(sys.argv) > 3 else "grok-4.7"
prompt = open(pf).read()
body = {"model": model, "input": [{"role": "user", "content": prompt}],
        "tools": [{"type": "web_search"}, {"type": "x_search"}],
        "stream": True, "max_turns": 4}
req = urllib.request.Request("https://api.x.ai/v1/responses", data=json.dumps(body).encode(),
                             headers={"Content-Type": "application/json"})
text, final = [], None
t0 = time.time()
with urllib.request.urlopen(req, timeout=600) as r:
    for raw in r:
        line = raw.decode("utf-8", "replace").strip()
        if not line.startswith("data:"): continue
        data = line[5:].strip()
        if data == "[DONE]": break
        try: ev = json.loads(data)
        except Exception: continue
        t = ev.get("type", "")
        if t == "response.output_text.delta": text.append(ev.get("delta", ""))
        if t == "response.completed": final = ev.get("response")
open(out + ".md", "w").write("".join(text))
if final:
    json.dump(final, open(out + ".json", "w"), indent=1)
    u = final.get("usage", {})
    print("cost_usd", u.get("cost_in_usd_ticks", 0) / 1e10, "secs", round(time.time() - t0))
print("".join(text)[:200])
