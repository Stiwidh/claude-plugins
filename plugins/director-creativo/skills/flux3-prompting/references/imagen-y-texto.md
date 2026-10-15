# Imagen y texto en pantalla con FLUX

Fuente: guías `prompting_unified_*` y `usecases_t2i_*` de `docs.bfl.ai`, consultadas el
2026-09-09.

**Aviso de estado:** FLUX 3 hace imagen además de vídeo, pero la generación de imagen de
FLUX 3 está en acceso anticipado. El modelo de imagen que está en producción y al que
apuntan las guías es **FLUX.2**. Lo de aquí abajo aplica a FLUX.2 y sigue siendo el patrón
correcto para FLUX 3 imagen cuando abra del todo.

---

## 1. Longitud del prompt

FLUX.2 admite hasta 32.000 tokens, pero la longitud no es el objetivo.

| Longitud | Palabras | Para qué |
|---|---|---|
| Corta | 10-30 | Conceptos rápidos, explorar estilo |
| Media | 30-80 | La mayoría de escenas, el día a día |
| Larga | 80-300+ | Escenas complejas con varios sujetos, resultados muy dirigidos |

Empieza corto y añade solo lo que cambia la imagen. **El detalle específico ayuda; el
relleno estorba.**

---

## 2. Los nueve componentes

| Componente | Qué controla | Ejemplo |
|---|---|---|
| Tipo de imagen | Categoría y encuadre general | `portrait`, `landscape`, `macro` |
| Sujeto | Lo principal que se ve | `a young woman with curly red hair` |
| Localización | El entorno | `in a futuristic space station` |
| Estilo | La dirección visual | `editorial photography`, `anime illustration` |
| Cámara | Óptica, encuadre, profundidad | `85mm lens, shallow depth of field` |
| Luz | Cómo está iluminada | `soft window light`, `golden hour sunlight` |
| Color | La paleta dominante | `muted earth tones`, `deep green and cream` |
| Efecto | Tratamiento visual extra | `motion blur`, `film grain`, `soft bloom` |
| Elementos añadidos | Detalles que enriquecen | `wind-blown fabric, falling leaves` |

No hacen falta los nueve. Usa los que mejoren la imagen que quieres.

Patrón fiable: **sujeto claro, luego la acción o el estado, y luego ambiente y dirección
visual solo cuando aportan.**

La diferencia se ve rápido:

```
Flojo:  A dog sitting in a sunny park

Bueno:  A golden retriever mid-leap chasing a tennis ball across a sunlit hardwood floor
        in a cozy living room, muddy paw prints trailing behind, warm afternoon light
        streaming through sheer curtains, shallow depth of field, candid pet photography,
        35mm lens
```

---

## 3. No hay prompt negativo

**La mayoría de modelos FLUX no admiten prompt negativo**, y aunque lo procesen, la negación
funciona mal: escribir "sin gafas" hace que el modelo se centre en las gafas.

La estrategia es de sustitución: identificas lo que sobra, te preguntas qué habría en su
lugar, y describes eso en positivo.

| En vez de | Escribe |
|---|---|
| "no people" | `empty`, `deserted`, `solitary` |
| "no colors" | `monochrome`, `black and white`, `grayscale` |
| "no text" | `clean surfaces`, `unmarked`, `blank` |
| "not dark" | `brightly lit`, `sun-drenched` |
| "not many" | `few`, `single`, `minimal` |
| "a street with no cars" | `a quiet pedestrian walkway with cobblestones` |
| "portrait with no background distractions" | `portrait with smooth gradient background transitioning from deep blue to black` |

**La excepción práctica es el vídeo con voz.** Ahí las fórmulas `no on-screen text`,
`no subtitles`, `no other speech` y `no music` sí funcionan y son las que recomienda la
documentación oficial de FLUX 3, porque están cerrando capas de audio y de rótulo, no
eliminando objetos de una escena.

---

## 4. Texto legible dentro de la imagen

FLUX.2 renderiza texto legible si se lo describes con precisión. Reglas:

- **Entre comillas:** `The text 'OPEN' appears in red neon letters above the door`
- **Di dónde va:** su posición respecto a los demás elementos
- **Di el estilo:** `elegant serif typography`, `bold industrial lettering`, `handwritten script`
- **Di el tamaño:** `large headline text`, `small body copy`
- **Color de marca por código hex:** `The logo text 'ACME' in color #FF5733`

Ejemplo de cartel completo:

```
Groovy retro poster with the quote "If you love me let me sleep". Bold 70s typography in
deep red and warm pink tones. Cream background and bold orange doodle around the text.
Funky layout with playful shadow. Style: bold vintage aesthetic, dopamine decor
```

> **Contraste importante con el vídeo:** en imagen el texto sale bien. En vídeo, la
> tipografía crítica de producción **no se genera**: se pone en montaje. Para una miniatura
> con texto, se genera la imagen y ahí sí se pide el texto.

---

## 5. Prompt en JSON

FLUX.2 entiende igual de bien la prosa y un JSON estructurado. El JSON compensa cuando hay
flujo de producción, automatización, varios sujetos con relaciones entre ellos, o cuando
quieres iterar un elemento sin tocar los demás.

```json
{
  "scene": "descripción general de la escena",
  "subjects": [
    { "description": "...", "position": "dónde en el cuadro", "action": "qué hace" }
  ],
  "style": "estilo artístico",
  "color_palette": ["#hex1", "#hex2", "#hex3"],
  "lighting": "descripción de la luz",
  "mood": "tono emocional",
  "background": "detalles del fondo",
  "composition": "encuadre y disposición",
  "camera": { "angle": "...", "lens": "...", "depth_of_field": "..." }
}
```

El bloque `camera` admite parámetros de fotografía reales: `lens-mm`, `f-number`, `ISO`,
`distance`, `focus`.

Para prosa suelta, exploración rápida y escenas de un solo sujeto, el lenguaje natural va
mejor.

---

## 6. Relación de aspecto

Elige la que encaje con la intención de la composición. Una relación que no cuadra obliga al
modelo a recortar o a rellenar.

| Relación | Formato | Para qué |
|---|---|---|
| 1:1 | Cuadrado | Redes, perfiles, producto |
| 16:9 | Apaisado | Cabeceras web, presentaciones |
| 9:16 | Vertical | Móvil, stories, editorial vertical |
| 4:3 | Estándar | Fotografía clásica |
| 3:2 | Foto | Estilo réflex |
| 21:9 | Ultra ancho | Cine, panorámica |

Un prompt apaisado se beneficia de 16:9; uno de retrato, de 9:16.
