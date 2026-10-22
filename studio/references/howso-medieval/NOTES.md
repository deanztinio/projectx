# Reference study: REF-A "Medieval Europe: 1000 Years in 20 Minutes" (How-So)

Source: https://www.youtube.com/watch?v=8VPPQAcac6U · PC copy: `D:\01 CLAUDE\PROJECT X\Medieval Europe 1000 Years in 20 Minutes.mkv`
· Cloud copy: this folder · Length: 22:24 (1344.6 s), 1920x1080, 30 fps · Published 25 Aug 2025
· Channel: How-So (@How-So), about 90K subscribers, run by "two guys handcrafting these videos" (their own reply on the Islamic World video)
· Views: 3.6M after about 1 year (dnz, from YouTube, 2026-10-22). 1of10 does not index How-So, so there is no official outlier score. Against the channel's 5 public long videos (median about 327K views) this video is about **11x**. It is the channel's biggest video.

Studied 2026-10-22 at max effort. dnz's brief: copy everything from this channel except the logo and the voice.

## Files in this folder
| Folder / file | What it is |
| --- | --- |
| `frames/0000.jpg ...` | 1 frame per second, 960 wide. File number = second (0000 = 0:00, 0161 = 2:41). |
| `cuts/cut_MMmSS.SSs.jpg` | One frame 0.2 s after every hard cut (scene score 0.3 or more). |
| `sheets/001.jpg ...` | Contact sheets, 30 s each (6x5 tiles, timecode burned in). 001 = 0:00-0:29. |
| `intro/001.jpg ...` | First 5 s at 10 fps. |
| `data/visual_log.md` | What is on screen, second by second, for the whole video. Read this first. |
| `data/transcript_timed.md` | Every sentence with start time, word count, length and the pause after it. |
| `data/srt_analysis.json`, `data/cuts.json`, `data/motion.txt`, `data/loudness.txt`, `data/palette_sheet.png` | Raw numbers behind this file. |
| `type/` | Font matching images (reference crop on top, candidates under it). |
| `data/anim_*.jpg`, `data/first5s_strip.jpg` | Frame strips (4-5 fps, timecode from the strip start) of key animations: label build (0:20), chapter card + lattice wipe (2:42), cutout slide-in (2:52), cutout + caption (3:59). |
| Tools | `studio/tools/refstudy/` regenerates all of this for a new reference. |

The SRT is an automatic TurboScribe transcript. It has small errors (for example 21:24 "had not only but almost shifted outward").

## 1. First 5 seconds, second by second
| t | What's on screen | Text | Motion | Sound |
| --- | --- | --- | --- | --- |
| 0.0-1.0 | Political map of Europe in 1500 (the END state of the story): France blue, Spain orange, Holy Roman Empire gold, England magenta, Ottomans green, dark slate sea, cloud wisps over the sea | Map labels only (FRANCE, SPAIN, HOLY ROMAN EMPIRE, HUNGARY, OTTOMAN EMPIRE), city dots | Fast push-in toward central Europe | Music hit at 0 s. VO starts at 0.37 s: "In the Middle Ages, a new civilization was forged on the European continent." |
| 1.0-2.2 | Same map, closer | Labels grow with the zoom | Push-in continues | VO |
| 2.2-2.5 | Cross-dissolve (about 0.3 s) | none | | VO |
| 2.5-4.0 | Oblique 3D relief map of western Europe (green land, Alps sprites) PACKED with castle, town, church and ship sprites | none | Slow glide forward with a slight tilt | VO ends 4.8 s |
| 4.0-5.0 | Same | none | Glide | 0.8 s pause, next line at 5.6 s |

Pattern: the first frame is already a rich, moving map. No logo, no title, no black. The first line names the era and the place.

## 2. Cut rhythm
- Hard cuts are rare because most changes are cross-dissolves or wipes. 68 hard cuts in 22:24 (median 13 s apart).
- Counting every new shot OR new element from the visual log: **a new visual beat every 7 s** (median, body), 90% of beats within 13 s.
- Hook (0:00-0:17): one shot per noun pair of the narration, 1-3 s each. 9 hard cuts in the first minute.
- Body: 1-5 hard cuts per minute. Inside a shot, things keep arriving (a cutout slides in, a fill spreads, a label builds).
- Fast moments: the hook montage (0:00-0:17), three paintings for "culture, quality of life" (0:32-0:36, 1-2 s each), inventions popping in (19:07-19:14).

## 3. Typography
- **One serif family everywhere. No sans-serif at all.** Old-style Garamond-type letters.
- Closest free match (see `type/`): **EB Garamond** for titles, map labels, chapter titles, names and dates (`type/cmp_chapter2.png`, `type/cmp_label.png`, `type/cmp_badge.png`). For the italic lines, **Crimson Pro Italic** is closer than EB Garamond Italic (`type/cmp_italic.png`, `type/cmp_italic2.png`).
- Colour: warm white (about #FBF8F2) with a soft dark drop shadow. On maps a faint dark glow behind the letters.
- Sizes and tracking (on a 1920 frame):

| Use | Case | Tracking | Example |
| --- | --- | --- | --- |
| Main title | CAPS, regular weight | very wide (about 0.35 em) | "MEDIEVAL EUROPE" 2:40 |
| Chapter card | Roman numeral (small) + Title Case + "(500 CE)" small | about 0.2 em | "I / Germanic Kingdoms / (500 CE)" 2:43 |
| Big map label | CAPS, curved along the territory | wide (0.2-0.3 em) | "ROMAN EMPIRE" 0:22, "CAROLINGIAN EMPIRE" 5:45 |
| Small map label | CAPS, small | wide | provinces 0:19 (ITALY, GAUL, DACIA) |
| City | Title case, small, next to a white dot | normal | "Rome", "Constantinople" 1:14 |
| Term card | CAPS or Title Case + small italic translation, in a dark translucent box | medium | "PAX ROMANA / Roman Peace" 0:26, "Emperor of the Romans / Imperator Romanorum" 5:53 |
| Person caption | Title case in a small dark rounded box near the cutout | normal | "Justinian I" 4:00, "Otto the Great" 10:19 |
| Date badge | Numerals, tracked, in a dark translucent box, era-coloured underline | wide | "0 - 200 CE" 0:20, "1000 - 1300 CE" 11:00 |

- How text enters: map labels **build letter by letter, left to right, about 0.1 s per letter, each letter fading in** ("ROMAN EMPIRE" 0:21.8-0:23.0). Captions fade in (about 0.25 s) at the bottom corner of the cutout, just as it lands (Justinian slides in 4:01.25-4:01.75, caption at 4:01.5). Chapter titles fade in about 0.4 s. Exit: fade out about 0.5 s. No bounce, no typewriter cursor, no kinetic type.
- On-screen text only names things (places, people, terms, dates). It never repeats the narration sentence.

## 4. Colour + finish
Sampled with k-means on whole frames (`data/palette_sheet.png`):

| Role | Hex | Where |
| --- | --- | --- |
| Sea (the main colour of the whole video) | #2C4448, #304B4F, #31484B | every map, 24-44% of the frame |
| Deep sea / shadow | #1D2C2F, #1E2B30 | map edges |
| Land (grey-beige relief) | #AB9E92, #BEB2A4, #B4A395, #988981 | every map |
| Roman Empire | #A53F50, #8A3141 | 0:23 |
| Franks / Carolingians | #4C796C, #3F8A81, #6DB9A8 | 2:55, 5:45 |
| Byzantine | #85456B, #9A3C5C | 4:50, 10:10 |
| Umayyad | #568176, #6C784F | 4:50 |
| Late map: France / Spain / HRE | #48636E, #AC694B, #B69960 | 20:15, 21:00 |
| Chapter card darks + gold highlight | #2E2D28, #17140B, #ECD17A | 2:45 |
| Diorama farmland | #67701D, #4F5818, #808424 | 11:40 |

- Fills are translucent: the relief and rivers show through. Fills have a soft inner glow at the border.
- Grade: muted, slightly desaturated, warm light and cool shadows. Paintings are darkened or tinted to sit with the maps.
- Vignette: yes. On average the corners are about 35% darker than the centre.
- Light: god rays and slow light sweeps on many scenes (0:12, 5:09, 11:42, 16:11). Cloud wisps drift across the edges of most maps.
- Grain: not visible at this compression. Paintings and manuscripts keep their own texture.

## 5. Motion + camera
Measured with feature tracking at 4 fps (`data/motion.txt`):
- The camera moves **82% of the time**. Median zoom speed 1.1% per second (75th percentile 3.5%/s). Median pan 19 px/s on a 1920 frame.
- Push-ins (44% of the time) beat pull-outs (31%).
- Feel: slow, continuous, nearly linear drifts. Bigger moves (travel to another region) ease in and out over 1-2 s.
- Parallax: dioramas and composited paintings have 2-4 layers (8:22, 11:11, 11:42).
- Motion blur on fast moves and whip transitions only.
- Transitions:
  - Cross-dissolve, 0.3-1 s: the default.
  - X-line or diamond-lattice wipe with coloured edges: out of most chapter cards (2:50, 5:20, 8:04, 14:20, 19:46).
  - Diamond-tile wipe: 3:59, 11:10, 17:48.
  - Whip or blur: 3:41, 6:12, 15:00. Zoom-blur push INTO a map to reach a diorama: 8:21.
  - Ragged or burnt-edge mask: 1:02, 5:50. Torn paper: 19:27. White bloom flash: 2:39.
  - Dip to black only at big breaks: 0:17 (after the hook, 2 s), 17:21, 18:20.

## 6. How it shows things
| Thing | How (timecode) |
| --- | --- |
| Places / maps | 2.5D political map: hillshade relief under translucent colour fills, dark slate sea, drifting clouds (0:19). Territory changes by a colour wipe that spreads across the region (10:31). Frontiers become a white-hot glowing line (1:48, 5:07, 13:09). Curved white migration and attack arrows (1:59, 7:24). Physical map with sprites when the topic is life, not borders: castles pop in (8:12), ships sail (7:34), riders move (8:54). Battles = crossed-swords icon + name ("Tours" 5:00, "Lechfeld" 10:19, "Hastings" 12:53). |
| Dates / time jumps | Date badge top-left on every shot (maps AND paintings), with an era-coloured underline: gold Early, light blue Central, purple Late. Chapter cards carry the date range and an era bar (EARLY / CENTRAL / LATE, 500-1000-1300-1500) with the current era in colour, the rest greyscale (10:56). |
| Numbers | Almost none on screen. Numbers are spoken. No charts. |
| Trends / comparisons | Glowing regions that split ("ROMAN CIVILIZATION" becomes three civilizations, 4:37-4:46). Three-panel infographic Ancient / Dark Ages / Modern (19:32). "RENAISSANCES" bar with a pointer that moves each time it returns (6:13, 12:14, 19:19). Greyscale everything except the subject. |
| People | Real museum objects cut out: statues, mosaics, coins, manuscript figures. They slide in from the frame edge (about 0.5 s, ease-out) and take the left or right third, often full height (Clovis 2:54, Justinian 4:01, Rollo 10:05). Small dark name box at the bottom corner of the cutout. Coins as portraits (2:14). Several people at once = small cutouts placed ON their territory (7:00) or portrait medallions linked by gold lines (9:06). One special name card with a monogram (Charlemagne 5:36). |
| Quotes / documents | Term cards for key terms and Latin names (0:26, 5:53, 9:18). Full-frame manuscripts and paintings with slow pans (11:21, 13:44, 18:53). No quoted sentences on screen. |
| Chapter changes | Short punch line, then a 5-9 s pause with the chapter card (numeral, title, date range, era bar, dark painting with god rays), then a lattice wipe into the first map. |
| Ideas (abstract) | Symbols on the map: a glowing cross for Christianity (0:44, 0:58), chess pieces for Church vs kings (14:40), an orange crack for conflict (14:45), storm clouds for a coming disaster (17:36), rats along the bottom of the Black Death card (17:42). |

## 7. What moves at every moment
- Something always moves. Truly still frames add up to only 5.4% of the video (72 s). The longest still stretches are chapter cards (5.3 s at 9:31, 4.3 s at 14:16, 3.5 s at 3:55), and even those have moving light.
- A normal shot has 2-3 moving layers: camera drift + a new element arriving + ambient motion (clouds, god rays, smoke, fire, dust, petals 6:13).
- The amount of change per minute stays even from start to end (mean frame difference 7-15 every minute). There is no dead stretch.

## 8. Sound (kept short: dnz said music and SFX are low priority)
- Voice: male (median pitch about 130 Hz), calm, even, neutral documentary read. No hype, no jokes. 150 words per minute while talking, 120 over the whole span. About 0.9 s between sentences, about 0.3 s between phrases, 5.4-8.7 s at chapter cards.
- Loudness: integrated -23.9 LUFS, range 3.7 LU (very even). Voice moments about -23.6 LUFS. Music alone in the gaps about -32 LUFS, so the bed sits about 8 LU under the voice.
- Music: one continuous bed (Epidemic Sound is credited). At chapter cards the music plays alone. Some cards get a swell (12:26, 14:14, 17:39, 20:26 peak at -19 to -22 LUFS), others drop almost to silence (10:55, -40 LUFS). The music in those pauses is rhythmic (rough estimate 100-110 bpm).
- SFX: not studied, by dnz's choice (2026-10-22).

## 9. Script structure (from the transcript)
- 2,645 words, 192 sentences, 22:07 of speech.
- **Hook (17 s, 3 sentences):** era + place in line 1 ("In the Middle Ages, a new civilization was forged on the European continent.") → a list of paired themes ("Nobles and kings, faith and warfare, culture and learning, trade and innovation...") → the title line ("This is the story of how Europe was born.") → 2 s of black.
- **Prologue (144 s):** the world before (Rome), ending on "Romans, Christians, barbarians. These were the three main ingredients that combined to create medieval Europe." → main title card at 2:40. The title comes after the prologue here.
- **12 chapters, 71-119 s each (about 93 s average).** Each opens with a time anchor and the situation ("Around 500 CE, Europe was covered by newly established kingdoms...", "In the 10th century, things started to change.", "The year 1000 marks a turning point..."). Each closes with a short line of 4-9 words that points forward: "Europe was under siege." (7:58), "The Catholic Church had awakened." (14:14), "A great calamity was approaching." (17:39). Then the 5-6 s breath and the next card.
- **Epilogue (48 s):** zooms out to the whole world, links the era to today. No call to action anywhere (no "subscribe", no "like").
- Sentence length: median 13 words (10% are 7 or fewer, 10% are 22 or more, max 30).
- Short lines for weight, about one per chapter: "Romans, Christians, barbarians." (2:32), "Europe was under siege." (7:58).
- Openers: The (34x), In the (15x), This (10x), But (10x), These (9x).
- Fact density: 1.4 dates per minute. Every sentence moves the story. Cause and effect drive it ("This led to", "As a result").
- 0 questions, 0 exclamations, 0 em dashes. First person once. Never "you". No humour.
- Names a term, then uses it ("the so-called Dark Ages", "Pax Romana", "the Europeanization of Europe").
- Scope is stated and defended: the video follows the Carolingian heartland (their reply to comments asking about Eastern Europe).

## 10. Packaging
- Title pattern: **"<Subject>: <N> Years in <M> Minutes"**. Also used for "The Islamic World: 1000 Years in 18 Minutes" (about 3.5M views) and "The Bronze Age: 2000 Years in 20 Minutes". The real runtime (22:24) is longer than the title says.
- Their two non-format videos ("Evolution Explained" about 117K, "Computer Networks Explained" about 35K) did far worse. An X post used the channel as the example of the format beating a plain title (The Islamic World 3.4M vs Evolution Explained 116K).
- Thumbnail (`thumbnail.jpg`): "MEDIEVAL EUROPE" in white serif caps across the top (92% of the width, cap height 74 px = 10% of the height, close to EB Garamond 600, tracking about 0.06 em). Background: the video's dark relief map of Europe, the Carolingian heartland glowing bright cyan with curved white arrows spreading out of it (the expansion story, as at 12:39), god rays from the top. Hero: a 19th-century painting of a crowned crusader king (red cross on white), cut out on the left at about 85% of the height, pointing at the glowing map. Bottom: manuscript knights on horseback charging in a row (compare 8:38). Fire on the left edge. Cyan border (#00B3DB) about 10-13 px wide around the whole image. Colours: #372922, #4D5B59, #8F958D, #AE5F31, #17AEC4, #E7B57A, #E8EBE1; mean brightness 133/255, saturation 104/255.
- **Thumbnail pattern (both thumbnails):**
  1. The title is the subject only ("MEDIEVAL EUROPE", "THE BRONZE AGE"), huge white serif caps across the top: 87-92% of the width, cap height 10-11% of the image height, dark drop shadow. The "N Years in M Minutes" part is only in the YouTube title.
  2. The background is the channel's own relief map of the region, with the story drawn on it (a glow, arrows).
  3. One or two huge real figures (a painting or museum statue), cut out, 70-90% of the image height. With two civilizations, one on each side, facing each other, each in its region colour.
  4. A row of small figures marches along the bottom (manuscript knights, relief figures).
  5. Fire on at least one edge, warm against cool (orange fire and gold against teal or blue).
  6. A bright coloured border around the whole image.
  7. Built from the video's own assets: the same map, cutouts and sprites.
  8. No narrator face, no clickbait arrows or circles, no question marks, no other words.
- The first frame of the video does NOT copy the thumbnail (REF-A opens on the political map of 1500; the thumbnail uses the glow map from 12:39). The channel-1 rule "first frame matches the thumbnail" is still only a candidate.
- `thumbnail.jpg` in this folder is the 1280x720 thumbnail (screenshot from dnz, 2026-10-22).

## 11. dnz likes / dislikes
- Likes (dnz 2026-10-22): "feels premium", "the script is engaging", "I feel like I really understand because of the animation in the map".
- Dislikes: not given yet.

## 12. Rules this adds to BRAND.md (each with its timecode)
1. One old-style serif family for all text, warm white with a soft shadow; no sans-serif. (REF-A 0:22, 2:43, 4:00)
2. Map labels build letter by letter, about 0.1 s per letter. (REF-A 0:21.8)
3. Date badge top-left on every shot, with an era colour. (REF-A 0:20, 11:00)
4. The base map: dark slate sea #2C4448, grey-beige relief land, translucent fills, cloud wisps. (REF-A 0:19)
5. Territory changes are animated spreads, never cuts. (REF-A 10:31)
6. People are real museum objects, cut out, sliding in from the edge (about 0.5 s) into the left or right third, with a small name box at the bottom corner of the cutout as it lands. (REF-A 2:54, 4:01)
7. The camera never stops. Still frames only on chapter cards, max about 5 s. (REF-A 9:31, motion data)
8. Something new every 5-10 s. (visual log)
9. Default transition is a cross-dissolve. Wipes are saved for chapter cards. Black only for big breaks. (REF-A 2:50, 0:17)
10. Chapter = punch line + 5-6 s breath + chapter card with era bar + lattice wipe. (REF-A 2:43-2:50, 7:58)
11. Hook: one shot per phrase, shots taken from later in the video, ends on the title line, then black. (REF-A 0:00-0:19)
12. First frame = a full, moving, coloured map. (REF-A 0:00)
13. Script: calm third person, no questions, no "you", no humour, cause and effect, 13-word median sentence. (transcript)
14. Abstract ideas get a symbol on the map (cross, crack, storm clouds). (REF-A 0:58, 14:45, 17:36)
15. Vignette and god rays on most shots. (REF-A 0:12, 11:42)
