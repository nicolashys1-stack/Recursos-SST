# ¿Qué es un incidente? — Video animado (Recursos SST)

**Formato:** vertical 9:16 · 1080×1920 · 30 fps · 55 s · sin locución (texto en pantalla + música y efectos), pensado para verse en silencio.
**Público:** trabajadores de cualquier sector (operarios, depósito, obra, industria).
**Objetivo de aprendizaje:** que el trabajador sepa definir un incidente, distinguir accidente de cuasi accidente y saber qué hacer cuando ocurre uno.

| Tiempo | Escena | En pantalla | Recurso visual / sonido |
|---|---|---|---|
| 0–4 s | **Gancho** | "NADIE SE LASTIMÓ… ¿ENTONCES NO PASÓ NADA?" → tachado: "Error. Mirá esto 👇" | Texto que rebota, tachado amarillo · pops |
| 4–12 s | **Historia** | Operario camina por el depósito sin mirar arriba; una caja "FRÁGIL" se tambalea y cae justo detrás. "¡PUM!" → "¡Uf… zafé!" | Temblor de cámara, polvo · crujido, silbido de caída, golpe, silencio dramático |
| 12–17 s | **Revelación** | Sello rojo: "ES UN INCIDENTE" · "Aunque nadie se haya lastimado" · "Es una ALERTA que no podés ignorar" | Cintas de peligro animadas, flash · golpe de sello |
| 17–25 s | **Definición** | "Todo suceso que ocurre por o durante el trabajo y que PODRÍA causar o CAUSA lesiones o daños a la salud." (basado en ISO 45001:2018, 3.35) · chips "Con lesión / Sin lesión: los dos cuentan" | Palabra por palabra con resaltado |
| 25–32 s | **Tipos** | ACCIDENTE (hay lesión) vs CUASI ACCIDENTE (sin lesión… esta vez) · "Los dos son INCIDENTES. Los dos se REPORTAN." | Tarjetas que entran desde los lados con personaje |
| 32–40.5 s | **Pirámide de Bird** | 600 incidentes sin lesión · 30 daños materiales · 10 lesiones leves · 1 lesión grave · "Si atacás la BASE, evitás la PUNTA" (F. E. Bird, 1969) | Pirámide que se construye con contadores |
| 40.5–48 s | **Qué hacer** | 1. Frená la tarea y asegurá la zona · 2. Avisá a tu supervisor o al servicio de SyH · 3. Reportalo aunque nadie se lastime · 4. Buscá la causa y corregila | Checklist con tildes verdes |
| 48–55 s | **CTA** | "Reportar un incidente HOY evita un ACCIDENTE MAÑANA." · botón "SEGUÍ a @recursos.sst" · Guardalo / Compartilo · pregunta para comentarios | Botón pulsante, acorde final |

## Archivos
- `que-es-un-incidente.mp4` — video final.
- `portada.jpg` — portada (cuadro del segundo 14,5).
- `animacion.html` — animación en canvas; `render(t)` dibuja el cuadro del segundo `t`.
- `render.js` — renderiza la animación con Playwright + ffmpeg: `node render.js salida.mp4 30`.
- `audio.py` — genera música y efectos sincronizados: `python3 audio.py banda.wav`.
- Mezcla final: `ffmpeg -i salida.mp4 -i banda.wav -c:v copy -c:a aac -b:a 192k -af loudnorm=I=-14:TP=-1.5:LRA=11 -shortest que-es-un-incidente.mp4`
- `PUBLICACIONES.md` — textos por red social.
