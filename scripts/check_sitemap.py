#!/usr/bin/env python3
"""
Check XML sitemap validity and coverage.

Fetches sitemap from robots.txt or /sitemap.xml, parses URLs,
reports stats. Supports nested sitemap indexes (one level deep).
Stdlib only (urllib + xml.etree.ElementTree).

Usage:
    python check_sitemap.py https://example.com
    python check_sitemap.py https://example.com --json
"""

import argparse
import io
import json
import sys
import urllib.request
import urllib.error
import urllib.robotparser
import xml.etree.ElementTree as ET
from urllib.parse import urlparse, urljoin

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"


def fetch_xml(url: str, timeout: int = 15) -> tuple:
    """Fetch and parse XML from URL. Returns (root, raw_text) or (None, error)."""
    req = urllib.request.Request(url, headers={"User-Agent": "SEO-Checker/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            return ET.fromstring(raw), raw.decode("utf-8", errors="replace")
    except Exception as e:
        return None, str(e)


def find_sitemap_url(url: str) -> str:
    """Find sitemap URL from robots.txt or default location."""
    parsed = urlparse(url)
    base = f"{parsed.scheme}://{parsed.netloc}"

    # Try robots.txt first
    robots_url = f"{base}/robots.txt"
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
        # Check site_maps() method
        sitemaps = []
        try:
            req = urllib.request.Request(robots_url, headers={"User-Agent": "SEO-Checker/1.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                text = resp.read().decode("utf-8", errors="replace")
                for line in text.splitlines():
                    if line.lower().startswith("sitemap:"):
                        parts = line.split(":", 1)
                        if len(parts) > 1:
                            sitemaps.append(parts[1].strip())
        except Exception:
            pass
        if sitemaps:
            return sitemaps[0]
    except Exception:
        pass

    # Fallback to default location
    return f"{base}/sitemap.xml"


def parse_sitemap(root) -> dict:
    """Parse a sitemap or sitemap index XML."""
    urls = []
    sitemaps = []

    # Check if it's a sitemap index
    for child in root:
        tag = child.tag
        if tag.endswith("sitemap"):
            loc = child.find(f"{SITEMAP_NS}loc")
            if loc is not None and loc.text:
                sitemaps.append(loc.text)
        elif tag.endswith("url"):
            loc = child.find(f"{SITEMAP_NS}loc")
            lastmod = child.find(f"{SITEMAP_NS}lastmod")
            changefreq = child.find(f"{SITEMAP_NS}changefreq")
            priority = child.find(f"{SITEMAP_NS}priority")

            url_entry = {
                "loc": loc.text if loc is not None else "",
                "lastmod": lastmod.text if lastmod is not None else None,
                "changefreq": changefreq.text if changefreq is not None else None,
                "priority": float(priority.text) if priority is not None and priority.text else None,
            }
            urls.append(url_entry)

    return {
        "is_index": len(sitemaps) > 0,
        "url_count": len(urls),
        "sitemap_count": len(sitemaps),
        "sitemaps": sitemaps,
        "urls": urls,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Check XML sitemap validity and coverage"
    )
    parser.add_argument("url", help="URL to check")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    if not args.url.startswith(("http://", "https://")):
        args.url = f"https://{args.url}"

    sitemap_url = find_sitemap_url(args.url)

    root, error_or_text = fetch_xml(sitemap_url)

    result = {
        "url": args.url,
        "sitemap_url": sitemap_url,
        "found": root is not None,
    }

    if root is None:
        result["error"] = error_or_text
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"\n❌ Sitemap not found at {sitemap_url}")
            print(f"   Error: {error_or_text}")
        sys.exit(1)

    parsed = parse_sitemap(root)

    score = 0
    max_score = 30

    # Score: exists and valid XML
    score += 10

    # Score: has URLs or child sitemaps
    if parsed["url_count"] > 0 or parsed["sitemap_count"] > 0:
        score += 10
    else:
        score += 0

    # Score: has lastmod dates
    urls_with_dates = sum(1 for u in parsed["urls"] if u.get("lastmod"))
    if parsed["url_count"] > 0:
        if urls_with_dates / parsed["url_count"] > 0.5:
            score += 10
        elif urls_with_dates > 0:
            score += 5

    result.update({
        "score": round(score / max_score * 100, 1),
        "is_index": parsed["is_index"],
        "url_count": parsed["url_count"],
        "sitemap_count": parsed["sitemap_count"],
        "child_sitemaps": parsed["sitemaps"],
        "sample_urls": [u["loc"] for u in parsed["urls"][:10]],
        "urls_with_lastmod": urls_with_dates,
    })

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"\n{'='*60}")
        print(f"  Sitemap Audit — {result['sitemap_url']}")
        print(f"  Score: {result['score']}/100")
        print(f"{'='*60}\n")
        print(f"  Status: {'✅ Found' if result['found'] else '❌ Not found'}")
        if result["is_index"]:
            print(f"  Type: Sitemap index")
            print(f"  Child sitemaps: {result['sitemap_count']}")
            for s in result["child_sitemaps"][:5]:
                print(f"    - {s}")
        else:
            print(f"  Type: Single sitemap")
            print(f"  URLs: {result['url_count']}")
            print(f"  URLs with lastmod: {result['urls_with_lastmod']}")
            print(f"  Sample URLs:")
            for u in result["sample_urls"][:5]:
                print(f"    - {u}")

    sys.exit(0 if result["found"] else 1)


if __name__ == "__main__":
    main()
