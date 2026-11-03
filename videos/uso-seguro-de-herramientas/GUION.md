# El uso seguro de las herramientas — Video animado (Recursos SST)

**Formato:** vertical 9:16 · 1080×1920 · 30 fps · 55 s · sin locución (texto en pantalla + música y efectos), pensado para verse en silencio.
**Público:** trabajadores de cualquier sector (taller, obra, mantenimiento, depósito).
**Objetivo de aprendizaje:** que el trabajador elija la herramienta correcta, la revise antes de usarla y sepa qué hacer si está dañada.

| Tiempo | Escena | En pantalla | Recurso visual / sonido |
|---|---|---|---|
| 0–4 s | **Gancho** | "ES SOLO UN MARTILLO… ¿QUÉ PODRÍA SALIR MAL?" → tachado: "Mucho. Mirá esto 👇" | Texto que rebota, tachado amarillo · pops |
| 4–12 s | **Historia** | Operario martilla un clavo con el mango flojo; en el golpe fuerte la cabeza sale volando hacia la cámara y raja la pantalla. "¡CRACK!" → "¡Casi me da en la cara!" | Martillazos, chispas, temblor, vidrio rajado · silencio dramático |
| 12–17 s | **Revelación** | "NO fue mala suerte…" · sello "HERRAMIENTA EN MAL ESTADO" · "Era un peligro anunciado. Y se evitaba revisándola antes" | Cintas de peligro, flash · golpe de sello |
| 17–25 s | **Norma** | "Las herramientas deben ser ADECUADAS a la tarea y estar SIN DEFECTOS ni desgastes que las hagan peligrosas." (basado en Dec. 351/79, Cap. 15 · Ley 19.587) · "La empresa: las da y las mantiene" / "Vos: las usás bien, las cuidás y avisás" | Palabra por palabra con resaltado |
| 25–32 s | **Así no / así sí** | Destornillador como palanca → cada una para lo suyo · Llave que no es de la medida → medida justa · En el bolsillo → en la caja o el cinturón · "Ese atajo te puede costar un ojo o una mano." | Tarjetas rojas y verdes enfrentadas |
| 32–40.5 s | **Revisala** | Martillo con lupa: cabeza firme · mango sano · limpia y seca · ¿algo mal? no la uses, avisá | Callouts con tildes |
| 40.5–48 s | **Qué hacer** | Usá la correcta · Revisala antes · Cortá hacia afuera · Guardala en su lugar y la rota, fuera de uso | Checklist con tildes verdes |
| 48–55 s | **CTA** | "La herramienta correcta, BIEN USADA, te devuelve a casa ENTERO." · SEGUÍ a @recursos.sst · Guardalo / Compartilo · pregunta | Botón pulsante, acorde final |

**Fuentes:** Ley 19.587 de Higiene y Seguridad en el Trabajo (arts. 8 y 10: obligaciones de empleador y trabajador); Dec. 351/79, Capítulo 15 "Máquinas y herramientas".

## Archivos
- `uso-seguro-de-herramientas.mp4` — video final · `portada.jpg` — cuadro del segundo 14,5.
- `animacion.html` · `render.js` (`node render.js salida.mp4 30`) · `audio.py` (`python3 audio.py banda.wav`).
- Mezcla: `ffmpeg -i salida.mp4 -i banda.wav -c:v copy -c:a aac -b:a 192k -af loudnorm=I=-14:TP=-1.5:LRA=11 -shortest uso-seguro-de-herramientas.mp4`
