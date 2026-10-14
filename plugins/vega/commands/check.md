---
description: Audita un guion ya escrito contra el checklist del Sistema Vega y devuelve veredicto PASS / PASS_WITH_FIXES / FAIL con correcciones concretas.
argument-hint: "{guion}"
---

# /vega:check

QA pre-grabación de un guion (tuyo o generado). Read-only.

## Argumentos
- `{guion}` — pega el texto del guion a revisar.

## Ejecución
1. `viral-qa` corre el checklist del §18 del Master Book.
2. Clasifica hallazgos por severidad: **BLOQUEANTE** (hook con preámbulo, sin bucle, CTA múltiple, dos+ takeaways, humo/datos inventados), **IMPORTANTE** (poca especificidad, aire muerto, payoff flojo, tono que resbala), **NICE**.
3. Da el **fix concreto** de cada hallazgo (no reescribe el guion entero).

## Output
```
## QA del guion — veredicto: [PASS / PASS_WITH_FIXES / FAIL]
Bloqueantes: [n] → línea → problema → fix
Importantes: [n]
Nice-to-fix: [n]
Resumen: [qué falta para PASS]
```

## Ejemplos
```
/vega:check [pega aquí tu guion]
```

## Cross-comandos
- Generar un guion desde cero → `/vega:script`
- Mejorar solo el hook → `/vega:hook`
