---
name: generate
description: Generar un asset suelto con Higgsfield (una imagen, un clip, animar una foto, un lipsync). Se activa con "genera una imagen", "haz un clip", "anima esta foto", "crea una imagen de", "un vídeo corto de", "prueba este prompt", "haz un lipsync". El higgsfield-maestro elige la herramienta correcta, te dice el coste, escribe bien el prompt y lo pide por el conector de Higgsfield.
---

# Generar un asset suelto

Una imagen o un clip, bien hechos: la herramienta correcta, el coste claro, el prompt como debe ser.

## Pasos

1. `higgsfield-maestro` elige la herramienta por la regla de Higgsfield (calidad primero); ver `references/higgsfield_modelos_costes.md`.
2. Escribe el prompt según el método: corto, concreto; si es animar una foto, solo el movimiento; lo que no quieres en positivo.
3. Te dice el coste. Asset suelto fluye; **lote de 3+ → presupuesto y tu OK primero**.
4. Lo genera por el conector de Higgsfield y te entrega el resultado + el coste real. Si el conector no está conectado en tu Claude, te dejo el prompt listo para pegarlo en la web de Higgsfield.

## Cuidado

- **Vertical:** imagen 9:16 primero, luego animarla (nunca vídeo vertical de texto directo).
- **Texto en vídeo:** no se genera. En imagen fija, GPT Image 2.
- Si Higgsfield rechaza por marca/persona real/contenido sensible: cambio el prompt, no insisto.
