---
name: platform-cheatsheet
description: Cobertura completa Tier 1 / Tier 2 / Tier 3 de plataformas de generación de imagen y video a mayo 2026 (vídeo Tier 1 re-verificado el 2026-10-15). Specs técnicos, sintaxis de prompt, pricing, capability sweet spots, deprecation status. Aplicar cuando se necesita confirmar capabilities exactas de una plataforma antes de generar, justificar elección de modelo, o detectar mismatch de capacidad.
user-invocable: true
argument-hint: "[platform_name]"
allowed-tools:
  - Read
  - Glob
  - Grep
---

# Skill — Platform Cheatsheet (mayo 2026)

Tabla resumen rápida + detalle expandido en `references/platforms-2026-05.md`.

## Tier 1 — Cobertura completa

| Plataforma | Tipo | Resolución | Duración | Audio | Text rendering | API | Sweet spot |
|------------|------|------------|----------|-------|----------------|-----|-----------|
| **Nano Banana Pro** | Imagen | 4K | — | — | 92% accuracy | ✅ | Brand identity + multi-image fusion (14) + factual grounding |
| **GPT Image 2** | Imagen | 4K | — | — | ~99% multi-script | ✅ | Texto largo / multi-idioma + reasoning + multi-turn edit |
| **Midjourney V8.1** | Imagen | 2K | — | — | Comillas inline | ❌ (Discord/web) | Dirección artística autoral, photography editorial |
| **FLUX.2 Pro** | Imagen | 4 MP | — | — | Multi-line typography | ✅ | Producción pro + character persistence + open weights `[dev]` |
| **Veo 3.1** | Video | 4K (solo a 8s) | 4/6/8s | ✅ siempre activo | 3 imgs ref | ✅ | Clip corto con audio nativo en 4K |
| **Gemini Omni Flash** | Video | no publicada | 10s (anuncio) | ✅ | texto+imagen+vídeo (audio NO) | ✅ | **Editar un vídeo ya hecho hablando con él** |
| **Kling 3.0** | Video | 4K nativo | 3-15s | ✅ nativo u off | n/a | ✅ | 8-15s en una toma con Multi-Shot + voz atada al element |
| **Seedance 2.5** | Video | 1080p | 4-30s (+ extensiones) | ✅ audio y vídeo juntos | n/a | ✅ BytePlus ModelArk | Varios planos hasta 30s + muchas referencias (30 img + 10 vídeos + 10 audios) |

**Kling 4.0** (anunciado el 30-sep-2026, 30s y 10 keyframes) está en despliegue limitado a 15-oct-2026: no se recomienda hasta que esté en la cuenta de quien genera.
| **Runway Gen-4.5** | Video | 4K | ≤60s | ✅ | — | ✅ | Multi-escena + character consistency + Motion Brush |

## Tier 2 — Cobertura básica

| Plataforma | Diferenciador |
|------------|---------------|
| **Ideogram V3** | Mejor text rendering puro (tipografía) |
| **Recraft V4** | **Único** modelo SVG/vector production-quality |
| **SD4 Ultra** | Open weights community |
| **Wan 2.7 Image** | Open source, Thinking Mode |
| **Luma Ray 3.14** | **Único** modelo HDR cine-grade nativo (16-bit EXR) |
| **Pika 2.5** | Camera direction first-class, scene extension |
| **Hailuo 2.3** | $0.28/video, volumen alto |
| **Dreamina Seedance 2.5** | Integración CapCut nativa |
| **Wan 2.7 Video** | Open source, lip-sync, self-host |

## Tier 3 — Deprecated / EOL

| Plataforma | Estado | Reemplazo |
|------------|--------|-----------|
| **Sora 2 / Sora 2 Pro** | ⚠️ API EOL 24-sep-2026, web/app 26-abr-2026 | Veo 3.1 (8s, audio nativo) o Runway Gen-4.5 (60s, multi-escena) |
| **DALL-E 2 / DALL-E 3** | ❌ Deprecated 12-may-2026 | GPT Image 2 (reemplazo directo OpenAI) |

## Sintaxis canónica por plataforma

### Nano Banana Pro
```
[Subject + scene] + [Composition / Camera] + [Lighting] + [Style + mood] + [Tech specs]

Include legible text: "EXACT" in [Font] typeface, [Size]pt, [Color hex], [Position]

Color hex preciso siempre que sea distintivo.
```

### GPT Image 2
```
[Descripción natural detallada]

Consider before generating:
- [Restricción 1]
- [Restricción 2]
Verify [requirement] before finalizing.

For text: "Include the exact text 'TEXT' in [Font Bold] [Size], [Color], [Position]. Use proper character spacing."
```

### Midjourney V8.1
```
[Subject + scene] --ar [ratio] --hd --q 4 [--sref URL] [--cref URL] [--no negative1, negative2]

For text: "EXACT TEXT" inline (con comillas)
```

### FLUX.2 Pro
```
[Descripción densa natural]

Multi-line typography:
Line 1: 'TEXT 1'
Line 2: 'TEXT 2'
Line 3: 'TEXT 3'
Typography: [Font] [Weight], spacing [tight/loose], color [hex]
```

### Veo 3.1
```
[Cinematografía]: [Subject] [Action], in [Setting + atmosphere], lit by [Light source].
Style: [Texture].
A woman says, "..."
SFX: glass shattering.
Ambient noise: distant traffic.
(audio en frases aparte, sin etiqueta "Audio:"; varios planos por tramos [00:00-00:03])
```

### Kling 3.0
```
[Subject + action] + [Environment] + [Camera] + [Style]

Founder (warm, confident tone): Llevo dos meses con esto.
Sound effects: a soft cup clink near the end.
Ambient: busy cafe, distant chatter.
Music: light lo-fi at very low volume.

Custom Multi-Shot (con Multi-Shot activo):
Shot 1 (4s): ... · Shot 2 (5s): ... · Shot 3 (6s): ...
(sin cfg_scale ni [AUDIO: ...]: no existen en la documentación de 3.0)
```

### Seedance 2.5
```
[Descripción natural de la escena y del arco: el modelo organiza los planos]

The woman from @Image 1 enters the office from @Image 2.
0-10s: wide establishing ...
11-20s: close-up ...
21-30s: medium shot, she speaks to camera.

A woman says, "..."
SFX: keyboard typing, soft pen tap.
Ambient: open office hum.
Music: ambient electronic, low volume.

Refs: hasta 30 imágenes + 10 vídeos + 10 audios, citados @Image 1, @Video 1...
Duración 4-30s o -1 (decide el modelo) · ratio 16:9, 4:3, 1:1, 3:4, 9:16, 21:9 o adaptive
```

### Runway Gen-4.5
```
[Subject + scene] + [Style]

camera_control: {type: "dolly", direction: "forward", speed: 0.5}

Director Mode (multi-escena):
scenes: [
  {shot, duration, camera, lighting, emotional_beat},
  ...
]
```

## Pricing (mayo 2026)

| Plataforma | Coste |
|------------|-------|
| Nano Banana Pro | $0.134/img 2K · $0.24/img 4K · Batch $0.12 (-50%) |
| GPT Image 2 | Disponible vía OpenAI API (pricing variable) |
| Midjourney V8.1 | Subscripción $10-120/mes (UI only) |
| FLUX.2 Pro | $0.03/MP texto-a-imagen · $0.045/MP edición |
| Veo 3.1 | Gemini API / AI Studio / Vertex AI, app de Gemini y Flow |
| Gemini Omni Flash | App de Gemini, Flow, YouTube Shorts, Google Vids, AI Studio y Gemini API |
| Kling 3.0 | Créditos Kling: ~6/s a 720p sin audio · ~12/s a 1080p con audio · 30/s a 4K |
| Seedance 2.5 | BytePlus ModelArk (por tokens) · Jimeng / Doubao / Dreamina |
| Runway Gen-4.5 | $35/mes Pro (2,250 créditos) · $95/mes Unlimited |
| Hailuo 2.3 | $0.28/video |

## Decisión rápida (cuando el use case es obvio)

| Use case | Plataforma |
|----------|-----------|
| 4K image con multi-image fusion (5+ refs) | **Nano Banana Pro** |
| 4K image con texto largo multi-script | **GPT Image 2** |
| Image artística sin API | **Midjourney V8.1** |
| Image self-host on-prem | **FLUX.2 [dev]** |
| Image vector / SVG | **Recraft V4** (Tier 2) |
| Video ≤8s con audio nativo + 4K | **Veo 3.1** |
| Video ≤15s con Multi-Shot, voz atada al personaje o Motion Control | **Kling 3.0** |
| Video ≤30s con varios planos o muchas referencias (imágenes, vídeos, audios) | **Seedance 2.5** |
| Video ≤60s multi-escena manual Director Mode | **Runway Gen-4.5** |
| Video HDR cine | **Luma Ray 3.14** (Tier 2) |
| Video low-cost UGC volumen | **Hailuo 2.3** (Tier 2) |

## Casos límite que requieren router

- Video 9-15s narrativa (Kling 3.0 con Custom Multi-Shot vs Seedance 2.5 con tramos de tiempo)
- Image con brand identity Y texto largo (Nano Banana vs GPT Image 2)
- Video 30-60s con character consistency (Runway vs Seedance 2.5 con extensión vs Veo 3.1 encadenado)
- Video con la misma voz en varios clips (Kling 3.0 voz atada al element vs Seedance 2.5 audio de referencia)
- Producto que pide Sora 2 (Tier 3 → router decide alternativa)

En todos esos casos derivar a `platform-router`.

## Mantenimiento del cheatsheet

Revisar trimestralmente o tras anuncio de nueva versión Tier 1. Update sequence:

1. WebSearch del catálogo actual
2. Update `references/platforms-2026-05.md` (rename con fecha actualizada)
3. Update tablas resumen aquí en SKILL.md
4. Bump version del plugin si capabilities cambiaron significativamente
5. Sincronizar con `platform_specifications.md` del GEM hermano

---

**Detalle expandido por plataforma** → `references/platforms-2026-05.md`
