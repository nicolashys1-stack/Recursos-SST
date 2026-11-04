// Renderiza cada <section class="s"> de placas.html a PNG 1080x1350.
// Uso: node render.js
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + path.resolve(__dirname, 'placas.html')); await p.evaluate(() => document.fonts.ready);
  const ids = await p.$$eval('section.s', s => s.map(e => e.id));
  for (const [i, id] of ids.entries()) {
    await p.locator('#' + id).screenshot({ path: path.resolve(__dirname, `placa-${String(i + 1).padStart(2, '0')}.png`) });
  }
  await b.close(); console.log('ok', ids.length);
})();
