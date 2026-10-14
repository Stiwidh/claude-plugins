---
description: Genera un guion completo de vídeo corto vertical (Reel / TikTok / Short) listo para grabar, con hook, estructura, payoff y CTA.
argument-hint: "{idea} [tofu|mofu|bofu] [reel|tiktok|short]"
---

# /vega:script

Genera un guion viral completo listo para grabar.

## Argumentos
- `{idea}` — el tema o mensaje del vídeo. Lo más concreto, mejor.
- `[tofu|mofu|bofu]` (opcional) — nivel de embudo: descubrir / conectar / vender. Si no se indica, se infiere del objetivo.
- `[reel|tiktok|short]` (opcional) — plataforma destino. Default: Reel.

Si la idea es genérica, el comando la hará específica (o pedirá 1 dato) antes de generar.

## Ejecución
1. `vega-scriptwriter` diagnostica el brief (embudo, ángulo, formato, nicho, plataforma).
2. Activa `angle-selection` para el ángulo que descarta.
3. Activa `hook-formulas` (o `hook-architect` para varias variantes) para el hook.
4. Activa `script-structure` + `retention-curve` para el cuerpo y el payoff.
5. Activa `spoken-word-optimization` para que suene hablado y `cta-soft-design` para el cierre.
6. Activa `platform-adaptation` según la plataforma.
7. Pasa por `viral-qa` antes de devolver.
8. Devuelve el guion en el formato canónico + notas de rodaje + opciones de refinar.

## Ejemplos
```
/vega:script cómo subir precios sin perder clientes bofu reel
/vega:script 3 errores que espantan clientes de tu perfil tofu
/vega:script el día que perdí a mi mayor cliente mofu tiktok
```

## Cross-comandos
- Solo el hook (varias variantes) → `/vega:hook`
- Toda la semana de un pilar → `/vega:batch`
- Validar un guion tuyo → `/vega:check`
