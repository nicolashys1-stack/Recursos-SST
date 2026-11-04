"""Genera miniaturas.html (una <section> por miniatura) con el estilo de las miniaturas del canal de YouTube.
Uso: python3 build.py && node render.js"""
import pathlib

HEAD = """<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Miniaturas YouTube</title>
<style>
@font-face{font-family:IX;src:url("file:///usr/share/fonts/opentype/inter/InterDisplay-Black.otf");font-weight:900}
@font-face{font-family:IX;src:url("file:///usr/share/fonts/opentype/inter/InterDisplay-Bold.otf");font-weight:700}
@font-face{font-family:IX;src:url("file:///usr/share/fonts/opentype/inter/InterDisplay-Medium.otf");font-weight:500}
*{box-sizing:border-box;margin:0}
body{background:#000}
.s{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:IX,sans-serif;color:#fff;
  background:radial-gradient(circle at 78% 24%,rgba(255,196,0,.22),rgba(255,196,0,0) 42%),#121212}
.s::before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 2px,transparent 2px),
  linear-gradient(90deg,rgba(255,255,255,.035) 2px,transparent 2px);background-size:90px 90px}
.in{position:absolute;left:92px;right:92px;top:0;bottom:0}
.logo{position:absolute;top:250px;display:flex;align-items:center;gap:24px}
.logo i{width:74px;height:74px;border-radius:50%;background:#FFC400;display:grid;place-items:center}
.logo b{display:block;font-weight:900;font-size:36px;letter-spacing:.5px}
.logo small{display:block;font-weight:500;font-size:24px;color:#bbb;margin-top:2px}
.tag{position:absolute;top:470px;background:#FFC400;color:#111;font-weight:900;font-size:34px;letter-spacing:2px;
  padding:12px 22px;border-radius:8px;text-transform:uppercase}
.h{position:absolute;top:590px;font-weight:900;font-size:128px;line-height:1.02;letter-spacing:-2px}
.h y{color:#FFC400}
.sub{margin-top:44px;border-left:8px solid #FFC400;padding-left:22px;font-weight:500;font-size:38px;line-height:1.25;
  color:#ddd;letter-spacing:0}
.box{position:absolute;bottom:300px;left:0;right:0;background:#FFC400;color:#111;border-radius:22px;padding:38px 40px;
  display:flex;align-items:center;gap:32px;box-shadow:0 0 70px rgba(255,196,0,.35)}
.box svg{flex:none}
.box p{font-weight:700;font-size:42px;line-height:1.2}
.box p b{font-weight:900;display:block}
</style></head><body>
<svg width="0" height="0" style="position:absolute">
<symbol id="hat" viewBox="0 0 40 40"><path d="M6 27h28v4H6z M9 26c0-7 4-12 11-12s11 5 11 12z" fill="#111"/>
<rect x="18" y="10" width="4" height="9" fill="#111"/></symbol>
<symbol id="chat" viewBox="0 0 48 44"><path d="M4 4h40v28H20l-10 9v-9H4z" fill="#111"/>
<circle cx="14" cy="18" r="3.4" fill="#FFC400"/><circle cx="24" cy="18" r="3.4" fill="#FFC400"/><circle cx="34" cy="18" r="3.4" fill="#FFC400"/></symbol>
</svg>
"""

# (archivo, etiqueta, titular con <y>resaltado</y>, bajada, pregunta, llamado)
ITEMS = [
    ("01-cv", "Currículum", "Tu título no te consigue <y>laburo</y>", "Tu CV, sí · errores que te dejan afuera",
     "¿Título o experiencia?", "Comentá qué pesa más"),
    ("02-herramientas", "Herramientas", "“Es solo un <y>martillo</y>”", "Revisala antes de usarla · Dec. 351/79",
     "¿Qué herramienta ves peor usada?", "Comentá"),
    ("03-incidente", "Incidentes", "Nadie se lastimó… ¿no <y>pasó nada</y>?", "Qué es un incidente · ISO 45001",
     "¿En tu laburo se reportan?", "Contame en comentarios"),
    ("04-accidente", "Normativa", "¿Qué es un <y>accidente de trabajo</y>?", "Ley 24.557, art. 6",
     "¿Te tocó vivir uno?", "Comentá"),
    ("05-condicion-insegura", "Prevención", "La ves todos los días y ya <y>no la ves</y>", "Condición insegura: detectala antes",
     "¿Cuál ves en tu laburo?", "Comentá"),
    ("06-descuido", "Investigación", "¿“Fue un <y>descuido</y>”?", "Entonces no investigaste el accidente",
     "¿Cómo investigan en tu empresa?", "Contame en comentarios"),
]

html = [HEAD]
for fid, tag, h, sub, q, c in ITEMS:
    html.append(f'''<section class="s" id="m{fid}"><div class="in">
<div class="logo"><i><svg width="46" height="46"><use href="#hat"/></svg></i><div><b>RECURSOS SST</b><small>Nico Silveyra</small></div></div>
<div class="tag">{tag}</div>
<div class="h">{h}<div class="sub">{sub}</div></div>
<div class="box"><svg width="70" height="64"><use href="#chat"/></svg><p>{q}<b>{c}</b></p></div>
</div></section>
''')
html.append("</body></html>\n")
pathlib.Path(__file__).with_name("miniaturas.html").write_text("".join(html), encoding="utf-8")
print("ok")
