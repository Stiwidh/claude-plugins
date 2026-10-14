---
description: Diagnostica el embudo de una cuenta o de un set de ideas — dónde está el desequilibrio (falta atraer, nutrir o vender) y qué ratio TOFU/MOFU/BOFU corregirlo.
argument-hint: "{cuenta/ideas/situación}"
---

# /stella:funnel

Diagnóstico de embudo + ratio recomendado.

## Argumentos
- `{cuenta/ideas/situación}` — describe tu situación (ej. "20k seguidores, casi no vendo") o pega tus ideas de contenido para clasificarlas.

## Ejecución
1. `funnel-mapper` clasifica cada idea en su nivel (TOFU/MOFU/BOFU) y consciencia (Schwartz).
2. Diagnostica el desequilibrio:
   - Muchos seguidores, poca venta → falta MOFU/BOFU.
   - Cuenta plana → falta TOFU.
   - Audiencia quemada → exceso de BOFU.
3. Recomienda el **ratio** correcto y qué contenido añadir/reducir.

## Output
```
## Diagnóstico de embudo
Desequilibrio actual · Ratio actual → recomendado
Qué añadir / reducir
Mapeo de tus ideas por nivel
```

## Ejemplos
```
/stella:funnel tengo 20k seguidores pero casi no vendo
/stella:funnel [pega tus ideas de contenido]
```

## Cross-comandos
- Convertir el diagnóstico en plan → `/stella:strategy`
