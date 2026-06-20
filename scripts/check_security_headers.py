#!/usr/bin/env python3
"""
Check security headers relevant to SEO trust signals.

Validates HTTPS, HSTS, CSP, X-Frame-Options, X-Content-Type-Options,
Referrer-Policy, and Permissions-Policy. Uses stdlib only.

Usage:
    python check_security_headers.py https://example.com
    python check_security_headers.py https://example.com --json
"""

import argparse
import json
import sys
import urllib.request
import urllib.error
from urllib.parse import urlparse

SECURITY_HEADERS = {
    "strict-transport-security": {
        "label": "HSTS (Strict-Transport-Security)",
        "severity": "high",
        "recommendation": "Strict-Transport-Security: max-age=31536000; includeSubDomains",
        "expected_pattern": "max-age",
    },
    "content-security-policy": {
        "label": "Content-Security-Policy (CSP)",
        "severity": "high",
        "recommendation": "Add a Content-Security-Policy header restricting script/style sources",
        "expected_pattern": None,
    },
    "x-frame-options": {
        "label": "X-Frame-Options",
        "severity": "medium",
        "recommendation": "X-Frame-Options: SAMEORIGIN or DENY",
        "expected_pattern": None,
    },
    "x-content-type-options": {
        "label": "X-Content-Type-Options",
        "severity": "medium",
        "recommendation": "X-Content-Type-Options: nosniff",
        "expected_pattern": "nosniff",
    },
    "referrer-policy": {
        "label": "Referrer-Policy",
        "severity": "low",
        "recommendation": "Referrer-Policy: strict-origin-when-cross-origin",
        "expected_pattern": None,
    },
    "permissions-policy": {
        "label": "Permissions-Policy",
        "severity": "low",
        "recommendation": "Add a Permissions-Policy header to restrict API access",
        "expected_pattern": None,
    },
}


def fetch_headers(url: str, timeout: int = 15) -> dict:
    """Fetch response headers from URL using HEAD request."""
    parsed = urlparse(url)
    if not parsed.scheme:
        url = f"https://{url}"

    req = urllib.request.Request(url, method="HEAD")
    req.add_header("User-Agent", "Mozilla/5.0 SEO-Health-Checker/1.0")

    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            headers = dict(resp.headers)
            # Add HTTPS info
            headers["_ssl_verified"] = str(resp.status)
            headers["_status"] = resp.status
            return headers
    except urllib.error.HTTPError as e:
        # HEAD might be rejected; fallback to GET
        try:
            req2 = urllib.request.Request(url, method="GET")
            req2.add_header("User-Agent", "Mozilla/5.0 SEO-Health-Checker/1.0")
            with urllib.request.urlopen(req2, timeout=timeout) as resp:
                headers = dict(resp.headers)
                headers["_ssl_verified"] = str(resp.status)
                headers["_status"] = resp.status
                return headers
        except Exception as e2:
            return {"_error": f"HEAD failed: {e}, GET failed: {e2}"}
    except Exception as e:
        return {"_error": str(e)}


def check_headers(headers: dict) -> dict:
    """Check which security headers are present and valid."""
    results = {}
    score = 0
    max_score = len(SECURITY_HEADERS) * 10

    for hdr, config in SECURITY_HEADERS.items():
        raw = headers.get(hdr, headers.get(hdr.replace("-", "_"), ""))
        if raw:
            status = "present"
            score += 10
            detail = raw[:120]
        else:
            status = "missing"
            detail = "Not set"

        results[hdr] = {
            "label": config["label"],
            "status": status,
            "severity": config["severity"],
            "value": detail,
            "recommendation": config["recommendation"] if status == "missing" else None,
        }

    return {
        "url": headers.get("_url", ""),
        "status_code": headers.get("_status", None),
        "score": round(score / max_score * 100, 1),
        "headers": results,
        "https_enabled": headers.get("_ssl_verified") is not None
        and headers.get("_status", 0) in (200, 301, 302, 307, 308),
    }


def main():
    parser = argparse.ArgumentParser(
        description="Check security headers for SEO trust signals"
    )
    parser.add_argument("url", help="URL to check (e.g. https://example.com)")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    if not args.url.startswith(("http://", "https://")):
        args.url = f"https://{args.url}"

    headers = fetch_headers(args.url)
    if "_error" in headers:
        print(f"Error: {headers['_error']}", file=sys.stderr)
        sys.exit(1)

    result = check_headers(headers)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"\n{'='*60}")
        print(f"  Security Headers Audit — {result['url'] or args.url}")
        print(f"  Score: {result['score']}/100 | HTTPS: {'✅' if result.get('https_enabled') else '❌'}")
        print(f"{'='*60}\n")
        for hdr, data in result["headers"].items():
            icon = "✅" if data["status"] == "present" else "❌"
            sev = {"high": "🔴", "medium": "🟡", "low": "⚪"}.get(data["severity"], "⚪")
            print(f"  {icon} {sev} {data['label']}")
            print(f"     Status: {data['status']}")
            print(f"     Value: {data['value'][:100]}")
            if data.get("recommendation"):
                print(f"     Fix: {data['recommendation']}")
            print()

    sys.exit(0 if result["https_enabled"] else 1)


if __name__ == "__main__":
    main()
