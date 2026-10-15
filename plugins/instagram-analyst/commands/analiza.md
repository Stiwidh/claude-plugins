---
description: Analiza cuentas de Instagram de competencia o referentes y devuelve qué les funciona, un benchmark y un plan para tu marca. Uso "/analiza @cuenta1 @cuenta2 @cuenta3".
---

# /analiza

Analiza las cuentas de Instagram que te paso y dime qué les está funcionando, con datos, para replicarlo en mi marca.

**Cuentas a analizar:** $ARGUMENTS

## Qué quiero que hagas

Actúa como el agente `instagram-analyst` y ejecuta el flujo completo **usando el navegador de verdad** (no describas lo que harías, hazlo):

1. **Pregúntame por mi marca** si no la conoces (a quién le hablo y qué vendo).
2. **Comprueba la sesión de IG** en el navegador. Si sale el muro de "inicia sesión", para y avísame (hay que entrar con una cuenta dedicada, nunca la de mi marca).
3. **Recoge** cada cuenta con la skill `recolectar-cuenta` (perfil + últimos 12-15 posts, a ritmo humano, solo mirando).
4. **Saca las métricas** con `metricas-derivadas` (engagement rate, qué post rompió, ritmo de publicación).
5. **Juzga la estrategia** con `analizar-contenido` (Stella + Vega + Aria).
6. **Disecciona los creativos ganadores** con `analizar-creativos`.
7. **Ensámblalo** con `informe-benchmark` y entrégame el informe en el chat + un documento para guardar.

Si no te paso cuentas en `$ARGUMENTS`, pídemelas (lo ideal, 3-5 por tanda).

Reglas: ritmo humano, solo miras (no likes, follows, comentarios ni mensajes), no te inventas métricas que no se ven, y el criterio lo tomas de los plugins de la comunidad, no lo reinventas.
