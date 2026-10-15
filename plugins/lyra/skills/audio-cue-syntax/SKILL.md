---
name: audio-cue-syntax
description: |
  Sintaxis canónica de audio para video por plataforma: Veo 3.1 (diálogo entre comillas + SFX + Ambient noise, audio siempre activo), Kling 3.0 (cada línea de diálogo con su personaje y tono + voz atada al element), Seedance 2.5 (audio y vídeo juntos + hasta 10 audios de referencia), Runway Gen-4.5 (Director Mode con audio per-scene). Aplicar siempre que el JSON v2.0 tiene `audio.required = true`. Audio bien estructurado diferencia un video amateur de uno profesional.
user-invocable: true
argument-hint: "<platform>"
allowed-tools:
  - Read
---

# Skill: Audio Cue Syntax

> **Corrección 2026-10-15.** Esta skill describía Kling 3.0 con la sintaxis `[AUDIO: ...]`, `voice_clone_ref` y `cfg_scale`, y Seedance 2.5 con "lip-sync por fonemas" y variantes Fast/Standard/Pro: eran datos de Kling 2.6 y Seedance 2.0 con la etiqueta cambiada. También tenía una fila "Veo 3.1 (T3) Limitado" que contradecía la de Tier 1. Ahora: **Veo 3.1** según la guía oficial de Google, **Kling 3.0** según sus guías oficiales y **Seedance 2.5** según su página oficial y la documentación de BytePlus ModelArk. Lo no confirmado se dice.

## Capas de audio en video pro

Un video con audio nativo (Veo 3.1, Kling 3.0, Seedance 2.5, Runway Gen-4.5) tiene 4 capas que deben describirse SEPARADAS:

1. **Dialog**: palabras habladas (diálogo de personajes o narrator)
2. **SFX** (Sound Effects): efectos puntuales sincronizados (un golpe, un click, una explosión)
3. **Ambient**: ruido de fondo continuo (cafe noise, lluvia, tráfico)
4. **Music**: música de fondo (mood, género, volumen relativo)

Mezclar las capas en una sola frase ("with sounds and dialogue") produce audio amateur con mala mezcla. Describirlas separadas da resultado pro.

## Soporte por plataforma

| Plataforma | Audio nativo | Dialog | SFX | Ambient | Music | Voz del personaje desde audio | Se puede apagar |
|------------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Veo 3.1 | ✅ siempre activo | ✅ | ✅ | ✅ | ✅ | ❌ (no acepta audio de referencia) | ❌ |
| Kling 3.0 | ✅ | ✅ (zh, en, ja, ko, es) | ✅ | ✅ | ✅ | **✅ voz atada al element** | ✅ (`audio: off`) |
| Seedance 2.5 | ✅ audio y vídeo juntos | ✅ (10+ idiomas) | ✅ | ✅ | ✅ | ✅ hasta 10 audios de referencia | ✅ en la API (`generate_audio`) |
| Runway Gen-4.5 | ✅ | ✅ | ✅ | ✅ | ✅ | Character reference | sin verificar |
| Hailuo 2.3 (T2) | ⚠️ No confirmado | n/d | n/d | n/d | n/d | n/d | n/d |

## Sintaxis canónica detallada

### Veo 3.1 (audio siempre activo)

Sintaxis de la **guía oficial de prompting de Veo 3.1** (Google Cloud): lenguaje natural, cada capa en su frase, sin etiqueta `Audio:`.

```
[Scene description].

A woman says, "Bienvenida a mi marca."
A man responds, "Let's get started."

SFX: glass shattering on impact.
SFX: keyboard taps throughout.

Ambient noise: distant city traffic, soft rain on metal roof.

A cinematic string score builds tension at low volume.
```

**Estructura:**
- `A [woman / man / child / narrator] says, "..."` para diálogo, siempre entre comillas
- `SFX:` para efectos puntuales
- `Ambient noise:` para ruido de fondo continuo
- Música en una frase natural con mood y volumen relativo ("low volume", "background", "prominent")
- Para varios planos, tramos de tiempo: `[00:00-00:03] ...` y el audio de cada tramo dentro de él

**El audio de Veo 3.1 está SIEMPRE activo y no se desactiva.** No hay ninguna opción tipo "foley auto": si no describes el sonido, el modelo lo genera coherente con la escena de todos modos. Para controlarlo, la única vía es describirlo tú en el prompt.

```json
"platform_specific": {
  "veo_3_1": {
    "duration_seconds": 8,
    "resolution": "4k"
  }
}
```

**Multi-character dialog:**
```
The woman says, "Did you finish the report?"
The man responds, "Almost, I just need to check the numbers."
She sighs and says, "We need it by 5."

SFX: keyboard typing, continuous and low volume.
Ambient noise: open office, distant typing, soft conversation, climate control hum.
```

---

### Kling 3.0 (personaje identificado + voz atada al element)

Sintaxis de las **guías oficiales de Kling VIDEO 3.0 y 3.0 Omni**: cada línea de diálogo lleva el personaje y, entre paréntesis, el tono. La voz en off igual.

```
[Scene description with camera + lighting]

Founder (warm, confident tone, slow pace): Llevo dos meses con el producto y recupero una hora al día.
Voiceover (calm female voice, Spanish from Spain): Así empieza tu mañana.

Sound effects: a soft cup clink near the end.
Ambient: busy cafe, distant chatter, espresso machine soft hiss.
Music: light upbeat lo-fi instrumental at very low volume.
```

**Estructura:**
- `Personaje (tono, ritmo, acento): línea` para cada línea de diálogo
- `Voiceover (descripción de la voz): línea` para narración
- En escenas con varios personajes, **cada línea con su personaje**: Kling 3.0 identifica quién habla
- SFX, ambiente y música en frases separadas
- Idiomas del diálogo: chino, inglés, japonés, coreano y español, con acentos y dialectos

**Ejemplo con varios personajes** (patrón de la guía oficial):
```
A father and his daughter talk at the kitchen table, eye-level two-shot, warm morning light.

Daughter (surprised, fast pace): ¿En serio lo has hecho tú?
Dad (in a low voice, agreeing, calm tone): Sí, ni yo me lo esperaba.
Ambient: quiet kitchen, a kettle starting to boil.
```

**La misma voz en varios clips:** se ata al **element** del personaje al crearlo (audio limpio de una sola persona; la guía de Omni recomienda 5-30 s, sin ruido de fondo; en un element creado desde vídeo, la voz se extrae del propio vídeo). Si el element ya tiene voz, **no describir otra voz en el prompt**: la guía lo desaconseja.

```json
"platform_specific": {
  "kling_3_0": {
    "model": "video_3_0_omni",
    "audio": "native",
    "element": "Founder",
    "voice_bound_to_element": true
  }
}
```

> La sintaxis `[AUDIO: ...]` en bloque, `voice_clone_ref` y `cfg_scale` venían de la ficha de Kling 2.6 y **no aparecen en la documentación de Kling 3.0**. No usarlas.

---

### Seedance 2.5 (audio y vídeo generados juntos)

Seedance 2.5 genera el audio y el vídeo en la misma pasada (en la API de BytePlus ModelArk se pide con `generate_audio`) y acepta **hasta 10 audios de referencia**, además de 30 imágenes y 10 vídeos (como máximo 30 s sumando vídeos y audios). Fuentes: página oficial de Seedance 2.5 (ByteDance Seed) y tutorial de ModelArk.

#### Sintaxis canónica

```
[Scene description natural]

A woman says, "We just shipped v2."
SFX: keyboard typing throughout, soft pen tap on the desk.
Ambient: open office, light conversation, climate hum.
Music: ambient electronic, low volume.
```

#### Varios planos y tramos de tiempo con audio coherente

En 30 s el modelo organiza varios planos. El audio se puede dirigir por tramos, con la misma sintaxis de los ejemplos oficiales:

```
0-10s: wide shot, the woman from @Image 1 reviews papers at her desk. SFX: paper rustle.
11-20s: close-up, she looks up and says, "And then the numbers came in." SFX: marker squeak.
21-30s: medium shot, she smiles at the screen. SFX: a soft UI click.
Ambient: office at evening, then morning.
Music: cinematic strings, from tense to hopeful.
```

#### Voz con audio de referencia

```json
"platform_specific": {
  "seedance_2_5": {
    "generate_audio": true,
    "audio_refs": ["https://tu-marca.com/voces/founder_voice.mp3"]
  }
}
```

En el prompt, las referencias se citan por número, como en los ejemplos oficiales (`@Image 1`, `@Video 1`...). Se pueden usar varios audios de referencia para distintas cosas (la voz del personaje, una música de estilo, un ambiente), hasta 10.

#### Veo 3.1 vs Seedance 2.5

| Aspecto | Veo 3.1 | Seedance 2.5 |
|---------|---------|--------------|
| Estructura básica | diálogo entre comillas + `SFX:` + `Ambient noise:` + música en frase | Misma estructura |
| Duración con audio | 8 s por clip | de 4 a 30 s por generación |
| Voz desde audio | ❌ | ✅ audios de referencia |
| Varios planos | tramos `[00:00-00:03]` dentro de 8 s | planos organizados por el modelo + tramos |
| Apagar el audio | ❌ no se puede | ✅ en la API (`generate_audio`) |

**Regla de selección:** Veo 3.1 para clips de hasta 8 s a 4K. **Kling 3.0** si quieres la voz atada al personaje y hasta 15 s. **Seedance 2.5** si necesitas hasta 30 s, varios planos o varios audios de referencia.

---

### Runway Gen-4.5 (Director Mode con audio per-scene)

Runway Gen-4.5 con multi-escena estructura el audio **por escena** en el Director Mode:

```
[Subject + scene description global]

camera_control: {type: "static", direction: null, speed: 0}

scenes:
  [Scene 1 - 12s]
  shot: wide_desk
  camera: static medium-wide
  lighting: cool desaturated evening
  audio:
    sfx: paper rustle (continuous, low volume)
    ambient: office at night, fluorescent buzz
    music: cinematic strings (tense, building)
    dialog: (none in this scene)

  [Scene 2 - 10s]
  shot: close_up_screen
  camera: slow push-in 50mm
  lighting: harsh blue screen-glow only
  audio:
    sfx: notification chimes (3 chimes layered over the 10s)
    ambient: silence except for the chimes
    music: cinematic strings (peak tension)
    dialog: (none)

  [Scene 3 - 18s]
  shot: wide_whiteboard
  camera: slow orbital around two people
  lighting: warm balanced morning
  audio:
    sfx: marker on whiteboard (squeaks, intermittent)
    ambient: morning office (light typing, soft conversation)
    music: hopeful piano + strings transition (shift in mood)
    dialog: narrator says, "When we found the right tool..."
```

**Multi-scene audio coherence:**
Runway gestiona transiciones de audio entre escenas. Indicar transitions explícitamente cuando aplica:

```
Audio transition from scene 2 to scene 3: fade out tension music, fade in hopeful piano (2 second crossfade).
```

---

## Sintaxis comparativa rápida

| Capa | Veo 3.1 | Kling 3.0 | Seedance 2.5 | Runway Gen-4.5 |
|------|-------|-----------|--------------|----------------|
| Dialog | `A woman says, "..."` | `Woman (tono): línea` | `A woman says, "..."` | `dialog: narrator says, "..."` en scene |
| SFX | `SFX: [descripción]` | `Sound effects: [descripción]` | `SFX: [descripción]` | `sfx: [descripción]` en scene |
| Ambient | `Ambient noise: [descripción]` | `Ambient: [descripción]` | `Ambient: [descripción]` | `ambient: [descripción]` en scene |
| Music | frase natural con mood + volumen | `Music: [mood + volumen]` | `Music: [mood + volumen]` | `music: [mood + transición]` en scene |
| Voz fija del personaje | ❌ | element con voz atada | `audio_refs` citados por número | Character reference |

## Reglas universales

1. **DESCRIBIR LAS 4 CAPAS POR SEPARADO**, no concatenar en una sola frase
2. **TIMING ESPECÍFICO** cuando aplica: "near the end", "fade in over 2s", "throughout", o tramos de tiempo
3. **VOLUMEN RELATIVO**: "very low volume", "prominent", "background". Sin esto el modelo nivela mal
4. **MOOD DE LA MÚSICA**: no "music" solo, sino "cinematic strings, tense, building" o "lo-fi instrumental, calm"
5. **AMBIENT debe ser COHERENTE** con la escena: café = "distant chatter + espresso", oficina = "typing + chatter + climate hum", calle = "traffic + footsteps + distant horn"
6. **DIÁLOGO con CHARACTER específico**: `A woman says, ...` (Veo, Seedance) o `Woman (tono): ...` (Kling). No genérico
7. **En Veo 3.1 el audio es inevitable**: no hay flag que lo apague, así que descríbelo tú si quieres controlarlo
8. **VOZ FIJA del personaje**: en Kling 3.0, el element con la voz atada; en Seedance 2.5, el mismo audio de referencia en cada generación. Veo 3.1 no la admite

## Anti-patterns

❌ `with sound effects and dialogue` (vago, sin specificity)
❌ `audio: dramatic music` (sin estructura, sin volumen, sin context)
❌ `[AUDIO: ...]` en bloque para Kling 3.0 (sintaxis de la ficha de 2.6, no documentada en 3.0)
❌ Diálogo sin character ("a voice says..." en lugar de "A woman says..." o "Woman (tono):")
❌ SFX sin timing en escenas largas (cuándo ocurre el sonido?)
❌ Mezclar music y SFX sin diferenciar volúmenes (música prominente tapa el SFX)
❌ Describir otra voz en el prompt cuando el element de Kling ya tiene una voz atada
❌ Pedir a Veo 3.1 "sin audio": no se puede apagar; describir "only quiet room tone" y quitar la pista en montaje

## Cómo se integra al JSON v2.0

El campo `audio` se rellena estructuradamente:

```json
{
  "audio": {
    "required": true,
    "dialog": [
      {"character": "WOMAN", "text": "Llevo dos meses con el producto..."},
      {"character": "NARRATOR", "text": "When we found the right tool..."}
    ],
    "sound_effects": [
      "soft cup clink near the end",
      "notification chimes (3 layered)"
    ],
    "music_mood": "Light upbeat lo-fi instrumental, very low volume in background",
    "ambient": "Cafe interior, distant chatter, soft espresso machine hiss"
  }
}
```

El natural language prompt construye la sintaxis específica de la plataforma destino desde este objeto (Veo 3.1 y Seedance 2.5 separan capas con `says,` / `SFX:` / `Ambient`, Kling 3.0 pone el personaje y el tono delante de cada línea, Runway estructura por scene).

## Casos especiales

### Video sin audio (silent, para doblar en post)

```json
{
  "audio": {
    "required": false
  }
}
```

- **Kling 3.0:** `audio: off`
- **Seedance 2.5:** `generate_audio: false` en la API; en las apps, comprobar si hay opción
- **Veo 3.1:** el audio no se puede apagar. Escribir "No dialogue, no music, only quiet room tone." y quitar la pista en montaje
- **Runway:** comprobar en la plataforma; si no hay opción, igual que Veo

### Solo música, sin SFX/dialog

```json
{
  "audio": {
    "required": true,
    "dialog": [],
    "sound_effects": [],
    "music_mood": "Ambient electronic, slow build, atmospheric",
    "ambient": ""
  }
}
```

Natural language: `Music only: ambient electronic, slow build, atmospheric. No dialogue, no sound effects, no ambient noise.`

### Solo ambient (autenticidad UGC)

```json
{
  "audio": {
    "required": true,
    "dialog": [],
    "sound_effects": ["soft pen tap on desk"],
    "music_mood": "",
    "ambient": "Light office ambient: distant typing, soft conversation murmur, climate control hum"
  }
}
```

Natural language: `SFX: a soft pen tap on the desk surface. Ambient noise: light office, distant typing, very soft conversation murmur, faint climate control hum. No music, ambient sound only.`

---

**Aplicación:** el `lyra-engineer` invoca esta skill cuando el JSON tiene `audio.required = true`. El `visual-prompt-auditor` valida que la sintaxis del NL prompt coincida con la plataforma destino (por ejemplo, `Personaje (tono): línea` en Kling 3.0 y nunca `[AUDIO: ...]`; diálogo entre comillas en Veo 3.1 y Seedance 2.5).
