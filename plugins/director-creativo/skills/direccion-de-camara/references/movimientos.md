# Biblioteca de movimientos de cámara: 46 bloques en 7 familias

Fuente: https://aicameramovements.com/ (vídeos en bucle de cada movimiento). Adaptado de la
skill "AI Camera Movements".

Cada bloque sigue `nombre. Movement: ... Speed: ... Framing: ... End: ...` y va **en inglés
dentro del prompt**. Se pega ANTES de la descripción de la escena (o solo, en imagen a vídeo).
Dirección y palabras de velocidad se cambian libremente; el esqueleto de cuatro partes no.

## Índice

1. Paneo e inclinación (7)
2. Zoom y lente (6)
3. Dolly y travelling (9)
4. Desplazamientos físicos (11)
5. Cámara humana (2)
6. Dron y grúa (5)
7. Especiales (6)

Al final: tabla de compatibilidad por objetivo.

---

## 1. Paneo e inclinación (la cámara gira desde un punto fijo)

### Plano fijo
Para: diálogo, cuadros estáticos, dejar que la acción ocurra dentro de un encuadre estable.
```
locked-off static shot. Movement: the camera holds a single fixed position for the entire clip. Speed: completely still. Framing: angle, height, lens distance and composition never change. End: identical framing to the opening frame.
```

### Paneo a la derecha
Para: descubrir espacio nuevo, seguir una acción lateral.
```
pan right. Movement: the camera rotates horizontally left-to-right from a fixed position. Speed: smooth, even rotation. Framing: horizon stays level as fresh space enters from the right edge. End: come to rest on a clear final composition.
```

### Paneo a la izquierda
```
pan left. Movement: the camera rotates horizontally right-to-left from a fixed position. Speed: smooth, even rotation. Framing: horizon stays level as fresh space enters from the left edge. End: come to rest on a clear final composition.
```

### Barrido a la derecha (whip pan)
Para: energía, transición entre escenas, revelado cómico.
```
whip pan right. Movement: the camera snaps its rotation quickly toward a new target on the right. Speed: very fast, with brief motion blur mid-rotation. Framing: start on one readable composition, land on a second readable target. End: settle sharply on the new frame.
```

### Barrido a la izquierda
```
whip pan left. Movement: the camera snaps its rotation quickly toward a new target on the left. Speed: very fast, with brief motion blur mid-rotation. Framing: start on one readable composition, land on a second readable target. End: settle sharply on the new frame.
```

### Inclinación hacia arriba (tilt up)
Para: revelar altura (edificios, personajes, escala).
```
tilt up. Movement: the camera rotates upward from a fixed position. Speed: smooth, constant tilt. Framing: the vertical subject or architecture stays centered as the frame climbs. End: land on the upper target.
```

### Inclinación hacia abajo (tilt down)
```
tilt down. Movement: the camera rotates downward from a fixed position. Speed: smooth, constant tilt. Framing: the vertical subject or architecture stays centered as the frame descends. End: land on the lower target.
```

---

## 2. Zoom y lente (cambia la focal, la cámara no se mueve)

### Zoom lento hacia dentro
Para: construir tensión, llevar la atención a un detalle.
```
slow zoom in. Movement: focal length increases gradually toward a tighter frame. Speed: slow and even. Framing: the main target stays readable as it grows in frame. End: rest on a stable, tighter composition.
```

### Zoom lento hacia fuera
Para: revelar contexto, distancia emocional.
```
slow zoom out. Movement: focal length decreases gradually toward a wider frame. Speed: slow and even. Framing: the main target stays readable as surrounding space appears. End: rest on a stable, wider composition.
```

### Zoom rápido hacia dentro
```
fast zoom in. Movement: focal length increases quickly toward the main target. Speed: quick and decisive. Framing: the target stays centered and readable through the scale change. End: rest on a stable, tighter composition.
```

### Zoom rápido hacia fuera
```
fast zoom out. Movement: focal length decreases quickly away from the main target. Speed: quick and decisive. Framing: the target stays readable as surrounding space appears. End: rest on a stable, wider composition.
```

### Zoom de golpe hacia dentro (crash zoom)
Para: énfasis cómico o dramático con pegada, revelado de producto.
```
crash zoom in. Movement: the lens snaps rapidly toward the main target. Speed: extremely fast and punchy. Framing: the target stays readable despite the sudden scale change. End: land on a bold, tight composition.
```

### Zoom de golpe hacia fuera
```
crash zoom out. Movement: the lens snaps rapidly away from the main target. Speed: extremely fast and punchy. Framing: the target stays readable as surrounding space rushes in. End: land on a bold, wide composition.
```

---

## 3. Dolly y travelling (la cámara viaja físicamente)

### Acercamiento (dolly in)
Para: intimidad, tensión, entrar en una escena.
```
dolly in. Movement: the camera physically travels forward in a straight line toward the subject. Speed: smooth, controlled push. Framing: height, lens direction and subject placement stay consistent while distance closes. End: rest on a tighter composition.
```

### Alejamiento (dolly out)
Para: aislamiento, revelar el entorno.
```
dolly out. Movement: the camera physically travels backward in a straight line away from the subject. Speed: smooth, controlled retreat. Framing: height and lens direction stay consistent while more environment enters frame. End: rest on a wider composition.
```

### Travelling
Para: acompañar a un sujeto por la escena, en general.
```
tracking shot. Movement: the camera travels through the scene together with the subject. Speed: matched to the subject's pace. Framing: the subject stays consistently readable while the environment flows past. End: hold a clear moving composition.
```

### Seguimiento por la espalda / sobre el hombro
Para: trayectos, historias casi en primera persona.
```
follow shot from behind. Movement: the camera trails the subject along their route at shoulder height. Speed: matched to the subject's pace. Framing: the back, shoulder or head serves as a foreground guide while the path ahead stays readable. End: keep following with the subject leading the frame.
```

### Travelling de frente (walk and talk)
Para: diálogo en movimiento, emoción de frente.
```
reverse tracking shot. Movement: the camera travels backward directly in front of the walking subject. Speed: matched to the subject's forward pace. Framing: face and body stay stable and front-facing while the background recedes behind them. End: hold a clean front-facing moving composition.
```

### Travelling lateral
Para: perfiles, carreras, movimiento en paralelo.
```
side tracking shot. Movement: the camera travels parallel to the subject along their direction of travel. Speed: matched to the subject's motion. Framing: the subject holds a side or three-quarter profile at constant distance. End: keep the parallel motion with clear horizontal flow.
```

### Travelling bajo
Para: pies, ruedas, drama a ras de suelo.
```
low tracking shot. Movement: the camera travels at ground or below-waist height alongside the subject's path. Speed: matched to the footsteps or wheels. Framing: the low detail stays readable while the ground plane streams through frame. End: keep the low perspective intact.
```

### Travelling de vehículo
```
vehicle tracking shot. Movement: the camera travels with the vehicle along its route. Speed: matched to the vehicle. Framing: the vehicle stays stable in frame while road and scenery stream past. End: hold a clear moving-vehicle composition.
```

### Persecución
Para: acción, urgencia.
```
chase shot. Movement: the camera pursues a fast-moving subject along the action route. Speed: fast, reactive, physically close. Framing: the subject stays visible while the frame reframes energetically. End: stay locked onto the subject in motion.
```

---

## 4. Desplazamientos físicos (laterales, verticales, curvos)

### Desplazamiento lateral a la derecha (truck right)
Para: revelados laterales con la lente mirando siempre al frente.
```
truck right. Movement: the camera travels physically rightward on a straight horizontal path. Speed: smooth, constant lateral travel. Framing: the lens keeps facing the same direction while the scene slides across frame. End: rest on a clean lateral composition.
```

### Desplazamiento lateral a la izquierda (truck left)
```
truck left. Movement: the camera travels physically leftward on a straight horizontal path. Speed: smooth, constant lateral travel. Framing: the lens keeps facing the same direction while the scene slides across frame. End: rest on a clean lateral composition.
```

### Subida vertical (pedestal up)
Para: revelar subiendo, sin inclinar la cámara.
```
pedestal up. Movement: the whole camera travels straight up. Speed: smooth, constant lift. Framing: the lens stays level and pointed the same way throughout the rise. End: hold the higher framing clearly.
```

### Bajada vertical (pedestal down)
```
pedestal down. Movement: the whole camera travels straight down. Speed: smooth, constant descent. Framing: the lens stays level and pointed the same way throughout the drop. End: hold the lower framing clearly.
```

### Slider a la derecha
Para: paralaje sutil, planos bonitos de producto.
```
slider right. Movement: the camera glides a short distance to the right. Speed: slow, controlled, constant. Framing: foreground, subject and background layers stay readable as parallax shifts between them. End: rest on a refined composition from the new right-side angle.
```

### Slider a la izquierda
```
slider left. Movement: the camera glides a short distance to the left. Speed: slow, controlled, constant. Framing: foreground, subject and background layers stay readable as parallax shifts between them. End: rest on a refined composition from the new left-side angle.
```

### Pasar por delante de un objeto (push past)
Para: profundidad, entrar en un espacio pasando junto a algo en primer término.
```
push past. Movement: the camera advances past a visible foreground object, edge or opening. Speed: smooth forward glide. Framing: the foreground brushes close to the lens while the space beyond sharpens into view. End: arrive inside or beyond the foreground layer.
```

### Arco a la derecha
Para: cambiar de ángulo alrededor del sujeto con suavidad.
```
arc right. Movement: the camera travels a shallow curved path around the subject toward its right side. Speed: smooth, measured curve. Framing: distance, height and subject readability stay constant as the angle shifts. End: rest at a new right-side angle.
```

### Arco a la izquierda
```
arc left. Movement: the camera travels a shallow curved path around the subject toward its left side. Speed: smooth, measured curve. Framing: distance, height and subject readability stay constant as the angle shifts. End: rest at a new left-side angle.
```

### Órbita en sentido horario
Para: plano héroe o de producto, revelados de 360 grados.
```
clockwise orbit. Movement: the camera circles clockwise around the subject at a constant radius. Speed: smooth, controlled orbit. Framing: the subject stays centered while the background rotates behind it. End: complete the planned arc or full circle with stable framing.
```

### Órbita en sentido antihorario
```
counterclockwise orbit. Movement: the camera circles counterclockwise around the subject at a constant radius. Speed: smooth, controlled orbit. Framing: the subject stays centered while the background rotates behind it. End: complete the planned arc or full circle with stable framing.
```

---

## 5. Cámara humana

### Cámara en mano
Para: realismo, aire documental, energía nerviosa.
```
handheld shot. Movement: the camera is carried at operator height with natural body motion. Speed: responsive and organic. Framing: the subject stays readable through subtle sway and micro-adjustments of the frame. End: settle into a natural handheld composition.
```

### Cámara pegada al cuerpo (snorricam)
Para: desorientación, drama pegado al personaje.
```
body-mounted Snorricam. Movement: the camera stays rigidly fixed relative to the subject's torso or face while the subject moves through the scene. Speed: matched to the subject's body. Framing: the subject remains close, centered and facing the lens while the world swings around them. End: subject still locked in frame.
```

---

## 6. Dron y grúa (subida y vuelo)

### Grúa hacia arriba
Para: finales, revelar escala.
```
crane up. Movement: the camera rises smoothly through open space. Speed: slow, controlled vertical lift. Framing: the subject or location stays readable as elevation grows. End: hold the higher, larger-scale view.
```

### Grúa hacia abajo
Para: aperturas, bajar hasta la escena.
```
crane down. Movement: the camera descends smoothly through open space. Speed: slow, controlled vertical drop. Framing: the subject or location stays readable as the camera comes down. End: hold the lower subject or destination clearly.
```

### Dron hacia delante
Para: aproximaciones aéreas a un destino.
```
drone push in. Movement: the camera flies smoothly forward through open air toward the subject or destination. Speed: controlled aerial glide. Framing: route and destination stay readable during the approach. End: arrive at a closer aerial composition.
```

### Dron hacia atrás
Para: revelados épicos del paisaje alrededor del sujeto.
```
drone pull back. Movement: the camera flies smoothly backward away from the subject or destination. Speed: controlled aerial retreat. Framing: the subject stays readable as more landscape opens up. End: rest on a wide aerial composition.
```

### Plano de helicóptero
Para: planos de situación a gran escala.
```
helicopter-style aerial. Movement: the camera travels a broad, gradual flight path at high altitude. Speed: steady aerial cruise. Framing: the landscape or distant moving subject stays readable at wide scale. End: hold a stable high-altitude composition.
```

---

## 7. Especiales (estilizados o con efecto)

### Primera persona (FPV)
Para: inmersión, sensación de videojuego, historia en primera persona.
```
first-person view. Movement: the camera advances at eye height from the character's own perspective. Speed: natural walking or reaching pace. Framing: visible hands, arms or body edges anchor the viewer physically in the scene. End: arrive at the next point of action from the same POV.
```

### Tilt-shift (efecto maqueta)
Para: ciudades o escenas que parecen de juguete.
```
tilt-shift miniature view. Movement: hold or drift gently from a high, angled vantage over the scene. Speed: minimal, precise motion. Framing: a narrow band of sharp focus crosses the key subject area, with soft blur above and below it. End: the miniature-scale look stays intact.
```

### Zoom infinito
Para: transiciones hipnóticas entre mundos anidados.
```
infinite zoom. Movement: the zoom drives continuously inward toward the exact center target. Speed: smooth and accelerating. Framing: the circular center target stays locked as it expands. End: the next visual world fills the frame.
```

### Zoom a la Tierra
Para: saltos de escala dramáticos, de un punto al planeta.
```
earth zoom out. Movement: the camera pulls upward from the starting point through street, city, landscape and planetary scale. Speed: rapid, expanding zoom out. Framing: the original location stays centered as scale multiplies. End: planet-scale view with the origin point implied at center.
```

### Time-lapse
Para: el paso del tiempo desde un mismo punto.
```
locked-camera time-lapse. Movement: the camera holds one fixed position while time races forward. Speed: heavy time compression, rock-stable camera. Framing: composition and horizon never change as motion streams through the frame. End: same angle, with the passage of time clearly visible.
```

### Atravesar objetos
Para: transiciones imposibles a través de paredes, ventanas u objetos.
```
pass-through movement. Movement: the camera advances toward a visible object, surface or barrier and continues through into the space beyond. Speed: smooth, centered glide. Framing: the opening or surface stays centered as the transition point. End: arrive inside the revealed space.
```

---

## Tabla de compatibilidad por objetivo

| Objetivo | Mejores opciones |
|---|---|
| Tensión | zoom lento hacia dentro, acercamiento, plano fijo |
| Energía | barrido, zoom de golpe, persecución, cámara en mano |
| Producto o protagonista | órbita, arco, slider, zoom de golpe hacia dentro |
| Revelar escala | grúa hacia arriba, dron hacia atrás, zoom a la Tierra |
| Acompañar al sujeto | travellings, seguimiento, travelling de frente |
| Transición entre escenas | barrido, atravesar objetos, zoom infinito |
| Realismo | cámara en mano, primera persona, plano fijo |

## Combinar dos movimientos

Solo si son mecánicamente compatibles, y se funden en un solo bloque manteniendo las cuatro
partes. La fuente da un ejemplo de cada lado: acercamiento más subida sí (efecto grúa),
barrido más órbita no. Bloque compuesto para el caso compatible:

```
rising push-in. Movement: the camera travels forward toward the subject while rising straight up. Speed: slow, smooth and continuous. Framing: the subject stays centered and readable as distance closes and height grows. End: rest on a tighter, slightly higher composition.
```

Para cualquier otra pareja no hay lista probada. Criterio propio, sin medir: si una cámara real
no podría hacer los dos movimientos a la vez, no se piden juntos. Ante la duda, un solo
movimiento.
