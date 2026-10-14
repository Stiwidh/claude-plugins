---
name: audio-cue-syntax
description: |
  Sintaxis canónica de audio para video por plataforma — Veo 3.1 (Audio + SFX + Ambient noise), Kling 3.0 ([AUDIO ...] bracket), Runway Gen-4.5 (Director Mode con audio per-scene). Aplicar siempre que el JSON v2.0 tiene `audio.required = true`. Audio bien estructurado diferencia un video amateur de uno profesional.
user-invocable: true
argument-hint: "<platform>"
allowed-tools:
  - Read
---

# Skill — Audio Cue Syntax

## Capas de audio en video pro

Un video con audio nativo (Veo 3.1, Kling 3.0, Runway Gen-4.5) tiene 4 capas que deben describirse SEPARADAS:

1. **Dialog** — palabras habladas (diálogo de personajes o narrator)
2. **SFX** (Sound Effects) — efectos puntuales sincronizados (un golpe, un click, una explosión)
3. **Ambient** — ruido de fondo continuo (cafe noise, lluvia, tráfico)
4. **Music** — música de fondo (mood, género, volumen relativo)

Mezclar las capas en una sola frase ("with sounds and dialogue") produce audio amateur con mala mezcla. Describirlas separadamente da resultado pro.

## Soporte por plataforma

| Plataforma | Audio nativo | Dialog | SFX | Ambient | Music | Voice clone | Lip-sync |
|------------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Veo 3.1 | ✅ audio nativo | ✅ | ✅ | ✅ | ✅ | Imágenes de referencia (máx. 3) | preciso |
| Kling 3.0 | ✅ Single-pass | ✅ | ✅ | ✅ | ✅ | ✅ Voice clone upload | Bueno |
| Seedance 2.5 | ✅ Unified arch | ✅ | ✅ | ✅ | ✅ | ✅ Audio ref upload | **Phoneme-level (líder)** |
| Runway Gen-4.5 | ✅ | ✅ | ✅ | ✅ | ✅ | Character reference | Bueno |
| Veo 3.1 (T3) | ⚠️ Limitado | ✅ basic | — | — | — | — | Limitado |
| Hailuo 2.3 (T2) | ⚠️ No confirmado | — | — | — | — | — | — |

## Sintaxis canónica detallada

### Veo 3.1 (mejor audio nativo Tier 1)

Veo 3.1 usa **lenguaje natural con keywords explícitos:**

```
[Scene description].

Audio:
A woman says, "Bienvenida a mi marca."
A man responds, "Let's get started."

SFX: glass shattering on impact at second 4.
SFX: keyboard taps throughout.

Ambient noise: distant city traffic, soft rain on metal roof.

Music: Cinematic strings, building tension, low volume.
```

**Estructura:**
- `Audio:` introduce la sección
- `A [woman / man / child / narrator] says, "..."` para diálogo
- `SFX:` para efectos puntuales (incluir timing si específico: "at second X")
- `Ambient noise:` para ruido de fondo continuo
- `Music:` para música (mood + volumen relativo: "low volume", "background", "prominent")

**El audio de Veo 3.1 está SIEMPRE activo y no se desactiva.** No hay ninguna opción tipo
"foley auto": si no describes el sonido, el modelo lo genera coherente con la escena de todos
modos. Para controlarlo, la única vía es describirlo tú en el prompt.

```json
"platform_specific": {
  "veo_3_1": {
    "duration_seconds": 8,
    "resolution": "4k"
  }
}
```

**Multi-character dialog (Veo 3.1 lo maneja bien):**
```
Audio:
The woman says, "Did you finish the report?"
The man responds, "Almost — just need to check the numbers."
She sighs and says, "We need it by 5."

SFX: keyboard typing (continuous low-volume).
Ambient noise: open office — distant typing, soft conversation, climate control hum.
```

---

### Kling 3.0 (bracket syntax)

Kling usa **bracket syntax** todo en una línea o sección:

```
[Scene description with camera + lighting]

[AUDIO: descripción densa de todo el audio en una frase larga separada por comas]
```

**Estructura:**
- `[AUDIO: ...]` engloba TODO el audio en un solo bloque
- Separación por comas para distintos sonidos
- Indicaciones temporales o de capa entre paréntesis

**Ejemplo simple:**
```
A noir detective walks through rain-soaked alley at night, low-angle tracking shot, cinematic film grain, 48fps.

[AUDIO: Heavy rain on pavement, distant thunder, slow footsteps on wet pavement, zippo lighter click at second 6, ambient muffled city traffic]
```

**Ejemplo con dialog:**
```
Young professional speaks directly to camera in cafe setting, eye-level wide shot, soft window light.

[AUDIO: Woman saying "Llevo dos meses con el producto y recupero una hora al día — literal", cafe ambient (distant chatter, espresso machine soft hiss), soft cup clink at second 8, light upbeat lo-fi instrumental at very low volume]
```

**Voice cloning (Kling única en Tier 1 con voice clone explícito):**
```json
"platform_specific": {
  "kling_3_0": {
    "cfg_scale": 7.5,
    "motion_intensity": "medium",
    "voice_clone_ref": "https://corvere.com/voices/founder.mp3"
  }
}
```

El audio del speaker en el video usará la voz del archivo de referencia.

---

### Seedance 2.5 (unified architecture — el modelo "oye" lo que genera)

Seedance 2.5 tiene **unified audio-video architecture**: en cada frame, el modelo escucha lo que está sonando mientras genera la imagen. Esto produce:

- Lip-sync **phoneme-level** (mejor del mercado a mayo 2026)
- Natural reverb coherente con el espacio visible
- Proximity effects automáticos (voz cercana suena distinto a voz lejana)
- SFX sincronizados con micro-acciones en el frame

#### Sintaxis canónica (similar a Veo 3.1 pero con auto-storyboard)

```
[Scene description natural]

Audio sincronizado (auto-generated por unified architecture):
A founder says, "We just shipped v2."
SFX: keyboard typing throughout, soft pen tap at second 4.
Ambient: open office — light conversation, climate hum.
Music: ambient electronic, low volume (-12dB relative).
```

**Estructura igual a Veo 3.1** (`A [character] says, "..."` + `SFX:` + `Ambient:` + `Music:`) — Seedance lo procesa con su unified architecture.

#### Multi-shot con audio coherente

Cuando Seedance auto-storyboards en N shots, mantiene **continuidad de audio** entre shots (música arrastra, ambiente se mantiene, voz coherente con character):

```
[Scene description across 3 shots — auto-storyboard]

Audio:
A woman says in shot 2, "And then the numbers came in."
SFX: paper rustle (shot 1), marker squeak (shot 2), soft UI click (shot 3).
Ambient: office at evening (s1, cool) → office at morning (s2, warm) → office at afternoon (s3, warm).
Music: cinematic strings, arcing from tense (s1) → hopeful (s2) → triumphant restrained (s3).
```

#### Voice cloning con audio_ref

```json
"platform_specific": {
  "seedance_2_5": {
    "variant": "pro",
    "audio_refs": ["https://corvere.com/voices/founder_voice.mp3"]
  }
}
```

→ Seedance clona la voz del audio_ref y aplica lip-sync phoneme-level al dialog del prompt. Más preciso que Kling voice clone porque la unified architecture genera frame por frame con el audio target ya conocido.

#### Multimodal audio refs (hasta 3)

Puedes pasar 3 audio_refs distintos para distintos usos:

```json
"audio_refs": [
  "https://corvere.com/voices/founder_voice.mp3",  // voice clone del speaker
  "https://corvere.com/music/cinematic_strings.mp3",  // style ref música
  "https://corvere.com/ambient/office_ambient.mp3"  // ambient sample
]
```

#### Sintaxis comparativa Veo 3.1 vs Seedance 2.5

| Aspecto | Veo 3.1 | Seedance 2.5 |
|---------|-------|--------------|
| Estructura básica | `Audio:` + `SFX:` + `Ambient noise:` + `Music:` | Misma estructura |
| Lip-sync | preciso (excelente) | **Phoneme-level (líder)** |
| Voice clone | Avatar zero-shot vía foto | Audio upload directo en `audio_refs` |
| Multi-shot audio | Director Mode manual | Auto-storyboard mantiene continuidad |
| Foley | Siempre activo, no configurable | Generado automáticamente por unified architecture |

**Regla de selección:** Veo 3.1 si necesitas 4K en 8s. Seedance 2.5 si necesitas multi-shot auto + lip-sync phoneme-level + multimodal input.

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
| Dialog | `A woman says, "..."` | `Woman saying "..."` dentro de `[AUDIO: ...]` | `A woman says, "..."` (igual que VEO) | `dialog: narrator says, "..."` en scene |
| SFX | `SFX: [descripción] at second [N]` | dentro de `[AUDIO: ...]` con comas | `SFX: [descripción]` (igual que VEO) | `sfx: [descripción]` en scene |
| Ambient | `Ambient noise: [descripción]` | dentro de `[AUDIO: ...]` con comas | `Ambient: [descripción]` (igual que VEO) | `ambient: [descripción]` en scene |
| Music | `Music: [mood + volumen]` | dentro de `[AUDIO: ...]` con comas | `Music: [mood + volumen]` (igual que VEO) | `music: [mood + transición]` en scene |

## Reglas universales

1. **DESCRIBIR LAS 4 CAPAS POR SEPARADO** — no concatenar en una sola frase
2. **TIMING ESPECÍFICO** cuando aplica — "at second 8", "fade in over 2s", "throughout"
3. **VOLUMEN RELATIVO** — "very low volume", "prominent", "background" — sin esto el modelo nivela mal
4. **MOOD DE LA MÚSICA** — no "music" solo, sino "cinematic strings, tense, building" o "lo-fi instrumental, calm"
5. **AMBIENT debe ser COHERENTE** con la escena — café = "distant chatter + espresso", oficina = "typing + chatter + climate hum", calle = "traffic + footsteps + distant horn"
6. **DIÁLOGO con CHARACTER específico** — `MAN / WOMAN / CHILD / NARRATOR / OLD_MAN`, no genérico
7. **En Veo 3.1 el audio es inevitable** — no hay flag que lo apague, así que descríbelo tú si quieres controlarlo
8. **VOICE CLONE** (Kling solo) — URL del audio de referencia en `platform_specific.kling_3_0.voice_clone_ref`

## Anti-patterns

❌ `with sound effects and dialogue` (vago — sin specificity)
❌ `audio: dramatic music` (sin estructura, sin volumen, sin context)
❌ `[AUDIO: rain]` en Kling (demasiado pobre, falta layering)
❌ Diálogo sin character ("a voice says..." en lugar de "A woman says...")
❌ SFX sin timing en escenas largas (cuándo ocurre el sonido?)
❌ Mezclar music y SFX sin diferenciar volúmenes (música prominente tapa el SFX)

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
      "soft cup clink at second 8",
      "notification chimes (3 layered)"
    ],
    "music_mood": "Light upbeat lo-fi instrumental, very low volume in background",
    "ambient": "Cafe interior — distant chatter, soft espresso machine hiss"
  }
}
```

El natural language prompt construye la sintaxis específica de la plataforma destino desde este objeto.

## Casos especiales

### Video sin audio (silent)

```json
{
  "audio": {
    "required": false
  }
}
```

Natural language explicito: `[NO AUDIO — muted asset]` para evitar que el modelo añada audio nativo.

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

Natural language: `Audio: Music only — ambient electronic, slow build, atmospheric. No dialog, no sound effects, no ambient.`

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

Natural language: `Audio: SFX: Soft pen tap on the desk surface around second 3. Ambient noise: Light office — distant typing, very soft conversation murmur, faint climate control hum. [No music — ambient sound only for authenticity]`

---

**Aplicación:** el `lyra-engineer` invoca esta skill cuando el JSON tiene `audio.required = true`. El `visual-prompt-auditor` valida que la sintaxis del NL prompt coincida con la plataforma destino (e.g., `[AUDIO: ...]` solo en Kling, no en Veo 3.1).
