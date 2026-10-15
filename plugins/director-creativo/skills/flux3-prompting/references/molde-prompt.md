# Cómo se escribe un prompt de FLUX 3

Fuente: `docs.bfl.ai` (guías "Text-to-Video", "Video Generation with FLUX", "Audio and
speech") y las skills oficiales de Black Forest Labs. Consultado el 2026-09-09.

---

## 1. La regla que manda sobre todas

**Se escribe en prosa, dirigiendo una escena.** No en lista de palabras clave, no en
etiquetas sueltas, no en estilo de pie de foto.

> Write the way you would brief a colleague on the shot. Keyword lists and caption-style
> prose both under-perform prose written the way you'd say it out loud.

Y la segunda, que corrige el instinto de amontonar adjetivos:

> An extra adjective on "warm afternoon light" rarely helps, but a new beat like "the cat's
> ear twitches on the thunder roll" almost always does.

Un prompt que nombra **de cinco a diez momentos concretos** gana a uno con cuarenta
adjetivos. Antes de añadir, aprieta.

---

## 2. Los cuatro formatos, y cuándo usa cada uno

FLUX 3 entiende varios formatos. No hay uno correcto: hay uno adecuado por trabajo.

### 2.1 Frase corta

Para explorar rápido y para B-roll sin exigencias.

```
A red fox leaping through fresh snow, telephoto.
```

El modelo rellena encuadre, movimiento y ambiente. Sale fresco y sale imprevisible.

### 2.2 Lenguaje natural largo (el que usarás casi siempre)

La forma por defecto. Una sola prosa con esta silueta:

```
[cámara] shot of [sujeto] [acción] in [entorno]. [detalles de movimiento y luz]. [audio].
```

```
A cozy ramen shop on a rainy Tokyo night: steam rising from the broth, neon reflections in
the window puddles, the cook working calmly. The camera drifts slowly past the counter.
Rain patter and quiet kitchen sounds.
```

### 2.3 Campos etiquetados

Cuando quieres tocar una palanca sin mover las demás.

```
Camera shot: wide shot, low angle
Subject + action: a lone rider crosses a shallow desert river
Depth of field: shallow (sharp on subject, blurred background)
Lighting + palette: warm backlight with soft rim - amber, cream, walnut
Motion: water splashes around the horse's legs, orange dust hangs in the light
Style: epic western realism
```

### 2.4 Por marcas de tiempo

Cuando la acción tiene que caer **en un momento concreto**. Dos o tres momentos por cada
cinco segundos, no más.

```
0.0-1.5s - locked wide of a still harbor at dawn, boats motionless on glassy water
1.5-3.0s - a slow push-in begins as gulls lift off the water
3.0-5.0s - the sun breaks the horizon, warm light spreads and the camera settles
```

---

## 3. El esquema largo, para piezas de varios planos

Cuando un look y una historia tienen que aguantar a lo largo de varios planos dentro de una
misma generación, BFL propone este esquema de seis bloques. No es obligatorio; es la
herramienta cuando la coherencia importa.

```yaml
Core summary: [una línea con la secuencia entera: quién, dónde, y el arco]

Scene:
  Shot 1: [sitio, calidad de luz, profundidad de campo]
  Shot 2: [...]

Subject description: [descripción fija del personaje, IDÉNTICA en todos los planos]

Dynamic narrative:
  Shot 1 [0.0s-2.5s]: [movimiento de cámara + acción del sujeto]
  Shot 2 [2.5s-5.0s]: [...]

Audio:
  Shot 1: [capas de sonido de ese plano]
  Shot 2: [...]

Style and color: [realismo, paleta, grano: lo que une todos los planos]
```

La clave del esquema es `Subject description`: **el mismo texto exacto en cada plano**. La
identidad se sostiene por repetición literal, no por describir "lo mismo" con otras palabras.

---

## 4. Audio: cuatro capas, y se nombran una a una

FLUX 3 genera el sonido en la misma pasada que la imagen. Si no lo describes, se lo inventa.

| Capa | Qué se describe | Ejemplo |
|---|---|---|
| **Habla** | Quién habla, las palabras exactas y cómo las dice | `The mechanic says, "Try it now." Quiet, matter-of-fact delivery.` |
| **Ambiente** | El sonido del sitio | `Rain against the windows, low diner chatter, refrigerator hum` |
| **Efectos** | Sonidos atados a algo que se ve | `A ceramic mug clicks against the saucer` |
| **Música** | Estilo, ritmo y dónde se coloca en la mezcla | `A sparse piano cue under the scene, low in the mix` |

No hacen falta las cuatro. Un plano hablado suele necesitar solo habla y tono de sala.

Molde:

```
[Plano y acción].
Dialogue or voiceover: [quién y las palabras exactas].
Ambience: [el sitio].
Effects: [acciones visibles].
Music: [estilo y papel].
```

### 4.1 Nombra la fuente, no el estado de ánimo

`Distant traffic and rain ticking against a metal awning` funciona. `Moody ambience` no.

### 4.2 El silencio se pide nombrando un sonido, no pidiendo silencio

Contraintuitivo y está documentado: pedir `quiet room tone` puede colapsar en ruido o en
vacío absoluto. Se nombra una fuente suave real.

Para que **no haya música**, se dice explícitamente, porque las escenas tensas tienden a
traerla sola:

```
Absolutely no music, no on-screen text.
```

Para un plano mudo de verdad, el parámetro: `generate_audio: false`.

### 4.3 Los efectos son causales

No una lista suelta. Se atan a lo que se ve:

```
As the cup hits the tile, it cracks with one sharp ceramic snap.
```

### 4.4 Qué manda en la mezcla

Se dice qué va delante y qué se queda debajo:

```
Her line is foreground and fully intelligible. Café chatter and espresso hiss remain low
and diffuse. A restrained piano pulse enters beneath the final words without masking them.
```

Y si hay una línea que importa, **fuera las voces de fondo**. La radio hablando y la gente
charlando se comen las palabras.

---

## 5. Presupuesto de acción por plano

De la skill oficial `flux-3-prompt-doctor`:

> **Action budget:** one subject action and one camera move per short clip.

Un plano corto aguanta **una acción del sujeto y un movimiento de cámara**. Si el encargo
pide varias acciones seguidas, varios sitios, un mecanismo exacto o varias réplicas
completas de diálogo, el encargo hay que repararlo, no generarlo.

Regla de duración por momentos, no por segundos:

| Lo que hay | Duración |
|---|---|
| Un solo momento | 5 s |
| Principio y final | 7-10 s |
| Tres cortes, cada uno con su aire | 12-18 s |

`duration: "auto"` mientras exploras. Se fija el número en cuanto la duración sea un
requisito.

---

## 6. Contradicciones que hay que cazar antes de generar

La skill oficial `flux-3-prompt-doctor` lista las que rompen un plano. Si tu prompt tiene
una de estas, el resultado será un promedio de las dos órdenes:

- cámara fija más cámara que sigue al sujeto
- primerísimo plano más plano general
- conservar el encuadre exacto más un cambio geométrico grande
- un plano continuo más cortes duros
- tipografía generada que es crítica para producción y no hay plan B en montaje
- identidad garantizada del mismo hablante entre generaciones distintas

---

## 7. Cómo se itera

**Una palanca por intento.** Cuando el resultado está cerca pero falla en una cosa (la luz,
la música, un detalle del sujeto), se fija esa capa y **se deja el resto del prompt intacto**.
Reescribirlo entero mueve también lo que ya te gustaba.

Después de dos fallos con la misma forma, el problema no son los adjetivos: es el concepto
o el método de producción.

Escalera de cambios, en este orden: geometría del suceso, luego material o luz, luego
composición, luego duración.
