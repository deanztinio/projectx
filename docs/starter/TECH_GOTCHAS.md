# Technical gotchas from channel 1 (save yourself hours)

## Cloud container + studio
- The container is wiped between sessions. The shared project folder is the working copy; work in a
  local copy for speed (`sync.sh pull` / `push`) and never leave work only in the local copy.
- Daily backup task: tar the studio's code/docs/fonts/images (exclude node_modules, out, renders,
  references, all audio/video, .env, files >10 MB) into the repo and merge a PR. Restore from history.
- Remotion's own browser download host is blocked: set
  `REMOTION_BROWSER=/opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell`.
  Never run `playwright install`.
- Google Fonts CDN and GitHub raw were blocked: bundle fonts as woff2 from npm `@fontsource/*`
  into `public/fonts`. npm, PyPI and GitHub releases work.
- Everything must be a pure function of the frame. Timing in frames = seconds × fps.
- Review renders at `--scale=0.5` (~40 s per 60 s of video) and contact sheets of 1 still/second.
- The Read tool can show a STALE image when a file path is overwritten: write stills to new filenames.
- Final render: `--codec=h264 --crf=18`, then ffmpeg `loudnorm=I=-14:TP=-1.5:LRA=11`, video stream copied.
- Stems: one render per audio mode (all / vo / sfx / foley / none) from the same composition so they
  line up to the frame and match the video's duration.

## Maps (d3-geo + world-atlas)
- SVG clipPath/mask of coastlines FAILS at high zoom in headless Chromium: cut shapes to land with
  the `polygon-clipping` npm package instead.
- Check every map label for overlaps on the actual still, at every zoom level.
- Flags: check they can't be misread (a single star on red reads as China).

## Colours / drawing
- Use 6-digit hex in generated SVG; a 3-digit hex bug turned hair blue once.
- When a helper matches by substring, make anchor names unique.

## ElevenLabs
- Header `xi-api-key` (no "Bearer"). Scope the key to TTS + voices read.
- Check the voice supports the model. A model the voice wasn't trained on silently swaps in a
  generic voice (it happened with a newer model).
- Requests over ~2,000 characters returned 502: split at paragraphs.
- Use the with-timestamps endpoint; save the alignment JSON next to the mp3 (`vo/chN.json`) and drive
  animation timing from it.
- Pace tweaks (+5% speed), pause trimming and silence removal: do them locally with ffmpeg, free.
- Bracket emotion tags worked on the model we used; test on the new voice before relying on them.
- Claude can't listen. dnz checks pronunciation and delivery; regenerate only flagged lines.

## Epidemic Sound
- Connector search + `DownloadSoundEffect` work; downloads need the `audiocdn.epidemicsound.com`
  host allowed (environment secret with placeholder header `X-Allow: 1`).
- Downloads are hi-res WAV (a whole video's cues reached ~3 GB): trim each to the used part before
  mixing, keep a `manifest.md` (cue id → search term → file), never sync raw files to the PC.
- Mix in batches of ≤40 ffmpeg inputs. Level beds by mean volume and hits by peak, then set the whole
  stem to a target LUFS under the VO.
- Measure VO vs SFX vs foley with ffmpeg (`ebur128` / `volumedetect`) before every preview.

## Research
- youtube.com is blocked: get transcripts through youtubetotranscript.com via WebFetch, or ask dnz.
- Wikipedia/Wikimedia were blocked or rate-limited (HTTP 429, about one query a minute). Allow the
  hosts in network settings early, or dnz downloads images manually. Use WebSearch as fallback.
- YouTube Data API: 10,000 units/day; `search` costs 100 units. Quota ran out once mid-research.
  Prefer 1of10 for discovery, the API for exact stats.
- 1of10 `optimize_video` only works on a published video on a channel linked in dnz's 1of10 account.
  Link the new channel once it exists.
- Grok (xAI Responses API, `grok-4.x` + `x_search` tool): MUST send `"stream": true` (non-streaming
  X search took ~70 s and the proxy returned 502). Keep `max_turns` ~3; one 4-part question cost
  ~$0.39. Ask for post URLs + handles so claims can be traced. Cost = `usage.cost_in_usd_ticks / 1e10`.
- Public-domain images only (pre-1900 works, government works). No Getty or modern press photos;
  modern people get a framed PHOTO SLOT for dnz to fill.

## PC sync (Claude desktop app must be open on the PC)
- `device_commit_files` rejects files over 25 MB (100 MB per call): `split -b 23M -d -a 2` into
  parts, commit them to `_parts\`, ship a `join-parts.bat` (`copy /b part00+part01 file.mp4`) that
  dnz double-clicks. Lossless, no re-encode.
- Claude can't move, rename or delete PC files: ship `.bat` files for that.
- Copy only the latest preview per chapter. Big final copies need dnz's yes.

## Permissions
- Read-only tools pre-approved in `.claude/settings.json` (see starter file). Applies to threads
  started after the merge. Credit-spending and writing tools still prompt. Add new research domains
  to the file in a PR rather than approving prompts one by one.
