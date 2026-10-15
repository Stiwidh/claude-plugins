---
name: analizar-creativos
description: Disecciona los creativos que ROMPIERON de una cuenta de Instagram (los posts outlier) con ojo de anunciante, para entender por qué funcionaron y poder replicar la mecánica. Usa el criterio de gancho y retención de Vega, el virality_predictor de Higgsfield si está conectado y, si la alumna tiene yt-dlp, ffmpeg y whisper, saca el gancho literal de cada reel. Se activa en un análisis de cuentas, tras las métricas, sobre los posts que más rindieron.
---

# Diseccionar los creativos ganadores (ojo de anunciante)

Fase 4. De `metricas-derivadas` salieron los **outliers**: los posts que rompieron. Aquí NO analizas todo el feed, solo esos. La pregunta es: **¿por qué funcionó esta pieza, y escalaría como anuncio?** Eso separa un golpe de suerte de un formato replicable.

Trabaja con las capturas que ya hiciste. Si un outlier es un reel, apóyate en lo que viste de los primeros segundos.

---

## Lente 1: el creativo como si fuera un anuncio

Juzga cada pieza con estas cinco preguntas (las skills `hook-formulas` y `retention-curve` de **`vega`** te dan el detalle si están instaladas):

- **Gancho de 3 segundos**: ¿engancha en los primeros 3 segundos? ¿Cómo (movimiento, texto, cara, pregunta, promesa)?
- **Retención**: ¿da razones para quedarse (bucle abierto, ritmo, cortes)?
- **Claridad**: ¿se entiende sin sonido? ¿El texto en pantalla sostiene el mensaje?
- **Primer fotograma**: ¿frena el scroll?
- **CTA**: ¿pide una acción clara?

Y una más: **¿escalaría como anuncio** en Instagram o solo funciona en orgánico (porque depende de la comunidad que ya tiene, de un momento o de un tema del día)?

---

## Lente 2: el gancho literal (si tienes las herramientas)

Si en tu terminal están **yt-dlp, ffmpeg y whisper**, saca el gancho exacto de los reels outlier en vez de fiarte de la captura. Solo de los outliers (2-5 reels), uno a uno y con pausas:

```bash
yt-dlp -o "%(id)s.%(ext)s" "URL_DEL_REEL"
ffmpeg -i ID.mp4 -t 10 -vn -ac 1 -ar 16000 gancho_ID.wav
whisper gancho_ID.wav --language es --model small --output_format txt
ffmpeg -i ID.mp4 -frames:v 1 primer_fotograma_ID.jpg
```

Con eso tienes **lo que dice en los primeros 10 segundos, palabra por palabra**, y el **primer fotograma** para juzgar si frena el scroll. Si yt-dlp pide sesión, usa `--cookies-from-browser` con el navegador de la cuenta dedicada, nunca con el de tu marca. Si no tienes las herramientas o no estás en una sesión con terminal (la pestaña Code de la app), salta esta lente y dilo.

---

## Lente 3: Higgsfield (nota objetiva del creativo)

Si el conector de **Higgsfield** está conectado, usa **`virality_predictor`** (analiza el vídeo: fuerza del gancho, atención, retención, riesgo de distracción, nota de creativo) sobre los reels outlier que puedas. Es una segunda opinión medible del gancho y la retención, además de tu criterio. Puede gastar créditos de tu cuenta: dilo antes de usarlo en más de un reel.

Si no está conectado, hazlo con tu criterio y dilo.

---

## Cómo diseccionar cada outlier

Para cada post que rompió, saca:
1. **Qué es** (tipo + tema + índice de outlier: cuánto rompió).
2. **El gancho exacto** (primeros segundos o primera línea) y por qué frena el scroll.
3. **El formato y la mecánica** (la estructura repetible, no el tema literal): por ejemplo, "pregunta incómoda en pantalla → contraejemplo → giro → CTA a comentar".
4. **Por qué funcionó** (gancho + retención + tema + momento).
5. **Nota de Higgsfield** si la tienes.

---

## Salida de esta skill

Una **disección por cada creativo ganador**: gancho, formato y mecánica replicable, por qué funcionó y nota. Y un mini **swipe file**: la lista de ganchos y estructuras que se repiten entre los outliers y que podrías reutilizar en tu marca (copiando la mecánica, no el tema). Esto va directo al informe final.
