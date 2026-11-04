# Motor de reels de 20 s

Formato corto (20 s, 124 bpm) para temas de "qué es y por qué importa". Escenas fijas:
gancho (0–2,6 s) → qué es: tarjeta de definición o dos columnas "vs" (2,6–7,6 s) → 3 claves con tildes (7,6–15 s) → remate + pregunta + CTA (15–20 s).

- Contenido de cada reel: `configs/<slug>.json` (badge, hook, hookBox, what, keys, end, q).
- `python3 build.py <slug>` → escribe `videos/<slug>/animacion.html` (usa las utilidades de `que-es-un-incidente/animacion.html` + `engine.js`).
- `python3 audio.py banda.wav` → banda sonora de 20 s, sincronizada con los cortes.
- `node render.js salida.mp4 30 ../<slug>` → video sin audio; mezcla con
  `ffmpeg -i salida.mp4 -i banda.wav -c:v copy -c:a aac -b:a 192k -af loudnorm=I=-14:TP=-1.5:LRA=11 -shortest <slug>.mp4`.
- Reels hechos: `normas-iso`, `normas-iram`, `art-y-srt`. Textos de redes en `<slug>/PUBLICACIONES.md`.
