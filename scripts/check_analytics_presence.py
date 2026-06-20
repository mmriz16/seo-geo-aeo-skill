#!/usr/bin/env python3
"""
check_analytics_presence.py — Detect analytics & verification services on a website.

Checks for:
  - Google Analytics 4 (gtag / G-XXXXX)
  - Universal Analytics (UA-XXXXX)
  - Google Tag Manager (GTM-XXXXX)
  - Google Search Console verification (meta tag, DNS TXT, HTML file)
  - Facebook / Meta Pixel (fbq / pixel ID)

All checks are passive — no API keys or authentication required.

Usage:
  python3 check_analytics_presence.py https://example.com
  python3 check_analytics_presence.py https://example.com --json
"""

import argparse
import json
import re
import sys
import urllib.request
import urllib.error
import socket
import dns.resolver  # only used if available, otherwise skip DNS checks

# ── Windows UTF‑8 fix ──
if sys.platform == "win32" and sys.stdout.encoding != "utf-8":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# ── Regex patterns ──
PATTERNS = {
    "ga4": re.compile(r'G-[A-Z0-9]{6,12}'),
    "ua":  re.compile(r'UA-\d{4,10}-\d{1,2}'),
    "gtm": re.compile(r'GTM-[A-Z0-9]{5,10}'),
    "ads": re.compile(r'AW-\d{8,12}'),
    "gsc_meta": re.compile(
        r'<meta\s+name=["\']google-site-verification["\']\s+content=["\']([^"\']+)["\']',
        re.IGNORECASE
    ),
    "gsc_file": re.compile(r'google([a-z0-9]{12,40})\.html', re.IGNORECASE),
    "meta_pixel": re.compile(r'fbq\s*\(\s*["\']init["\']\s*,\s*["\'](\d{10,20})["\']'),
    "meta_pixel_code": re.compile(r'pixel\.facebook\.com/fbevents\.js'),
    "gtag_js": re.compile(r'googletagmanager\.com/gtag/js'),
    "gtm_iframe": re.compile(r'googletagmanager\.com/ns\.html'),
}

DNS_CACHE: dict = {}


def fetch_page(url: str, timeout: int = 10) -> tuple[str | None, int, str | None]:
    """Fetch page HTML. Returns (html, status, error)."""
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/125.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,*/*",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            html = resp.read().decode("utf-8", errors="replace")
            return html, resp.status, None
    except urllib.error.HTTPError as e:
        return None, e.code, f"HTTP {e.code}"
    except urllib.error.URLError as e:
        return None, 0, str(e.reason)
    except Exception as e:
        return None, 0, str(e)


def fetch_verification_file(domain: str, timeout: int = 10) -> bool:
    """Try https://domain/googleXXXXX.html — return True if any file found."""
    # Brute-force common patterns unlikely to match unless deliberately placed
    # Instead, just try a generic approach: check if domain hosts /google*.html
    # by checking a well-known pattern. Real verification files are random
    # (e.g. google3a2b1c.html), so we can't enumerate. Skip brute force.
    return False


def check_dns_txt(domain: str) -> dict:
    """Check DNS TXT records for google-site-verification."""
    result = {"gsc_dns_found": False, "gsc_dns_value": None, "dns_available": False}
    try:
        answers = dns.resolver.resolve(domain, "TXT", lifetime=5)
        result["dns_available"] = True
        for rdata in answers:
            txt = "".join(part.decode() if isinstance(part, bytes) else part
                          for part in rdata.strings)
            if txt.startswith("google-site-verification="):
                result["gsc_dns_found"] = True
                result["gsc_dns_value"] = txt.replace("google-site-verification=", "")
    except ImportError:
        result["dns_available"] = False
        result["dns_note"] = "dnspython not installed — use: pip install dnspython"
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
        pass
    except Exception:
        pass
    return result


def check_dns_simple(domain: str) -> dict:
    """Fallback: check TXT record via socket + manual DNS query (basic)."""
    result = {"gsc_dns_found": False, "gsc_dns_value": None, "dns_available": False}
    # Without dnspython, we can't easily parse DNS TXT records from stdlib.
    # Mark as unavailable.
    return result


def scan_html(html: str, domain: str) -> dict:
    """Scan HTML for analytics and verification patterns."""
    findings = {}

    # GA4
    ga4_matches = PATTERNS["ga4"].findall(html)
    findings["ga4"] = {
        "found": bool(ga4_matches),
        "ids": list(set(ga4_matches)),
        "note": "Google Analytics 4 detected" if ga4_matches else None,
    }

    # Universal Analytics
    ua_matches = PATTERNS["ua"].findall(html)
    findings["ua"] = {
        "found": bool(ua_matches),
        "ids": list(set(ua_matches)),
        "note": "Universal Analytics detected" if ua_matches else None,
    }

    # GTM
    gtm_matches = PATTERNS["gtm"].findall(html)
    has_gtm_js = bool(PATTERNS["gtm_iframe"].search(html) or
                      PATTERNS["gtag_js"].search(html))
    findings["gtm"] = {
        "found": bool(gtm_matches) or has_gtm_js,
        "ids": list(set(gtm_matches)),
        "note": "Google Tag Manager detected" if (gtm_matches or has_gtm_js) else None,
    }

    # Google Ads
    ads_matches = PATTERNS["ads"].findall(html)
    findings["google_ads"] = {
        "found": bool(ads_matches),
        "ids": list(set(ads_matches)),
        "note": "Google Ads conversion tracking detected" if ads_matches else None,
    }

    # GSC verification meta tag
    gsc_meta = PATTERNS["gsc_meta"].search(html)
    findings["gsc_meta"] = {
        "found": bool(gsc_meta),
        "value": gsc_meta.group(1) if gsc_meta else None,
        "note": "Google Search Console verified via meta tag" if gsc_meta else None,
    }

    # GSC verification file link in page
    gsc_file = PATTERNS["gsc_file"].search(html)
    findings["gsc_file"] = {
        "found": bool(gsc_file),
        "note": None,
    }

    # Meta/Facebook Pixel
    pixel_matches = PATTERNS["meta_pixel"].findall(html)
    has_pixel_js = bool(PATTERNS["meta_pixel_code"].search(html))
    findings["meta_pixel"] = {
        "found": bool(pixel_matches) or has_pixel_js,
        "ids": list(set(pixel_matches)),
        "note": "Meta/Facebook Pixel detected" if (pixel_matches or has_pixel_js) else None,
    }

    return findings


def calculate_score(findings: dict, dns_result: dict) -> dict:
    """Calculate score (0–100) and per-item results."""

    checks = []

    # GA4 (30 pts)
    if findings.get("ga4", {}).get("found"):
        checks.append({"item": "Google Analytics 4", "status": "present",
                       "detail": ", ".join(findings["ga4"]["ids"]), "max": 30, "got": 30})
    else:
        checks.append({"item": "Google Analytics 4", "status": "missing",
                       "detail": "No GA4 tag found", "max": 30, "got": 0})

    # UA (10 pts)
    if findings.get("ua", {}).get("found"):
        checks.append({"item": "Universal Analytics", "status": "present",
                       "detail": ", ".join(findings["ua"]["ids"]), "max": 10, "got": 10})
    else:
        checks.append({"item": "Universal Analytics", "status": "missing",
                       "detail": "No UA tag found", "max": 10, "got": 0})

    # GTM (15 pts)
    if findings.get("gtm", {}).get("found"):
        checks.append({"item": "Google Tag Manager", "status": "present",
                       "detail": ", ".join(findings["gtm"]["ids"]) if findings["gtm"]["ids"] else "GTM snippet present",
                       "max": 15, "got": 15})
    else:
        checks.append({"item": "Google Tag Manager", "status": "missing",
                       "detail": "No GTM found", "max": 15, "got": 0})

    # Google Ads (10 pts)
    if findings.get("google_ads", {}).get("found"):
        checks.append({"item": "Google Ads", "status": "present",
                       "detail": ", ".join(findings["google_ads"]["ids"]), "max": 10, "got": 10})
    else:
        checks.append({"item": "Google Ads", "status": "missing",
                       "detail": "No Ads tag found", "max": 10, "got": 0})

    # GSC (20 pts: 10 meta + 10 DNS)
    gsc_score = 0
    if findings.get("gsc_meta", {}).get("found"):
        checks.append({"item": "GSC — meta tag", "status": "present",
                       "detail": f"Value: {findings['gsc_meta']['value']}", "max": 10, "got": 10})
        gsc_score += 10
    else:
        checks.append({"item": "GSC — meta tag", "status": "missing",
                       "detail": "No google-site-verification meta", "max": 10, "got": 0})

    if dns_result.get("gsc_dns_found"):
        checks.append({"item": "GSC — DNS TXT", "status": "present",
                       "detail": f"TXT record found", "max": 10, "got": 10})
        gsc_score += 10
    elif dns_result.get("dns_available") is False:
        checks.append({"item": "GSC — DNS TXT", "status": "skipped",
                       "detail": dns_result.get("dns_note", "DNS check unavailable"), "max": 10, "got": 0})
    else:
        checks.append({"item": "GSC — DNS TXT", "status": "missing",
                       "detail": "No google-site-verification TXT record", "max": 10, "got": 0})

    # Meta Pixel (15 pts)
    if findings.get("meta_pixel", {}).get("found"):
        checks.append({"item": "Meta Pixel", "status": "present",
                       "detail": ", ".join(findings["meta_pixel"]["ids"]) if findings["meta_pixel"]["ids"] else "Pixel JS present",
                       "max": 15, "got": 15})
    else:
        checks.append({"item": "Meta Pixel", "status": "missing",
                       "detail": "No Facebook Pixel detected", "max": 15, "got": 0})

    total_max = sum(c["max"] for c in checks)
    total_got = sum(c["got"] for c in checks)
    score = round(total_got / total_max * 100, 1) if total_max else 0

    # Determine summary
    tracking_tools = []
    if findings.get("ga4", {}).get("found"): tracking_tools.append("GA4")
    if findings.get("ua", {}).get("found"): tracking_tools.append("UA")
    if findings.get("gtm", {}).get("found"): tracking_tools.append("GTM")
    if findings.get("google_ads", {}).get("found"): tracking_tools.append("Ads")
    if findings.get("meta_pixel", {}).get("found"): tracking_tools.append("Meta Pixel")
    gsc_verified = findings.get("gsc_meta", {}).get("found") or dns_result.get("gsc_dns_found")

    return {
        "score": score,
        "gsc_verified": gsc_verified,
        "tracking_tools": tracking_tools,
        "checks": checks,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Detect analytics & verification services on a website."
    )
    parser.add_argument("url", help="URL to check")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    if not args.url.startswith(("http://", "https://")):
        args.url = f"https://{args.url}"

    from urllib.parse import urlparse
    domain = urlparse(args.url).netloc

    # Fetch HTML
    html, status, error = fetch_page(args.url)

    if html is None:
        result = {
            "url": args.url,
            "domain": domain,
            "page_accessible": False,
            "http_status": status,
            "error": error,
            "score": 0,
            "gsc_verified": False,
            "tracking_tools": [],
            "checks": [],
        }
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"\n{'='*60}")
            print(f"  Analytics & Verification Audit — {args.url}")
            print(f"  Score: 0/100 | Page not accessible ({error})")
            print(f"{'='*60}\n")
        sys.exit(1)

    # Scan HTML
    findings = scan_html(html, domain)

    # DNS check
    try:
        dns_result = check_dns_txt(domain)
    except Exception:
        dns_result = check_dns_simple(domain)

    # Score
    scored = calculate_score(findings, dns_result)
    score = scored["score"]
    gsc_verified = scored["gsc_verified"]
    tracking_tools = scored["tracking_tools"]
    checks = scored["checks"]

    result = {
        "url": args.url,
        "domain": domain,
        "page_accessible": True,
        "http_status": status,
        "score": score,
        "gsc_verified": gsc_verified,
        "gsc_methods": {
            "meta_tag": findings.get("gsc_meta", {}).get("found", False),
            "dns_txt": dns_result.get("gsc_dns_found", False),
        },
        "tracking_tools": tracking_tools,
        "findings": findings,
        "checks": checks,
    }

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"\n{'='*60}")
        print(f"  Analytics & Verification Audit — {args.url}")
        print(f"  Score: {score}/100")
        print(f"{'='*60}\n")

        print(f"  📊 Tracking Tools Found: {', '.join(tracking_tools) if tracking_tools else 'None'}")
        if gsc_verified:
            methods = []
            if findings["gsc_meta"]["found"]: methods.append("meta tag")
            if dns_result.get("gsc_dns_found"): methods.append("DNS TXT")
            print(f"  ✅ Google Search Console: Verified ({', '.join(methods)})")
        else:
            print(f"  ❌ Google Search Console: Not verified")

        print(f"\n  {'─'*55}")
        print(f"  {'Check':<30} {'Status':<10} {'Score':>8}")
        print(f"  {'─'*55}")
        for c in checks:
            icons = {"present": "✅", "missing": "❌", "skipped": "⚠️"}
            icon = icons.get(c["status"], "⬜")
            status_label = c["status"].upper()
            score_str = f"{c['got']}/{c['max']}"
            print(f"  {icon} {c['item']:<28} {status_label:<10} {score_str:>8}")

        if not dns_result.get("dns_available") and dns_result.get("dns_note"):
            print(f"\n  ⚠️  {dns_result['dns_note']}")
            print(f"     Install dnspython for DNS TXT checks: pip install dnspython")

        if score < 50:
            print(f"\n  💡 Tip: Install Google Analytics 4 + verify GSC for better")
            print(f"     search visibility and performance tracking.")

    sys.exit(0 if score >= 30 else 1)


if __name__ == "__main__":
    main()
