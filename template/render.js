// Usage: node render.js out_dir file1.html file2.html ...
// Prints "<png> overflow <px>" per slide; any overflow > 0 means text spilled and the slide must be fixed.
const { chromium } = require('playwright-core');
const fs = require('fs'), path = require('path');
function findChrome() {
  const base = '/opt/pw-browsers';
  if (fs.existsSync(base)) for (const d of fs.readdirSync(base).sort().reverse()) {
    const p = path.join(base, d, 'chrome-linux', 'chrome'); if (d.startsWith('chromium-') && fs.existsSync(p)) return p; }
  // macOS fallback: playwright-core bundles no browser, so on a Mac the
  // launch fails with "Executable doesn't exist" unless `npx playwright
  // install` has been run. Use the Chrome that is already installed instead.
  for (const p of ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
                   '/Applications/Chromium.app/Contents/MacOS/Chromium']) {
    if (fs.existsSync(p)) return p;
  }
  return undefined; // let playwright find its own
}
(async () => {
  const [outDir, ...files] = process.argv.slice(2);
  fs.mkdirSync(outDir, { recursive: true });
  const b = await chromium.launch({ executablePath: findChrome(), args: ['--allow-file-access-from-files'] });
  let bad = 0;
  for (const f of files) {
    const m = fs.readFileSync(f, 'utf8').match(/html,body\{width:(\d+)px;height:(\d+)px/);
    const p = await b.newPage({ viewport: { width: +m[1], height: +m[2] } });
    await p.goto('file://' + path.resolve(f)); await p.evaluate(() => document.fonts.ready);
    const over = await p.evaluate(() => { const w = document.querySelector('.wrap'); return w ? w.scrollHeight - w.clientHeight : 0; });
    const out = path.join(outDir, path.basename(f).replace('.html', '.png'));
    await p.screenshot({ path: out }); console.log(out, 'overflow', over); if (over > 0) bad++; await p.close();
  }
  await b.close(); if (bad) { console.error(bad + ' slide(s) overflow'); process.exit(2); }
})();
