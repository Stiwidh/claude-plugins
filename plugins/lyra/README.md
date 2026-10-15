# Plugin `lyra` — Lyra by Corvere Solutions

Plugin de Claude Code que cubre el dominio **prompt engineering para generación de imagen y video** con las 8 plataformas Tier 1 vigentes a mayo 2026.

**Hermano del GEM** [Lyra GEM](../../GEMINI/Lyra/) — mismo dominio, distinto vehículo. Ambos comparten JSON Schema universal y best practices.

Producto cliente vendible — pensado para equipos creativos que quieren prompts production-ready sin invertir tiempo en research por plataforma.

---

## 🗺️ Estructura

```
lyra/
├── .claude-plugin/plugin.json
├── README.md
├── agents/                              (4 sub-agents)
│   ├── lyra-engineer.md        ← CREADOR PRINCIPAL (Opus)
│   ├── platform-router.md               ← ESPECIALISTA (Sonnet)
│   ├── reference-image-analyzer.md      ← ESPECIALISTA (Sonnet)
│   └── visual-prompt-auditor.md         ← AUDITOR (Sonnet)
├── skills/                              (6 skills atómicas)
│   ├── universal-json-schema/SKILL.md
│   ├── platform-cheatsheet/
│   │   ├── SKILL.md
│   │   └── references/platforms-2026-05.md
│   ├── negative-prompt-library/SKILL.md
│   ├── cot-multi-element-scene/SKILL.md
│   ├── text-rendering-pattern/SKILL.md
│   └── audio-cue-syntax/SKILL.md
└── commands/                            (4 slash commands)
    ├── image.md       (/lyra:image)
    ├── video.md       (/lyra:video)
    ├── audit.md       (/lyra:audit)
    └── refine.md      (/lyra:refine)
```

---

## 🤖 Sub-agents

### Creador principal (1)

| Agent | Rol | Cuándo se invoca |
|-------|-----|------------------|
| `lyra-engineer` | **CREADOR PRINCIPAL** | Diseñar prompts production-grade para imagen / video. Razona sobre target platform, JSON schema, sintaxis específica, character consistency, audio layering, deprecation paths. NO solo "aplica templates". |

### Especialistas (2)

| Agent | Rol | Cuándo |
|-------|-----|--------|
| `platform-router` | DECISIÓN DE PLATAFORMA | Elegir el modelo óptimo entre las 7 plataformas Tier 1 (mayo 2026) según use case, requisitos técnicos, presupuesto y deprecation status. Decision tree explícito. |
| `reference-image-analyzer` | EXTRACCIÓN DE BASELINE | Cuando el usuario aporta imagen de referencia. Analiza composición, lighting, paleta de color (hex codes), depth of field, cámara inferida, mood. Devuelve baseline aesthetic estructurado. |

### Auditor (1)

| Agent | Rol | Cuándo |
|-------|-----|--------|
| `visual-prompt-auditor` | PRE-FLIGHT REVIEW | Read-only review antes de enviar prompt a generación. Detecta vague terms, conflicting instructions, platform mismatch, negative prompt ausente, deprecation warnings faltantes, aspect ratio incoherente con use case. |

**Patrón de roles** (alineado con plugins canónicos Corvere `aiml`, `typescript`, `retell`): 1 creador principal + 2 especialistas + 1 auditor.

---

## 🛠️ Skills atómicas

| Skill | Propósito | Tipo |
|-------|-----------|------|
| `universal-json-schema` | JSON Schema v2.0 cross-platform — la fundación de cualquier prompt estructurado | Patrón |
| `platform-cheatsheet` | Cobertura completa Tier 1/2/3 mayo 2026 con sintaxis por plataforma + `references/platforms-2026-05.md` | Patrón |
| `negative-prompt-library` | Negative prompts canónicos por use case (personas, producto, video cinemático, texto, brand, arquitectura, comida) | Patrón |
| `cot-multi-element-scene` | Chain-of-Thought espacial (foreground / mid-ground / background) para escenas complejas | Técnica |
| `text-rendering-pattern` | Sintaxis exacta para incluir texto literal en imagen — Nano Banana, GPT Image 2, FLUX.2, Midjourney | Patrón |
| `audio-cue-syntax` | Sintaxis canónica de audio por plataforma video: Veo 3.1 y Seedance 2.5 (diálogo entre comillas + `SFX:`), Kling 3.0 (`Personaje (tono): línea` + voz atada al element), Runway (audio en director mode) | Patrón |

---

## ⚡ Slash commands

| Command | Atajo a | Sub-agent responsable |
|---------|---------|------------------------|
| `/lyra:image <descripción>` | Wizard imagen → JSON + natural language | `lyra-engineer` |
| `/lyra:video <descripción>` | Wizard video → JSON + natural language | `lyra-engineer` |
| `/lyra:audit <prompt>` | Audit pre-generación read-only | `visual-prompt-auditor` |
| `/lyra:refine <json>` | Iteración acotada (cambiar 1-2 campos) | `lyra-engineer` |

---

## 🎯 Cobertura de plataformas (mayo 2026)

**Tier 1 — Cobertura completa con sintaxis específica:**

| Plataforma | Tipo | Highlight |
|------------|------|-----------|
| Nano Banana Pro | Imagen | 4K, 92% text accuracy, multi-image fusion 14 |
| GPT Image 2 | Imagen | 4K, ~99% multi-script text, reasoning nativo |
| Midjourney V8.1 | Imagen | 2K, artistic direction, sin API oficial |
| FLUX.2 Pro | Imagen | 4MP, typography multi-line, open weights `[dev]` |
| Veo 3.1 | Video | 4, 6 u 8s · hasta 4K (solo a 8s) · audio nativo |
| Gemini Omni Flash | Video | edición conversacional de un vídeo existente |
| Kling 3.0 | Video | 3-15s · 4K nativo · Multi-Shot y Custom Multi-Shot · voz atada al element · Motion Control |
| Seedance 2.5 | Video | 4-30s (+ extensiones), varios planos y tramos de tiempo, hasta 1080p, referencias (30 imgs + 10 vídeos + 10 audios) |
| Runway Gen-4.5 | Video | 60s, multi-scene, motion brush |

Kling 4.0 (anunciado el 30-sep-2026) está en despliegue limitado a 15-oct-2026: Lyra lo anota y avisa, pero no lo recomienda todavía.

**Tier 2 — Cobertura básica:** Ideogram V3, Recraft V4, SD4 Ultra, Wan 2.7 Image, Luma Ray 3.14, Pika 2.5, Hailuo 2.3, Dreamina (wrapper consumer de Seedance 2.5 con UI CapCut), Wan 2.7 Video.

**Tier 3 — Deprecated / EOL:**
- ⚠️ Sora 2 (API EOL 24-sep-2026)
- ⚠️ DALL-E 2/3 (deprecated 12-may-2026)

---

## 🔒 Reglas absolutas del plugin

1. **JSON SCHEMA UNIVERSAL** — Todo prompt sale en JSON v2.0 (estructura cross-platform) + natural language platform-optimizado. Nunca solo natural language sin JSON.
2. **NO HARDCODE DE CATÁLOGO EN PROMPTS DE USUARIO** — El catálogo de modelos vive en `skills/platform-cheatsheet/references/platforms-2026-05.md`. Cuando el catálogo cambie, actualizar ese archivo, no los prompts de los agentes.
3. **DEPRECATION WARNINGS OBLIGATORIOS** — Si el target platform es Tier 3 (Sora 2, DALL-E 2/3), el JSON DEBE incluir `meta.deprecation_warning` y el agente DEBE advertir al usuario antes de generar.
4. **NEGATIVE PROMPT POR DEFECTO CORVERE** — Siempre incluir `["blurry", "low quality", "distorted proportions", "bad lighting", "amateur"]` + context-specific. El auditor flagea ausencia.
5. **NO INVENTAR CAPABILITIES** — Si un modelo no soporta una feature, el agente lo declara explícitamente. No "creer" que Veo 3.1 hace 60s (max 8s) o que Midjourney tiene API oficial (no la tiene).
6. **TEXT IN IMAGE → SINTAXIS ESPECÍFICA** — Si el JSON tiene `text_in_image.elements` poblado, el natural language DEBE usar la sintaxis del modelo (e.g., `Include legible text: "..."` para Nano Banana, `--no` no para Midjourney sino comillas inline).
7. **REFERENCE IMAGE → EXTRACCIÓN ESTRUCTURADA** — Si el usuario aporta imagen ref, el `reference-image-analyzer` extrae hex codes / DoF / cámara inferida ANTES de generar JSON. No "describir vagamente" la referencia.

---

## 📚 Patrones canónicos integrados

| Patrón | Implementación |
|--------|---------------|
| **JSON Schema v2.0** | `skills/universal-json-schema/` — fundación de todo prompt |
| **Decision tree de plataforma** | `agents/platform-router.md` + `skills/platform-cheatsheet/` |
| **CoT espacial (FG/MG/BG)** | `skills/cot-multi-element-scene/` — para escenas multi-elemento |
| **Negative prompt library** | `skills/negative-prompt-library/` — canónicos por use case |
| **Text rendering** | `skills/text-rendering-pattern/` — sintaxis por modelo |
| **Audio layering** | `skills/audio-cue-syntax/` — dialog + SFX + ambient + music |
| **Pre-flight audit** | `agents/visual-prompt-auditor.md` — quality checklist |

---

## 🤝 Relación con el GEM Lyra

Ambos productos comparten **el mismo dominio** y **la misma fuente de verdad** (catálogo Tier 1/2/3 + JSON Schema universal + best practices). La diferencia es el **vehículo de uso**:

| Vehículo | Cuándo |
|----------|--------|
| **GEM (Google Gemini)** | Cliente que opera en stack Google, quiere acceso web/mobile fácil, no usa Claude Code |
| **Plugin Claude** | Cliente que opera en stack Claude Code, quiere integración terminal / IDE, agentic workflow |

Si el cliente tiene ambos, ambos consumen el mismo catálogo y producen JSON intercambiable.

---

## 🔄 Sincronización con el GEM

Cuando el catálogo de modelos cambia (nueva versión Tier 1, deprecation, modelo nuevo top-tier):

1. **Actualizar primero** `skills/platform-cheatsheet/references/platforms-2026-05.md` en este plugin
2. **Sincronizar** `platform_specifications.md` del GEM en `PROYECTOS/PROTOCOLO_EVA/COMMUNITY_AGENTS/GEMINI/Lyra/`
3. **Validar** que el `schema_version` del JSON sigue alineado entre ambos
4. **Bump version** del plugin y del GEM en paralelo

Drift entre los dos vehículos = bug. Si un cliente con ambos productos detecta inconsistencia, es responsabilidad de Corvere Solutions reconciliarlo.

---

## 🚀 Instalación

### En la app de Claude (lo normal para la comunidad)

Necesitas la app de Claude en el ordenador y un plan de pago (Pro o Max).

1. Barra lateral → **Customize** → **Plugins**
2. **Agregar desde un repositorio** → pega `Stiwidh/claude-plugins`
3. En el catálogo **eva-comunidad**, instala **lyra**
4. Activa la sincronización automática del catálogo: así cada mejora te llega sola
5. Para usarlo, escribe `/` y elige, o describe la tarea y se activa solo

Si antes lo instalaste subiendo `lyra.zip`, quita esa copia para no tenerlo repetido.

### En Claude Code

```bash
/plugin install lyra --marketplace Stiwidh/claude-plugins
```

---

## 📋 Changelog

### v2.2.1 (2026-10-15)
- El catálogo de instalación pasa a llamarse **eva-comunidad**.

### v2.2.0 (2026-10-15)
**Kling 3.0 y Seedance 2.5 con sus datos de verdad.** La corrección anterior cambió el nombre de los modelos pero dejó dentro los datos de las versiones viejas. Ahora, verificado contra las fuentes oficiales (URL y fecha en cada ficha):
- **Kling 3.0:** 3-15s, 4K nativo desde el 23-abr-2026, Multi-Shot y Custom Multi-Shot, element con la voz atada, diálogo `Personaje (tono): línea`. Fuera `cfg_scale`, `motion_intensity`, `voice_clone_ref` y `[AUDIO: ...]`, que eran de Kling 2.x
- **Seedance 2.5:** publicado el 31-jul-2026, 4-30s, hasta 1080p (no 2K), 6 aspect ratios más `adaptive`, referencias 30/10/10 citadas como `@Image 1`, tramos de tiempo, API en BytePlus ModelArk. Fuera el lip-sync "por fonemas" y las variantes Fast/Standard/Pro, que no están en ninguna fuente oficial
- `audio-cue-syntax`: fuera la fila "Veo 3.1 (T3) Limitado", que contradecía la de Tier 1. Veo 3.1 tampoco aparece ya como deprecado en el auditor
- Ejemplos de 12s y 15s que mandaban a Veo 3.1 (máximo 8s) corregidos
- Kling 4.0 anotado como anunciado y en despliegue limitado, sin recomendarlo
- Gemini Omni Flash estaba listado como Tier 3 en este README: es Tier 1

### v2.1.1 (2026-10-15)
- Instalación desde el repositorio `Stiwidh/claude-plugins` en vez del ZIP

### v2.1.0 — 2026-05-18 (mismo día)
- **Seedance 2.5 promocionado de Tier 2 a Tier 1** (feature signature: multi-shot auto-storyboard + lip-sync phoneme-level + multimodal input nativo 30 imgs + 10 videos + 10 audios)
- Dreamina queda como wrapper consumer en Tier 2 (UI CapCut con safety estricta)
- JSON Schema añade `platform_specific.seedance_2_5`
- Decision tree de video re-priorizado con Seedance como default para narrativa ≤15s

### v2.0.0 — 2026-05-18
- Release inicial como producto cliente vendible
- Cobertura Tier 1 de 7 plataformas mayo 2026
- 4 sub-agents + 6 skills + 4 commands
- JSON Schema universal v2.0
- Hermano del GEM Lyra v2.0

---

## 🆘 Soporte

**Contacto:** tech@corveresolutions.com

**Master Reference:** `../../GEMINI/Lyra/` (GEM hermano con doc completa)
