---
name: negative-prompt-library
description: Librería canónica de negative prompts por use case para modelos de generación de imagen y video. Aplicar siempre que se completa el campo `negative_prompt` del JSON v2.0. Defaults canónicos + extensions context-specific (personas, producto, video cinemático, texto en imagen, brand, arquitectura, comida).
user-invocable: true
argument-hint: "<use-case>"
allowed-tools:
  - Read
---

# Skill — Negative Prompt Library

## Defaults canónicos (siempre incluir)

```json
["blurry", "low quality", "distorted proportions", "bad lighting", "amateur"]
```

Estos 5 son baseline universal. Se añaden a cualquier negative_prompt.

## Soporte por plataforma

| Plataforma | Soporte | Sintaxis |
|------------|---------|----------|
| Nano Banana Pro | ✅ Nativo | `negative_prompt: [array]` en API |
| GPT Image 2 | ⚠️ Vía lenguaje natural | "Avoid X, Y, Z" en el prompt principal |
| Midjourney V8.1 | ✅ Nativo | `--no X, Y, Z` al final |
| FLUX.2 Pro | ✅ Nativo | `negative_prompt` en API |
| Kling 3.0 | sin verificar en la API 3.0 | Si la interfaz no tiene campo de negative, exclusión en el prompt |
| Seedance 2.5 | sin verificar | Si la interfaz no tiene campo de negative, exclusión en el prompt |
| Veo 3.1 | ⚠️ Sin parámetro en la Gemini API | Exclusión descriptiva en prompt principal (describir lo que sí se quiere) |
| Runway Gen-4.5 | ✅ Nativo | En API |

## Librería por use case

### Personas fotorrealistas

```json
["deformed hands", "extra fingers", "missing fingers", "blurry face", "uncanny valley", "asymmetric eyes", "distorted proportions", "weird teeth", "fused fingers"]
```

**Cuándo:** retratos, lifestyle con personas, UGC con humanos. Cualquier escena donde personas son sujeto primario.

---

### Product photography

```json
["low quality", "watermark", "text artifacts", "pixelated", "oversaturated", "plastic look", "fake reflections", "stock photo aesthetic", "cluttered background"]
```

**Cuándo:** packaging, e-commerce, product hero shots, ads.

---

### Cinematic video

```json
["shaky camera", "motion blur (unintended)", "compression artifacts", "rapid cuts", "frame drops", "low frame rate", "amateur handheld"]
```

**Cuándo:** brand films, narrative pieces, video Veo 3.1 / Kling 3.0 / Seedance 2.5 / Runway Gen-4.5.

---

### Imagen con texto

```json
["illegible text", "misspelled words", "blurry letters", "distorted fonts", "gibberish text", "low contrast text", "inconsistent kerning", "wrong character spacing"]
```

**Cuándo:** posters, infografías, packaging con typography, banners, ads con copy.

---

### Brand assets

```json
["off-brand colors", "generic stock photo look", "clipart style", "low-poly", "generic icons", "Photoshop filter aesthetic"]
```

**Cuándo:** activos de marca específicos, deliverables cliente con guía de identidad estricta.

---

### Arquitectura / interiores

```json
["crooked lines", "warped perspective", "impossible geometry", "melting walls", "non-Euclidean space", "inconsistent shadows", "fake windows"]
```

**Cuándo:** real estate, interior design, architectural visualization.

---

### Comida (food photography)

```json
["unappetizing", "plastic-looking", "overcooked", "gray tones", "fake garnish", "wet plastic look", "oversaturated reds", "uncanny shine"]
```

**Cuándo:** restaurant content, recipe photography, food brand assets.

---

### Vehículos

```json
["distorted body panels", "asymmetric headlights", "wrong wheel proportions", "fake reflections on paint", "inconsistent shadows"]
```

**Cuándo:** automotive content, dealership ads, vehicle reviews.

---

### Wildlife / animales

```json
["distorted anatomy", "extra limbs", "wrong fur texture", "uncanny eyes", "deformed snout/beak", "incorrect species traits"]
```

**Cuándo:** wildlife photography, pet content, nature documentaries style.

---

### Naturaleza / paisaje

```json
["overprocessed HDR", "fake sky", "implausible weather", "distorted clouds", "unrealistic reflections on water", "color banding"]
```

**Cuándo:** landscape photography, nature content, travel content.

---

### Tech / UI screens

```json
["distorted UI elements", "garbled text on screens", "fake app interface", "low-res screen", "incorrect device proportions", "stock UI aesthetic"]
```

**Cuándo:** product demos, screen recording style, tech advertising.

---

### Video con audio sincronizado

```json
["out of sync audio", "lip-sync mismatch", "audio dropout", "audio clipping", "robotic voice", "uncanny dialogue delivery"]
```

**Cuándo:** Veo 3.1 / Kling 3.0 / Seedance 2.5 / Runway Gen-4.5 con dialog.

## Cómo aplicarlo

1. **Empezar con defaults canónicos** (siempre los 5 baseline)
2. **Detectar use case** (personas, producto, brand, etc.)
3. **Añadir negative del use case** correspondiente
4. **Adaptar a la plataforma:**
   - Tier 1 con soporte nativo → meter en `negative_prompt` array del JSON
   - GPT Image 2 / Veo 3.1 (y Kling 3.0 / Seedance 2.5 si la interfaz no tiene campo de negative) → incluir como "Avoid X, Y, Z" en natural language prompt

## Ejemplos combinados

### Use case: portrait fundador + texto en imagen
```json
{
  "negative_prompt": [
    "blurry", "low quality", "distorted proportions", "bad lighting", "amateur",
    "deformed hands", "uncanny valley", "asymmetric eyes",
    "illegible text", "misspelled words", "blurry letters"
  ]
}
```

### Use case: cinematic brand video con personas y dialog
```json
{
  "negative_prompt": [
    "blurry", "low quality", "distorted proportions", "bad lighting", "amateur",
    "deformed hands", "extra fingers", "uncanny valley",
    "shaky camera", "compression artifacts", "rapid cuts",
    "out of sync audio", "lip-sync mismatch"
  ]
}
```

### Use case: producto e-commerce flatlay
```json
{
  "negative_prompt": [
    "blurry", "low quality", "distorted proportions", "bad lighting", "amateur",
    "watermark", "text artifacts", "plastic look", "fake reflections",
    "stock photo aesthetic", "cluttered background"
  ]
}
```

## Anti-patterns

❌ Negative prompt vacío → SIEMPRE incluir al menos defaults canónicos
❌ Negative prompt copy-paste de otra escena sin context-specific → no aplica los mismos riesgos
❌ Negative prompts contradictorios al positive prompt → ej. "blurry" negative + "shallow depth of field" positive (shallow DoF genera blur intencional)
❌ Negative prompts excesivamente largos (>15 items) → diluye la señal al modelo

---

**Aplicación:** el `lyra-engineer` consume esta skill al completar el campo `negative_prompt` del JSON v2.0. El `visual-prompt-auditor` valida que esté poblado coherentemente con el use case.
