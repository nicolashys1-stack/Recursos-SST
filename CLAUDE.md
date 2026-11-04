# Recursos SST — Memoria del community manager

Claude actúa como **community manager y diseñador instruccional de SST** de Recursos SST (Nicolás).
Leé este archivo completo al empezar cada sesión y **actualizalo** (sección "Historial" y "Aprendizajes")
cada vez que se publique algo o se aprenda algo nuevo. Hacé commit y push al terminar.

## Cómo trabajamos
- **Proyecto de claude.ai:** ideas, guiones, textos, calendario, respuestas a comentarios, análisis de métricas
  y publicación en Metricool de contenido que ya tenga URL pública.
- **Claude Code (repo nicolashys1-stack/Recursos-SST):** producir videos animados, subirlos al repo y publicarlos.
  La memoria vive en este `CLAUDE.md`; si cambia, actualizar también el conocimiento del Proyecto.
- **Autonomía:** [COMPLETAR: publicar directo cuando lo pida / mostrar el texto final antes de publicar /
  proponer calendario semanal y publicar lo aprobado].

### Si estás en la app de claude.ai (sin acceso al repo)
Es normal: desde la app no hay acceso a GitHub ni a internet desde la computadora. Entonces:
- **Videos:** no renderizar ni subir. O bien (a) preparar guion + textos y pedirle a Nicolás que abra una sesión de
  Claude Code con el repo para producir y publicar, o bien (b) si Nicolás ya tiene el video, pedirle que lo suba a
  **Google Drive** (vinculado a Metricool), compartido como "cualquier persona con el enlace", y usar ese link en `media`.
- **Publicar en Metricool:** sí se puede desde la app con el conector de Metricool, siempre que el video tenga URL pública.
- **Historial y aprendizajes:** no hacer commit. Al final de cada sesión, entregar las filas nuevas de la tabla
  "Historial" y los aprendizajes en un bloque listo para pegar, para que Nicolás los pase a la próxima sesión de Claude Code
  (o los consulte con `getScheduledPosts` en Metricool, que es la fuente real de lo publicado).

## Objetivos y ritmo
- **Objetivo principal:** [COMPLETAR: ej. crecer seguidores / vender checklists de recursos-sst.com.ar].
- **Frecuencia:** [COMPLETAR: ej. 3 videos por semana, lunes, miércoles y viernes 12:40].
- **Pilares de contenido:** conceptos básicos de SST · normativa argentina explicada · charlas de 5 minutos ·
  errores comunes en obra/depósito.

## Marca
- **Nombre:** Recursos SST · Argentina · Seguridad e Higiene / Salud Ocupacional.
- **Web:** recursos-sst.com.ar (checklists y recursos; "link en la bio").
- **Usuario en redes:** @recursos.sst (Instagram, TikTok) · Facebook Page "Recursos SST" · canal de YouTube.
- **Público:** trabajadores de todos los sectores (depósito, obra, industria), técnicos y licenciados en SyH, supervisores.
- **Tono:** español rioplatense (voseo: "frená", "avisá", "seguí", "laburo"), directo, cercano, sin vueltas, técnico pero simple.
  Gancho fuerte en el primer segundo, datos concretos, cierre con CTA.
- **Identidad visual:** fondo azul marino `#0E1A2B`, amarillo seguridad `#FFC400`, naranja `#FF6B1A`, rojo `#E53935`,
  verde `#22C55E`; tipografía Inter Display Black; cintas de peligro amarillo/negro; personaje operario con casco amarillo y chaleco naranja.
- **Rigor:** citar fuente normativa (Ley 19.587, Ley 24.557, Dec. 351/79, Res. SRT, ISO 45001, etc.). No inventar datos ni artículos.

## Metricool (publicación)
- Marca: "Recursos SST Argentina" · **blogId `7809658`** · zona horaria **America/Buenos_Aires**.
- Redes conectadas: Instagram, Facebook, TikTok, YouTube.
- Metricool necesita **URL pública** del video. Método que funciona: commitear el `.mp4` en este repo (es público),
  pushear y usar `https://raw.githubusercontent.com/nicolashys1-stack/Recursos-SST/<branch>/<ruta>.mp4`.
  Metricool lo copia a su servidor, después no depende de GitHub.
- **Una publicación por red** (textos adaptados), con `autoPublish: true`. La fecha no puede ser pasada:
  para "publicar ya" programar +2–3 min.
- Campos obligatorios aprendidos: TikTok exige `tiktokData.title`; YouTube exige `title` y `madeForKids`.
- Instagram y Facebook: `type: "REEL"`, `videoCoverMilliseconds` para portada. YouTube: `type: "short"`, categoría `EDUCATION`.
- Declaración IA: Instagram `isAiGenerated: true` y TikTok `isAigc: true` para videos generados por Claude;
  YouTube `isAiGeneratedContent: false` (solo aplica a contenido realista).
- Después de publicar, verificar con `getScheduledPosts` que el estado sea `PUBLISHED` y reportar los links.

## Fórmula de copy
- **Gancho** (pregunta o mito que se rompe: "¿Un accidente es mala suerte? No.").
- Definición/dato con emojis de viñeta (📌 🔴 🟡 ✅ 🔺).
- **CTA:** 💾 Guardalo para tu charla de 5 minutos · 📤 Compartilo con tu equipo · 👉 Seguí a @recursos.sst ·
  💬 pregunta para comentarios · link en la bio a recursos-sst.com.ar cuando aplique.
- Hashtags base: #SeguridadEHigiene #SeguridadLaboral #SST #HigieneYSeguridad #PrevencionDeRiesgos #SaludOcupacional
  #SeguridadIndustrial #TecnicoEnSeguridad #CharlaDe5Minutos #Argentina + 2–4 del tema. TikTok: + #fyp #parati. YouTube: #Shorts.

## Producción de videos animados
Plantilla en `videos/que-es-un-incidente/`:
- `animacion.html`: animación canvas 1080×1920; cada escena es una función `sX(t, lt)`; `render(t)` determinista.
- `render.js`: Playwright + ffmpeg → mp4 (≈1 min de render para 55 s).
- `audio.py`: música (112 bpm) + SFX sincronizados con numpy.
- Mezcla: `ffmpeg ... -af loudnorm=I=-14:TP=-1.5:LRA=11`.
- Estructura que funciona (≈55 s): gancho (0–4 s) → mini historia con personaje → revelación/sello →
  definición normativa → comparación → dato/pirámide → qué hacer (checklist) → CTA.
- Limitaciones del entorno: no hay TTS (voces bloqueadas por red) → videos con texto en pantalla + música, pensados para ver sin sonido.
  Zonas seguras: contenido clave entre y=220 y y=1500, márgenes 80 px (la UI de TikTok/Reels tapa abajo y a la derecha).

## Producción de carruseles
Plantilla en `carruseles/historia-de-marca/`:
- `placas.html`: cada `<section class="s">` es una placa de 1080×1350 (4:5) en HTML/CSS. Fuente Inter Display local
  (`file:///usr/share/fonts/opentype/inter/InterDisplay-*.otf`). Componentes: `.top` (marca + n/N), `.bot` (@recursos.sst + "Deslizá →"),
  `.tag` (etiqueta de color), `.list/.li` (tarjetas con emoji y borde de color: `.x` rojo, `.ok` verde), `.tape` (cinta de peligro
  en portada y cierre), `<symbol id="op">` (operario SVG con casco amarillo y chaleco naranja), clase `.c` para centrar el contenido vertical.
- `render.js`: Playwright saca una captura de cada section → `placa-01.png`... (tarda segundos).
- `README.md`: tabla placa por placa + textos por red.
- Estructura: portada con gancho + "Deslizá →" → una idea por placa → cierre con CTA (comentá emoji / guardá / seguí / web).
- Revisión: armar una hoja de contacto (PIL, 4×2 miniaturas) y mirarla antes de publicar; centrar verticalmente las placas con poco texto.
- Publicar: commit + push, URLs `raw.githubusercontent.com/.../<branch>/carruseles/<slug>/placa-NN.png` en `media` (en orden),
  Instagram `instagramData.type: "POST"` + `isAiGenerated: true`; Facebook `facebookData.type: "POST"`; TikTok (modo foto) con `tiktokData.title`
  y **JPG** (TikTok rechaza PNG: exportar `placa-NN.jpg` con PIL `convert('RGB').save(..., quality=92)` y usar esas URLs).

## Historial de publicaciones
| Fecha | Tema | Redes | Links |
|---|---|---|---|
| 2026-11-02 10:54 | ¿Qué es un accidente de trabajo? (Ley 24.557, art. 6) | FB, IG, YT · TikTok falló ("Error interno de TikTok") y se re-publicó 11:04 | [IG](https://www.instagram.com/reel/DfPdqeijaFX/) · [FB](https://facebook.com/reel/2427125157822778) · [YT](https://www.youtube.com/shorts/J9nxIJdoO5M) · [TT](https://www.tiktok.com/@recursos.sst/video/7703575306979790100) |
| 2026-11-02 12:40 | ¿Qué es un incidente? (ISO 45001, pirámide de Bird) — video animado propio | IG, FB, TT, YT ✅ | [IG](https://www.instagram.com/reel/DfPprJdjhMm/) · [FB](https://facebook.com/reel/1158300287020885) · [TT](https://www.tiktok.com/@recursos.sst/video/7703599566091750674) · [YT](https://www.youtube.com/shorts/VdAD4CnRhx4) |
| 2026-11-02 21:52 | Historia de marca: "Nadie sale de casa pensando que no vuelve" — carrusel 8 placas | IG, FB ✅ | [IG](https://www.instagram.com/p/DfQo9giCkgy/) · [FB](https://facebook.com/122112359901508879/posts/122112518493508879) |
| 2026-11-03 11:05 | El uso seguro de las herramientas (Dec. 351/79 Cap. 15, Ley 19.587) — video animado propio | IG, FB, TT, YT ✅ | [IG](https://www.instagram.com/reel/DfSDt9klHnm/) · [FB](https://facebook.com/reel/28826604753687001) · [TT](https://www.tiktok.com/@recursos.sst/video/7703946286814317842) · [YT](https://www.youtube.com/shorts/VMGcXLdRGUA) |
| 2026-11-03 11:10 | Uso seguro de herramientas — carrusel 8 placas (Dec. 351/79 Cap. 15) | IG, FB ✅ · TikTok ✅ 15:40 (falló con PNG, re-publicado en JPG) | [IG](https://www.instagram.com/p/DfSEPSTDVv_/) · [FB](https://facebook.com/122112359901508879/posts/122112705819508879) · [TT](https://www.tiktok.com/@recursos.sst/video/7704017064037469448) |
| 2026-11-03 22:01 | CV en Seguridad e Higiene — carrusel polémico 9 placas ("Tu título no te consigue laburo. Tu CV, sí.") | IG, FB, TT ✅ | [IG](https://www.instagram.com/p/DfTPDPwiK22/) · [FB](https://facebook.com/122112359901508879/posts/122112853971508879) · [TT](https://www.tiktok.com/@recursos.sst/video/7704115717309861140) |
| 2026-11-03 22:01 | Reel viral: "Tu título no te consigue laburo. Tu CV, sí." (CV para técnicos/licenciados/ingenieros en SyH) — video animado 42 s | IG, FB, TT, YT ✅ | [IG](https://www.instagram.com/reel/DfTO9mugq2g/) · [FB](https://facebook.com/reel/2223469601933376) · [TT](https://www.tiktok.com/@recursos.sst/video/7704115752478985493) · [YT](https://www.youtube.com/shorts/mWuUlUZpX9A) |

## Ideas de próximos temas (serie de conceptos básicos)
Acto inseguro vs condición insegura · Peligro vs riesgo · Pirámide de Bird en detalle · EPP: cuándo es la última barrera ·
Jerarquía de controles · Cómo reportar un cuasi accidente · Accidente in itinere · Orden y limpieza (5S) ·
Trabajo en altura (verificar norma vigente antes de citarla) · Riesgo eléctrico: 5 reglas de oro · Uso de matafuegos (clases de fuego) · Ergonomía y levantamiento manual de cargas.

## Aprendizajes
- TikTok puede fallar con "Error interno de TikTok": re-programar solo TikTok unos minutos después.
- Si el push a GitHub da 403, el usuario tiene que habilitar la app de Claude en el repo (https://github.com/apps/claude/installations/select_target).
- Carruseles: Metricool acepta PNG de raw.githubusercontent.com en `media` (los copia a static.metricool.com). Una publicación por red. IG tarda varios minutos en "publishing" con 8 placas: es normal.
- Historias de marca: usar un personaje ilustrativo ("un operario") en lugar de inventar biografía o datos; conflicto → quiebre → transformación → resolución.
- Hora: el contenedor NO tiene tzdata → `TZ=America/Buenos_Aires date` devuelve la hora UTC (3 h adelantada). Calcular la hora de BA como
  `date -u -d '-3 hours'` o mirar el `creationDate` que devuelve Metricool. (Pasó: un "publicar ya" quedó 3 h tarde y hubo que reprogramar).
- Sesiones paralelas (videos y carruseles) pushean a la misma rama: antes de pushear hacer `git pull --rebase origin <branch>`
  y releer CLAUDE.md por si la otra sesión agregó aprendizajes.
- Videos: la plantilla se reutiliza bien copiando `animacion.html` y reemplazando solo las funciones de escena (mantener los mismos
  cortes 0/4/12/17/25/32/40.5/48/55 s permite reusar casi todo `audio.py`). Revisar con una hoja de contacto de cuadros (PIL) antes del render final.
- Normativa de herramientas: citar "Dec. 351/79, Cap. 15 (Máquinas y herramientas)" y Ley 19.587 (arts. 8 y 10) sin inventar número de artículo.
- Formato "reel viral/polémico" (ej. `videos/tu-titulo-no-te-consigue-laburo/`): 42 s en vez de 55, 124 bpm, badge "🔥 OPINIÓN IMPOPULAR",
  palabras que entran con golpe de zoom (`punch`), errores con humor reconocible, antes/después concreto (marcar "ejemplos" si hay números
  inventados) y cierre con debate binario en comentarios (🎓 vs 🦺) + "mandáselo al colega que…". Portada en el gancho (s 2,8).
- Coordinación video/carrusel: cuando Nicolás pide el mismo tema a las dos sesiones, salen a la misma hora (pasó con herramientas
  y con el CV a las 22:01). Antes de programar, mirar `getScheduledPosts` del día y, si ya hay otra pieza del tema, separar 2–4 h.
- Miniaturas de YouTube (estilo del canal): `videos/miniaturas-youtube/` (`build.py` → `miniaturas.html`, `node render.js` → JPG 1080×1920).
  Fondo negro #121212 con grilla y brillo amarillo arriba a la derecha · logo casco + "RECURSOS SST / Nico Silveyra" · etiqueta amarilla
  en mayúsculas · titular blanco Inter Display Black con palabra clave en amarillo · bajada con barra amarilla · caja amarilla con globo
  de chat: pregunta + "Comentá". Contenido entre y=250 y y=1620 (YouTube recorta arriba y abajo en la grilla de Shorts).
  Metricool NO cambia miniaturas de videos ya publicados y desde el contenedor no hay API de YouTube ni acceso a i.ytimg.com:
  Nicolás las sube a mano en YouTube Studio. Para videos nuevos, pasar la miniatura en `videoThumbnailUrl` al programar.
- **Límite de Metricool (plan gratuito): 20 publicaciones.** Cada red cuenta como una publicación (1 video en 4 redes = 4).
  Al pasarse, `createScheduledPost` igual responde OK y queda PENDING, pero a la hora falla con ERROR
  "You have reached your Metricool account limit." (pasó el 2026-11-04 con los reels de ISO, IRAM y ART/SRT). Antes de programar
  tandas grandes, preguntar a Nicolás cuántas publicaciones le quedan en el mes.
- Reels de 20 s: motor en `videos/reel20/` (configs JSON → `build.py` → `animacion.html`, `audio.py` y `render.js` compartidos).
- Grupos de Facebook: NO se puede publicar automáticamente (Meta cerró la API de Grupos en 2024; Metricool no lo soporta) y automatizar
  la cuenta personal con un bot viola las reglas de Facebook y arriesga la cuenta y la Página. Alternativa: publicar en la Página con
  Metricool y que Nicolás comparta a los grupos con "Compartir → Compartir en un grupo", con variantes de texto para no repetir.
- TikTok modo foto: solo acepta JPG/JPEG/WEBP ("The 'image/png' type is not allowed"). IG y FB aceptan PNG.
- Coordinar con la sesión de videos: el mismo día salieron video y carrusel del mismo tema; conviene alternar temas o espaciar horarios.
- Formato "viral/polémico" para carruseles: tag 🔥 OPINIÓN IMPOPULAR en portada, placa de identificación (A vs B), autodiagnóstico
  ("¿cuántos tiene tu CV?"), antes/después, una frase que divida (placa roja), checklist guardable, cierre empático y CTA binario
  ("comentá TÍTULO o CV") + etiquetar a un colega. Plantilla: `carruseles/cv-seguridad-e-higiene/` (clases `.vs/.card.bad/.good`).
- Otra vez coincidieron video y carrusel del mismo tema a la misma hora (22:01, CV). Si Nicolás pide el mismo tema a las dos sesiones,
  separar al menos 3–4 h entre video y carrusel, o preguntar.
