# El guion se respeta: diálogo literal en FLUX 3

> Este es el documento que resuelve el fallo "le doy un guion y se inventa otro".
> Todo lo de aquí sale de la documentación oficial de Black Forest Labs
> (`docs.bfl.ai`, guía "Audio and speech", cookbook "Multi-shot films" y las skills
> oficiales `flux-3-audio-dialogue` y `flux-3-prompt-doctor`), consultada el 2026-09-09.

---

## 1. Por qué se inventa los diálogos

No hay un fallo, hay **cinco**, y actúan en cadena. Cada uno se cierra con una llave distinta.

| # | Qué pasa de verdad | Por qué | La llave |
|---|---|---|---|
| 1 | El agente reescribe la línea antes de generarla | Nadie declaró que el guion fuera literal | **Ley del texto intocable** (apartado 2) |
| 2 | El modelo parafrasea la idea | La línea iba sin comillas, así que es una descripción, no una réplica | **Comillas** (apartado 3) |
| 3 | La línea sale escrita en pantalla, no hablada | Hay una línea entrecomillada pero ninguna boca a la que asignarla | **Hablante o voz en off** (apartado 4) |
| 4 | Repite, alarga, mete relleno o añade frases que no están | Falta la orden de decirla una vez y solo esa | **Candado de una sola vez** (apartado 5) |
| 5 | La dice en inglés, o mezcla idiomas | Sin candado de idioma, el modelo tiende a traducir la línea al inglés y hablar esa | **Candado de idioma** (apartado 6) |

Cita literal del cookbook oficial de BFL sobre los dos últimos:

> **The exactly-once direction.** "Speaks on camera exactly once, the complete sentence,
> no repetition and no other words in the entire shot." Without it, lines repeat or pick
> up filler.
>
> **The language lock.** "Every word in French, no English words at all." Without it,
> the model tends to translate the line back to English and speak that.

Y sobre el tercero, de la guía de audio:

> A quoted line without a visible speaker or a voiceover cue may be treated as text that
> belongs in the frame.

---

## 2. Ley del texto intocable (esta es para ti, agente)

**El diálogo que llega en un guion es dato, no material de partida.**

Cuando recibas un guion con líneas de diálogo, esas líneas se copian **carácter a carácter**
al prompt. Está prohibido:

- reescribirlas, aunque suenen mejor de otra forma
- traducirlas a otro idioma
- acortarlas para que quepan
- corregir su puntuación, su registro o sus muletillas
- fundir dos líneas en una
- añadir una línea que no estaba, ni siquiera un saludo o un cierre

Si la línea no cabe en la duración del plano, **no se recorta: se avisa**. La reparación
correcta es subir la duración o partir la escena en dos planos, y esa decisión la toma
quien escribió el guion, no tú.

Si crees que una línea está mal escrita para ser dicha en alto, lo dices aparte, como nota,
y esperas. Nunca la cambias por tu cuenta dentro del prompt.

**Único cambio permitido sin preguntar:** escribir fonéticamente un nombre propio raro
para que la pronunciación salga bien, dejando constancia de que lo has hecho.

---

## 3. Comillas: la línea va entre comillas o no es una línea

El modelo renderiza como habla lo que encuentra entre comillas. Lo que va fuera lo trata
como descripción, y una descripción se puede parafrasear.

```
MAL:   Ella le dice que el tren de las seis y diez vuelve a ir con retraso.
BIEN:  She says: "El de las seis y diez vuelve a llegar tarde. Dicen que diez minutos."
```

Las comillas van alrededor de la línea **exacta**, sin corchetes, sin acotaciones dentro,
sin puntos suspensivos que el modelo pueda leer como pausa infinita.

**Puntuación simple.** Demasiadas comas y pausas convierten la lectura en cantinela.
La guía oficial lo llama `sing-song`, y la reparación es simplificar la puntuación.

---

## 4. Hablante visible o voz en off: hay que elegir, siempre

Una línea entre comillas sin dueño es una línea huérfana, y el modelo resuelve la orfandad
poniéndola de rótulo en pantalla. Hay dos salidas y ninguna es opcional.

### 4.1 Hablante en cámara (con sincronía labial)

Describe a la persona antes de la línea: **edad aproximada, un rasgo físico, la ropa** y
qué está haciendo. Eso le da al modelo una cara a la que mover la boca.

```
Primer plano medio de una mujer de unos treinta y cinco años, melena castaña recogida,
jersey de punto crudo, sentada al borde de la mesa de la cocina. Mira a cámara y dice,
tranquila y directa: "..."
```

### 4.2 Voz en off (sin cara)

Hay que etiquetarla con la palabra: `voiceover` o `narration`. Sin la etiqueta, el modelo
sigue buscando una boca.

```
An off-screen voiceover says exactly once: "..."
```

### 4.3 El cierre obligatorio

Termina **siempre** el prompt con:

```
No on-screen text, no subtitles.
```

Sin esa frase, el modelo tiene permiso para dibujar la línea en pantalla además de decirla,
o en lugar de decirla.

---

## 5. Candado de una sola vez

Esta es la frase que más diálogo inventado corta de raíz. Va pegada a la línea:

```
...says on camera exactly once, the complete sentence, with no repetition and no other
words in the entire shot: "<la línea literal>"
```

Desmenuzada, cada trozo bloquea un fallo distinto:

| Trozo | Qué impide |
|---|---|
| `exactly once` | que repita la frase o parte de ella |
| `the complete sentence` | que se coma el final |
| `no repetition` | los ecos y los tartamudeos |
| `no other words in the entire shot` | **el diálogo inventado**, el saludo de más, el relleno |

Y refuérzalo en la capa de audio con `no other speech`, que cierra la puerta a voces de
fondo que el modelo se invente.

---

## 6. Candado de idioma

Sin él, el modelo traduce la línea al inglés y dice la traducción. Para español:

```
She speaks entirely in Spanish, every word in Spanish, native Castilian accent and
cadence, no English words at all.
```

Cámbialo por el idioma que toque. La estructura es siempre la misma: **nombra el idioma,
repite que cada palabra va en ese idioma, y niega el inglés explícitamente.**

FLUX 3 habla, entre otros: inglés, español, chino, francés, alemán, japonés, portugués,
ruso, italiano, indonesio, turco, hindi y punjabi. Puedes escribir la línea en su alfabeto
nativo, y es lo más fiable cuando las palabras exactas importan.

---

## 7. La plantilla completa, montada

Este es el molde que debes usar cuando haya diálogo. Copia la estructura, cambia el contenido.

```
[Duración y tipo de plano]. [Descripción del hablante: edad, rasgo, ropa, dónde está y
qué hace]. [Luz y ambiente].

[Verbo de habla + cómo lo dice] on camera exactly once, the complete sentence, with no
repetition and no other words in the entire shot: "<LÍNEA LITERAL DEL GUION>"

[Candado de idioma].

Audio: [su voz, con qué carácter y qué micro], [una o dos capas de ambiente con fuente
concreta]. No music, no other speech. No on-screen text, no subtitles.
```

### Ejemplo real, español, ocho segundos

```
An 8-second interior medium close-up in a small home studio. A woman in her thirties with
a dark bob and round glasses sits at a wooden desk in warm morning light, hands resting on
a notebook, looking straight to camera.

She says on camera exactly once, warm and unhurried, the complete sentence, with no
repetition and no other words in the entire shot: "Llevo tres años haciendo esto y sigo
sin usar plantillas."

She speaks entirely in Spanish, every word in Spanish, native Castilian accent and cadence,
no English words at all.

Audio: her voice clean and close, the faint hum of a laptop fan, distant traffic through a
closed window. No music, no other speech. No on-screen text, no subtitles.
```

---

## 8. Conversaciones de varios personajes

Aquí es donde más se rompe, y la documentación oficial lo admite sin adornos:

> Multi-speaker attribution and interruptions are still review-heavy.
>
> Do not force several speakers, a long script, and multiple visual beats into a short clip.
> Split the scene when each part needs its own timing.

La skill oficial `flux-3-prompt-doctor` va más lejos y marca como **REVISE** cualquier
encargo que pida "multiple full dialogue lines" en un plano corto. O sea: un guion de
conversación metido entero en un clip **no es un encargo válido**, y devolverlo tal cual
garantiza el resultado inventado.

### Regla de reparto

| Cuántas réplicas | Qué hacer |
|---|---|
| 1 | Un plano. Molde del apartado 7. |
| 2, cortas, mismo espacio | Un plano de 10 s o más, con las dos réplicas atribuidas por un rasgo visible y separadas por una pausa. |
| 3 o más | **Un plano por réplica**, generados por separado y montados después. |

### Cómo se atribuye cuando hay dos

Nunca por el nombre del personaje, que el modelo no conoce. **Por un rasgo visible**, y
el mismo rasgo en el prompt y en la escena:

```
The woman in the mustard jacket speaks first, practical: "<línea 1>"
After she finishes, the man in the grey apron replies, quieter: "<línea 2>"
Keep the speakers distinct, the turns short and separate, with no overlap and no other
speech.
```

`with no overlap` importa: si se pisan, las palabras salen ininteligibles.

### Cuando son varios planos

Cada réplica es una generación independiente. Para que parezca la misma conversación:

- **Copia la descripción del personaje palabra por palabra** en todos sus planos. La
  consistencia entre generaciones sale de que el texto sea idéntico, no parecido.
- Copia también el mismo párrafo de espacio, luz y paleta (la "biblia" del apartado 9 de
  `multiplano-continuidad.md`).
- Advertencia honesta de BFL: repetir la dirección de voz conserva **un tipo de voz**, no
  garantiza el mismo actor en cada generación. Escucha los planos seguidos antes de montar.

---

## 9. El límite honesto: lo que la generación no te va a dar

La documentación oficial de BFL reserva estas cosas para post-producción, no para el
generador:

> Reserve for deterministic post: final loudness, EQ, ducking, and fades; **guaranteed
> wording or speaker identity**; frame-accurate sync; subtitles and captions; continuity
> across separately generated clips.

Traducido a lo que importa aquí: **la redacción exacta es un objetivo dirigible, no un
control garantizado.** Las llaves de este documento suben mucho la tasa de acierto, pero
no la ponen en el 100%.

Por eso, cuando el texto exacto es una condición de aceptación del cliente (una promesa
legal, una cifra, el nombre de una marca, un claim regulado), la ruta correcta no es
insistir con el prompt:

1. Genera el plano **sin voz** (`generate_audio: false`).
2. Graba o sintetiza la voz aparte, donde el texto es exacto por construcción.
3. Monta las dos pistas.

Es más trabajo y es la única forma de que la frase sea la frase.

**Y una consecuencia práctica:** cada take con diálogo se **escucha entero** antes de darlo
por bueno. No vale mirar el vídeo. Si una palabra cambió, el take está mal.

---

## 10. Tabla de reparación

Cambia **una sola cosa** por intento. Si dos intentos seguidos fallan igual, el problema
es la estructura del plano, no el adjetivo.

| Lo que ves | Lo que se cambia |
|---|---|
| La línea aparece escrita en pantalla | Falta hablante visible o la etiqueta `voiceover`. Añade uno y cierra con `no on-screen text, no subtitles` |
| Dice otra cosa parecida | La línea no iba entre comillas |
| Dice la línea y luego se inventa más | Falta `no other words in the entire shot` y `no other speech` |
| Repite la frase | Falta `exactly once` |
| La dice en inglés | Falta el candado de idioma |
| Se come la última palabra | Línea demasiado larga: sube la duración o parte la escena. Nunca aceleres la lectura |
| Se entiende mal, palabras pastosas | Hay voces compitiendo (radio, gente hablando, otro narrador). Quítalas del ambiente |
| Suena a anuncio, locutor de radio | Sustituye los adjetivos de elogio por persona, micro y situación. Añade `no announcer delivery, no sales voice` |
| Cantinela, ritmo raro | Simplifica la puntuación de la línea |
| Atribuye la réplica al personaje equivocado | Atribuye por rasgo visible, no por nombre. Si hay tres o más réplicas, sepáralas en planos |

---

## 11. Checklist antes de mandar a generar

Ninguna casilla es opcional cuando hay diálogo:

- [ ] La línea del prompt es **idéntica** a la del guion, carácter a carácter
- [ ] Va entre comillas
- [ ] Hay hablante descrito (edad + rasgo + ropa) **o** la etiqueta `voiceover`
- [ ] Lleva `exactly once, the complete sentence, with no repetition and no other words in the entire shot`
- [ ] Lleva candado de idioma
- [ ] La capa de audio dice `no other speech`
- [ ] El prompt termina en `No on-screen text, no subtitles`
- [ ] La duración da margen para decir la línea entera y sobra un poco
- [ ] Hay **una sola** réplica por plano, o dos cortas atribuidas por rasgo visible
- [ ] Si el texto exacto es condición de aceptación, esto va por la ruta de voz aparte (apartado 9)
