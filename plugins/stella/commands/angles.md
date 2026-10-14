---
description: Explota un pilar de contenido en 8-12 ángulos concretos repartidos por el embudo, listos para que Vega escriba el guion o Aria monte la story.
argument-hint: "{pilar} [nicho]"
---

# /stella:angles

Genera ángulos de contenido de un pilar — para no quedarte sin qué publicar.

## Argumentos
- `{pilar}` — el territorio temático a explotar (ej. "precios", "vender sin vergüenza").
- `[nicho]` (opcional) — para aplicar la especificidad que descarta.

## Ejecución
1. `angle-generator` explota el pilar en **8-12 ángulos**.
2. Cada ángulo cruza dolor/deseo + nivel de consciencia + formato.
3. Los **reparte por el embudo** (TOFU/MOFU/BOFU).
4. Aplica **especificidad que descarta** (el detalle concreto que clava a la persona).

## Output
```
## Ángulos del pilar: [pilar]
| # | Ángulo (con detalle específico) | Consciencia | Embudo | Formato |
(8-12 filas repartidas por el embudo)
```

## Ejemplos
```
/stella:angles precios coach de negocios
/stella:angles comer sin culpa nutricionista
```

## Cross-comandos
- Escribir el guion de un ángulo → plugin `vega` (`/vega:script`)
- Montar el calendario con los ángulos → `/stella:calendar`
