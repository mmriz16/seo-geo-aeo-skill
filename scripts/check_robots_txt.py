#!/usr/bin/env python3
"""
Check robots.txt for SEO and AI crawler management.

Parses robots.txt, validates AI bot rules, checks sitemap directives.
Uses stdlib only (urllib.robotparser).

Usage:
    python check_robots_txt.py https://example.com
    python check_robots_txt.py https://example.com --json
"""

import argparse
import io
import json
import sys
import urllib.robotparser
import urllib.request
import urllib.error
from urllib.parse import urlparse

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

AI_CRAWLERS = [
    "GPTBot",
    "ChatGPT-User",
    "ClaudeBot",
    "PerplexityBot",
    "Google-Extended",
    "anthropic-ai",
    "Applebot-Extended",
    "Bytespider",
    "CCBot",
    "FacebookBot",
]

RECOMMENDED_ALLOW = [
    "GPTBot",
    "ChatGPT-User",
    "ClaudeBot",
    "PerplexityBot",
    "Google-Extended",
]

RECOMMENDED_DISALLOW = [
    "CCBot",
    "Bytespider",
]


def fetch_robots(url: str, timeout: int = 15) -> tuple:
    """Fetch and parse robots.txt from a domain. Returns (rp, raw_text, robots_url)."""
    parsed = urlparse(url)
    if not parsed.scheme:
        url = f"https://{url}"
        parsed = urlparse(url)

    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) SEO-Checker/1.0"

    # Manually fetch with a browser-like UA (Cloudflare blocks Python-urllib)
    try:
        req = urllib.request.Request(robots_url, headers={"User-Agent": user_agent})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw_text = resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        return None, None, robots_url, str(e)

    # Parse into RobotFileParser
    rp = urllib.robotparser.RobotFileParser()
    rp.parse(raw_text)

    return rp, raw_text, robots_url, None


def extract_sitemaps(raw_text: str) -> list:
    """Extract Sitemap directives from robots.txt."""
    sitemaps = []
    if not raw_text:
        return sitemaps
    for line in raw_text.splitlines():
        if line.lower().startswith("sitemap:"):
            parts = line.split(":", 1)
            if len(parts) > 1:
                sitemaps.append(parts[1].strip())
    return sitemaps


def check_ai_bots(rp: urllib.robotparser.RobotFileParser, test_url: str = "/") -> dict:
    """Check if AI crawlers are explicitly managed."""
    results = {}
    for bot in AI_CRAWLERS:
        try:
            allowed = rp.can_fetch(bot, test_url)
            results[bot] = "allowed" if allowed else "disallowed"
        except Exception:
            results[bot] = "unknown"
    return results


def main():
    parser = argparse.ArgumentParser(
        description="Check robots.txt for SEO and AI crawler management"
    )
    parser.add_argument("url", help="URL to check")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    rp, raw_text, robots_url, error = fetch_robots(args.url)

    result = {
        "url": args.url,
        "robots_url": robots_url,
        "exists": rp is not None,
        "error": error,
    }

    if rp is None:
        result["status"] = "error"
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"❌ Error: robots.txt not found or unreachable")
            print(f"   {robots_url}")
            if error:
                print(f"   {error}")
        sys.exit(1)

    sitemaps = extract_sitemaps(raw_text)
    ai_bots = check_ai_bots(rp)

    score = 0
    max_score = 30

    # Score: exists
    score += 10

    # Score: has sitemap directive
    if sitemaps:
        score += 10
    else:
        sitemaps = ["(not found in robots.txt)"]

    # Score: recommended AI bots allowed
    allowed_count = sum(1 for bot in RECOMMENDED_ALLOW if ai_bots.get(bot) == "allowed")
    score += int((allowed_count / len(RECOMMENDED_ALLOW)) * 10)

    bot_warnings = []
    for bot in RECOMMENDED_DISALLOW:
        if ai_bots.get(bot) != "disallowed":
            bot_warnings.append(f"Consider disallowing {bot} (training-only crawler)")

    result.update({
        "score": round(score / max_score * 100, 1),
        "sitemaps": sitemaps,
        "ai_bots": ai_bots,
        "warnings": bot_warnings,
        "user_agents_count": raw_text.count("User-agent:") if raw_text else 0,
        "raw_length": len(raw_text) if raw_text else 0,
    })

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"\n{'='*60}")
        print(f"  Robots.txt Audit — {robots_url}")
        print(f"  Score: {result['score']}/100")
        print(f"{'='*60}\n")
        print(f"  Status: {'✅ Found' if result['exists'] else '❌ Not found'}")
        print(f"  User-agent rules: {result['user_agents_count']}")
        print(f"  Sitemaps: {len(sitemaps)} found")
        for s in sitemaps[:3]:
            print(f"    {s}")
        print(f"\n  AI Crawler Rules:")
        for bot, status in ai_bots.items():
            icon = "✅" if status == "allowed" else "❌" if status == "disallowed" else "⚠️"
            print(f"    {icon} {bot}: {status}")
        for w in bot_warnings:
            print(f"\n  ⚠️ {w}")

    sys.exit(0 if result["exists"] else 1)


if __name__ == "__main__":
    main()
