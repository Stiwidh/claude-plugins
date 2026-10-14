---
name: weekly-calendar-planning
description: Planifica la semana completa de Instagram Stories del Protocolo EVA con balance correcto VENTA/MARCA/VsV según calendario canónico Lunes-Domingo. Trigger keywords - calendario stories, planificar semana, qué publicar mañana, semana stories, plan editorial stories, distribución secuencias.
---

# Weekly Calendar Planning (Stories)

Planifica la semana de stories siguiendo el **calendario canónico** Sistema Aria aplicado a tu marca personal. Cada día tiene un tipo asignado para mantener balance algorítmico (no quemar a la audiencia con venta) y narrativa coherente.

## Instructions

### Calendario canónico

| Día | Tipo | Función |
|---|---|---|
| **Lunes** | VENTA | Apertura de semana — promueve oferta principal o lead magnet |
| **Martes** | VENDER SIN VENDER | Demo, métrica, behind-scenes — refuerza el lunes sin repetir |
| **Miércoles** | MARCA | Autoridad técnica, posicionamiento, opinión |
| **Jueves** | VENTA | Recordatorio + nuevo ángulo de la oferta |
| **Viernes** | MARCA + VENDER SIN VENDER | Doble bloque — primero conexión personal, luego prueba |
| **Sábado** | DESCANSO | Sin secuencia. Permite reset algorítmico |
| **Domingo** | LIBRE | Lo que pida el momento — testimonio sorpresa, opinión, off-topic relevante |

### Paso 1 — Inputs

- **Tema central de la semana:** un eje narrativo que une los 5-7 días (ej. "miedo a mostrar la cara", "cómo nace un avatar", "la semana del lanzamiento")
- **Producto / oferta activa:** qué hay para vender (programa Skool, lead magnet, lista espera, webinar)
- **Material disponible:** fotos, vídeos, screenshots agendados
- **Eventos de la semana:** lanzamiento, sesión live, fecha límite, novedad técnica

### Paso 2 — Estructura narrativa de la semana

Cada secuencia debe **conectar** con la del día anterior. Patrón canónico:

```
LUN (Venta) → presenta oferta / abre loop
MAR (VsV) → da prueba real que valida lunes
MIE (Marca) → eleva con autoridad / opinión que conecta
JUE (Venta) → re-introduce oferta con nuevo ángulo
VIE (Marca + VsV) → cierra la semana con conexión + prueba final
DOM (Libre) → lo que pida el contexto o reposo
```

**Regla:** un mismo seguidor que ve toda la semana debe tener una experiencia narrativa, no 7 piezas inconexas.

### Paso 3 — Output (planning)

```
## Semana del [Lunes DD-MM] al [Domingo DD-MM]

**Tema central:** [eje narrativo]
**Oferta activa:** [producto / null]
**Eventos:** [lanzamiento / live / nada]

---

### LUNES — VENTA
- **Sub-tema:** [cómo conecta con tema central]
- **Producto/CTA:** [qué se promueve]
- **Keyword/Link:** [keyword ManyChat o link bio]
- **Material:** [qué se necesita]
- **Activar skill:** `secuencia-venta`

### MARTES — VENDER SIN VENDER
- **Sub-tema:** [validación del lunes]
- **Sub-tipo:** [demo / antes-después / métrica / BTS / validación externa]
- **Material:** [...]
- **Activar skill:** `secuencia-vender-sin-vender`

### MIÉRCOLES — MARCA
- **Sub-tema:** [autoridad / opinión / behind-scenes]
- **Tipo interacción:** [encuesta / cajita / reacción]
- **Material:** [...]
- **Activar skill:** `secuencia-marca`

### JUEVES — VENTA
- **Sub-tema:** [nuevo ángulo de la oferta]
- **Diferencia con lunes:** [no repetir formato — si lunes fue resultado, jueves angular dolor]
- **Material:** [...]
- **Activar skill:** `secuencia-venta`

### VIERNES — MARCA + VsV (doble bloque)
- **Bloque 1 (mañana):** MARCA — [conexión personal cierre semana]
- **Bloque 2 (tarde):** VsV — [prueba final coherente con tema]
- **Material:** [...]
- **Activar skills:** `secuencia-marca` + `secuencia-vender-sin-vender`

### SÁBADO — DESCANSO
- **No hay secuencia.** Reset algorítmico.

### DOMINGO — LIBRE
- **Sub-tema:** [lo que pida el momento — testimonio sorpresa, off-topic relevante]
- **Tipo:** [a definir]

---

📌 **Notas semanales:**
- Hilo rojo común a la semana: [elemento rojo recurrente]
- Tono general: [si hay lanzamiento, urgencia creciente; si no, cadencia normal]
- Coherencia narrativa: [cómo se conectan los días]
```

### Paso 4 — Anti-patrones

- ❌ 3+ días seguidos de VENTA — quema lista, baja engagement
- ❌ Todo MARCA en semana de lanzamiento — desperdicia tracción
- ❌ Días desconectados narrativamente — la semana se siente caótica
- ❌ Saltar sábado / publicar igual los 7 días — el algoritmo IG castiga
- ❌ Reusar mismo formato 4 veces (todos foto+texto) — visual monótono

## Knowledge Base

- `<plugin>/skills/aria-method/references/aria_method.md` (sección calendario)
- `<plugin>/skills/aria-method/references/aria_method.md`
- `<plugin>/skills/aria-method/references/aria_method.md` (histórico de lo que se ha publicado — evita repetir)

## Cross-skill / agent

- Si quieres GENERAR las 5-7 secuencias completas (no solo el planning) → activar agent `weekly-stories-batch`
- Cada día activa la skill correspondiente para producir la secuencia final
