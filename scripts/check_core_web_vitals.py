#!/usr/bin/env python3
"""
Fetch Core Web Vitals and performance data from Google PageSpeed Insights API.

Uses the free PSI API v5. No API key required but rate limits apply without one.
Stdlib only (urllib + json).

Usage:
    python check_core_web_vitals.py https://example.com
    python check_core_web_vitals.py https://example.com --strategy mobile
    python check_core_web_vitals.py https://example.com --json
"""

import argparse
import json
import sys
import urllib.request
import urllib.error
import urllib.parse

PSI_API = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
VALID_STRATEGIES = ("mobile", "desktop")

CWV_THRESHOLDS = {
    "LCP": {"good": 2500, "poor": 4000, "unit": "ms", "label": "Largest Contentful Paint"},
    "INP": {"good": 200, "poor": 500, "unit": "ms", "label": "Interaction to Next Paint"},
    "CLS": {"good": 0.1, "poor": 0.25, "unit": "", "label": "Cumulative Layout Shift"},
    "FCP": {"good": 1800, "poor": 3000, "unit": "ms", "label": "First Contentful Paint"},
    "TTFB": {"good": 800, "poor": 1800, "unit": "ms", "label": "Time to First Byte"},
}

PSI_METRIC_MAP = {
    "LARGEST_CONTENTFUL_PAINT_MS": "LCP",
    "INTERACTION_TO_NEXT_PAINT": "INP",
    "CUMULATIVE_LAYOUT_SHIFT_SCORE": "CLS",
    "FIRST_CONTENTFUL_PAINT_MS": "FCP",
    "EXPERIMENTAL_TIME_TO_FIRST_BYTE": "TTFB",
}


def fetch_psi(url: str, strategy: str = "mobile") -> dict:
    """Call PageSpeed Insights API for a URL and strategy."""
    params = urllib.parse.urlencode({
        "url": url,
        "strategy": strategy,
        "category": "PERFORMANCE",
    })
    api_url = f"{PSI_API}?{params}"

    req = urllib.request.Request(api_url, headers={"User-Agent": "SEO-Checker/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return {"error": f"HTTP {e.code}: {body[:200]}"}
    except Exception as e:
        return {"error": str(e)}


def extract_metrics(data: dict) -> dict:
    """Extract CWV metrics from PSI response."""
    if "error" in data:
        return {"error": data["error"]}

    result = {"score": None, "metrics": {}, "opportunities": [], "diagnostics": []}

    try:
        lighthouse = data.get("lighthouseResult", {})
        result["score"] = lighthouse.get("score", None)

        # Numeric metrics
        audits = lighthouse.get("audits", {})
        for psi_name, our_name in PSI_METRIC_MAP.items():
            audit = audits.get(psi_name, {})
            if audit.get("numericValue") is not None:
                value = audit["numericValue"]
                thresholds = CWV_THRESHOLDS[our_name]
                if value <= thresholds["good"]:
                    status = "good"
                elif value <= thresholds["poor"]:
                    status = "needs-improvement"
                else:
                    status = "poor"
                result["metrics"][our_name] = {
                    "value": round(value, 2),
                    "unit": thresholds["unit"],
                    "status": status,
                    "label": thresholds["label"],
                }

        # Loading experience
        loading = data.get("loadingExperience", {})
        metrics_loading = loading.get("metrics", {})
        for psi_name, our_name in PSI_METRIC_MAP.items():
            if psi_name in metrics_loading and our_name not in result["metrics"]:
                mc = metrics_loading[psi_name]
                if mc and mc.get("percentile"):
                    value = mc["percentile"]
                    thresholds = CWV_THRESHOLDS[our_name]
                    if isinstance(value, (int, float)):
                        if value <= thresholds["good"]:
                            status = "good"
                        elif value <= thresholds["poor"]:
                            status = "needs-improvement"
                        else:
                            status = "poor"
                        result["metrics"][our_name] = {
                            "value": round(value, 2),
                            "unit": thresholds["unit"],
                            "status": status,
                            "label": thresholds["label"],
                        }

        # Opportunities
        for audit_id, audit in audits.items():
            if audit.get("details", {}).get("type") == "opportunity":
                result["opportunities"].append({
                    "id": audit_id,
                    "title": audit.get("title", ""),
                    "description": audit.get("description", ""),
                    "wasted_ms": round(audit.get("details", {}).get("overallSavingsMs", 0)),
                })

    except Exception as e:
        result["error"] = f"Parse error: {e}"

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Check Core Web Vitals via PageSpeed Insights API"
    )
    parser.add_argument("url", help="URL to check")
    parser.add_argument("--strategy", choices=VALID_STRATEGIES, default="mobile",
                        help="mobile or desktop (default: mobile)")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    if not args.url.startswith(("http://", "https://")):
        args.url = f"https://{args.url}"

    print(f"Fetching PSI data for {args.url} ({args.strategy})...", file=sys.stderr)
    data = fetch_psi(args.url, args.strategy)

    if "error" in data:
        print(f"API Error: {data['error']}", file=sys.stderr)
        # Maybe still try field data
        data = {"lighthouseResult": {}, "loadingExperience": data.get("loadingExperience", {})}

    result = extract_metrics(data)

    if args.json:
        print(json.dumps(result, indent=2))
        return

    if result.get("error"):
        print(f"\n❌ Error: {result['error']}")
        return

    perf_score = result.get("score")
    if perf_score is not None:
        perf_score = round(perf_score * 100)

    print(f"\n{'='*60}")
    print(f"  Core Web Vitals — {args.url} ({args.strategy})")
    print(f"  Performance Score: {perf_score}/100" if perf_score else "  Performance Score: N/A")
    print(f"{'='*60}\n")

    for name, m in result["metrics"].items():
        icon = {"good": "✅", "needs-improvement": "🟡", "poor": "❌"}.get(m["status"], "⚪")
        unit_str = f" {m['unit']}" if m["unit"] else ""
        print(f"  {icon} {m['label']}: {m['value']}{unit_str} ({m['status']})")

    ops = result.get("opportunities", [])
    if ops:
        print(f"\n  Top Opportunities:")
        for o in sorted(ops, key=lambda x: x["wasted_ms"], reverse=True)[:5]:
            print(f"    🔧 {o['title']} (save ~{o['wasted_ms']}ms)")

    print()


if __name__ == "__main__":
    main()
