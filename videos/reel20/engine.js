// ======================================================================
//  Motor de reels de 20 s (Recursos SST). Se configura con window.CFG.
//  Escenas: gancho (0–2.6) → qué es (2.6–7.6) → 3 claves (7.6–15) → remate + CTA (15–20)
// ======================================================================
const SC = [
  { a: 0, b: 2.6, f: sHook },
  { a: 2.6, b: 7.6, f: sWhat },
  { a: 7.6, b: 15, f: sKeys },
  { a: 15, b: 20, f: sEnd },
];
const punch = (lt, at) => lt < at ? 0 : 1 + .25 * Math.exp(-(lt - at) * 9) * Math.cos((lt - at) * 20);
const col = c => C[c] || c;
function check(x, y, s, alpha = 1) {
  withT(x, y, s, 0, () => { ctx.fillStyle = C.green; ctx.beginPath(); ctx.arc(0, 0, 40, 0, 7); ctx.fill();
    ctx.strokeStyle = '#fff'; ctx.lineWidth = 10; ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(-17, 2); ctx.lineTo(-4, 15); ctx.lineTo(19, -12); ctx.stroke(); }, alpha);
}
function badge(lt, str, y = 300, bg = C.red) {
  const k = popIn(lt, 0, .35);
  withT(540, y, k, -.03, () => {
    ctx.font = F(900, 46); const w = ctx.measureText(str).width + 90;
    ctx.fillStyle = bg; rr(-w / 2, -48, w, 96, 48); ctx.fill();
    text(str, 0, 4, { size: 46, color: C.white });
  }, clamp(k));
}

// 1) GANCHO
function sHook(t, lt) {
  bgGradient('#0E1A2B', '#1B3354'); dotsGrid(t);
  burst(540, 860, 330, 460, 14, t * .5, 'rgba(255,196,0,.12)');
  badge(lt, CFG.badge);
  CFG.hook.forEach(([w, s, c], i) => { const at = .2 + i * .35;
    if (lt >= at) withT(540, 600 + i * 165, punch(lt, at), 0, () => text(w, 0, 0, { size: s, color: col(c), shadow: true })); });
  const at = .3 + CFG.hook.length * .35;
  if (lt > at) {
    const k = popIn(lt, at, .35);
    withT(540, 600 + CFG.hook.length * 165 + 90, k, -.04, () => {
      ctx.font = F(900, 80); const w = ctx.measureText(CFG.hookBox).width + 120;
      ctx.fillStyle = C.yellow; rr(-w / 2, -80, w, 160, 40); ctx.fill();
      text(CFG.hookBox, 0, 6, { size: 80, color: C.ink });
    }, clamp(k));
  }
}

// 2) QUÉ ES (tarjeta con definición, o dos columnas "vs")
function sWhat(t, lt) {
  bgGradient('#0E1A2B', '#13243B'); dotsGrid(t, .06);
  const W2 = CFG.what;
  const kT = popIn(lt, .05, .35);
  withT(540, 300, kT, 0, () => { ctx.font = F(900, 60); const w = ctx.measureText(W2.title).width + 110;
    ctx.fillStyle = C.yellow; rr(-w / 2, -66, w, 132, 66); ctx.fill(); text(W2.title, 0, 4, { size: 60, color: C.ink }); }, clamp(kT));
  if (W2.vs) {
    W2.vs.forEach((c, i) => {
      const k = easeOut(prog(lt, .4 + i * .5, .8 + i * .5)), x = 70 + i * 480;
      ctx.save(); ctx.globalAlpha = k; ctx.translate((1 - k) * (i ? 300 : -300), 0);
      ctx.fillStyle = col(c.color); rr(x, 440, 460, 900, 40); ctx.fill();
      const tc = col(c.text || 'white');
      text(c.name, x + 230, 560, { size: 120, color: tc });
      c.lines.forEach((ln, j) => text(ln, x + 230, 700 + j * 62, { size: 44, weight: j < 2 ? 900 : 700, color: tc }));
      ctx.restore();
    });
    const kv = popIn(lt, 1.4, .35);
    withT(540, 1250, kv, 0, () => { burst(0, 0, 60, 95, 10, lt, C.white); text('≠', 0, 6, { size: 80, color: C.ink }); }, clamp(kv));
  } else {
    const kc = easeOut(prog(lt, .3, .7));
    ctx.save(); ctx.globalAlpha = kc; ctx.translate(0, (1 - kc) * 80);
    ctx.fillStyle = C.white; rr(80, 450, 920, 760, 44); ctx.fill();
    ctx.fillStyle = C.orange; rr(80, 450, 22, 760, 11); ctx.fill();
    ctx.restore();
    const kn = popIn(lt, .6, .4);
    withT(550, 590, kn, 0, () => text(W2.name, 0, 0, { size: W2.nameSize || 110, color: C.orange }), clamp(kn));
    W2.lines.forEach((ln, i) => {
      const k = easeOut(prog(lt, 1.1 + i * .35, 1.45 + i * .35));
      ctx.save(); ctx.translate(0, (1 - k) * 30); richLine(ln.map(([s, c]) => [s, col(c)]), 550, 740 + i * 95, 60, 900, k); ctx.restore();
    });
    text(W2.src, 540, 1150, { size: 34, weight: 500, color: C.steel, alpha: prog(lt, 2.6, 3) });
  }
  if (W2.foot) text(W2.foot, 540, 1420, { size: 46, weight: 700, color: C.yellow, alpha: prog(lt, 3.2, 3.6) });
}

// 3) TRES CLAVES
function sKeys(t, lt) {
  bgGradient('#0E1A2B', '#16304F');
  hazardStripe(200, 36, lt * 120, .9);
  text(CFG.keys.title, 540, 340, { size: 70, color: C.yellow, alpha: prog(lt, 0, .3) });
  CFG.keys.items.forEach(([ic, a, b], i) => {
    const d = .5 + i * 1.9, k = easeOut(prog(lt, d, d + .35));
    if (k <= 0) return;
    const y = 450 + i * 300;
    ctx.save(); ctx.globalAlpha = k; ctx.translate((1 - k) * 220, 0);
    ctx.fillStyle = C.white; rr(80, y, 920, 250, 40); ctx.fill();
    ctx.fillStyle = C.navy; ctx.beginPath(); ctx.arc(200, y + 125, 80, 0, 7); ctx.fill();
    text(ic, 200, y + 130, { size: 80 });
    text(a, 320, y + 95, { size: 56, color: C.ink, align: 'left' });
    text(b, 320, y + 170, { size: 38, weight: 500, color: C.steel, align: 'left' });
    ctx.restore();
    check(930, y + 125, popIn(lt, d + .35, .3), clamp(popIn(lt, d + .35, .3)));
  });
  if (CFG.keys.foot) text(CFG.keys.foot, 540, 1420, { size: 36, weight: 700, color: C.gray, alpha: prog(lt, 6.4, 6.8) });
}

// 4) REMATE + CTA
function sEnd(t, lt) {
  bgGradient('#1B3354', '#0E1A2B');
  burst(540, 600, 340, 500, 16, lt * .3, 'rgba(255,196,0,.10)');
  CFG.end.forEach(([w, s, c], i) => { const at = .1 + i * .3;
    if (lt >= at) withT(540, 420 + i * 140, punch(lt, at), 0, () => text(w, 0, 0, { size: s, color: col(c), shadow: true })); });
  const yq = 420 + CFG.end.length * 140 + 40;
  const kq = popIn(lt, 1.3, .35);
  withT(540, yq, kq, -.02, () => {
    ctx.fillStyle = C.white; rr(-460, -70, 920, 140, 34); ctx.fill();
    ctx.font = F(900, 46); const qs = Math.min(46, 46 * 840 / ctx.measureText(CFG.q).width);
    text(CFG.q, 0, 4, { size: qs, color: C.ink });
  }, clamp(kq));
  const k2 = popIn(lt, 2.1, .4), pulse = 1 + Math.sin(lt * 6) * .035 * clamp(lt - 2.5);
  withT(540, yq + 200, k2 * pulse, 0, () => {
    ctx.fillStyle = C.yellow; rr(-400, -80, 800, 160, 80); ctx.fill();
    text('SEGUÍ a @recursos.sst', 0, 4, { size: 58, color: C.ink });
  }, clamp(k2));
  text('💾 Guardalo · 📤 Compartilo con tu equipo', 540, yq + 360, { size: 42, weight: 700, alpha: prog(lt, 2.8, 3.2) });
}
