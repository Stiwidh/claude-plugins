# Vocabulario de cámara, luz y estilo para FLUX 3

Los 119 términos del cheatsheet oficial de Black Forest Labs
(`docs.bfl.ai/guides/prompting_video_camera_terms`), consultado el 2026-09-09, más las
reglas de uso de la guía "Text-to-Video".

**Se escriben en inglés dentro del prompt**, aunque el diálogo vaya en español. Son los
términos con los que el modelo fue entrenado.

---

## 1. Dos reglas antes del vocabulario

**Si no nombras la cámara, se mueve sola.** El comportamiento por defecto es una deriva
suave. Para que un plano esté quieto de verdad hay que pedirlo: `camera locked at eye
level`, `the camera holds locked`.

**La cámara es un contrato físico y no admite contradicción.** Una cámara fija no puede
seguir a nadie. Un primerísimo plano no puede establecer una localización. Elige una.

---

## 2. Tamaño de plano

| Término | Qué da |
|---|---|
| `Macro` | Detalle extremo de una superficie muy pequeña |
| `Extreme close-up` | Un solo detalle diminuto llenando el cuadro |
| `Close-up` | Cara, textura o un objeto único |
| `Medium shot` | Sujeto y entorno equilibrados |
| `Cowboy shot` | Desde medio muslo hacia arriba |
| `Full shot` | Cuerpo entero, de la cabeza a los pies |
| `Wide shot` | Cuerpo entero y bastante entorno |
| `Establishing shot` | Sitúa lugar y escala antes de la acción |
| `Two shot` | Dos sujetos compartiendo cuadro |
| `Aerial` | Vista desde muy arriba |

## 3. Ángulo y punto de vista

| Término | Qué da |
|---|---|
| `Eye level` | Altura neutra, a los ojos del sujeto |
| `Low angle` | Mira hacia arriba: escala, dominio |
| `High angle` | Mira hacia abajo: comprime, expone |
| `Worm's eye` | Ángulo bajo extremo, mirando recto arriba |
| `Bird's eye (top-down)` | Cenital recto |
| `Ground level` | A ras de suelo, mirando a través de la escena |
| `Dutch angle` | Horizonte inclinado: inquietud, tensión |
| `POV` | Desde la perspectiva del sujeto |
| `Over-the-shoulder` | Acción encuadrada por encima de un hombro |
| `Profile shot` | Perfil estricto |
| `Object POV` | Desde la perspectiva de un objeto |
| `Voyeur` | Vista escondida y obstruida, espiando |
| `Fourth wall` | El sujeto mira y habla directo a cámara |
| `Tableau` | Cuadro amplio, estático, simétrico y compuesto |

> `Fourth wall` es el término para **presentador que habla a cámara**, el caso más común
> en contenido de marca.

## 4. Composición

| Término | Qué da |
|---|---|
| `Leading lines` | Líneas de la escena que guían la mirada |
| `Center framing` | Sujeto clavado en el centro |
| `Rule of thirds` | Sujeto descentrado, equilibrado |
| `Symmetry` | Formas espejadas: precisión o tensión |
| `Negative space` | Aire alrededor del sujeto |
| `Frame within frame` | Un hueco de la escena enmarca al sujeto |
| `Foreground occlusion` | Objetos desenfocados delante que dan profundidad |
| `Silhouette` | Sujeto oscuro contra luz fuerte |
| `Reflection framing` | Compuesto sobre una superficie reflectante |

## 5. Movimiento de cámara

| Término | Qué da |
|---|---|
| `Pan` | Rota a izquierda o derecha desde un punto fijo |
| `Tilt` | Rota arriba o abajo |
| `Dolly in` | Se acerca físicamente al sujeto |
| `Tracking shot` | Se desplaza junto al sujeto |
| `Trucking` | Desliza lateralmente junto a la escena |
| `Orbit` | Rodea al sujeto |
| `Arc shot` | Barre medio círculo alrededor del sujeto |
| `Crane / boom` | Sube o baja sobre una pluma |
| `Pedestal` | Sube o baja recto en el espacio |
| `Handheld` | Movimiento suelto, orgánico |
| `Steadicam follow` | Seguimiento estabilizado y suave |
| `Whip pan` | Barrido rápido que emborrona entre sujetos |
| `Dolly zoom` | Zoom y travelling opuestos: efecto vértigo |
| `Push through` | Atraviesa un hueco hacia otro espacio |
| `Snorricam` | Cámara montada al sujeto, el mundo se balancea |
| `Camera roll` | Gira sobre el eje del objetivo |
| `Locked-on` | El sujeto queda fijo y el fondo se emborrona |
| `Lazy Susan` | El sujeto gira sobre plato, la cámara quieta |

Empareja el movimiento con la duración para controlar el ritmo:
`camera pushes slowly forward from wide to close over 6 seconds`.

## 6. Foco y óptica

| Término | Qué da |
|---|---|
| `Shallow depth of field` | Sujeto nítido, fondo blando |
| `Deep focus` | Todo nítido, delante y detrás |
| `Rack focus` | El foco salta de un plano a otro |
| `Split diopter` | Cerca y lejos nítidos a la vez |
| `Focus breathing reveal` | El desenfoque se resuelve y revela al sujeto |
| `Tilt shift` | Foco selectivo, efecto maqueta |
| `Wide angle (24mm)` | Espacio exagerado, distorsión en los bordes |
| `Telephoto compression` | Aplana la profundidad y apila los planos |
| `Macro lens` | Magnificación extrema del detalle |
| `Probe lens` | Objetivo sonda que se cuela por sitios estrechos |
| `Fisheye` | Gran angular curvo extremo |
| `Anamorphic flares` | Destellos horizontales y bokeh ovalado |
| `Halation` | Halos luminosos alrededor de las altas luces |
| `Parallax` | Capas de profundidad deslizando a distinta velocidad |
| `Vignette` | Bordes oscurecidos, centro luminoso |

Combinaciones que funcionan como carácter de imagen:

- `35mm lens, shallow depth of field` : documental editorial
- `70mm long lens, subject in sharp focus, background compressed` : retrato
- `24mm wide lens close to the subject, slight edge distortion` : cámara en mano subjetiva
- `anamorphic 2.35:1, cinematic bokeh, lens flare on the highlights` : largometraje

## 7. Tiempo y velocidad

| Término | Qué da |
|---|---|
| `Slow motion` | Acción estirada por debajo del tiempo real |
| `Fast motion` | Acción acelerada |
| `Speed ramp` | La velocidad cambia dentro del mismo plano |
| `Timelapse` | Horas comprimidas en segundos |
| `Long exposure look` | El movimiento se convierte en estelas de luz |
| `Bullet time` | Instante congelado mientras la cámara lo rodea |
| `Freeze frame` | El sujeto se congela y la cámara sigue |
| `Boomerang` | Acción corta hacia delante y hacia atrás en bucle |
| `Step printing` | Movimiento a saltos, con estelas |
| `Cinemagraph` | Foto fija con un único movimiento en bucle |

## 8. Luz

| Término | Qué da |
|---|---|
| `Rim light` | Contraluz que perfila el borde del sujeto |
| `Chiaroscuro` | Contraste fuerte de luz y sombra profunda |
| `Golden hour` | Contraluz cálido de sol bajo |
| `Hard light` | Sombras duras de borde nítido |
| `Volumetric light` | Haces visibles y rayos de dios en la bruma |
| `Haze` | Atmósfera densa que revela los haces |
| `Neon practicals` | Fuentes de luz de color dentro de la escena |
| `Spotlight` | Un haz aísla al sujeto en la oscuridad |
| `Light flash` | Ráfagas de flash que congelan el movimiento |
| `Projections` | Imágenes proyectadas sobre el sujeto |
| `Underwater light` | Cáusticas ondulando sobre las superficies |

## 9. Transiciones y montaje dentro de un plano

| Término | Qué da |
|---|---|
| `Match cut` | Una forma o un movimiento cruza el corte |
| `Whip transition` | Un barrido esconde el corte |
| `Foreground wipe` | Un objeto que pasa barre a la escena siguiente |
| `Jump cut` | Cortes bruscos y discontinuos en el mismo encuadre |
| `Object portal` | La cámara se mete en un objeto y sale en otra escena |
| `Pass-through` | Un movimiento continuo que enhebra varios espacios |
| `Quick cuts` | Montaje rítmico de planos cortos |
| `Screen-in-screen` | Pantalla dentro de pantalla, recursiva |

## 10. Formatos y cámaras concretas

| Término | Qué da |
|---|---|
| `Drone FPV` | Vuelo de dron rápido y ágil en primera persona |
| `Bodycam` | POV de pecho, moviéndose con el cuerpo |
| `Dashcam` | Vista fija desde el coche |
| `Mirror POV` | El sujeto visto en un espejo |
| `Cinemascope (21:9)` | Cuadro anamórfico ultra ancho |
| `Vertical (9:16)` | Cuadro alto, para móvil |
| `Vintage (4:3)` | Encuadre retro de videocámara |
| `Split screen` | Dos planos lado a lado |

## 11. Efectos y mundos

| Término | Qué da |
|---|---|
| `Double exposure` | Dos imágenes fundidas en un cuadro |
| `Datamosh` | Corrupción de píxel, glitch que se arrastra |
| `Kaleidoscope` | Patrones simétricos repetidos |
| `Morphing` | Un sujeto se transforma con fluidez en otro |
| `Slit scan` | Movimiento convertido en cintas de tiempo |
| `X-ray` | Vista interior, transparente |
| `Levitation` | Objetos o personas flotando |
| `Dreamcore` | Espacios liminales, nostálgicos, inquietantes |
| `Dystopian` | Mundo futurista opresivo |
| `Magical realism` | Magia discreta dentro de una escena corriente |
| `Maximalism` | Escenografía densa, recargada |
| `Diorama` | Mundo maqueta con tilt-shift |
| `Stop motion` | Animación artesanal fotograma a fotograma |
| `Pixel art` | Estética retro de 16 bits |
| `Zoetrope` | Animación de tambor giratorio pre-cine |
| `Kinetic typography` | Texto animado como elemento visual principal |

---

## 12. El estilo tiene que ser visible

Un adjetivo de estado de ánimo no es una instrucción. Se traduce a lo que la cámara puede
ver:

- "tenso" se convierte en **postura rígida, respiración corta y un avance lento de cámara**
- "vintage" se convierte en **un formato de captura con nombre, una estructura de grano y
  luz práctica**

Y para salir de lo fotorrealista, se cita un ancla de estilo con nombre propio:
`Ghibli-adjacent watercolour style with visible pencil linework`,
`Aardman-adjacent stop-motion claymation`. El modelo construye hacia esa gramática en vez
de caer en un cine genérico.

Nada de chispas, campanas ni efectos sin motivo. Si algo suena o brilla, algo lo ha causado
dentro del cuadro.

---

## 13. Conceptos que aguantan y conceptos que no

Del `field-guide` oficial. Antes de gastar créditos, mira en qué lado cae tu idea.

### Aguantan bien

- **Luz atmosférica en un medio:** un faro barriendo niebla marina, un relámpago a través
  de un invernadero, una bengala inundando la niebla.
- **Superficies mojadas y reflejos** que participan: un reflejo que se rompe en cintas y se
  recompone.
- **Macro de materiales viscosos:** miel enroscándose, crema de café plegándose, caramelo
  enfriando.
- **Contacto táctil e ignición simple:** una llama recorriendo un quemador, una cerilla.
- **Noir y ambientes contenidos:** casi monocromo, lluvia, niebla, luces prácticas.

### Hay que sacarlos de la generación

- interpretación humana en primer plano
- fuerza o tensión transmitida a distancia
- tipografía como copy legible protagonista, y rótulos que aparecen tarde en el plano
- mecánicas secuenciales tipo máquina de escribir
- sincronía audiovisual exacta o foley completo
- productos donde la identidad exacta es crítica y no hay imagen de referencia
- narrativas largas de varios pasos con tiempos exactos

### Test de seis preguntas

Antes de generar, todo tiene que ser un sí:

1. ¿Se describe como un solo plano suelto?
2. ¿Hay una causa visible, una respuesta y un desenlace?
3. ¿Causa y efecto se leen dentro del mismo cuadro?
4. ¿La luz, el material, el tiempo o un reflejo hacen que el plano sea cine?
5. ¿El plano sigue siendo interesante aunque el texto y la sincronía no salgan exactos?
6. ¿Sabría un montador dónde meterlo?
