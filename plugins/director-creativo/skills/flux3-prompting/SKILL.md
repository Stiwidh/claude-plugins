---
name: flux3-prompting
description: >-
  Escribir prompts de FLUX 3 (Black Forest Labs) que el modelo obedece: vídeo hasta 20 s con audio nativo, y sobre todo diálogo LITERAL que respeta el guion palabra por palabra en vez de inventarse las conversaciones. Cubre las cinco cerraduras del diálogo (comillas, hablante, exactly-once, candado de idioma, sin texto en pantalla), el molde de prompt, vocabulario oficial de cámara y luz, multiplano con HARD CUT, keyframes, continuación, parámetros y coste. Trigger keywords - flux 3, flux3, prompt para flux, se inventa los diálogos, no respeta el guion, el personaje dice otra cosa, la frase sale escrita en pantalla, lo dice en inglés, vídeo con voz, audio nativo, lipsync flux, diálogo literal, guion a prompt, hard cut, keyframes flux, continuar clip, cuánto cuesta un vídeo flux.
---

<!--
@SHARED_WITH
  Copia adaptada para la comunidad de Protocolo EVA. Tiene gemelas internas: un cambio de doctrina se replica a mano en todas. Registro: SHARED_COMPONENTS.md
-->

# /director-creativo:flux3-prompting

FLUX 3 genera imagen, vídeo y **audio en la misma pasada**. Eso es lo que lo hace potente y
lo que rompe los guiones: si no lo atas, se inventa lo que se dice.

Esta skill es la doctrina para escribirle. Todo verificado contra la documentación oficial
de Black Forest Labs el 2026-09-09.

---

## Lo que hay que saber de memoria

**Qué es.** Un solo modelo multimodal. Vídeo de 5 a 20 segundos, con voz, efectos y ambiente
sincronizados, en 720p o 1080p, en ocho relaciones de aspecto. Cuatro modos: texto a vídeo,
imagen a vídeo con keyframes, continuación de un clip, y repetición de un borrador.

**Dónde se ejecuta.** En Higgsfield, modelo `flux_3_video` (el camino normal), o por la API
de BFL cuando hacen falta borradores baratos, keyframes con segundo exacto o continuación.

**Cuánto cuesta.** 0,17 $ por segundo en 720p. Un plano de 8 segundos son 1,36 $. Son precios
orientativos de la API de BFL, verificados el 2026-09-09: pueden haber cambiado, y en Higgsfield
manda el coste que te enseñe tu cuenta. Un lote de tres generaciones o más lleva presupuesto y
visto bueno antes.

---

## 1. La regla que no se negocia: el guion es literal

**El diálogo que te dan es dato, no material de partida.**

Cuando recibas un guion con líneas habladas, esas líneas se copian al prompt **carácter a
carácter**. No se reescriben, no se traducen, no se acortan, no se les arregla la puntuación,
no se fusionan y no se les añade nada. Ni un saludo, ni un cierre.

Si la línea no cabe en la duración, **no la recortes: dilo**. Se sube la duración o se parte
la escena, y esa decisión es de quien escribió el guion.

Esta regla existe porque el fallo empieza aquí, antes de que el modelo intervenga.

---

## 2. Las cinco cerraduras del diálogo

Una línea hablada necesita las cinco. Falta una y el modelo improvisa.

| # | Cerradura | Cómo se escribe |
|---|---|---|
| 1 | **Comillas** | La línea exacta entre comillas. Lo que va fuera es descripción, y una descripción se parafrasea |
| 2 | **Hablante** | Persona visible descrita (edad, un rasgo, ropa) **o** la etiqueta `voiceover`. Sin dueño, la frase sale escrita en pantalla |
| 3 | **Una sola vez** | `exactly once, the complete sentence, with no repetition and no other words in the entire shot` |
| 4 | **Candado de idioma** | `She speaks entirely in Spanish, every word in Spanish, native Castilian accent and cadence, no English words at all` |
| 5 | **Sin rótulos** | El prompt termina en `No on-screen text, no subtitles`, y el audio lleva `no other speech` |

La tercera es la que corta el diálogo inventado. La cuarta evita que traduzca tu línea al
inglés y hable esa.

### Molde listo para copiar

```
[Duración y plano]. [Hablante: edad, rasgo, ropa, dónde está y qué hace]. [Luz].

[Verbo + cómo lo dice] on camera exactly once, the complete sentence, with no repetition
and no other words in the entire shot: "<LÍNEA LITERAL DEL GUION>"

She speaks entirely in Spanish, every word in Spanish, native Castilian accent and cadence,
no English words at all.

Audio: [su voz y el micro], [una o dos capas de ambiente con fuente concreta].
No music, no other speech. No on-screen text, no subtitles.
```

### El límite honesto

BFL lo dice sin adornos: la redacción exacta es **un objetivo dirigible, no un control
garantizado**, y reserva para post-producción "guaranteed wording or speaker identity".

Cuando el texto exacto sea condición de aceptación del cliente (una cifra, un claim, el
nombre de una marca), la ruta no es insistir con el prompt: se genera el plano **sin voz**
(`generate_audio: false`), se graba la voz aparte y se monta. Y todo take con diálogo **se
escucha entero** antes de darlo por bueno.

Detalle completo, conversaciones de varios personajes y tabla de reparación:
[references/dialogo-literal.md](references/dialogo-literal.md).

---

## 3. Cómo se escribe el resto del prompt

**Prosa, dirigiendo una escena.** No listas de palabras clave, no estilo de pie de foto.
Como se lo contarías a un compañero en voz alta.

**Un prompt que nombra de cinco a diez momentos concretos gana a uno con cuarenta
adjetivos.** Un adjetivo más sobre "luz cálida de tarde" no aporta; un momento nuevo como
"la oreja del gato se mueve cuando retumba el trueno" casi siempre sí.

**Si no nombras la cámara, se mueve sola.** Para que un plano esté quieto hay que pedirlo:
`the camera holds locked`.

**Presupuesto por plano:** una acción del sujeto y un movimiento de cámara. Si el encargo
pide varias acciones seguidas, varios sitios o varias réplicas completas de diálogo, el
encargo se repara, no se genera.

**Duración por momentos:** un momento son 5 s, principio y final son 7-10 s, tres cortes con
aire son 12-18 s.

Los cuatro formatos de prompt, el esquema largo de seis bloques y las capas de audio:
[references/molde-prompt.md](references/molde-prompt.md).

Los 119 términos oficiales de encuadre, ángulo, movimiento, óptica, luz y estilo, más los
conceptos que aguantan y los que hay que sacar de la generación:
[references/camara-luz-estilo.md](references/camara-luz-estilo.md).

---

## 4. Varios planos

Dentro de una generación, con `HARD CUT`, hasta dos o tres planos. Los planos seguidos
tienen que **contrastar fuerte** (la escala es el contraste más potente) y llevar **una sola
idea de audio** cruzándolos, o el corte se lee como zapeo.

A partir de ahí, un plano por generación y se montan. Lo que une la pieza es **una biblia
del mundo copiada palabra por palabra** en todos los prompts, no parafraseada, más un motivo
de audio nombrado en cada plano.

Keyframes, continuación y cadenas largas:
[references/multiplano-continuidad.md](references/multiplano-continuidad.md).

---

## 5. Ejecución

Parámetros, modos, estados de la API, la trampa de `result.samples` como lista, límites de
concurrencia y la tabla de precios:
[references/api-parametros.md](references/api-parametros.md).

---

## 6. Imagen y texto

FLUX 3 imagen está en acceso anticipado; el modelo de imagen en producción es FLUX.2.
Componentes del prompt, ausencia de prompt negativo y cómo se pide texto legible dentro de
una imagen: [references/imagen-y-texto.md](references/imagen-y-texto.md).

Regla corta que se cruza con el vídeo: **en imagen el texto sale bien, en vídeo la
tipografía crítica se pone en montaje.** Una miniatura con texto se genera como imagen.

---

## 7. Antes de dar por buena una generación

- [ ] La línea del prompt es idéntica a la del guion
- [ ] Las cinco cerraduras están puestas
- [ ] Una sola réplica por plano (o dos cortas, atribuidas por rasgo visible)
- [ ] La duración deja margen para decir la línea entera
- [ ] El take se ha **escuchado** entero, no solo visto
- [ ] Si hay presentador o voz de IA hacia público, la pieza lleva el aviso de contenido
      generado con IA (Art. 50 del Reglamento de IA de la UE)
