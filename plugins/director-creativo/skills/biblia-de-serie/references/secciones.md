# El molde de la biblia y las secciones que esta skill añade

## El molde base

Toda biblia empieza con estas secciones, cortas y en este orden. Si el personaje ya tiene una
biblia con otro formato, se respeta y se le añaden las secciones de más abajo.

- **Quién es:** una tabla con nombre, edad, ciudad, oficio y a quién le habla.
- **Aspecto:** pelo, piel, rasgos, ropa habitual y marcas que lo distinguen.
- **Arquetipo y voz:** qué papel cumple, cómo habla, sus muletillas y lo que nunca diría.
- **Color firma:** el color o la prenda que lo distingue de los demás personajes de la marca.
- **Elementos de Higgsfield:** el identificador de su personaje Soul y la foto de cara que va
  primera.
- **Pendiente:** todo lo marcado como `[POR DECIDIR]`.

## Las secciones que añade esta skill

Son secciones **libres**, que van al final del mismo documento, con estos títulos exactos para
que siempre se encuentren igual. Un personaje, un documento.

Todo dato lleva su fuente entre corchetes: `[reel 03]`, `[carrusel 01]`, `[biblia v2]`,
`[decisión de <quién>, <fecha>]`.

---

## `## Lo que ya se ha contado`

Una fila por pieza publicada, la más reciente arriba.

```markdown
## Lo que ya se ha contado

| Pieza | Fecha | Qué estableció (hechos nuevos) | Gancho | Cierre / CTA |
|---|---|---|---|---|
| <pieza> | <fecha> | <hecho nuevo> [<pieza>] | "<gancho literal>" | "<cierre literal>" |
```

Lo que importa es la columna del medio: **qué quedó dicho que ya no se puede desdecir**. El
gancho y el cierre están para no repetirlos sin querer y para comparar con los otros personajes
de la misma marca.

---

## `## Hilos abiertos`

Lo sembrado que todavía no se ha pagado.

```markdown
## Hilos abiertos

| ID | Qué se sembró | Dónde | Tipo | Estado | Cómo se paga / dónde se pagó |
|---|---|---|---|---|---|
| H1 | "<lo que se prometió, literal>" | [<pieza>] | promesa | ABIERTO | idea: <cómo se podría pagar> |
| H2 | <lo que se sembró> | [<pieza>] | preparación | AVANZADO [<pieza>] | |
| H3 | <...> | [<pieza>] | misterio | PAGADO [<pieza>] | <cómo se pagó> |
| H4 | <...> | [<pieza>] | sin querer | ABANDONADO, decisión de <quién>, <fecha> | |
```

Tipos:
- **promesa:** algo que se le prometió al público ("la semana que viene"). Es el que más daña
  si se olvida.
- **misterio:** una pregunta que la serie dejó abierta.
- **preparación:** algo que se enseñó para usarlo después.
- **sin querer:** un hilo que nadie quiso abrir pero quedó abierto. Se señala siempre.

Un hilo solo sale de la tabla como PAGADO o ABANDONADO, con fuente o con decisión y fecha.

---

## `## Continuidad fina`

Los datos pequeños que rompen la ilusión cuando fallan.

```markdown
## Continuidad fina

### Ropa y aspecto por pieza
- <personaje>: <prenda> [<pieza> a <pieza>] · <otra prenda> en <set> [<pieza>]

### Objetos
- <objeto>: <cómo es y quién lo tiene> [<pieza>]

### Fechas, edades y números (BLOQUEADOS)
- <Nombre del personaje>: 44 años declarados [biblia]. Cambiar esto es una decisión explícita

### Nombres y grafías
- <nombre canónico> (no <variante que se cuela>)

### Referencias de producción
- Cara: `referencias/cara.jpeg`, siempre la primera
- Elemento de Higgsfield: el id está en la sección de elementos del molde
```

---

## `## Relaciones` (si el personaje tiene gente alrededor)

```markdown
## Relaciones

### <personaje> y <otra persona>
- Qué son: <relación> [<fuente>]
- Cómo ha ido cambiando: [pieza] → [pieza] → ahora
- Lo que uno sabe y el otro no: ...
```

---

## `## El mundo de la serie` (solo si la serie tiene mundo propio)

Si lo que hay es el mundo de **una marca** (sus sets, lo que nunca se dice, su tono), eso vive
en el documento de tu marca, no aquí: se lee y, si aparece una regla nueva, se propone
añadirla allí. Esta sección es para cuando **una cuenta concreta** tiene su
propio mundo (una casa, un barrio, un trabajo, una rutina).

```markdown
## El mundo de la serie

### Reglas (lo que nunca pasa aquí)
- <lo que nunca pasa> [decisión de <quién>, <fecha>]

### Lugares
| Sitio | Cómo es (fijo) | Referencia |
|---|---|---|
| Cocina | Paredes verde salvia, molduras blancas, ventana de guillotina | `SET - COCINA vacia.jpeg` |

### Calendario
- Lo que ya ha pasado en la vida del personaje, en orden, con la pieza que lo contó

### Por decidir
- [POR DECIDIR] ...
```

---

## `## Registro de cambios`

Solo se añade, nunca se reescribe. La entrada más reciente arriba.

```markdown
## Registro de cambios

### <fecha>
- Leído: <pieza>
- Choques: 1 rotura (resuelta: manda lo nuevo, decisión tuya), 1 nota
- Hilos: H2 avanzado, H5 abierto (nuevo)
- Biblia guardada: versión 3
```

La última línea importa: si la biblia se editó y la versión nueva no se guardó (o una copia
quedó atrás), aquí se ve.
