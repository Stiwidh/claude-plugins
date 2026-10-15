---
name: continuidad-y-pruebas
description: Que una pieza de varios clips generados parezca una sola película y que el vídeo caro no se queme a ciegas. Inventario de assets antes de generar, referencias bloqueadas con línea de identidad literal, orden de referencias, prueba barata antes del render final, encadenar clips uno detrás de otro, guardas contra personajes duplicados y finales congelados, y transiciones en cámara con fotograma inicial y final. Trigger keywords - varios clips, el personaje cambia de cara entre planos, se duplica el personaje, desaparecen los de fondo, continuidad, encadenar clips, que un clip siga al anterior, prueba antes del final, test barato, 480p, transición entre planos, fotograma inicial y final, lista de assets, qué genero primero, hoja de personaje, storyboard a lápiz.
---

<!--
@SHARED_WITH
  Copia adaptada para la comunidad de Protocolo EVA. Tiene gemelas internas: un cambio de doctrina se replica a mano en todas. Registro: SHARED_COMPONENTS.md
-->

# Continuidad y pruebas

Dos problemas y un mismo método. El primero: en una pieza de varios clips, el personaje cambia
de cara, los de fondo desaparecen y la luz salta de un plano a otro. El segundo: el vídeo es lo
caro, y equivocarse en el render final cuesta el render final entero.

La respuesta es la misma: **decidir en lo barato y bloquear antes de lo caro.** Cambiar de
idea en un boceto cuesta casi nada; en un clip a 1080p cuesta créditos o puntos.

Adaptado de "The Storyboard Method", "Production Suite" y "Real Estate Video Tours" (Skill
Library de Ann), con lo que admite cada herramienta **verificado el 2026-09-30** contra el
catálogo vivo de Higgsfield y lo que ofrece Google Flow (que se usa a mano, en el navegador).

**Cuándo se usa:** pieza con dos o más clips de vídeo generado, personaje, producto o lugar que
sale en más de un plano, o cualquier tanda de vídeo que merezca una prueba antes.

---

## 1. Inventario antes de generar nada

Leer el guion entero (sin saltar escenas) y sacar todo lo que hay que generar, con las escenas
en que aparece:

- **Personajes**, incluidos los de fondo.
- **Looks:** una entrada por cada cambio de ropa de cada personaje.
- **Lugares:** con su variante de hora y clima (la misma calle de día y de noche son dos).
- **Objetos** que se tocan o se enseñan, **vehículos**, **animales**.
- **Efectos** (fuego, lluvia, humo).
- **Apoyos:** carteles, pantallas, documentos, logos.

Cada uno se clasifica:

- **Reutilizable** (sale en 2 o más escenas): se construye una vez y se referencia en todas.
- **Único** (una escena): vale un método más barato y va al final.
- **Riesgo alto** (caras, texto dentro de la imagen, criaturas complejas): necesita hoja de
  referencia.

Y el orden de generación sale solo: **P1** reutilizable + riesgo alto (todo lo demás depende
de esto), **P2** reutilizable sencillo, **P3** únicos.

**Huecos del guion (obligatorio):** lo que el guion nombra y nunca describe ("en la escena 7
aparece el aparato" y nunca se dice cómo es). Encontrarlos antes de producir es la mitad del
valor del inventario.

## 2. El estilo, fijado

Con dos o más clips, un **fotograma de estilo** como referencia en todos los planos (modo
FIJAR de la skill `estilo-visual`).

## 3. Referencias bloqueadas

Por cada elemento recurrente, una referencia aprobada y una **línea de identidad**:

| Elemento | Referencia |
|---|---|
| Persona real (quien sale en cámara) | Personaje Soul entrenado (skill `soul-id`) |
| Personaje inventado | Hoja de personaje; una vez aprobado el diseño, **hoja de giro**: frente, tres cuartos, perfil, espalda y primer plano de cara, en una sola hoja horizontal y en el estilo fijado. La hoja de giro, no el primer boceto, es la referencia de ahí en adelante |
| Lugar | Una referencia de entorno |
| Producto u objeto protagonista | Una referencia limpia |

Para hojas de personaje y trabajo con referencias de identidad, la skill oficial de
Higgsfield recomienda Nano Banana 2 o Pro.

**La línea de identidad** es una frase ("mujer joven, piel clara, pelo oscuro largo y
ondulado, ojos gris azulado, vestido de satén plateado") que se repite **palabra por palabra**
cada vez que ese elemento aparece en un prompt. Es repetitivo a propósito: la repetición es el
mecanismo que mantiene la identidad entre planos.

**Pocas referencias.** La fuente recomienda de 2 a 4 en total: cuantas más, más formas tiene
el modelo de confundirse.

## 4. El orden de las referencias

Las referencias se numeran por el orden en que se adjuntan. Orden fijo: **personajes, objetos
y lugar primero; el fotograma de estilo después; el storyboard, si va, el último.** Si el
prompt nombra las referencias por número, los números tienen que coincidir con ese orden: un
desajuste es la primera causa de que se intercambien las identidades.

- **Google Flow (modo Ingredientes):** las fotos van en orden y la primera pesa más; en un personaje,
  la foto de la cara primero.
- **Higgsfield:** Seedance 2.0 acepta varias referencias de imagen (`image_references`). Si
  entiende etiquetas tipo "@Image 1" dentro del prompt **no está verificado**; mientras no se
  pruebe, cada referencia se nombra con su línea de identidad, no solo con un número.

## 5. Storyboard a lápiz (opcional, el paso más barato)

Una hoja horizontal con una viñeta por momento del guion, **a lápiz en blanco y negro**. Sirve
para decidir encuadres y orden antes de gastar en vídeo. Se hace con un modelo fuerte en
maquetación y texto (GPT Image 2; si no está a mano, Nano Banana Pro con el mismo prompt).
Plantilla en `references/plantillas.md`.

- Solo lápiz: un boceto demasiado acabado se pelea con el estilo fijado.
- Las referencias, **solo para identidad y forma** ("do NOT copy color or photoreal
  rendering"), o salen viñetas fotográficas.
- **Sin tiempos ni diálogos** en las viñetas: el tiempo y la voz van en el prompt de vídeo.
- **Si el storyboard va como referencia al vídeo, placas limpias**: sin números dentro de las
  viñetas, sin flechas, con los rótulos pequeños y fuera. Los números y las flechas se cuelan en
  el vídeo aunque se pida que no.

Se itera aquí (cambiar viñetas, reordenar, cambiar encuadres) hasta que se aprueba.

## 6. Prueba barata antes del final

**Mismo prompt, mismas referencias, mismo orden. Solo cambian el modo y la resolución.**

| Dónde | Prueba | Final |
|---|---|---|
| Higgsfield · Seedance 2.0 | `mode: fast`, 480p (fast solo admite 480p o 720p) | `mode: std`, 1080p |
| Higgsfield · Kling 3.0 | `mode: std` | `mode: pro` (4k solo si se pide) |
| Google Flow (a mano) | Omni 1.1 Flash o Veo 3.1 Lite | Veo 3.1 Quality |

- **El coste se lee siempre de la herramienta** (lo que enseña Higgsfield antes de generar, o
  lo que declara Google Flow en pantalla antes de lanzar), nunca de una tabla, y se enseña
  antes. La prueba lleva su propio OK y el final el suyo.
- **Qué enseña la prueba:** ritmo, encuadre, identidad y si el prompt se entiende. **Qué no
  garantiza:** el acabado del final, sobre todo en Google Flow, donde la prueba y el final son
  modelos distintos. Si la prueba falla, se arregla **el prompt** (no el storyboard, salvo que
  falle el momento en sí) y se vuelve a probar.

## 7. Encadenar clips

Cuando un clip **continúa** al anterior (misma acción, mismo sitio), se generan **de uno en
uno y en orden**, nunca en paralelo: clip 1, aprobado; clip 2 a partir del 1, aprobado; y así.

- **Seedance 2.0 (Higgsfield):** el clip anterior **entero** va como referencia de vídeo
  (`video_references`, el rol existe, verificado el 2026-09-30), y el prompt abre con el bloque
  de CONTINUIDAD de `references/plantillas.md`. La fuente dice que así los de fondo no
  desaparecen y se mantienen posiciones, ritmo y sonido mejor que con solo el último
  fotograma; **aquí no está medido todavía**: la primera vez, comparar.
- **Kling 3.0, Veo 3.1 y Google Flow (modo Fotogramas):** no admiten vídeo como referencia. Se
  saca el **último fotograma** del clip anterior y va como fotograma inicial del siguiente
  (`start_image` en Higgsfield, el fotograma inicial en Flow). Extracción en `references/plantillas.md`.

**Cuándo NO se encadena:** planos independientes separados por un corte seco, cada uno con su
momento. Esos se lanzan en paralelo y el ritmo se decide en el montaje (así lo hace también
`flux3-prompting` en su multiplano).

## 8. Guardas dentro del prompt

- **Conteo exacto de personajes y anatomía:** "exactly two characters in this story: THE MAN
  and THE KID, never duplicated, never more than one of each in frame, correct anatomy, two arms
  and two hands each".
- **Los de fondo, bloqueados:** si tienen que seguir ahí, número exacto ("EXACTLY FIVE boys,
  present in every wide shot, never changing count") más la línea de identidad del más visible,
  repetida en cada clip. Sin bloquear, desaparecen entre generaciones.
- **Final vivo:** el último plano mantiene el movimiento ("...motion staying alive through the
  final frame") para que el clip no se congele de golpe. Compatible con el `End` del bloque de
  cámara: el plano llega a su composición final sin pararse en seco.
- **El audio, decidido:** Seedance 2.0 genera audio por defecto (`generate_audio: true`). Si la
  voz o la música van luego en el montaje, se desactiva o se pide solo sonido diegético. La
  fuente defiende "solo sonido diegético, sin música" como más premium; es su criterio, no un
  dato medido.
- **Si el storyboard va de referencia:** bloque de REGLA ABSOLUTA al principio (solo orden y
  composición; cero lápiz, marcos, números o flechas en ningún fotograma).

## 9. Transiciones en cámara

Una transición que parece rodada, no editada: un clip corto con **fotograma inicial = último
fotograma del plano anterior** y **fotograma final = primer fotograma del siguiente**.

- **Dónde se puede:** Kling 3.0 y Seedance 2.0 en Higgsfield (`start_image` + `end_image`,
  verificado), y Google Flow en modo Fotogramas (fotograma inicial + final). **Veo 3.1 en Higgsfield no admite
  fotograma final.**
- Duración corta: Kling 3.0 desde 3 segundos, Seedance 2.0 desde 4.
- **Se elige por lo que existe en los dos fotogramas** (una puerta, una pared, una ventana
  luminosa). Biblioteca de cinco en `references/plantillas.md`.
- Máximo **dos del mismo tipo** por pieza, para que no se note la fórmula.
- **Solo donde aporta:** el resto de cambios de plano, corte seco (sin generación).
- **Antideriva:** si el último fotograma sale corrupto o inventado, se usa la imagen original
  del plano como inicio. Un pequeño salto es mejor que una transición desde un fotograma roto.
- Se generan **después** de aprobar los planos que unen, nunca antes.

## 10. Texto en pantalla

La regla del plugin se mantiene: **el texto en vídeo generado no se genera, se diseña** y se
pone en el montaje. La fuente propone otra vía (generar la cartela como imagen de referencia y
pedir al vídeo que la respete); **no está probada aquí** y no es la vía por
defecto.

## 11. En el montaje

- **Recortar cabezas y colas muertas:** los clips generados suelen arrancar o acabar con
  fotogramas casi quietos. Se recortan antes de montar, como haría un montador.
- Vídeo y voz por separado, para poder cambiar uno sin volver a generar el otro.

## 12. Al entregar

Lista de todo lo fijado: fotograma de estilo, referencias con su línea de identidad, orden de
referencias, storyboard aprobado y prompts finales. Con eso la pieza se puede rehacer o
ampliar otro día sin empezar de cero.

## Referencias

- `references/plantillas.md`: prompt del storyboard a lápiz, prompt de vídeo por planos y de
  plano secuencia, bloques de CONTINUIDAD, guardas y REGLA ABSOLUTA, biblioteca de
  transiciones y extracción del último fotograma.
