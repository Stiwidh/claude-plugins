---
name: cot-multi-element-scene
description: Chain-of-Thought espacial (foreground / mid-ground / background) para escenas con 3+ sujetos o elementos. Reduce ambigüedad espacial, respeta jerarquía visual, mejora interpretación del modelo. Aplicar siempre que el subject tenga 3+ elementos con interacción o cuando hay riesgo de "everything in one sentence" colapsando la composición.
user-invocable: true
argument-hint: "<scene-description>"
allowed-tools:
  - Read
---

# Skill — Chain-of-Thought Multi-Element Scene

## Por qué funciona

Los modelos de imagen y video priorizan tokens iniciales. En escenas multi-elemento, describirlas en una frase larga colapsa la jerarquía:

❌ **Plano denso, sin jerarquía:**
```
"A knight fighting a dragon in a castle courtyard with fire and people watching"
```
El modelo no sabe qué priorizar. Resultado: composición ambigua, escala incorrecta, sujetos compitiendo por atención.

✅ **CoT espacial estructurado:**
```
"Medieval castle courtyard at dusk.

FOREGROUND: A knight in silver armor lunges forward with raised sword, cape billowing behind him.
MID-GROUND: A massive red dragon rears back, flames erupting from its mouth.
BACKGROUND: Stone castle walls with terrified onlookers peering from windows.
LIGHTING: Orange firelight from the dragon's breath, purple twilight sky overhead, sharp shadows from front lighting."
```

Resultado: composición clara, jerarquía respetada, escalado correcto.

## Cuándo aplicar

Aplicar CoT espacial cuando:

- **3+ sujetos** en la escena (personas, animales, objetos prominentes)
- **Hay interacción** entre elementos (no solo coexistencia)
- **Hay jerarquía espacial** importante (uno principal, otros secundarios)
- **El use case requiere claridad compositiva** (ads, narrative video, hero shots)

**NO aplicar CoT** en escenas simples (1-2 sujetos sin interacción compleja), portraits únicos, abstractas/motion graphics.

## Estructura canónica

```
[Establishing shot: location + time + atmosphere]

FOREGROUND: [Protagonista + action + detalle distintivo]
MID-GROUND: [Supporting elements + interacción + escala]
BACKGROUND: [Environment + atmosphere + extras out-of-focus]
LIGHTING: [Setup completo coherente con la escena]
```

## Ejemplos por use case

### Brand video — equipo trabajando

```
Modern open-plan office at mid-morning, bright productive atmosphere.

FOREGROUND: Founder (mid-30s, dark sweater, glasses) stands at standing desk, gesturing with hands while explaining something on laptop screen.
MID-GROUND: Two team members (junior designer + senior dev) lean in attentively, one taking notes on tablet, the other nodding.
BACKGROUND: Out-of-focus open office with subtle plants, soft window light streaming from camera-left, other team members visible faintly typing.
LIGHTING: Soft natural window light from camera-left (key), gentle fill from above (overhead office lights), warm color temperature 4000K, medium-high intensity, bright productive mood.
```

### E-commerce flatlay — multi-product

```
Premium minimal product flatlay on natural walnut surface, top-down 45° tilt.

FOREGROUND: Hero product (ceramic coffee mug) centered, steaming, perfectly aligned.
MID-GROUND: Leather notebook (closed, brass clasp) angled 15° left, fountain pen resting on top.
BACKGROUND: Small succulent plant in terracotta pot at upper-right corner, subtle wooden ruler at lower-edge running horizontal.
LIGHTING: Diffused overhead studio softbox (key) with subtle warm fill from camera-back-right, deep depth of field (everything sharp), commercial editorial style.
```

### Cinematic narrative — multi-character scene

```
Noir-style detective office, late 1940s, rainy night.

FOREGROUND: Detective (trench coat, fedora) sits at desk facing camera, lighting a cigarette, face half-shadowed by table lamp.
MID-GROUND: Mysterious client (femme fatale silhouette in red dress) stands in doorway frame, hand on door handle, only partially visible.
BACKGROUND: Rain-streaked window with neon city lights blurred behind, wooden bookcase faintly visible to one side.
LIGHTING: Hard amber key from table lamp (Rembrandt-style), cool blue rim from window (neon implication), high contrast film noir, smoke layer adding atmospheric depth.
```

### Marketing carrousel — "before vs after" split

```
Split composition advertisement, top-down 45° tilt, deep depth of field, 4:5 vertical.

LEFT HALF (FOREGROUND of left zone):
- Cluttered manual workflow: paper folder, ballpoint pen, scattered sticky notes
- Color palette: muted earth #8B7355, #D4C4A8
- Caption "Antes" in Inter Medium 24pt color #8B7355, top-left

RIGHT HALF (FOREGROUND of right zone):
- Clean automated workflow: modern smartphone showing simple UI with checkmark
- Color palette: marca purple (ejemplo) #13052D background, #9245FF accents
- Caption "Después" in Inter Medium 24pt color #9245FF, top-right

CENTER: Thin vertical gradient line (#8B7355 → #9245FF) as visual divider

LIGHTING: Diffused overhead studio, high intensity, clean commercial style.
```

## Reglas

1. **MAX 4 capas** (foreground / mid-ground / background / lighting). Más capas diluyen.
2. **CADA capa con UN sujeto principal** + descripción. No meter 5 cosas en foreground.
3. **JERARQUÍA explícita:** lo más importante en foreground, lo más contextual en background.
4. **LIGHTING como capa propia:** no mezclar con descripción de sujetos.
5. **NO usar "and"** para concatenar elementos en una capa — usa frase por elemento.
6. **AJUSTAR el lens al ancho de campo:** wide lens (28mm) captura más capas, telephoto (85mm+) comprime y suele tener menos capas visibles.

## Anti-patterns

❌ **CoT en escena simple:**
```
"Portrait of CEO.
FOREGROUND: CEO smiling.
MID-GROUND: (nada).
BACKGROUND: gray wall."
```
Demasiada estructura para una composición simple. Usar prompt natural normal.

❌ **CoT con sobrecarga por capa:**
```
"FOREGROUND: 5 personas haciendo 5 cosas distintas con 5 objetos."
```
Sigue siendo overload — divide en sub-capas o simplifica.

❌ **CoT sin lighting layer:**
```
"FG: knight. MG: dragon. BG: castle." (sin LIGHTING)
```
La iluminación une la composición. Sin ella, las capas parecen recortes pegados.

## Combinación con otras skills

- **+ `text-rendering-pattern`:** si una capa incluye texto, aplicar sintaxis específica del modelo
- **+ `negative-prompt-library`:** añadir negative del use case (personas, producto, video)
- **+ `audio-cue-syntax`** (video): el audio puede tener su propia "capa" sincronizada con foreground/background

## Cómo se integra al JSON v2.0

El CoT vive en `subject.main` + `subject.secondary_elements`:

```json
{
  "subject": {
    "main": "FOREGROUND: [protagonista]. MID-GROUND: [supporting]. BACKGROUND: [environment].",
    "secondary_elements": ["[detalle FG]", "[detalle MG]", "[detalle BG]"]
  },
  "lighting": {
    "type": "Cinematic",
    "direction": "[setup completo]",
    "intensity": "High",
    "mood": "[atmosphere]"
  }
}
```

El natural language prompt usa la estructura CoT explícita con saltos de línea.

---

**Aplicación:** el `lyra-engineer` invoca esta skill cuando detecta escenas con 3+ elementos en `subject`. El `visual-prompt-auditor` flagea si una escena multi-elemento NO usa CoT (anti-pattern de información overload).
