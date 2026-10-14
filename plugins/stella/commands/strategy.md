---
description: Diseña un plan de contenido completo — persona, pilares, embudo, ratio, ángulos, formatos y calendario — con la ejecución derivada a Vega/Aria/Lyra.
argument-hint: "{marca/nicho/situación}"
---

# /stella:strategy

Genera un plan de contenido completo y accionable.

## Argumentos
- `{marca/nicho/situación}` — describe tu marca, tu nicho, tu clienta ideal y qué quieres (crecer, vender, lanzar). Lo más concreto, mejor.

Si falta algo crítico (persona, si hay lanzamiento), el comando pregunta 1-2 cosas antes de generar.

## Ejecución
1. `content-strategist` diagnostica (persona, pilares, situación de embudo, cadencia sostenible).
2. Activa `content-pillars` para los 3-5 pilares.
3. Activa `funnel-tofu-mofu-bofu` + `awareness-to-funnel` para el embudo y el ratio (delega a `funnel-mapper` si hace falta diagnóstico).
4. Activa `angle-bank` para explotar pilares en ángulos (delega a `angle-generator` para lotes).
5. Activa `format-mix` + `content-calendar` para formatos y calendario (delega a `calendar-architect`). Si hay lanzamiento, aplica el calendario de lanzamiento.
6. Pasa por `strategy-qa`.
7. Devuelve el plan + deriva la ejecución (Vega/Aria/Lyra).

## Ejemplos
```
/stella:strategy coach de negocios para creativas, publico mucho y no vendo
/stella:strategy nutricionista antidietas, quiero lanzar mi programa el mes que viene
```

## Cross-comandos
- Solo el calendario → `/stella:calendar`
- Solo el diagnóstico de embudo → `/stella:funnel`
- Ángulos de un pilar → `/stella:angles`
- Los guiones de los Reels → plugin `vega` · las stories → plugin `aria`
