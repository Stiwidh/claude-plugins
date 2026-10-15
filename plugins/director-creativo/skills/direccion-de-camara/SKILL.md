---
name: direccion-de-camara
description: Decidir y escribir la cámara de cada plano generado con IA (Seedance, Kling, Veo, Omni, FLUX 3). Primero la emoción que tiene que provocar el plano, luego el tamaño, el ángulo, la lente y el movimiento, y el movimiento se escribe con un bloque de cuatro partes (movimiento, velocidad, encuadre, final) sacado de una biblioteca de 46 movimientos. Trigger keywords - movimiento de cámara, qué cámara pongo, qué plano uso, dolly, travelling, paneo, zoom, grúa, dron, órbita, cámara en mano, barrido, plano secuencia, cómo filmo esta escena, que se sienta tenso, que se sienta íntimo, que se sienta épico, shot list, lista de planos, plano de producto, revelado.
---

<!--
@SHARED_WITH
  Copia adaptada para la comunidad de Protocolo EVA. Tiene gemelas internas: un cambio de doctrina se replica a mano en todas. Registro: SHARED_COMPONENTS.md
-->

# Dirección de cámara

**Primero la emoción, después la cámara.** Un plano sin un porqué se corta. La cámara no se
elige por variedad ni porque quede bonita: se elige por lo que tiene que sentir quien mira en
ese momento.

Esta skill tiene dos mitades:

- **El porqué:** la gramática emocional de la cámara (tamaño, ángulo, lente, movimiento,
  composición, luz). Está en `references/gramatica-emocional.md`.
- **El cómo:** 46 bloques de movimiento listos para pegar en el prompt, en
  `references/movimientos.md`.

Se carga cada vez que el guion lleva un plano generado (B-roll, anuncio, personaje, producto).
No aplica a lo que se graba con cara real a cámara, ni a grabaciones de pantalla.

---

## 1. Antes de elegir cámara: el mapa emocional de la escena

Por cada escena, cuatro preguntas. Si el guion no las contesta, se pregunta **una** sola:
"¿de quién es la escena y cómo tiene que sentirse quien mira al final?".

1. **De quién es.** La cámara suele ponerse de su lado.
2. **Quién manda.** Y si el poder cambia a mitad de escena.
3. **El arco.** Empieza en un sentimiento y acaba en otro; la cámara recorre ese mismo camino.
4. **El giro.** El momento más importante de la escena. Se lleva el plano más distintivo.

Con eso se escribe **la estrategia visual en una frase**, y gobierna todos los planos de la
escena. Ejemplo: "empezamos abiertos y lejos; según se sinceran, el espacio se cierra; acabamos
en primeros planos sueltos".

Y un control: **cada escena tiene que cambiar algo**. Si el sentimiento del principio y el del
final son el mismo, la escena es relleno. Se corta o se le mete un giro.

## 2. Cada plano lleva su porqué

Por cada plano generado se deciden estos campos, y el último no es opcional:

| Campo | Qué se decide |
|---|---|
| Tamaño + ángulo | p. ej. primer plano, ligeramente contrapicado |
| Lente | focal y para qué (comprimir, distorsionar, aislar) |
| Movimiento | un bloque de `movimientos.md`, o plano fijo |
| Composición | equilibrio, aire, marco dentro del marco, líneas |
| Luz | de qué lado entra, calidad, fuente visible |
| **Por qué** | una línea: el trabajo emocional de este plano en esta escena |

Reglas del porqué:

- **Atado a esta escena**, no consejo genérico de escuela de cine.
- **Una opción fuerte por plano**, no un menú. Se pueden marcar una o dos alternativas
  valientes ("segura: plano fijo medio / valiente: acercamiento lento de 8 segundos").
- **No sobrecubrir.** Las mejores escenas suelen necesitar de 4 a 6 planos.
- **La escala acompaña la intensidad.** Los planos se cierran (o se abren) con la emoción,
  nunca al azar.

## 3. El movimiento se escribe con cuatro partes

Todos los bloques siguen el mismo esqueleto, y esa regularidad es lo que los hace fiables
entre modelos:

```
[nombre del movimiento]. Movement: [qué hace físicamente la cámara]. Speed: [ritmo y carácter]. Framing: [qué se mantiene legible y estable]. End: [dónde termina el plano].
```

Los modelos de vídeo obedecen mejor la cámara cuando el movimiento, la velocidad, lo que no
se mueve y el fotograma de llegada van dichos por separado. "Cámara cinematográfica" a secas
da movimiento aleatorio.

**El `End` es la parte que más se olvida y la que más importa**: en imagen a vídeo decide
cómo acaba el clip, y cuando se encadenan clips es el fotograma del que arranca el siguiente.

Los bloques se escriben **en inglés dentro del prompt**, aunque el resto de la pieza vaya en
español. Se pueden cambiar la dirección (derecha e izquierda, dentro y fuera) y las palabras
de velocidad (lento y suave, rápido y seco) sin tocar el esqueleto.

## 4. De la intención a la familia de movimientos

| Qué tiene que sentir quien mira | Familia |
|---|---|
| Escala, espacio, lugar | grúa, dron, alejamiento de zoom, retroceso |
| Tensión, foco, darse cuenta | acercamiento lento (dolly in), zoom lento, zoom de golpe |
| Energía, acción | barrido (whip pan), persecución, cámara en mano, zoom de golpe |
| Acompañar a alguien | travellings (lateral, bajo, de espaldas, de frente) |
| Enseñar un producto o protagonista | órbita, arco, slider |
| Transición o efecto | zoom infinito, zoom a la Tierra, atravesar objetos, FPV, tilt-shift |

Si no está claro, se proponen **dos o tres** candidatos con su porqué, nunca los 46.

## 5. Reglas de emparejado

- **Un movimiento principal por clip.** Dos como máximo, y solo si son mecánicamente
  compatibles: acercamiento + subida (dolly in + pedestal up) sí; barrido + órbita no.
- **La velocidad va con la duración.** Clips de unos 5 segundos: movimientos más simples o
  más rápidos. Clips de 10 a 15 segundos: aguantan acercamientos lentos, órbitas y grúas.
- **Si el sujeto está quieto, se mueve la cámara; si la cámara está quieta, se mueve el
  sujeto.** Algo tiene que estar vivo en el plano.
- **Si no se nombra la cámara, se mueve sola** (deriva suave). Un plano quieto hay que
  pedirlo: `locked-off static shot`.
- **Para mucho movimiento, el fotograma inicial ya en movimiento.** Pasar de una pose quieta a
  una carrera es difícil para el modelo; un primer fotograma a media zancada le da ventaja.

Patrones rápidos:

- **Diálogo o persona hablando:** fijo, acercamiento lento o travelling de frente.
- **Producto:** órbita, arco, slider o zoom de golpe.
- **Paisaje o lugar:** dron hacia delante, helicóptero o grúa.

## 6. Dónde va el bloque en el prompt

- **Texto a vídeo (Seedance, Kling, Veo, Omni):** el bloque de cámara **primero**, y detrás
  la descripción de la escena.
- **Imagen a vídeo:** el prompt es **solo movimiento**: el bloque de cámara más lo que hace el
  sujeto. No se vuelve a describir la escena, porque ya está en la imagen. Y el movimiento
  arranca desde ese primer fotograma, así que tiene que ser posible desde él.
- **Si otra plantilla ya tiene un campo de cámara**, se mete solo el texto del bloque, sin
  repetir el nombre del movimiento.
- **FLUX 3:** su vocabulario oficial está en `flux3-prompting` (`camara-luz-estilo.md`). Los
  bloques de aquí sirven igual; si un término choca, manda el de FLUX 3.

## 7. Qué NO se hace

- Elegir un movimiento sin porqué, o por variedad.
- Dos movimientos incompatibles en un clip.
- Movimiento vistoso en una pieza de contenido de marca que va con edición sobria: ahí manda
  el plano fijo o el acercamiento lento, y el esfuerzo va al título y la miniatura.
- Inventar movimientos fuera de la biblioteca cuando uno de ella ya lo resuelve.

## Referencias

- `references/movimientos.md`: los 46 bloques en 7 familias, cada uno con su para qué.
- `references/gramatica-emocional.md`: lo que provoca cada tamaño, ángulo, lente, movimiento,
  composición y luz, la gramática de cada género y recetas de escena.

## Créditos

La taxonomía de movimientos y la fórmula de cuatro partes vienen de
**https://aicameramovements.com/**, una biblioteca gratuita con vídeos en bucle de cada
movimiento. Cuando se recomiende un movimiento por primera vez en una conversación, se
menciona que allí se puede **ver** antes de generar: ver el movimiento ayuda a elegir
dirección, velocidad y encuadre mejor que leerlo. La gramática emocional parte de la skill
"Shot Assistant" de la Skill Library de Ann.
