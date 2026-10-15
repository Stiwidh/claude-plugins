# Recetas: cómo meter el ADN en un prompt

## El orden

`[sujeto] + [trato del sujeto] + [entorno] + [ADN de luz] + [cámara] + [acabado y textura] + [lógica de color + paleta NUEVA] + [registro emocional] + [ajustes]`

Delante lo que más importa: los modelos pesan más los primeros términos.

## Plantilla general (Nano Banana, GPT Image, Soul, FLUX, Seedream...)

Un párrafo en lenguaje natural, en inglés, en ese orden:

```
A [rendering mode] image of [subject], [treatment stance]. Set in [environment].
Lit by [direction] [quality] light with [temperature behavior]. Shot as if on a [focal]mm lens,
[depth of field], from [angle]. [Texture and finish sentence]. The palette is strictly [swatches
with HEX and ratios], following [color logic]. Overall mood: [register].
```

**Lo que no se quiere, en positivo.** La skill de origen añade una línea "Avoid: ...". En
Higgsfield el método oficial pide los negativos en positivo ("tack sharp", no "no blur"),
así que la lista de lo que se tira sirve para saber qué reforzar, y se escribe como lo que sí:
en vez de "avoid teal", "shadows stay warm brown". Solo se usa un campo de negativos donde la
herramienta lo tenga.

**La paleta, en palabras y en HEX.** Se nombran los tonos y se dan 2 o 3 HEX.

## Referencias de estilo que llegan de Midjourney

Midjourney no está entre las herramientas de este plugin. Si llega un código de estilo (`--sref`) o una imagen hecha
con él, se analiza la imagen y se reconstruye con la plantilla general; el código no se copia
al prompt, porque la gracia es no depender de él.

## Lo frágil: avisos de deriva

Cuando la columna SE QUEDA lleva alguno de estos, se avisa, porque se degradan al generar:

| Elemento frágil | Qué pasa | Cómo reforzarlo |
|---|---|---|
| Poca profundidad de campo en formatos anchos | se pierde la intimidad | "85mm, close quarters, background dissolved" |
| Paletas restringidas | el modelo se va a todo color | repetir la paleta dos veces y decir en positivo qué tonos mandan |
| Bordes rotos o pictóricos | se suavizan | "visible brushwork, textured edges" |
| Clave baja / subexpuesto | el modelo aclara solo | "deep shadows hold no detail, exposed for the highlights" |
| Grano o defectos de impresión | desaparecen | palabras de proceso: "scanned 35mm negative, halation on highlights" |
| Aire / espacio negativo | el modelo lo rellena | "vast empty [color] field filling 70% of the frame" |

## Paletas alternativas ("sorpréndeme")

Tres paletas con nombre que respeten la LÓGICA de color del ADN y cambien todos los tonos:

- Cada una: nombre, 5 a 7 HEX, una línea de ánimo y proporción de uso.
- Distintas de verdad: una cálida, una fría, una inesperada.
- Comprobar que la estrategia sobrevive: si el ADN es "apagado con un acento saturado", las tres
  llevan exactamente esa estructura.

## Coherencia en una serie

- Se congela un **sufijo de estilo** (todo lo que va detrás del sujeto): mismas palabras en
  cada prompt.
- Solo varían el sujeto y el entorno.
- Relación de aspecto y ajustes del modelo, constantes.
- El sufijo va escrito en el entregable, listo para copiar.
- La prueba antes de darlo por bueno: pegarlo detrás de tres sujetos muy distintos y
  comprobar que los tres salen en el mismo estilo.
