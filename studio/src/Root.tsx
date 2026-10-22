import { Composition } from 'remotion';
import { RenderTest } from './RenderTest';

// 16:9 1920x1080 @ 30 fps (BRAND_TEMPLATE)
export const Root = () => (
  <>
    <Composition id="RenderTest" component={RenderTest} durationInFrames={90} fps={30} width={1920} height={1080} />
  </>
);
