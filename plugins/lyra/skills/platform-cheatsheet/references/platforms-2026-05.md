# Platforms Catalog — Detailed Reference (mayo 2026)

**Snapshot:** 2026-05-18
**Versión:** 2.0
**Fuente primaria:** WebSearch oficial 2026 + documentación de cada plataforma

Detalle expandido del catálogo. La SKILL.md tiene la tabla resumen — este archivo es la enciclopedia.

---

## 🎨 IMAGEN

### Nano Banana Pro (Gemini 3 Pro Image)

- **Developer:** Google DeepMind
- **Versión actual:** Gemini 3 Pro Image
- **Variante rápida:** Nano Banana 2 (Gemini 3.1 Flash Image) — 512px–4K, velocidad Flash

#### Capabilities
- Resolución: 1K / 2K / 4K (4096×4096) nativo
- Aspect ratios: 1:1, 2:3, 3:2, 3:4, 4:3, 9:16, 16:9, 21:9
- Text rendering: 92% accuracy multi-idioma (latín, CJK, hindi)
- Multi-image fusion: hasta **14 imágenes** / **5 sujetos consistentes**
- Real-world grounding via Google Search (datos verificables en infografías)
- "Thinking" mode: planifica composición antes de renderizar
- Multi-turn editing limitado

#### Pricing
| Resolución | Per image | Batch API (-50%) |
|------------|-----------|------------------|
| 2K | $0.134 | — |
| 4K | $0.24 | $0.12 |

#### Sintaxis del prompt
```
[Subject + scene description] + [Composition / camera] + [Lighting] + [Style + mood] + [Text elements] + [Technical specs]

Texto literal:
Include legible text: "EXACT TEXT" in [Font] typeface, [Size]pt, [Color hex], [Position]

Color preciso (siempre hex):
Deep purple background (#13052D), vibrant magenta accents (#9245FF), neutral grays (#A09FA0)
```

#### `platform_specific.nano_banana_pro`
```json
{
  "multi_image_fusion": false,
  "search_grounding": false,
  "thinking_mode": true
}
```

#### Sweet spot
Identidad de marca consistente · infografías con texto · hero shots comerciales con tipografía precisa · packaging.

---

### GPT Image 2 (OpenAI)

- **Developer:** OpenAI
- **Lanzamiento:** 21-abr-2026
- **Sustituye:** DALL-E 2 y DALL-E 3 (Tier 3 deprecated 12-may-2026)

#### Capabilities
- Resolución: 4K (4096×4096) nativo
- Aspect ratios: 3:1 a 1:3 (todos los intermedios)
- Text rendering: **~99% accuracy multi-script** (latín, CJK, hindi, bengali) — **mejor del mercado para texto largo**
- Multi-image: hasta 8 imágenes coherentes
- **Reasoning nativo:** "piensa" antes de generar, puede buscar referencia en web, self-check
- Edición multi-turn conversacional sobre la misma imagen

#### Sintaxis del prompt
```
[Descripción natural detallada con reasoning cues]

"Diseña un poster para [evento]. Considera:
- Tipografía legible a 5 metros
- Jerarquía visual con CTA destacado
- Paleta corporativa [#hex]
- Subtítulo exacto: '[TEXTO]' en [Font]

Verifica que [restricción] antes de finalizar."

Multi-turn edit (segunda llamada):
"Sobre la imagen anterior, cambia solo [campo]. Mantén el resto idéntico."
```

#### `platform_specific.gpt_image_2`
```json
{
  "reasoning": true,
  "multi_turn_edit": false
}
```

#### Sweet spot
Posters con texto largo · edición conversacional iterativa · control estilístico fino · multi-script (chino + inglés + árabe en una sola imagen).

---

### Midjourney V8.1

- **Developer:** Midjourney
- **Versión actual:** V8 (17-mar-2026), V8.1 Alpha (14-abr-2026)
- **API:** ❌ No tiene API oficial. Solo web/Discord.

#### Capabilities
- Resolución: 2K nativo con `--hd`, `--q 4` para coherencia extra
- 5× más rápido que V7
- Image prompts: sí (V8.1 con image weights ajustables)
- Reference syntax: `--sref` (style), `--cref` (character), Omni Reference (`--oref`), Moodboards
- Draft Mode: 10× más rápido para iteración (`--draft`)

#### Sintaxis del prompt
```
[Subject + scene description] --ar [ratio] --hd --q 4 [--sref URL] [--cref URL] [--no negative1, negative2]

Texto literal: comillas inline → "EXACT TEXT"

Style reference (mantener look ajeno):
[prompt] --sref https://midjourney.com/styles/[style]

Character reference (mismo personaje):
[prompt] --cref https://midjourney.com/refs/[char]

Omni Reference (estilo + character + objeto):
[prompt] --oref https://midjourney.com/refs/[ref]
```

#### `platform_specific.midjourney_v81`
```json
{
  "sref": null,
  "cref": null,
  "hd": true,
  "quality": 4
}
```

#### Sweet spot
Dirección artística autoral · fotografía editorial estilizada · ilustración con voz propia. **No usar para pipelines programáticos** (sin API).

---

### FLUX.2 Pro (Black Forest Labs)

- **Developer:** Black Forest Labs
- **Versión actual:** FLUX 2 Pro (nov-2025)
- **Variantes:** `[pro]` cloud · `[dev]` open weights · `[flex]` · `[klein]` sub-segundo (16-ene-2026)

#### Capabilities
- Resolución: hasta 4 MP (~2K+)
- Multi-reference: hasta **8 imágenes**
- **Typography engine** multi-line de calidad production
- **Kontext Engine:** edición en lenguaje natural sobre imagen existente
- Open weights `[dev]` disponibles — único Tier 1 self-hostable

#### Pricing
| Operación | Coste |
|-----------|-------|
| Texto a imagen | $0.03 / MP |
| Edición | $0.045 / MP |

#### Acceso
API: BFL directo · OpenRouter · fal.ai · Cloudflare Workers AI

#### Sintaxis del prompt
```
[Descripción natural densa]

Multi-line typography:
"Three-line layout:
Line 1: 'TEXT 1' in [Font] [Weight], color [hex]
Line 2: 'TEXT 2' in [Font] [Weight], color [hex]
Line 3: 'TEXT 3' in [Font] [Weight], color [hex]"

Kontext editing (edición natural sobre imagen existente):
"En la imagen ref, cambia [campo] a [valor], mantén el resto idéntico."

Reference stacking (hasta 8 imágenes con weights):
{
  "references": [
    {"url": "...", "weight": 0.8, "type": "style"},
    {"url": "...", "weight": 0.6, "type": "character"}
  ]
}
```

#### `platform_specific.flux_2_pro`
```json
{
  "kontext_edit": false,
  "reference_count": 0
}
```

#### Sweet spot
Producción profesional con identidad de personaje persistente · fotografía de producto · pipelines self-hosted con `[dev]` · edición conversacional con Kontext.

---

### Ideogram V3 (Tier 2)

- **Tiers:** Turbo (2 créditos, ~8s) · Default (4 créditos, ~10s) · Quality
- **Sweet spot:** Logos · posters · infografías · headlines legibles. Mejor text rendering para tipografía pura.
- **Resolución máxima:** No confirmado al 2026-05 (≥2K probable)

### Recraft V4 (Tier 2)

- **Ranking:** #1 en Text-to-Image Arena (HuggingFace) sobre Midjourney V8 y DALL-E 3
- **Sweet spot único:** **Único modelo que exporta SVG real production-quality** (no raster). Vector graphics, logos, ilustración editorial vectorial, brand assets.

### Stable Diffusion 4 Ultra (Tier 2)

- **Acceso:** Open weights (community license) + API
- **Sweet spot:** Fine-tuning on-prem, workflows ComfyUI custom, LoRAs

### Wan 2.7 Image (Tier 2)

- **Developer:** Alibaba
- **Sweet spot:** Pipelines self-hosted, open source, integración con Wan 2.7 Video para coherencia cross-modal. Thinking Mode previo a generación.

---

## 🎬 VIDEO

### Veo 3.1 (Google)

- **Developer:** Google DeepMind
- **Variantes:** Veo 3.1 · Veo 3.1 Fast · Veo 3.1 Lite

**Verificado:** 5-ago-2026 contra `ai.google.dev/gemini-api/docs/veo` y `deepmind.google/models/veo/`
**Model IDs:** `veo-3.1-generate-preview` · `veo-3.1-fast-generate-preview` · `veo-3.1-lite-generate-preview`

#### Capabilities
- Duración: **4, 6 u 8 segundos.** Obligatorio 8s con extensión, imágenes de referencia, 1080p o 4K
- Resolución: 720p · 1080p (solo a 8s) · 4K (solo a 8s). Con extensión de vídeo, solo 720p
- Aspect ratios: 16:9 (por defecto) y 9:16. **No hay 1:1**
- **Audio nativo siempre activo**, no se desactiva: diálogo, SFX y ambiente
- **Hasta 3 imágenes de referencia** (obligan a duración 8s)
- Extensión de vídeo e interpolación de primer y último frame
- Variante Lite: solo text-to-video e image-to-video, sin referencias ni extensión

#### Acceso
Gemini API, Google AI Studio y Vertex AI. También en la app de Gemini y en Flow.

#### Sintaxis del prompt
```
[Camera move + lens]: [Subject] [Action], in [Setting + atmosphere], lit by [Light source].
Style: [Texture + color grading].
[El audio va en frases aparte, sin etiqueta "Audio:"]

Diálogo (entre comillas):
A woman says, "Bienvenida a mi marca."

SFX:
SFX: glass shattering on impact.

Ambiente:
Ambient noise: distant traffic, light rain on metal roof.

⚠️ Veo 3.1 NO tiene multi-shot ni "Director's Mode". Para varios planos en una
generación, el modelo es Kling 3.0 (Custom Multi-Shot). Aquí solo se puede
extender el clip, y al extender baja a 720p.

Imágenes de referencia (máx. 3, obligan a duración 8s):
{
  "platform_specific": {
    "veo_3_1": {
      "duration_seconds": 8,
      "reference_images": ["https://...", "https://..."]
    }
  }
}
```

#### `platform_specific.veo_3_1`
```json
{
  "variant": "generate | fast | lite",
  "duration_seconds": 8,
  "resolution": "720p | 1080p | 4k",
  "reference_images": [],
  "video_extension": false,
  "first_last_frame": false
}
```

#### Sweet spot
Pieza cinemática de hasta 8s con audio nativo de un solo paso. Para más de 8s hay que extender el clip (baja a 720p) o cambiar de modelo.

---

### Kling 3.0 (Kuaishou)

- **Developer:** Kuaishou Technology
- **Lanzamiento:** 3-dic-2025
- **Sucesor:** Kling 3.0 referenciado en agregadores (Higgsfield) — 2.6 sigue deploy de referencia documentado

#### Capabilities
- Resolución: 1080p @ 48 fps (4K upscale post)
- Duración: 10s por clip (extensible a 3 min con chaining first/last frame)
- **Audio nativo single-pass:** voz + SFX + ambiente + música simultáneo
- **Voice Control:** clonado de voz desde upload
- Elements: hasta 4 imágenes ref para consistencia
- First/last frame chaining

#### Parámetros críticos
| Parameter | Type | Range | Description |
|-----------|------|-------|-------------|
| `cfgScale` | float | 1.0 - 20.0 | Prompt adherence (7.5 recomendado) |
| `motion_type` | enum | slow / medium / fast | Intensidad de movimiento |
| `camera_control` | enum | static / pan / zoom / tracking | Cinematic camera |

#### Sintaxis del prompt
```
[Subject] + [Action] + [Environment] + [Camera + fps] + [Style] + [Audio cue]

Audio (bracket syntax):
[AUDIO: Heavy rain on pavement, distant thunder, approaching footsteps, zippo lighter click]

Camera + FPS:
"Low-angle tracking shot following subject from behind, 48fps cinematic motion"

CFG scale:
- 1.0-5.0: Creative, loose
- 5.0-10.0: Balanced (default 7.5)
- 10.0-20.0: Strict adherence

Voice cloning:
"voice_clone_ref": "https://corvere.com/voices/founder.mp3"

Elements (4 refs character consistency):
"elements_refs": ["url1", "url2", "url3", "url4"]

First/last frame chaining (>10s):
Clip 1 termina con frame B → Clip 2 empieza con frame B
```

#### `platform_specific.kling_3_0`
```json
{
  "cfg_scale": 7.5,
  "motion_intensity": "medium",
  "voice_clone_ref": null,
  "first_frame_ref": null
}
```

#### Sweet spot
Clips con audio sincronizado coste-eficiente · diálogo en mandarín o inglés · long-form (>8s) cuando Veo 3.1 no es accesible.

---

### Seedance 2.5 (ByteDance)

- **Developer:** ByteDance
- **Lanzamiento:** feb-2026 API pública, variantes Fast / Standard / Pro

#### Capabilities
- Duración: hasta **30s** en una generación, extensible dos veces más
- Resolución: 480p · 720p · **2K nativo** (+30% speed boost en 2K)
- Aspect ratios: **21:9, 16:9, 4:3, 1:1, 3:4, 9:16** (los 6 principales)
- **Audio-video unified architecture:** el modelo "oye" mientras genera — natural reverb, proximity effects para dialog
- **Lip-sync phoneme-level:** mejor del mercado según benchmarks 2026 (supera Veo 3.1)
- **Multi-shot storyboard automático nativo:** un solo prompt → modelo decompone en shots con coherencia personajes/escenas. Feature signature única
- **Multimodal input nativo:** Text + hasta **30 imágenes** + **10 vídeos** + **10 audios** de referencia en una sola pasada
- Multilingual performance: líder en consistencia cross-language vs Sora 2, Veo 3.1, Kling 3.0

#### Variantes
| Variante | Use case |
|----------|----------|
| Seedance 2.5 Fast | Iteración / prototipado / volumen |
| Seedance 2.5 Standard | Default — balance calidad/coste |
| Seedance 2.5 Pro | Producción premium — máxima calidad multi-shot + audio |

#### Acceso
API pública: Replicate · fal.ai · Atlas Cloud · BytePlus · Apiyi

#### Sintaxis del prompt
```
[Scene description natural — el modelo auto-storyboards los shots]

Audio sincronizado (unified architecture):
A founder says, "We just shipped v2."
SFX: keyboard typing, soft pen tap on desk.
Ambient: open office — light conversation, climate hum.
Music: ambient electronic, low volume.

Shot breakdown manual (override auto-storyboard):
"Generate with 3 shots:
Shot 1 (4s): wide establishing — founder at desk
Shot 2 (5s): close-up reaction
Shot 3 (6s): medium with dialog"

Multimodal references:
image_refs: [URL1, ..., URL9]  (consistencia personaje + estética)
video_refs: [URL1, ..., URL3]  (consistencia movement/style)
audio_refs: [URL1, ..., URL3]  (voice clone, music style)

Duration auto: duration_sec = -1 → modelo decide óptimo
```

#### `platform_specific.seedance_2_5`
```json
{
  "variant": "standard",
  "auto_storyboard": true,
  "shot_breakdown": null,
  "image_refs": [],
  "video_refs": [],
  "audio_refs": [],
  "duration_auto": false
}
```

#### Sweet spot
**Narrativa multi-shot con audio sincronizado profesional desde un solo prompt.** Mejor que Runway Gen-4.5 para narrativa ≤15s (sin Director Mode manual). Mejor que Veo 3.1 en lip-sync (phoneme-level). Mejor que Kling 3.0 en multi-shot automático. Multimodal input nativo (30 imgs + 10 videos + 10 audios) = único en el mercado a mayo 2026.

---

### Runway Gen-4.5

- **Developer:** Runway
- **Lanzamiento:** Gen-4 mar-2025, Gen-4.5 dic-2025
- **Ranking:** #1 en Video Arena vs Veo 3.1 y Kling 3.0 (a mayo 2026)

#### Capabilities
- Duración: hasta **60 segundos**
- Resolución: 4K
- Temporal consistency: personajes coherentes en piezas largas
- **Motion Brush:** pintar movimiento sobre zonas específicas
- **Camera Control:** zoom / pan / dolly / arc con valores numéricos
- Green Screen integrado
- **Director Mode:** multi-escena con transiciones controladas

#### Pricing
| Plan | Coste mensual | Créditos |
|------|---------------|----------|
| Pro | $35 | 2,250 |
| Unlimited | $95 | Ilimitado |

#### Multi-model marketplace
Runway es ahora marketplace multi-modelo: la suscripción incluye VEO + Kling + Seedance + FLUX + Seedream en una sola UI. Útil para clientes que quieren un solo workflow.

#### Sintaxis del prompt
```
[Subject + scene] + [Style direction]

Camera control numérico:
camera_control: {
  type: "dolly",
  direction: "forward",
  speed: 0.5,
  duration_sec: 4
}

Motion Brush (pintar movimiento en zonas):
motion_brush_zones: [
  {"zone": "subject_face", "motion": "subtle smile", "intensity": 0.3},
  {"zone": "background_clouds", "motion": "drift right", "intensity": 0.5}
]

Director Mode (multi-escena):
{
  "scenes": [
    {"shot": "wide_establishing", "duration": 8, "characters": ["founder"]},
    {"shot": "medium_dialog", "duration": 12, "characters": ["founder", "client"]},
    {"shot": "close_up_reaction", "duration": 6, "characters": ["client"]},
    {"shot": "wide_resolution", "duration": 8, "characters": ["founder", "client"]}
  ]
}
```

#### `platform_specific.runway_gen_45`
```json
{
  "motion_brush_zones": [],
  "camera_control": {"type": "static", "direction": null, "speed": 0},
  "director_mode": null
}
```

#### Sweet spot
Workflow profesional multi-escena con personajes consistentes y control de cámara fino. Cliente que quiere "una sola plataforma para todo".

---

### Luma Ray 3.14 (Tier 2)

- **Developer:** Luma Labs
- **Lanzamiento:** Ray 3 mar-2026, Ray 3.14 con HDR
- **Diferenciador único:** Primer modelo con HDR studio-grade nativo (export 16-bit EXR)
- **Sweet spot:** Post-pro híbrida con actor real (Ray 3 Modify enhance preservando timing/eyeline/emoción), color grading HDR para pipelines de cine.

### Pika 2.5 (Tier 2)

- **Capabilities:** Camera direction first-class, scene extension 15s nativo + 25s con Pikaframes, prompt adherence multi-sujeto
- **Sweet spot:** Short-form social UGC, iteración creativa rápida

### MiniMax Hailuo 2.3 (Tier 2)

- **Developer:** MiniMax
- **Pricing:** $0.28 / video
- **Resolución:** 1080p
- **Estilos:** anime, ilustración, ink painting, game CG
- **Sweet spot:** Volumen alto a coste bajo (UGC, ads paid, A/B testing creativo)

### Dreamina (wrapper consumer de Seedance 2.5) (Tier 2)

- **Developer:** ByteDance
- **Lanzamiento:** feb-2026, integrado en CapCut desde mar-2026
- **Diferencia con Seedance 2.5 Tier 1:** Dreamina es la UI consumer (CapCut) con safety policy más estricta — no genera vídeo desde caras reales.
- **Sweet spot:** Content social vertical (tutorial / recipe / fitness), integración nativa con edición CapCut. Si cliente edita en CapCut sin caras reales → Dreamina. Si requiere API + caras reales + control fino → **Seedance 2.5 Tier 1 directo**.

### Wan 2.7 Video (Tier 2)

- **Developer:** Alibaba
- **Suite:** `t2v` + `i2v` + `r2v` + `videoedit`
- **Sweet spot:** Deployment on-prem, edición video-a-video, lip-sync nativo si das audio, control endpoint exacto.

---

## ⚠️ TIER 3 — Deprecated / EOL

### Sora 2 / Sora 2 Pro (OpenAI)

- **Estado:** API discontinúa **24-sep-2026**. Web/app cerrados 26-abr-2026.
- **Feature signature:** Character Cameos (insertar persona real desde clip de referencia con lip-sync), 25s/60s duration
- **Pricing API:** $0.10/s @ 720p base, $0.30/s @ 720p Pro, $0.50/s @ 1080p Pro
- **Alternativa Tier 1:** Veo 3.1 (audio nativo, hasta 4K, 8s) o Runway Gen-4.5 (60s, character cameos vía cref)
- **Acción del prompt engineer:** advertir antes de generar con `meta.deprecation_warning`

### DALL-E 2 / DALL-E 3 (OpenAI)

- **Estado:** Deprecated 12-may-2026
- **Reemplazo directo:** GPT Image 2 (~99% text accuracy)
- **Acción:** redirigir sin excepción a GPT Image 2

> **Veo 3.1 ya no está en Tier 3.** Estaba aquí como "legacy" por debajo de un "VEO 4" que no
> existe. Veo 3.1 es el modelo de vídeo vigente de Google y vive en Tier 1.

---

## 📊 Matriz de comparación

### Imagen
| Capability | Nano Banana Pro | GPT Image 2 | MJ V8.1 | FLUX.2 Pro |
|------------|:--:|:--:|:--:|:--:|
| Resolución máx | 4K | 4K | 2K | 4 MP |
| Texto en imagen | 92% | 99% multi-script | Sí, comillas | Sí multi-línea |
| API oficial | ✅ | ✅ | ❌ | ✅ |
| Multi-image ref | 14 | 8 | Sí | 8 |
| Character consistency | ✅ | ✅ | ✅ cref | ✅ |
| Open weights | ❌ | ❌ | ❌ | ✅ [dev] |

### Video
| Capability | Veo 3.1 | Kling 3.0 | Seedance 2.5 | Runway Gen-4.5 |
|------------|:--:|:--:|:--:|:--:|
| Resolución máx | 4K | 1080p (4K up) | 2K | 4K |
| Duración máx | 8s | 10s | 15s | 60s |
| Audio nativo | ✅ siempre activo | ✅ Single-pass | ✅ Unified architecture | ✅ |
| Lip-sync accuracy | preciso | Bueno | **Phoneme-level (líder)** | Bueno |
| Multi-shot auto | ❌ (solo extensión de clip) | **✅ Custom Multi-Shot nativo** | **✅ Auto-storyboard nativo** | Director Mode (manual) |
| Multimodal input | Avatar ref | Elements (4 imgs) | **30 imgs + 10 videos + 10 audios** | Char ref |
| Voice clone | Imágenes de referencia (máx. 3) | ✅ Audio upload | ✅ Audio ref | Char reference |
| API oficial | ✅ | ✅ | ✅ | ✅ |
| Open weights | ❌ | ❌ | ❌ | ❌ |

---

**Próxima revisión:** 2026-08-18 o tras anuncio de nueva versión Tier 1 (whichever first)
