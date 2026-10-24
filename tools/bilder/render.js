// Rendert SVG-Dateien aus assets/bilder/ als PNG (Chromium via Playwright).
// Aufruf:  node tools/bilder/render.js            -> alle SVGs
//          node tools/bilder/render.js name1 name2 -> nur diese (ohne Endung)
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const dir = path.resolve(__dirname, '..', '..', 'assets', 'bilder');

(async () => {
  let files = fs.readdirSync(dir).filter(f => f.endsWith('.svg')).sort();
  const only = process.argv.slice(2);
  if (only.length) files = files.filter(f => only.includes(f.replace(/\.svg$/, '')));
  const browser = await chromium.launch();
  const page = await browser.newPage();
  for (const f of files) {
    const svg = fs.readFileSync(path.join(dir, f), 'utf8');
    const m = svg.match(/<svg[^>]*width="(\d+)"[^>]*height="(\d+)"/);
    const w = m ? parseInt(m[1], 10) : 1600;
    const h = m ? parseInt(m[2], 10) : 900;
    await page.setViewportSize({ width: w, height: h });
    await page.goto('file://' + path.join(dir, f));
    await page.waitForTimeout(80);
    const out = path.join(dir, f.replace(/\.svg$/, '.png'));
    await page.screenshot({ path: out, clip: { x: 0, y: 0, width: w, height: h } });
    console.log('PNG:', path.relative(process.cwd(), out));
  }
  await browser.close();
})();
