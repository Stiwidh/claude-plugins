---
name: creative-qa
description: >-
  El control de calidad del vídeo. Lo activas cuando dices "revisa la pieza", "está bien el vídeo", "antes de publicar", "qué te parece", "puntúa el vídeo", "revisa el guion antes de generar". Revisa en dos momentos: ANTES de generar (¿el guion encaja con el concepto?, ¿el presupuesto en créditos es razonable?, ¿lleva aviso de IA si hace falta?) y DESPUÉS de generar (¿la pieza dice lo que tiene que decir?, ¿el vertical está bien?, ¿el texto no salió corrupto?, y opcionalmente la puntúa con el Virality Predictor de Higgsfield). Devuelve APROBAR / APROBAR CON CAMBIOS / RECHAZAR con lo que hay que arreglar.
---

# Control de calidad

Reviso la pieza en sus dos momentos críticos: antes de gastar créditos y antes de publicar.

## Antes de generar (para no malgastar créditos)

- **¿El guion encaja con el concepto** y con el tipo de pieza (marca vs anuncio)?
- **¿Hay presupuesto en créditos** calculado y razonable para lo que vale la pieza? Sin presupuesto en un lote → no se genera.
- **¿Lleva aviso de IA?** Si hay presentador o voz de IA y va a público o cliente: tiene que llevar "contenido generado con IA" (Art. 50, obligatorio).
- **Contenido de marca:** ¿el hook descarta a quien no es el cliente? ¿hay 3 títulos? ¿está pensada la miniatura?
- **Cámara:** cada plano generado lleva su bloque de movimiento y su porqué, y un solo movimiento principal (skill `direccion-de-camara`).
- **Varios clips o personaje que se repite** (skill `continuidad-y-pruebas`): ¿hay lista de lo que hay que generar, fotograma de estilo y frase de identidad **idéntica** en cada prompt? ¿se ha planeado una prueba barata antes del final? ¿los clips que siguen a otro van de uno en uno?

## Después de generar (antes de publicar)

- **¿La pieza dice lo que tiene que decir?** Que lo que cuenta la voz coincida con lo que se ve.
- **Vertical bien:** que no esté girado (el fallo típico de Higgsfield al generar vídeo vertical).
- **Sin texto corrupto:** que no haya letras generadas ilegibles en pantalla.
- **Sonido:** voz clara, música por debajo, sin cortes raros.
- **Aviso de IA presente** si la pieza lo necesita.
- **Continuidad entre clips:** la misma cara, ropa y luz en cada plano del mismo personaje; nadie duplicado ni con manos o brazos raros; los de fondo siguen ahí; ningún clip se congela al empezar o al acabar; y nada del storyboard colado (trazo de lápiz, números, flechas).
- **Puntuación opcional (recomendada):** pásala por el **Virality Predictor** de Higgsfield para saber la fuerza del gancho, la atención y la retención antes de publicar. Te doy la nota y qué mejorar.

## Lo que entrego

`APROBAR` / `APROBAR CON CAMBIOS` / `RECHAZAR`, con la lista de qué arreglar y quién lo hace. Si es un vídeo corto con guion hablado y tienes el plugin `vega`, te recomiendo pasar también ese guion por `/vega:check` antes de grabar o publicar.
