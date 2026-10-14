---
name: text-rendering-pattern
description: Sintaxis exacta para incluir texto literal en imágenes generadas — específica por plataforma (Nano Banana Pro, GPT Image 2, Midjourney V8.1, FLUX.2 Pro). Aplicar siempre que el JSON v2.0 tiene `text_in_image.elements` poblado. Sin la sintaxis correcta, los modelos suelen escribir mal o ignorar el texto.
user-invocable: true
argument-hint: "<platform>"
allowed-tools:
  - Read
---

# Skill — Text Rendering Pattern

## Por qué importa la sintaxis específica

Cada plataforma de imagen entrena con datasets distintos y responde a convenciones distintas. Pedir "Add text 'HELLO' in big letters" funciona mal en TODAS — el texto sale borroso, mal escrito o desplazado.

La sintaxis correcta por plataforma:

| Plataforma | Sintaxis canónica | Accuracy esperada |
|------------|-------------------|--------------------|
| Nano Banana Pro | `Include legible text: "TEXT" in [Font] typeface, [Size]pt, [Color hex], [Position]` | 92% multi-idioma |
| GPT Image 2 | Lenguaje natural detallado con reasoning cues | **~99% multi-script** (mejor del mercado) |
| Midjourney V8.1 | `"TEXT"` inline con comillas + describir tipografía | Buena en V8.1 (mejorado vs V7) |
| FLUX.2 Pro | Estructura multi-line típica `Line 1: 'TEXT' ...` | Excelente para multi-line typography |

## Soporte de texto por plataforma

| Plataforma | Soporte | Multi-script | Multi-line |
|------------|---------|--------------|------------|
| Nano Banana Pro | ✅ 92% accuracy | ✅ latín, CJK, hindi | ✅ |
| GPT Image 2 | ✅ ~99% accuracy | ✅ todos (latín, CJK, hindi, bengali, árabe) | ✅ |
| Midjourney V8.1 | ✅ Mejorado V8 | Limitado en non-latin | ✅ |
| FLUX.2 Pro | ✅ Typography engine | ✅ | ✅ EXCELENTE |
| Ideogram V3 (T2) | ✅ Best-in-class | ✅ | ✅ |
| Recraft V4 (T2) | ✅ Vector + raster | ✅ | ✅ |

**Imagen sin soporte text rendering:** SD4 Ultra (sigue limitado vs Tier 1), Wan 2.7 Image.

## Sintaxis canónica detallada

### Nano Banana Pro

```
Include legible text: "EXACT TEXT" in [Font Name] typeface, [Size]pt, [Color hex], [Position]
```

**Estructura mandatory:**
- Comillas en el texto literal
- Font especificado (Nano Banana entiende: Montserrat, Inter, Helvetica, Times, Arial, Roboto, Open Sans, Lato, Playfair, etc.)
- Size: en `pt` absoluto o relative ("large", "medium", "small")
- Color: hex code preferido
- Position: descriptiva ("top-left", "centered top", "bottom-right corner", "middle-left", etc.)

**Ejemplos:**

```
Include legible text: "CORVERE SOLUTIONS" in Montserrat Bold typeface, 72pt, #9245FF, centered top
```

```
Include legible text: "Adopción IA 2026" in Inter Bold typeface, 32pt, #13052D, centered top of frame
```

```
Include legible text: "78%" in Inter Black typeface, 96pt, #9245FF, middle-left as large statistic callout
```

**Multi-element text** (varias frases en la misma imagen):
```
Include legible text:
- "CORVERE" in Montserrat Black typeface, very large, #FAFAFA, centered top with wide letter-spacing
- "AI SOLUTIONS" in Montserrat Bold typeface, large, #9245FF, centered middle
- "FOR BUSINESS — 2026" in Montserrat Medium typeface, medium, #FAFAFA, centered bottom
```

---

### GPT Image 2

GPT Image 2 tiene reasoning nativo — la sintaxis es lenguaje natural detallado con reasoning cues.

```
Include the exact text "TEXT" in [Font] [Weight] [Size], color [hex], positioned [location].
Ensure proper character spacing and kerning. Verify legibility at intended viewing distance.

[Si multi-script:]
Use [language]-appropriate typography. Each language uses its native font.
```

**Ejemplos:**

```
Include the exact text "Adopción IA 2026" in Inter Bold 32pt color #13052D, positioned centered top.
Below the title, in italic and lighter color, include "AI Adoption 2026" in Inter Regular Italic 16pt color #666666.
Ensure proper character spacing and visual hierarchy between Spanish and English versions.
```

```
Generate a poster with three lines of text:
Line 1 (top, very large): "CORVERE" in Montserrat Black, color #FAFAFA, wide letter-spacing for visual impact
Line 2 (middle, large): "AI SOLUTIONS" in Montserrat Bold, color #9245FF
Line 3 (bottom, medium): "FOR BUSINESS — 2026" in Montserrat Medium, color #FAFAFA

Verify the typography hierarchy is clear: largest at top, smallest at bottom. Maintain consistent center alignment.
```

**Multi-script (ventaja única de GPT Image 2):**

```
Generate a multilingual poster:
- Spanish title: "IA para Empresas" in Inter Bold 48pt color #13052D
- English subtitle: "AI for Business" in Inter Regular 24pt color #666666
- Chinese footer: "企业人工智能解决方案" in PingFang SC 20pt color #999999

Each language uses its native typography. Spacing and proportions adapted per writing system. Verify Chinese characters render correctly without distortion.
```

---

### Midjourney V8.1

```
[scene description with text in quotes] --ar [ratio] --hd --q 4
```

**Estructura:**
- Texto literal en comillas dobles inline
- Descripción de la tipografía como parte del style del prompt
- NO usar parámetros JSON aquí — Midjourney es solo prompt natural + flags

**Ejemplos:**

```
A vintage poster with the text "CORVERE" rendered in bold serif typography, deep purple background --ar 3:4 --hd --q 4
```

```
Modern minimalist poster featuring large bold text "AI SOLUTIONS" in sans-serif font, vibrant magenta color on dark background --ar 16:9 --hd --q 4
```

**Limitaciones Midjourney V8.1 con texto:**
- Multi-line funciona pero menos preciso que FLUX/Nano Banana
- Multi-script limitado a latín (CJK genera errores frecuentes)
- Recomendación: para texto >5 palabras, usar otra plataforma

---

### FLUX.2 Pro

FLUX.2 Pro tiene typography engine optimizado para multi-line. La sintaxis ideal es structured:

```
[Scene description densa]

Multi-line typography layout:
Line 1: 'TEXT 1' in [Font] [Weight], color [hex]
Line 2: 'TEXT 2' in [Font] [Weight], color [hex]
Line 3: 'TEXT 3' in [Font] [Weight], color [hex]

Typography spec:
- Spacing: [tight / loose]
- Alignment: [centered / left / right / justified]
- Hierarchy: [largest at top / equal weight / decreasing size]
```

**Ejemplo (poster Swiss design):**

```
Premium event poster, vertical 3:4 format, Swiss design aesthetic in the tradition of Massimo Vignelli minimalism.

Three-line stacked typography layout, centered:
Line 1 (top, very large): "CORVERE" in Montserrat Black, color #FAFAFA, wide letter-spacing
Line 2 (middle, large): "AI SOLUTIONS" in Montserrat Bold, color #9245FF
Line 3 (bottom, medium): "FOR BUSINESS — 2026" in Montserrat Medium, color #FAFAFA

Typography spec: tight kerning on line 1, consistent baseline grid, increasing weight toward bottom for visual stability.

Background: vertical gradient mesh #13052D → #2A0F4D. Thin horizontal divider lines #4A3D6E between text lines.
```

**Kontext editing del texto** (cambiar solo el texto manteniendo el resto):

```
On the previous image, change Line 2 text to "FOR ALL". Keep typography, color, position, and the rest of the design identical.
```

## Reglas universales

1. **TEXTO LITERAL SIEMPRE ENTRE COMILLAS** — sin comillas, el modelo lo trata como descripción y improvisa.
2. **FONT EXPLÍCITO** — "bold typography" es vago. "Montserrat Bold" o "Inter Black" tiene resultado consistente.
3. **SIZE RELATIVO O ABSOLUTO** — "72pt" cuando se conoce el contexto, "large/medium/small" cuando es relativo.
4. **COLOR HEX** — siempre que sea distintivo del brand. "Purple" produce inconsistencia.
5. **POSITION DESCRIPTIVA** — "centered top" / "bottom-left corner" / "middle-right" — más específico mejor.
6. **MULTI-LINE → LISTAR LÍNEAS** — no concatenar todo en una frase.
7. **NEGATIVE PROMPT** — incluir `["illegible text", "misspelled words", "blurry letters", "distorted fonts"]`.
8. **VERIFICAR multi-script** — GPT Image 2 es la única plataforma confiable para non-latin scripts long-form.

## Anti-patterns

❌ `Add the text 'WELCOME'` (sin font, size, color, position → resultado random)
❌ `Big bold text saying CORVERE` (sin comillas → el modelo no sabe si es texto literal o descripción)
❌ `Multi-line text with the words HELLO and WORLD and CORVERE` (sin estructura → fragmentos pegados)
❌ Texto largo (>15 palabras) en Midjourney V8.1 (limit de accuracy)
❌ Multi-script complejo en Nano Banana Pro (mejor GPT Image 2)

## Cómo se integra al JSON v2.0

El campo `text_in_image.elements` se rellena con cada texto:

```json
{
  "text_in_image": {
    "elements": [
      {
        "content": "CORVERE",
        "font": "Montserrat Black",
        "size": "very large",
        "color": "#FAFAFA",
        "position": "centered top, wide letter-spacing"
      },
      {
        "content": "AI SOLUTIONS",
        "font": "Montserrat Bold",
        "size": "large",
        "color": "#9245FF",
        "position": "centered middle"
      }
    ]
  }
}
```

El natural language prompt construye la sintaxis específica de la plataforma desde este array.

---

**Aplicación:** el `lyra-engineer` invoca esta skill al construir el natural language cuando el JSON tiene `text_in_image.elements` poblado. El `visual-prompt-auditor` valida que la sintaxis del NL prompt coincida con la plataforma destino.
