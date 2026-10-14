---
name: aria-method
description: |
  Master Book canónico del **Sistema Aria** completo en `references/aria_method.md`. Source of truth del plugin `aria` para cualquier decisión sobre Instagram Stories como canal de ventas — funcionamiento del algoritmo de Stories, los 3 modos canónicos (VENTA / MARCA / VENDER SIN VENDER), anatomía de una secuencia (apertura + desarrollo + cierre), 7 anti-patterns que matan visualizaciones, stickers oficiales de Instagram, decisión link vs ManyChat keyword con balance 70/30, reglas de publicación, calendario semanal balanceado, cómo construir prueba social, sistema de planificación, qué hacer sin testimonios todavía. 16 secciones canónicas. Consultar siempre que haya duda estratégica sobre stories o se necesite citar el método aplicado.
---

# Sistema Aria — Master Book

Source of truth del plugin `aria`. Contenido propio de Corvere Solutions, basado en principios universales del marketing en Instagram Stories y observaciones públicas del comportamiento del algoritmo a 2026.

## Cómo se usa esta skill

Aria consulta este master book cuando:

- Necesita citar el método al usuario ("según el Sistema Aria...")
- Toma decisiones estratégicas y duda sobre la regla canónica (ej: ¿cuántos slides máximo? ¿qué errores matan visualizaciones? ¿por qué vender sin vender funciona?)
- El usuario pide explícitamente referencia al método ("explícame cómo funciona el algoritmo de Stories", "qué dice el método sobre los anti-patterns")
- Aplica las reglas duras del plugin (≤6 slides, 70/30 ManyChat vs link, calendario semanal canónico, modo único por secuencia)
- `story-quality-check` (auditor) valida una secuencia y necesita citar la regla violada con base canónica

**No volcar el archivo completo al usuario** — Aria resume, referencia o cita fragmentos. La metodología completa (~28 KB, 16 secciones) está en `references/aria_method.md`.

## Secciones del Master Book

| § | Sección |
|---|---------|
| 1 | Por qué Stories es un canal de ventas (Reels vs Stories vs DMs en el embudo) |
| 2 | Cómo decide Instagram a quién mostrar tus Stories (3 señales del algoritmo + interacciones positivas/negativas) |
| 3 | La fórmula de la tasa de visualización (cómo medir tu baseline) |
| 4 | Los 3 modos de Stories (VENTA / MARCA / VENDER SIN VENDER) + subtipos canónicos |
| 5 | Anatomía de una secuencia (apertura + desarrollo + cierre + hilo rojo + 5 patrones de apertura) |
| 6 | 7 anti-patterns que matan visualizaciones |
| 7 | Stickers oficiales de Instagram (a 2026) |
| 8 | CTAs: link directo vs ManyChat keyword (balance 70/30) |
| 9 | Reglas de publicación (de seguido, máx 6, reset 24h, archivar) |
| 10 | El calendario semanal del Sistema Aria (L→D + proporciones) |
| 11 | Cómo construir prueba social útil (categorías + reglas de uso) |
| 12 | El sistema de planificación (qué planificar / qué dejar para el día) |
| 13 | Qué hacer cuando no tienes testimonios todavía |
| 14 | Cómo aplica Aria este método (workflow interno) |
| 15 | Reglas absolutas del Sistema Aria (10 reglas inviolables) |
| 16 | Maintenance del Sistema |

## Reglas duras derivadas del Master Book

Estas reglas son **inviolables** dentro del plugin `aria` (ver §15):

1. **Máximo 6 slides por secuencia** (§5, §9)
2. **Apertura fuerte obligatoria** (§5) — slides 1-2 con uno de los 5 patrones canónicos
3. **Hilo rojo entre slides** (§5) — los slides son una historia, no piezas sueltas
4. **CTA único en VENTA** (§8) — no mezclar link y keyword en el mismo CTA
5. **Cero CTAs en MARCA** (§4) — solo stickers de interacción
6. **Stickers solo oficiales de Instagram** (§7) — nada inventado
7. **Publicar de seguido** (§9) — sin dividir entre franjas horarias
8. **Modo único por secuencia** (§6) — no mezclar VENTA + MARCA en la misma secuencia
9. **Anonimizar testimonios** (§11) — nombres, datos identificables fuera
10. **No inventar resultados ni métricas** (§13) — la audiencia detecta los falsos

## Cómo el master book sirve a otras skills

- `opener-design` aplica §5 (anatomía + 5 patrones de apertura)
- `secuencia-venta` aplica §4 (modo VENTA + subtipos) + §8 (CTAs)
- `secuencia-marca` aplica §4 (modo MARCA + subtipos) + regla "cero CTAs"
- `secuencia-vender-sin-vender` aplica §4 (modo VENDER SIN VENDER + subtipos)
- `weekly-calendar-planning` aplica §10 (calendario semanal canónico)
- `audience-narrative` complementa con la voz propia de la marca (el método es genérico, la voz es personal)
- `manychat-keyword-routing` aplica §8 (CTA por automatización)

## Maintenance

Este master book se actualiza solo cuando:

- Instagram cambia algo material en el algoritmo de Stories
- Aparecen nuevos stickers oficiales o se discontinúan los actuales
- Surgen nuevas integraciones nativas (cambios en ManyChat, WhatsApp, etc.)
- El feedback de la comunidad de usuarios revela casos no cubiertos

Owner: Corvere Solutions.

Drift entre este master book y el del GEM hermano (`GEMINI/Aria/aria_method.md`) = bug. Ambos se actualizan en paralelo.

## Reference

Archivo completo (~28 KB, 16 secciones): `references/aria_method.md`
