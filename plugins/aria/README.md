# Plugin `aria` — Aria by Corvere Solutions

Plugin de Claude Code para la **comunidad de Protocolo EVA** que aplica la metodología **Sistema Aria** a tu marca personal. Aria es una mentora IA cálida y didáctica que te guía paso a paso para crear secuencias de Instagram Stories listas para publicar — sin que necesites ser experta en storytelling.

**Hermana del GEM** [Aria](../../GEMINI/Aria/) — mismo dominio, distinto vehículo. Ambos comparten el Sistema Aria + los tipos canónicos (VENTA / MARCA / VENDER SIN VENDER) + el calendario semanal balanceado.

---

## 🗺️ Estructura

```
aria/
├── .claude-plugin/plugin.json
├── README.md
├── agents/ (3 sub-agents)
│ ├── aria-storyseller.md ← CREADOR PRINCIPAL (Opus)
│ ├── weekly-stories-batch.md ← ESPECIALISTA semanal (Sonnet)
│ └── story-quality-check.md ← AUDITOR (Sonnet)
├── skills/ (7 skills atómicas)
│ ├── aria-method/ ← Master Book del Sistema Aria como reference
│ │ ├── SKILL.md
│ │ └── references/aria_method.md
│ ├── opener-design/SKILL.md ← Slides 1-2 (retención swipe-up)
│ ├── secuencia-venta/SKILL.md ← Secuencias tipo VENTA (CTA)
│ ├── secuencia-marca/SKILL.md ← Secuencias tipo MARCA (conexión sin CTA)
│ ├── secuencia-vender-sin-vender/SKILL.md ← Mostrar resultados sin pedir
│ ├── weekly-calendar-planning/SKILL.md ← Calendario L→D balanceado
│ ├── audience-narrative/SKILL.md ← Encontrar la voz propia de tu marca
│ └── manychat-keyword-routing/SKILL.md ← Diseñar keywords ManyChat sin colisión
└── commands/ (3 slash commands)
 ├── secuencia.md (/aria:secuencia) ← Secuencia completa lista para publicar
 ├── calendar.md (/aria:calendar) ← Calendario semanal completo
 └── check.md (/aria:check) ← QA sobre secuencia ya escrita
```

---

## 🤖 Sub-agents

### Creador principal (1)

| Agent | Rol | Cuándo se invoca |
|-------|-----|------------------|
| `aria-storyseller` | **CREADOR PRINCIPAL** | Diseñar secuencias de Stories production-ready. Razona sobre el tipo correcto (VENTA / MARCA / VsV), el opener que enganche, el hilo rojo, la posición en el calendario semanal, el CTA correcto y la integración ManyChat. No "aplica templates" — toma decisiones estratégicas basadas en tu brief. |

### Especialistas (1)

| Agent | Rol | Cuándo |
|-------|-----|--------|
| `weekly-stories-batch` | BATCH SEMANAL | Crea las 5-7 secuencias de toda la semana (L→D) coherentes entre sí — balance VENTA/MARCA/VsV correcto. Útil cuando planificas la semana completa de una sola pasada, no día a día. |

### Auditor (1)

| Agent | Rol | Cuándo |
|-------|-----|--------|
| `story-quality-check` | PRE-PUBLICACIÓN | Read-only review antes de publicar. Valida ≤6 slides, opener efectivo, hilo rojo entre slides, CTA correcto por tipo, sticker apropiado. Reporta BLOQUEANTES / IMPORTANTES / NICE-TO-FIX. |

**Patrón de roles** (alineado con Lyra y los plugins canónicos `aiml`, `typescript`, `retell`): 1 creador principal + 1 especialista + 1 auditor.

---

## 🛠️ Skills atómicas

| Skill | Propósito | Tipo |
|-------|-----------|------|
| `aria-method` | Master Book del Sistema Aria (16 secciones canónicas) como reference RAG | Reference |
| `opener-design` | Cómo enganchar al usuario en slides 1-2 — sin esto la secuencia muere | Técnica |
| `secuencia-venta` | Estructura canónica de secuencia VENTA — con CTA link directo o ManyChat keyword | Patrón |
| `secuencia-marca` | Estructura canónica de secuencia MARCA — conexión sin CTA, solo stickers de interacción | Patrón |
| `secuencia-vender-sin-vender` | Mostrar resultados naturales — la audiencia se convence sola | Patrón |
| `weekly-calendar-planning` | Distribuir tipos de secuencia L→D balanceado (~2 VENTA + 3 MARCA + 2 VsV) | Patrón |
| `audience-narrative` | Encontrar la voz propia de tu marca personal — sin perder autenticidad | Técnica |
| `manychat-keyword-routing` | Diseñar keywords ManyChat únicas que no colisionen entre flujos | Operativa |

---

## ⚡ Slash commands

| Command | Atajo a | Sub-agent responsable |
|---------|---------|------------------------|
| `/aria:secuencia <tipo> <tema>` | Secuencia completa lista para publicar | `aria-storyseller` |
| `/aria:calendar <tema mensual>` | Calendario semanal completo (L→D balanceado) | `weekly-stories-batch` |
| `/aria:check <secuencia>` | QA pre-publicación read-only | `story-quality-check` |

---

## 🎯 Los 3 tipos canónicos de secuencia (Sistema Aria)

| Tipo | Objetivo | CTA | Cuándo usar |
|------|----------|-----|-------------|
| **VENTA** | Acción concreta (comprar, registrarse, agendar) | SÍ — link directo o ManyChat keyword | Cuando tienes oferta activa, lanzamiento, descuento |
| **MARCA** | Conexión + autoridad indirecta | NO — solo stickers de interacción | Behind the scenes, lifestyle, opiniones, valores |
| **VENDER SIN VENDER** | Mostrar resultados naturales | Implícito — sin pedir nada | Testimonios casuales, screenshots de resultados, demos de uso real |

**Calendario semanal canónico** (Sistema Aria adaptable):
- Lunes: VENTA · Martes: VENDER SIN VENDER · Miércoles: MARCA · Jueves: VENTA · Viernes: MARCA + VsV · Sábado: descanso · Domingo: libre

---

## 🔒 Reglas absolutas del plugin

1. **MÁXIMO 6 SLIDES POR SECUENCIA** — regla canónica del Sistema Aria. La retención cae brutalmente después.
2. **OPENER FUERTE OBLIGATORIO** — slides 1-2 con hook + curiosidad o quiebre de patrón. Sin esto, nadie llega al slide 3.
3. **HILO ROJO EN TODA LA SECUENCIA** — los slides NO son piezas sueltas. Setup → desarrollo → CTA.
4. **CTA ÚNICO EN VENTA** — un solo destino (link sticker O ManyChat keyword), nunca ambos.
5. **CERO CTAs EN MARCA** — secuencia MARCA es conexión, no venta. Solo stickers de interacción (encuesta, reacción, cajita preguntas).
6. **BALANCE 70/30 ManyChat vs Link** — 70% keyword automatización (más alcance), 30% link directo (más conversión).
7. **NUNCA STICKERS INVENTADOS** — Instagram solo tiene: link, encuesta, quiz, slider, pregunta, cuenta atrás, ubicación, mención, GIF, música, hashtag. Solo esos.
8. **PUBLICAR DE SEGUIDO** — nunca dividir la misma secuencia entre mañana/mediodía/noche. Reset 24h entre secuencias.
9. **MASTER BOOK ES SOURCE OF TRUTH** — la skill `aria-method` tiene el conocimiento canónico. Cuando dudes, consulta antes.

---

## 🎭 Tono y personalidad

Aria es una **mentora cálida y didáctica** para personas que están empezando con Instagram Stories como canal de venta.

- **Acogedora:** cero condescendencia, cero jerga innecesaria. Si uso un término técnico, lo explico en la misma frase.
- **Didáctica:** explico el "por qué" antes del "cómo" cuando aporta valor.
- **Paciente:** si te atascas, te ofrezco una alternativa más sencilla en lugar de pedirte más detalles técnicos.
- **Competente:** aunque el trato es cálido, las decisiones estratégicas son rigurosas — bajo tu barrera de entrada, NO bajo el listón de tus secuencias.
- **Adaptable a tu marca:** no impongo una voz "Aria". Te ayudo a encontrar y aplicar la voz propia de TU marca personal.

---

## 🤝 Relación con el GEM Aria

Ambos productos comparten **el mismo Master Book** (Sistema Aria) y los mismos tipos canónicos. La diferencia es el vehículo:

| Vehículo | Cuándo usar |
|----------|-------------|
| **GEM (Google AI Studio)** | Acceso web/mobile fácil, conversacional. Ideal si no usas Claude Code y solo quieres pedirle a Aria que te genere una secuencia. |
| **Plugin Claude Code** | Si trabajas en Claude Code / IDE, quieres workflow programático, integrar con otros plugins (Lyra para imágenes, copywriter, etc.) |

Si tienes ambos, ambos producen secuencias coherentes con el mismo Master Book.

---

## 🚀 Instalación

### En la app de Claude (lo normal para la comunidad)

Necesitas la app de Claude en el ordenador y un plan de pago (Pro o Max).

1. Barra lateral → **Customize** → **Plugins**
2. **Agregar desde un repositorio** → pega `Stiwidh/claude-plugins`
3. En el catálogo **protocolo-eva**, instala **aria**
4. Activa la sincronización automática del catálogo: así cada mejora te llega sola
5. Para usarlo, escribe `/` y elige, o describe la tarea y se activa solo

Si antes lo instalaste subiendo `aria.zip`, quita esa copia para no tenerlo repetido.

### En Claude Code

```bash
/plugin install aria --marketplace Stiwidh/claude-plugins
```

---

## 🔄 Sincronización con el GEM

Cuando se actualice el Sistema Aria (una nueva iteración del Sistema Aria, nuevos formatos IG, nuevos stickers, cambios en algoritmo):

1. **Actualizar primero** `skills/aria-method/references/aria_method.md` en este plugin
2. **Sincronizar** el knowledge file del GEM en `GEMINI/Aria/aria_method.md`
3. **Bump version** del plugin y del GEM en paralelo

Drift entre los dos vehículos = bug.

---

## 📋 Changelog

### v1.0.0 — 2026-05-26
- Release inicial como producto comunidad Protocolo EVA
- Adaptado del plugin Cowork interno `sistema-aria` (eva-tania) — quitadas referencias EVA-específicas (Brand Voice EVA, Cliente Ideal EVA, ManyChat Flujos EVA)
- Renombrada skill `a2h-narrative` (Avatar-to-Human específico de EVA) → `audience-narrative` (genérico para marca personal)
- Master Book incluido dentro del plugin como `skills/aria-method/references/`
- 3 sub-agents + 8 skills + 3 commands
- Producto neutro adaptable a la marca de cada alumna

---

## 🆘 Soporte

**Contacto:** tech@corveresolutions.com

*Aria by Corvere Solutions — producto para la comunidad de Protocolo EVA*
