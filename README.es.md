# SEO, GEO, AEO y LLMO — Marco de Optimización Completo

**v2.0.0** · 1.599 líneas · 70KB

**Python ≥ 3.7** requerido. No necesita `pip install` — todos los scripts usan solo la biblioteca estándar.

**🌐 Leer en otros idiomas:** [English](README.md) · [Bahasa Indonesia](README.id.md) · [中文](README.zh.md) · [Español](README.es.md) · [日本語](README.ja.md)

Un skill integral para **visibilidad de búsqueda full-stack** — desde rastreabilidad y sitemaps hasta preparación para citas de IA e infraestructura preparada para agentes. Cubre las cinco capas de descubrimiento superpuestas:

```
SEO ↔ Entity SEO ↔ GEO ↔ AEO ↔ LLMO
```

## Cobertura

| Capa | Enfoque | Dimensión de Puntuación |
|------|---------|:----------------------:|
| **SEO** | Rastreabilidad técnica, on-page, hubs de contenido, backlinks, E-E-A-T | Técnica + Contenido |
| **Entity SEO** | Knowledge Graph, Wikidata QID, sameAs, Knowledge Panel | Entidad |
| **GEO** | Citación de IA (ChatGPT, Perplexity, Gemini), llms.txt, pricing.md, query fan-out | Preparación GEO |
| **AEO** | Fragmentos destacados (párrafo/lista/tabla), PAA, búsqueda por voz, speakable schema | Preparación AEO |
| **LLMO** | Profundidad semántica, autoridad hub-and-spoke, señales de confianza, frescura de contenido | Confianza |
| **Futuro** | Infraestructura preparada para agentes, OKF, UCP, AGENTS.md, DOM semántico | — |

## Características Principales

- **ROSTIDO-SCORE** — 6 dimensiones × 72 ítems, puntuación ponderada 0-100, 7 ítems de veto que limitan la puntuación total
- **Skill Contract & Handoff** — salida YAML estandarizada para encadenar flujos de auditoría → optimización → creación
- **Profundidad AEO** — 3 variantes de fragmento (párrafo 40-55 palabras, lista ≤9 ítems, tabla ≤4 columnas) + PAA + voz + speakable schema
- **Query Fan-Out Framework** — 30+ plantillas de consulta en 4 categorías, guía de mapeo paso a paso
- **Rastreador Mensual de Visibilidad de IA** — plantilla para rastrear citas en ChatGPT, Perplexity, Gemini, AI Overviews
- **Niveles de Prioridad** — P0 (ítems de veto) → P3 (continuo), mapeados a dimensiones de puntuación
- **8 Scripts Reales en Python** (1.623 líneas) — solo stdlib, listos para ejecutar: seguridad de cabeceras, robots.txt, CWV, schema, llms.txt, sitemap, informe HTML, rastreador de visibilidad de IA
- **22 Enlaces Oficiales de Referencia** — hrefs directos a la documentación de Google Search Central

## Requisitos

- **Python ≥ 3.7** — todos los scripts usan solo la biblioteca estándar (no necesita `pip install`)
- **Internet** — los scripts obtienen datos en vivo de URLs objetivo y APIs de Google
- **SO** — probado en Windows 10/11, debería funcionar en Linux/macOS

## Cómo Usar

### Inicio rápido: auditoría completa en 3 comandos

```bash
# 1. Clonar el repositorio
git clone https://github.com/mmriz16/seo-geo-aeo-skill.git
cd seo-geo-aeo-skill

# 2. Ejecutar todas las comprobaciones individuales
python3 scripts/check_security_headers.py https://example.com
python3 scripts/check_robots_txt.py https://example.com
python3 scripts/check_llms_files.py https://example.com
python3 scripts/check_schema.py https://example.com
python3 scripts/check_sitemap.py https://example.com
python3 scripts/check_core_web_vitals.py https://example.com

# 3. Generar informe HTML (agregar todos los resultados)
python3 scripts/generate_score_report.py https://example.com --output report.html --open
```

### Comprobación rápida de una consulta

```bash
# Solo cabeceras
python3 scripts/check_security_headers.py https://example.com

# Cabeceras como JSON (para tuberías con otras herramientas)
python3 scripts/check_security_headers.py https://example.com --json | jq .score

# Visibilidad de IA (interactivo)
python3 scripts/check_ai_visibility.py
```

### Como skill de agente CLI (Claude Code, Cursor, Codex, etc.)

```bash
# Copiar al directorio de skills de su agente
cp -r SKILL.md scripts/ ~/.agents/skills/seo-geo-aeo/
```

Luego en su agente:

```
"AUDIT https://example.com using ROSTIDO-SCORE — run all scripts and generate HTML report"
"Check GEO readiness for rostido.termicons.com"
"Create an AEO-optimized FAQ section with speakable schema"
"Map query fan-out for 'social media automation'"
```

### Como documento de referencia

Abra `SKILL.md` y navegue:

- **§1-2** → SEO Técnico + Entity SEO (fundamentos)
- **§3** → GEO: valor de citación, llms.txt, fan-out
- **§4** → AEO: fragmentos, PAA, voz, speakable
- **§5** → LLMO: profundidad semántica, señales de confianza
- **§6** → Rastreador de medición mensual
- **§8** → Marco ROSTIDO-SCORE (puntuación completa)
- **§9** → Skill contract & handoff protocol
- **§10** → Plantillas de query fan-out
- **§12** → Niveles de prioridad P0-P3
- **`scripts/`** → 8 scripts reales en Python

## Referencia de Scripts

| Script | Comprobaciones | Códigos de Salida | Salida |
|--------|---------------|:-----------------:|--------|
| `check_security_headers.py` | HSTS, CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy, HTTPS | 0=éxito, 1=fallo | Puntuación 0-100 + estado por cabecera |
| `check_robots_txt.py` | robots.txt existe, directiva Sitemap, reglas de crawler IA (10 bots) | 0=encontrado, 1=no encontrado | Puntuación 0-100 + permitir/bloquear por bot |
| `check_core_web_vitals.py` | LCP, INP, CLS, TTFB, FCP vía Google PageSpeed Insights | 0=ok, 1=error | Puntuación 0-100 + valores de métricas + oportunidades |
| `check_schema.py` | Todos los bloques JSON-LD, validación de 10 tipos de schema recomendados | 0=puntuación≥50, 1=<50 | Puntuación 0-100 + schemas encontrados + recomendaciones |
| `check_llms_files.py` | /llms.txt, /pricing.md, /AGENTS.md — estado HTTP + calidad de contenido | 0=puntuación≥50, 1=<50 | Puntuación 0-100 + estadísticas por archivo + vista previa |
| `check_sitemap.py` | Sitemap XML, soporte de índice anidado, cobertura lastmod | 0=encontrado, 1=no encontrado | Puntuación 0-100 + recuento de URL + URLs de ejemplo |
| `generate_score_report.py` | Agrega todas las comprobaciones → dashboard HTML ROSTIDO-SCORE | 0=ok, 1=error | Archivo HTML autónomo con gráficos + prioridades |
| `check_ai_visibility.py` | Seguimiento interactivo ChatGPT/Perplexity/Gemini/AI Overviews | 0=ok | JSON + guarda en ai_visibility_tracker.json |

### Banderas comunes (todos los scripts)

| Banderas | Efecto |
|----------|--------|
| `--json` | Salida JSON en lugar de formato legible |
| `-h` / `--help` | Mostrar ayuda |

### Flujo de auditoría completo

```bash
# Paso 1: Ejecutar todas las comprobaciones (guardar resultados JSON)
python3 scripts/check_security_headers.py https://example.com --json > /tmp/seo-headers.json
python3 scripts/check_robots_txt.py https://example.com --json > /tmp/seo-robots.json
python3 scripts/check_llms_files.py https://example.com --json > /tmp/seo-llms.json
python3 scripts/check_schema.py https://example.com --json > /tmp/seo-schema.json
python3 scripts/check_sitemap.py https://example.com --json > /tmp/seo-sitemap.json

# Paso 2: Generar informe
python3 scripts/generate_score_report.py https://example.com --output rostido-report.html
```

### Limitaciones

Estos scripts **NO** comprueban:
- Estructura de enlaces internos o enlaces rotos
- Profundidad de rastreo o páginas huérfanas
- Colocación de palabras clave, calidad del contenido o legibilidad
- Core Web Vitals **datos de campo** (usa datos de laboratorio de PSI — cercano pero no datos reales de CrUX)
- INP directamente (PSI lo proporciona como métrica experimental para algunos orígenes)
- Presencia en redes sociales, perfil de backlinks o análisis de menciones de marca
- Contenido renderizado por JS (solo obtiene HTML crudo)

Para esas comprobaciones, use herramientas especializadas como Screaming Frog, Ahrefs o Google Search Console.

## Sistema de Puntuación

**ROSTIDO-SCORE** evalúa 6 dimensiones:

| Dimensión | Peso | Máx | Ítems de Veto |
|-----------|:----:|:---:|:-------------:|
| **T** — Técnica | 20% | 120 | sitemap, canónicos, HTTPS |
| **C** — Contenido | 20% | 120 | — |
| **E** — Entidad | 15% | 120 | Schema Org |
| **G** — Preparación GEO | 20% | 120 | llms.txt |
| **A** — Preparación AEO | 15% | 120 | Schema FAQPage |
| **R** — Confianza | 10% | 120 | Validez del schema |

Cada ítem puntúa 0 (ausente), 5 (parcial) o 10 (completamente implementado). Los ítems de veto limitan la puntuación total a 50.

## Fuentes

- Google Search Central — Guía de Optimización de IA (2026)
- Investigación GEO de Princeton — KDD 2024
- Lumar — Guía de Estrategia GEO/AEO 2026
- HubSpot — Estado de AEO 2026
- Digital Applied — Guías de GEO, LLMO, Entity SEO
- schema.org — Documentación de Datos Estructurados
- llmstxt.org — Especificación LLMs.txt
- Ahrefs — Estudio de Menciones de Marca vs Backlinks (Dic 2025)
- Search Engine Land — Concepto de Entity Home (Jason Barnard / Kalicube)

## Claves de API y Límites de Velocidad

Algunos scripts llaman a APIs externas y se benefician de una clave de API gratuita para evitar límites de velocidad:

| Script | API | Límite (sin clave) | Límite (con clave) | Cómo Obtener Clave |
|--------|-----|:------------------:|:------------------:|--------------------|
| `check_core_web_vitals.py` | **Google PageSpeed Insights** | 240 consultas/día por IP | 25,000 consultas/día | [Google Cloud Console](https://console.cloud.google.com/apis/credentials) → Crear API Key → Habilitar PageSpeed Insights API → Establecer `PAGESPEED_API_KEY` variable de entorno |

### Configuración de Claves de API

```bash
# Opción 1: Variable de entorno (por sesión)
export PAGESPEED_API_KEY=AIzaSy...

# Opción 2: Archivo .env en la raíz del proyecto
echo "PAGESPEED_API_KEY=AIzaSy..." >> .env

# Opción 3: Pasar inline
PAGESPEED_API_KEY=AIzaSy... python3 scripts/check_core_web_vitals.py https://example.com
```

Todos los scripts funcionan correctamente sin claves de API — funcionarán pero pueden alcanzar límites de velocidad bajo uso intensivo.

## Licencia

Apache-2.0
