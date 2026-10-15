# Varios planos y continuidad en FLUX 3

Fuente: cookbook oficial "Multi-shot films" y skill `flux-3-keyframes-continuation` de
Black Forest Labs. Consultado el 2026-09-09.

Una generación tiene un tope de 20 segundos. Una pieza, no. Hay dos formas de alargar y se
usan para cosas distintas.

---

## 1. Cortes dentro de una sola generación

Se escriben los planos en el prompt y el modelo ejecuta cortes de verdad, con un solo
soundtrack cosiéndolos.

```
SHOT ONE: wide aerial of a desert highway at dawn, a single red car speeding through.
HARD CUT. SHOT TWO: interior close-up, the driver's hands drumming the wheel to the radio.
HARD CUT. SHOT THREE: from the roadside, the car shrinking into the heat haze.
Warm engine hum under one continuous music bed across all three shots.
```

Dos cosas hacen que el corte se lea como corte:

**Los planos seguidos tienen que contrastar fuerte**, y el contraste más potente es la
escala. Macro, luego general, luego aéreo se lee como tres cortes deliberados. Tres ángulos
parecidos se funden en una sola toma que deriva.

**Una sola idea de audio cruzando todos los planos.** Si nombras una base continua, los
cortes se leen como montaje. Si no, parece zapeo.

**Tope: dos o tres planos por generación.** Más que eso es trabajo del método siguiente.

---

## 2. Una pieza como lista de planos

A partir de tres o cuatro planos, cada plano es su propia generación y luego se montan.
Tiene ventajas reales sobre una generación larga: los planos se lanzan en paralelo, un fallo
cuesta un plano y no la pieza entera, y el control del ritmo se queda en montaje.

Lo que sostiene una pieza hecha de varias generaciones:

### 2.1 La biblia del mundo

Un párrafo que describe el mundo (sitio, paleta, luz, acabado) y que se pega en **todos**
los prompts **palabra por palabra**.

> Consistency across generations comes from consistent text, so copy it, don't paraphrase
> it per shot.

Esto es literal: **copiar, no reescribir**. Parafrasear la biblia en cada plano es la forma
más común de que la pieza no case.

```
The world: a vast Victorian glasshouse after closing, at night. Moonlight and a few sodium
service lamps glow through fogged, dripping glass. Wet leaves, black soil, brass pipes and
old iron staging. Deep green-and-amber palette, soft film grain, gentle slow-drifting
camera, photorealistic. No on-screen text.
```

### 2.2 Un motivo de audio

La misma idea musical nombrada en cada plano, colocada según dónde cae ese plano en la
pieza: entra, se calienta, crece, resuelve. Tú cortas la imagen; el motivo lleva el hilo.

```
Audio: a slow, sparse celeste melody with a glass-bell tone enters quietly, under dripping
water...
Audio: ...continues, warmer and a little fuller...
Audio: ...builds, another voice joining it...
Audio: ...resolves and fades to a single held note...
```

### 2.3 Un momento por plano

Cada plano hace una cosa. La pieza es la secuencia, no ningún clip suelto.

### 2.4 El montaje

Cortes secos en el orden del guion. Sin fundidos: los planos se escribieron para contrastar
y el motivo de audio ya lleva la continuidad.

---

## 3. Personaje recurrente

Dos herramientas, y hacen cosas distintas:

- **La biblia del mundo** sostiene el mundo.
- **Las imágenes de referencia** sostienen una cara.

Aviso importante y documentado: no existe ningún campo que lleve la identidad de un sujeto
**sin poner esa imagen en pantalla**. Con `keyframes`, la imagen aparece píxel a píxel. Si
necesitas que el personaje salga en un plano nuevo sin que se vea la imagen original, hay
que describirlo con palabras, y entonces la identidad no está garantizada.

Para la voz, lo mismo: repetir la dirección de voz conserva **un tipo de voz**, no al mismo
actor. Escucha los planos seguidos antes de montarlos.

---

## 4. Continuar un clip (`v2v`)

Se escribe **desde el final**, no se resume lo que ya pasó. Se dice qué ocurre a
continuación y qué cruza la frontera: inercia, encuadre, sujetos y sonido.

```
The camera continues a slow push-in as the closed flower opens naturally into the final
bloom. The stem remains fixed in place, the same soft morning light holds across the shot,
and a light breeze moves the surrounding leaves without changing the composition.
```

```
Continue from the rider's existing forward momentum. The camera keeps the same low trailing
angle as the horse crests the hill and enters dense fog; hoofbeats and wind carry across
the boundary without a reset.
```

Para cadenas de varios tramos: conserva un final limpio, apunta la dirección, la velocidad y
la relación con la cámara, continúa desde el archivo real del final, repite solo lo
invariable más la acción siguiente, y revisa cada costura antes de seguir. Si hay deriva,
cambia **una** variable de continuidad por intento.

Recuerda que `v2v` cuesta dos veces y media un plano nuevo (ver `api-parametros.md`, apartado 5).

---

## 5. Keyframes: cada forma se prompted distinto

| Lo que necesitas | Petición |
|---|---|
| Que esos píxeles exactos abran el clip | `i2v`, `keyframes`: una imagen |
| Primer y último fotograma exactos, relleno en medio | `i2v`, `keyframes`: dos imágenes |
| Un storyboard ordenado que el modelo une | `i2v`, `keyframes`: 3 a 10 imágenes más `duration` entero |
| Fotogramas clavados en momentos exactos | `i2v`, `keyframes`: pares `[segundo, imagen]` ascendentes, más `duration` entero |
| Seguir desde donde acaba este clip | `v2v`, `start_video` |

- **Una imagen:** describe **lo que se mueve**. Volver a describir lo que ya se ve en la
  imagen invita al modelo a reimaginarlo.
- **Dos imágenes:** describe las etapas del cambio en orden y deja la cámara quieta. Que los
  dos extremos guarden relación: los saltos grandes provocan deriva.
- **Storyboard:** mantén identidad, paleta y punto de vista coherentes salvo que el cambio
  sea intencionado.
- **Fijados por tiempo:** un keyframe a mitad de clip es una fecha de entrega. Di para qué
  son los segundos que quedan después, o se van a apagar solos. Fija solo lo que importe:
  demasiadas anclas agarrotan el movimiento.

---

## 6. Cuándo NO alargar dentro de la generación

Si el plano necesita:

- varias réplicas completas de diálogo (ver `dialogo-literal.md`, apartado 8)
- varios sitios distintos
- un mecanismo exacto de varios pasos
- tiempos exactos entre acciones

entonces no es un plano: son varios. Partirlo es más barato que repetirlo.
