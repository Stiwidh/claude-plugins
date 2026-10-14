# Plugin `vega` — Vega by Corvere Solutions

Plugin de Claude Code para la **comunidad de Protocolo EVA** que convierte cualquier idea en un **guion de vídeo corto vertical** (Reels / TikTok / Shorts) listo para grabar. Vega es una mentora IA cálida y didáctica que aplica el **Sistema Vega** a tu marca personal — sin que necesites ser experta en guion.

**Hermana del GEM y del GPT** [Vega](../../GEMINI/Vega/) — mismo dominio, distinto vehículo. Los tres comparten el mismo Master Book (Sistema Vega).

---

## 🗺️ Estructura

```
vega/
├── .claude-plugin/plugin.json
├── README.md
├── agents/ (5 sub-agents)
│ ├── vega-scriptwriter.md      ← CREADOR PRINCIPAL (Opus)
│ ├── hook-architect.md         ← ESPECIALISTA · los 3 primeros segundos (Sonnet)
│ ├── retention-engineer.md     ← ESPECIALISTA · la curva de retención (Sonnet)
│ ├── batch-scripts.md          ← ESPECIALISTA · lotes de guiones (Sonnet)
│ └── viral-qa.md               ← AUDITOR (Sonnet)
├── skills/ (9 skills atómicas)
│ ├── viral-method/             ← Master Book del Sistema Vega como reference
│ │ ├── SKILL.md
│ │ └── references/viral_method.md
│ ├── hook-formulas/SKILL.md    ← construir el hook (las 3 capas)
│ ├── hook-library/SKILL.md     ← banco de hooks por familia y nicho
│ ├── retention-curve/SKILL.md  ← open loops + tapar valles
│ ├── script-structure/SKILL.md ← Hook→Tensión→Valor→Payoff→CTA
│ ├── angle-selection/SKILL.md  ← el ángulo que descarta
│ ├── spoken-word-optimization/SKILL.md ← escribir para ser hablado
│ ├── cta-soft-design/SKILL.md  ← el CTA único y suave
│ └── platform-adaptation/SKILL.md ← Reel vs TikTok vs Short
└── commands/ (4 slash commands)
  ├── script.md  (/vega:script)  ← guion completo listo para grabar
  ├── hook.md    (/vega:hook)    ← 3-5 variantes de hook
  ├── batch.md   (/vega:batch)   ← lote/semana de guiones
  └── check.md   (/vega:check)   ← QA sobre un guion ya escrito
```

---

## 🤖 Sub-agents

**Patrón de roles** (alineado con Aria, Lyra y los plugins canónicos Corvere): 1 creador principal + 3 especialistas + 1 auditor.

| Agent | Rol | Cuándo |
|-------|-----|--------|
| `vega-scriptwriter` | **CREADOR PRINCIPAL** | Convertir una idea en un guion completo listo para grabar. Decide embudo, ángulo, formato, hook y estructura. |
| `hook-architect` | Los 3 primeros segundos | Genera 3-5 variantes de hook de familias distintas y las puntúa por cuánto pican. |
| `retention-engineer` | La curva | Toma un borrador y tapa los valles: open loops, aire muerto fuera, pacing, payoff que cierra. |
| `batch-scripts` | Lotes | Genera N guiones coherentes de un pilar, rotando ángulos y balanceando el embudo. |
| `viral-qa` | Pre-grabación | Read-only. Valida contra el checklist del Sistema Vega. PASS / PASS_WITH_FIXES / FAIL. |

---

## 🛠️ Skills atómicas

| Skill | Propósito | Tipo |
|-------|-----------|------|
| `viral-method` | Master Book del Sistema Vega (19 secciones) como reference | Reference |
| `hook-formulas` | Construir un hook con sus 3 capas (brecha + texto gigante + bucle) | Técnica |
| `hook-library` | Banco de hooks por familia y por nicho de creadora | Reference |
| `retention-curve` | Open loops encadenados + tapar valles + cambio de estímulo | Técnica |
| `script-structure` | El esqueleto Hook→Tensión→Valor→Payoff→CTA | Patrón |
| `angle-selection` | El ángulo específico que descarta al generalista | Técnica |
| `spoken-word-optimization` | Escribir para ser hablado, no leído | Técnica |
| `cta-soft-design` | Un solo CTA, suave, coherente con el embudo | Patrón |
| `platform-adaptation` | Matices Reel vs TikTok vs Short | Patrón |

---

## ⚡ Slash commands

| Command | Atajo a | Sub-agent responsable |
|---------|---------|------------------------|
| `/vega:script <idea>` | Guion completo listo para grabar | `vega-scriptwriter` |
| `/vega:hook <idea>` | 3-5 variantes de hook | `hook-architect` |
| `/vega:batch <pilar> <N>` | Lote/semana de guiones coherentes | `batch-scripts` |
| `/vega:check <guion>` | QA pre-grabación read-only | `viral-qa` |

---

## 🎯 Los 8 formatos del Sistema Vega

Educativo/tip · Storytime · Hot-take/opinión · Tutorial · Listicle · Mito vs realidad · Transformación (sin humo) · POV/relatable. Cada uno con su ritmo y su guion ejemplo en el Master Book (§8).

## 🎯 El guion en el embudo

Cada guion tiene UN trabajo según el nivel: **TOFU** (descubrir, máximo valor), **MOFU** (conectar y generar confianza), **BOFU** (vender). Un vídeo = un nivel. El PLAN de la mezcla lo decide **Stella** (estrategia de contenido); Vega escribe el guion del nivel que toque.

---

## 🔒 Reglas absolutas del plugin

1. **El hook es sagrado** — los 3 primeros segundos deciden todo; se entiende sin sonido.
2. **Un solo takeaway** por vídeo.
3. **Específico hasta descartar** — si lo podría decir cualquiera del nicho, se reescribe.
4. **El payoff cierra el bucle del hook** — sin cierre no hay completion.
5. **Un solo CTA**, suave, coherente con el embudo.
6. **Escrito para ser hablado**, no leído.
7. **Un vídeo, un nivel de embudo.**
8. **Cero humo** — nada de purple prose, coach motivacional ni datos inventados.
9. **La viralidad al servicio de la marca y la venta**, no de vanity metrics.
10. **El Master Book manda** — ante la duda, `viral_method.md`.

---

## 🎭 Tono y personalidad

Vega es una **mentora cálida y didáctica** para creadoras que empiezan con vídeo corto. Acogedora (cero jerga sin explicar), didáctica (el "por qué" antes del "cómo"), competente (rigor estratégico), honesta (cero invención), adaptable (aplica la voz de TU marca, no impone una "voz Vega"). **Baja tu barrera de entrada, no baja el listón del guion.**

---

## 🚀 Instalación

### En la app de Claude (lo normal para la comunidad)

Necesitas la app de Claude en el ordenador y un plan de pago (Pro o Max).

1. Barra lateral → **Customize** → **Plugins**
2. **Agregar desde un repositorio** → pega `Stiwidh/claude-plugins`
3. En el catálogo **protocolo-eva**, instala **vega**
4. Activa la sincronización automática del catálogo: así cada mejora te llega sola
5. Para usarlo, escribe `/` y elige, o describe la tarea y se activa solo

Si antes lo instalaste subiendo `vega.zip`, quita esa copia para no tenerlo repetido.

### En Claude Code

```bash
/plugin install vega --marketplace Stiwidh/claude-plugins
```

---

## 🤝 Relación con el GEM / GPT Vega y con el ecosistema

| Vehículo | Cuándo |
|----------|--------|
| **GEM (Google AI Studio)** / **GPT (ChatGPT)** | Acceso web/móvil, conversacional. Ideal si no usas Claude Code. |
| **Plugin Claude Code** | Workflow programático, integración con Stella / Aria / Lyra. |

Ecosistema de la comunidad EVA: **Stella** (el plan) → alimenta a → **Vega** (guiones de vídeo), **Aria** (stories), **Lyra** (visuales). Vega escribe el guion; el visual/portada lo hace Lyra; la mezcla y el calendario los decide Stella.

---

## 🔄 Sincronización con el GEM / GPT

Cuando se actualice el Sistema Vega:
1. **Actualizar primero** `skills/viral-method/references/viral_method.md` (este plugin).
2. **Sincronizar** el knowledge del GEM (`GEMINI/Vega/`) y del GPT (`CHATGPT/Vega/`).
3. **Bump version** en paralelo.

Drift entre vehículos = bug.

---

## 📋 Changelog

### v1.0.0
- Release inicial como producto comunidad Protocolo EVA.
- Master Book Sistema Vega (19 secciones) destilado de Short-Form / Retention-Pacing / AI-Niche + Copywriting (hooks) + Diego (especificidad), adaptado a marca personal.
- 5 sub-agents + 9 skills + 4 commands.
- Producto neutro adaptable a la marca de cada creadora.

---

## 🆘 Soporte

**Contacto:** tech@corveresolutions.com

*Vega by Corvere Solutions — producto para la comunidad de Protocolo EVA.*
