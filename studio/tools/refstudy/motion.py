#!/usr/bin/env python3
# usage: motion.py <video> <out.json> [fps]
# Global camera motion between consecutive samples (ORB + RANSAC similarity) + mean abs frame difference.
import sys, json, subprocess, numpy as np, cv2
vid, out = sys.argv[1], sys.argv[2]
fps = float(sys.argv[3]) if len(sys.argv) > 3 else 4.0
W, H = 640, 360
cmd = ["ffmpeg", "-v", "error", "-i", vid, "-vf", f"fps={fps},scale={W}:{H}", "-f", "rawvideo", "-pix_fmt", "gray", "-"]
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
orb = cv2.ORB_create(1500)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
prev, pk, pd, i, res = None, None, None, 0, []
while True:
    buf = p.stdout.read(W * H)
    if len(buf) < W * H: break
    f = np.frombuffer(buf, np.uint8).reshape(H, W)
    k, d = orb.detectAndCompute(f, None)
    rec = {"t": round(i / fps, 2)}
    if prev is not None:
        rec["diff"] = round(float(np.mean(cv2.absdiff(f, prev))), 2)
        if d is not None and pd is not None and len(k) > 20 and len(pk) > 20:
            m = bf.match(pd, d)
            if len(m) > 20:
                a = np.float32([pk[x.queryIdx].pt for x in m]); b = np.float32([k[x.trainIdx].pt for x in m])
                M, inl = cv2.estimateAffinePartial2D(a, b, method=cv2.RANSAC, ransacReprojThreshold=2.0)
                if M is not None:
                    s = float(np.sqrt(M[0, 0] ** 2 + M[1, 0] ** 2)); rot = float(np.degrees(np.arctan2(M[1, 0], M[0, 0])))
                    rec.update({"scale": round(s, 5), "rot": round(rot, 3), "tx": round(float(M[0, 2]) * 1920 / W, 2),
                                "ty": round(float(M[1, 2]) * 1920 / W, 2), "inl": int(inl.sum()), "n": len(m)})
    res.append(rec); prev, pk, pd = f, k, d; i += 1
json.dump({"fps": fps, "samples": res}, open(out, "w"))
print("samples", len(res))
