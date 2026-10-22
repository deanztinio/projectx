# Reference study: <REF-ID> <title>

Source: <link / PC path> · Length: · Channel: · Views / outlier score (1of10):

## How to extract (cloud)
```bash
mkdir -p studio/references/<ref>/{frames,cuts,sheets}
ffmpeg -i ref.mp4 -vf fps=1 studio/references/<ref>/frames/%04d.jpg                 # 1 fps
ffmpeg -i ref.mp4 -vf "select='gt(scene,0.3)',showinfo" -vsync vfr studio/references/<ref>/cuts/%04d.jpg 2> cuts.log  # every cut
ffmpeg -i ref.mp4 -vf "fps=1,scale=384:-1,tile=6x5" studio/references/<ref>/sheets/%03d.jpg   # 30-s contact sheets
ffmpeg -i ref.mp4 -ss 0 -t 5 -vf fps=10 studio/references/<ref>/intro_%03d.jpg            # first 5 s at 10 fps
ffmpeg -i ref.mp4 -af ebur128 -f null - 2> loudness.log                                   # loudness over time
```
Look at the sheets; open single frames only where detail matters. Compare our renders against the
reference at matching timecodes side by side (a compare script makes this one command).

## 1. First 5 seconds, second by second
| t | What's on screen | Text | Motion | Sound |
| --- | --- | --- | --- | --- |

## 2. Cut rhythm
- Hook: average shot length · Body: average shot length · Fast-cut moments (where, why):

## 3. Typography
- Fonts (closest free match): · Sizes · Weight · Tracking · Case · How text enters/exits:

## 4. Colour + finish
- Sampled hex: · Grade · Grain · Vignette · Light:

## 5. Motion + camera
- Easing feel · Camera moves · Motion blur · Transitions:

## 6. How it shows things
| Thing | How (timecode) |
| --- | --- |
| Places / maps | |
| Dates / time jumps | |
| Numbers | |
| Trends / comparisons | |
| People | |
| Quotes / documents | |
| Chapter changes | |

## 7. What moves at every moment (is there ever a still frame? how long?)

## 8. Sound
- Voice style + pace (words per minute):
- Music: genre, energy, where it drops out:
- SFX: how many per minute, how loud vs voice (dB), which kinds:

## 9. Script structure (from the transcript)
- Hook length + pattern · Chapter open/close · Sentence length · Humour · Fact density:

## 10. Packaging
- Title pattern · Thumbnail (brightness, text, faces, colours):

## 11. dnz likes / dislikes (ask!)

## 12. Rules this adds to BRAND.md (each with its timecode)
