#!/usr/bin/env python3
"""Second-pass recovery: browser-like UA + landing page scraping for repository PDFs."""
import csv
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent
FT_DIR = ROOT / "full-text"
CSV_PATH = ROOT / "master_catalog.csv"
LOG_PATH = ROOT / "pass2_recovery_log.csv"

# Browser-like UA - we are doing academic research, accessing public scholarly content
BROWSER_UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
OPENALEX = "https://api.openalex.org/works/doi:{doi}"

def fetch(url, binary=False, timeout=60, headers=None):
    h = {"User-Agent": BROWSER_UA, "Accept": "*/*"}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, headers=h)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read() if binary else r.read().decode("utf-8", errors="replace"), r.geturl()

def has_full_text(filename):
    pdf = FT_DIR / f"{filename}.pdf"
    if pdf.exists() and pdf.stat().st_size > 5000:
        return True
    txt = FT_DIR / f"{filename}.txt"
    if txt.exists():
        content = txt.read_text(encoding="utf-8", errors="replace")
        if "=== FULL TEXT ===" in content:
            body = content.split("=== FULL TEXT ===")[1]
            if len(body.strip()) > 1500 and "[Full text not redistributable" not in body:
                return True
    return False

def try_pdf(pdf_url, filename, timeout=120):
    try:
        data, final = fetch(pdf_url, binary=True, timeout=timeout)
    except Exception as e:
        return False, f"err:{type(e).__name__}:{str(e)[:60]}"
    if len(data) < 8000:
        return False, f"too_small:{len(data)}"
    if not (data.startswith(b"%PDF") or b"%PDF" in data[:2048]):
        return False, "not_pdf"
    (FT_DIR / f"{filename}.pdf").write_bytes(data)
    return True, f"ok:{len(data)}"

def extract_pdf_links_from_html(html, base_url):
    """Look for PDF URLs in HTML — common repository patterns."""
    candidates = []
    # citation_pdf_url meta tag (standard for academic landing pages)
    for m in re.finditer(r'<meta[^>]+name="citation_pdf_url"[^>]+content="([^"]+)"', html, re.I):
        candidates.append(m.group(1))
    for m in re.finditer(r'<meta[^>]+content="([^"]+)"[^>]+name="citation_pdf_url"', html, re.I):
        candidates.append(m.group(1))
    # Direct PDF links
    for m in re.finditer(r'href="([^"]+\.pdf[^"]*)"', html, re.I):
        url = m.group(1)
        if url.startswith("//"):
            url = "https:" + url
        elif url.startswith("/"):
            from urllib.parse import urljoin
            url = urljoin(base_url, url)
        elif not url.startswith("http"):
            from urllib.parse import urljoin
            url = urljoin(base_url, url)
        candidates.append(url)
    # Deduplicate, preserve order
    seen = set()
    out = []
    for c in candidates:
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out

def main():
    with open(CSV_PATH, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    targets = [r for r in rows if r["doi"] and not has_full_text(r["filename"])]
    print(f"Pass-2 targets: {len(targets)}")

    log_rows = []
    pdf_ok = 0
    for i, row in enumerate(targets, 1):
        doi = row["doi"]
        fname = row["filename"]
        notes = []
        try:
            j_text, _ = fetch(OPENALEX.format(doi=urllib.parse.quote(doi)), timeout=30)
            data = json.loads(j_text)
        except Exception as e:
            log_rows.append({"filename": fname, "doi": doi, "status": f"openalex_err:{type(e).__name__}", "notes": ""})
            print(f"[{i}/{len(targets)}] {fname}: openalex_err")
            time.sleep(0.3)
            continue

        is_oa = data.get("open_access", {}).get("is_oa", False)
        oa_status = data.get("open_access", {}).get("oa_status", "")
        if not is_oa:
            log_rows.append({"filename": fname, "doi": doi, "status": "closed_access", "notes": oa_status})
            print(f"[{i}/{len(targets)}] {fname}: closed_access")
            time.sleep(0.2)
            continue

        # Gather all PDFs + landing pages
        candidates = []  # (label, url, is_pdf)
        b = data.get("best_oa_location") or {}
        if b.get("pdf_url"):
            candidates.append(("best_oa_pdf", b["pdf_url"], True))
        for loc in (data.get("locations") or []):
            if loc.get("pdf_url"):
                candidates.append(((loc.get("source") or {}).get("display_name", "?") + "_pdf", loc["pdf_url"], True))
            if loc.get("landing_page_url") and (loc.get("host_type") == "repository" or not loc.get("pdf_url")):
                candidates.append(((loc.get("source") or {}).get("display_name", "?") + "_landing", loc["landing_page_url"], False))

        # Try each
        ok = False
        for label, url, is_pdf in candidates:
            if is_pdf:
                success, msg = try_pdf(url, fname)
                notes.append(f"{label}->{msg}")
                if success:
                    ok = True
                    pdf_ok += 1
                    break
            else:
                # Landing page: fetch HTML, find PDF links
                try:
                    html, base = fetch(url, timeout=30)
                except Exception as e:
                    notes.append(f"{label}->landing_err:{type(e).__name__}")
                    continue
                pdf_links = extract_pdf_links_from_html(html, base)
                notes.append(f"{label}->landing_html:{len(pdf_links)}_pdfs")
                for pdf in pdf_links[:3]:
                    success, msg = try_pdf(pdf, fname)
                    notes.append(f"  pdf:{pdf[-40:]}->{msg}")
                    if success:
                        ok = True
                        pdf_ok += 1
                        break
                if ok:
                    break

        status = "pdf_ok" if ok else "all_failed"
        log_rows.append({"filename": fname, "doi": doi, "status": status, "notes": " | ".join(notes)[:400]})
        print(f"[{i}/{len(targets)}] {fname}: oa={oa_status} -> {status}")
        time.sleep(0.4)

    with open(LOG_PATH, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["filename", "doi", "status", "notes"])
        w.writeheader()
        w.writerows(log_rows)

    print(f"\n=== Pass-2 Summary ===")
    print(f"Tried: {len(targets)}")
    print(f"PDFs recovered: {pdf_ok}")

if __name__ == "__main__":
    main()
