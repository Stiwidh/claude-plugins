---
name: estilo-visual
description: Leer el ADN de un estilo visual (9 capas) y convertirlo en prompts que lo reproducen sin copiarlo, fijar el look de una pieza con un fotograma de estilo, mantenerlo en una serie con un sufijo fijo, y montar un moodboard con paleta HEX. Separa la paleta (se cambia) de la lógica de color (es el estilo). Trigger keywords - estilo, look, quiero que se vea como esto, referencia visual, sacar el estilo de estas imágenes, ADN del estilo, moodboard, paleta, paleta de colores, identidad visual, dirección de arte, que todos los planos tengan el mismo look, que la serie sea coherente, copiar el estilo sin copiar los colores, sref, style reference, fotograma de estilo.
---

<!--
@SHARED_WITH
  Copia adaptada para la comunidad de Protocolo EVA. Tiene gemelas internas: un cambio de doctrina se replica a mano en todas. Registro: SHARED_COMPONENTS.md
-->

# Estilo visual

**Ver el estilo, no el tema.** Un estilo no es "fotos de café en tonos naranjas": es cómo cae
la luz, a qué distancia está la cámara, dónde se permite la saturación y qué textura tiene la
superficie. Eso es lo que se lleva de una referencia a otra pieza. El tema y los colores
concretos se pueden cambiar.

Adaptado de la skill "Visual Style Suite" (Skill Library de Ann).

---

## 0. Qué modo toca

| Modo | Cuándo | Qué sale |
|---|---|---|
| **TRADUCIR** | Una referencia ("quiero este estilo, pero con mis colores") | Qué se queda y qué se tira + paleta nueva + 2 o 3 prompts |
| **EXTRAER** | Varias referencias (3 o más): "qué tienen en común", "mi estilo" | Documento de ADN del estilo, reutilizable |
| **MOODBOARD** | Inspiración + "moodboard", "dirección de arte", "identidad visual" | Paquete de dirección: paleta HEX, 9 celdas con su prompt, tipografías |
| **FIJAR** | Una pieza con 2 o más clips, o una serie | Fotograma de estilo + sufijo de estilo fijo |

Si no está claro, una pregunta con las opciones. Se encadenan: EXTRAER alimenta a MOODBOARD y
a TRADUCIR; cualquiera de los tres acaba en FIJAR cuando se va a producir.

**La marca manda.** Si la pieza es de una marca con manual de identidad, su paleta, tipografía
y prohibiciones van por encima de cualquier paleta que salga de aquí. Aquí se propone el
estilo; el manual pone los límites.

## 1. La lectura del ADN (todos los modos)

Por cada imagen, en este orden (detalle y vocabulario en `references/adn-9-capas.md`):

1. **Luz:** dirección, calidad, contraste, temperatura de la propia luz.
2. **Composición:** lógica del encuadre, aire, recorrido de la mirada, profundidad.
3. **Cámara:** sensación de focal, profundidad de campo, ángulo, distancia.
4. **Acabado:** fotográfico, pictórico, gráfico o 3D; bordes; dónde se concentra el detalle.
5. **Textura y materiales:** superficies, grano, desgaste.
6. **Relaciones de color:** la LÓGICA, no los colores (ver abajo).
7. **Registro emocional:** en dos palabras, y qué combinación lo produce.
8. **Época y género:** marcas de periodo y de género, y cuáles sostienen el estilo.
9. **Trato del sujeto:** heroico, espontáneo, clínico, tierno, icónico.

**Regla de oro de la capa 6:** la paleta es superficie; la lógica de color es ADN. "Un acento
complementario que ocupa el 10 %" es ADN. "Naranja y azul verdoso" es paleta.

**La prueba de ADN o superficie:** si cambio esto, ¿se sigue reconociendo el estilo? Si sí, es
superficie (colores concretos, temas, lugares). Si se viene abajo, es ADN (comportamiento de
la luz, lógica de color, acabado, distancia, la máquina que produce el ánimo).

## 2. TRADUCIR: el estilo de otro, con tus colores

1. Lectura del ADN de la referencia. Si solo hay un código de estilo o un nombre, se piden una
   o dos imágenes de muestra: un código a secas no se puede analizar.
2. Tabla **SE QUEDA (ADN) / SE TIRA (superficie)**. A la segunda columna van la paleta, los
   temas firma y las composiciones reconocibles.
3. Paleta destino: la de la marca si la hay; si no, la que diga quien pide, o se ofrecen tres
   con nombre y una línea de ánimo cada una.
4. Dos o tres prompts que codifican la columna SE QUEDA con la paleta nueva
   (`references/recetas-prompt.md`).
5. **Aviso de deriva:** qué elementos del ADN son frágiles al generar y cómo reforzarlos.

## 3. EXTRAER: el estilo de un conjunto

1. Lectura del ADN por imagen, en notas agrupadas.
2. **Invariantes:** lo que aparece en el 70 % o más del conjunto es ADN; del 30 al 70 %,
   tendencia; por debajo del 30 %, ruido. Se dicen los dos lados: lo fijo y lo libre.
3. Un nombre de trabajo de 2 a 4 palabras. Un estilo con nombre se usa; uno sin nombre, no.
4. Documento de ADN con la plantilla de `references/plantilla-adn.md`: principios por capa,
   parejas de sí y no, las **3 jugadas firma**, parámetros libres y sufijo de estilo.
5. **Cláusula de diferenciación:** 2 o 3 desvíos deliberados para que el estilo sea propio y
   no una imitación de las referencias.

## 4. MOODBOARD: de la inspiración a una dirección de arte

1. Lectura del ADN de todo; paleta de 5 a 7 colores HEX (dominante, secundario, dos acentos,
   neutros) con nombre y proporción de uso (60/30/10).
2. Temas, materiales, luces y patrones de composición que se repiten.
3. **Moodboard de 3 × 3:** nueve celdas, cada una con su contenido, su papel y qué capa del ADN
   carga. Equilibrio: 2 o 3 de textura o material, 2 o 3 de sujeto, 1 o 2 de color o
   abstractas, 1 de tipografía, 1 de luz o ambiente.
4. El paquete: nombre de la estética y manifiesto de una línea, paleta con proporciones, los
   nueve prompts, 2 o 3 parejas tipográficas (titular y texto, con el porqué) y notas de
   dirección (qué dice, dónde funciona, qué evitar).
5. **Generar las nueve celdas es un lote:** se presupuesta y se pide el OK antes, como
   cualquier tanda de tres o más generaciones. Sin OK se entregan los prompts.

## 5. FIJAR: que toda la pieza parezca la misma película

**Una pieza con 2 o más clips:** un **fotograma de estilo**. Se genera (2 a 4 candidatos de un
momento clave, cada uno con un tratamiento distinto) o se aporta una imagen. El elegido va como
referencia en **todos** los planos de la pieza ("matching the look, grade and lighting of the
style reference"). El estilo va separado de los personajes a propósito: el estilo deriva con
facilidad y anclarlo a una sola imagen mantiene todos los planos en la misma película.

**Una serie (muchas piezas con el mismo look):** un **sufijo de estilo** fijo.

- Todo lo que va detrás del sujeto en el prompt se congela y se repite palabra por palabra.
- Solo cambian el sujeto y el entorno.
- Relación de aspecto y ajustes del modelo, constantes en toda la serie.
- El sufijo se guarda escrito en el documento de ADN para copiarlo tal cual.

## 6. Reglas

- **Describir, nunca reproducir.** Se analizan principios; no se promete replicar la obra de
  un artista vivo. Las influencias se nombran como "en la tradición de" y siempre se empuja
  hacia la diferenciación.
- **Cada recomendación con su porqué** en una línea.
- **Salidas largas a fichero** (documento de ADN, moodboard); la paleta y el veredicto, en el
  chat.
- Los HEX, los términos de cámara y los de oficio se quedan como son.

## Referencias

- `references/adn-9-capas.md`: el marco de análisis capa por capa, con vocabulario.
- `references/recetas-prompt.md`: cómo meter el ADN en un prompt, lista de lo frágil y
  paletas alternativas.
- `references/plantilla-adn.md`: la estructura del documento de ADN (modo EXTRAER).
