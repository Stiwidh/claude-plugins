# ElevenLabs: referencia verificada

Consultado el **2026-09-30** en la documentación oficial, descargada en bruto (`.md`):

- Modelos: `elevenlabs.io/docs/overview/models`
- Eleven v4: `elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4`
- Buenas prácticas y prompting de v4 y v3: `elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices`
- Ajustes de voz (API): `elevenlabs.io/docs/api-reference/voices/settings/update`
- Voice Changer: `elevenlabs.io/docs/overview/capabilities/voice-changer` y `elevenlabs.io/docs/api-reference/speech-to-speech/convert`
- Etiquetas de audio: `elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/how-do-audio-tags-work-with-eleven-v3-and-v4`

ElevenLabs cambia modelos con frecuencia (v4 no existía cuando se escribió la skill de
origen). Si pasa tiempo, se vuelve a mirar antes de fijar un modelo.

---

## 1. Modelos de voz

| Modelo | Id | Para qué |
|---|---|---|
| Eleven v4 | `eleven_v4` | El más expresivo; el que ElevenLabs recomienda para contenido, narración y personajes. 90+ idiomas |
| Eleven v4 Turbo | `eleven_v4_turbo` | Tiempo real (~100 ms); admite etiquetas de audio |
| Eleven v3 | `eleven_v3` | Generación anterior; ElevenLabs recomienda pasar a v4. Los clones profesionales (PVC) no están del todo optimizados en v3 |
| Multilingual v2 | `eleven_multilingual_v2` | Estable, 29 idiomas; recomendado junto a v4 para calidad y narración de vídeo |
| Flash v2.5 | `eleven_flash_v2_5` | El más rápido (~75 ms), para agentes; no normaliza números por defecto |
| Voice Changer | `eleven_multilingual_sts_v2` | Cambio de voz sobre una grabación (el recomendado, también para inglés) |

`eleven_turbo_v2_5` y `eleven_turbo_v2` están obsoletos: se usan los Flash.

**Español:** v4 lista "Spanish (LatAm)"; Multilingual v2 y el Voice Changer, "Spanish (Spain,
Mexico)"; v3, "Spanish". Para castellano se prueba antes de producir. Según la página de v4,
cuando el idioma generado coincide con el de la voz de referencia, el acento se conserva;
cuando no coincide, v4 habla el idioma de destino con fluidez nativa en vez de arrastrar el
acento original (no es un fallo, es el comportamiento por diseño).

## 2. Ajustes de voz

| Ajuste | Por defecto | Qué hace (según la documentación) | Dónde existe |
|---|---|---|---|
| `stability` | 0.5 | Cuánto varía la voz entre generaciones. Bajo: más rango emocional. Alto: puede sonar monótona | Todos, v4 incluido |
| `similarity_boost` (Similarity) | 0.75 | Cuánto se pega a la voz original. Alto: más fiel, a veces menos natural | Todos, v4 incluido |
| `style` | 0 | Exagera el estilo del hablante original; consume más y puede añadir latencia si no es 0 | **No en v4** |
| `use_speaker_boost` | true | Refuerza el parecido con el hablante original; algo más de cálculo y latencia | La página de v4 no lo menciona (solo Stability y Similarity) |
| `speed` | 1.0 | Velocidad. Mínimo 0.7, máximo 1.2; los extremos pueden empeorar la calidad | **No en v4** |

En la web, `similarity_boost` se llama "Clarity + Similarity Enhancement".

**Criterio de la fuente, no verificado en la documentación** (se usa como punto de partida y
se escucha):

- `stability` 0.30 a 0.45 para escenas dramáticas; 0.50 a 0.65 conversacional; 0.70 o más
  para narración o corporativo.
- `style` alto (más de 0.6) degrada la estabilidad: compensar subiendo `stability` o
  generando más tomas.
- `speaker boost` apagado en narración de una sola voz. La documentación solo dice que
  viene encendido por defecto y que cuesta algo de latencia.

## 3. Dirigir dentro del texto

**Etiquetas de audio (v3 y v4; también v4 Turbo).** Una instrucción corta entre corchetes,
donde cambia la entrega:

- Emoción: `[curious]`, `[crying]`, `[mischievously]`, `[sarcastic]`, `[excited]`
- Dirección: `[whispers]`, `[shouts]`
- Reacciones: `[laughs]`, `[sighs]`, `[exhales]`, `[clears throat]`
- Experimentales: `[strong X accent]`, `[sings]`; menos consistentes entre voces

Matices de la documentación:

- Funcionan mejor si la voz ya tiene esa entrega en su entrenamiento; v4 sigue etiquetas
  aunque no la tenga, con menos garantía.
- En v4 una etiqueta puede leerse como **efecto de sonido** en vez de como entrega. Hay que
  escribirla describiendo la voz: `[low, gravelly voice]`.
- Se pueden **combinar** varias etiquetas. (La skill de origen decía "una por línea, al
  principio": la documentación no lo exige, y queda como precaución opcional.)
- Las etiquetas tienen que casar con el carácter de la voz: una voz seria no responde bien a
  `[giggles]`.

**Puntuación (v4):** los puntos suspensivos añaden pausa y peso; las mayúsculas, énfasis; la
puntuación normal da el ritmo.

**Pausas:**

- Multilingual v2 y Flash: `<break time="1.5s" />`, hasta 3 segundos. Demasiadas en una
  generación la vuelven inestable (acelera o mete ruidos).
- v3 y v4: **no admiten SSML**. Pausas con puntos suspensivos, etiquetas y estructura del
  texto.

**Emoción por contexto (modelos sin etiquetas):** acotaciones narrativas ("dijo, con la voz
temblando"). Dan resultados más previsibles, pero **el modelo también las lee en voz alta**:
se cortan en el montaje.

**Ritmo:** depende mucho de la muestra con la que se creó la voz. Muestras largas y seguidas
evitan voces que corren de más.

## 4. Pronunciación

- **v4:** entiende IPA entre barras: `"/transcripción_IPA/"`, con las marcas de acento (`ˈ`). Más consistente que antes, pero varía
  por voz: probar los nombres importantes antes de producir y generar más de una vez si hace
  falta.
- **Flash v2:** etiquetas de fonema SSML (CMU o IPA).
- **Multilingual v2:** sin fonemas; se escribe la palabra como suena, con mayúsculas o
  guiones, o se usa un diccionario de pronunciación con alias.
- **Diccionarios de pronunciación** (TXT o `.PLS`) en Studio, Dubbing y la API: para nombres
  de marca y siglas que se repiten.

## 5. Voice Changer

- Transforma una grabación en otra voz **conservando la interpretación**: susurros, risas,
  llanto, acentos, matices.
- Modelo: `eleven_multilingual_sts_v2` (29 idiomas). `eleven_english_sts_v2`, solo inglés.
- Máximo **5 minutos** por segmento; lo más largo se trocea.
- Cobro: 1.000 caracteres por minuto de audio procesado.
- `remove_background_noise`: quita el ruido de fondo de la entrada.
- `seed`: intenta repetir el mismo resultado con los mismos parámetros; no está garantizado.
- `voice_settings`: se pueden pasar para esa petición sin tocar los guardados de la voz.
- La voz destino puede ser cualquier voz clonada o diseñada de la biblioteca.

## 6. Problemas típicos

**De la documentación:**

| Síntoma | Qué hacer |
|---|---|
| Pausas irregulares | En v2/Flash, `<break>` bien escrito; en v3/v4, puntos suspensivos y estructura |
| Pronuncia mal | IPA en v4, fonemas en Flash v2, reescritura fonética o diccionario |
| La emoción no encaja | Más contexto narrativo o etiquetas explícitas; cortar las acotaciones después |
| Voz rápida de más | Revisar la muestra de la voz; en v2, `speed` por debajo de 1.0 |
| Mismo IPA, resultados distintos | Generar varias veces y quedarse con la mejor |

**Criterio de la fuente, no verificado:**

| Síntoma | Qué probar |
|---|---|
| Suena metálica o tiembla | `stability` +0.15, `style` -0.2 |
| Plana, monótona | `stability` a 0.4-0.5 y más variedad de puntuación |
| La voz se va a lo largo de muchas líneas | Generaciones más cortas, `similarity` +0.1, speaker boost encendido |
| Risas o ruidos que no se pidieron | Quitar etiquetas contiguas, `stability` +0.1 |
| Acento equivocado | Una frase de contexto en el idioma de destino |

## 7. Varias voces en una pieza

Criterio de la fuente, sensato: fijar los ajustes de cada personaje **antes** de producir
ninguna escena, generar las réplicas de cada personaje por tandas (no intercaladas) y
guardar los ajustes de cada uno como su ficha de voz para toda la serie. Para diálogo con
varias voces en una sola generación, ElevenLabs tiene la API de diálogo (Text to Dialogue)
con v3 y v4.
