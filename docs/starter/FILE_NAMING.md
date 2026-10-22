# File naming + delivery layout (locked from day one)

Locked on channel 1 after we had to rename everything halfway. Use it from the very first file.

## File names
`<slug>_CH<n>_<ASSET>_v<n>.<ext>`
- slug = short video name in kebab-case (e.g. `great-fire`). No codes like VID002.
- NO zero padding: `CH3`, `v4` (never `CH03`, `v04`).
- NEVER the word "final" in any name. The delivered version is simply the last approved version.
- ASSET codes: `PREV` (review preview), `VO`, `SFX`, `FOLEY` (foley + ambience), `MX` (music, dnz's),
  `THUMB`. The delivered video has NO asset tag: `great-fire_CH3_v5.mp4`.
- Script: `<slug>_SCRIPT_v3.md`. Clip slot labels: `<slug>_CH3_CLIP1`.
- Preview and delivery share one version number. Stems match the video's version and duration and
  start at frame 0.

## Folders (identical in the cloud `studio/renders/<slug>/` and on the PC `<PC root>\<slug>\`)
```
<slug>\
  1_SCRIPT\
  2_PREVIEWS\            latest preview per chapter; older ones in 2_PREVIEWS\_old
  3_DELIVERY\
    CH0\                 <slug>_CH0_v3.mp4 + _VO_ / _SFX_ / _FOLEY_ wavs of the same version
    CH1\ ...
    _old\                superseded versions
  4_GFX\                 stills, thumbnail mockups
  5_PREMIERE\            dnz's own. Claude never writes here.
  6_EXPORTS\             dnz's own. Claude never writes here.
```
- Split-transfer parts go in a `_parts` subfolder next to their target, with one `join-parts.bat` at
  the video root that rebuilds every file and deletes the parts.
- Source/working files (code, raw VO, cue lists) live in `studio/videos/<slug>/` and are not renamed.
- Claude can't move or delete files on the PC: any reorganisation ships as a `.bat` dnz double-clicks.
