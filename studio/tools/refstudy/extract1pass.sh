#!/bin/bash
# one decode pass: 1 fps frames (1920 wide), 30-s contact sheets, scene scores; plus audio + loudness + intro
set -x
D="$1"; cd "$D" || exit 1
FONT=/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf
mkdir -p frames sheets intro audio logs stills4k
ffmpeg -nostdin -y -v error -i ref.mkv -vn -ac 2 -ar 44100 -c:a pcm_s16le audio/mix.wav
ffmpeg -nostdin -v info -i audio/mix.wav -af "ebur128=peak=true" -f null - 2> logs/ebur128.log
ffmpeg -nostdin -y -v error -threads 4 -t 5 -i ref.mkv -vf "fps=10,scale=1920:-2" -q:v 3 intro/%03d.jpg
ffmpeg -nostdin -y -v error -threads 4 -i ref.mkv -filter_complex \
 "[0:v]split=3[a][b][c];\
  [a]fps=1,scale=1920:-2[fr];\
  [b]fps=1,scale=384:-2,drawtext=fontfile=$FONT:text='%{pts\:hms}':x=4:y=4:fontsize=18:fontcolor=yellow:box=1:boxcolor=black@0.6,tile=6x5:padding=2[sh];\
  [c]scale=480:-2,select='gte(scene,0)',metadata=print:file=logs/scene.txt,nullsink" \
 -map "[fr]" -q:v 3 frames/%04d.jpg -map "[sh]" -q:v 3 sheets/%03d.jpg
echo DONE
