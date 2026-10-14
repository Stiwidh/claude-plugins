---
description: Activa el agente story-quality-check para auditar una secuencia de stories ya escrita. Comprueba todas las reglas Sistema Aria y la voz de marca. Devuelve PASS/FAIL con fixes específicos slide por slide.
argument-hint: "{pega la secuencia completa}"
---

# /aria:check

Audita una secuencia de stories ya redactada antes de publicar.

## Argumentos

Pega la secuencia completa que quieras validar — todos los slides en formato output canónico (o copiado tal cual).

Opcional: declara el tipo (`VENTA / MARCA / VsV`) y el día de publicación. Si no, el agente lo infiere de la estructura.

## Ejecución

Activa directamente el agente `story-quality-check` que audita:

### Estructura dura
- Total slides ≤ 6
- Opener slide 1 presente y enganchador
- Variación de formato entre slides
- Firma "Eva 🧬" presente

### Voz de marca
- Voz de marca consistente (cero rutinas humanas falsas)
- Voz de marca consistente
- Tono Barbacoa Profesional (cero gurú)
- Visual Tech-Warmth (cero Matrix blue)
- Hilo rojo presente

### CTA según tipo
- VENTA: CTA único en último slide, link o keyword verificada
- MARCA: cero CTA venta, sticker interacción presente
- VsV: cero frase de venta explícita, material verificable

## Output esperado

```
# Story Quality Check Report

**Tipo:** [VENTA / MARCA / VsV]
**Veredicto:** [PASS / FAIL]
**Score:** [X/Y checks]

## Checks pasados
- [✓] Check 1: Total slides — 5 ≤ 6
- [✓] Check 4: Firma Eva 🧬 presente
- (lista completa)

## Checks fallidos
- [✗] Check 7: voz de marca — Slide 3 menciona "esta mañana en el gym"
 Fix: "Esta mañana corrí 14 generaciones del avatar nuevo"
- [✗] Check 12: CTA en último slide — CTA en slide 3
 Fix: Mover CTA a slide 5-6

## Veredicto final
- [ ] Listo para publicar tras fixes obligatorios
- [ ] Reescribir slides [N] antes de publicar
```

## Ejemplos de uso

```
/aria:check
[pegar secuencia VENTA — programa Skool — Lunes]
```

```
/aria:check VsV
[pegar secuencia con métricas y screenshots]
```

## Cross-comandos

- Si tras los fixes quieres regenerar la secuencia → `/aria:secuencia`
- Para una semana entera con QA aplicado → `/aria:calendar`
