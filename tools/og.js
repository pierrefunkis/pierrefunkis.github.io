/* Renders tools/og-card.html to a 1200x630 PNG.
 *
 *   npm i -D playwright && node tools/og.js tools/og-card.html og-image.png
 *
 * The card inlines its own web fonts, so this does not depend on Google Fonts
 * being reachable from the machine generating the image.
 */
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const [src, out] = process.argv.slice(2);
  if (!src || !out) {
    console.error('usage: node tools/og.js <card.html> <out.png>');
    process.exit(1);
  }
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 1200, height: 630 },
    deviceScaleFactor: 1,
  });
  await page.goto('file://' + path.resolve(src), { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: out });
  await browser.close();
  console.log('wrote ' + out);
  process.exit(0);
})();
