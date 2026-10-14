---
name: manychat-keyword-routing
description: Escoge la keyword ManyChat correcta para una secuencia de stories Protocolo EVA. Verifica que NO colisiona con flujos existentes y mapea a flujo correcto. Trigger keywords - keyword ManyChat, automatización stories, responde X, flujo ManyChat, palabra mágica stories, link en bio vs keyword.
---

# ManyChat Keyword Routing

Escoge la keyword correcta para un CTA tipo "Responde [PALABRA]" en stories. **Una keyword mal asignada rompe la automatización** — la usuaria recibe el flujo incorrecto, o el flujo se solapa con otro.

## Instructions

### Paso 1 — Inputs

- **Objetivo del CTA:** captar lead / vender programa / inscribir webinar / repartir guía / activar VIP
- **Stage funnel:** primer contacto / nurturing / hot lead / cliente
- **Lead magnet asociado** (si aplica)

### Paso 2 — Consulta OBLIGATORIA antes de asignar keyword

**ANTES de proponer keyword nueva**, leer:

```
`<plugin>/skills/aria-method/references/aria_method.md`
```

Listar:
1. Keywords ya activas y a qué flujo apuntan
2. Keywords retiradas/legacy (no reutilizar)
3. Triggers compuestos (ej. "EVA + número")

Si el archivo no es legible o el path falla → PARAR. Pedir confirmación al usuario antes de inventar keyword nueva.

### Paso 3 — Reglas de naming de keyword

1. **MAYÚSCULAS** siempre — ManyChat es case-insensitive pero por convención EVA usa mayúsculas.
2. **1 sola palabra** — "GUIA" sí, "GUIA AVATAR" no (ambiguo, falla matching).
3. **Sin acentos ni Ñ** — usuarios escriben mal. "GUIA" no "GUÍA".
4. **5-8 caracteres** — corto se recuerda. "VIP", "EVA7", "AVATAR" sí. "INSCRIBETEYA" no.
5. **Semántica clara** — debe sugerir el contenido. "GUIA" para guía, "VIP" para programa premium, "AVATAR" para curso.
6. **No genérica** — "INFO", "HOLA", "SI" son malas (colisión obvia).

### Paso 4 — Casos canónicos por objetivo

| Objetivo | Keyword sugerida | Flujo destino esperado |
|---|---|---|
| Lead magnet "Guía EVA 2.0" | `GUIA` o `GUIA20` | Welcome + entrega PDF + nurturing 3 emails |
| Programa Skool gratis | `SKOOL` o `EMPEZAR` | Invite Skool + welcome message |
| Programa pago | `VIP` o `AVATAR` | Aplicación + sales call booking |
| Webinar / lanzamiento | `WEBINAR` + fecha | Inscripción + recordatorios |
| Lista espera | `ESPERA` | Subscriber list dedicada |
| Tutorial específico | nombre tutorial | Entrega tutorial + upsell |

(Verificar contra <tus flujos ManyChat> antes de confirmar — pueden estar ya tomadas o cambiadas.)

### Paso 5 — Output

```
## Keyword ManyChat — [Objetivo]

**Keyword propuesta:** `[PALABRA]`
**Flujo destino:** [Nombre del flujo en ManyChat]
**Estado:** [Existe activo / Crear nuevo]
**Verificación contra <tus flujos ManyChat>:** [SÍ — sin colisión / NO — colisiona con [X]]

### Texto sugerido del slide CTA:
"[Texto que invita a responder con la keyword]"
"Responde [PALABRA] y te llega ahora mismo."

### Si el flujo es nuevo:
- [ ] Crear flujo en ManyChat antes de publicar la story
- [ ] Documentar en <tus flujos ManyChat> (añadir entrada)
- [ ] Probar con cuenta de test antes de publicar
```

### Paso 6 — Anti-patrones

- ❌ Inventar keyword sin consultar <tus flujos ManyChat>
- ❌ Reutilizar keyword retirada (puede colisionar con campañas pasadas guardadas)
- ❌ Frase larga ("RESPONDE QUIERO LA GUIA") — falla matching
- ❌ Keywords con números arbitrarios sin lógica (`EVA847`)
- ❌ Crear flujo nuevo sin probar antes — usuaria recibe error y se va

## Knowledge Base

- `<plugin>/skills/aria-method/references/aria_method.md` (CRÍTICO — fuente única de verdad)

## Cross-skill

- Tras escoger keyword → activa skill de secuencia (`secuencia-venta`) y pásale la keyword final
- Si la keyword es para captación de lead magnet → puede activar también `copywriter:optin-leadmagnet` para el copy del slide CTA
