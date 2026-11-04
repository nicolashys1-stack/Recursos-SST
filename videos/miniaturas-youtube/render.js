// Captura cada <section> de miniaturas.html como JPG 1080×1920. Uso: node render.js
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.resolve(__dirname, 'miniaturas.html'));
  await p.evaluate(() => document.fonts.ready);
  for (const s of await p.$$('section.s')) {
    const id = (await s.getAttribute('id')).slice(1);
    await s.screenshot({ path: path.join(__dirname, `miniatura-${id}.jpg`), type: 'jpeg', quality: 92 });
    console.log(id);
  }
  await b.close();
})();
