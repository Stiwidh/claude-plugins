---
description: Monta el calendario de contenido (semanal o mensual) balanceando pilares y embudo con cadencia sostenible; incluye calendario de lanzamiento si hay oferta.
argument-hint: "{periodo: semana|mes} [pilares] [lanzamiento?]"
---

# /stella:calendar

Genera un calendario de contenido balanceado y ejecutable.

## Argumentos
- `{periodo}` — `semana` o `mes`.
- `[pilares]` (opcional) — tus pilares, si ya los tienes. Si no, se definen primero.
- `[lanzamiento?]` (opcional) — si hay una oferta que lanzar en el periodo → aplica el calendario de lanzamiento.

## Ejecución
1. `calendar-architect` monta el calendario balanceando **pilares × embudo** con el ratio (~50/30/20).
2. Fija una **cadencia sostenible** y asigna **formato** a cada pieza.
3. Si hay lanzamiento → patrón calentar (S1-2) → preparar (S3) → lanzar (S4).
4. Marca la **reutilización** de ideas entre formatos.
5. Cada pieza indica quién la ejecuta (Vega/Aria/Lyra).

## Output
```
## Calendario — [periodo]
Cadencia · Ratio
[Día] — [Formato] · [Pilar] · [nivel] — [ángulo] → ejecuta: [...]
Nota de reutilización
```

## Ejemplos
```
/stella:calendar mes
/stella:calendar semana pilares: precios, vender sin vergüenza, mi método
/stella:calendar mes lanzamiento
```

## Cross-comandos
- Plan completo (persona + pilares + embudo) → `/stella:strategy`
