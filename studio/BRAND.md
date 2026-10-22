# PROJECT X (channel 2): brand + house rules (read this first)

The ONE page of current rules. Anything older that disagrees with this file is stale: fix or delete
it. Every rule cites where it came from: a reference timecode (`REF-A 0:12`) or dnz's approval
(`dnz 2026-10-22`). Visual building blocks: `library/INDEX.md`. Updated: 2026-10-22.

**Status: DRAFT from the How-So reference study.** It locks after the design test stills and the
voice audition (master prompt §6). Details and evidence: `references/howso-medieval/NOTES.md` (REF-A)
and `references/howso-bronze-age/NOTES.md` (REF-B).

**The copy rule:** we copy How-So's look, art style, pacing, script style and maps. Only the logo,
the voice and the channel name are our own. (dnz 2026-10-22)

## Channel
- Niche: big history eras told in one sitting, same as How-So. (dnz 2026-10-22)
- Angle / one-line promise: a whole era in about 20 minutes, told as one clear story of cause and
  effect, on maps that move. (dnz 2026-10-22: "I feel like I really understand because of the
  animation in the map")
- Title format: **"<Era or region>: <N> Years in <M> Minutes"**. (REF-A, REF-B titles. Their two big format
  videos got about 3.5M views each; their plain titles got 35K-117K.)
- Topic lesson: broad, famous eras win. Medieval Europe about 3.6M and The Islamic World about 3.5M,
  but The Bronze Age (more polished, narrower topic) about 0.3M. (REF-B header)
- Format: 16:9, 1920x1080, 30 fps (both references are 30 fps; REF-B is uploaded in 4K, consider 4K
  finals later). Runtime about 22 min for a "20 Minutes" title (REF-A 22:24, REF-B 22:10).
  1 upload per week (master prompt).
- Tone: calm, confident, third-person documentary. See `SCRIPT_RULES.md` "Channel voice".
- dnz likes: premium feel, engaging script, map animation that makes it easy to understand.
  Dislikes: not given yet. (dnz 2026-10-22)

## References
| ID | Video | What we take from it | What we don't |
| --- | --- | --- | --- |
| REF-A | How-So, "Medieval Europe: 1000 Years in 20 Minutes" (2025, about 3.6M views, about 11x the channel median) | Everything: relief map + fills, cutouts, chapter cards with the era bar, date badge, transitions, pacing, script voice | Their logo, voice and handle |
| REF-B | How-So, "The Bronze Age: 2000 Years in 20 Minutes" (2026, 4K, newest) | Everything: badge with progress bar + tags, multi-row timeline bar, native-script name tags, term labels, 3D terrain and dioramas, epilogue + next-video teaser, end card | Their logo, voice and handle; their typo ("Greate Powers" 16:43) |

## Look
### Palette (sampled from the references)
| Role | Hex | Source |
| --- | --- | --- |
| Sea, the main colour of every map | #2C4448 (dark slate teal) | REF-A 0:23 |
| Deep sea / map shadow | #1D2C2F | REF-A 5:45 |
| Land, Europe-type eras (grey-beige relief) | #AB9E92, #BEB2A4 | REF-A 0:23 |
| Land, desert eras (sand relief) | #D5B594, #C19F76; sea there #32413B | REF-B 0:03 |
| Card background (dark, warm) | #17140B, #2E2D28, #131412 | REF-A 2:45, REF-B 6:53 |
| Gold accent (titles light, Early era, Egypt) | #ECD17A / #EECF79 | REF-A 2:45, 2:46 |
| Era colours on the badge and era bar | Early #EECF79 gold, Central #86C4EB light blue, Late #B175D3 purple | REF-A 2:46, 11:05, 17:45 |
| Text | #FBF8F2 warm white, soft dark shadow | REF-A 2:43, REF-B 2:35 |
| Text box (badge, caption, name tag) | near-black at about 60-70% opacity, small rounded corners | REF-A 4:01, REF-B 10:13 |

- **One colour per state or region, kept for the whole video**, and the same colour on its badge tag.
  Examples: Rome crimson #A53F50, Franks teal #3F8A81, Byzantium magenta #85456B, Umayyads green
  #568176 (REF-A 0:23, 5:45, 4:50); Egypt gold #F5DA78, Mesopotamia cyan #67EFF3, Akkad purple,
  Assyria red #804035 (REF-B 5:18, 10:28, 13:40, `badges.png`).
- Fills are translucent so the relief shows through, with a soft glow along the border.
  (REF-A 0:23, REF-B 10:25)

### Fonts (closest free match, bundled in `public/fonts`)
- **EB Garamond** for everything: titles, chapter titles, map labels, names, dates, numbers.
  Weights: 400-500 for labels and dates, 500 for chapter titles, 700 for era-card titles.
  (REF-A 2:43, 1:14, 0:20; REF-B 2:35, 10:13; `type/` comparisons)
- **Crimson Pro Italic** for italic lines: translations and subtitles ("Imperator Romanorum",
  "Cuneiform Script"). (REF-A 5:53, REF-B 3:35)
- No sans-serif anywhere. (REF-A, REF-B: none seen)
- Sizes on a 1920x1080 frame (approximate; match side by side in the design test):

| Text | Size | Case + tracking | Source |
| --- | --- | --- | --- |
| Main title | about 90-100 px | CAPS, 0.35 em | REF-A 2:40, REF-B 0:41 |
| Chapter / era card title | 55-70 px | Title Case 0.2 em (REF-A) or bold CAPS 0.12 em (REF-B) | REF-A 2:43, REF-B 2:35 |
| Date range under a title | about 40 px | numerals | REF-B 2:35 |
| Big territory label | 40-80 px, scales with the map | CAPS, 0.3 em, curved along the territory | REF-A 0:22, REF-B 10:28 |
| City label | 22-32 px, scales with the map | Title case next to a dot or square | REF-A 1:14, REF-B 10:13 |
| Name tag / caption | about 34 px | Title case | REF-A 4:01, REF-B 10:13 |
| Date badge | about 30 px | numerals, "c." and "BCE" smaller | REF-A 0:20, REF-B 10:12 |
| Term label | about 32 px + 24 px italic line | CAPS 0.2 em + italic | REF-B 3:34 |

### Texture + finish
- Vignette on almost every shot (corners about 20-35% darker than the centre). (REF-A, REF-B frame
  measurement)
- God rays and slow light sweeps on cards, dioramas and many maps. (REF-A 0:12, 5:09; REF-B 2:35, 8:38)
- Cloud wisps drifting over the edges of maps. (REF-A 0:00, REF-B 10:12)
- Muted, slightly desaturated grade; warm light, cool shadows. The grade follows the story: golden
  for prosperity, cold and dim for conquest, orange-sepia for collapse, purple haze for plague.
  (REF-B 3:48, 10:25, 20:10; REF-A 17:42)
- Paintings are darkened or tinted to sit with the maps. (REF-A 1:03, 18:13)

### Text animation in/out
- Map and term labels **build letter by letter, left to right, about 0.1-0.15 s per letter**, each
  letter fading in. (REF-A 0:21.8-0:23.0, REF-B 10:28.7-10:31, 3:34)
- Captions and name tags fade in (about 0.25 s) at the bottom corner of their cutout, as it lands or
  up to 0.5 s after. (REF-A 4:01.5, REF-B 10:13.3)
- Italic subtitle lines fade in about 0.5-1 s after their main line has built. (REF-B 3:34.7-3:35.3)
- Chapter titles fade in about 0.4 s; old text fades out about 0.5 s. (REF-A 2:42-2:44)
- Never bounce, pop, typewriter cursor or kinetic type. (REF-A, REF-B: none seen)

### Camera moves
- **The camera never stops.** It moves about 80% of the time (REF-A 82%, REF-B 79%). Truly still
  frames are under 6% of a video and only on cards, max about 5 s. (`data/motion.txt` in both)
- Default drift: median zoom about 1% per second, median pan about 20 px/s; push-ins more often than
  pull-outs. (REF-A, REF-B motion data)
- Travel between regions: a 1-2 s eased move across the same map, not a cut. (REF-A 0:44, 3:05)
- Parallax in dioramas and composited paintings (2-4 layers). (REF-A 8:22, 11:42)
- 3D terrain flyovers (oblique camera, clouds below) and slow orbits around dioramas. (REF-B 1:37,
  2:42, 21:35)

### Transitions
- Default: cross-dissolve, 0.3-1 s. (REF-A, REF-B)
- Out of a chapter card: X-line / diamond-lattice wipe with coloured edges, about 0.5 s.
  (REF-A 2:50, 5:20, 8:04)
- Occasional variety: diamond tiles (REF-A 3:59), whip blur (REF-A 3:41), zoom-blur push into the
  map (REF-A 8:21), ragged or burnt edge (REF-A 1:02), torn paper (REF-A 19:27), a foreground object
  walking past the camera (REF-B 5:01), sun-flare whiteout (REF-B 9:33).
- Black only at big breaks: 1-2 s after the hook, about 6 s before the epilogue. (REF-A 0:17,
  REF-B 0:40, 21:29)

### Logo / intro sting / end card
- No logo sting at the start. The video opens straight on a full, moving map. (REF-A 0:00, REF-B 0:00)
- **Logo: our own, to design in the design test.** (dnz 2026-10-22: logo is not copied)
- Main title card right after the hook (REF-B 0:41) or after the prologue (REF-A 2:40): title in tracked
  caps over a dark landscape painting with god rays, the era timeline building in under it.
- End card, 16-20 s: "Thank you for watching" + our handle top-centre, the full timeline (or era
  strip) at the bottom, a play arrow pointing to the next video, room for end-screen elements.
  (REF-A 22:08, REF-B 21:48)

## Pacing
- Hook: one shot per phrase, 1-3 s each, using shots from later in the video. A list of peoples or
  themes gets one image per name, exactly on the word. (REF-A 0:00-0:17, REF-B 0:25-0:30)
- Body: **something new every 5-10 s** (median beat 7-8.5 s; 90% within 13-15 s). A beat is a new
  shot OR a new element in the same shot (cutout, fill, label, arrow). (visual logs, both)
- Chapters: REF-A uses 12 short chapters of 70-120 s; REF-B 6 era chapters of 2-4 min. Master prompt
  asks 2-3 min: use REF-B's era-chapter rhythm. (REF-A, REF-B script tables)
- **Chapter break = a short forward-pointing line, then a 5-6.5 s pause on the chapter card** (music
  carries it), then the wipe into the first map. (REF-A 7:58, 17:39; REF-B 6:50, 15:58)
- Pauses: about 0.3 s between phrases, about 1 s between sentences. (both SRTs)

### How chapters are signposted
- Chapter card: chapter number (roman numeral, REF-A) or era name (REF-B), title, date range, over a
  dark painting with god rays, with the **era bar / timeline bar** at the bottom showing the current
  segment lit and the rest dimmed or greyscale. (REF-A 2:43, 10:56; REF-B 2:35, 6:51)
- REF-B era cards add gold-lit artifact cutouts in the middle, or a split screen of the two regions
  (gold left, blue right). (REF-B 2:35, 6:51, 9:48)
- **Date badge top-left on every shot** (maps and art): dark rounded box, "c. 2300 BCE", a thin
  progress bar for where we are in the whole span, then two tags: period + region in its colour.
  (REF-B 10:12, `badges.png`; simpler version REF-A 0:20)

### How dates, numbers, places, people, trends are shown
| Thing | Rule | Source |
| --- | --- | --- |
| Places | Relief map with translucent colour fills, dark sea, drifting clouds. Territories change by spreading like ink from the capital, never by a cut. Frontiers = glowing white line. Movements = curved white arrows. Battles = crossed swords + name. Trade = dotted lines with caravans walking. | REF-A 0:19, 1:48, 1:59, 5:00; REF-B 10:13, 13:46 |
| Decline | Fills dissolve into smoke, shatter into fragments, or fade; a ruler head shrinks away. | REF-B 5:30, 11:14, 11:55 |
| Life, building, economy | Physical map full of sprites (towns, castles, ships, riders) or a 3D diorama that grows (village to walled city). | REF-A 8:12, REF-B 2:42, 9:21 |
| Dates | The badge + chapter-card date range. Big dates are spoken, not flashed. | REF-A 0:20, REF-B 10:12 |
| Numbers | Spoken only. No charts. | REF-A, REF-B |
| People | Real museum objects (statues, reliefs, mosaics, coins) cut out, sliding in from the edge into the left or right third, with a name tag. REF-B tags show the name in the person's own script above the serif name. Many rulers = statues standing on the map like game pieces. | REF-A 2:54, 4:01; REF-B 10:12, 16:30 |
| Crowds | Carved-relief or manuscript figures moving as groups. Prehistory = red rock-art figures. | REF-B 7:08, 0:53; REF-A 8:32 |
| Comparisons | Two medallions or a split screen; greyscale everything except the subjects; glowing regions that split. | REF-B 5:18, 17:39; REF-A 4:40 |
| Ideas | A symbol on the map: a glowing cross, a crack, storm clouds, rings pulsing out from a city, a pyramid of gods. | REF-A 0:58, 14:45, 17:36; REF-B 3:15, 8:03 |
| Terms | Term label (small tracked caps + italic line) under the object, or a term card in a dark box. | REF-B 3:34, REF-A 5:53 |

## Text on screen
- Text only names things: places, people, terms, dates. It never repeats the narration sentence.
  (REF-A, REF-B: no sentence ever appears on screen)
- No quotes or paragraphs on screen. Documents are shown as objects. (REF-B 3:31, 14:19)
- Every on-screen word is spell-checked. (REF-B 16:43 typo)
- Keep labels inside the safe margin and never overlapping (master prompt §9).

## Images, clips, people
- **Code + public domain only.** No AI image or video models, no Blender for now. How-So's 3D
  terrain is built in code from real elevation data; dioramas become layered 2.5D scenes; sprites
  come from public-domain museum photos, paintings and old engravings. (dnz 2026-10-22, option A;
  Blender only if the design stills look flat and dnz agrees)
- Maps and terrain: built in code from real elevation data (AWS terrain tiles work from the cloud).
- People and objects: real museum pieces, public domain or CC0 photos (Wikimedia Commons images
  download fine from the cloud; Met, Smithsonian and Cleveland sites are blocked here), cut out.
- Paintings: public domain, darkened or tinted to match, slow pans. (REF-A 1:03, 18:53)
- Third-party clips: none in the references, so none planned.
- Modern people: a labelled PHOTO SLOT for dnz (TECH_GOTCHAS).

## Sound
- Voice: **our own** (dnz 2026-10-22). ElevenLabs voice <TBD by audition>, model <TBD>, settings
  <TBD>. Confirm the voice is trained for this model. Target energy from the references: male-range,
  calm, even documentary read, about 145-150 words per minute while talking. (REF-A, REF-B)
- Script length: about 2,550-2,650 words for about 22 min at that pace. (REF-A 2,645 words,
  REF-B 2,541 words)
- Levels measured in the references: integrated -24 to -22 LUFS before upload normalisation, range
  3.7 LU. Music bed 8-12 LU under the voice. (REF-A, REF-B `data/loudness.txt`) Our masters follow
  the master prompt: -14 LUFS, -1.5 dBTP.
- Music is dnz's. Style: continuous cinematic orchestral / ambient bed under the voice; at chapter
  cards it either swells briefly (REF-A 12:26, 17:39, 20:26) or drops to near silence (REF-B 6:50,
  15:58). Epidemic Sound is what How-So credits.
- Epidemic search prompts (short, generic):
  1. "Cinematic documentary underscore, slow build"
  2. "Ambient orchestral strings, history documentary"
  3. "Epic orchestral swell, short sting"
  4. "Medieval ambient choir drone"
  5. "Ancient Middle Eastern ambient, duduk and strings"
- SFX and foley: not studied yet, by dnz's choice (2026-10-22). Rules from the master prompt apply.
- NEVER: the same loud whoosh every few seconds.

## Never
- The AI default slop look (see master prompt §9).
- Black/empty frames (except the planned 1-2 s black after the hook and before the epilogue).
  "final" in file names. Alpha .mov deliverables. Building past an unapproved gate.
- Sans-serif text, bouncy or kinetic text, on-screen sentences that repeat the voice. (REF-A, REF-B)
- A frame where nothing moves for more than about 5 s. (REF-A, REF-B motion data)
- Cutting between two states of the same map. Animate the change on the same map. (REF-A 10:31)
- Copying How-So's logo, voice or handle. (dnz 2026-10-22)

## Workflow gates
Title + thumb idea → script → VO → spec sheet → design sheet (stills) → MP4 preview (max 2 rounds)
→ foley pass → finals (per-chapter MP4 + VO/SFX/FOLEY stems).
