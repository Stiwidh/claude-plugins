# instagram-analyst: tu analista de Instagram

Plugin de la comunidad de Protocolo EVA. Le pasas cuentas de Instagram (tu competencia o tus referentes) y Claude entra a sus perfiles **con el navegador**, saca **métricas de verdad** y te devuelve un informe con qué copiar en tu marca.

**Cómo piensa:** este plugin recoge y calcula. El **criterio** de qué hace bueno un contenido no lo reinventa: lo toma de los otros plugins de la comunidad (**Stella** para la estrategia, **Vega** para ganchos y guiones, **Aria** para cómo abre y la narrativa). Si los tienes instalados, el análisis es más fino.

## Cómo se activa

> "analízame estos perfiles: @cuenta1 @cuenta2 @cuenta3"
> "qué le funciona a @cuenta"
> "estudia esta competencia y sácame ideas"
> "/analiza @cuenta1 @cuenta2"

Lo ideal, 3-5 cuentas por tanda.

## Qué hace (5 fases)

1. **Recoge** con el navegador: perfil (seguidores, bio, ritmo) y últimos 12-15 posts (reproducciones, likes, comentarios, gancho, formato, CTA). A ritmo humano y solo mirando. (`recolectar-cuenta`)
2. **Saca métricas de verdad**: engagement rate, qué post **rompió** (índice de outlier), ratio comentarios/likes y ritmo. Separa lo que funciona de la vanidad. (`metricas-derivadas`)
3. **Juzga la estrategia**: nivel del embudo y de consciencia (Stella), ganchos, ángulo y retención (Vega), cómo abre y si hay historia (Aria). (`analizar-contenido`)
4. **Disecciona los creativos ganadores** con ojo de anunciante. Si tienes yt-dlp, ffmpeg y whisper, saca el gancho literal de cada reel que rompió; si tienes Higgsfield conectado, le pide su nota. (`analizar-creativos`)
5. **Ensambla el informe**: ficha por cuenta, benchmark comparativo, creativos diseccionados, swipe file y plan para tu marca con calendario. (`informe-benchmark`)

## Qué entrega

Informe en el chat y, si lo pides, documento Markdown para guardar. Dentro: veredicto **comprador o vanidad** por cuenta, tabla comparativa, los posts que rompieron diseccionados, un swipe file de ganchos y un plan de contenido priorizado para tu marca.

## Requisitos

- **Plan de pago de Claude** (Pro o Max) y la **app de escritorio** (Cowork o la pestaña Code), con un **navegador conectado a Claude** (por ejemplo, Claude in Chrome). En el chat web no navega.
- **Sesión de Instagram iniciada en ese navegador con una cuenta dedicada**, nunca la de tu marca. Si sale el muro de "inicia sesión", el agente para y te avisa: hay que entrar una vez, a mano.
- **Opcional:** los plugins `stella`, `vega` y `aria` para el juicio completo; yt-dlp, ffmpeg y whisper para el gancho literal (pestaña Code); el conector de Higgsfield para la nota de cada reel (puede gastar créditos).

## ⚠️ Antes de usarlo: Instagram y la recogida automatizada

Las [condiciones de uso de Instagram](https://help.instagram.com/581066165581870/) no permiten recoger información de forma automatizada sin su permiso, y Instagram [restringe las cuentas que lo hacen](https://help.instagram.com/740480200552298/). Este plugin navega a ritmo humano, solo mira y no interactúa, pero sigue siendo Claude quien recoge los datos. Por eso: **usa siempre una cuenta dedicada, nunca la de tu marca**, y úsalo sabiendo ese riesgo.

## Límites

- Solo datos **públicos y visibles**: reproducciones (reels), likes, comentarios y el contenido. Guardados, compartidos y alcance de cuentas ajenas **no se ven**, y no se inventan.
- Las cuentas **privadas** no se pueden analizar.
- Va a **ritmo humano** y **solo lee** (no da likes, no sigue, no comenta, no manda mensajes).

## 🚀 Instalación

### En la app de Claude (lo normal para la comunidad)

Necesitas la app de Claude en el ordenador y un plan de pago (Pro o Max).

1. Barra lateral → **Customize** → **Plugins**
2. **Agregar desde un repositorio** → pega `Stiwidh/claude-plugins`
3. En el catálogo **protocolo-eva**, instala **instagram-analyst**
4. Activa la sincronización automática del catálogo: así cada mejora te llega sola
5. Para usarlo, escribe `/` y elige, o describe la tarea y se activa solo

### En Claude Code

```bash
/plugin install instagram-analyst --marketplace Stiwidh/claude-plugins
```

---

## Estructura

```
instagram-analyst/
├── .claude-plugin/plugin.json
├── agents/instagram-analyst.md     ← orquestador: navega, aplica el criterio y ensambla
├── commands/analiza.md             ← disparo directo "/analiza @x @y"
└── skills/
    ├── recolectar-cuenta/     (fase 1) navegar un perfil y extraer los datos
    ├── metricas-derivadas/    (fase 2) engagement rate, outlier, ratios, ritmo
    ├── analizar-contenido/    (fase 3) lentes de Stella, Vega y Aria
    ├── analizar-creativos/    (fase 4) gancho, retención, gancho literal y Higgsfield
    └── informe-benchmark/     (fase 5) ficha, benchmark, swipe file y plan
```

## Changelog

- **1.0.0** (2026-10-15): versión para la comunidad, basada en la versión interna 2.0.0. El criterio pasa a Stella, Vega y Aria; nueva lente opcional con yt-dlp, ffmpeg y whisper para el gancho literal de cada reel; aviso sobre las condiciones de Instagram.
