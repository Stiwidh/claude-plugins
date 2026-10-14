---
name: secuencia-venta
description: Genera secuencias de Instagram Stories tipo VENTA para Protocolo EVA. Lleva a la audiencia a una acción concreta - link directo o ManyChat keyword. Aplica Sistema Aria y modelo audience-narrative. Trigger keywords - secuencia venta, story de venta, vender en stories, stories con CTA, lanzar oferta en stories, pre-lanzamiento, last call, recordatorio venta.
---

# Secuencia VENTA (Stories)

Genera secuencias de stories tipo VENTA: 5-6 slides con OPENER + CONTENIDO + CTA cerrando con link o keyword ManyChat.

## Instructions

### Paso 1 — Inputs obligatorios

- **Tema/Producto:** qué se vende (programa Skool, lead magnet, webinar, oferta limitada, etc.)
- **Stage del funnel:** anuncio nuevo / nurturing / lanzamiento / last call / oferta especial
- **CTA preferido:** link directo en bio O keyword ManyChat (`Responde [PALABRA]`)
- **Material disponible:** screenshots, fotos, vídeos cortos
- **Awareness Level** del seguidor target (si no se especifica, asumir Awareness 3-4 en cuenta IG warm)

Si falta CTA o material — PREGUNTA antes de generar. No inventes link ni keyword nueva (si keyword nueva, activar skill `manychat-keyword-routing` primero).

### Paso 2 — Estructura 5-6 slides

| Slide | Bloque | Función |
|---|---|---|
| 1 | OPENER | Engancha + genera curiosidad. Activar skill `opener-design`. |
| 2 | OPENER (opcional) | Si el tema es complejo, segundo slide para dimensionar el problema |
| 3-4 | CONTENIDO | Historia de venta (transformación / autoridad técnica / resultado concreto) |
| 5 | CTA | Acción cerrada — link bio o keyword ManyChat |
| 6 | (opcional) | Recordatorio + sentido de urgencia si aplica |

### Paso 3 — Reglas de slide

1. **Variación de formato** entre slides — alternar foto+texto, vídeo corto, fondo oscuro, encuesta.
2. **Vídeos máximo 30 segundos** con texto/subtítulos siempre.
3. **Espacio negativo** para texto. Si no se lee fácil → fondo oscuro o técnica del marcador.
4. **Texto largo → alinear izquierda**. Mucha info → dividir en slides.
5. **Tipografía:** máximo 2 tipografías nativas Instagram, consistentes.
6. **Hilo rojo:** al menos un elemento rojo (vestido, manzana, label, sticker).
7. **Firma "Eva 🧬"** en algún slide (preferible últimos 2).

### Paso 4 — CTA según balance 70/30

- **70% ManyChat keyword** (`Responde GUIA / VIP / PRECIO`) — fricción baja, alimenta lista, automatiza nurturing
- **30% link directo** (bio, sticker link) — para tráfico caliente o lanzamientos

Si keyword es nueva → consultar primero `<plugin>/skills/aria-method/references/aria_method.md` o activar skill `manychat-keyword-routing`.

### Paso 5 — Output (formato obligatorio)

```
## VENTA — [Tema]

### Slide 1 — OPENER
- **Formato:** [foto+texto / vídeo / fondo oscuro]
- **Visual:** [descripción]
- **Texto:** "[texto exacto del slide]"
- **Sticker/CTA:** [Encuesta / Reacción / Ninguno]

### Slide 2 — [BLOQUE]
- **Formato:** [...]
- **Visual:** [...]
- **Texto:** "[...]"
- **Sticker/CTA:** [...]

(continúa para slides 3-N)

### Slide 5 — CTA
- **Formato:** fondo oscuro / sticker link
- **Visual:** [...]
- **Texto:** "[texto que invita acción]"
- **CTA:** [Link bio / "Responde [PALABRA]"]

📌 **Notas de publicación:**
- Mejor hora sugerida: [si aplica]
- Material necesario: [screenshots/fotos]
- Keyword ManyChat usada: [PALABRA] (verificar flujo activo en cuenta)
- Hilo rojo aplicado: [qué elemento rojo]
- Firma: "Eva 🧬" en slide [N]
```

### Paso 6 — Pre-entrega checklist

- [ ] Max 6 slides
- [ ] Opener engancha (test "¿quiero ver el siguiente?")
- [ ] Hilo rojo presente
- [ ] Firma "Eva 🧬"
- [ ] CTA único y claro
- [ ] Variación de formato entre slides
- [ ] Si keyword ManyChat — verificada vs <tus flujos ManyChat>
- [ ] Voz de marca respetada (voz de marca consistente)
- [ ] Tono Barbacoa Profesional (cero gurú)

## Knowledge Base

- `<plugin>/skills/aria-method/references/aria_method.md` (sección sobre tipo VENTA)
- `<plugin>/skills/aria-method/references/aria_method.md` (paleta colores, tipografía)
- `<plugin>/skills/aria-method/references/aria_method.md` (keywords activas)

## Cross-skill

- Para diseño OPENER detallado → activar `opener-design`
- Para keyword nueva → activar `manychat-keyword-routing`
- Para copy DENTRO del slide (texto exacto) → `copywriter:rrss-captions`
- Para PROMPT de imagen/vídeo del slide → `lyra`
