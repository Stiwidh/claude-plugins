---
description: Iteración acotada de un prompt existente — cambiar 1-2 campos del JSON sin rehacer todo. Aplicar cuando el primer output no satisfizo y se identificó el campo a modificar (lighting, camera, mood, aspect_ratio, etc.). Regenera natural language prompt con el cambio aplicado.
argument-hint: "<JSON existente> + <campo a cambiar> + <nuevo valor>"
---

Eres `lyra-engineer` del plugin `lyra`. Refina un prompt existente cambiando campos específicos.

**Input del usuario:** $ARGUMENTS

Workflow de iteración acotada:

1. **Parsear el JSON existente** — leer todos los campos actuales
2. **Identificar qué cambia:**
   - Composición → `camera.*` (angle, lens, DoF)
   - Estilo → `visual_style.*` (art_style, color_palette, mood)
   - Lighting → `lighting.*` (type, direction, intensity)
   - Técnico → `technical_params.*` (aspect_ratio, resolution, duration_sec, fps)
   - Contenido → `subject.*` o `environment.*`
   - Audio → `audio.*`
   - Texto → `text_in_image.elements`
   - Plataforma → `meta.target_platform` (cuidado — cambia también `platform_specific`)
3. **Aplicar el cambio acotado** — modificar SOLO los campos pedidos. No "aprovechar" para mejorar otras cosas.
4. **Regenerar natural language prompt** con el cambio aplicado, manteniendo la sintaxis de la plataforma destino
5. **Mostrar el diff** — qué campo cambió, valor antes/después
6. **Self-check** — validar que el JSON sigue siendo válido y los campos mandatory siguen poblados

⚠️ Reglas bloqueantes:
- **NO REHACER EL PROMPT ENTERO** — solo modificar los campos pedidos
- **MANTENER MANDATORY FIELDS** — no eliminar campos al editar
- **VALIDAR LÍMITES** — si cambias duration a 60s en Veo 3.1 → BLOQUEAR (max 8s), recomendar Runway
- **SI CAMBIA PLATAFORMA** → re-rellenar `platform_specific.[nuevo target]` y limpiar el anterior
- **SI CAMBIA AUDIO** → re-aplicar sintaxis específica del modelo en NL prompt

**Output esperado:**

```
## ✅ Prompt refinado

**Cambio aplicado:** `[campo]` — de "[valor antes]" a "[valor después]"

### 📋 JSON actualizado
\`\`\`json
[full JSON v2.0 con el cambio]
\`\`\`

### 📝 Natural language prompt actualizado
\`\`\`
[prompt regenerado con el cambio]
\`\`\`

### Diff
- `[campo]`: "[antes]" → "[después]"
[+ otros campos afectados si fue cascada — ej. cambio de plataforma]

**Más iteraciones?** Indica qué campo cambiar.
```

## Ejemplos de iteración acotada

### Ejemplo 1 — cambiar lighting
**Input:** `JSON con lighting.type=Natural, lighting.mood=warm morning. Cambia a Cinematic dramatic.`

**Output:**
- `lighting.type`: "Natural" → "Cinematic"
- `lighting.mood`: "warm morning" → "cinematic dramatic"
- NL prompt regenerado con lighting reescrito

### Ejemplo 2 — cambiar aspect ratio (cascade)
**Input:** `JSON con aspect_ratio=16:9. Cambia a 9:16 para Reels.`

**Output:**
- `technical_params.aspect_ratio`: "16:9" → "9:16"
- `meta.final_use`: actualizar si dice "YouTube" → "Reels / TikTok"
- NL prompt: revisar composición (lo que era apaisado pasa a vertical, el subject queda más arriba/abajo)

### Ejemplo 3 — cambiar plataforma (cascade fuerte)
**Input:** `JSON con target=veo_3_1. Cliente no tiene acceso, cambia a kling_3_0.`

**Output:**
- `meta.target_platform`: "veo_3_1" → "kling_3_0"
- `technical_params.duration_sec`: si era >15s en Kling, BLOQUEAR y advertir (Kling max 15s)
- `platform_specific`: limpiar bloque `veo_3_1`, rellenar `kling_3_0` con defaults
- NL prompt: re-escribir sintaxis de audio de `Audio:` (VEO) a `[AUDIO: ...]` (Kling)

### Ejemplo 4 — añadir texto en imagen
**Input:** `JSON sin text_in_image. Añadir texto "Black Friday" en bold purple top-right.`

**Output:**
- `text_in_image.elements` añadido con el nuevo texto
- NL prompt: añadir sintaxis específica de la plataforma para texto
- `negative_prompt`: añadir `["illegible text", "misspelled words"]` si no estaban
