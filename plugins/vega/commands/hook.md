---
description: Genera 3-5 variantes de hook (los 3 primeros segundos) de familias distintas, cada una con su texto de apertura gigante y su bucle abierto, puntuadas por cuánto pican.
argument-hint: "{idea} [nicho]"
---

# /vega:hook

Genera varias variantes de hook para una idea y recomienda la ganadora.

## Argumentos
- `{idea}` — el mensaje del vídeo.
- `[nicho]` (opcional) — para aplicar la especificidad que descarta.

## Ejecución
1. `hook-architect` genera 3-5 variantes de **familias distintas** (error, hot-take, pregunta, cifra, transformación, callout, revelación, mito, storytime, lista).
2. Cada variante con las 3 capas: lo que se dice (brecha) · texto gigante ≤8 palabras · bucle abierto.
3. Aplica el filtro de especificidad (§3).
4. Puntúa cada una (1-5) y recomienda la ganadora con el porqué.

## Output
```
### Hooks para: [idea]
1. [familia] — pica ★★★★☆ · [TEXTO GIGANTE] · se dice · bucle
2. [familia] — pica ★★★★★ · ...
Recomiendo la #N porque [brecha + especificidad + claridad sin sonido].
```

## Ejemplos
```
/vega:hook subir precios sin perder clientes coach de negocios
/vega:hook por qué no crece tu cuenta aunque publiques mucho
```

## Cross-comandos
- Guion completo → `/vega:script`
