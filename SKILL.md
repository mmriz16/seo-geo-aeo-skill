---
name: seo-geo-aeo-complete
description: "Comprehensive SEO, GEO, AEO, and LLMO optimization — make any website rank in traditional search, get cited by AI engines, appear in answer boxes, and stay visible in the AI-search era. Use when the user asks about SEO, search optimization, AI search, generative engine optimization, answer engine optimization, LLM optimization, getting cited by ChatGPT/Perplexity/Claude/Gemini, AI Overviews, AI Mode, Knowledge Graph, entity SEO, llms.txt, or any combination of these. Also use when auditing or building a website that needs to be future-proof across all discovery channels."
metadata:
  version: 2.0.0
  sources:
    - Google Search Central — AI Optimization Guide (2026)
    - Google Search Central — Search Essentials
    - Princeton GEO Research — KDD 2024
    - Lumar — GEO/AEO Strategy Guide 2026
    - HubSpot — State of AEO 2026
    - Digital Applied — GEO, LLMO, Entity SEO Guides
    - Evergreen Media — LLMO Guide 2025-2026
    - Frase.io — Entity Optimization for GEO
    - Chapters EG — Technical SEO Checklist 2026
    - Onely — AI Overview Citation Analysis
    - Search Engine Land — Entity Home Concept (Jason Barnard / Kalicube)
    - Ahrefs — Brand Mentions vs Backlinks Study (Dec 2025)
    - schema.org — Structured Data Documentation
    - llmstxt.org — LLMs.txt Specification
    - Google Developers — Speakable Schema
    - Google Developers — Rich Results (FAQ, HowTo, Product)
    - Google Search Central — Robots.txt & AI Crawlers
    - Google Search Central — Core Web Vitals
    - Google Search Central — JavaScript SEO
    - Barry Schwartz — SEO & AI Overviews Research
tags:
  - seo
  - geo
  - aeo
  - llmo
  - entity-seo
  - generative-engine-optimization
  - answer-engine-optimization
  - ai-search
  - ai-overviews
  - knowledge-graph
  - search-optimization
  - technical-seo
  - content-strategy
---

# SEO, GEO, AEO & LLMO — Complete Optimization Framework v2.0.0

You are an expert in **full-stack search visibility**. You understand that in 2026, a website must be optimized for five overlapping but distinct discovery layers:

1. **SEO** — Traditional search engines (Google, Bing) — crawl, index, rank
2. **Entity SEO** — Knowledge Graph, Wikidata, brand identity — the foundation of **what you are**
3. **GEO** — Generative AI engines (ChatGPT, Perplexity, Claude, Gemini) — be cited as a source
4. **AEO** — Answer engines (featured snippets, AI Overviews, voice assistants) — be extracted as the answer
5. **LLMO** — Large Language Model authority (RAG-based citation, semantic trust) — be recommended

These layers build on each other like a pyramid:

```
        ┌──────────────────────────────────────┐
        │      AGENT-READY INFRASTRUCTURE       │
        │  OKF, UCP, AGENTS.md, semantic DOM    │
        ├──────────────────────────────────────┤
        │        LLMO — LLM AUTHORITY           │
        │     semantic depth, trust signals,    │
        │     thematic authority, freshness     │
        ├──────────────────────────────────────┤
        │     AEO — ANSWER READY STRUCTURE       │
        │  featured snippets, PAA, speakable,   │
        │  FAQ schema, 40-55 word blocks, tables│
        ├──────────────────────────────────────┤
        │    GEO — CITATION-WORTHINESS          │
        │  sources, statistics, quotes,         │
        │  llms.txt, pricing.md, fan-out        │
        ├──────────────────────────────────────┤
        │   ENTITY SEO — KNOWLEDGE GRAPH        │
        │  Wikidata QID, sameAs, Knowledge      │
        │  Panel, entity home, KG consistency   │
        ├──────────────────────────────────────┤
        │  CORE SEO — TECHNICAL + CONTENT       │
        │  crawl, index, speed, sitemap,        │
        │  canonicals, schema, backlinks, EEAT  │
        └──────────────────────────────────────┘
```

## How This Skill Works

This skill follows a **structured audit and improvement protocol**:

1. **Scoring** — Every audit produces a ROSTIDO-SCORE (0-100 across 6 dimensions) with veto checks
2. **Handoff** — Every job outputs a standardized handoff summary for chaining to other tasks
3. **Priority** — Fixes are ordered P0→P3 by impact and effort
4. **Measurement** — Every change is tracked monthly using the AI Visibility Tracker

---

# PART 1: TRADITIONAL SEO

> **Official reference**: [Google Search Central — Search Essentials](https://developers.google.com/search/docs/fundamentals/seo-starter-guide), [Google Search Central — SEO Documentation](https://developers.google.com/search/docs)

## 1.1 Technical SEO — The Foundation

If search engines can't crawl, index, or render your content, nothing else matters.

### Crawlability & Indexing

| # | Check | Implementation |
|---|-------|----------------|
| 1 | **robots.txt** | Allow important sections (`/blog/`, `/products/`). Disallow only admin, internal search, staging. Include `Sitemap:` directive. Add AI bot rules (see §3.5). |
| 2 | **XML Sitemap** | Include only 200-status, indexable URLs. No redirects, 404s, or noindex. Auto-update on publish. Submit in Google Search Console. Break into multiple sitemaps for 10K+ URLs. |
| 3 | **Canonical tags** | Every page needs `<link rel="canonical" href="...">`. Prevent duplicate content across URL variants. |
| 4 | **meta robots** | Use `noindex` sparingly. Never block important pages. |
| 5 | **Crawl budget** | Prioritize high-value pages in sitemap. Fix redirect chains. Remove thin/low-value pages from index. |
| 6 | **JavaScript SEO** | Ensure critical content renders without JS. Use SSR/SSG over CSR for SEO-critical pages. Test with Google's `?debug_jsa=1` or URL Inspection Tool. |
| 7 | **Log file analysis** | Monitor actual Googlebot crawl patterns. Identify crawl waste and blocked resources. |

> **Reference**: [Google — JS SEO Basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)

### Core Web Vitals & Performance

| Metric | Target | How |
|--------|--------|-----|
| **LCP** (Largest Contentful Paint) | ≤ 2.5s | Optimize images, preload key resources, use CDN, eliminate render-blocking resources |
| **INP** (Interaction to Next Paint) | ≤ 200ms | Code splitting, lazy load non-critical JS, avoid long tasks |
| **CLS** (Cumulative Layout Shift) | ≤ 0.1 | Set explicit dimensions on images/ads, avoid late-loading content shifts |
| **TTFB** (Time to First Byte) | ≤ 800ms | Use CDN, optimize server, edge caching |

> **Reference**: [Google — Core Web Vitals](https://web.dev/articles/vitals), [Google — PageSpeed Insights](https://pagespeed.web.dev/)

### Mobile & UX

- Mobile-first indexing is default — test all pages on mobile viewport
- Touch targets ≥ 48px
- No intrusive interstitials
- Font sizes readable without zoom

> **Reference**: [Google — Mobile-First Indexing](https://developers.google.com/search/docs/crawling-indexing/mobile-first-indexing)

### Security & Trust Signals (Technical E-E-A-T)

| Signal | Implementation |
|--------|----------------|
| **HTTPS** | TLS 1.2+ with valid cert. Redirect HTTP → HTTPS. |
| **HSTS** | `Strict-Transport-Security` header |
| **CSP** | Content-Security-Policy to prevent XSS |
| **X-Frame-Options** | `DENY` or `SAMEORIGIN` to prevent clickjacking |
| **X-Content-Type-Options** | `nosniff` |
| **Referrer-Policy** | Control referrer info leakage |
| **Clean footer** | Privacy policy, terms of service, contact info, physical address |

## 1.2 On-Page SEO

| Element | Best Practice |
|---------|---------------|
| **Title tag** | Unique per page, 50-60 chars, primary keyword near front, brand at end |
| **Meta description** | Unique, 150-160 chars, includes keyword + CTA, induces click |
| **H1** | One per page, matches search intent, includes primary keyword |
| **H2/H3** | Logical hierarchy, covers subtopics, includes secondary keywords naturally |
| **URL structure** | Short, descriptive, hyphen-separated, e.g. `/seo-tips-2026` not `/page123?cat=5` |
| **Image alt text** | Descriptive, includes keyword where natural, every `<img>` needs `alt` |
| **Internal linking** | Link to related content, use descriptive anchor text, distribute link equity |
| **Content length** | Match search intent — some queries need 300 words, some need 3,000 |
| **Keyword placement** | In H1, first paragraph, at least one H2, naturally throughout body |

## 1.3 Content SEO — Topical Authority

In 2026, Google's AI systems understand **topical clusters, not individual keywords**. Single-page-per-keyword is dead.

### Hub-and-Spoke Architecture

```
Hub: "Social Media Management 2026" (pillar, 3K-5K words)
├── Spoke: "Best Tools for Scheduling Posts"
├── Spoke: "How to Auto-Reply Comments on Instagram"
├── Spoke: "Instagram vs TikTok for Business"
├── Spoke: "Social Media Analytics Guide"
└── Spoke: "AI-Powered Social Media Automation"
```

- **Hub**: Comprehensive overview of main topic, targets primary keyword cluster, links to all spokes
- **Spoke**: Deep dive into subtopic, links back to hub and related spokes, targets long-tail keywords

### Topical Cluster Strategy

1. Pick a core topic relevant to your business
2. Map the semantic field — related entities, concepts, questions, attributes
3. Create hub page with comprehensive coverage
4. Create spoke pages for each subtopic
5. Interlink hub ↔ spokes, spokes ↔ related spokes
6. Update regularly

### Content Freshness

- Display "Last updated: [date]" prominently on every content page
- Refresh content every 3-6 months minimum
- Update statistics, examples, screenshots
- Add new sections for emerging subtopics
- Remove or update outdated claims

## 1.4 Off-Page SEO & E-E-A-T

### Backlinks

- Quality over quantity — one link from a high-authority domain > 100 from low-quality
- Earn links through: original research, expert quotes, guest posts, digital PR, resource pages
- Avoid: PBNs, paid links, spammy directories, link exchanges at scale
- Monitor: toxic backlinks and disavow when necessary

### E-E-A-T Signals

| Signal | Implementation |
|--------|----------------|
| **Experience** | First-hand experience demonstrated (reviews, case studies, tutorials with real examples) |
| **Expertise** | Author bios with credentials, publication history, professional recognition |
| **Authoritativeness** | Cited by other authoritative sources, industry recognition, awards |
| **Trustworthiness** | Transparent sourcing, accurate claims, clear distinction fact vs opinion, secure site, clear policies |

> **Reference**: [Google — E-E-A-T Explained](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)

### Brand Mentions

- Brand mentions correlate with AI visibility **3x stronger than backlinks** (0.664 vs 0.218) — Ahrefs Dec 2025 study
- Get mentioned on: Wikipedia, industry publications, review sites (G2, Capterra), Reddit, Quora
- Ensure consistent NAP (Name, Address, Phone) across all platforms

---

# PART 2: ENTITY SEO & KNOWLEDGE GRAPH

Google's Knowledge Graph now holds **500 billion+ facts on 5 billion+ entities**. Gemini AI is trained on it. If your brand isn't in the Knowledge Graph, you're invisible to AI Overviews and AI Mode.

> **Reference**: [Search Engine Land — Entity Home Guide](https://searchengineland.com/google-knowledge-panel-entity-home-443429), [schema.org/Organization](https://schema.org/Organization)

## 2.1 Entity Home Page

This is the single URL that anchors your brand identity for algorithms. Usually your **About page**.

### Requirements

```
- Carry Organization JSON-LD with @id pointing to canonical domain
- Include sameAs declarations linking to all authoritative profiles
- State unambiguously: who, what, when founded, where operates, who leads
- Content must be factually consistent with all external sources
```

### JSON-LD Example

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://rostido.termicons.com/#organization",
  "name": "Rostido",
  "url": "https://rostido.termicons.com",
  "description": "Automate comments, schedule posts, filter spam, and send DMs across Instagram, TikTok, YouTube, Facebook, LinkedIn, and more.",
  "foundingDate": "2025",
  "sameAs": [
    "https://wikidata.org/wiki/Q...",
    "https://www.linkedin.com/company/...",
    "https://twitter.com/...",
    "https://github.com/..."
  ]
}
```

## 2.2 Wikidata Entry

**Unlike Wikipedia, Wikidata has no notability requirement** — any legitimate business can create an entry. Each entity gets a unique QID.

### Steps

1. Create account at wikidata.org
2. Create item for your brand/company
3. Add properties: official website (P856), inception (P571), country (P17), social media links (P553, P554)
4. Link to Wikipedia if exists
5. Add your QID to your page's JSON-LD via `sameAs` or `identifier` property

> **Reference**: [Wikidata — Create Item](https://www.wikidata.org/wiki/Special:NewItem)

## 2.3 Knowledge Panel

- Claim your Knowledge Panel via Google's Knowledge Panel claiming tool
- If Wikipedia doesn't exist, Google may pull description from your About page (entity home)
- Ensure data consistency: your website, Wikidata, Wikipedia, Crunchbase, LinkedIn must all agree
- If your Knowledge Panel shows wrong info, fix the authoritative source (usually Wikipedia or Wikidata), not your website — Google pulls panels from external sources

> **Reference**: [Google — Knowledge Panel Claiming](https://support.google.com/websearch/answer/10778271)

## 2.4 sameAs Schema

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "sameAs": [
    "https://www.wikidata.org/wiki/Q123456",
    "https://www.linkedin.com/company/...",
    "https://twitter.com/...",
    "https://www.crunchbase.com/organization/...",
    "https://github.com/..."
  ]
}
```

---

# PART 3: GEO — GENERATIVE ENGINE OPTIMIZATION

**Goal**: Get cited as a source when ChatGPT, Perplexity, Gemini, or Claude generate answers.

## 3.1 The Princeton Research (KDD 2024)

Ranked effectiveness of 9 optimization methods:

| Method | Visibility Boost | How |
|--------|:---------------:|-----|
| **Cite authoritative sources** | **+40%** | Link to academic research, official docs, recognized publications |
| **Add statistics with sources** | **+37%** | Specific numbers + source + date |
| **Include expert quotations** | **+30%** | "According to [Expert], [Title]: ..." |
| **Use technical terms** | +28% | Domain-specific terminology, properly used |
| **Authoritative tone** | +25% | Demonstrated expertise, confident voice |
| **Fluency optimization** | +15-30% | Readability, flow, sentence variety |
| **Clarity improvements** | +20% | Simplify complex concepts |
| **Unique vocabulary** | +15% | Word diversity, avoid repetition |
| ❌ **Keyword stuffing** | **-10%** | **Actively hurts AI visibility** |

**Best combination**: Fluency + Statistics = maximum boost. Low-ranking sites benefit up to 115% increase with citations.

> **Reference**: [KDD 2024 — Princeton GEO Paper](https://dl.acm.org/doi/10.1145/3637528.3671579), [Digital Applied GEO Guide](https://www.digitalapplied.com/blog/geo-guide-generative-engine-optimization-2026)

## 3.2 Platform-Specific Behavior

| Platform | Citations/Answer | Source Preference | AI Search Method |
|----------|:----------------:|-------------------|------------------|
| **ChatGPT** | ~2.6 | Authoritative, recent, structured | Bing search + own training data |
| **Perplexity** | ~6.6 | Recent + authoritative, shows links | Real-time web search |
| **Google Gemini** | ~6.1 | Knowledge Graph + Google index | Trained on KG + Search index |
| **Google AI Overviews** | Varies | Traditional ranking first, then extract | Core Search ranking + AI |
| **Claude (Brave)** | Varies | Brave Search, well-structured, factual | Brave Search API |
| **Copilot** | Varies | Bing index, authoritative, recent | Bing + OpenAI |
| **Meta AI** | Low | Limited citation, Facebook data | In-house |

**Key insight**: ChatGPT cites only ~2.6 sources per answer — competition is fierce. Perplexity cites ~6.6 — more opportunities. **Only 11% of domains** are cited by both ChatGPT and AI Overviews for the same query — platform-specific optimization is essential.

## 3.3 Content Structure for AI Extractability

### Answer Blocks (40-60 words)

AI systems extract passages, not pages. Every key claim should work as a standalone statement.

```
✅ GOOD:
"Rostido is a social media management platform that automates comment replies, 
post scheduling, spam filtering, and direct messages across Instagram, TikTok, 
YouTube, Facebook, LinkedIn, X, and Threads — all from one dashboard."

❌ BAD:
"Welcome to our blog! Today we're going to talk about social media management 
and how it can help your business. First, let's start with some background..."
```

### Content Block Templates

**Definition block** (for "What is X?" queries):
> [Term] is a [category] that [core function]. Unlike [alternative], it [key differentiator]. Used by [audience] for [primary use case].

**Comparison block** (for "X vs Y" queries):
> | Feature | [Product A] | [Product B] |
> |---------|:-----------:|:-----------:|
> | Price | $29/mo | $49/mo |
> | Platforms | 7 | 3 |
> | AI replies | Yes | No |

**Statistic block** (for data-driven queries):
> According to [Source] ([date]), [statistic]. This represents a [change] from [previous period], indicating [implication].

**Step block** (for "How to X" queries):
> 1. First, [action]
> 2. Then, [next action]
> 3. Finally, [final action]

## 3.4 Machine-Readable Files

### `/llms.txt`

Context file for AI systems. Follows llmstxt.org spec:

```markdown
# Rostido

> Automate comments, schedule posts, filter spam, and send DMs across Instagram, 
> TikTok, YouTube, Facebook, LinkedIn, X, and Threads — all from one dashboard.

## Key Pages
- [Features](https://rostido.termicons.com/#features)
- [Pricing](https://rostido.termicons.com/#pricing)
- [Login](https://rostido.termicons.com/login)
- [Register](https://rostido.termicons.com/register)

## About
Rostido is a social media automation platform launched in 2025...
```

> **Reference**: [llmstxt.org](https://llmstxt.org/)

### `/pricing.md`

Structured pricing for AI agents (who now evaluate products programmatically):

```markdown
# Pricing — Rostido

## Free
- Price: $0/month
- Limits: 2 social platforms, 10 scheduled posts/month
- Features: Comment inbox (read-only), content calendar, basic analytics (7d)

## Creator
- Price: $9/month (billed monthly)
- Limits: 5 social platforms, 100 scheduled posts/month
- Features: AI auto-reply (basic), comment reply + DM, AI caption writer, analytics (30d)
```

### `/AGENTS.md`

Capability description for autonomous agents:

```markdown
# Agent Capabilities — Rostido

## What we do
Rostido automates social media management: auto-reply comments, schedule posts, 
filter spam, and send DMs across multiple platforms.

## How agents can use this site
- Browse /pricing.md for structured pricing
- Visit /docs for API documentation
- Use /llms.txt for a quick overview
```

## 3.5 robots.txt — AI Bot Configuration

Don't block citation-enabled bots. Block only training-only crawlers if needed:

```
User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: CCBot
Disallow: /    # Block Common Crawl (training only, no citation)
```

> **Reference**: [Google — AI Crawlers in robots.txt](https://developers.google.com/search/docs/crawling-indexing/blocking-ai-crawlers)

## 3.6 Query Fan-Out Framework

This section defines the **Query Fan-Out** — the set of all possible query variations around a topic that users and AI engines might generate. Covering fan-out variants is the #1 content gap that prevents AI citation.

### Fan-Out Patterns

Every topic generates queries across these patterns:

| Pattern | Example | Content Recommendation |
|---------|---------|----------------------|
| **What is X?** | "What is social media automation?" | Definition block (see §3.3) |
| **How to X?** | "How to automate Instagram comments" | Step-by-step guide + HowTo schema |
| **Best X?** | "Best social media tools 2026" | Comparison page with table |
| **X vs Y?** | "Rostido vs Hootsuite" | Comparison block with pros/cons |
| **X pricing?** | "Rostido pricing plans" | Pricing page + pricing.md |
| **X alternatives?** | "Rostido alternatives" | Alternatives/comparison page |
| **X for Y?** | "Social media automation for small business" | Use-case specific page |
| **X review?** | "Rostido review 2026" | Review/testimonial page |
| **Is X worth it?** | "Is Rostido worth it?" | Value proposition + ROI data |
| **X features?** | "What features does Rostido have" | Features section with structured list |
| **X vs Y vs Z?** | "Buffer vs Hootsuite vs Rostido" | Multi-way comparison |
| **Why X?** | "Why use social media automation" | Benefits/ROI page |
| **X for beginners?** | "Social media automation for beginners" | Beginner-friendly guide |
| **Does X support Y?** | "Does Rostido support TikTok?" | Platform-specific page |
| **X API?** | "Rostido API documentation" | Developer docs page |

### How to Map Fan-Out for Any Topic

```
1. Identify the core entity/topic
2. Generate all 15+ pattern variants
3. Check which variants your site already covers
4. Prioritize missing variants by search volume + AI citation potential
5. Create content for uncovered variants
6. Track new variant coverage monthly
```

---

# PART 4: AEO — ANSWER ENGINE OPTIMIZATION

**Goal**: Get cited as a direct answer in featured snippets, AI Overviews, voice assistants, and PAA (People Also Ask) boxes.

## 4.1 The AEO Mindset

AEO is **not** about ranking. It's about being **extracted as a direct answer**.

| SEO | AEO |
|-----|-----|
| "Write a comprehensive guide" | "Write a concise answer first, then elaborate" |
| Keywords in title | Question in title |
| 2,000+ word depth | 40-55 word answer blocks |
| Click-through is success | Citation/extraction is success |
| Optimize for Google bot | Optimize for AI extraction |
| Competitor keywords | User questions and intent |
| Content volume | Answer precision |

## 4.2 Featured Snippet Optimization

Featured snippets have 3 variants: **Paragraph**, **List**, and **Table**. Each has specific structural requirements.

### 4.2.1 Paragraph Snippet (most common)

Use for: informational queries, definitions, fact-based questions.

**Requirements:**
- Direct answer in **first 40-55 words** of the first paragraph after a relevant H2 or H3
- Answer starts with the keyword or variant: "X is...", "X refers to...", "To do X..."
- No jargon in the first answer sentence — plain language
- Supporting context paragraph follows (2-4 sentences)
- Avoid: "Great question!", "In this article we will...", "Let's dive in"

```
✅ H2: What is social media automation?
Social media automation is the use of software tools to schedule posts, 
auto-reply comments, filter spam, and manage direct messages across 
multiple platforms from a single dashboard.

This eliminates repetitive manual tasks, letting teams focus on strategy 
and engagement instead of day-to-day posting logistics.
```

### 4.2.2 List Snippet

Use for: procedures, rankings, comparisons, features, steps.

**Requirements:**
- Use `<ol>` (ordered) or `<ul>` (unordered) immediately after the H2/H3
- **5-9 list items** — more than 9 triggers truncation
- Each item ≤ 15 words for clean display
- H2/H3 must be phrased as the **actual question** users search

```html
<h2>How to automate Instagram comments in 3 steps</h2>
<ol>
  <li>Connect your Instagram Business account to Rostido via OAuth</li>
  <li>Set auto-reply rules (keyword-based or AI-powered)</li>
  <li>Monitor and refine responses from the dashboard</li>
</ol>
```

### 4.2.3 Table Snippet

Use for: comparisons, pricing, specifications, feature matrices.

**Requirements:**
- Use `<table>` with `<th>` header row
- **≤ 4 columns** (wider tables are truncated in snippets)
- Use `<thead>` and `<tbody>` for proper structure
- First column is the primary entity (product, plan, feature)
- Include schema-aware column labeling

```html
<table>
  <thead>
    <tr>
      <th>Feature</th>
      <th>Rostido Free</th>
      <th>Rostido Creator</th>
      <th>Rostido Business</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Platforms</td><td>2</td><td>5</td><td>7</td></tr>
    <tr><td>Scheduled posts/mo</td><td>10</td><td>100</td><td>Unlimited</td></tr>
    <tr><td>AI auto-reply</td><td>Read-only</td><td>Basic</td><td>Advanced</td></tr>
  </tbody>
</table>
```

## 4.3 People Also Ask (PAA) Optimization

PAA questions are selected by Google based on **semantic relatedness** to the primary query. Owning multiple PAA entries significantly increases SERP real estate.

### Requirements

| # | Element | Detail |
|---|---------|--------|
| 1 | **Discover PAA questions** | Search your primary keyword, scrape the PAA box, identify top 5-8 questions |
| 2 | **H2/H3 as exact questions** | Each PAA question gets its own heading phrased **exactly** as users ask |
| 3 | **Direct answer below each** | 30-50 word answer paragraph immediately under the question heading |
| 4 | **Plain language first** | Answer starts with the answer, not context. "Rostido supports..." not "When it comes to platforms..." |
| 5 | **No filler** | No "Great question!", "In this article we will..." — Google penalizes these for PAA |
| 6 | **FAQPage schema** | Only for qualified sites. Otherwise use `speakable` schema instead. |

### PAA Content Structure

```html
<h2>What platforms does Rostido support?</h2>
<p>Rostido supports Instagram, TikTok, YouTube, Facebook, LinkedIn, 
X (Twitter), and Threads — all manageable from a single dashboard.</p>

<h2>How much does Rostido cost?</h2>
<p>Rostido offers a Free plan at $0/month, Creator at $9/month, and 
Business at $29/month. Each tier adds more platforms and features.</p>
```

### PAA Question Clusters

PAA questions naturally cluster. If you answer one, Google may add related questions. Map these clusters:

```
Social Media Automation
├── What is social media automation?
├── How does social media automation work?
├── Best social media automation tools?
│   ├── What is Rostido?
│   ├── How much does Rostido cost?
│   └── Does Rostido support Instagram?
├── Social media automation vs manual posting?
└── Is social media automation worth it?
```

## 4.4 Voice Search Optimization

Voice assistants (Google Assistant, Siri, Alexa, Cortana) pull answers from featured snippets and Knowledge Graph.

### Requirements

| Requirement | Why |
|-------------|-----|
| **TTFB < 2s** | Voice assistants timeout fast — slow pages lose answers |
| **HTTPS required** | Siri and Alexa refuse to read non-HTTPS content |
| **Conversational answers** | Voice answers should read naturally aloud: "Rostido is a social media management platform..." |
| **Direct answer in first paragraph** | Voice reads top content first |
| **`speakable` schema** | Marks sections as suitable for text-to-speech (see §4.5) |

### Platform-Specific Voice

| Assistant | Source | Optimization Focus |
|-----------|--------|-------------------|
| **Google Assistant** | Featured snippets + Knowledge Graph | Snippet ownership + speakable schema |
| **Siri** | Knowledge Graph + Bing | Entity SEO + Knowledge Panel |
| **Alexa** | Bing + external sources | Entity signals + content freshness |
| **Cortana** | Bing | Bing Webmaster Tools + indexing |

> **Reference**: [Google — speakable Schema](https://developers.google.com/search/docs/appearance/structured-data/speakable), [Bing — Voice Search](https://www.bing.com/webmasters/help/webmasters-voice-search-6937dbe0)

## 4.5 speakable Schema

Marks specific sections of a page as optimal for text-to-speech. Voice assistants and Google Assistant use this to determine what to read aloud.

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "What Is Social Media Automation?",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [".article-summary", ".definition-block"]
  }
}
```

Implementation notes:
- Target 1-2 sections per page (voice doesn't read the entire article)
- Keep speakable sections between 40-80 words
- Use class names that match your CSS selectors
- Multiple `cssSelector` values are OR'd — any matching section is speakable

## 4.6 FAQ Section with Schema

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What platforms does Rostido support?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Rostido supports Instagram, TikTok, YouTube, Facebook, LinkedIn, X (Twitter), and Threads — all from one dashboard."
    }
  }]
}
```

**Critical**: FAQ content must be visible in the HTML, not hidden behind JS click-to-expand. Use CSS `hidden` or `details`/`summary` for progressive disclosure, but keep it in the initial DOM.

> **Reference**: [Google — FAQ Schema Guidelines](https://developers.google.com/search/docs/appearance/structured-data/faqpage)

## 4.7 HowTo Schema

For step-by-step process content:

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Automate Instagram Comments",
  "step": [
    {
      "@type": "HowToStep",
      "position": 1,
      "name": "Connect",
      "text": "Connect your Instagram Business account to Rostido via OAuth.",
      "image": "https://rostido.termicons.com/img/connect.jpg"
    },
    {
      "@type": "HowToStep",
      "position": 2,
      "name": "Set Rules",
      "text": "Configure auto-reply rules: keyword triggers or AI-powered responses.",
      "image": "https://rostido.termicons.com/img/rules.jpg"
    }
  ],
  "totalTime": "PT5M",
  "tool": [
    {
      "@type": "HowToTool",
      "name": "Rostido account"
    }
  ]
}
```

> **Reference**: [Google — HowTo Schema](https://developers.google.com/search/docs/appearance/structured-data/how-to)

## 4.8 AEO Full Checklist

- [ ] Direct answer in first 40-55 words after H2/H3 for every key section
- [ ] Paragraph snippet structure: answer starts with keyword variant
- [ ] List snippet structure: ≤9 items, ≤15 words per item, `<ol>`/`<ul>` right after heading
- [ ] Table snippet structure: ≤4 columns, `<thead>` + `<tbody>`, first column = primary entity
- [ ] PAA: H2/H3 phrased as exact user questions, 30-50 word answers below each
- [ ] FAQPage JSON-LD with visible HTML content
- [ ] speakable schema on key definition sections
- [ ] HowTo schema for process/tutorial content
- [ ] Voice-readiness: TTFB < 2s, HTTPS, conversational answers
- [ ] Voice test: read first answer paragraph aloud — does it sound natural?
- [ ] Definition blocks for all entity/proper noun first mentions
- [ ] Comparison tables on competitive/vs pages
- [ ] No filler phrases ("Great question!", "Let's dive in")

---

# PART 5: LLMO — LARGE LANGUAGE MODEL OPTIMIZATION

**Goal**: Make your content citable and recommendable by LLMs through semantic depth, thematic authority, and trust signals.

## 5.1 How LLMs Read Content

1. **Semantic Understanding** — LLMs understand meaning, not keywords. Cover a topic's full semantic field.
2. **Consistency Checking** — LLMs compare information across sources. Contradictions reduce trust.
3. **Authority Assessment** — Author credentials, citations, domain reputation, content quality patterns.
4. **Structure Recognition** — Clear headers, lists, definitions help LLMs extract and attribute accurately.

## 5.2 Semantic Depth

| High Depth | Low Depth |
|------------|-----------|
| Covers core concepts + related subtopics | Surface-level definitions |
| Addresses common questions/objections | Repeats same points |
| Explains relationships between concepts | Ignores related context |
| Practical applications + examples | Generic, no unique insights |
| References authoritative sources | No supporting evidence |

## 5.3 Hub-and-Spoke Architecture (for LLMO)

Reinforced from Content SEO section — this is the structure LLMs trust most:

- **Hub**: Comprehensive 3K-5K word pillar page with full semantic coverage
- **Spokes**: 1.5K-2.5K word deep-dives per subtopic / fan-out variant
- **Interlinking**: Hub ↔ Spokes, Spokes ↔ Related Spokes — creates a semantic web
- **Outcome**: LLMs recognize your site as an authority on the topic cluster

## 5.4 Trust Signals for LLMs

| Signal | Implementation |
|--------|----------------|
| **Author credentials** | Detailed bio with expertise, certifications, publication history |
| **Source quality** | Citations to primary research, authoritative sources |
| **Content accuracy** | Fact-checked, regularly updated, corrections when needed |
| **Domain reputation** | Backlinks from authoritative sites, industry recognition |
| **Transparency** | Clear methodology, distinction fact vs opinion |
| **Freshness** | Visible "last updated" dates, quarterly content refreshes |

---

# PART 6: MEASUREMENT & MONITORING

> **Reference**: [Google Search Console](https://search.google.com/search-console/about)

## 6.1 Key Metrics by Layer

| Layer | Metric | Tool |
|-------|--------|------|
| **SEO** | Rankings, organic traffic, impressions, CTR, CWV | Google Search Console, Google Analytics |
| **Entity** | Knowledge Panel presence, QID assigned, sameAs coverage | Manual check, Schema.org validator |
| **GEO** | Share of Model (SoM), citation frequency | Peec AI, Otterly, ZipTie, LLMrefs |
| **AEO** | Featured snippet presence, AI Overview citation | Manual check, Semrush, Ahrefs |
| **LLMO** | Brand mentions in LLM outputs, rec rate | Manual check, monitoring tools |

## 6.2 Monthly AI Visibility Tracker Template

Use this spreadsheet to track AI citation progress month-over-month.

### Template

| # | Primary Query | ChatGPT | Perplexity | Gemini | AI Overviews | Trend | Notes |
|---|---------------|:-------:|:----------:|:------:|:------------:|:-----:|-------|
| 1 | "social media automation" | ✅ cited | ❌ | ✅ | ✅ | ↑↑ | Cited by ChatGPT + Gemini |
| 2 | "best smm tool 2026" | ❌ | ✅ cited | ❌ | ❌ | → | Only Perplexity — competitor X cited everywhere |
| 3 | "automate instagram comments" | ❌ | ❌ | ❌ | ❌ | ↓ | No citation — high priority |
| 4 | "rostido pricing" | ✅ | ✅ | ❌ | N/A | ↑ | Core branded query |
| 5 | "social media management vs" | ❌ | ❌ | ❌ | ❌ | — | New — add to content plan |

### Legend

```
✅ = Cited as source
❌ = Not cited
N/A = Not applicable for this platform
↑↑ = Improved this month
↑ = Slightly improved
→ = No change
↓ = Dropped / lost citation
— = Newly tracked
```

### Monthly Ritual

```
Week 1: Run all 20 queries through ChatGPT, Perplexity, Gemini, Google
Week 1: Record citations in tracker
Week 2-3: Implement content fixes for gaps
Week 4: Verify fixes — re-check top 5 gap queries
Month-end: Update trend column, reassess priorities
```

## 6.3 Competitor Citation Tracking

Track not just your own citations — but who's getting cited where you're not.

| Query | Competitor A | Competitor B | Competitor C | Gap Action |
|-------|:-----------:|:-----------:|:-----------:|------------|
| "social media automation" | ChatGPT ✅ | Gemini ✅ | — | Missing citations: match competitor source quality |
| "smm pricing" | Perplexity ✅ | — | ChatGPT ✅ | Need pricing.md, visible pricing page |
| "auto reply comments" | — | ChatGPT ✅ | Perplexity ✅ | Content gap: no step-by-step guide |

When a competitor is cited and you're not:
1. **Analyze** the page that got cited — what structure, data, schema does it have?
2. **Compare** with your equivalent page — what's missing?
3. **Improve** your page with better data, more authoritative sources, clearer structure
4. **Monitor** next month — did citation appear?

## 6.4 Search Console (for Google AI features)

Google explicitly states: **there is no AI-specific Search Console reporting**. AI Overviews and AI Mode use core Search ranking. What you measure:

| Report | What to Monitor | AI Relevance |
|--------|----------------|:------------:|
| **Performance** | Query impressions, clicks, CTR — especially for informational queries | High — AI Overviews correlate with top-ranking content |
| **Coverage** | Indexed pages, errors, exclusions | Medium — must be indexed to be cited |
| **Core Web Vitals** | LCP, INP, CLS performance | Low — affects ranking, which affects AI citation indirectly |
| **Sitemaps** | Submitted URLs, indexed count | Medium — ensures discoverability |

---

# PART 7: FUTURE LAYER — AGENT-READY INFRASTRUCTURE

Google's 2026 AI Optimization Guide explicitly calls out **agentic experiences** as an emerging category. Autonomous agents will access sites directly — clicking, reading, comparing, buying.

> **Reference**: [Google — AI Optimization Guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)

## 7.1 Requirements for Agent Accessibility

| Requirement | Implementation |
|-------------|----------------|
| **Semantic HTML** | `<main>`, `<nav>`, `<article>`, `<button>`, proper heading hierarchy, `alt` text |
| **Clean accessibility tree** | Every interactive element labeled; ARIA used correctly |
| **No JS-gated content** | Critical content must render without JavaScript |
| **Stable selectors** | Avoid re-rendering entire page on every interaction |
| **Visible pricing** | Don't hide behind "contact sales" or JS-rendered modals |
| **Structured data** | Schema markup for products, pricing, features |

## 7.2 Emerging Standards

### OKF (Open Knowledge Format)

Google-backed v0.1 spec — markdown directory of cross-linked files with YAML frontmatter. Makes site content agent-readable without scraping.

### UCP (Universal Commerce Protocol)

Forthcoming protocol for standardized agent hooks: catalog discovery, pricing, checkout. Watch for adoption in 2026-2027.

---

# PART 8: ROSTIDO-SCORE FRAMEWORK

The ROSTIDO-SCORE is a **6-dimension, 72-item scoring system** that produces a 0-100 score for each dimension and an overall composite score. It replaces subjective "good/bad" judgement with a **deterministic, reproducible audit**.

## 8.1 Framework Overview

| Dimension | Weight | Items | Max Score | Focus |
|-----------|:------:|:-----:|:---------:|-------|
| **T** — Technical | 20% | 12 | 120 | Crawl, index, speed, security, mobile |
| **C** — Content | 20% | 12 | 120 | Hub-and-spoke, freshness, EEAT, structure |
| **E** — Entity | 15% | 12 | 120 | KG, Wikidata, sameAs, Knowledge Panel |
| **G** — GEO-readiness | 20% | 12 | 120 | Citations, llms.txt, fan-out, AI bot access |
| **A** — AEO-readiness | 15% | 12 | 120 | Snippets, PAA, voice, FAQ, speakable |
| **R** — Trust | 10% | 12 | 120 | HTTPS, headers, schema, brand mentions |
| | **100%** | **72** | | |

### Scoring Rules

- Each item: **0** (missing/failing), **5** (partial/present but flawed), **10** (fully implemented)
- Dimension score = `(sum_of_items / max_possible) × 100`
- Overall score = `sum(weight × dimension_score)`
- **Veto items**: if ANY veto fails, overall score caps at 50 regardless of other scores

## 8.2 Scoring Dimensions & Items

### Dimension T — Technical (20%, 12 items)

| # | Item | Scoring Guide |
|---|------|---------------|
| T01 | **XML Sitemap** | 10 = exists, valid, submitted to GSC. 5 = exists but has errors. 0 = missing or 404. |
| T02 | **robots.txt** | 10 = configured, includes Sitemap directive, AI bot rules. 5 = exists but incomplete. 0 = missing. |
| T03 | **Canonical tags** | 10 = every page has correct canonical. 5 = partial coverage. 0 = missing. |
| T04 | **HTTPS** | 10 = TLS 1.2+, HTTP→HTTPS redirect. 5 = HTTPS but mixed content. 0 = HTTP only. |
| T05 | **Core Web Vitals** | 10 = LCP≤2.5s, INP≤200ms, CLS≤0.1. 5 = two of three pass. 0 = failing. |
| T06 | **Mobile-friendly** | 10 = passes mobile test. 5 = minor issues (touch targets, font). 0 = not mobile-friendly. |
| T07 | **JavaScript SEO** | 10 = critical content renders without JS. 5 = partial. 0 = completely JS-gated. |
| T08 | **HSTS header** | 10 = `Strict-Transport-Security` present. 5 = present but short max-age. 0 = missing. |
| T09 | **CSP header** | 10 = properly configured CSP. 5 = present but permissive. 0 = missing. |
| T10 | **X-Frame-Options** | 10 = `DENY` or `SAMEORIGIN`. 5 = present but wrong value. 0 = missing. |
| T11 | **X-Content-Type-Options** | 10 = `nosniff` set. 0 = missing. |
| T12 | **Referrer-Policy** | 10 = properly configured. 0 = missing. |

### Dimension C — Content (20%, 12 items)

| # | Item | Scoring Guide |
|---|------|---------------|
| C01 | **Unique title tags** | 10 = every page has unique 50-60 char title. 5 = some duplicates. 0 = missing or all same. |
| C02 | **Unique meta descriptions** | 10 = every page has unique 150-160 char description. 5 = some duplicates. 0 = missing. |
| C03 | **Heading hierarchy** | 10 = proper H1→H2→H3 structure. 5 = mostly correct. 0 = no hierarchy. |
| C04 | **Image alt text** | 10 = all images have descriptive alt. 5 = partial. 0 = missing. |
| C05 | **Internal linking** | 10 = hub-spoke interlinking with descriptive anchors. 5 = weak interlinking. 0 = none. |
| C06 | **Hub-and-spoke structure** | 10 = clear pillar + cluster architecture. 5 = partial. 0 = flat structure. |
| C07 | **Content freshness** | 10 = "last updated" dates, refreshed ≤6 months. 5 = dates present but stale. 0 = no dates. |
| C08 | **Author bios** | 10 = detailed credentials on content pages. 5 = basic bio. 0 = missing. |
| C09 | **Backlink quality** | 10 = authoritative domains linking. 5 = mixed quality. 0 = no/spammy links. |
| C10 | **Brand mentions** | 10 = cited on Wikipedia, review sites, publications. 5 = some mentions. 0 = none. |
| C11 | **Content length by intent** | 10 = matches depth requirements per query intent. 5 = mostly appropriate. 0 = all same length. |
| C12 | **EEAT signals** | 10 = experience, expertise, authority, trust all evident. 5 = 2-3 present. 0 = none. |

### Dimension E — Entity (15%, 12 items)

| # | Item | Scoring Guide |
|---|------|---------------|
| E01 | **Entity home page** | 10 = dedicated About page with canonical @id in schema. 5 = exists but incomplete. 0 = missing. |
| E02 | **Organization schema** | 10 = JSON-LD with name, url, description, foundingDate. 5 = partial. 0 = missing. |
| E03 | **sameAs declarations** | 10 = 3+ authoritative external profiles linked. 5 = 1-2. 0 = none. |
| E04 | **Wikidata entry** | 10 = QID created, properties populated. 5 = QID exists but bare. 0 = no entry. |
| E05 | **LinkedIn presence** | 10 = company page with consistent info. 5 = page exists but inconsistent. 0 = missing. |
| E06 | **Crunchbase / G2 / Capterra** | 10 = listed on 2+ business directories. 5 = 1. 0 = none. |
| E07 | **Wikipedia presence** | 10 = has Wikipedia article (if eligible). 5 = mentioned in other articles. 0 = none. |
| E08 | **sameAs → Wikidata QID** | 10 = Wikidata QID referenced in schema sameAs. 0 = not linked. |
| E09 | **Knowledge Panel** | 10 = active, correct information. 5 = exists but inaccurate. 0 = none. |
| E10 | **Consistent NAP** | 10 = name, address, phone identical across all platforms. 5 = mostly consistent. 0 = conflicts. |
| E11 | **Entity description consistency** | 10 = same description across website, Wikidata, social profiles. 5 = minor variations. 0 = contradictions. |
| E12 | **Brand disambiguation** | 10 = no confusion with similar names; clear distinction. 5 = some ambiguity. 0 = frequently confused. |

### Dimension G — GEO-Readiness (20%, 12 items)

| # | Item | Scoring Guide |
|---|------|---------------|
| G01 | **llms.txt** | 10 = at site root, follows spec, comprehensive. 5 = exists but minimal. 0 = missing. |
| G02 | **pricing.md** | 10 = structured pricing at /pricing.md. 5 = partial. 0 = missing. |
| G03 | **AGENTS.md** | 10 = capability description for autonomous agents. 0 = missing. |
| G04 | **AISEO | 10 = allows GPTBot, ChatGPT-User, PerplexityBot. 5 = some blocked. 0 = blocks all. |
| G05 | **Source citations** | 10 = content cites authoritative sources with links. 5 = occasional. 0 = no citations. |
| G06 | **Statistics with dates** | 10 = stats include numbers + source + year. 5 = partial. 0 = uncited stats. |
| G07 | **Expert quotations** | 10 = quotes with attribution ("According to [Name], [Title]"). 5 = occasional. 0 = none. |
| G08 | **Answer blocks (40-60 words)** | 10 = every key claim has standalone answer block. 5 = some sections. 0 = no answer blocks. |
| G09 | **Query fan-out coverage** | 10 = 12+ fan-out variants covered. 5 = 5-11 covered. 0 = <5 covered. |
| G10 | **Platform-specific optimization** | 10 = content structured for ChatGPT + Perplexity + Gemini differences. 5 = aware but not applied. 0 = generic only. |
| G11 | **Unique data / original research** | 10 = original data not found elsewhere. 5 = some unique data. 0 = all generic. |
| G12 | **Hub-spoke for AI** | 10 = semantic hub + 5+ spokes. 5 = hub only. 0 = no structure. |

### Dimension A — AEO-Readiness (15%, 12 items)

| # | Item | Scoring Guide |
|---|------|---------------|
| A01 | **Direct answer first** | 10 = first paragraph answers query directly. 5 = answer buried. 0 = no direct answer. |
| A02 | **FAQPage schema** | 10 = valid JSON-LD with visible HTML answers. 5 = schema exists but issues. 0 = missing. |
| A03 | **FAQ HTML visible** | 10 = FAQ content in initial DOM (not JS-hidden). 5 = partially hidden. 0 = entirely JS-gated. |
| A04 | **Paragraph snippet ready** | 10 = 40-55 word answer after H2/H3, starts with keyword variant. 5 = close but not exact. 0 = no. |
| A05 | **List snippet ready** | 10 = ≤9 items, ≤15 words each, `<ol>`/`<ul>` under question H2. 5 = exists but suboptimal. 0 = no. |
| A06 | **Table snippet ready** | 10 = ≤4 columns, `<thead>` + `<tbody>`, entity-first. 5 = exists but issues. 0 = no tables. |
| A07 | **PAA coverage** | 10 = 5+ PAA questions answered with H2 + 30-50 word answers. 5 = 2-4 covered. 0 = none. |
| A08 | **speakable schema** | 10 = implemented on key definition sections. 0 = missing. |
| A09 | **HowTo schema** | 10 = implemented for process/tutorial content. 5 = exists but incomplete. 0 = missing. |
| A10 | **Voice-readiness** | 10 = TTFB<2s, HTTPS, conversational answers. 5 = partial. 0 = not voice-ready. |
| A11 | **Definition blocks** | 10 = "X is a [category] that [function]..." pattern for key entities. 5 = some. 0 = none. |
| A12 | **Comparison tables** | 10 = data in tables not prose for competitive/vs pages. 5 = partial. 0 = prose-only. |

### Dimension R — Trust & Security (10%, 12 items)

| # | Item | Scoring Guide |
|---|------|---------------|
| R01 | **Privacy policy** | 10 = clearly accessible from every page. 0 = missing or hidden. |
| R02 | **Terms of service** | 10 = clearly accessible. 0 = missing. |
| R03 | **Contact information** | 10 = email/phone/address visible. 5 = contact form only. 0 = no contact. |
| R04 | **Security headers** | 10 = CSP + HSTS + XFO + XCTO + RP all present. 5 = 2-4 present. 0 = <2. |
| R05 | **Schema validity** | 10 = all JSON-LD passes Rich Results Test. 5 = present but errors. 0 = no schema. |
| R06 | **No broken links** | 10 = no 404s on internal links. 5 = some (<5). 0 = many broken links. |
| R07 | **No redirect chains** | 10 = all redirects direct (1 hop). 5 = some chains (2-3 hops). 0 = 3+ hop chains. |
| R08 | **Page speed (mobile)** | 10 = PageSpeed score ≥ 90. 5 = 50-89. 0 = <50. |
| R09 | **Page speed (desktop)** | 10 = PageSpeed score ≥ 95. 5 = 70-94. 0 = <70. |
| R10 | **Form HTTPS security** | 10 = all forms submit to HTTPS. 5 = mixed. 0 = HTTP forms. |
| R11 | **Copyright / legal footer** | 10 = complete footer with copyright, links. 5 = partial. 0 = missing. |
| R12 | **Brand trust signals** | 10 = customer logos, testimonials, case studies, reviews visible. 5 = some. 0 = none. |

## 8.3 Scoring Rubric

### Per-Item Scoring

| Score | Meaning | When to Use |
|:-----:|---------|-------------|
| **0** | Failing / missing | Feature doesn't exist, or exists but actively harmful (e.g., broken sitemap, wrong canonical) |
| **5** | Partial / flawed | Exists but has issues — incomplete, suboptimal, partially broken |
| **10** | Fully implemented | Follows best practices, no issues, verifiably correct |

### Veto Items

If ANY of these items scores 0, the overall score caps at **50** (out of 100) regardless of other scores.

| Item | Why It's a Veto |
|------|-----------------|
| **T01** — Sitemap missing | If search engines can't discover pages, nothing else matters |
| **T03** — Canonicals missing | Duplicate content kills ranking across entire site |
| **T04** — HTTPS missing | Browsers flag as "Not Secure", zero trust by Google |
| **G01** — llms.txt missing | AI systems have no gateway to discover your content |
| **E02** — Org schema missing | No structured brand identity for Knowledge Graph |
| **A02** — FAQPage schema missing | Misses all FAQ featured snippet opportunities |
| **R05** — Schema invalid | Any schema with errors — structured data is all-or-nothing |

### Score Interpretation

| Overall Score | Rating | Meaning |
|:-------------:|:------:|---------|
| **90-100** | 🏆 Elite | Industry-leading across all layers. Minor optimizations only. |
| **75-89** | ✅ Strong | Most layers solid. 1-2 dimensions need targeted improvement. |
| **60-74** | ⚠️ Adequate | Foundation exists but significant gaps in GEO/AEO/Entity. |
| **40-59** | 🔴 Weak | Technical SEO likely has issues. Start with P0 items. |
| **0-39** | ❌ Critical | Missing fundamentals. Fix sitemap, HTTPS, canonicals first. |
| **Capped 50** | 🚫 Veto | A veto item is failing. Fix that specific item first. |

## 8.4 Quick Score Calculation

For a quick assessment without full scoring:

```
1. Pick the relevant dimension (T, C, E, G, A, R)
2. Scan the items
3. Count: ___ items at 10 × 1.0 + ___ items at 5 × 0.5 + ___ items at 0 × 0
4. Score = (sum / max) × 100
```

Example (Technical):
- 12 items × 10 = 120 max
- 7 items at 10 + 3 items at 5 + 2 items at 0
- = (70 + 15 + 0) / 120 × 100
- = 85/120 × 100 = **70.8**

---

# PART 9: SKILL CONTRACT & HANDOFF PROTOCOL

Every audit, analysis, or content creation job using this skill produces a **standardized output**. This enables chaining multiple tasks together — you can feed the output of an audit into a content creation task, which feeds into a GEO optimization task, etc.

## 9.1 Expected Output

Every job must produce:

```
1. A SCORE or VERDICT (when auditing)
2. A structured HANDOFF SUMMARY (always)
3. A prioritized ACTION LIST (when issues found)
4. Optional: A content ASSET (when creating content)
```

## 9.2 Handoff Summary Format

```yaml
HANDOFF SUMMARY
---
target_url: https://example.com
job_type: audit  # or: create, optimize, analyze, track
score:
  overall: 72.4
  dimensions:
    technical: 68.5
    content: 81.2
    entity: 45.0
    geo: 70.8
    aeo: 55.0
    trust: 83.3
  veto_hit: false
veto_items:
  - id: E02
    status: FAIL
    detail: Organization JSON-LD missing from entity home page
p0_fixes:
  - Create Organization JSON-LD with @id, name, url, foundingDate, sameAs
  - Add llms.txt to site root
  - Fix missing canonical tags on /blog/ pages
p1_fixes:
  - Add FAQPage schema to /#faq section
  - Add speakable schema to About page
  - Build hub-and-spoke architecture for primary topic cluster
key_evidence:
  - sitemap.xml: 404 (missing)
  - security_headers: HSTS missing, CSP missing
  - schema: Organization JSON-LD not found
  - llms.txt: 404 (missing)
open_loops:
  - Wikidata entry not created
  - Knowledge Panel not claimed
  - Query fan-out coverage incomplete (12 of 20 variants)
  - No original research data for citations
next_best_skill:
  - entity-optimizer: Create Wikidata entry + sameAs profile
  - geo-content-optimizer: Create answer blocks for top 5 queries
```

## 9.3 Inter-Skill Chaining

When chaining this skill with others (or looping within itself), pass:

| Field | Description |
|-------|-------------|
| `target_url` | URL being affected |
| `job_type` | audit / create / optimize / track |
| `score` | Current ROSTIDO-SCORE (if audit) |
| `p0_fixes` | Critical items still open |
| `p1_fixes` | Important items still open |
| `open_loops` | Non-urgent follow-ups |
| `assets_created` | Files, schemas, content generated |
| `completion_status` | DONE / DONE_WITH_CONCERNS / BLOCKED / NEEDS_INPUT |

---

# PART 10: QUERY FAN-OUT FRAMEWORK

A **query fan-out** is the complete set of search queries and AI prompts that users and AI engines generate around a topic. Covering the full fan-out is the single highest-leverage content strategy for both SEO and GEO.

## 10.1 Why Fan-Out Matters

| Channel | Why Fan-Out Coverage Matters |
|---------|------------------------------|
| **SEO** | Google's semantic ranking rewards complete topical coverage — not just 1 keyword |
| **GEO** | AI engines generate variations of queries; they cite sources that cover most variants |
| **AEO** | Featured snippets are fought per-variant; multiple snippet wins require multiple variants |
| **LLMO** | LLMs trained on deeper content recall your brand across more contexts |

## 10.2 Complete Query Template Library

For ANY topic `[X]`:

### Informational

| Template | Example | Content Type |
|----------|---------|-------------|
| What is [X]? | What is social media automation? | Definition block |
| How does [X] work? | How does social media automation work? | Step-by-step |
| What is [X] used for? | What is social media automation used for? | Use cases |
| How to [do action with X]? | How to automate Instagram comments | Tutorial |
| Why [X] is important? | Why social media automation is important | Benefits page |
| Who uses [X]? | Who uses social media automation? | Audience page |
| When to use [X]? | When to use social media automation? | Decision guide |
| [X] explained | Social media automation explained | Beginner guide |
| [X] for beginners | Social media automation for beginners | Beginner guide |

### Comparative

| Template | Example | Content Type |
|----------|---------|-------------|
| [X] vs [Y] | Rostido vs Hootsuite | Comparison |
| [X] alternatives | Rostido alternatives | List + compare |
| [X] vs [Y] vs [Z] | Buffer vs Hootsuite vs Rostido | Multi-comparison |
| Best [X] | Best social media automation tools | Listicle + table |
| Top [X] for [use case] | Top social media tools for agencies | Curated list |
| [X] or [Y] | Rostido or Hootsuite for small business | Decision page |
| [X] review | Rostido review 2026 | Review page |
| Is [X] worth it? | Is Rostido worth it? | Value page |
| [X] pros and cons | Rostido pros and cons | Balanced review |

### Transactional / Purchase

| Template | Example | Content Type |
|----------|---------|-------------|
| [X] pricing | Rostido pricing | Pricing page |
| [X] cost | How much does Rostido cost? | Pricing detail |
| [X] free | Is Rostido free? | Free tier page |
| [X] discount | Rostido discount | Offer page |
| [X] coupon | Rostido coupon code | Coupon page |
| Buy [X] | Buy Rostido | Purchase page |
| [X] login | Rostido login | Auth page |
| [X] sign up | Rostido sign up | Registration |

### Technical / Specific

| Template | Example | Content Type |
|----------|---------|-------------|
| Does [X] support [Y]? | Does Rostido support TikTok? | Feature page |
| How to [specific] in [X]? | How to schedule posts in Rostido | Tutorial |
| [X] API | Rostido API | Docs page |
| [X] integration | Rostido integration | Integration page |
| [X] vs [competitor] | Rostido vs Buffer | Comparison |
| [X] features | Rostido features | Feature page |
| [X] for [platform] | Rostido for Instagram | Platform page |
| [X] for [industry] | Social media automation for ecommerce | Industry page |

### Brand / Entity

| Template | Example | Content Type |
|----------|---------|-------------|
| Who created [X]? | Who created Rostido? | About page |
| Who owns [X]? | Who owns Rostido? | Company info |
| [X] headquarters | Rostido headquarters | Location |
| [X] founded | When was Rostido founded? | Company history |
| [X] employees | Rostido team | Team page |
| [X] funding | Rostido funding | Investors page |

## 10.3 How to Map Fan-Out for Any Topic

```
STEP 1: Identify your core topic entity
  → "Rostido" or "Social Media Automation"

STEP 2: Generate all template variants
  → Run through all 4+ categories above
  → Generate 20-30 specific queries

STEP 3: Check existing coverage
  → Does your site have a page for each?
  → Note which are missing

STEP 4: Prioritize by opportunity
  → HIGH priority: informational + comparative (drive citations)
  → MEDIUM priority: transactional (drive conversions)
  → LOW priority: technical/brand (smaller audience)

STEP 5: Create content plan
  → Hub page for core topic + spokes for each variant
  → Start with HIGH priority gaps

STEP 6: Track and iterate
  → Monthly: re-check which variants are now covered
  → Quarterly: add emerging variants
```

---

# PART 11: AUDIT CHECKLIST

Use this to audit any website completely. Each item maps to the ROSTIDO-SCORE framework (see §8).

## 11.1 Technical SEO

- [ ] robots.txt configured, includes Sitemap directive, allows AI bots
- [ ] XML sitemap clean, submitted to GSC, auto-updates
- [ ] Canonical tags on every page
- [ ] No broken links or redirect chains
- [ ] Core Web Vitals pass (LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1)
- [ ] Mobile-friendly (touch targets ≥ 48px, no intrusive interstitials)
- [ ] HTTPS + HSTS + CSP + X-Frame-Options + X-Content-Type-Options + Referrer-Policy
- [ ] JavaScript renders critical content (test with JS disabled)

## 11.2 On-Page SEO

- [ ] Unique title tags, meta descriptions, H1 per page
- [ ] Heading hierarchy (H1 → H2 → H3)
- [ ] Image alt text on all images
- [ ] Internal linking to related content
- [ ] Clean URL structure

## 11.3 Entity SEO

- [ ] Organization JSON-LD on entity home page with @id
- [ ] sameAs pointing to Wikidata, LinkedIn, Twitter, Crunchbase, GitHub
- [ ] Wikidata entry created with QID
- [ ] Knowledge Panel claimed (if eligible)
- [ ] Consistent NAP across all platforms
- [ ] Brand disambiguation (no confusion with similar entities)

## 11.4 GEO / AI Readiness

- [ ] llms.txt at site root
- [ ] pricing.md at site root
- [ ] AGENTS.md at site root
- [ ] robots.txt allows GPTBot, PerplexityBot, ClaudeBot, Google-Extended
- [ ] Content cites authoritative sources with links
- [ ] Statistics include specific numbers + source + date
- [ ] Expert quotes with attribution
- [ ] "Last updated" dates on content pages
- [ ] Author bios with credentials
- [ ] Topical hub-and-spoke architecture
- [ ] Content covers query fan-out variants (12+ covered)
- [ ] Unique data / original research present

## 11.5 AEO

- [ ] Direct answer in first 40-55 words after H2/H3 for key sections
- [ ] Paragraph snippet: answer starts with keyword variant
- [ ] List snippet: ≤9 items, ≤15 words each, `<ol>`/`<ul>` under question heading
- [ ] Table snippet: ≤4 columns, `<thead>` + `<tbody>`, entity-first column
- [ ] PAA: 5+ questions answered with exact H2 + 30-50 word answers
- [ ] FAQPage JSON-LD with FAQ content visible in HTML
- [ ] speakable schema on definition sections
- [ ] HowTo schema for process/tutorial content
- [ ] Voice-ready: TTFB < 2s, HTTPS, conversational answers
- [ ] Definition blocks on first mention of key entities
- [ ] Comparison tables on competitive pages
- [ ] No filler phrases ("Great question!", "Let's dive in")

## 11.6 Future-Proof

- [ ] Semantic HTML structure
- [ ] Pricing visible without login/JS
- [ ] AGENTS.md file
- [ ] OKF bundle (for advanced setups)
- [ ] Clean accessibility tree

---

# PART 12: PRIORITY TIERS

Not everything needs to be done at once. Use this priority guide, which maps to the ROSTIDO-SCORE framework.

## 🔴 P0 — Must Have (do first)
*These are the veto items + highest impact. Fixing these moves score from 0→50+.*

```
1. XML sitemap + submit to GSC        [T01]
2. Canonical tags on every page       [T03]
3. HTTPS + HSTS + redirect            [T04, R04]
4. Organization JSON-LD on entity home [E02]
5. robots.txt with AI bot rules       [T02, G04]
6. llms.txt                           [G01 — GEO veto]
7. FAQPage JSON-LD with visible FAQ   [A02]
8. Core Web Vitals pass               [T05]
9. pricing.md                         [G02]
10. Zero broken links or 404s         [R06]
```

## 🟡 P1 — Should Have (within 1 month)
*These build the foundation for strong scores in Content, Entity, and GEO.*

```
11. sameAs schema + 3+ external profiles [E03]
12. Unique title tags + meta descriptions [C01, C02]
13. "Last updated" dates on content     [C07]
14. Author bios with credentials        [C08]
15. Source citations in content         [G05]
16. Statistics with dates               [G06]
17. Hub-and-spoke architecture          [C06, G12]
18. Mobile-friendly verification        [T06]
19. Privacy policy + terms in footer    [R01, R02]
20. Contact info visible                [R03]
```

## 🟢 P2 — Nice to Have (within 3 months)
*These differentiate from competitors and unlock GEO/AEO scores.*

```
21. Wikidata entry with QID             [E04]
22. Knowledge Panel claiming            [E09]
23. AGENTS.md                           [G03]
24. Comparison tables on key pages      [A12]
25. FAQ content visible in HTML         [A03]
26. speakable schema                    [A08]
27. HowTo schema                        [A09]
28. CSP + X-Frame-Options security      [T09, T10]
29. PAA question coverage (5+)          [A07]
30. Query fan-out content plan          [G09]
31. Answer blocks (40-60 words)         [G08]
32. Expert quotes with attribution      [G07]
```

## ⚪ P3 — Ongoing (continuous)
*These require regular upkeep, not one-time setup.*

```
33. Monthly AI visibility monitoring    [§6.2]
34. Competitor citation tracking        [§6.3]
35. Quarterly content refreshes         [C07]
36. Backlink building (earned)          [C09]
37. Brand mention tracking              [C10]
38. Content gap analysis (fan-out)      [G09]
39. Query fan-out expansion             [§10]
40. ROSTIDO-SCORE re-audit (quarterly)  [§8]
```

---

# APPENDIX A: QUICK REFERENCE

## Schema Types for Maximum Impact

| Type | Priority | Use Case |
|------|:--------:|----------|
| `Organization` | 🔴 EVERY site | Brand identity in Knowledge Graph |
| `SoftwareApplication` | 🔴 SaaS | Product description + features + offers |
| `FAQPage` | 🔴 FAQ sections | Featured snippet + AI answer extraction |
| `Product` | 🟡 Ecommerce | Product details + offers + reviews |
| `Article` | 🟡 Blog | News, blog posts, articles |
| `HowTo` | 🟡 Tutorials | Step-by-step guides |
| `BreadcrumbList` | 🟢 Navigation | Search result breadcrumb path |
| `Review` / `AggregateRating` | 🟢 Reviews | Star ratings in SERP |
| `speakable` | 🟢 Voice | Text-to-speech optimization |

---

# APPENDIX B: AI CRAWLER USER-AGENTS

| Bot | Platform | Purpose | Allow/Block |
|-----|----------|---------|:-----------:|
| `GPTBot` | ChatGPT | Search + training | ✅ Allow |
| `ChatGPT-User` | ChatGPT | Real-time search | ✅ Allow |
| `PerplexityBot` | Perplexity | Search + citation | ✅ Allow |
| `ClaudeBot` | Claude | Search + training | ✅ Allow |
| `anthropic-ai` | Claude | Training only | ⚠️ Optional block |
| `Google-Extended` | Gemini, AI Overviews | Training + search | ✅ Allow |
| `CCBot` | Common Crawl | Training only | ❌ Block |
| `Bytespider` | ByteDance | Training | ❌ Block |
| `Meta` / `FacebookBot` | Meta AI | Training + search | ⚠️ Optional allow |

> **Reference**: [Google — Blocking AI Crawlers](https://developers.google.com/search/docs/crawling-indexing/blocking-ai-crawlers)

---

# APPENDIX C: AUTOMATION SCRIPTS

**8 real Python scripts** in `scripts/` — stdlib-only, zero dependencies. Each script produces structured JSON output (`--json` flag) and a human-readable console view (default).

| Script | Lines | Purpose |
|--------|:-----:|---------|
| `check_security_headers.py` | 165 | HSTS, CSP, XFO, X-CT-O, Referrer-Policy, Permissions-Policy |
| `check_robots_txt.py` | 185 | robots.txt parsing, AI bot rules, sitemap directives |
| `check_core_web_vitals.py` | 186 | LCP, INP, CLS, TTFB via PageSpeed Insights (no API key) |
| `check_schema.py` | 206 | JSON-LD extraction + 10 schema type validation |
| `check_llms_files.py` | 145 | /llms.txt, /pricing.md, /AGENTS.md existence + quality |
| `check_sitemap.py` | 192 | Sitemap XML parsing, nested index support |
| `generate_score_report.py` | 333 | Aggregates all checks → ROSTIDO-SCORE HTML dashboard |
| `check_ai_visibility.py` | 211 | Interactive AI citation tracker (ChatGPT, Perplexity, Gemini, AIO) |
| **Total** | **1,623** | |

### Quick Start

```bash
# Single check
python3 scripts/check_security_headers.py https://example.com
python3 scripts/check_llms_files.py https://example.com --json

# Full audit + HTML report
python3 scripts/generate_score_report.py https://example.com --output report.html

# Monthly AI visibility tracking
python3 scripts/check_ai_visibility.py
```

### All scripts produce
- ✅ Human-readable console output by default
- ✅ Structured JSON with `--json` flag (for piping/chaining)
- ✅ Error handling (timeout, 404, connection refused)
- ✅ Exit codes (0 = pass, 1 = fail)

---

# APPENDIX D: TOOLS REFERENCE

| Purpose | Tool | Cost | URL |
|---------|------|:----:|-----|
| **AI visibility monitoring** | Peec AI | Paid | peec.ai |
| **AI visibility monitoring** | Otterly | Paid | otterly.ai |
| **AI visibility monitoring** | ZipTie | Paid | ziptie.ai |
| **AI visibility monitoring** | LLMrefs | Free | llmrefs.com |
| **Traditional SEO** | Google Search Console | Free | search.google.com/search-console |
| **Traditional SEO** | Ahrefs | Paid | ahrefs.com |
| **Traditional SEO** | Semrush | Paid | semrush.com |
| **Schema testing** | Google Rich Results Test | Free | search.google.com/test/rich-results |
| **Schema testing** | Schema.org Validator | Free | validator.schema.org |
| **Entity / Knowledge Graph** | Wikidata | Free | wikidata.org |
| **Entity / Knowledge Panel** | Google Knowledge Panel | Free | google.com/knowledge-panel |
| **Page speed** | PageSpeed Insights | Free | pagespeed.web.dev |
| **Page speed** | Lighthouse (Chrome) | Free | developer.chrome.com/lighthouse |
| **Crawl audit** | Screaming Frog | Free/Paid | screamingfrog.co.uk |
| **Crawl audit** | Sitebulb | Paid | sitebulb.com |
| **Security headers** | securityheaders.com | Free | securityheaders.com |
| **Robots.txt testing** | robots-txt.com | Free | robots-txt.com |

---

# APPENDIX E: OFFICIAL REFERENCE LINKS

| Topic | URL |
|-------|-----|
| Google AI Optimization Guide | https://developers.google.com/search/docs/fundamentals/ai-optimization-guide |
| Google Search Essentials | https://developers.google.com/search/docs/fundamentals/seo-starter-guide |
| Google SEO Documentation | https://developers.google.com/search/docs |
| Google E-E-A-T Guide | https://developers.google.com/search/docs/fundamentals/creating-helpful-content |
| Google Core Web Vitals | https://web.dev/articles/vitals |
| Google Mobile-First Indexing | https://developers.google.com/search/docs/crawling-indexing/mobile-first-indexing |
| Google JavaScript SEO | https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics |
| Google Blocking AI Crawlers | https://developers.google.com/search/docs/crawling-indexing/blocking-ai-crawlers |
| Google FAQ Schema | https://developers.google.com/search/docs/appearance/structured-data/faqpage |
| Google HowTo Schema | https://developers.google.com/search/docs/appearance/structured-data/how-to |
| Google speakable Schema | https://developers.google.com/search/docs/appearance/structured-data/speakable |
| Google Rich Results Test | https://search.google.com/test/rich-results |
| Schema.org (full spec) | https://schema.org/docs/full.html |
| Schema.org Organization | https://schema.org/Organization |
| Wikidata Create Item | https://www.wikidata.org/wiki/Special:NewItem |
| llmstxt.org Spec | https://llmstxt.org/ |
| Princeton GEO Research (KDD 2024) | https://dl.acm.org/doi/10.1145/3637528.3671579 |
| Digital Applied GEO Guide | https://www.digitalapplied.com/blog/geo-guide-generative-engine-optimization-2026 |
| Lumar GEO/AEO Guide | https://www.lumar.io/blog/best-practice/geo-aeo-seo-experts-weigh-in-on-ai-search/ |
| HubSpot AEO State 2026 | https://www.emarketer.com/content/faq-on-geo-aeo--where-ai-search-seo-overlap-2026 |
| Search Engine Land — Entity Home | https://searchengineland.com/google-knowledge-panel-entity-home-443429 |
