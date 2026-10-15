---
name: trailer-y-spots
description: >-
  Convertir una historia, una serie o un producto en un tráiler o un spot corto (15, 30, 60 o 90 segundos) que vende la pregunta y no la respuesta: el gancho de los primeros segundos, las mejores frases, la subida, el silencio antes del golpe, el título y el remate, con mapa de música, textos en pantalla y ritmo. Sin destripar el final. Trigger keywords - tráiler, el tráiler de la serie, teaser, avance, promo, un anuncio de 15 segundos, un spot de 30 segundos, vídeo corto para anunciar, cómo vendo esto en un minuto, anuncio del lanzamiento, adelanto del próximo vídeo, pieza para anunciar la serie, montaje promocional.
---

<!--
@SHARED_WITH
  Copia adaptada para la comunidad de Protocolo EVA. Tiene gemelas internas: un cambio de doctrina se replica a mano en todas. Registro: SHARED_COMPONENTS.md
-->

# Tráiler y spots

**Se vende la pregunta, nunca la respuesta.** Un tráiler no resume: crea ganas. Un spot corto
es lo mismo con una sola idea.

Adaptado de la skill "Trailer Builder" (Skill Library de Ann).

---

## 0. Antes de nada: qué se promociona y con qué material

- **Tipo de pieza (Paso 0 del Director).** El tráiler y el spot son piezas de **producción**
  (anuncio, lanzamiento, serie). El contenido de marca de nutrición no se monta como tráiler:
  va con edición mínima y el esfuerzo en título y miniatura.
- **Con qué se monta.** Material ya existente (clips de la serie, planos generados que ya
  tienes) o planos que hay que generar. Si hay que generar, cada plano del tráiler es coste:
  el esquema va a `continuidad-y-pruebas` y a presupuesto antes de nada.
- **El ritmo de corte de esta skill NO vale para un avatar hablando a cámara.** La curva de
  planos por cada 10 segundos (sección 4 de la referencia) y su multiplicador para vertical
  vienen de montar metraje real, donde cortar es gratis. Aquí cada segundo se genera y cada
  corte en una pieza de avatar hablando delata el lipsync y la convierte en anuncio barato; por
  eso este plugin no importa "un corte cada 2 a 4 segundos" a ese tipo de pieza. Esa curva solo
  se aplica a **spots de montaje**: B-roll, planos de producto o planos generados sin nadie
  hablando a cámara.
- **Mensaje comercial.** Si el spot vende (oferta, precio, CTA de compra), un solo CTA, claro y
  suave, y una oferta que diga solo lo que puedes cumplir. Si tienes el plugin `vega`, su skill
  `cta-soft-design` te ayuda a afinar el CTA.

## 1. Entrada

- Leer el material entero (guion, historia, escaleta, sinopsis o la ficha del producto).
- **Una** pregunta como mucho si no se sabe: duración (15, 30, 60 o 90 s) y destino (horizontal
  tipo YouTube, vertical para Reels y TikTok). Por defecto de la fuente: 60 s horizontal.
- Sacar: género, tono, **el gancho** (el "¿y si...?" más magnético de la premisa) y, lo primero
  de todo, **la lista de lo que no se puede enseñar**: todo lo que pasa después de más o menos
  el 65 % de la historia, y cualquier giro, revelado, muerte o final. Queda FUERA.

## 2. Cosechar el material

Recorrer el material y apuntar, con la escena de origen:

- **Ganchos:** los 2 o 3 momentos que hacen que un desconocido deje de hacer scroll.
- **Frases de oro:** cortas, con pegada, que se entienden fuera de contexto (las preguntas y las
  amenazas funcionan mejor en tráiler).
- **Subidas de tensión:** momentos de conflicto que escalan, de la primera mitad.
- **Lo más visual:** las imágenes más cinematográficas (o los mejores planos generados, si es
  una pieza hecha con IA).
- **El adelanto del clímax:** un destello del clímax que enseña lo que está en juego, no el
  resultado.
- **El remate:** un último golpe después del título (un chiste, un susto o una pregunta).

**Para un producto** (spot de anuncio) la cosecha es otra: el problema que resuelve, el momento
en que se ve funcionar y la frase que lo resume. Criterio propio de la adaptación.

## 3. Montar sobre la columna

Se elige la estructura para esa duración y ese género en `references/estructuras-trailer.md` y
se rellena con lo cosechado. Reglas de la fuente:

- **El gancho, dentro de los 3 primeros segundos** (5 en formato cine).
- **Curva de ritmo:** gancho lento, construir, acelerar, corte a negro, remate.
- **Las frases se pueden reordenar y recontextualizar, nunca inventar.** Si alguien habla en el
  vídeo generado, la frase va literal (skill `flux3-prompting`, diálogo literal).
- **Cada destello del tercer acto:** un segundo como máximo, sin contexto, solo lo que está en
  juego.
- **La pregunta del tráiler no es la respuesta de la historia.**

## 4. La entrega

Tabla del esquema:

| Tiempo | Sección | Contenido (escena o frase) | Qué se ve | Audio y música | Texto en pantalla | Ritmo de corte |
|---|---|---|---|---|---|---|

Y además:

- **Mapa de música:** el ánimo de la música por sección, con los puntos de sincronía (p. ej.
  "0 a 8 s: una nota de piano y ambiente; 45 s: percusión que sube; silencio seco en el 52").
- **Textos en pantalla:** el texto exacto, cuándo y cuánto dura. Pocos: de 3 a 5 en 60 s, de 6
  palabras como mucho y al menos 1,5 s en pantalla (criterio de la fuente). Se diseñan en el
  montaje, **nunca se generan dentro del vídeo** (regla del plugin: el texto generado sale
  corrupto).
- **Notas de sonido:** subidas, golpes y dónde va el silencio (justo antes del golpe más
  grande).
- **Curva de ritmo:** planos por cada 10 segundos por sección, **solo si es un spot de
  montaje** (sección 0).
- **Voz en off:** solo si el género la admite; si se usa, se escriben las frases.
- **Aviso de IA:** si hay presentador o voz sintética y va a público, el rótulo "contenido
  generado con IA" entra en el esquema (Art. 50).

## 5. Variantes (se ofrecen, no se imponen)

- **Teaser** de 15 a 20 s: gancho y título, nada de trama.
- **Corte vertical:** reencuadre y gancho en el primer fotograma para el autoplay del feed,
  contando con que se ve sin sonido (subtítulos).
- **Si hay que generar los planos:** cada plano del esquema pasa a `storyboard-artist` con su
  bloque de cámara (`direccion-de-camara`) y su plan de continuidad y prueba barata
  (`continuidad-y-pruebas`).

## 6. Reglas duras

- **Proteger el final es absoluto.** Cada pieza se contrasta con la lista de lo que no se puede
  enseñar antes de colocarla.
- **Cada elección con su porqué** en una línea: qué trabajo hace en la venta.
- **No prometer otro tono:** el tráiler tiene que prometer la pieza que existe. Un tráiler que
  engaña deja público enfadado.
- **30 segundos o menos: UNA idea.** Todo lo demás, fuera.

## Referencia

- `references/estructuras-trailer.md`: la columna universal, estructuras de 90, 60, 30 y 15 a
  20 segundos, convenciones por género, reglas de música, textos, ritmo y el cortafuegos de
  spoilers.
