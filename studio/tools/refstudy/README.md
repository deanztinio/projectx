# Reference study tools

Used for the How-So study (2026-10-22). Results: `studio/references/howso-*/NOTES.md`.

Setup (cloud container): ffmpeg is installed. Python packages:
`python3 -m venv venv && venv/bin/pip install opencv-python-headless numpy scipy scikit-learn pillow librosa`
Font candidates come from npm: `npm pack @fontsource/<family>` then unpack (Google Fonts is blocked).

| Script | What it does |
| --- | --- |
| `extract1pass.sh <dir>` | One decode of `<dir>/ref.mkv`: 1 fps frames, 30-s contact sheets, scene scores, audio + ebur128 loudness, first 5 s at 10 fps. Use this for 4K files. (`extract.sh` = same, several passes.) |
| `srt_stats.py <srt> <outdir>` | Sentences, words, pace, pause after each sentence -> `srt_analysis.json` + `transcript_timed.md`. |
| `script_stats.py <srt_analysis.json> "m:ss=Chapter" ...` | Per-chapter table, sentence openers, dates per minute, questions, "we"/"you", short lines. |
| `scenes.py <scene.txt> <outdir> [thr]` | Hard cuts from scene scores -> `cuts.json`, shot lengths, cuts per minute. |
| `motion.py <video> <out.json> [fps]` | Camera zoom/pan per frame (ORB + RANSAC). `motion_stats.py <json>` summarises it. |
| `palette.py <frames> <outdir> sec:label ...` | k-means colours of chosen seconds + swatch sheet. |
| `font_compare2.py <crop.png> <out.png> "<text>" <tracking_em> family:weight:style ...` | Renders font candidates under a text crop from the video. |
| `loud_pauses.py <ebur128.log> <srt_analysis.json>` | Loudness while talking vs in gaps, and at every pause of 3 s or more. |
| `export_ref.sh <workdir> <shared ref dir>` | Copies frames (960 wide), a frame after every cut, sheets and the intro into the shared folder. |
| `grok.py <out> <prompt_file> [model]` | xAI Responses API with web + X search (streams; prints the cost). |
