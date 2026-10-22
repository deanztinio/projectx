# Reference study: REF-B "The Bronze Age: 2000 Years in 20 Minutes" (How-So)

Source: https://www.youtube.com/watch?v=IpyAEDPa4Nw · PC copy: `D:\01 CLAUDE\PROJECT X\The Bronze Age 2000 Years in 20 Minutes.mkv`
· Cloud copy: this folder (joined from 6 parts, SHA256 matches the PC file) · Length: 22:10 (1330.6 s), **3840x2160 (4K)**, 30 fps · Published 23 Jul 2026
· Channel: How-So (@How-So), about 90K subscribers, two creators
· Views: about 319K (web scrape, Oct 2026), so about 1x the channel median. Not an outlier yet, although it is their most polished video. The broad, famous topics did 10x better (Medieval Europe about 3.6M, The Islamic World about 3.5M). Topic choice matters as much as polish.

Studied 2026-10-22 at max effort. Compare with REF-A (`../howso-medieval/NOTES.md`): same system, newer and more 3D.

## Files in this folder
Same layout as REF-A: `frames/` (1 fps, 960 wide, file number = second), `cuts/`, `sheets/` (30 s each), `intro/` (first 5 s at 10 fps), `data/` (visual_log.md, transcript_timed.md, srt_analysis.json, cuts.json, motion.txt, loudness.txt, palette_sheet.png, badges.png), `type/`. The full-resolution 4K video is here for any frame you need sharp.

## 1. First 5 seconds, second by second
| t | What's on screen | Text | Motion | Sound |
| --- | --- | --- | --- | --- |
| 0.0-1.0 | Top-down relief map of the Near East: sandy desert, dark teal seas. Empty | none | Slow push-in | Music from 0 s. VO at 0.42 s: "In the ancient Near East, the world's first civilizations emerged." |
| 1.0-1.5 | A white pyramid sprite POPS IN at Giza (scales up from nothing in about 0.3 s) | none | Push-in | VO |
| 1.5-2.0 | A ziggurat sprite pops in on Mesopotamia; a red territory blooms in the north | none | Push-in | VO |
| 2.0-3.0 | Pharaoh statue, Sphinx, small pyramids at Egypt; a mauve territory in Anatolia; more sprites in the Levant | none | Push-in | VO |
| 3.0-5.0 | More fills and sprites keep popping (Aegean green, a palace on Crete, a statue under god rays) until the map is full | none | Push-in | VO ends 4.7 s, then a 1.4 s pause |

Pattern: the first sentence is acted out literally. "First civilizations emerged" = civilizations pop up one by one on an empty map.

## 2. Cut rhythm
- 59 hard cuts in 22:10 (median 10.5 s apart). Most changes are dissolves, so count visual beats instead: **a new shot or element every 8.5 s** (median, body), 90% within 15 s.
- Hook (0:00-0:40): one image per phrase, about 1 s each when a list is read ("Egyptians, Sumerians, Akkadians..." = one statue per name, 0:25-0:30). 13 hard cuts in the first minute.
- Body: 0-5 hard cuts per minute. The big map scenes run 20-30 s but keep changing inside (fills grow, cutouts arrive, labels build).

## 3. Typography
Same family as REF-A: old-style Garamond-type serif, warm white with a soft shadow. Closest free match: **EB Garamond** (`type/cmp_title.png`, `type/cmp_sargon.png`, `type/cmp_date.png`). Weights are heavier here than in REF-A:

| Use | Look | Example |
| --- | --- | --- |
| Main title | "THE BRONZE AGE" small tracked caps over "NEAR EAST" big tracked caps (0.35 em), "3200 - 1200 BCE" under it | 0:41 |
| Era card title | Bold tracked caps (EB Garamond 700), date range under it in regular | "THE URBAN REVOLUTION / 4000 - 3000 BCE" 2:35 |
| Big map label | Huge tracked caps, curved, built letter by letter | "AKKADIAN EMPIRE" 10:28, "ASSYRIA" 16:42 |
| Term label | Small tracked caps at bottom centre, NO box, optional small italic line under it | "WRITING / Cuneiform Script" 3:34, "CITIES" 2:45, "AGRICULTURAL REVOLUTION" 1:21 |
| Object label | Small title case placed on the object | "Temples", "Patron Deity", "Storehouse" 3:21 |
| City | Small title case next to a white square; capitals get a square with a dot and a bigger label | "Akkad" 10:13 |
| Name tag | Dark rounded box: the person's name in THEIR OWN SCRIPT (cuneiform or hieroglyphs) on top, the name in serif under it | "Sargon" 10:13, "Narmer" 6:08, "Mentuhotep II" 14:56 |
| Date badge | See section 6 | top-left, always |

- Text in: map labels build letter by letter (about 0.15 s per letter: "AKKADIAN EMPIRE" builds 10:28.7-10:31). Term labels build letter by letter too ("WRITING" in 0.7 s at 3:34), then the italic line fades in under it (3:35). Name tags fade in about 0.5 s after the cutout lands (cutout 10:12.0-10:12.8, tag 10:13.3). Out: fade.
- Spelling slip in the reference: the badge says "Greate Powers" (16:43). We spell-check every on-screen word.

## 4. Colour + finish
Sampled with k-means (`data/palette_sheet.png`):

| Role | Hex | Where |
| --- | --- | --- |
| Desert land (main colour) | #D5B594, #C19F76, #AA895B, #C7A680 | every map |
| Sea / rivers | #32413B, #32443E, #384942 (rivers glow turquoise in 3D flyovers) | every map |
| Green valleys | #4C5B4D, #546152, #769177 | 1:15, 16:15 |
| Egypt | gold / yellow / orange (#E9B65E highlight) | 5:20, 8:38 |
| Mesopotamia / Sumer | blue and cyan (#486087), purple city blobs | 5:20, 5:48 |
| Akkadian Empire | magenta, then deep purple #2D223F | 10:28 |
| Upper Mesopotamia (Assyria) | red #804035 | 13:40 |
| Era / title card darks | #131412, #1B1C15, #29241F, gold #CDA653 | 0:45, 2:38, 6:53 |
| Chariot dust stage | #EEA54F, #EBCB88, #E0B876 | 18:45 |
| Collapse grade (whole map) | burnt orange-sepia #744718, #8C561F, #583719 with near-black #14130F | 20:15 |
| End card night | #0F171E, #070B0F, blue #80A6BE, gold #E1B857 | 22:00 |

- Region colour code stays the same all video: Egypt = gold, Mesopotamia = blue, each empire its own colour. The date badge tag uses the same colour.
- Grade shifts with the story: golden light for prosperity (3:48), cold dim map for dominance (10:25), whole-map orange-sepia for the collapse chapter (20:10 to the end of the chapter).
- Vignette: yes, lighter than REF-A (corners about 22% darker than the centre on average).
- Light: god rays from above on cards and dioramas, light sweeps along rivers (6:28, 8:38), spotlights on statues (13:19, 15:59), sun-flare whiteout (9:33).

## 5. Motion + camera
Measured at 4 fps (`data/motion.txt`):
- Camera moves **79% of the time**. Median zoom 0.9%/s (75th percentile 4.1%/s). Median pan 20 px/s on a 1920 frame. Push-ins 42%, pull-outs 33%.
- Truly still: 3.8% of the video (51 s). Longest still stretches: the end card (4.8 s at 22:02), the pantheon card (3.5 s at 14:42), Khafre (3.5 s at 9:06).
- New here: **3D terrain flyovers** (oblique camera over real relief, rivers glowing, clouds below the camera: 1:37-2:06, 4:41, 16:30) and **slow orbits** around 3D dioramas (2:42 the village becomes a walled city, 9:21 Giza construction, 21:35 museum gallery).
- Transitions: cross-dissolves by default; a foreground object walks past the camera as the wipe (5:01); sun-flare whiteout (9:33); fade to black around the main title (0:40, 0:51) and before the epilogue (21:29, 6 s of black, the longest pause of the video).

## 6. How it shows things
| Thing | How (timecode) |
| --- | --- |
| Places / maps | Two map types. (1) Top-down relief map, sandy desert, teal seas and rivers; territories as soft glowing colour clouds (12:54), growing hatched zones (5:12) or solid fills with a glowing rim (10:25, 16:12). (2) Oblique 3D terrain flyovers with sprites standing on the land (1:37, 16:30). City = white square, capital = square with a dot. Trade routes = thin white dotted lines with donkey caravans walking them (13:46). Attacks = white strike arrow (15:40). Battle = crossed swords + name ("Kadesh" 19:09). |
| Growth / decline of a state | Fill spreads from the capital like ink (10:13-10:16). Decline: the fill dissolves into teal smoke (5:30), shatters into drifting fragments (11:14), or fades (12:51). A ruler head shrinks away when the king loses power (11:55). |
| Dates / time jumps | **Date badge, top-left, on every shot**: "c. 2300 BCE" in a dark rounded box, a thin progress bar under it showing where we are in the 2,000 years, then two tags: the period ("Early Bronze") and the region or empire in its colour ("Akkadian E."). See `data/badges.png`. Era cards and the title carry a **multi-row timeline bar**: Egypt row, Mesopotamia row, era row, the active segment lit (0:41, 2:35). |
| Numbers | Rare and spoken only. No charts. |
| Trends / comparisons | Two medallions side by side, Egypt (gold) vs Mesopotamia (blue) (5:18). Split era cards, gold left vs blue right (6:51). Greyscale map with only the five great kings in colour, linked by white lines with gifts sliding along them (17:39). A pantheon as a pyramid of small white god figures on black (8:03, 9:10, 14:40). Kings toppling like dominoes for a chain collapse (19:40). |
| People | Real artifact cutouts: Sargon's bronze head (10:12), the Narmer Palette relief (6:08), Hammurabi (13:59), Ramesses II (19:12). They slide in from the edge into the left or right third. Name tag with native script. Several rulers at once = statues standing ON the map like board-game pieces (16:30) or lit one by one on a dark stage (13:19, 15:59). Crowds = carved-relief figures (soldiers 7:08, a procession 3:48). Prehistory = red rock-art figures animated walking and hunting on a landscape painting (0:53, 1:21). |
| Quotes / documents | Objects, not quotes: tablets, steles and the Code of Hammurabi shown as lit 3D objects with a term label (3:31, 14:19). Letters = lines of cuneiform floating up (17:56). |
| Daily life / building | 3D dioramas: houses multiply and a wall draws itself around a village (2:42), pyramids rise while workers drag blocks (9:21), a whole scene built from real Egyptian tomb models (15:05). |
| Chapter changes | Forward-pointing punch line, then a 4.7-6.6 s pause on the era card: title + date range on top, gold-lit artifact cutouts in the middle, the timeline bar at the bottom (2:35, 6:51, 9:48, 12:32). Late Bronze Age: five king statues lit by coloured spotlights (15:59). Collapse: the same five kings with fire at their feet, then they topple (19:32-19:45). |
| Ideas (abstract) | Rings pulsing out from a city = its control of the land (3:15). Sun flare = "join the sun" (9:33). Smoky vignette bubbles on black = myths and legends (21:22). |

## 7. What moves at every moment
- Still frames are only 3.8% of the video. Even cards have moving light, smoke or particles.
- Map scenes stack 2-4 motions: camera push + fill growing + cutout arriving + clouds drifting (10:12-10:31).
- Change per minute stays even (mean frame difference 5.5-14.7 every minute). The quietest minutes (6:00, 8:00) are long map passages that still drift.

## 8. Sound (kept short: dnz said music and SFX are low priority)
- Voice: male (median pitch about 140 Hz), same calm documentary read as REF-A. 142 words per minute while talking, 115 over the whole span. About 1 s between sentences. 4.7-6.6 s at era cards.
- Loudness: integrated -22.3 LUFS, range 3.7 LU. Voice moments about -22.2 LUFS, music alone about -34.3 LUFS, so the bed sits about 12 LU under the voice. That is lower than REF-A.
- Music: at era cards the music DROPS (down to -42 to -49 LUFS at 6:50 and 15:58) instead of swelling. The music in those pauses is sparse and sustained (about 1 note onset per second), so ambient pads rather than rhythm.
- SFX: not studied, by dnz's choice (2026-10-22).

## 9. Script structure (from the transcript)
- 2,541 words, 180 sentences, 22:03 of speech.
- **Hook (41 s, 6 sentences):** era + place ("In the ancient Near East, the world's first civilizations emerged.") → a growth chain ("farming villages grew into fortified cities, cities linked to form kingdoms, and kingdoms expanded into vast empires.") → "Yet the path was never straightforward." → "cycles of growth, prosperity, and collapse" → a roll call of peoples, one statue each → title line "This is the Bronze Age Near East." → 1 s black → main title with the full timeline (0:41). Here the title comes RIGHT after the hook.
- **Prologue (106 s):** "Our story begins in prehistoric times." Hunter-gatherers → farming → villages → cities, ending on "a new era that we call the Bronze Age."
- **6 era chapters, 117-256 s each (about 190 s average, longer than REF-A).** Openers anchor time and place and name the new player: "Around 2000 BCE, a new player entered the stage, the Amorites." (12:37), "Out of the fractured world of 1600 BCE, a new order emerged." (16:04). Closers point forward: "But a dramatic reversal would soon change everything." (9:44), "The entire Near East was fragmenting, but not for long." (15:54), "But at the very moment it reached its zenith, it collapsed completely." (19:25).
- Inside chapters, Egypt and Mesopotamia alternate in parallel ("Meanwhile, in Egypt...").
- **Epilogue (34 s):** "its achievements endured" over a museum gallery of the artifacts we met, then a **next-video teaser**: "In the next video, we will venture into the Iron Age..." No "subscribe" or "like".
- Sentence length: median 13 words (10% are 7 or fewer, 10% are 23 or more, max 39).
- Short fragments for weight, one at a time: "Life was fairly comfortable." (1:08), "The first cities." (2:52), "A king." (6:06), "The pyramids." (9:25).
- 1.2 dates per minute. 0 questions, 0 exclamations, 0 em dashes. "We" 9 times, only in the framing ("Our story begins", "what we call", "In the next video, we will"). Never "you". No humour.
- Repeated story shape: growth → prosperity → collapse → a new player. The script names this cycle in the hook and keeps returning to it ("yet another reversal of fortunes").

## 10. Packaging
- Title: "The Bronze Age: 2000 Years in 20 Minutes", the same "<Subject>: <N> Years in <M> Minutes" pattern as REF-A. Runtime 22:10.
- Uploaded in 4K.
- Thumbnail: not studied yet (YouTube images are blocked from the cloud).

## 11. dnz likes / dislikes
- Likes (dnz 2026-10-22, for the channel overall): premium feel, engaging script, map animation that makes it easy to understand.
- Dislikes: not given yet.

## 12. Rules this adds to BRAND.md (each with its timecode)
1. Date badge with a progress bar and two tags (period + region in its colour). (REF-B 10:12, `data/badges.png`)
2. Multi-row timeline bar on the title, every era card and the end card, active segment lit. (REF-B 0:41, 2:35, 21:48)
3. Name tag shows the person's name in their own script above the serif name, about 0.5 s after the cutout lands. (REF-B 10:13)
4. Term labels: small tracked caps at the bottom centre, no box, built letter by letter, optional italic line. (REF-B 3:34)
5. One colour per region or empire, kept for the whole video, matched in the badge tag. (REF-B 5:18, 10:28)
6. First 5 s act out the first sentence on the map. (REF-B 0:00-0:05)
7. Hook roll call: one image per name, about 1 s each, exactly on the word. (REF-B 0:25-0:30)
8. Daily life and building are shown as 3D dioramas, not as maps. (REF-B 2:42, 9:21, 15:05)
9. Several rulers at once = statues standing on the map like game pieces. (REF-B 16:30)
10. The grade follows the story: gold for prosperity, sepia-orange for collapse. (REF-B 3:48, 20:10)
11. Era cards drop the music; the next line starts on silence. (REF-B 6:50, 15:58)
12. Epilogue revisits the artifacts we met, then a teaser for the next video, no call to action. (REF-B 21:35, 21:49)
13. End card: "Thank You for Watching" + handle top-centre, the full timeline at the bottom with a play arrow pointing to the next video, 20 s. (REF-B 21:48)
