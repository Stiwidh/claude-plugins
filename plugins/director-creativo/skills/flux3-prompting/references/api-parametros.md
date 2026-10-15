# FLUX 3: parámetros, ejecución y coste

Verificado el 2026-09-09 contra `docs.bfl.ai` (referencia de API y skill oficial
`flux-3-generate`) y contra el catálogo **vivo** de Higgsfield por MCP.

---

## 1. Dónde se ejecuta, y qué cambia según por dónde

FLUX 3 Video se puede lanzar por dos caminos, y **no exponen lo mismo**.

### 1.1 Higgsfield (el camino normal, el del día a día)

Modelo `flux_3_video`, de Black Forest Labs. Comprobado en el catálogo en vivo:

| Parámetro | Valores | Por defecto |
|---|---|---|
| `duration` | Segundos enteros, 5 a 20 | 5 |
| `resolution` | `720p`, `1080p` | `720p` |
| `generate_audio` | booleano | `true` |
| Relaciones de aspecto | `auto`, `21:9`, `2:1`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16` | `auto` |
| Medios | roles `start_image`, `end_image`, `image_references`, `video_references` | - |

**Lo que Higgsfield NO expone hoy:** el modo borrador (`draft`). Ahí cada prueba se paga
como render completo, así que el ahorro sale de acertar el prompt a la primera, no de
tirar borradores.

### 1.2 API directa de Black Forest Labs

`POST https://api.bfl.ai/v1/flux-3-video`, autenticando con la cabecera `x-key`.

El campo `mode` es obligatorio y decide qué otros campos van:

| `mode` | Campo de medio | Qué hace |
|---|---|---|
| `t2v` | ninguno | Genera el clip solo con el texto |
| `i2v` | `keyframes` (obligatorio) | Pone tus imágenes en pantalla, píxel a píxel, como fotogramas fijados |
| `v2v` | `start_video` (obligatorio) | Continúa desde los últimos fotogramas de tu clip |
| `draft_enhance` | `draft_cache` (obligatorio) | Repite un borrador a calidad completa. **No acepta ningún otro campo, ni siquiera `prompt`** |

Ajustes comunes: `aspect_ratio`, `duration` (entero 5-20 o `"auto"`), `resolution`
(`hd` o `fhd`), `generate_audio`, `draft`, `safety_tolerance` (0 a 4, por defecto 2),
`version` (`latest`).

**El esquema es estricto.** Cualquier campo que no conozca devuelve un `422` nombrándolo
(`Extra inputs are not permitted`). Un campo obligatorio que falte, igual.

---

## 2. Reglas de los medios de entrada

**Keyframes (`i2v`).** De una a diez imágenes, mínimo 256x256, por URL pública o base64.

- Una imagen: es el primer fotograma.
- Dos: fijan principio y final, el modelo rellena el medio.
- Tres o más: la primera abre, la última cierra, el resto se reparten. **Requieren
  `duration` entero.**
- Pares `[segundo, imagen]` en orden ascendente: cada imagen cae en ese segundo exacto.
  También requieren `duration` entero.

Un keyframe **aparece en pantalla, píxel a píxel**. No existe ningún campo que lleve la
identidad de un sujeto sin poner la imagen en pantalla. Una imagen que solo sea inspiración
se describe con palabras, no se adjunta.

**Video de entrada (`v2v`).** Máximo 15 segundos y 50 MB de entrada, máximo 15 segundos de
salida. Ojo: la duración de `v2v` va de 5 a 15, no llega a 20. Y un vídeo de entrada a más
resolución puede recortar la duración máxima, lo que cambia la planificación por tramos.

---

## 3. Ejecutar el trabajo (API directa)

Es asíncrono: se envía, se recibe un `polling_url`, y se consulta hasta que termina.

1. **Enviar una vez.** Guarda el `id` y el `polling_url`.
2. **Consultar cada 6 segundos**, con la cabecera `x-key`, siguiendo redirecciones.

   Los estados son exactos:

   | Seguir consultando | Parar |
   |---|---|
   | `Pending`, `Reasoning`, `Generating` | `Ready` (bien), `Error`, `Request Moderated`, `Content Moderated`, `Task not found` (mal) |

   Ninguno de los estados finales pasa luego a `Ready`. Que tarde en pensar un encargo
   complejo es normal, no es que se haya colgado.

3. **Descargar de inmediato.** Las URLs firmadas caducan más o menos una hora después. El
   parámetro `se=` de la propia URL es la caducidad real: léelo, no lo supongas.

   Trampa cara y documentada: `result.samples` es una **lista**, y `result.draft_caches`
   también. El singular `result.draft_cache` es solo el primer elemento. Un cliente que lea
   solo el singular tira artefactos ya pagados que no se recuperan cuando la URL caduca.
   Recorre las dos listas enteras.

4. **Validar:** que el contenedor decodifica, que duración, resolución y aspecto son los que
   pediste, y que hay audio exactamente cuando lo pediste. Que sea técnicamente válido no
   quiere decir que esté aprobado.

### Errores

- **`429` al enviar:** el tope de generaciones simultáneas de la organización está lleno y
  **no se creó ninguna tarea**. No hay nada que consultar. Espera un hueco y reenvía el
  mismo cuerpo.
- **`429` al consultar:** la tarea existe y no le pasa nada. Espera y sigue consultando el
  mismo `polling_url`. **Nunca reenvíes**, o pagas un segundo render.
- **`503`:** espera acotada y reintento.

El límite es de **generaciones simultáneas** (5 por organización en la API), no de peticiones
por segundo. Para varios planos a la vez, tres en vuelo deja margen.

---

## 4. Modo borrador (solo API directa)

`draft: true` devuelve una vista previa rápida y barata más un `draft_cache`. Después,
`mode: "draft_enhance"` con ese `draft_cache` **repite esa misma generación** a calidad
completa, sin replanificar la escena.

Un borrador se juzga por si el suceso se lee, por la composición, por la cámara y por la
continuidad. Que se vea blando es el precio de los pocos pasos y se arregla solo en la
versión completa.

---

## 5. Coste

1 crédito = 0,01 USD. El vídeo se paga **por segundo**.

Precios **orientativos** de la API de BFL, verificados el 2026-09-09: pueden haber cambiado.
Compruébalos en tu cuenta antes de gastar, y si generas desde Higgsfield, manda el coste que
te enseñe Higgsfield.

| Modo | Render completo | Borrador |
|---|---|---|
| Texto a vídeo (`t2v`) | 0,17 $/s en `hd`, 0,29 $/s en `fhd` | 0,06 $/s |
| Imagen a vídeo (`i2v`) | 0,17 $/s en `hd`, 0,29 $/s en `fhd` | 0,06 $/s |
| Continuación (`v2v`) | 0,43 $/s en `hd`, 0,54 $/s en `fhd` | 0,12 $/s |

Cuentas rápidas que conviene tener en la cabeza:

- Un plano de 8 s en `hd`: **1,36 $**
- Un plano de 8 s en `fhd`: **2,32 $**
- Una pieza de cuatro planos de 5 s en `hd`: **3,40 $**
- El mismo plano de 8 s en borrador: **0,48 $**

Continuar un clip cuesta **dos veces y media** lo que generarlo de cero. Extender solo
cuando hace falta esa continuidad exacta.

El escalado de vídeo (`FLUX Video Upscale`) se paga por megapíxel-segundo: 0,07 $ en modo
preciso y 0,10 $ en modo creativo. Subir un clip de 10 s a 1080p sale a 1,39 $ o 1,98 $.
Admite hasta 20 s de entrada.

**Regla de gasto:** un lote de tres generaciones o más lleva presupuesto por escrito
y visto bueno antes de lanzarse.

---

## 6. Resolución: cuándo cada una

`720p` / `hd` es el nivel de trabajo: rápido, barato, suficiente para iterar, para redes y
para casi todo el movimiento dentro de producto.

`1080p` / `fhd` es el nivel de entrega: cabecera de una landing, un anuncio pagado, una
pieza de lanzamiento. Cuesta un 70% más por segundo.

---

## 7. Higgsfield frente a la API: qué usar

| Situación | Camino |
|---|---|
| Trabajo del día a día, conversando | Higgsfield, modelo `flux_3_video` |
| Necesitas borradores baratos para iterar | API directa (`draft`) |
| Necesitas continuar un clip existente (`v2v`) | API directa |
| Necesitas keyframes fijados a segundos exactos | API directa |
| Varios planos generados a la vez de forma programada | API directa con hasta 3 en vuelo |
