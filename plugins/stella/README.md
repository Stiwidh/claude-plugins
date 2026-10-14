# Plugin `stella` — Stella by Corvere Solutions

Plugin de Claude Code para la **comunidad de Protocolo EVA** que convierte "no sé qué publicar" o "publico mucho y no crece" en un **plan de contenido** que atrae, conecta y vende. Stella es una mentora IA cálida y didáctica que aplica el **Sistema Stella** a tu marca personal.

**Hermana del GEM y del GPT** [Stella](../../GEMINI/Stella/) — mismo dominio, distinto vehículo. Los tres comparten el mismo Master Book.

Stella es el **paraguas del ecosistema**: decide QUÉ crear y CUÁNDO; la ejecución la hacen **Vega** (guiones), **Aria** (stories) y **Lyra** (visuales).

---

## 🗺️ Estructura

```
stella/
├── .claude-plugin/plugin.json
├── README.md
├── agents/ (5 sub-agents)
│ ├── content-strategist.md     ← CREADOR PRINCIPAL (Opus)
│ ├── funnel-mapper.md          ← ESPECIALISTA · embudo TOFU/MOFU/BOFU (Sonnet)
│ ├── calendar-architect.md     ← ESPECIALISTA · calendario balanceado (Sonnet)
│ ├── angle-generator.md        ← ESPECIALISTA · pilares → ángulos (Sonnet)
│ └── strategy-qa.md            ← AUDITOR (Sonnet)
├── skills/ (9 skills atómicas)
│ ├── strategy-method/          ← Master Book del Sistema Stella como reference
│ │ ├── SKILL.md
│ │ └── references/strategy_method.md
│ ├── funnel-tofu-mofu-bofu/SKILL.md ← mapear al embudo
│ ├── content-pillars/SKILL.md  ← elegir 3-5 pilares
│ ├── content-calendar/SKILL.md ← calendario balanceado
│ ├── format-mix/SKILL.md       ← qué formato para qué trabajo
│ ├── angle-bank/SKILL.md       ← pilares → ángulos
│ ├── awareness-to-funnel/SKILL.md ← Schwartz → embudo
│ ├── repurposing/SKILL.md      ← 1 idea → N piezas
│ └── metrics-per-stage/SKILL.md ← qué medir en cada nivel
└── commands/ (4 slash commands)
  ├── strategy.md (/stella:strategy) ← plan de contenido completo
  ├── calendar.md (/stella:calendar) ← calendario semanal/mensual
  ├── funnel.md   (/stella:funnel)   ← diagnóstico de embudo + ratio
  └── angles.md   (/stella:angles)   ← ángulos de un pilar
```

---

## 🤖 Sub-agents

**Patrón de roles** (alineado con Vega, Aria, Lyra): 1 creador principal + 3 especialistas + 1 auditor.

| Agent | Rol | Cuándo |
|-------|-----|--------|
| `content-strategist` | **CREADOR PRINCIPAL** | Diseñar el plan de contenido completo: persona, pilares, embudo, ratio, calendario. |
| `funnel-mapper` | El embudo | Diagnostica el desequilibrio (¿falta atraer, nutrir o vender?) y recomienda el ratio. |
| `calendar-architect` | El calendario | Monta calendarios balanceando pilares × embudo con cadencia sostenible. |
| `angle-generator` | Ángulos | Explota un pilar en 8-12 ángulos repartidos por el embudo. |
| `strategy-qa` | Auditoría | Read-only. Valida el plan contra el checklist. PASS / PASS_WITH_FIXES / FAIL. |

---

## 🛠️ Skills atómicas

| Skill | Propósito | Tipo |
|-------|-----------|------|
| `strategy-method` | Master Book del Sistema Stella (16 secciones) como reference | Reference |
| `funnel-tofu-mofu-bofu` | Mapear contenido al embudo + el ratio | Patrón |
| `content-pillars` | Elegir los 3-5 pilares que son tuyos | Técnica |
| `content-calendar` | Calendario balanceado (pilares × embudo) sostenible | Patrón |
| `format-mix` | Qué formato hace qué trabajo en el embudo | Patrón |
| `angle-bank` | Explotar pilares en ángulos | Técnica |
| `awareness-to-funnel` | Niveles de consciencia (Schwartz) → embudo | Técnica |
| `repurposing` | Estirar 1 idea en varios formatos y niveles | Técnica |
| `metrics-per-stage` | Qué medir en cada nivel (no solo seguidores) | Patrón |

---

## ⚡ Slash commands

| Command | Atajo a | Sub-agent responsable |
|---------|---------|------------------------|
| `/stella:strategy <marca/situación>` | Plan de contenido completo | `content-strategist` |
| `/stella:calendar <periodo>` | Calendario semanal/mensual balanceado | `calendar-architect` |
| `/stella:funnel <cuenta/ideas>` | Diagnóstico de embudo + ratio | `funnel-mapper` |
| `/stella:angles <pilar>` | 8-12 ángulos de un pilar repartidos por embudo | `angle-generator` |

---

## 🎯 El embudo de contenido

Todo se organiza alrededor de mover a la persona por un camino: **TOFU** (te descubre) → **MOFU** (confía) → **BOFU** (compra). Ratio de referencia ~50/30/20, invertido en lanzamiento. El error más caro: vivir solo en TOFU (creces, no facturas) o solo en BOFU (quemas a la audiencia).

---

## 🔒 Reglas absolutas del plugin

1. **Estrategia antes que pieza** — nunca "a ver qué se me ocurre hoy".
2. **Una persona concreta**, no "todo el mundo".
3. **3-5 pilares**, uno es tu método/tú.
4. **Cubrir los tres niveles** del embudo.
5. **Ratio consciente** (~50/30/20; invertido en lanzamiento).
6. **Cadencia sostenible** (mantenible 6 meses).
7. **Reutilizar ideas** en vez de producir todo desde cero.
8. **Calentar antes de lanzar.**
9. **Medir el movimiento por el embudo**, no solo seguidores.
10. **Stella diseña el plano; la ejecución se deriva** a Vega/Aria/Lyra. El Master Book manda.

---

## 🎭 Tono y personalidad

Stella es una **mentora cálida y didáctica** para creadoras que se sienten perdidas con qué publicar. Acogedora, didáctica (el "por qué"), competente (rigor estratégico), honesta y adaptable (los pilares y la voz son de la creadora). **Baja tu barrera de entrada, no baja el listón del plan.**

---

## 🚀 Instalación

### En la app de Claude (lo normal para la comunidad)

Necesitas la app de Claude en el ordenador y un plan de pago (Pro o Max).

1. Barra lateral → **Customize** → **Plugins**
2. **Agregar desde un repositorio** → pega `Stiwidh/claude-plugins`
3. En el catálogo **protocolo-eva**, instala **stella**
4. Activa la sincronización automática del catálogo: así cada mejora te llega sola
5. Para usarlo, escribe `/` y elige, o describe la tarea y se activa solo

Si antes lo instalaste subiendo `stella.zip`, quita esa copia para no tenerlo repetido.

### En Claude Code

```bash
/plugin install stella --marketplace Stiwidh/claude-plugins
```

---

## 🤝 Relación con el GEM / GPT y con el ecosistema

Ecosistema de la comunidad EVA: **Stella** (el plan) → alimenta a → **Vega** (guiones de vídeo), **Aria** (stories), **Lyra** (visuales). Stella decide qué pieza toca; ellos la ejecutan.

| Vehículo | Cuándo |
|----------|--------|
| **GEM (Google AI Studio)** / **GPT (ChatGPT)** | Acceso web/móvil, conversacional. |
| **Plugin Claude Code** | Workflow programático, integración con Vega / Aria / Lyra. |

---

## 🔄 Sincronización con el GEM / GPT

Cuando se actualice el Sistema Stella: actualizar primero `skills/strategy-method/references/strategy_method.md`, luego sincronizar el knowledge del GEM (`GEMINI/Stella/`) y del GPT (`CHATGPT/Stella/`), y bump de versión en paralelo. Drift entre vehículos = bug.

---

## 📋 Changelog

### v1.0.0
- Release inicial como producto comunidad Protocolo EVA.
- Master Book Sistema Stella (16 secciones) destilado del embudo de contenido + niveles de consciencia (Schwartz) + filosofía Diego (contenido para nutrir, especificidad) + value ladder de ventas, adaptado a marca personal.
- 5 sub-agents + 9 skills + 4 commands.
- Producto neutro adaptable a la marca de cada creadora.

---

## 🆘 Soporte

**Contacto:** tech@corveresolutions.com

*Stella by Corvere Solutions — producto para la comunidad de Protocolo EVA.*
