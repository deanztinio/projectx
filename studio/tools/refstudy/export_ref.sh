#!/bin/bash
# usage: export_ref.sh <local workdir> <shared ref dir>
# copies the study outputs into the shared folder: 960-wide 1 fps frames (0000.jpg = 0:00), a frame after every hard cut,
# contact sheets, first 5 s at 10 fps, and the data files
W="$1"; R="$2"
mkdir -p "$R"/{frames,cuts,sheets,intro,data,type}
# 1 fps frames: local 0001.jpg = second 0 -> shared 0000.jpg
for f in "$W"/frames/*.jpg; do n=$((10#$(basename "$f" .jpg) - 1)); printf -v o "%04d" "$n"
  ffmpeg -nostdin -v error -y -i "$f" -vf scale=960:-2 -q:v 4 "$R/frames/$o.jpg"; done
# frame 0.2 s after every hard cut (scene score >= 0.3)
python3 -c "import json,sys; print('\n'.join(str(c) for c in json.load(open(sys.argv[1]))['cuts']))" "$W/cuts.json" | while read t; do
  o=$(python3 -c "t=float('$t'); print(f'{int(t//60):02d}m{t%60:05.2f}s')")
  ffmpeg -nostdin -v error -y -ss "$(python3 -c "print(float('$t')+0.2)")" -i "$W/ref.mkv" -frames:v 1 -vf scale=960:-2 -q:v 3 "$R/cuts/cut_$o.jpg"; done
cp "$W"/sheets/*.jpg "$R/sheets/"
for f in "$W"/intro/*.jpg; do ffmpeg -nostdin -v error -y -i "$f" -vf scale=960:-2 -q:v 3 "$R/intro/$(basename "$f")"; done
echo done
