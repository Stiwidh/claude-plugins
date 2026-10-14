---
description: Genera un lote (o la semana) de guiones coherentes de un mismo pilar, rotando ángulos sin repetición y balanceando el nivel de embudo TOFU/MOFU/BOFU.
argument-hint: "{pilar} {N|semana}"
---

# /vega:batch

Genera varios guiones de una pasada, coherentes y variados.

## Argumentos
- `{pilar}` — el tema paraguas de la semana/lote (ej. "vender sin sentirte vendedora").
- `{N|semana}` — cuántos guiones (número) o "semana".

## Ejecución
1. `batch-scripts` genera N guiones del pilar.
2. **Rota ángulos** (§9) — sin repetir la sensación entre guiones.
3. **Balancea el embudo** (§12) — mezcla TOFU/MOFU/BOFU declarada.
4. Mantiene hilo de marca (misma voz, referencias que se acumulan).
5. Pasa el lote por `viral-qa`.
6. Si no hay plan de contenido detrás, avisa de pasar antes por `stella` (o genera un default equilibrado y lo declara).

## Output
```
## Lote — [pilar] · [N] · [plataforma]
Mezcla de embudo: [X TOFU · Y MOFU · Z BOFU]
Ángulos usados: [lista sin repetición]
### Guion 1 … Guion N (formato canónico)
### QA del lote
```

## Ejemplos
```
/vega:batch vender sin sentirte vendedora 5
/vega:batch productividad para creadoras semana
```

## Cross-comandos
- Un guion suelto → `/vega:script`
- El plan de pilares y calendario → plugin `stella`
