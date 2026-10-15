# Plantillas

Los prompts van en inglés. Se rellenan; el esqueleto no se toca, porque cada bloque tiene su
trabajo. Donde pone `[REF estilo]` o `[REF personaje A]`, se nombra la referencia como la
entienda la herramienta y **siempre** con su línea de identidad al lado.

---

## 1. Storyboard a lápiz (GPT Image 2, o Nano Banana Pro)

```
REFERENCES (identity and shape ONLY: do NOT copy their color, grade or photoreal rendering):
[REF A] = [identity line of character or object A]. Identity and shape only, drawn in pencil.
[REF B] = [identity line of B]. Identity and shape only.
[REF C] = [location description]. Use as the environment and layout for every panel.

Use the references as exact locked designs, consistent across every panel.

Create a single landscape STORYBOARD SHEET titled "[TITLE]": storyboard only, no character
sheet, no swatches. NO color.

STYLE: rough black-and-white graphite pencil storyboard, grayscale only, loose gestural
linework, light hatching for depth, plain paper, thin panel borders, small hand-printed
captions BELOW each panel. Sketch the environment as a loose outline in every panel. It must
read as a rough pre-production sketch: do not push into the final look, grade, color or
photoreal rendering.

CONTENT: [N] panels, each with a caption using shot sizes (WS / MS / MCU / CU / ECU):
1. [SIZE]: [what happens, who is in frame, which way they move].
2. ...
(one line per approved moment; NO timestamps, NO dialogue)

LAYOUT: wide landscape, [N] panels in a clean [3x2 / 4x2] grid, generous size each.
```

**Si el storyboard va a ir como referencia del vídeo (placas limpias):** quitar las flechas y
los números de dentro de las viñetas, y los rótulos, pequeños y fuera o ninguno. Los números y
las flechas se cuelan en el vídeo.

**Casos especiales:**

- **Plano secuencia desde una cámara fija:** añadir "EVERY panel is framed from the SAME fixed
  camera. The camera never changes angle and never cuts. Only what happens inside the frame
  changes." y repetir el encuadre en cada línea.
- **Elemento en 3D dentro de imagen real** (producto gigante, criatura): "NOTE: [element] is
  high-end photoreal 3D in the final film; sketch it here only as a clean pencil silhouette".

---

## 2. Vídeo por planos (varios planos en una generación)

Cada plano repite: (1) el estilo fijado, (2) las líneas de identidad completas, (3) la
coletilla de acabado. Sí, es repetitivo: es el mecanismo.

```
[00:00-00:02] Shot 1: [style sentence: "Photorealistic cinematic [genre], matching the grade,
lighting and world of [REF style]"]. [shot size + camera block] as [REF A] ([full identity line])
[action]. [finish shorthand: lens, grade, grain]. Hard cut to Shot 2.

[00:02-00:04] Shot 2: [same skeleton: style repeated, identity lines repeated] ...

[00:XX-00:YY] Shot N (final beat): [action]. [something] lingering, motion staying alive through
the final frame. [finish shorthand].
```

- Unos **2 segundos por plano** es la regla de la fuente: 10 s son 5 o 6 planos; 15 s, 7 u 8.
  Si piden 15 momentos en 10 segundos, no se va a leer: se dice.
- Transiciones dichas: "Hard cut to Shot N", "Whip match-cut to Shot N".
- El bloque de cámara de cada plano sale de `direccion-de-camara`.

## 3. Plano secuencia (una toma sin cortes)

```
One seamless unbroken shot, no cuts, filmed entirely from [the locked camera]: [style and grade
sentence matching REF style]. The whole story plays out in this one continuous take and the
camera stays locked the entire time; it never cuts and never jumps to another angle.
[REF A] ([identity line]) [moment 1]... [every moment in order, in flowing prose, with the
sound cues woven in]... [final action] lingering, motion staying alive through the final frame.
```

## 4. Bloque de sonido

```
Natural diegetic sound only: [the specific sounds in story order: ambience, footsteps, key
sound effects, breaths]. High-quality sound effects and full sound design throughout.
No music, no score.
```

Solo si la voz y la música no van después en el montaje. Si van, audio desactivado.

## 5. Bloque de CONTINUIDAD (clip 2 en adelante, Seedance 2.0 con el clip anterior de referencia)

Va al principio del prompt. El clip anterior se describe en prosa; no lleva número de
referencia de imagen, y los números de las referencias de imagen no cambian respecto a los
clips anteriores.

```
CONTINUITY: this clip continues DIRECTLY from the attached reference VIDEO (the previous clip):
same location, same light, same [secondary characters] in the same positions, same pacing and
sound world. Pick up exactly where it ended: [one line describing the final state of the
previous clip].
```

## 6. Guardas

**Conteo y anatomía:**
```
Exactly [N] characters in this story: [NAME A] and [NAME B], never duplicated, never more than
one of each in frame unless a shot says so, correct anatomy, two arms and two hands each.
```

**Secundarios bloqueados:**
```
EXACTLY [N] [group], present in every wide shot, never disappearing, never changing count.
Their most visible member is [identity line].
```

**REGLA ABSOLUTA (si el storyboard va de referencia):**
```
ABSOLUTE RULE: the storyboard reference is for SHOT ORDER AND COMPOSITION ONLY. Zero pencil
style, zero panel borders, zero numbers or captions and absolutely no arrows may appear in any
frame.
```

---

## 7. Transiciones en cámara (fotograma inicial + fotograma final)

Se elige por lo que existe de verdad en los dos fotogramas. Máximo dos del mismo tipo por
pieza.

1. **Atravesar una puerta** (hay puerta o marco visible):
   ```
   The camera glides forward through the open doorway, the doorframe edges wipe across the frame in the foreground, and we emerge seamlessly into the next space, one continuous unbroken camera move, smooth gimbal motion, no cut.
   ```
2. **Cortinilla con pared o columna** (pared, columna o mueble alto cerca del borde):
   ```
   The camera pans laterally and a foreground wall passes fully across the frame, momentarily filling it, and as it clears we are revealed to be in the next space, invisible-cut transition, continuous camera move.
   ```
3. **Barrido** (vale siempre, con energía):
   ```
   Fast whip pan to the right with strong motion blur that fully abstracts the frame, decelerating smoothly to land composed on the next scene, in-camera whip pan transition, no visible cut.
   ```
4. **Fundido con destello** (ventana luminosa o lámpara en cuadro):
   ```
   The camera drifts toward the bright window until the frame blooms into white light flare, then the flare recedes revealing the next scene, elegant luminous transition, continuous move.
   ```
5. **Inclinación al suelo** (cambio de suelo o contraste fuerte entre planos):
   ```
   The camera tilts down to the floor texture, which morphs seamlessly into the floor of the next scene as the camera tilts back up, match-cut style continuous transition.
   ```

Siempre al final:
```
End exactly on the provided end frame composition, photorealistic, no morphing of objects.
```

---

## 8. Sacar el último fotograma de un clip

```bash
ffmpeg -sseof -0.15 -i clip_N.mp4 -frames:v 1 -q:v 2 ultimo_N.jpg -y
```

`-sseof -0.15` coge el fotograma 0,15 s antes del final, para evitar los negros del último
grupo de fotogramas. Si sale negro o borroso, repetir con `-sseof -0.4`. Sin ffmpeg a mano, una
captura del último fotograma en el editor sirve igual.

Antes de usarlo, **mirarlo**: si está corrupto o tiene cosas inventadas, se usa la imagen
original del plano (sección 9 de la skill, antideriva).
