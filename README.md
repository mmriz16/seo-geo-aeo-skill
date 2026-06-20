# SEO, GEO, AEO & LLMO — Complete Optimization Framework

**v2.0.0** · 1,599 lines · 70KB

A comprehensive skill for **full-stack search visibility** — from crawlability and sitemaps to AI citation readiness and future agent-ready infrastructure. Covers all five overlapping discovery layers:

```
SEO ↔ Entity SEO ↔ GEO ↔ AEO ↔ LLMO
```

## What This Covers

| Layer | Focus | Score Dimension |
|-------|-------|:--------------:|
| **SEO** | Technical crawlability, on-page, content hubs, backlinks, E-E-A-T | Technical + Content |
| **Entity SEO** | Knowledge Graph, Wikidata QID, sameAs, Knowledge Panel | Entity |
| **GEO** | AI citation (ChatGPT, Perplexity, Gemini), llms.txt, pricing.md, query fan-out | GEO-readiness |
| **AEO** | Featured snippets (paragraph/list/table), PAA, voice search, speakable schema | AEO-readiness |
| **LLMO** | Semantic depth, hub-and-spoke authority, trust signals, content freshness | Trust |
| **Future** | Agent-ready infra, OKF, UCP, AGENTS.md, semantic DOM | — |

## Key Features

- **ROSTIDO-SCORE** — 6 dimensions × 72 items, weighted scoring 0-100, 7 veto items that cap overall score
- **Skill Contract & Handoff** — standardized YAML output for chaining audit → optimize → create workflows
- **AEO Depth** — 3 snippet variants (paragraph 40-55 words, list ≤9 items, table ≤4 cols) + PAA + voice + speakable schema
- **Query Fan-Out Framework** — 30+ query templates across 4 categories, step-by-step mapping guide
- **Monthly AI Visibility Tracker** — template for tracking citations across ChatGPT, Perplexity, Gemini, AI Overviews
- **Priority Tiers** — P0 (veto items) → P3 (ongoing), mapped to score dimensions
- **8 Real Python Scripts** (1,623 lines) — stdlib-only, ready to run: security headers, robots.txt, CWV, schema, llms.txt, sitemap, HTML report, AI visibility tracker
- **22 Official Reference Links** — direct hrefs to Google Search Central docs throughout

## How to Use

### As a CLI agent skill (Claude Code, Cursor, Codex, etc.)

```bash
# Copy to your agent's skills directory
cp SKILL.md ~/.agents/skills/seo-geo-aeo/
# Or add via skillfish
npx skillfish add mmriz16/seo-geo-aeo-skill seo-geo-aeo
```

Then in your agent:

```
"AUDIT https://example.com using ROSTIDO-SCORE"
"Check GEO readiness for rostido.termicons.com"
"Create an AEO-optimized FAQ section with speakable schema"
"Map query fan-out for 'social media automation'"
```

### As a reference document

Open `SKILL.md` and navigate:

- **§1-2** → Technical SEO + Entity SEO (foundation)
- **§3** → GEO: citation-worthiness, llms.txt, fan-out
- **§4** → AEO: snippets, PAA, voice, speakable
- **§5** → LLMO: semantic depth, trust signals
- **§6** → Monthly measurement tracker
- **§8** → ROSTIDO-SCORE framework (full scoring)
- **§9** → Skill contract & handoff protocol
- **§10** → Query fan-out templates
- **§12** → Priority tiers P0-P3
- **Appendix C** → Automation scripts (8 real Python scripts, 1,623 lines)
- **`scripts/`** → Ready-to-run Python scripts: `check_security_headers.py`, `check_robots_txt.py`, `check_core_web_vitals.py`, `check_schema.py`, `check_llms_files.py`, `check_sitemap.py`, `generate_score_report.py`, `check_ai_visibility.py`

## Scoring System

The **ROSTIDO-SCORE** evaluates 6 dimensions:

| Dimension | Weight | Max | Veto Items |
|-----------|:------:|:---:|:----------:|
| **T** — Technical | 20% | 120 | sitemap, canonicals, HTTPS |
| **C** — Content | 20% | 120 | — |
| **E** — Entity | 15% | 120 | Org schema |
| **G** — GEO-readiness | 20% | 120 | llms.txt |
| **A** — AEO-readiness | 15% | 120 | FAQPage schema |
| **R** — Trust | 10% | 120 | Schema validity |

Each item scores 0 (missing), 5 (partial), or 10 (fully implemented). Veto items cap overall at 50.

## Sources

- Google Search Central — AI Optimization Guide (2026)
- Princeton GEO Research — KDD 2024
- Lumar — GEO/AEO Strategy Guide 2026
- HubSpot — State of AEO 2026
- Digital Applied — GEO, LLMO, Entity SEO Guides
- schema.org — Structured Data Documentation
- llmstxt.org — LLMs.txt Specification
- Ahrefs — Brand Mentions vs Backlinks Study (Dec 2025)
- Search Engine Land — Entity Home concept (Jason Barnard / Kalicube)

## API Keys & Rate Limits

Some scripts call external APIs and benefit from a free API key to avoid rate limits:

| Script | API | Rate Limit (no key) | Rate Limit (with key) | How to Get Key |
|--------|-----|:-------------------:|:---------------------:|----------------|
| `check_core_web_vitals.py` | **Google PageSpeed Insights** | 240 queries/day per IP | 25,000 queries/day | [Google Cloud Console](https://console.cloud.google.com/apis/credentials) → Create API Key → Enable PageSpeed Insights API → Set `PAGESPEED_API_KEY` env var |

### Setting API Keys

```bash
# Option 1: Environment variable (per session)
export PAGESPEED_API_KEY=AIzaSy...

# Option 2: .env file in project root
echo "PAGESPEED_API_KEY=AIzaSy..." >> .env

# Option 3: Pass inline
PAGESPEED_API_KEY=AIzaSy... python3 scripts/check_core_web_vitals.py https://example.com
```

All scripts fall back gracefully without API keys — they'll work but may hit rate limits under heavy use.

## License

Apache-2.0
