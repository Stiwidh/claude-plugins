# Plugin `director-creativo`: Director Creativo by Corvere Solutions

Plugin de Claude para la **comunidad de Protocolo EVA** que te lleva de una idea suelta a un **vídeo con IA** terminado: concepto, guion por escenas con la cámara de cada plano, un estilo visual coherente, qué modelo usar en cada plano, control de créditos y revisión de calidad. Es un director creativo cálido y claro: **no necesitas saber de planos ni de modelos de IA**, él decide y te explica cada decisión en lo que va a sentir quien mira.

---

## 🎬 Qué hace

- **Decide contigo el tipo de pieza** antes de nada: contenido de marca (nutrir) o anuncio de producto (vender). Las reglas son opuestas.
- **Escribe el guion por escenas:** qué dice la voz, qué se ve, con qué cámara y por qué, más 3 títulos y la idea de miniatura.
- **Fija el estilo:** saca el "ADN" de una referencia, monta un moodboard y hace que todos los clips parezcan la misma película.
- **Elige el modelo de cada plano** y te dice cuánto cuesta **antes** de generar.
- **Cuida la continuidad:** que el personaje no cambie de cara entre clips, prueba barata antes del render final, clips encadenados y transiciones.
- **Genera con Higgsfield** si tienes su conector conectado en tu Claude, o te deja los prompts listos para pegarlos donde generes.
- **Revisa la pieza** antes y después de generar (incluido el Virality Predictor de Higgsfield).

---

## ⚡ Cómo se activa

Habla normal: *"hazme un reel sobre X"*, *"un anuncio de la crema"*, *"genera una imagen de Y"*, *"cuánto cuesta este vídeo"*, *"pasa este PDF a vídeo"*. El Director (`creative-director`) coge el control y va decidiendo contigo. También puedes escribir `/` y elegir una de sus skills.

---

## ✅ Requisitos

- **Un plan de pago de Claude** (Pro o Max).
- **Para generar vídeo o imágenes:** una cuenta de Higgsfield con créditos y su conector conectado en Claude. Sin eso el plugin sigue sirviendo para el concepto, el guion, el estilo y los prompts.
- **Los créditos cuestan dinero.** El plugin te enseña el coste y **te pide el OK antes de gastar** cuando hay un lote de 3 o más generaciones. Los costes que cita son orientativos (con la fecha en que se consultaron): mira siempre el que te muestra tu cuenta.
- **Funciona mejor en Cowork o en la pestaña Code** de la app de escritorio de Claude.
- Solo para la skill de vídeo de diapositivas: Python 3 y ffmpeg en tu ordenador (Windows o Mac). No gasta créditos.

---

## 🗺️ Estructura

```
director-creativo/
├── .claude-plugin/plugin.json
├── README.md
├── agents/ (4 agentes)
│   ├── creative-director.md      ← EL DIRECTOR · decide tipo de pieza y orquesta
│   ├── higgsfield-maestro.md     ← ESPECIALISTA · qué herramienta, qué coste, qué prompt
│   ├── storyboard-artist.md      ← ESPECIALISTA · el guion por escenas, títulos, miniatura
│   └── creative-qa.md            ← AUDITOR · control de calidad antes y después
└── skills/ (15 skills)
```

---

## 🤖 Agentes

| Agente | Rol | Cuándo |
|--------|-----|--------|
| `creative-director` | **El Director** | Una idea suelta que hay que llevar a pieza terminada. Decide marca vs anuncio, el concepto, y orquesta al resto. |
| `higgsfield-maestro` | Herramienta y coste | Qué modelo de Higgsfield para cada plano, cuántos créditos cuesta y cómo escribir el prompt. |
| `storyboard-artist` | El guion | Escenas con voz, imagen, cámara y porqué; 3 títulos y la idea de miniatura. |
| `creative-qa` | Control de calidad | Antes de gastar créditos y antes de publicar: APROBAR / APROBAR CON CAMBIOS / RECHAZAR. |

---

## 🛠️ Skills

| Skill | Para qué |
|-------|----------|
| `produce` | Producir un vídeo entero, de la idea a la pieza revisada |
| `storyboard` | Solo el guion, sin producir nada |
| `generate` | Un asset suelto: una imagen, un clip, animar una foto |
| `presupuesto` | Cuánto cuesta un vídeo o un lote antes de generar |
| `miniatura` | Título y miniatura (la portada) |
| `soul-id` | Tu personaje fijo de IA (Soul) para que salga siempre la misma cara |
| `direccion-de-camara` | El porqué de cada plano y 46 movimientos de cámara listos para pegar |
| `estilo-visual` | Sacar el ADN de una referencia, moodboard y mismo look en toda la pieza |
| `continuidad-y-pruebas` | Que el personaje no cambie entre clips, prueba barata antes del final, encadenar clips y transiciones |
| `flux3-prompting` | Prompts de FLUX 3 para que el vídeo diga exactamente lo que pone en el guion |
| `estructura-de-guion` | Qué le falla a un guion y cómo subir una escena floja |
| `trailer-y-spots` | Anuncios de 15 a 90 segundos y tráileres |
| `biblia-de-serie` | Que un personaje sea el mismo de una pieza a otra, y que la serie no se contradiga |
| `direccion-de-voz` | Cómo tiene que sonar cada frase, y cómo cambiar la voz cuando toca |
| `video-de-diapositivas` | Pasar un PDF o un temario a vídeo narrado, con su propio programa |

---

## 🎞️ Dónde se genera

- **Conector de Higgsfield** (conversando): imágenes, vídeos y clips sueltos.
- **Plataforma web de Higgsfield:** Marketing Studio (anuncios terminados) y Cinema Studio (narrativo).
- **Google Flow, si lo usas:** lo usas tú a mano en el navegador. El plugin no se conecta a Flow: te deja el prompt y los ajustes listos y tú los pegas.
- **El montaje** de varias escenas, si hace falta, se hace en tu editor (CapCut o similar): aquí se generan los trozos.

---

## 🔒 Reglas que respeta

1. **Nada de gastar créditos a ciegas:** un lote de 3 o más generaciones lleva presupuesto y tu OK primero.
2. **Prueba barata antes del final** en vídeo de varios clips, y los clips que siguen a otro, de uno en uno.
3. **Aviso de IA:** presentador o voz de IA hacia público o clientes lleva el aviso "contenido generado con IA" (Art. 50 del reglamento europeo de IA).
4. **En contenido de marca,** el esfuerzo va en el título y la miniatura, con edición sencilla.
5. **No inventa modelos ni costes:** si no está seguro, lo comprueba en Higgsfield.

---

## 🤝 Con el resto de plugins de la comunidad

| Si necesitas... | Usa |
|-----------------|-----|
| El guion hablado de un Reel, TikTok o Short, con su gancho y sus títulos | `vega` |
| Decidir qué publicar y cuándo (el plan de contenido) | `stella` |
| Secuencias de stories de Instagram | `aria` |
| Prompts de imagen y vídeo pulidos para cada herramienta | `lyra` |

El Director convierte en vídeo lo que ellos planifican y escriben.

---

## 🚀 Instalación

### En la app de Claude (lo normal para la comunidad)

Necesitas la app de Claude en el ordenador y un plan de pago (Pro o Max).

1. Barra lateral → **Customize** → **Plugins**
2. **Agregar desde un repositorio** → pega `Stiwidh/claude-plugins`
3. En el catálogo **eva-comunidad**, instala **director-creativo**
4. Activa la sincronización automática del catálogo: así cada mejora te llega sola
5. Para usarlo, escribe `/` y elige, o describe la tarea y se activa solo

### En Claude Code

```bash
/plugin install director-creativo --marketplace Stiwidh/claude-plugins
```

---

## 📋 Changelog

- **1.0.1** (2026-10-15): el catálogo de instalación pasa a llamarse **eva-comunidad**.
- **1.0.0**: versión para la comunidad, basada en director-creativo 1.7.0.

---

## Créditos

Parte de la doctrina de cámara, estilo, continuidad, guion, tráiler, biblia, voz y vídeo de diapositivas procede de la Skill Library de Ann y de ai-camera-movements, reescrita, adaptada y verificada por Corvere Solutions.
