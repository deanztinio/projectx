import { staticFile } from 'remotion';

// Fonts are bundled locally (Google Fonts CDN is blocked), from npm @fontsource (OFL licences in public/fonts).
// Brand fonts from the How-So study (BRAND.md "Fonts"): EB Garamond for all text, Crimson Pro Italic for italic lines.
// Inter is the old day-one placeholder, kept so RenderTest still renders.
const LATIN =
  'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD';
const LATIN_EXT =
  'U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF';

type Face = { family: string; weight: string; style: 'normal' | 'italic'; file: string; range?: string };

// One face per subset: latin + latin-ext (diacritics in names like "Ḫattušili").
const brand = (family: string, slug: string, weight: string, style: 'normal' | 'italic'): Face[] => [
  { family, weight, style, file: `fonts/${slug}-latin-${weight}-${style}.woff2`, range: LATIN },
  { family, weight, style, file: `fonts/${slug}-latin-ext-${weight}-${style}.woff2`, range: LATIN_EXT },
];

const faces: Face[] = [
  { family: 'Inter', weight: '400', style: 'normal', file: 'fonts/inter-latin-400-normal.woff2' },
  { family: 'Inter', weight: '700', style: 'normal', file: 'fonts/inter-latin-700-normal.woff2' },
  ...(['400', '500', '600', '700'] as const).flatMap((w) => brand('EB Garamond', 'eb-garamond', w, 'normal')),
  ...(['400', '500'] as const).flatMap((w) => brand('EB Garamond', 'eb-garamond', w, 'italic')),
  ...(['400', '500'] as const).flatMap((w) => brand('Crimson Pro', 'crimson-pro', w, 'normal')),
  ...(['400', '500'] as const).flatMap((w) => brand('Crimson Pro', 'crimson-pro', w, 'italic')),
];

export const loadFonts = () =>
  Promise.all(
    faces.map((f) => {
      const face = new FontFace(f.family, `url(${staticFile(f.file)}) format('woff2')`, {
        weight: f.weight,
        style: f.style,
        ...(f.range ? { unicodeRange: f.range } : {}),
      });
      document.fonts.add(face);
      return face.load();
    }),
  );
