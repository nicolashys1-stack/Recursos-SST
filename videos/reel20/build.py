"""Arma videos/<slug>/animacion.html a partir de la plantilla (utilidades), engine.js y la config del reel.
Uso: python3 build.py <slug>  (config en configs/<slug>.json)"""
import json, pathlib, sys
here = pathlib.Path(__file__).parent
slug = sys.argv[1]
cfg = json.loads((here / 'configs' / f'{slug}.json').read_text(encoding='utf-8'))
src = (here.parent / 'que-es-un-incidente' / 'animacion.html').read_text(encoding='utf-8')
src = src.replace('<title>Qué es un incidente</title>', f"<title>{cfg['title']}</title>")
src = src.replace('//  "¿Qué es un incidente?" — Recursos SST', f'//  "{cfg["title"]}" — Recursos SST (reel 20 s)')
src = src.replace('DURATION = 55', 'DURATION = 20')
a = src.index('// ---------- estantería y caja ----------'); b = src.index('// ---------- marca persistente ----------')
c = src.index('// ======================================================================\n//  ESCENAS'); d = src.index('// ---------- transición entre escenas ----------')
engine = (here / 'engine.js').read_text(encoding='utf-8')
src = src[:a] + src[b:c] + 'const CFG = ' + json.dumps(cfg, ensure_ascii=False) + ';\n' + engine + '\n' + src[d:]
out = here.parent / slug; out.mkdir(exist_ok=True)
(out / 'animacion.html').write_text(src, encoding='utf-8')
print('ok', out / 'animacion.html')
