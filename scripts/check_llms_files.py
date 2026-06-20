#!/usr/bin/env python3
"""
Check AI-readiness files at site root: /llms.txt, /pricing.md, /AGENTS.md.

Fetches each path, reports HTTP status and content stats.
Stdlib only (urllib).

Usage:
    python check_llms_files.py https://example.com
    python check_llms_files.py https://example.com --json
"""

import argparse
import io
import json
import sys
import urllib.request
import urllib.error

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

FILES_TO_CHECK = [
    {
        "path": "/llms.txt",
        "label": "llms.txt",
        "purpose": "AI context file (llmstxt.org spec)",
        "min_chars": 50,
    },
    {
        "path": "/pricing.md",
        "label": "pricing.md",
        "purpose": "Structured pricing for AI agents",
        "min_chars": 100,
    },
    {
        "path": "/AGENTS.md",
        "label": "AGENTS.md",
        "purpose": "Agent capability description",
        "min_chars": 50,
    },
]


def fetch_file(base_url: str, path: str, timeout: int = 10) -> dict:
    """Fetch a single file from the site root."""
    url = base_url.rstrip("/") + path
    req = urllib.request.Request(url, method="GET", headers={
        "User-Agent": "SEO-Checker/1.0",
        "Accept": "text/markdown, text/plain, */*",
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            content = resp.read().decode("utf-8", errors="replace")
            return {
                "url": url,
                "status": resp.status,
                "content_length": len(content),
                "content_preview": content[:300] if content else "",
                "exists": resp.status == 200,
            }
    except urllib.error.HTTPError as e:
        return {
            "url": url,
            "status": e.code,
            "content_length": 0,
            "content_preview": "",
            "exists": False,
            "error": f"HTTP {e.code}",
        }
    except Exception as e:
        return {
            "url": url,
            "status": 0,
            "content_length": 0,
            "content_preview": "",
            "exists": False,
            "error": str(e),
        }


def main():
    parser = argparse.ArgumentParser(
        description="Check AI-readiness files (llms.txt, pricing.md, AGENTS.md)"
    )
    parser.add_argument("url", help="URL to check")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    if not args.url.startswith(("http://", "https://")):
        args.url = f"https://{args.url}"

    results = {}
    score = 0
    max_score = len(FILES_TO_CHECK) * 10

    for f in FILES_TO_CHECK:
        result = fetch_file(args.url, f["path"])
        result["label"] = f["label"]
        result["purpose"] = f["purpose"]
        result["min_chars"] = f["min_chars"]

        if result["exists"] and result["content_length"] >= f["min_chars"]:
            result["quality"] = "good"
            score += 10
        elif result["exists"] and result["content_length"] < f["min_chars"]:
            result["quality"] = "too_short"
            score += 5
        elif result["status"] in (301, 302, 307, 308):
            result["quality"] = "redirected"
            score += 5
        else:
            result["quality"] = "missing"
            score += 0

        results[f["label"]] = result

    overall = {
        "url": args.url,
        "score": round(score / max_score * 100, 1) if max_score else 0,
        "files": results,
    }

    if args.json:
        print(json.dumps(overall, indent=2))
    else:
        print(f"\n{'='*60}")
        print(f"  AI Readiness Files — {args.url}")
        print(f"  Score: {overall['score']}/100")
        print(f"{'='*60}\n")
        for name, data in results.items():
            if data.get("exists"):
                icon = "✅" if data.get("quality") == "good" else "🟡"
            else:
                icon = "❌"
            status_text = f"HTTP {data['status']}" if data["status"] else data.get("error", "unknown")
            print(f"  {icon} {data['label']} ({status_text})")
            print(f"     Purpose: {data['purpose']}")
            if data.get("exists"):
                print(f"     Size: {data['content_length']} chars")
            if data.get("quality") == "too_short":
                print(f"     ⚠️ Too short ({data['content_length']} chars, min {data['min_chars']})")
            print()

    sys.exit(0 if overall["score"] >= 50 else 1)


if __name__ == "__main__":
    main()
