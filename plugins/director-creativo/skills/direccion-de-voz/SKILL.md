---
name: direccion-de-voz
description: >-
  Dirigir cómo suena la voz de una pieza: la voz nativa que genera el modelo de vídeo (lo normal) y, cuando toca, el cambio de voz con ElevenLabs o con Higgsfield. Lee el guion como un director de doblaje (quién habla, qué siente, dónde cae el golpe), marca la actuación, propone dos tomas en los momentos clave y, si se pasa por ElevenLabs, da los ajustes con su porqué, verificados contra su documentación. Trigger keywords - la voz suena a robot, suena a locutor, que suene más natural, cámbiale la voz, pon otra voz, que lo diga enfadada, que lo diga susurrando, más emoción, la voz cambia entre clips, no es la misma voz, pronuncia mal el nombre, elevenlabs, ajustes de voz, stability, voice changer, doblaje, voz en off, dirección de voz.
---

<!--
@SHARED_WITH
  Copia adaptada para la comunidad de Protocolo EVA. Tiene gemelas internas: un cambio de doctrina se replica a mano en todas. Registro: SHARED_COMPONENTS.md
-->

# Dirección de voz

**La voz se dirige igual que la cámara: primero qué tiene que sentir quien escucha, luego
cómo se consigue.** Nada de ajustes a ciegas ni de "que suene bien".

En estas piezas la voz es, **por defecto, la nativa del modelo de vídeo** (la que genera
el clip junto con la imagen). A veces se cambia con ElevenLabs, y depende de la pieza. Esta
skill cubre los dos caminos.

Adaptado de la skill "Voice Director" (Skill Library de Ann). Todo lo que es de ElevenLabs
está **comprobado el 2026-09-30** contra su documentación oficial (`elevenlabs.io/docs`); lo
que la skill de origen afirma y la documentación no confirma va marcado como criterio de la
fuente. Detalle en `references/elevenlabs.md`.

---

## 0. Qué camino toca

| Situación | Camino |
|---|---|
| El personaje habla dentro del clip generado | **Voz nativa** del modelo (sección 2) |
| El clip ya está hecho y la voz no convence, o cambia de un clip a otro | **Cambiar la voz** del clip: `voice_change` de Higgsfield o el Voice Changer de ElevenLabs (sección 3) |
| El texto exacto es condición de aceptación (cifra, claim, nombre de marca), o hay narración larga en off | **Voz aparte**: el clip sin voz y la voz sintetizada en ElevenLabs, montadas juntas (sección 3) |

Generar, cambiar o sintetizar voz **gasta**. Nada se lanza sin el coste delante y el OK en el
chat.

## 1. Leer el guion como director de doblaje

Antes de tocar nada, por cada réplica o bloque:

- **Quién habla** y en qué **estado** está (no lo que dice: cómo está).
- **Subtexto:** lo que dice frente a lo que quiere.
- **Intensidad:** dónde sube, dónde baja, dónde está el golpe.
- **Contexto:** reel, anuncio, tutorial, narración. Si no está claro, una sola pregunta.

Y por cada personaje, un **perfil de voz**: edad aproximada, timbre, acento, energía y
textura (cálida, grave, brillante, con aire). Una línea de por qué encaja con el personaje o
la marca. Ese perfil se escribe una vez y se repite **igual** en cada clip donde habla ese
personaje, como la línea de identidad de `continuidad-y-pruebas`.

## 2. Voz nativa del modelo

**FLUX 3:** todo lo que hace falta para que diga exactamente lo que pone el guion (comillas,
hablante, "exactly once", candado de idioma, tabla de reparación) está en `flux3-prompting`.
Aquí no se repite: se lee allí.

**Cómo se dice una línea.** El patrón documentado por Black Forest Labs para FLUX 3 es una
indicación corta de entrega pegada a la línea y a una situación concreta, en vez de adjetivos
de elogio:

```
The mechanic says, "Try it now." Quiet, matter-of-fact delivery.
```

En Seedance, Veo, Kling u Omni se aplica el mismo patrón (quién, qué dice, cómo lo dice, en
qué idioma), pero **es criterio extrapolado**: no hemos consultado una guía de voz propia de
cada modelo. Se prueba con la prueba barata antes del final.

**La misma voz en varios clips no está garantizada.** La propia documentación de FLUX 3 lo
avisa: repetir la descripción de la voz conserva un tipo de voz, no el mismo actor en cada
generación. Rutas, de menos a más trabajo:

1. **Seedance 2.0 con voz de referencia** (`audio_references`, el rol existe, verificado el
   2026-09-30 en el catálogo de Higgsfield). Que mantenga la voz entre clips **no está
   medido** todavía: la primera vez, comparar.
2. **Cambiar la voz después** a una sola voz fija, clip a clip (sección 3).
3. **Voz aparte** para toda la pieza.

**Cada take con voz se escucha entero** antes de darlo por bueno. Mirar el vídeo no vale.

## 3. Cambiar la voz o sintetizarla

### Cambiar la voz de un clip ya generado

- **Higgsfield, `voice_change`:** sustituye la voz hablada de un vídeo por otra, mantiene los
  tiempos y la imagen y vuelve a montar el audio sobre el vídeo (según la descripción de la
  herramienta, consultada el 2026-09-30). La voz destino sale de `list_voices`: voces
  predefinidas o voces propias del espacio de trabajo.
- **ElevenLabs, Voice Changer:** transforma una grabación en otra voz **conservando la
  interpretación** (susurros, risas, llanto, acentos). Modelo recomendado por ElevenLabs:
  `eleven_multilingual_sts_v2`, incluso para inglés. Máximo 5 minutos por segmento. Tiene
  opción de quitar el ruido de fondo (`remove_background_noise`).

La ventaja de cambiar la voz frente a sintetizarla: **la actuación ya está hecha** (ritmo,
pausas, emoción) y solo cambia quién suena.

### Sintetizar la voz aparte (ElevenLabs, texto a voz)

Modelo, ajustes y marcas en `references/elevenlabs.md`. Lo esencial:

- **Eleven v4** es el que ElevenLabs recomienda hoy para contenido. Solo tiene dos ajustes,
  `Stability` y `Similarity`; **no tiene `Style` ni `Speed`, y no admite SSML** (ni pausas con
  `<break>`). La emoción se dirige con **etiquetas de audio** entre corchetes, puntuación y
  mayúsculas.
- **Ojo con el español:** en la lista de idiomas de v4 figura "Spanish (LatAm)";
  Multilingual v2 declara "Spanish (Spain, Mexico)". Para castellano, **probar las dos**
  con la voz elegida antes de producir. Según la documentación, si el idioma generado coincide
  con el de la voz de referencia, v4 conserva su acento.
- **Multilingual v2** admite los cinco ajustes (`stability`, `similarity_boost`, `style`,
  `use_speaker_boost`, `speed`) y pausas con `<break time="1.5s" />` hasta 3 segundos.

## 4. Marcar la actuación

El guion vuelve marcado para la toma. Notación:

```
MARA: [whispers] No tenías que venir aquí.
MARA: [angry] Vete. AHORA.            <- énfasis en mayúsculas, 3 tomas
NARRADOR: Y así... la ciudad se quedó en silencio.
```

- **Etiquetas de audio** (`[whispers]`, `[sighs]`, `[laughs]`, `[curious]`...): funcionan en
  ElevenLabs v3 y v4. En la voz nativa de un modelo de vídeo no son un mecanismo
  documentado: ahí se describe la entrega en inglés, como en la sección 2.
- **Puntos suspensivos** para pausa y peso; **mayúsculas** para énfasis, con cuentagotas.
- **Contexto narrativo** en modelos sin etiquetas (Multilingual v2): "dijo, con la voz
  temblando". ElevenLabs avisa de que el modelo **también lee esa acotación en voz alta**, y
  hay que cortarla en el montaje.
- Cada elección que se note lleva **una línea de por qué**: por qué este susurro, por qué la
  pausa va antes de la revelación y no después.

## 5. Tomas y alternativas

En los picos (la revelación, el chiste, el golpe) se proponen **dos lecturas contrastadas**:
"Toma A: fría y baja (da más miedo). Toma B: explosiva (más catártica)". Se dice cuál probar
primero y qué escuchar para elegir.

## 6. Sonido alrededor

Breve: tono de sala, un sonido que acompañe, música por debajo o corte seco. Es el
condimento, no el plato. Si la música va en el montaje, la voz del clip se pide limpia.

## 7. Qué se entrega

Una **hoja de producción** por personaje y réplica: camino (nativa, cambio o aparte),
modelo, ajustes, marcas, tomas necesarias y el porqué en una línea. Se presenta como
propuesta y no se ejecuta hasta que se aprueba.

## 8. Reglas

- **Explicar sin jerga.** Cada ajuste se cuenta por lo que se va a oír ("más estable: suena
  igual cada vez, pero más plana"), no por el nombre del parámetro.
- **Coherencia por encima de la perfección:** un perfil y unos ajustes fijos por personaje
  para toda la pieza; solo se desvía en los picos marcados.
- **Voz sintética o cambiada hacia público o cliente: aviso de contenido generado con IA**
  (Art. 50), como el resto del contenido sintético.
- **Voz de una persona real** (clonada o como destino de un cambio de voz): solo con su
  permiso.
- **No inventar cifras de ElevenLabs.** Lo que no esté en `references/elevenlabs.md` se
  comprueba en su documentación antes de decirlo.
- Si piden "solo los ajustes, sin explicaciones", se comprime a la hoja de la sección 7.

## Referencias

- `references/elevenlabs.md`: modelos vigentes, ajustes con sus valores por defecto,
  etiquetas de audio, pausas, pronunciación, Voice Changer y problemas típicos, con la fuente
  de cada dato.
