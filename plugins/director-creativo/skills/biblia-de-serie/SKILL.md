---
name: biblia-de-serie
description: >-
  La memoria de un personaje, una serie o una marca, para que la pieza 12 no contradiga a la 3. Arranca la biblia de un personaje o del mundo de una marca con pocas preguntas, prepara el briefing antes de cada pieza (dónde lo dejamos, qué no se puede contradecir, qué hilos están maduros), revisa cada pieza nueva contra lo ya contado antes de publicarla, y audita una biblia o una serie entera buscando contradicciones. Guarda todo en un único markdown por personaje, dentro de la carpeta de tu proyecto, con su kit de referencias, sin montar un sistema aparte. Trigger keywords - que mi personaje sea el mismo que en el reel 12, qué hemos contado ya de este personaje, que no se contradiga la serie, biblia del personaje, biblia de la serie, continuidad de la cuenta, qué dijo en el reel anterior, siguiente reel de mi personaje, personaje nuevo, avatar nuevo, el mundo de la marca, lo que nunca pasa en esta marca, hilos abiertos, esto choca con lo que ya dijimos, revisa la serie, repasa la biblia.
---

<!--
@SHARED_WITH
  Copia adaptada para la comunidad de Protocolo EVA. Tiene gemelas internas: un cambio de doctrina se replica a mano en todas. Registro: SHARED_COMPONENTS.md
-->

# Biblia de serie

Una serie de piezas acumula cientos de datos pequeños: la edad que dijo, cuántos hijos tiene,
qué frase de cierre usó el martes, qué prometió enseñar "la semana que viene". Las personas se
olvidan y las conversaciones con Claude empiezan de cero. La solución es que **todo lo que ya
es canon viva en un documento**, se lea antes de cada pieza y se actualice después.

Adaptado de "Story Series Manager" y "Worldbuilding Suite" (Skill Library de Ann), sobre las
piezas que ya tienes. **No monta un sistema nuevo:** un solo markdown por personaje, con su
molde y su kit de referencias. Esta skill le añade la memoria de lo contado y la revisión de
contradicciones.

---

## 0. Dónde vive cada cosa

La biblia vive como markdown en la carpeta de proyecto de la propia creadora, junto a las
piezas del personaje. Si todavía no tienes carpeta, se propone una (por ejemplo
`personajes/<nombre>/`) y se crea con tu OK.

| Qué | Dónde | Notas |
|---|---|---|
| **La biblia del personaje** | Un markdown `BIBLIA - <Nombre>.md` en la carpeta del personaje | Es el documento de trabajo y la única fuente de verdad. Se edita aquí |
| **Cómo se escribe** | El molde base de `references/secciones.md` (quién es, aspecto, arquetipo, color firma, elementos de Higgsfield, pendiente) y, debajo, las secciones de memoria | Un personaje, un documento |
| **Las referencias visuales** | Una carpeta `referencias/` dentro de la carpeta del personaje, con un `LEEME.md` (cara, ángulos, cuerpo, sets) | La foto de cara que va primera se anota en el `LEEME.md` |
| **El mundo de la marca** | El documento de tu marca (tono, lo que nunca dices, sets) y, si lo tienes, tu plan de contenido hecho con `stella` | Los sets, lo que nunca se dice, el tono |
| **Lo que ya se ha producido** | Las carpetas de piezas del personaje (guiones, brutos, montaje, publicaciones) | De aquí sale lo que la serie ya ha contado |

**Qué añade esta skill a la biblia:** unas secciones libres (lo contado, los hilos, la
continuidad fina) al final del mismo documento. La plantilla está en `references/secciones.md`.
No se crean ficheros aparte: **un personaje, un documento**.

## 1. Qué modo toca

| Modo | Cuándo |
|---|---|
| **ARRANCAR** | Personaje, avatar o serie nuevos, o un personaje que existe sin biblia |
| **ANTES DE LA PIEZA** | "Vamos con el reel 13 de mi personaje", "siguiente carrusel", "¿dónde lo dejamos?" |
| **DESPUÉS DE LA PIEZA** | Hay un guion, un reel o un carrusel nuevo y hay que mirarlo contra lo ya contado |
| **AUDITAR** | "Revisa la serie", "algo no cuadra", o antes de dar por buena una biblia nueva |

Si no está claro, una pregunta. Se encadenan: después de ARRANCAR, un AUDITAR rápido; el
DESPUÉS de una pieza es el ANTES de la siguiente.

## 2. ARRANCAR

**Preguntar antes de inventar.** El personaje y el mundo son de quien los encarga. Pero sin
interrogatorios: cada turno entrega algo.

1. **Leer lo que ya hay** (documento de marca, plan de contenido, personajes existentes, fotos).
   No se pregunta lo que el material ya contesta.
2. **Como mucho tres preguntas por turno**, cada una con 2 a 4 opciones concretas más
   "sorpréndeme". Orden de palanca: para qué sirve el personaje y a quién le habla, **lo que
   nunca puede decir ni hacer**, qué le da autoridad, su historia (3 a 5 hechos que siguen
   pesando), un martes normal de su vida, y la textura (sets, objetos firma, forma de hablar).
   Banco de preguntas en `references/auditoria-y-preguntas.md`.
3. **Límites antes que poderes.** Lo que el personaje no puede decir o prometer se define antes
   que lo que dice. Sin límites, cualquier pieza vale y ninguna se parece a la anterior.
4. **Consecuencias en cadena.** Cada dato aceptado arrastra otros dos o tres, y se apuntan
   ("si es enfermera, puede hablar de piel con autoridad, y no puede recetar").
5. **Números bloqueados.** Edad, años de casada, ciudad, número de hijos: una vez escritos,
   cambiarlos es una decisión explícita. Son la primera fuente de contradicciones.
6. **La prueba del martes:** si no se puede contar un día normal del personaje, es un perfil,
   no una persona.
7. Se escribe la biblia **con el molde base y las secciones** de `references/secciones.md`. Lo
   que falte se marca `[POR DECIDIR]`: nunca se rellena en silencio en una sesión posterior.

## 3. ANTES DE LA PIEZA: el briefing

Leer la biblia entera (está pensada para ser corta), el `LEEME.md` del kit de referencias y los
guiones de las últimas piezas. Devolver exactamente esto, corto:

- **Dónde lo dejamos:** dos o tres frases.
- **Continuidad activa:** lo que va a importar en esta pieza (ropa, set, lo que sabe o no sabe
  el personaje, qué se prometió).
- **Hilos maduros:** lo que se sembró y puede pagarse o avanzar aquí, con dónde se sembró y una
  idea de cómo. Si un hilo lleva muchas piezas dormido, se dice.
- **Cuidado con:** lo fácil de contradecir, y **lo que ya han usado los otros personajes de la
  misma marca hoy** (frases, CTA, ganchos). La unidad que se audita es la marca, no el
  personaje: dos cuentas de la misma marca diciendo lo mismo el mismo día lo ve quien sigue a
  las dos.

## 4. DESPUÉS DE LA PIEZA: choque y actualización

1. **Primero el choque**, contra la biblia y lo ya publicado, por gravedad:
   - **ROTURA:** contradice un hecho (edad distinta, un hijo de más, un set que "nunca" se usa).
     Se citan los dos lados con su fuente.
   - **DERIVA:** no contradice pero se aleja (habla de otra manera, salta de sitio sin motivo,
     repite el gancho de hace dos piezas).
   - **NOTA:** un hecho nuevo que ata el futuro; se confirma que es a propósito.
2. **Se pregunta antes de resolver.** Nunca se "arregla" en silencio ni la pieza ni la
   biblia: decide quien encarga si manda lo nuevo o lo de antes.
3. **Se actualiza la biblia:** hechos nuevos a su sección, hilos que cambian de estado,
   entrada en el registro de cambios.
4. **Se guarda la versión nueva** en el mismo documento, y en las copias si las hay (punto 5).

## 5. Reglas que la hacen fiable

- **La biblia es la única fuente de verdad.** Si la conversación y la biblia no coinciden, se
  dice; no se adivina.
- **Nunca se inventa canon.** Solo entra lo que está escrito en una pieza o lo que se ha
  aprobado. Las ideas van en el briefing, no en la biblia.
- **Todo dato con su fuente:** `[reel 03]`, `[carrusel 01]`, `[biblia v2]`. Un dato sin fuente
  es un rumor.
- **Un hilo no desaparece:** solo se cierra como `PAGADO [fuente]` o `ABANDONADO, decisión de
  <quién>, <fecha>`.
- **Lo que no se vio no se borra:** se marca como no visto.
- **Una sola biblia.** Se edita siempre el mismo markdown. Si has pegado una copia en otro sitio
  (un Proyecto de Claude, un documento compartido), se actualiza justo después de cada cambio;
  si no, queda desfasada y alguien trabajará con datos viejos.
- **Las referencias visuales son canon también:** el identificador del elemento de Higgsfield,
  la foto de cara que va primera, el set. Van en la biblia (la sección de elementos del molde) y
  en el `LEEME.md` del kit.
- **Una biblia no se lee a trozos para decidir:** antes de dar un dato por nuevo o por
  inexistente, se lee entera.

## 6. AUDITAR

Se pasa la lista de `references/auditoria-y-preguntas.md` (fechas y edades, sitios, reglas de
la marca, continuidad del personaje, lo que sabe cada uno, nombres y grafías, tono) sobre la
biblia y las piezas publicadas.

- Cada hallazgo cita **los dos lados** y dice en una línea por qué rompe.
- Dos arreglos por hallazgo: **parche** (el cambio mínimo) y **rehacer** (el de fondo), y qué
  conserva cada uno.
- Lo que parece contradicción pero puede ser a propósito se pregunta, no se marca como error.
- Máximo unos 15 hallazgos; el resto, resumido en una línea.
- Se cierra con lo que está sólido (dos o tres cosas de verdad, no relleno).

## Referencias

- `references/secciones.md`: el molde base de la biblia y las secciones que esta skill añade
  (lo contado, hilos, continuidad fina, el mundo de la serie, registro de cambios).
- `references/auditoria-y-preguntas.md`: el banco de preguntas para ARRANCAR y la lista de
  comprobación para AUDITAR.
