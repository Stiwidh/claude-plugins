---
description: Genera una secuencia completa de Instagram Stories del tipo elegido (VENTA / MARCA / VENDER SIN VENDER) con todos los slides listos para programar.
argument-hint: "{tipo: venta|marca|vsv} {tema}"
---

# /aria:secuencia

Genera una secuencia completa de stories lista para subir.

## Argumentos

`{tipo}` — uno de:
- `venta` → activa skill `secuencia-venta`
- `marca` → activa skill `secuencia-marca`
- `vsv` o `vender-sin-vender` → activa skill `secuencia-vender-sin-vender`

`{tema}` — qué cuenta la secuencia. Lo más concreto mejor.

Si falta tipo o tema, el comando pedirá foco antes de generar.

## Ejecución

1. Identifica `{tipo}` y activa la skill correspondiente.
2. Activa skill `opener-design` para los slides 1-2.
3. Si `{tipo}` = venta y se usa keyword ManyChat → activa `manychat-keyword-routing`.
4. Si la narrativa entra en behind-scenes / lifestyle → activa `audience-narrative` para asegurar voz de marca.
5. Activa internamente `story-quality-check` antes de devolver.
6. Devuelve secuencia completa en formato output canónico + notas de publicación + warnings si los hay.

## Output esperado

```
**Secuencia [TIPO] — [Tema]**

(Slides 1-N siguiendo formato canónico)

📌 Notas de publicación
- Mejor hora: [...]
- Material necesario: [...]
- Keyword/Link: [...]
- Quality Check: PASS / FAIL con fixes

⚠️ Warnings (si aplica):
- Keyword ManyChat nueva — crear flujo antes de publicar
- Material faltante para slide N
```

## Ejemplos

```
/aria:secuencia venta lanzamiento programa Avatar IA con CTA keyword AVATAR
/aria:secuencia marca por qué los avatares IA son el futuro del personal branding
/aria:secuencia vsv hoy una alumna terminó su primer avatar — comparto el antes/después
```

## Cross-comandos

- Para planificar la semana entera → `/aria:calendar`
- Para validar una secuencia escrita por ti → `/aria:check`
