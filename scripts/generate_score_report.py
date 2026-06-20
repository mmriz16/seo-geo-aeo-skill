#!/usr/bin/env python3
"""
Generate interactive ROSTIDO-SCORE HTML report with actionable solutions.

Can run all check scripts and aggregate results, or load from existing JSON.
Includes specific Next.js/Tailwind implementation recommendations.

Usage:
    python generate_score_report.py https://example.com --output report.html
    python generate_score_report.py https://example.com --output report.html --open
"""

import argparse
import io
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime
from urllib.parse import urlparse

import urllib.request
import urllib.error

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# ─── ROSTIDO-SCORE dimension definitions ───────────────────────────────
ROSTIDO_DIMENSIONS = {
    "technical": {"label": "Technical SEO", "weight": 20, "color": "#4A90D9", "max": 100},
    "content":   {"label": "Content & Authority", "weight": 20, "color": "#50B86C", "max": 100},
    "entity":    {"label": "Entity & Knowledge Graph", "weight": 15, "color": "#9B59B6", "max": 100},
    "geo":       {"label": "GEO-readiness", "weight": 20, "color": "#E67E22", "max": 100},
    "aeo":       {"label": "AEO-readiness", "weight": 15, "color": "#E74C3C", "max": 100},
    "trust":     {"label": "Trust & Security", "weight": 10, "color": "#1ABC9C", "max": 100},
}

VETO_DIMENSIONS = {
    "technical": {"items": ["sitemap", "canonicals", "HTTPS"], "threshold": 30},
    "geo":       {"items": ["llms.txt"], "threshold": 30},
    "aeo":       {"items": ["FAQPage schema"], "threshold": 30},
    "entity":    {"items": ["Organization schema"], "threshold": 30},
}

# ─── Check script mapping → dimension ─────────────────────────────────
CHECK_MAP = {
    "check_security_headers": {
        "dim": "technical",
        "weight_in_dim": 0.5,
        "label": "Security Headers"
    },
    "check_robots_txt": {
        "dim": "technical",
        "weight_in_dim": 0.3,
        "label": "Robots.txt"
    },
    "check_sitemap": {
        "dim": "technical",
        "weight_in_dim": 0.2,
        "label": "Sitemap"
    },
    "check_core_web_vitals": {
        "dim": "content",
        "weight_in_dim": 0.3,
        "label": "Core Web Vitals"
    },
    "check_llms_files": {
        "dim": "geo",
        "weight_in_dim": 1.0,
        "label": "LLMS Files"
    },
    "check_schema": {
        "dim": "aeo",
        "weight_in_dim": 0.6,
        "label": "Schema"
    },
}

# ─── Icons ──────────────────────────────────────────────────────────────
def score_icon(score: float) -> str:
    if score is None: return "⚪"
    if score >= 80: return "🟢"
    if score >= 50: return "🟡"
    return "🔴"

def check_status_icon(score: float) -> str:
    if score is None: return "⚠️"
    if score >= 80: return "✅"
    if score >= 50: return "⚠️"
    return "❌"

# ─── Run checks ────────────────────────────────────────────────────────
def run_check(script_path: str, url: str) -> dict:
    try:
        result = subprocess.run(
            [sys.executable, script_path, url, "--json"],
            capture_output=True, text=True, timeout=30,
        )
        if result.returncode == 0 and result.stdout.strip():
            return json.loads(result.stdout)
        return {"score": None, "error": result.stderr[:300] or "no output"}
    except subprocess.TimeoutExpired:
        return {"score": None, "error": "timeout (30s)"}
    except Exception as e:
        return {"score": None, "error": str(e)}


def run_all_checks(url: str, scripts_dir: str) -> dict:
    checks = {}
    script_names = [
        "check_security_headers.py",
        "check_robots_txt.py",
        "check_core_web_vitals.py",
        "check_schema.py",
        "check_llms_files.py",
        "check_sitemap.py",
    ]
    for name in script_names:
        path = os.path.join(scripts_dir, name)
        key = name.replace(".py", "")
        if os.path.exists(path):
            checks[key] = run_check(path, url)
        else:
            checks[key] = {"score": None, "error": f"Script not found: {path}"}
    return checks

# ─── Dimension scoring ─────────────────────────────────────────────────
def compute_dimension_scores(checks: dict) -> dict:
    """Map check results to ROSTIDO-SCORE dimensions with proper weighting."""
    dim_scores = {k: [] for k in ROSTIDO_DIMENSIONS}

    for check_name, meta in CHECK_MAP.items():
        result = checks.get(check_name, {})
        score = result.get("score")
        error = result.get("error", "")
        # Skip checks that explicitly failed (e.g. CWV quota exceeded)
        if score is not None and not error:
            dim_scores[meta["dim"]].append((score, meta["weight_in_dim"]))

    scores = {}
    for dim, pairs in dim_scores.items():
        if pairs:
            total_weight = sum(w for _, w in pairs)
            if total_weight > 0:
                weighted = sum(s * w for s, w in pairs) / total_weight
                scores[dim] = round(weighted, 1)
            else:
                scores[dim] = 0.0
        else:
            scores[dim] = 0.0

    # Entity dimension isn't covered by automated checks
    # Derive from schema: if Organization schema present → 80, else 20
    schema_check = checks.get("check_schema", {})
    schema_recs = schema_check.get("recommendations", {})
    org_status = schema_recs.get("Organization", {}).get("status", "missing")
    scores["entity"] = 80.0 if org_status == "present" else 20.0

    # Trust dimension: HTTPS + security headers status
    sec = checks.get("check_security_headers", {})
    trust_score = 0
    if sec.get("https_enabled"): trust_score += 30
    hdrs = sec.get("headers", {})
    if hdrs.get("strict-transport-security", {}).get("status") == "present": trust_score += 20
    if hdrs.get("content-security-policy", {}).get("status") == "present": trust_score += 20
    if hdrs.get("x-frame-options", {}).get("status") == "present": trust_score += 15
    if hdrs.get("x-content-type-options", {}).get("status") == "present": trust_score += 15
    scores["trust"] = float(trust_score)

    return scores


def compute_overall(dim_scores: dict) -> float:
    overall = 0.0
    for key, dim in ROSTIDO_DIMENSIONS.items():
        overall += dim_scores.get(key, 0) * (dim["weight"] / 100)
    return round(overall, 1)


def check_veto(dim_scores: dict, checks: dict) -> tuple:
    """Check veto conditions. Returns (veto_hit: bool, veto_details: list)."""
    veto_items = []

    # Technical veto: HTTPS
    sec_check = checks.get("check_security_headers", {})
    if not sec_check.get("https_enabled", False):
        veto_items.append({"id": "HTTPS", "detail": "HTTPS not enabled"})
    elif dim_scores.get("technical", 100) < 30:
        veto_items.append({"id": "sitemap", "detail": "Technical SEO score < 30"})

    # Schema vetoes
    schema_check = checks.get("check_schema", {})
    schema_recs = schema_check.get("recommendations", {})
    if schema_recs.get("Organization", {}).get("status") == "missing":
        veto_items.append({"id": "Organization schema", "detail": "Missing Organization JSON-LD"})
    if schema_recs.get("FAQPage", {}).get("status") == "missing":
        veto_items.append({"id": "FAQPage schema", "detail": "Missing FAQPage JSON-LD"})

    # llms.txt veto
    llms_check = checks.get("check_llms_files", {})
    llms_files = llms_check.get("files", {})
    if not llms_files.get("llms.txt", {}).get("exists", False):
        veto_items.append({"id": "llms.txt", "detail": "Missing llms.txt at site root"})

    return len(veto_items) > 0, veto_items

# ─── Recommendation generator ──────────────────────────────────────────
def generate_recommendations(dim_scores: dict, checks: dict) -> tuple:
    """Generate P0/P1/P2 recommendations from check data. Returns (p0, p1, p2)."""
    p0, p1, p2 = [], [], []

    # Technical
    sec_check = checks.get("check_security_headers", {})
    headers = sec_check.get("headers", {})
    for hkey, hdata in headers.items():
        if hdata.get("status") == "missing":
            severity = hdata.get("severity", "low")
            rec = hdata.get("recommendation", "")
            entry = f"[{severity.upper()}] {hdata.get('label')}: {rec}"
            if severity == "high":
                p0.append(entry)
            elif severity == "medium":
                p1.append(entry)
            else:
                p2.append(entry)

    if not sec_check.get("https_enabled", True):
        p0.append("[HIGH] HTTPS: Enable HTTPS — required for ranking, SEO, and GEO trust")

    # Sitemap
    sm_check = checks.get("check_sitemap", {})
    if sm_check.get("found"):
        urls = sm_check.get("sample_urls", [])
        if not any(u for u in urls if u.rstrip("/") not in ("/login", "/register", "/privacy", "/terms", "/robots.txt", "/llms.txt", "/pricing.txt", "/")):
            p1.append("[MEDIUM] Sitemap only contains auth/legal pages — add main content URLs (dashboard, features, blog, etc.)")

    # Schema gaps
    schema_check = checks.get("check_schema", {})
    schema_recs = schema_check.get("recommendations", {})
    schema_map = {
        "WebSite": ("[MEDIUM] Add WebSite schema — needed for Google Sitelinks Search Box and brand recognition in AI responses", "p1"),
        "BreadcrumbList": ("[MEDIUM] Add BreadcrumbList schema — helps Google understand page hierarchy and shows breadcrumbs in SERP", "p1"),
        "speakable": ("[LOW] Add speakable schema — enables Google Assistant to read your content aloud (text-to-speech/AEO)", "p2"),
    }
    for stype, (msg, tier) in schema_map.items():
        if schema_recs.get(stype, {}).get("status") == "missing":
            if tier == "p1": p1.append(msg)
            else: p2.append(msg)

    # llms.txt quality
    llms_check = checks.get("check_llms_files", {})
    llms_files = llms_check.get("files", {})
    for fname, fdata in llms_files.items():
        if fdata.get("exists") and fdata.get("status") != 200:
            p2.append(f"[LOW] {fname} returns HTTP {fdata.get('status')} instead of 200")

    # Robots.txt AI crawler warnings
    robots_check = checks.get("check_robots_txt", {})
    for w in robots_check.get("warnings", []):
        p2.append(f"[LOW] {w}")

    return p0, p1, p2


def generate_solutions_block(checks: dict) -> str:
    """Generate a detailed HTML solutions block with code/config examples."""
    sections = []

    # Security headers solution
    sec_check = checks.get("check_security_headers", {})
    missing_high = []
    for hkey, hdata in sec_check.get("headers", {}).items():
        if hdata.get("status") == "missing" and hdata.get("severity") == "high":
            missing_high.append(hdata)

    if missing_high:
        code_lines = []
        for h in missing_high:
            code_lines.append(f"  // {h['label']}")
            code_lines.append(f"  '{h['recommendation'].split(':')[0].strip()}': '{': '.join(h['recommendation'].split(': ')[1:])}'," if ': ' in h.get('recommendation','') else f"  // Set: {h['recommendation']}")

        # Use actual HSTS/CSP examples
        csp_rec = "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self' data:; connect-src 'self' https:; frame-ancestors 'none'"

        sections.append(f"""
    <div class="solution-block">
      <h4>🔒 Security Headers (Next.js / Vercel / Cloudflare)</h4>
      <p>Add to <code>next.config.js</code> or Cloudflare Transform Rules:</p>
      <pre class="code-block">// next.config.js
const securityHeaders = [
  {{ key: 'Strict-Transport-Security', value: 'max-age=31536000; includeSubDomains' }},
  {{ key: 'X-Frame-Options', value: 'SAMEORIGIN' }},
  {{ key: 'X-Content-Type-Options', value: 'nosniff' }},
  {{ key: 'Referrer-Policy', value: 'strict-origin-when-cross-origin' }},
  {{ key: 'Permissions-Policy', value: 'camera=(), microphone=(), geolocation=()' }},
  {{
    key: 'Content-Security-Policy',
    value: '{csp_rec}'
  }},
]

module.exports = {{
  async headers() {{
    return [
      {{
        source: '/(.*)',
        headers: securityHeaders,
      }},
    ]
  }},
}}</pre>
    </div>""")

    # Schema gaps
    schema_check = checks.get("check_schema", {})
    schema_recs = schema_check.get("recommendations", {})
    missing_schemas = [k for k, v in schema_recs.items() if v.get("status") == "missing"]

    if missing_schemas:
        extra = ""
        if "WebSite" in missing_schemas:
            extra += """
      <p><strong>WebSite schema</strong> — add to layout.tsx:</p>
      <pre class="code-block">{{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Rostido",
  "url": "https://rostido.termicons.com",
  "potentialAction": {{
    "@type": "SearchAction",
    "target": "https://rostido.termicons.com/search?q={{search_term_string}}",
    "query-input": "required name=search_term_string"
  }}
}}</pre>"""
        if "BreadcrumbList" in missing_schemas:
            extra += """
      <p><strong>BreadcrumbList schema</strong> — add to each page:</p>
      <pre class="code-block">{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [{{
    "@type": "ListItem",
    "position": 1,
    "name": "Home",
    "item": "https://rostido.termicons.com"
  }}]
}}</pre>"""
        if "speakable" in missing_schemas:
            extra += """
      <p><strong>Speakable schema</strong> — add for AEO / Google Assistant:</p>
      <pre class="code-block">{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "speakable": {{
    "@type": "SpeakableSpecification",
    "cssSelector": [".headline", ".summary"]
  }}
}}</pre>"""
        sections.append(f"""
    <div class="solution-block">
      <h4>📋 Missing Schema Types</h4>
      <p>Missing schemas: {', '.join(missing_schemas)}</p>{extra}
    </div>""")

    # Sitemap content coverage
    sm_check = checks.get("check_sitemap", {})
    if sm_check.get("found") and sm_check.get("url_count", 0) <= 8:
        sections.append("""
    <div class="solution-block">
      <h4>🗺️ Sitemap Content Coverage</h4>
      <p>Current sitemap only has login/register/privacy/terms pages. Add main content pages to help Google discover them:</p>
      <pre class="code-block">// next-sitemap.config.js (or generate manually)
module.exports = {
  siteUrl: 'https://rostido.termicons.com',
  generateRobotsTxt: true,
  additionalPaths: async (config) => [
    await config.transform(config, '/dashboard'),
    await config.transform(config, '/pricing'),
    await config.transform(config, '/features'),
    await config.transform(config, '/docs'),
  ],
}</pre>
    </div>""")

    # GEO readiness suggestions
    llms_check = checks.get("check_llms_files", {})
    llms_files = llms_check.get("files", {})
    if llms_files.get("llms.txt", {}).get("exists", False):
        length = llms_files["llms.txt"].get("content_length", 0)
        if length < 2000:
            sections.append("""
    <div class="solution-block">
      <h4>🤖 GEO / LLMS.txt Optimization</h4>
      <p>llms.txt exists but is relatively short. For better AI context, expand with:</p>
      <ul>
        <li>API endpoints and authentication method</li>
        <li>Supported platforms (TikTok, YouTube, Instagram, etc.)</li>
        <li>Key differentiators from competitors</li>
        <li>Technical stack summary (Next.js, Tailwind, etc.)</li>
        <li>User count or trust signals (if available)</li>
      </ul>
    </div>""")

    return "\n".join(sections)


# ─── HTML generator ────────────────────────────────────────────────────
CSS = """
/* ═══ Framer-inspired Dark Canvas Design System ═══ */
/* canvas: #090909 | surface-1: #141414 | ink: #ffffff | ink-muted: #999999 */
/* accent-blue: #0099ff | hairline: #262626 | pill radius: 100px */

* { margin:0; padding:0; box-sizing:border-box; }

body {
  font-family: 'Inter Variable', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  font-feature-settings: 'cv01' 1, 'cv05' 1, 'cv09' 1, 'cv11' 1, 'ss03' 1, 'ss07' 1, 'dlig' 1;
  background: #090909;
  color: #ffffff;
  line-height: 1.4;
  -webkit-font-smoothing: antialiased;
}

.container { max-width:1000px; margin:0 auto; padding:30px 20px; }

/* ── Typography ── */
h1 {
  font-size: 32px;
  font-weight: 500;
  letter-spacing: -1px;
  line-height: 1.13;
  margin-bottom: 4px;
  color: #ffffff;
}
h2 {
  font-size: 20px;
  font-weight: 500;
  letter-spacing: -0.8px;
  line-height: 1.13;
  margin: 40px 0 15px;
  color: #ffffff;
}
h3 {
  font-size: 15px;
  font-weight: 500;
  letter-spacing: -0.15px;
  line-height: 1.4;
  color: #999999;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 15px;
}
h4 {
  font-size: 15px;
  font-weight: 500;
  margin-bottom: 8px;
  color: #ffffff;
  letter-spacing: -0.15px;
}

.subtitle {
  color: #999999;
  font-size: 13px;
  font-weight: 500;
  letter-spacing: -0.13px;
  margin-bottom: 30px;
}

/* ── Score Card (Gradient Spotlight) ── */
.score-card {
  background: linear-gradient(135deg, #141414, #1c1c1c);
  border: 1px solid #262626;
  border-radius: 20px;
  padding: 40px 32px;
  text-align: center;
  margin-bottom: 30px;
  position: relative;
  overflow: hidden;
}
/* Spotlight glow effect */
.score-card::before {
  content: '';
  position: absolute;
  top: -50%; right: -30%;
  width: 300px; height: 300px;
  background: radial-gradient(circle, rgba(106,76,245,0.12) 0%, transparent 70%);
  pointer-events: none;
}
.score-card::after {
  content: '';
  position: absolute;
  bottom: -40%; left: -20%;
  width: 250px; height: 250px;
  background: radial-gradient(circle, rgba(255,122,61,0.08) 0%, transparent 70%);
  pointer-events: none;
}

.big-score {
  font-size: 85px;
  font-weight: 500;
  letter-spacing: -4.25px;
  line-height: 0.95;
  position: relative;
  z-index: 1;
}
.big-score.good { color: #22c55e; }
.big-score.ok { color: #ffffff; }
.big-score.bad { color: #ff5577; }

.score-label {
  font-size: 14px;
  font-weight: 500;
  letter-spacing: -0.14px;
  color: #999999;
  margin-top: 8px;
  position: relative;
  z-index: 1;
}
.freshness-note {
  color: #999999;
  font-size: 12px;
  font-weight: 400;
  letter-spacing: -0.12px;
  margin-top: 8px;
  opacity: 0.6;
}

/* ── Veto Banner (Coral spotlight card) ── */
.veto-banner {
  background: linear-gradient(135deg, #ff5577, #d44df0);
  color: #ffffff;
  padding: 14px 20px;
  border-radius: 15px;
  font-weight: 500;
  font-size: 14px;
  letter-spacing: -0.14px;
  margin-bottom: 20px;
  text-align: center;
}
.veto-item {
  background: rgba(255,85,119,0.08);
  border: 1px solid rgba(255,85,119,0.25);
  padding: 10px 16px;
  border-radius: 10px;
  margin-bottom: 8px;
  font-size: 13px;
  color: #ff5577;
}

/* ── Dimension Bars ── */
.dimension { margin-bottom: 16px; }
.dim-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 6px;
  font-size: 14px;
  letter-spacing: -0.14px;
}
.dim-label { flex: 1; font-weight: 500; }
.dim-weight { color: #999999; margin-right: 15px; font-size: 12px; }
.dim-score { font-weight: 500; min-width: 40px; text-align: right; font-variant-numeric: tabular-nums; }
.bar-bg {
  background: #1c1c1c;
  border-radius: 100px;
  height: 10px;
  overflow: hidden;
}
.bar-fill {
  height: 100%;
  border-radius: 100px;
  transition: width 0.8s ease;
}

/* ── Cards / Sections ── */
.section {
  background: #141414;
  border: 1px solid #262626;
  border-radius: 15px;
  padding: 24px;
  margin-bottom: 15px;
}

/* ── Solution Blocks ── */
.solution-block {
  background: rgba(20,20,20,0.5);
  border-left: 3px solid #0099ff;
  padding: 20px;
  margin: 15px 0;
  border-radius: 0 15px 15px 0;
}
.solution-block h4 { color: #ffffff; }
.solution-block p { font-size: 14px; margin-bottom: 10px; color: #999999; letter-spacing: -0.14px; }
.solution-block ul { margin: 10px 0 10px 20px; font-size: 14px; color: #999999; letter-spacing: -0.14px; }
.solution-block li { margin-bottom: 6px; }

.code-block {
  background: #090909;
  padding: 16px 20px;
  border-radius: 10px;
  font-family: 'SF Mono', 'Fira Code', 'Cascadia Code', monospace;
  font-size: 12px;
  overflow-x: auto;
  color: #ffffff;
  white-space: pre-wrap;
  margin: 10px 0;
  border: 1px solid #262626;
  line-height: 1.5;
}
code {
  background: #1c1c1c;
  padding: 2px 8px;
  border-radius: 6px;
  font-family: monospace;
  font-size: 13px;
  color: #0099ff;
}

/* ── Priority Lists ── */
ul.priority { list-style: none; }
ul.priority li {
  padding: 10px 0;
  border-bottom: 1px solid #1a1a1a;
  font-size: 14px;
  letter-spacing: -0.14px;
  line-height: 1.5;
}
ul.priority li:last-child { border-bottom: none; }
.p0 { color: #ff5577; }
.p1 { color: #ff7a3d; }
.p2 { color: #999999; }

/* ── Check Results Table ── */
.check-item {
  display: flex;
  align-items: center;
  padding: 10px 0;
  border-bottom: 1px solid #1a1a1a;
  font-size: 14px;
  letter-spacing: -0.14px;
}
.check-item:last-child { border-bottom: none; }
.check-icon { margin-right: 12px; font-size: 16px; width: 24px; text-align: center; }
.check-label { flex: 1; font-weight: 500; }
.check-detail {
  color: #999999;
  font-size: 12px;
  margin-right: 15px;
  max-width: 300px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.check-score {
  font-weight: 500;
  font-family: 'SF Mono', monospace;
  font-variant-numeric: tabular-nums;
  min-width: 44px;
  text-align: right;
}

/* ── Footer ── */
.footer {
  text-align: center;
  color: #999999;
  font-size: 12px;
  font-weight: 400;
  letter-spacing: -0.12px;
  margin-top: 60px;
  padding: 24px;
  border-top: 1px solid #1a1a1a;
}
"""


def generate_html(data: dict) -> str:
    url = data.get("url", "N/A")
    domain = urlparse(url).netloc if url != "N/A" else "N/A"
    checks = data.get("checks", {})
    dim_scores = data.get("dim_scores", {})
    overall = data.get("overall", 0)
    veto_hit = data.get("veto_hit", False)
    veto_items = data.get("veto_items", [])
    p0 = data.get("p0", [])
    p1 = data.get("p1", [])
    p2 = data.get("p2", [])
    solutions = data.get("solutions", "")
    ts = datetime.now().strftime("%Y-%m-%d %H:%M UTC")

    # ── dimension bars ──
    dim_bars = ""
    for key, dim in ROSTIDO_DIMENSIONS.items():
        val = dim_scores.get(key, 0)
        icon = score_icon(val)
        dim_bars += f"""
    <div class="dimension">
        <div class="dim-header">
            <span class="dim-label">{icon} {dim['label']}</span>
            <span class="dim-weight">{dim['weight']}%</span>
            <span class="dim-score">{val:.0f}</span>
        </div>
        <div class="bar-bg">
            <div class="bar-fill" style="width:{max(val,0)}%;background:{dim['color']}"></div>
        </div>
    </div>"""

    # ── veto ──
    veto_html = ""
    if veto_items:
        veto_html = '<div class="veto-banner">🚫 VETO ITEMS ACTIVE — overall score capped at 50/100</div>'
        for v in veto_items:
            veto_html += f'<div class="veto-item">❌ {v.get("id","")}: {v.get("detail","")}</div>'

    # ── priority lists ──
    def prio_list(items, cls):
        if not items: return ""
        return "".join(f'<li class="{cls}">{item}</li>' for item in items)

    p0_html = prio_list(p0, "p0")
    p1_html = prio_list(p1, "p1")
    p2_html = prio_list(p2, "p2")

    if not (p0_html or p1_html or p2_html):
        all_ok = '<li style="color:#50B86C;font-weight:600;">✅ No issues found — all checks pass!</li>'
    else:
        all_ok = ""

    # ── check results ──
    checks_html = ""
    for check_name, result in checks.items():
        score = result.get("score")
        icon = check_status_icon(score)
        label = check_name.replace("check_", "").replace("_", " ").title()
        error = result.get("error", "")
        detail = error[:80] if error else ""
        checks_html += f"""
    <div class="check-item">
        <span class="check-icon">{icon}</span>
        <span class="check-label">{label}</span>
        <span class="check-detail">{detail}</span>
        <span class="check-score">{f"{score:.0f}" if score is not None else "N/A"}</span>
    </div>"""

    # ── grade & spotlight ──
    if overall >= 75:
        grade_class = "good"
        spotlight = "violet"
    elif overall >= 50:
        grade_class = "ok"
        spotlight = "orange"
    else:
        grade_class = "bad"
        spotlight = "coral"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ROSTIDO-SCORE Report — {domain}</title>
<style>{CSS}</style>
</head>
<body>
<div class="container">
    <h1>ROSTIDO-SCORE Report</h1>
    <div class="subtitle">{domain} · Generated {ts}</div>

    <div class="score-card">
        <div class="big-score {grade_class}">{overall:.0f}</div>
        <div class="score-label">Overall Score {' (CAPPED)' if veto_hit else ''} /100</div>
        <div class="freshness-note">ROSTIDO-SCORE v2.0 — All checks run live</div>
    </div>

    {veto_html}

    <div class="section">
        <h3>📊 Dimension Scores</h3>
        {dim_bars}
    </div>

    <h2>🔍 Check Results</h2>
    <div class="section">
        {checks_html}
    </div>

    <h2>🎯 Priority Actions</h2>
    {f'<div class="section"><h3 style="color:#E74C3C;">🔴 P0 — Must Fix</h3><ul class="priority">{p0_html}</ul></div>' if p0_html else ''}
    {f'<div class="section"><h3 style="color:#E67E22;">🟡 P1 — Should Fix</h3><ul class="priority">{p1_html}</ul></div>' if p1_html else ''}
    {f'<div class="section"><h3 style="color:#8b949e;">⚪ P2 — Nice to Have</h3><ul class="priority">{p2_html}</ul></div>' if p2_html else ''}
    {f'<div class="section">{all_ok}</div>' if all_ok else ''}

    {f'<h2>🔧 Solutions & Code Examples</h2><div class="section">{solutions}</div>' if solutions else ''}

    <div class="footer">
        ROSTIDO-SCORE Framework v2.0 · github.com/mmriz16/seo-geo-aeo-skill
    </div>
</div>
</body>
</html>"""


# ─── Main ──────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Generate ROSTIDO-SCORE HTML report")
    parser.add_argument("url", nargs="?", help="URL to audit")
    parser.add_argument("--output", default="rostido-report.html", help="Output HTML path")
    parser.add_argument("--open", action="store_true", help="Open in browser")
    args = parser.parse_args()

    if not args.url:
        parser.print_help()
        sys.exit(1)

    # ── Run checks ──
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Running all checks for {args.url}...", file=sys.stderr)
    checks = run_all_checks(args.url, scripts_dir)

    # ── Compute scores ──
    dim_scores = compute_dimension_scores(checks)
    overall = compute_overall(dim_scores)
    veto_hit, veto_items = check_veto(dim_scores, checks)
    p0, p1, p2 = generate_recommendations(dim_scores, checks)
    solutions = generate_solutions_block(checks)

    data = {
        "url": args.url,
        "checks": checks,
        "dim_scores": dim_scores,
        "overall": overall,
        "veto_hit": veto_hit,
        "veto_items": veto_items,
        "p0": p0,
        "p1": p1,
        "p2": p2,
        "solutions": solutions,
    }

    # ── Generate HTML ──
    html = generate_html(data)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(html)

    abs_path = os.path.abspath(args.output)
    print(f"✅ Report generated: {abs_path}", file=sys.stderr)

    if args.open:
        try:
            import webbrowser
            webbrowser.open(f"file://{abs_path}")
        except Exception:
            pass

    # Also print summary to stderr
    print(file=sys.stderr)
    print(f"  Overall: {overall:.0f}/100", file=sys.stderr)
    for k, v in dim_scores.items():
        print(f"  {k}: {v:.0f}/100", file=sys.stderr)
    if veto_hit:
        print(f"  VETO: {len(veto_items)} item(s) active", file=sys.stderr)
    print(f"  P0: {len(p0)} | P1: {len(p1)} | P2: {len(p2)}", file=sys.stderr)


if __name__ == "__main__":
    main()
