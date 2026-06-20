#!/usr/bin/env python3
"""
Check AI visibility across ChatGPT, Perplexity, Gemini, and AI Overviews.

This script is interactive/manual-assisted — it prompts you to check each
platform and enter results. Use it to track citation status month-over-month.

Usage:
    # Interactive mode with built-in queries
    python check_ai_visibility.py

    # With custom query file (one query per line)
    python check_ai_visibility.py --queries queries.txt

    # Output as JSON (for chaining into reports)
    python check_ai_visibility.py --json > visibility.json

    # Quick run: just show the template
    python check_ai_visibility.py --template
"""

import argparse
import io
import json
import os
import sys
from datetime import datetime

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

TRACKER_PATH = os.path.join(os.path.dirname(__file__), "..", "ai_visibility_tracker.json")

PLATFORMS = ["ChatGPT", "Perplexity", "Gemini", "AI Overviews"]

DEFAULT_QUERIES = [
    "social media automation",
    "best social media management tools 2026",
    "automate instagram comments",
    "social media scheduling tool",
    "social media management pricing",
]


def load_tracker() -> dict:
    """Load existing tracker data if available."""
    path = os.path.expanduser(TRACKER_PATH) if "~" in TRACKER_PATH else TRACKER_PATH
    if os.path.exists(path):
        try:
            with open(path) as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {"queries": [], "history": []}
    return {"queries": [], "history": []}


def save_tracker(data: dict):
    """Save tracker data."""
    path = os.path.expanduser(TRACKER_PATH) if "~" in TRACKER_PATH else TRACKER_PATH
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"  💾 Saved to {path}")


def interactive_check(queries: list[str]) -> dict:
    """Run interactive citation check for each query."""
    month = datetime.now().strftime("%Y-%m")
    results = []

    print(f"\n{'='*60}")
    print(f"  AI Visibility Check — {month}")
    print(f"  Check each query and enter results for each platform.")
    print(f"  Enter: y (cited), n (not cited), s (skip), q (quit)")
    print(f"{'='*60}\n")

    for i, query in enumerate(queries, 1):
        print(f"\n[{i}/{len(queries)}] Query: {query}")
        print(f"{'-'*40}")

        platform_results = {}
        for platform in PLATFORMS:
            while True:
                try:
                    answer = input(f"  {platform}: ").strip().lower()
                except (EOFError, KeyboardInterrupt):
                    print("\n  Quitting...")
                    return {"month": month, "queries": results, "status": "incomplete"}

                if answer == "q":
                    return {"month": month, "queries": results, "status": "incomplete"}
                elif answer in ("y", "yes"):
                    platform_results[platform] = "cited"
                    break
                elif answer in ("n", "no"):
                    platform_results[platform] = "not_cited"
                    break
                elif answer == "s":
                    platform_results[platform] = "skipped"
                    break
                else:
                    print("    Please enter y, n, s, or q")

        results.append({
            "query": query,
            "platforms": platform_results,
        })

    # Trend: compare with previous month
    prev_results = load_tracker()

    return {
        "month": month,
        "queries": results,
        "previous_month": prev_results.get("month"),
        "status": "complete",
    }


def print_tracker(data: dict, show_table: bool = True):
    """Print tracker results in a readable format."""
    month = data.get("month", "unknown")
    queries = data.get("queries", [])

    if show_table and queries:
        print(f"\n{'='*60}")
        print(f"  AI Visibility Tracker — {month}")
        print(f"{'='*60}\n")

        # Header
        header = f"  {'Query':<45} |"
        for p in PLATFORMS:
            header += f" {p:<14} |"
        print(header)
        print(f"  {'-'*45}-+-{'-'*15}-+-{'-'*15}-+-{'-'*14}-+-{'-'*14}")

        for q in queries:
            query = q["query"][:43]
            row = f"  {query:<45} |"
            for p in PLATFORMS:
                status = q.get("platforms", {}).get(p, "?")
                icon = {"cited": "✅", "not_cited": "❌", "skipped": "⬜"}.get(status, "❓")
                row += f" {icon:<14} |"
            print(row)

        # Summary
        total = len(queries)
        cited_any = sum(
            1 for q in queries
            if any(v == "cited" for v in q.get("platforms", {}).values())
        )
        print(f"\n  Cited on at least 1 platform: {cited_any}/{total}")
        for p in PLATFORMS:
            count = sum(1 for q in queries if q.get("platforms", {}).get(p) == "cited")
            print(f"  {p}: {count}/{total}")

    print()


def print_template():
    """Print a template for tracking."""
    print(f"""\
# AI Visibility Tracker — {datetime.now().strftime('%Y-%m')}

| # | Query | ChatGPT | Perplexity | Gemini | AI Overviews | Trend | Notes |
|---|-------|:-------:|:----------:|:------:|:------------:|:-----:|-------|
{"".join(f'| {i} | "{q}" | ❌ | ❌ | ❌ | ❌ | — | |\n' for i, q in enumerate(DEFAULT_QUERIES[:10], 1))}

## Legend
✅ = Cited as source  ❌ = Not cited  N/A = Not applicable
↑↑ = Improved  ↑ = Slightly  → = No change  ↓ = Dropped
""")


def main():
    parser = argparse.ArgumentParser(
        description="Check AI visibility across ChatGPT, Perplexity, Gemini, AI Overviews"
    )
    parser.add_argument("--queries", help="File with one query per line")
    parser.add_argument("--json", action="store_true", help="Output JSON only")
    parser.add_argument("--template", action="store_true", help="Print tracker template")
    parser.add_argument("--view", action="store_true", help="View existing tracker data")
    args = parser.parse_args()

    if args.template:
        print_template()
        return

    if args.view:
        data = load_tracker()
        if data.get("queries"):
            print_tracker(data)
            print(f"  Month: {data.get('month')}")
            print(f"  Previous: {data.get('previous_month', 'none')}")
        else:
            print("No existing tracker data found.")
        return

    # Load queries
    queries = DEFAULT_QUERIES[:]
    if args.queries:
        with open(args.queries) as f:
            queries = [line.strip() for line in f if line.strip()]

    # Run interactive check
    result = interactive_check(queries)
    save_tracker(result)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_tracker(result)


if __name__ == "__main__":
    main()
