#!/usr/bin/env python3
"""
Extract and validate JSON-LD structured data from a webpage.

Fetches HTML, extracts <script type="application/ld+json"> blocks,
parses JSON, identifies schema types, and validates recommended schemas.

Usage:
    python check_schema.py https://example.com
    python check_schema.py https://example.com --json
"""

import argparse
import io
import json
import re
import sys
import urllib.request
import urllib.error

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

RECOMMENDED_SCHEMAS = {
    "Organization": {
        "priority": "high",
        "description": "Brand identity in Knowledge Graph",
        "required_props": ["name", "url"],
    },
    "SoftwareApplication": {
        "priority": "high",
        "description": "SaaS product description",
        "required_props": ["name", "applicationCategory"],
    },
    "FAQPage": {
        "priority": "high",
        "description": "Featured snippet + AI answer extraction",
        "required_props": ["mainEntity"],
    },
    "WebSite": {
        "priority": "medium",
        "description": "Site name in search results",
        "required_props": ["name", "url"],
    },
    "Product": {
        "priority": "medium",
        "description": "Product details + offers",
        "required_props": ["name"],
    },
    "Article": {
        "priority": "medium",
        "description": "Blog/news articles",
        "required_props": ["headline", "author"],
    },
    "HowTo": {
        "priority": "medium",
        "description": "Step-by-step guides",
        "required_props": ["step"],
    },
    "BreadcrumbList": {
        "priority": "low",
        "description": "Breadcrumb in SERP",
        "required_props": ["itemListElement"],
    },
    "speakable": {
        "priority": "low",
        "description": "Voice/text-to-speech optimization",
        "required_props": ["cssSelector"],
    },
    "Review": {
        "priority": "low",
        "description": "Star ratings in SERP",
        "required_props": ["itemReviewed", "reviewRating"],
    },
}


def fetch_html(url: str, timeout: int = 15) -> str:
    """Fetch HTML content from URL."""
    parsed = urllib.parse.urlparse(url)
    if not parsed.scheme:
        url = f"https://{url}"

    req = urllib.request.Request(url, headers={"User-Agent": "SEO-Checker/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        return ""


def extract_jsonld(html: str) -> list:
    """Extract all JSON-LD blocks from HTML."""
    schemas = []
    pattern = re.compile(
        r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        re.IGNORECASE | re.DOTALL,
    )
    for match in pattern.finditer(html):
        raw = match.group(1).strip()
        try:
            data = json.loads(raw)
            if isinstance(data, list):
                schemas.extend(data)
            else:
                schemas.append(data)
        except json.JSONDecodeError:
            schemas.append({"@type": "PARSE_ERROR", "_raw": raw[:200]})
    return schemas


def check_recommended(schemas: list) -> dict:
    """Check which recommended schemas are present and valid."""
    found_types = set()
    for s in schemas:
        types = s.get("@type", s.get("type", ""))
        if isinstance(types, list):
            found_types.update(types)
        else:
            found_types.add(types)

    results = {}
    for schema_type, config in RECOMMENDED_SCHEMAS.items():
        if schema_type in found_types:
            # Find the matching schema to check required props
            matching = [s for s in schemas if s.get("@type") == schema_type or
                       (isinstance(s.get("@type"), list) and schema_type in s["@type"])]
            props_present = []
            props_missing = []
            if matching:
                for prop in config["required_props"]:
                    if prop in matching[0]:
                        props_present.append(prop)
                    else:
                        props_missing.append(prop)

            status = "present" if not props_missing else "incomplete"
            results[schema_type] = {
                "status": status,
                "count": len(matching),
                "required_props_present": props_present,
                "required_props_missing": props_missing,
            }
        else:
            results[schema_type] = {
                "status": "missing",
                "count": 0,
                "required_props_present": [],
                "required_props_missing": config["required_props"],
            }

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Extract and validate JSON-LD structured data"
    )
    parser.add_argument("url", help="URL to check")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    if not args.url.startswith(("http://", "https://")):
        args.url = f"https://{args.url}"

    html = fetch_html(args.url)
    schemas = extract_jsonld(html)
    recommendations = check_recommended(schemas)

    # Count high-priority coverage
    high_priority = [t for t, c in RECOMMENDED_SCHEMAS.items() if c["priority"] == "high"]
    high_found = sum(1 for t in high_priority if recommendations.get(t, {}).get("status") != "missing")
    score = round((high_found / len(high_priority)) * 100, 1) if high_priority else 0

    result = {
        "url": args.url,
        "total_schemas_found": len(schemas),
        "score": score,
        "schemas": schemas[:10],  # limit output
        "recommendations": recommendations,
    }

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print(f"\n{'='*60}")
        print(f"  Schema Audit — {args.url}")
        print(f"  Score: {result['score']}/100 | Schemas found: {len(schemas)}")
        print(f"{'='*60}\n")

        for schema_type, data in recommendations.items():
            icon = {"present": "✅", "incomplete": "🟡", "missing": "❌"}.get(data["status"], "⚪")
            prio = {"high": "🔴", "medium": "🟡", "low": "⚪"}.get(
                RECOMMENDED_SCHEMAS.get(schema_type, {}).get("priority", "low"), "⚪"
            )
            print(f"  {icon} [{prio}] {schema_type} ({data['status']})")
            if data["required_props_missing"]:
                print(f"     Missing: {', '.join(data['required_props_missing'])}")

        if schemas:
            print(f"\n  Raw Schemas Found:")
            for i, s in enumerate(schemas[:5], 1):
                stype = s.get("@type", "unknown")
                print(f"    {i}. {stype}")

    sys.exit(0 if result["score"] >= 50 else 1)


if __name__ == "__main__":
    main()
