#!/bin/bash
# usage: extract.sh <workdir>  (expects ref.mkv inside)
set -x
D="$1"; cd "$D" || exit 1
FONT=/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf
mkdir -p frames sheets intro audio logs
# audio first (fast) -> wav for analysis
ffmpeg -nostdin -y -v error -i ref.mkv -vn -ac 2 -ar 44100 -c:a pcm_s16le audio/mix.wav
# loudness timeline (momentary/short-term every 100 ms)
ffmpeg -nostdin -v info -i audio/mix.wav -af "ebur128=peak=true" -f null - 2> logs/ebur128.log
# 1 fps frames, full res (frame N.jpg = second N-1)
ffmpeg -nostdin -y -v error -i ref.mkv -vf fps=1 -q:v 3 frames/%04d.jpg
# contact sheets: 30 s each (6x5), timecode burned on each tile
ffmpeg -nostdin -y -v error -i ref.mkv -vf "fps=1,scale=384:-2,drawtext=fontfile=$FONT:text='%{pts\:hms}':x=4:y=4:fontsize=18:fontcolor=yellow:box=1:boxcolor=black@0.6,tile=6x5:padding=2" -q:v 3 sheets/%03d.jpg
# first 5 s at 10 fps
ffmpeg -nostdin -y -v error -t 5 -i ref.mkv -vf "fps=10" -q:v 3 intro/%03d.jpg
# scene-change score for every frame (low res is fine)
ffmpeg -nostdin -v error -i ref.mkv -an -vf "scale=480:-2,select='gte(scene,0)',metadata=print:file=logs/scene.txt" -f null -
echo DONE
