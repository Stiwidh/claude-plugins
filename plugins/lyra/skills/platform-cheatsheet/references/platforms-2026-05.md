# Platforms Catalog — Detailed Reference (mayo 2026)

**Snapshot:** 2026-05-18 · **vídeo Tier 1 re-verificado:** 2026-10-15
**Versión:** 2.1
**Fuente primaria:** WebSearch oficial 2026 + documentación de cada plataforma

> **Corrección 2026-10-15.** Las fichas de Kling 3.0 y Seedance 2.5 llevaban el nombre nuevo con
> los datos de Kling 2.6 y Seedance 2.0 (10s, cfg_scale, `[AUDIO: ...]`, 2K, variantes Fast/Pro,
> lip-sync "por fonemas"). Veo 3.1, Kling 3.0 y Seedance 2.5 llevan ahora dentro la fuente oficial
> y la fecha de verificación. Lo que no se ha podido verificar se dice. El resto de fichas
> (imagen, Runway, Tier 2) **no se ha re-verificado** en esta revisión.

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

**Verificado:** 15-oct-2026 contra `ai.google.dev/gemini-api/docs/veo`, `deepmind.google/models/veo/` y la guía oficial de prompting (`cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1`). No existe ningún "Veo 4".
**Model IDs:** `veo-3.1-generate-preview` · `veo-3.1-fast-generate-preview` · `veo-3.1-lite-generate-preview`

#### Capabilities
- Duración: **4, 6 u 8 segundos.** Obligatorio 8s con extensión, imágenes de referencia, 1080p o 4K
- Resolución: 720p · 1080p (solo a 8s) · 4K (solo a 8s, no en Lite). Con extensión de vídeo, solo 720p
- Aspect ratios: 16:9 (por defecto) y 9:16. **No hay 1:1 ni 4:5**
- **Audio nativo siempre activo**, no se desactiva: diálogo, SFX, ambiente y música
- **Hasta 3 imágenes de referencia** (obligan a duración 8s)
- Interpolación de primer y último frame
- Extensión de vídeo: +7s por extensión, hasta 20 veces (máx. 148s), solo 720p
- Varios planos dentro del clip con prompts por tramos de tiempo (`[00:00-00:02] ...`)
- Personas: en la UE solo `allow_adult`
- Sin parámetro de negative prompt en la Gemini API: las exclusiones se describen en el prompt
- Variante Lite: solo text-to-video e image-to-video, sin referencias ni extensión

#### Acceso
Gemini API, Google AI Studio y Vertex AI. También en la app de Gemini y en Flow.

#### Sintaxis del prompt
```
[Cinematografía] + [Sujeto] + [Acción] + [Contexto] + [Estilo y ambiente]
[El audio va en frases aparte, sin etiqueta "Audio:"]

Diálogo (entre comillas):
A woman says, "Bienvenida a mi marca."

SFX:
SFX: glass shattering on impact.

Ambiente:
Ambient noise: distant traffic, light rain on metal roof.

Música (frase natural):
A gentle orchestral score plays at low volume.

Varios planos dentro del clip (tramos de tiempo):
[00:00-00:03] Medium shot: ...
[00:03-00:06] Close-up: ...
[00:06-00:08] Wide shot: ...

Imágenes de referencia (máx. 3, obligan a duración 8s):
"Using the provided images for [personaje], create ..."
{
  "platform_specific": {
    "veo_3_1": {
      "duration_seconds": 8,
      "reference_images": ["https://...", "https://..."]
    }
  }
}
```

⚠️ Veo 3.1 no tiene "Director's Mode" ni storyboard aparte: los varios planos se dirigen por tramos dentro de los 8s. Para pasar de 8s, extender el clip (baja a 720p), encadenar con primer y último frame, o cambiar a Kling 3.0 (15s) o Seedance 2.5 (30s).

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
Pieza cinemática de hasta 8s con audio nativo de un solo paso, a 4K. Para más de 8s hay que extender el clip (baja a 720p) o cambiar de modelo.

---

### Kling 3.0 (Kuaishou)

- **Developer:** Kuaishou Technology
- **Modelos:** Kling VIDEO 3.0 · Kling VIDEO 3.0 Omni
- **4K nativo:** desde el 23-abr-2026 en la serie 3.0

**Verificado:** 15-oct-2026 contra `kling.ai/quickstart/klingai-video-3-model-user-guide`, `kling.ai/quickstart/klingai-video-3-omni-model-user-guide`, `kling.ai/blog/kling-ai-introduces-native-4k-video-model` y `kling.ai/blog/kling-4-vs-3`.

> **Kling 4.0** (anunciado el 30-sep-2026): hasta 30s nativos, hasta 10 keyframes, hasta 15 referencias combinadas, HDR 10-bit a 1080p y 4K. A 15-oct-2026 está en despliegue limitado (Kling 4.0 Flash en acceso anticipado desde el 28-sep) y el modelo completo "sale en octubre". **No se recomienda** hasta que esté disponible en la cuenta de quien genera: si la persona lo pide, se avisa y se ofrece Kling 3.0 o Seedance 2.5.

#### Capabilities
- Duración: **de 3 a 15s** por generación, a elegir
- Resolución: 720p · 1080p · **4K nativo**
- Aspect ratios: 16:9, 9:16 y 1:1 según la referencia de la API de kling.ai (no se ha podido leer la página entera: confirmarlo en la interfaz)
- **Audio nativo** (diálogo, SFX, ambiente, música) o sin audio, a elegir
- Diálogo en chino, inglés, japonés, coreano y español, con acentos y dialectos
- **Multi-Shot** (el modelo planifica los planos) y **Custom Multi-Shot** (número de planos y duración de cada uno)
- **Elements:** personaje fijo a partir de 2-4 imágenes desde varios ángulos, o de un vídeo de 3-8s
- **Voz atada al element:** audio limpio de una sola persona (la guía de Omni recomienda 5-30s); la voz se mantiene entre vídeos
- Omni: hasta 7 imágenes/elements sin vídeo, o hasta 4 con un vídeo de referencia
- Primer y último frame
- Diálogo de varios personajes con cada línea atribuida
- Motion Control como herramienta aparte

#### Parámetros de la API 3.0
| Parameter | Valores | Description |
|-----------|---------|-------------|
| `duration` | 3-15 | Segundos |
| `resolution` | 720p / 1080p / 4K | Según plan |
| `audio` | native / off | Audio nativo o vídeo mudo |
| `multi_shot` | true / false | Sin él, un solo plano aunque el prompt describa varios |

`cfg_scale`, `motion_intensity`, `voice_clone_ref` y la etiqueta `[AUDIO: ...]` eran de Kling 2.x y de algunos agregadores; **no aparecen en la documentación de 3.0**. No usarlos.

#### Coste (créditos Kling, guía oficial)
| Modo | Coste |
|------|-------|
| 720p sin audio | ~6 créditos/s (30 por 5s) |
| 1080p con audio nativo | ~12 créditos/s (60 por 5s) |
| Control de voz | +2 créditos/s |
| 4K | 30 créditos/s |

#### Sintaxis del prompt
```
[Subject] + [Action] + [Environment] + [Camera] + [Style]

Diálogo (personaje y tono entre paréntesis, sintaxis de la guía oficial):
Founder (warm, confident tone): Llevo dos meses con esto y recupero una hora al día.
Voiceover (calm female voice, Spanish from Spain): Así empieza tu mañana.

Resto del audio en frases separadas:
Sound effects: a soft cup clink near the end.
Ambient: busy cafe, distant chatter, espresso machine hiss.
Music: light lo-fi instrumental at very low volume.

Custom Multi-Shot (con Multi-Shot activo):
Shot 1 (4s): eye-level medium shot ...
Shot 2 (5s): slow dolly-in ...
Shot 3 (6s): close-up ...

Element con voz atada:
se crea una vez en Kling y se reutiliza; si ya tiene voz, no describir otra en el prompt.
```

#### `platform_specific.kling_3_0`
```json
{
  "model": "video_3_0 | video_3_0_omni",
  "audio": "native | off",
  "multi_shot": false,
  "custom_shots": [],
  "element": null,
  "voice_bound_to_element": false,
  "first_frame_ref": null,
  "last_frame_ref": null
}
```

#### Sweet spot
Piezas de 8 a 15s en una sola generación, a 1080p o 4K, con varios planos y con la voz del personaje coherente entre clips.

---

### Seedance 2.5 (ByteDance)

- **Developer:** ByteDance Seed
- **Publicado:** 31-jul-2026
- **API:** BytePlus ModelArk, model ID `dreamina-seedance-2-5-260628`. El anuncio del 31-jul la daba como "próximamente"; a 15-oct-2026 BytePlus la anuncia disponible para clientes

**Verificado:** 15-oct-2026 contra `seed.bytedance.com/en/seedance2_5`, `seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5`, `ai.byteplus.com/en/activity/seedance2-5` y el tutorial de ModelArk (`docs.byteplus.com/en/docs/ModelArk/2607688`).

#### Capabilities
- Duración: **de 4 a 30s** en una sola generación, o `-1` para que el modelo la decida; con extensiones sucesivas sobre el resultado (la página del modelo habla de extender dos veces; el blog, de "varias rondas")
- **Varios planos dentro de los 30s:** el modelo organiza planos conectados (planteamiento, desarrollo, giro, cierre)
- **Control por tramos de tiempo** en el prompt (`0-10s: ...`, `11-20s: ...`) y edición puntual posterior de personajes, acciones o tramos concretos
- **Referencias multimodales:** hasta **30 imágenes**, **10 vídeos** y **10 audios** en una sola pasada (50 en total, y como máximo 30s sumando los vídeos y audios), citados en el prompt como `@Image 1`, `@Video 1`...
- Audio y vídeo generados juntos (diálogo, efectos, ambiente); en la API se pide con `generate_audio`
- Más de 10 idiomas de forma nativa
- Resolución: **480p · 720p · 1080p** a 24 fps (1080p en 10 bits y H.265). Modo borrador (Draft) a 480p para validar antes del final. No hay 2K ni 4K en la documentación
- Aspect ratios: **16:9, 4:3, 1:1, 3:4, 9:16, 21:9** y `adaptive` (el modelo elige según el prompt y las referencias)

**No verificado en fuente oficial** (no afirmarlo): lip-sync "por fonemas" y variantes Fast / Standard / Pro de 2.5.

#### Acceso
Jimeng AI, Doubao y Dreamina; API en BytePlus ModelArk. En agregadores, comprobar qué versión ofrecen: a junio de 2026 Higgsfield listaba Seedance 2.0.

#### Sintaxis del prompt
```
[Descripción natural de la escena y del arco: el modelo organiza los planos]

Referencias citadas por número:
The woman from @Image 1 walks into the office from @Image 2 ...

Tramos de tiempo (sintaxis de los ejemplos oficiales):
0-10s: wide establishing, the woman from @Image 1 enters the office.
11-20s: close-up, she picks up a red apple.
21-30s: medium shot, she speaks to camera.

Audio en frases separadas:
A woman says, "..."
SFX: keyboard typing, soft pen tap on desk.
Ambient: open office, light conversation, climate hum.
Music: ambient electronic, low volume.

Extensión (sobre un resultado anterior):
Continue from the visuals and subjects in @Video 1 and generate another 30-second clip,
keeping the characters, scene, visual style and sound consistent.
```

#### `platform_specific.seedance_2_5`
```json
{
  "duration_sec": 30,
  "resolution": "480p | 720p | 1080p",
  "ratio": "16:9 | 4:3 | 1:1 | 3:4 | 9:16 | 21:9 | adaptive",
  "generate_audio": true,
  "image_refs": [],
  "video_refs": [],
  "audio_refs": [],
  "timestamped_segments": [],
  "extend_from": null
}
```

#### Sweet spot
**Narrativa de hasta 30s con varios planos y audio desde un solo prompt**, y piezas que necesitan muchas referencias (hasta 30 imágenes, 10 vídeos y 10 audios). Para más de 30s, extender sobre el resultado manteniendo personajes y escena.

---

### Runway Gen-4.5

- **Developer:** Runway
- **Lanzamiento:** Gen-4 mar-2025, Gen-4.5 dic-2025
- **Ranking:** #1 en Video Arena (dato de mayo 2026, sin re-verificar)

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
- **Lanzamiento:** feb-2026, integrado en CapCut desde mar-2026 (dato de mayo 2026). BytePlus ya anuncia "Dreamina Seedance 2.5"
- **Diferencia con Seedance 2.5 Tier 1:** Dreamina es la UI consumer (CapCut) con safety policy más estricta: no genera vídeo desde caras reales.
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
| Resolución máx | 4K (solo a 8s) | 4K nativo | 1080p (10 bits) | 4K |
| Duración máx por generación | 8s (extensión +7s en 720p) | 15s | 30s (+ extensiones) | 60s |
| Audio nativo | ✅ siempre activo | ✅ nativo u off | ✅ audio y vídeo juntos | ✅ |
| Varios planos en una generación | por tramos de tiempo dentro de 8s | **✅ Multi-Shot y Custom Multi-Shot** | **✅ planos organizados por el modelo + tramos** | Director Mode (manual) |
| Referencias | hasta 3 imágenes | elements de 2-4 imágenes (Omni: hasta 7) | **30 imgs + 10 vídeos + 10 audios** | Char ref |
| Voz del personaje desde audio | ❌ | ✅ voz atada al element | ✅ audios de referencia | Char reference |
| API oficial | ✅ | ✅ | ✅ BytePlus ModelArk | ✅ |
| Open weights | ❌ | ❌ | ❌ | ❌ |

Las columnas de Veo 3.1, Kling 3.0 y Seedance 2.5 están verificadas el 2026-10-15 (fuentes en cada ficha). La de Runway no se ha re-verificado.

---

**Próxima revisión:** cuando Kling 4.0 salga del despliegue limitado (anunciado para octubre de 2026) o tras anuncio de nueva versión Tier 1, lo que llegue antes.
