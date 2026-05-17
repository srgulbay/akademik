#!/usr/bin/env python3
"""Use OpenAlex to find OA copies (publisher / repository / preprint) of articles
that we don't yet have full text for. Downloads PDFs directly.
"""
import csv
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent
FT_DIR = ROOT / "full-text"
CSV_PATH = ROOT / "master_catalog.csv"
LOG_PATH = ROOT / "openalex_recovery_log.csv"

USER_AGENT = "AcademicSystematicReview/1.0 (mailto:research@akademik.local)"
OPENALEX = "https://api.openalex.org/works/doi:{doi}"

def fetch(url, binary=False, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read() if binary else r.read().decode("utf-8", errors="replace")

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
    """Attempt to download a PDF. Returns (ok, info)."""
    try:
        data = fetch(pdf_url, binary=True, timeout=timeout)
    except Exception as e:
        return False, f"download_err:{type(e).__name__}:{str(e)[:60]}"
    if len(data) < 8000:
        return False, f"too_small:{len(data)}"
    if not (data.startswith(b"%PDF") or b"%PDF" in data[:1024]):
        return False, "not_pdf"
    (FT_DIR / f"{filename}.pdf").write_bytes(data)
    return True, f"ok:{len(data)}"

def main():
    with open(CSV_PATH, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    targets = [r for r in rows if r["doi"] and not has_full_text(r["filename"])]
    print(f"Articles to recover via OpenAlex: {len(targets)}")

    log_rows = []
    pdf_ok = 0
    for i, row in enumerate(targets, 1):
        doi = row["doi"]
        fname = row["filename"]
        try:
            data = json.loads(fetch(OPENALEX.format(doi=urllib.parse.quote(doi)), timeout=30))
        except Exception as e:
            log_rows.append({"filename": fname, "doi": doi, "is_oa": "", "oa_status": "", "tried_urls": "", "status": f"openalex_err:{type(e).__name__}"})
            print(f"[{i}/{len(targets)}] {fname}: openalex_err")
            time.sleep(0.3)
            continue

        is_oa = data.get("open_access", {}).get("is_oa", False)
        oa_status = data.get("open_access", {}).get("oa_status", "")

        # Build candidate PDF URLs (in priority order)
        candidates = []
        # 1) best_oa_location pdf
        b = data.get("best_oa_location") or {}
        if b.get("pdf_url"):
            candidates.append(("best_oa", b["pdf_url"]))
        # 2) all locations with pdf_url
        for loc in (data.get("locations") or []):
            pdf = loc.get("pdf_url")
            if pdf and pdf not in [c[1] for c in candidates]:
                src = (loc.get("source") or {}).get("display_name", "?")
                candidates.append((src, pdf))

        tried = []
        ok = False
        info = ""
        for label, url in candidates:
            tried.append(f"{label}:{url[:80]}")
            success, msg = try_pdf(url, fname)
            if success:
                ok = True
                info = f"{label}:{msg}"
                pdf_ok += 1
                break

        status = "pdf_ok" if ok else ("no_pdf_url" if not candidates else "all_failed")
        log_rows.append({
            "filename": fname,
            "doi": doi,
            "is_oa": str(is_oa),
            "oa_status": oa_status,
            "tried_urls": " | ".join(tried)[:300],
            "status": status if not ok else f"pdf_ok:{info}",
        })
        print(f"[{i}/{len(targets)}] {fname}: oa={is_oa}/{oa_status} -> {status} ({len(candidates)} candidate(s))")
        time.sleep(0.3)

    with open(LOG_PATH, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(log_rows[0].keys()))
        w.writeheader()
        w.writerows(log_rows)

    print(f"\n=== Summary ===")
    print(f"Tried: {len(targets)}")
    print(f"PDFs recovered: {pdf_ok}")
    print(f"Log: {LOG_PATH}")

if __name__ == "__main__":
    main()
