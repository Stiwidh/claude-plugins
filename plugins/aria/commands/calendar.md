---
description: Activa el agente weekly-stories-batch para generar las 5-7 secuencias completas de la semana siguiendo el calendario canónico L→D balanceado.
argument-hint: "{tema mensual o semanal} | {producto/oferta activa} | {material disponible}"
---

# /aria:calendar

Genera la semana completa de stories en una sola pasada.

## Argumentos

`{tema}` — eje narrativo que une los 5-7 días.
`{producto/oferta activa}` — qué se vende esta semana (programa Skool, lead magnet, lista espera, webinar). Si no hay → semana se enfoca en MARCA.
`{material disponible}` — fotos, vídeos, screenshots ya agendados.

Si falta tema o producto → pedir antes de ejecutar (no inventar).

## Ejecución

Activa el agente `weekly-stories-batch` que internamente:

1. `weekly-calendar-planning` → estructura editorial L→D
2. `secuencia-venta` (Lun, Jue) — 2 secuencias VENTA con ángulos distintos
3. `secuencia-vender-sin-vender` (Mar, Vie tarde) — 2 secuencias VsV con material verificable
4. `secuencia-marca` (Mié, Vie mañana) — 2 secuencias MARCA con interacción
5. Verificación de coherencia narrativa cross-día
6. `manychat-keyword-routing` si aplica
7. `story-quality-check` global antes de devolver

## Output esperado

```
# Semana del [Lun DD-MM] al [Dom DD-MM] — Stories

**Tema central:** [...]
**Oferta activa:** [...]
**Hilo rojo común:** [...]

## LUNES — VENTA
[secuencia completa]

## MARTES — VsV
[secuencia completa]

(... días restantes)

## SÁBADO — DESCANSO
(Sin secuencia. Reset algorítmico.)

# Material a preparar
[tabla por día]

# Keywords ManyChat usadas
[tabla con flujo destino + estado activo]

# Quality Check global
- Total secuencias: [N]
- Score: [X/Y]
- Issues bloqueantes: [...]
```

## Ejemplos

```
/aria:calendar la semana del miedo a la cámara | programa Skool gratis | tengo 3 testimonios + 5 generaciones nuevas
/aria:calendar pre-lanzamiento programa AVATAR | programa AVATAR | tengo screenshots Skool + demos
```

## Cross-comandos

- Para una secuencia individual → `/aria:secuencia`
- Para validar una secuencia ya escrita → `/aria:check`
