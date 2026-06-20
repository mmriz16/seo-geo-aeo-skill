#!/usr/bin/env python3
"""
Generate interactive HTML report from SEO audit data.

Takes JSON input from any of the check_* scripts and produces a
self-contained HTML report with scoring visualization.
Can also run all checks and aggregate results.

Usage:
    # From existing JSON
    python generate_score_report.py --input scores.json --output report.html

    # Run all checks and generate report
    python generate_score_report.py https://example.com --output report.html
    python generate_score_report.py https://example.com --output report.html --open
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
from datetime import datetime
from urllib.parse import urlparse

import urllib.request
import urllib.error

# ROSTIDO-SCORE dimension definitions
ROSTIDO_DIMENSIONS = {
    "technical": {
        "label": "Technical SEO",
        "weight": 20,
        "color": "#4A90D9",
        "max": 100,
    },
    "content": {
        "label": "Content & Authority",
        "weight": 20,
        "color": "#50B86C",
        "max": 100,
    },
    "entity": {
        "label": "Entity & Knowledge Graph",
        "weight": 15,
        "color": "#9B59B6",
        "max": 100,
    },
    "geo": {
        "label": "GEO-readiness",
        "weight": 20,
        "color": "#E67E22",
        "max": 100,
    },
    "aeo": {
        "label": "AEO-readiness",
        "weight": 15,
        "color": "#E74C3C",
        "max": 100,
    },
    "trust": {
        "label": "Trust & Security",
        "weight": 10,
        "color": "#1ABC9C",
        "max": 100,
    },
}

VETO_ITEMS = ["sitemap", "canonicals", "https", "llms_txt", "org_schema", "faq_schema", "schema_valid"]


def run_check(script_path: str, url: str) -> dict:
    """Run a check script and return parsed JSON result."""
    try:
        result = subprocess.run(
            [sys.executable, script_path, url, "--json"],
            capture_output=True, text=True, timeout=30,
        )
        if result.returncode == 0 and result.stdout.strip():
            return json.loads(result.stdout)
        return {"error": result.stderr[:200] or "no output"}
    except Exception as e:
        return {"error": str(e)}


def run_all_checks(url: str, scripts_dir: str) -> dict:
    """Run all check scripts and aggregate results."""
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
        if os.path.exists(path):
            checks[name.replace(".py", "")] = run_check(path, url)
        else:
            checks[name.replace(".py", "")] = {"error": f"Script not found: {path}"}

    return checks


def load_input(path: str) -> dict:
    """Load JSON input from file."""
    with open(path, "r") as f:
        return json.load(f)


def generate_html(data: dict) -> str:
    """Generate self-contained HTML report."""
    url = data.get("url", "N/A")
    domain = urlparse(url).netloc if url != "N/A" else "N/A"
    score = data.get("score", {})
    dimensions = score.get("dimensions", {})
    overall = score.get("overall", 0)
    veto_hit = score.get("veto_hit", False)
    veto_items = score.get("veto_items", [])
    p0 = data.get("p0_fixes", [])
    p1 = data.get("p1_fixes", [])
    checks = data.get("checks", {})

    ts = datetime.now().strftime("%Y-%m-%d %H:%M UTC")

    # Build dimension bars HTML
    dim_bars = ""
    for key, dim in ROSTIDO_DIMENSIONS.items():
        val = dimensions.get(key, 0)
        dim_bars += f"""
        <div class="dimension">
            <div class="dim-header">
                <span class="dim-label">{dim['label']}</span>
                <span class="dim-weight">{dim['weight']}%</span>
                <span class="dim-score">{val:.1f}</span>
            </div>
            <div class="bar-bg">
                <div class="bar-fill" style="width:{val}%;background:{dim['color']}"></div>
            </div>
        </div>"""

    # Build veto items
    veto_html = ""
    if veto_items:
        veto_html = '<div class="veto-banner">🚫 VETO ITEMS ACTIVE (score capped at 50)</div>'
        for v in veto_items:
            veto_html += f'<div class="veto-item">❌ {v.get("id", "")}: {v.get("detail", "")}</div>'

    # Build P0/P1 lists
    p0_html = "".join(f'<li>{item}</li>' for item in p0[:10])
    p1_html = "".join(f'<li>{item}</li>' for item in p1[:10])

    # Build check results summary
    checks_html = ""
    for name, result in checks.items():
        status = "✅" if "error" not in result else "❌"
        label = name.replace("check_", "").replace("_", " ").title()
        score_val = result.get("score", "N/A")
        checks_html += f"""
        <div class="check-item">
            <span class="check-status">{status}</span>
            <span class="check-label">{label}</span>
            <span class="check-score">{score_val}</span>
        </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ROSTIDO-SCORE Report — {domain}</title>
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif; background:#0f1117; color:#e1e4e8; line-height:1.5; }}
.container {{ max-width:960px; margin:0 auto; padding:24px 16px; }}
h1 {{ font-size:28px; margin-bottom:4px; }}
h2 {{ font-size:20px; margin:24px 0 12px; color:#8b949e; }}
.subtitle {{ color:#8b949e; font-size:14px; margin-bottom:24px; }}
.score-card {{ background:#161b22; border:1px solid #30363d; border-radius:12px; padding:24px; text-align:center; margin-bottom:24px; }}
.big-score {{ font-size:64px; font-weight:700; }}
.big-score.good {{ color:#50B86C; }}
.big-score.ok {{ color:#E67E22; }}
.big-score.bad {{ color:#E74C3C; }}
.score-label {{ font-size:16px; color:#8b949e; }}
.veto-banner {{ background:#E74C3C; color:#fff; padding:12px 16px; border-radius:8px; font-weight:600; margin-bottom:12px; }}
.veto-item {{ background:rgba(231,76,60,.1); border:1px solid #E74C3C; padding:8px 12px; border-radius:6px; margin-bottom:6px; font-size:14px; }}
.dimension {{ margin-bottom:16px; }}
.dim-header {{ display:flex; justify-content:space-between; margin-bottom:4px; font-size:14px; }}
.dim-label {{ flex:1; }}
.dim-weight {{ color:#8b949e; margin-right:16px; }}
.dim-score {{ font-weight:600; min-width:40px; text-align:right; }}
.bar-bg {{ background:#21262d; border-radius:8px; height:12px; overflow:hidden; }}
.bar-fill {{ height:100%; border-radius:8px; transition:width .5s; }}
.section {{ background:#161b22; border:1px solid #30363d; border-radius:12px; padding:20px; margin-bottom:16px; }}
.section h3 {{ margin-bottom:12px; font-size:16px; color:#8b949e; text-transform:uppercase; letter-spacing:.5px; }}
ul.priority {{ list-style:none; }}
ul.priority li {{ padding:8px 0; border-bottom:1px solid #21262d; font-size:14px; }}
ul.priority li:last-child {{ border-bottom:none; }}
.check-item {{ display:flex; align-items:center; padding:8px 0; border-bottom:1px solid #21262d; font-size:14px; }}
.check-item:last-child {{ border-bottom:none; }}
.check-status {{ margin-right:12px; font-size:16px; }}
.check-label {{ flex:1; }}
.check-score {{ color:#8b949e; font-family:monospace; }}
.footer {{ text-align:center; color:#484f58; font-size:12px; margin-top:32px; padding:16px; }}
</style>
</head>
<body>
<div class="container">
    <h1>ROSTIDO-SCORE Report</h1>
    <div class="subtitle">{domain} · Generated {ts}</div>

    <div class="score-card">
        <div class="big-score {'good' if overall >= 75 else 'ok' if overall >= 50 else 'bad'}">{overall:.1f}</div>
        <div class="score-label">Overall Score {' (CAPPED)' if veto_hit else ''}/100</div>
    </div>

    {veto_html}

    <div class="section">
        <h3>📊 Dimension Scores</h3>
        {dim_bars}
    </div>

    <div class="section">
        <h3>🔴 Priority P0 — Must Fix</h3>
        <ul class="priority">{p0_html}</ul>
    </div>

    <div class="section">
        <h3>🟡 Priority P1 — Should Fix</h3>
        <ul class="priority">{p1_html}</ul>
    </div>

    <div class="section">
        <h3>🔍 Automated Checks</h3>
        {checks_html}
    </div>

    <div class="footer">
        ROSTIDO-SCORE Framework v2.0 · SEO-GEO-AEO Skill
    </div>
</div>
</body>
</html>"""


def main():
    parser = argparse.ArgumentParser(
        description="Generate ROSTIDO-SCORE HTML report from SEO audit data"
    )
    parser.add_argument("url", nargs="?", help="URL to audit (runs all checks)")
    parser.add_argument("--input", help="Input JSON file (skip live checks)")
    parser.add_argument("--output", default="rostido-report.html", help="Output HTML path")
    parser.add_argument("--open", action="store_true", help="Open report in browser")
    args = parser.parse_args()

    if args.input:
        # Load from existing JSON
        with open(args.input) as f:
            data = json.load(f)
    elif args.url:
        # Run all checks
        scripts_dir = os.path.dirname(os.path.abspath(__file__))
        print(f"Running all checks for {args.url}...", file=sys.stderr)
        checks = run_all_checks(args.url, scripts_dir)
        data = {
            "url": args.url,
            "checks": checks,
            "score": {"dimensions": {}, "overall": 0, "veto_hit": False, "veto_items": []},
            "p0_fixes": [],
            "p1_fixes": [],
        }

        # Extract scores from checks
        scores = {
            "technical": checks.get("check_security_headers", {}).get("score", 50),
            "content": checks.get("check_robots_txt", {}).get("score", 50),
            "entity": 0,
            "geo": checks.get("check_llms_files", {}).get("score", 50),
            "aeo": checks.get("check_schema", {}).get("score", 50),
            "trust": checks.get("check_security_headers", {}).get("https_enabled", False) and 80 or 30,
        }

        # Manual scores for dimensions not covered by scripts
        # (entity needs manual check - Wikidata, sameAs, etc.)
        data["score"]["dimensions"] = scores

        # Calculate weighted overall
        overall = 0
        for key, dim in ROSTIDO_DIMENSIONS.items():
            overall += scores.get(key, 0) * (dim["weight"] / 100)
        data["score"]["overall"] = round(overall, 1)

        # Veto check
        data["score"]["veto_hit"] = overall < 30

        # Generate P0/P1 from analysis
        if scores.get("technical", 0) < 60:
            data["p0_fixes"].append("Fix technical SEO: sitemap, canonicals, HTTPS")
        if scores.get("geo", 0) < 50:
            data["p0_fixes"].append("Add llms.txt and pricing.md to site root")
        if scores.get("aeo", 0) < 50:
            data["p0_fixes"].append("Add FAQPage JSON-LD with visible FAQ content")
        if scores.get("entity", 0) < 50:
            data["p1_fixes"].append("Create Organization JSON-LD and Wikidata entry")
        if scores.get("trust", 0) < 60:
            data["p0_fixes"].append("Fix security headers: HSTS, CSP, X-Frame-Options")
    else:
        parser.print_help()
        sys.exit(1)

    html = generate_html(data)

    with open(args.output, "w") as f:
        f.write(html)

    print(f"✅ Report generated: {args.output}", file=sys.stderr)

    if args.open:
        try:
            import webbrowser
            webbrowser.open(f"file://{os.path.abspath(args.output)}")
        except Exception:
            pass


if __name__ == "__main__":
    main()
