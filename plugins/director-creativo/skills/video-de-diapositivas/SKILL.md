---
name: video-de-diapositivas
description: >-
  Convertir un documento, un PDF, un guion o un temario en un vídeo de diapositivas narrado (MP4 1080p listo para YouTube, la web o una formación), con una idea por diapositiva y la voz marcando el ritmo. Trae el script que lo monta en local con Pillow y ffmpeg, en Windows y en Mac. Trigger keywords - pásame este PDF a vídeo, un vídeo explicativo con diapositivas, vídeo de formación, vídeo de onboarding, vídeo para explicar el servicio, convierte esta presentación en vídeo, vídeo con diapositivas y voz, temario a vídeo, tutorial con diapositivas, vídeo de bienvenida para clientes, módulo de curso en vídeo.
---

<!--
@SHARED_WITH
  Copia adaptada para la comunidad de Protocolo EVA. Tiene gemelas internas: un cambio de doctrina se replica a mano en todas. Registro: SHARED_COMPONENTS.md
-->

# Vídeo de diapositivas

Para explicar, no para impresionar: presentaciones de servicio, formación, onboarding de
clientes, módulos de curso o un PDF que nadie se va a leer. Diapositivas limpias, una voz que
lo cuenta y un MP4 que se sube tal cual. Sin generación con IA de imagen ni vídeo: cero
créditos.

Adaptado de la skill "Slide Video" (Skill Library de Ann). El script que usaba no venía en el
paquete; `scripts/build_video.py` está escrito de nuevo y probado.

---

## 1. El oficio: cómo se escribe un deck que se entiende

- **Una idea por diapositiva.** Si hay dos, son dos diapositivas.
- **Las viñetas son para el ojo; la narración, para el oído.** La voz no lee las viñetas:
  las explica como se lo contarías a alguien sentado al lado. Las viñetas son las palabras
  clave que quedan en pantalla.
- **Máximo 4 viñetas, de unas 8 palabras cada una.** Más que eso no se lee mientras se
  escucha. El script avisa si una diapositiva se pasa o si el texto no cabe.
- **El ritmo lo marca la narración.** Cada diapositiva dura lo que dura su voz más un respiro;
  una o dos frases por diapositiva es lo normal.
- **Título al principio, separadores de sección cuando cambia el tema, y un cierre con el
  siguiente paso** (qué hacer ahora, a quién escribir, dónde reservar).
- **Si viene de un PDF o un documento:** leerlo entero, sacar la estructura (secciones, ideas),
  y convertir cada idea en una diapositiva con su narración. No copiar párrafos a la pantalla.

## 2. El formato del deck (`deck.md`)

```markdown
---
title: Cómo trabajamos           # opcional
theme: sobrio                    # sobrio, claro o noche
accent: 8b5cf6                   # color de acento de la marca, en hex
footer: tumarca.com               # texto pequeño abajo a la izquierda
---

# Cómo trabajamos                <- el primer "# " es la portada
Del primer contacto a la entrega <- línea normal bajo un "# " = subtítulo
> Te cuento en dos minutos cómo trabajamos.   <- "> " = lo que dice la voz

## Semana uno: el diagnóstico    <- "## " = diapositiva de contenido
- Entrevista con tu equipo       <- "- " = viñeta
- Mapa de lo que ya tienes
image: capturas/diagnostico.png  <- opcional: imagen a la derecha
audio: voz/02.mp3                <- opcional: la voz de esta diapositiva
duration: 6                      <- opcional: segundos si no hay voz
> La primera semana solo escuchamos y medimos.

# Siguiente paso                 <- un "# " más adelante = separador de sección
> Si te encaja, reserva una llamada en la web.
```

Las rutas de `image:` y `audio:` son relativas al deck. Hay un ejemplo completo en
`ejemplo/deck.md`.

## 3. La voz

Por cada diapositiva, en este orden:

1. **`audio:` en el deck.** La voz que ya existe: una grabación propia, una voz de ElevenLabs,
   la que sea. Es la opción buena para piezas que salen fuera.
2. **edge-tts, si está instalado** (voces gratuitas de Microsoft; necesita internet). El script
   no lo instala: si se quiere, `python -m pip install edge-tts`. Voz por defecto
   `es-ES-AlvaroNeural`; otra con `--voice` (lista: `edge-tts --list-voices`).
3. **Sin voz.** Cada diapositiva dura `duration:` o `--seconds-per-slide` (5 s por defecto).
   El vídeo lleva igualmente una pista de audio en silencio, para que las plataformas no se
   quejen.

**Aviso de IA (Art. 50):** si la voz es sintética (edge-tts, ElevenLabs) y el vídeo va a
público o a clientes, lleva el rótulo "Contenido generado con IA", por ejemplo en el `footer`
o en la portada.

## 4. Cómo se ejecuta

Necesitas tres cosas instaladas: **Python 3**, **ffmpeg** y la librería **Pillow**
(`python -m pip install pillow`). Si te falta Pillow o ffmpeg, el script te lo dice con el
comando para instalarlos.

**Windows** (PowerShell):
1. Python 3: descárgalo de python.org y, al instalar, marca "Add python.exe to PATH".
2. ffmpeg: `winget install Gyan.FFmpeg`. Cierra y vuelve a abrir PowerShell para que lo encuentre.
3. Ejecuta:
```powershell
python <ruta de la skill>\scripts\build_video.py deck.md -o salida.mp4 --accent 8b5cf6 --srt
```

**Mac** (Terminal, con Homebrew instalado: brew.sh):
1. Python 3 y ffmpeg: `brew install python ffmpeg`. Pillow: `python3 -m pip install pillow`. Si
   el Mac responde "externally-managed-environment", pídele a Claude que te cree un entorno
   virtual (venv) para esto.
2. Ejecuta:
```bash
python3 <ruta de la skill>/scripts/build_video.py deck.md -o salida.mp4 --accent 8b5cf6 --srt
```

Opciones útiles:

| Opción | Para qué |
|---|---|
| `--theme sobrio / claro / noche` | tema base (por defecto, sobrio: gris carbón) |
| `--accent`, `--bg`, `--fg`, `--muted` | colores de la marca en hex; mandan sobre el tema |
| `--footer "texto"` | marca, web o el aviso de IA abajo a la izquierda |
| `--no-motion` | quita el zoom lento sobre cada diapositiva |
| `--resolution 1080x1920` | vertical para Reels o Shorts (por defecto 1920x1080) |
| `--srt` | subtítulos `.srt` de la narración, junto al MP4 |
| `--no-audio` | todo sin voz, con tiempo fijo |
| `--font`, `--font-bold` | otra tipografía `.ttf` (la de la marca) |
| `--keep-temp` | conserva los PNG de cada diapositiva para revisarlos |

Salida: MP4 H.264 + AAC, 1080p a 30 fps, listo para subir. Tarda unos segundos por
diapositiva.

## 5. Antes de entregar

- **Mirar 2 o 3 fotogramas** (portada, una de contenido, la última): que el texto se lee, que
  no se corta y que las tildes salen bien. Con `--keep-temp` se ven los PNG directamente.
- Comprobar que la duración total cuadra con la narración (el script la imprime por
  diapositiva).
- Si el script avisa de que el texto no cabe o de que hay más de 4 viñetas, se arregla el deck,
  no se entrega así.

## Qué NO hace

- No genera imágenes ni vídeo con IA: las imágenes se ponen con `image:` (capturas, fotos,
  diagramas que ya existan).
- No usa servicios de pago. La única llamada de red es edge-tts, y solo si está instalado.
