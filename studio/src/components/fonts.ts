import { staticFile } from 'remotion';

// Fonts are bundled locally (Google Fonts CDN is blocked). Placeholder until the brand picks real fonts.
const faces = [
  { family: 'Inter', weight: '400', file: 'fonts/inter-latin-400-normal.woff2' },
  { family: 'Inter', weight: '700', file: 'fonts/inter-latin-700-normal.woff2' },
];

export const loadFonts = () =>
  Promise.all(
    faces.map((f) => {
      const face = new FontFace(f.family, `url(${staticFile(f.file)}) format('woff2')`, { weight: f.weight });
      document.fonts.add(face);
      return face.load();
    }),
  );
