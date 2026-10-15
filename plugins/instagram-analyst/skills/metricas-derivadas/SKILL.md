---
name: metricas-derivadas
description: >-
  Convierte los datos crudos de una cuenta de Instagram (followers, views, likes, comentarios, fechas) en métricas que sí dicen algo: engagement rate normalizado, qué post rompió (índice de outlier), ratio comentarios/likes, ritmo de publicación y mix de formatos. Se activa tras recolectar una cuenta, para separar lo que de verdad funciona de la vanidad. Solo usa lo visible, no inventa reach ni guardados.
---

# Métricas que sí dicen algo (no vanidad)

Fase 2. Ya tienes la tabla de posts de `recolectar-cuenta`. Aquí la conviertes en **señales comparables**. El número de views suelto engaña (una cuenta con 200k followers siempre tendrá más que una de 5k). Estas métricas corrigen eso.

Calcula por cuenta, con lo que recogiste. Si te falta un dato, dilo y sigue con los que tengas.

---

## 1. Engagement rate (ER): el gran igualador

Permite comparar cuentas de tamaños distintos.

```
ER de un post = (likes + comentarios) / seguidores  × 100
ER de la cuenta = media del ER de sus posts
```

Lectura orientativa (IG 2026, varía por nicho):
- **< 1%** flojo · **1-3%** normal · **3-6%** bueno · **> 6%** muy bueno.
Lo importante no es el número absoluto, sino **comparar las cuentas entre sí** y contra la tuya.

---

## 2. Índice de outlier: qué post ROMPIÓ

La media miente: te interesa el post que se salió de su propia norma, porque ahí está lo que funcionó.

```
mediana = el valor del medio de las views (o likes) de sus posts
índice de outlier de un post = views del post / mediana de la cuenta
```

- **≈ 1** rinde como lo normal de esa cuenta.
- **≥ 2-3** es un **outlier**: rompió. Esos son los que hay que diseccionar (formato + gancho + tema). Van a la fase de creativos.
- Usa **mediana**, no media (un solo viral dispararía la media y falsearía el resto).

---

## 3. Ratio comentarios/likes: comunidad vs like fácil

```
ratio = comentarios / likes
```

- Ratio **alto** (mucho comentario por like) → contenido que genera **conversación**, comunidad real, gente que se moja.
- Ratio **bajo** → like de pasada, más vanidad.
Cruza esto con lo que leíste en los comentarios (¿público comprador o aplausos?).

---

## 4. Ritmo de publicación

Con las fechas de los posts:
```
posts por semana ≈ nº de posts / semanas que cubren
```
Anota también la **consistencia** (¿publica regular o a rachas?) y el **mix de formatos** (% reels vs carruseles vs fotos). Muchas veces el rendimiento se concentra en un formato: dilo.

---

## 5. Dónde se concentra el rendimiento

Mira qué **formato** y qué **tema/ángulo** acumulan los outliers. Si el 80% de lo que rompe son reels de "voz en off + b-roll" sobre un tema concreto, esa es la mina.

---

## Salida de esta skill

Por cuenta: ER medio, lista de **outliers** (post + índice), ratio comentarios/likes, posts/semana, mix de formatos y **dónde se concentra el rendimiento**. Con esto, pasa a `analizar-contenido` (estrategia) y `analizar-creativos` (los outliers). Recuerda: todo se calcula sobre lo **visible**; nada de reach/guardados inventados.
