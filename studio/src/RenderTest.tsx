import { useEffect, useState } from 'react';
import { AbsoluteFill, continueRender, delayRender, interpolate, useCurrentFrame } from 'remotion';
import { loadFonts } from './components/fonts';

// Pipeline check only: proves fonts, render and frame timing work. Not a brand design.
export const RenderTest = () => {
  const frame = useCurrentFrame();
  const [handle] = useState(() => delayRender('fonts'));
  useEffect(() => {
    loadFonts().then(() => continueRender(handle));
  }, [handle]);
  const x = interpolate(frame, [0, 89], [-200, 200]);
  return (
    <AbsoluteFill style={{ backgroundColor: '#202020', justifyContent: 'center', alignItems: 'center' }}>
      <div style={{ fontFamily: 'Inter', fontWeight: 700, fontSize: 96, color: '#f0f0f0', transform: `translateX(${x}px)` }}>
        RENDER TEST {frame}
      </div>
    </AbsoluteFill>
  );
};
