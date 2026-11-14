# WE3 VO v8 (Sound designer, 15 Nov 2026, Manila)

**The clock: `ottoman-empire_VO_v8s_words.json`** (+ `ottoman-empire_CH<n>_VO_v8s_timings.csv`). Time everything to the v8s files.

- Audio: `studio/renders/ottoman-empire/VO/v8/ottoman-empire_CH<n>_VO_v8s.wav` (48 kHz 24-bit, for the edit and stems) and `.mp3` (previews). Full listen: `ottoman-empire_FULL_VO_v8s.mp3`. Names check reel (34 names, 82 s): `ottoman-empire_VO_v8_NAMES-CHECK.mp3`, index in `names_check_index.json`.
- words.json: per chapter `duration`, `offset` (start if the 8 chapters play back to back), `paras` [{para, start, end, text}] and `words` [{i, word, said, start, end, para}]. Times are seconds from the chapter file start; running time = offset + start. `word` is the script spelling, `said` the respelling sent to the voice. Word starts can lag the sound by up to ~0.3 s.
- Source script: `../../ottoman-empire_VO-SCRIPT_v8.md` (word for word from the v8 doc). Pronunciation: `PRONUNCIATION_v8.md`.
- Pipeline: `make_vo_v8.py` (one take per chapter, James eleven_v4, never re-pays an existing take) -> `words_v8.py` (raw clock, `_RAW_words.json`, raw takes `*_VO_v8.mp3`) -> `space_v8.py` (v8s: paragraph gaps to 0.75 s, 1.0 s before a new [tag], sentence gaps to 0.42 s, cutting only inside >=60 ms of silence under -50 dBFS; words untouched).
- Why v8s: the raw takes read at ~160 wpm with 0.1-0.4 s between paragraphs (v1 was ~147 wpm). v8s is 21:22 at ~150 wpm.
- ElevenLabs characters used: 18,603.
