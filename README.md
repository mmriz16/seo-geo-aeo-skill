# SEO, GEO, AEO & LLMO — Complete Optimization Framework

**v2.0.0** · 1,599 lines · 70KB

**Python ≥ 3.7** required for scripts. No pip packages needed — all scripts use stdlib only.

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

## Requirements

- **Python ≥ 3.7** — all scripts use stdlib only (zero `pip install` needed)
- **Internet** — scripts fetch live data from target URLs and Google APIs
- **OS** — tested on Windows 10/11, should work on Linux/macOS

## How to Use

### Quick start: full audit in 3 commands

```bash
# 1. Clone atau download repo
git clone https://github.com/mmriz16/seo-geo-aeo-skill.git
cd seo-geo-aeo-skill

# 2. Jalanin semua check individual
python3 scripts/check_security_headers.py https://example.com
python3 scripts/check_robots_txt.py https://example.com
python3 scripts/check_llms_files.py https://example.com
python3 scripts/check_schema.py https://example.com
python3 scripts/check_sitemap.py https://example.com
python3 scripts/check_core_web_vitals.py https://example.com

# 3. Generate HTML report (aggregate semua hasil)
python3 scripts/generate_score_report.py https://example.com --output report.html --open
```

### Fast single-query check

```bash
# Headers only
python3 scripts/check_security_headers.py https://example.com

# Headers as JSON (for piping into other tools)
python3 scripts/check_security_headers.py https://example.com --json | jq .score

# AI visibility (interactive)
python3 scripts/check_ai_visibility.py
```

### As a CLI agent skill (Claude Code, Cursor, Codex, etc.)

```bash
# Copy to your agent's skills directory
cp -r SKILL.md scripts/ ~/.agents/skills/seo-geo-aeo/
```

Then in your agent:

```
"AUDIT https://example.com using ROSTIDO-SCORE — run all scripts and generate HTML report"
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
- **`scripts/`** → 8 real Python scripts

## Scripts Reference

| Script | Checks | Exit Codes | Output |
|--------|--------|:----------:|--------|
| `check_security_headers.py` | HSTS, CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy, HTTPS | 0=pass, 1=fail | Score 0-100 + per-header status |
| `check_robots_txt.py` | robots.txt exists, Sitemap directive, AI crawler rules (10 bots) | 0=found, 1=not found | Score 0-100 + per-bot allow/block |
| `check_core_web_vitals.py` | LCP, INP, CLS, TTFB, FCP via Google PageSpeed Insights | 0=ok, 1=error | Score 0-100 + metric values + opportunities |
| `check_schema.py` | All JSON-LD blocks, 10 recommended schema types validation | 0=score≥50, 1=<50 | Score 0-100 + found schemas + recommendations |
| `check_llms_files.py` | /llms.txt, /pricing.md, /AGENTS.md — HTTP status + content quality | 0=score≥50, 1=<50 | Score 0-100 + per-file stats + preview |
| `check_sitemap.py` | Sitemap XML, nested index support, lastmod coverage | 0=found, 1=not found | Score 0-100 + URL count + sample URLs |
| `generate_score_report.py` | Aggregates all checks → ROSTIDO-SCORE HTML dashboard | 0=ok, 1=error | Self-contained HTML file with bar charts + priorities |
| `check_ai_visibility.py` | Interactive ChatGPT/Perplexity/Gemini/AI Overviews tracking | 0=ok | JSON + save to ai_visibility_tracker.json |

### Common flags (all scripts)

| Flag | Effect |
|------|--------|
| `--json` | Output JSON instead of human-readable format |
| `-h` / `--help` | Show usage |

### Full audit workflow

```bash
# Step 1: Run all checks (save JSON results)
python3 scripts/check_security_headers.py https://example.com --json > /tmp/seo-headers.json
python3 scripts/check_robots_txt.py https://example.com --json > /tmp/seo-robots.json
python3 scripts/check_llms_files.py https://example.com --json > /tmp/seo-llms.json
python3 scripts/check_schema.py https://example.com --json > /tmp/seo-schema.json
python3 scripts/check_sitemap.py https://example.com --json > /tmp/seo-sitemap.json

# Step 2: Generate report
echo '{"url":"https://example.com","checks":{' > /tmp/seo-all.json
# Combine results manually or use the all-in-one:
python3 scripts/generate_score_report.py https://example.com --output rostido-report.html
```

### Limitations

These scripts **do NOT** check:
- Internal link structure or broken links
- Crawl depth or orphan pages
- Keyword placement, content quality, or readability
- Core Web Vitals **field data** (uses lab data from PSI — close but not CrUX real-user data)
- INP directly (PSI provides it as experimental metric for some origins)
- Social media presence, backlink profile, or brand mention analysis
- JS-rendered content (fetches raw HTML only)

For those checks, use dedicated tools like Screaming Frog, Ahrefs, or Google Search Console.

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
