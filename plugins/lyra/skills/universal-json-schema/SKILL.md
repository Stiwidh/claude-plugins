---
name: universal-json-schema
description: JSON Schema universal v2.0 para prompts de generación de imagen y video — cross-platform, version-controllable, repeatable. Estructura canónica del plugin `lyra` que alimenta tanto el GEM hermano como el plugin Claude. Aplicar siempre que se diseñe un prompt nuevo o se refactorice uno existente.
user-invocable: true
argument-hint: "<image|video>"
allowed-tools:
  - Read
  - Write
  - Edit
---

# Skill — Universal JSON Schema v2.0

## Por qué JSON-first

- **Repeatability:** mismo JSON → output aproximadamente igual
- **Version control:** Git-trackable evolution
- **A/B testing:** modificar un campo (`lighting.type`), comparar
- **Programabilidad:** API integration directa con la plataforma destino
- **Cross-platform:** mismo JSON sirve para 7 plataformas Tier 1 con solo cambiar `meta.target_platform` + `platform_specific`

## El Schema completo v2.0

```json
{
  "meta": {
    "schema_version": "2.0",
    "generated_at": "[ISO8601 timestamp]",
    "content_type": "image | video",
    "target_platform": "nano_banana_pro | gpt_image_2 | midjourney_v81 | flux_2_pro | veo_3_1 | kling_3_0 | seedance_2_5 | runway_gen_45 | [tier2/3]",
    "final_use": "[caso de uso real: META Ad / Hero Web / Reels / etc.]",
    "deprecation_warning": "[STRING opcional — solo si target es Tier 3]"
  },
  "subject": {
    "main": "[descripción detallada del sujeto principal]",
    "secondary_elements": ["[prop 1]", "[prop 2]"],
    "character_consistency": {
      "reference_images": ["[url1]", "[url2]"],
      "specific_traits": "[features clave si es persona/personaje]"
    }
  },
  "action": {
    "primary_motion": "[video only — qué pasa]",
    "emotional_state": "[mood del sujeto]",
    "interaction": "[cómo interactúan los elementos]"
  },
  "environment": {
    "location": "[dónde]",
    "time_of_day": "[golden hour / night / morning / etc.]",
    "weather_atmosphere": "[mood ambiental]"
  },
  "visual_style": {
    "art_style": "Photorealistic | 3D Render | Cinematic | Illustration | Anime | Vector | [custom]",
    "color_palette": "[hex codes precisos si son distintivos, e.g. #13052D #9245FF]",
    "reference_artists": ["[Annie Leibovitz]", "[Wes Anderson]"],
    "mood": "[overall tone]"
  },
  "camera": {
    "angle": "Eye-level | Low-angle | High-angle | POV | Bird's-eye | Dutch angle | [custom]",
    "movement": "Static | Pan | Dolly | Crane | Zoom | Tracking | Orbit | [video only]",
    "lens": "Wide 24-28mm | Standard 50mm | Portrait 85mm | Telephoto 135mm+ | Macro | Fisheye",
    "depth_of_field": "Shallow | Medium | Deep | Rack-focus"
  },
  "lighting": {
    "type": "Natural | Studio | Cinematic | Dramatic | High-key | Low-key",
    "direction": "[front / camera-left / camera-right / back / top]",
    "intensity": "Low | Medium | High",
    "mood": "[warm morning / cinematic dramatic / cool editorial / etc.]"
  },
  "technical_params": {
    "aspect_ratio": "16:9 | 9:16 | 1:1 | 3:4 | 4:3 | 21:9 | 2:3 | 3:2 | [custom]",
    "resolution": "720p | 1080p | 2K | 4K",
    "duration_sec": 0,
    "fps": 30
  },
  "audio": {
    "required": false,
    "dialog": [
      {
        "character": "MAN | WOMAN | CHILD | NARRATOR",
        "text": "[exact words]"
      }
    ],
    "sound_effects": ["[sfx 1 con timing si aplica]"],
    "music_mood": "[tono musical o vacío]",
    "ambient": "[ambient sound description]"
  },
  "text_in_image": {
    "elements": [
      {
        "content": "[exact text]",
        "font": "[typeface name]",
        "size": "[pt o relative — '24pt' / 'large' / 'small']",
        "color": "[hex code]",
        "position": "[top-left / centered / bottom / etc.]"
      }
    ]
  },
  "negative_prompt": ["blurry", "low quality", "distorted proportions", "bad lighting", "amateur", "[context-specific]"],
  "platform_specific": {
    "nano_banana_pro": {
      "multi_image_fusion": false,
      "search_grounding": false,
      "thinking_mode": true
    },
    "gpt_image_2": {
      "reasoning": true,
      "multi_turn_edit": false
    },
    "midjourney_v81": {
      "sref": null,
      "cref": null,
      "hd": true,
      "quality": 4
    },
    "flux_2_pro": {
      "kontext_edit": false,
      "reference_count": 0
    },
    "veo_3_1": {
      "variant": "generate | fast | lite",
      "duration_seconds": "4 | 6 | 8 — obligatorio 8 con 1080p, 4k, extensión o referencias",
      "resolution": "720p | 1080p | 4k",
      "reference_images": "0-3 (no disponible en lite)",
      "video_extension": false,
      "first_last_frame": false
    },
    "gemini_omni_flash": {
      "task": "text_to_video | image_to_video | reference_to_video | edit",
      "source_video_uri": null,
      "delivery": "uri si el vídeo supera 4MB, si no base64",
      "audio_reference": "NO SOPORTADO"
    },
    "kling_3_0": {
      "model": "video_3_0 | video_3_0_omni",
      "audio": "native | off",
      "multi_shot": false,
      "custom_shots": [],
      "element": null,
      "voice_bound_to_element": false,
      "first_frame_ref": null,
      "last_frame_ref": null
    },
    "seedance_2_5": {
      "duration_sec": "4-30, o -1 para que decida el modelo",
      "resolution": "480p | 720p | 1080p",
      "ratio": "16:9 | 4:3 | 1:1 | 3:4 | 9:16 | 21:9 | adaptive",
      "generate_audio": true,
      "image_refs": "0-30",
      "video_refs": "0-10",
      "audio_refs": "0-10",
      "timestamped_segments": [],
      "extend_from": null
    },
    "runway_gen_45": {
      "motion_brush_zones": [],
      "camera_control": {"type": "static", "direction": null, "speed": 0},
      "director_mode": null
    }
  }
}
```

## Regla canónica del `platform_specific`

**Solo el bloque del `meta.target_platform` está rellenado.** Los demás bloques NO se incluyen en el JSON final. Esto evita confusión en el destino y mantiene el JSON limpio.

❌ JSON con los 7 bloques de `platform_specific` rellenados todos
✅ JSON solo con `platform_specific.veo_3_1` si `meta.target_platform = "veo_3_1"`

## Inferencia de defaults

Cuando el usuario no especifica un campo, aplicar defaults sensatos:

| Campo | Default |
|-------|---------|
| `visual_style.art_style` | "Photorealistic" |
| `technical_params.aspect_ratio` | "16:9" (más versátil) |
| `technical_params.resolution` | Max soportado por plataforma (4K en Nano Banana / GPT Image 2 / Veo 3.1 a 8s / Kling 3.0 / Runway; 2K en MJ; 1080p en Seedance 2.5) |
| `technical_params.duration_sec` (video) | 8 |
| `technical_params.fps` (video) | 24 para narrativa, 30 para social |
| `lighting.type` | "Natural" outdoor / "Studio" producto / "Cinematic" si mood lo pide |
| `negative_prompt` | Defaults canónicos: `["blurry", "low quality", "distorted proportions", "bad lighting", "amateur"]` |

## Validación de campos mandatory

Antes de declarar un JSON como entregable, validar que están todos:

- `meta.schema_version` = "2.0"
- `meta.content_type`
- `meta.target_platform`
- `meta.final_use`
- `subject.main`
- `environment.location`
- `visual_style.art_style`
- `camera.angle`
- `lighting.type`
- `technical_params.aspect_ratio`
- `technical_params.resolution`
- `negative_prompt` (array no vacío)
- `platform_specific.[target]` (el bloque correspondiente)

Si video → adicionalmente:
- `action.primary_motion`
- `technical_params.duration_sec`
- `technical_params.fps`

Si tiene texto → adicionalmente:
- `text_in_image.elements[]` poblado

## Workflow

1. **Detectar content_type:** ¿image o video?
2. **Decidir target_platform** (o derivar al `platform-router` si dudoso)
3. **Rellenar todos los campos mandatory** con datos del usuario + defaults
4. **Rellenar campos opcionales relevantes** (audio si video, text_in_image si aplica)
5. **Rellenar solo el bloque platform_specific del target**
6. **Validar contra el checklist de mandatory**
7. **Entregar JSON listo**

## Cambios v1.0 → v2.0

- `meta.schema_version` añadido (versioning explícito)
- `meta.deprecation_warning` añadido (Tier 3 awareness)
- `text_in_image.elements` formalizado como array de objetos estructurados
- `platform_specific` ampliado a 7 plataformas Tier 1
- `audio.dialog` ahora es array de objetos `{character, text}` en vez de array de strings
- `audio.ambient` añadido como campo separado de `sound_effects`
- `camera.angle` y `camera.lens` con valores enumerados ampliados

---

**Skill canónica del plugin `lyra` — versión 2.0 alineada con GEM hermano.**
