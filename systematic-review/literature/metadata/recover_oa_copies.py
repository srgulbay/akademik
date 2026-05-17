#!/usr/bin/env python3
"""Find and download OA copies of paywalled articles via Unpaywall + Europe PMC."""
import csv
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent
FT_DIR = ROOT / "full-text"
FT_DIR.mkdir(parents=True, exist_ok=True)
CSV_PATH = ROOT / "master_catalog.csv"
INV_PATH = ROOT / "fulltext_inventory.csv"
LOG_PATH = ROOT / "oa_recovery_log.csv"

EMAIL = "researcher@example.com"
USER_AGENT = "AcademicSystematicReview/1.0"
UNPAYWALL = "https://api.unpaywall.org/v2/{doi}?email=" + EMAIL
EUROPEPMC_SEARCH = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:{doi}&format=json&resultType=core"
EUROPEPMC_FULL = "https://www.ebi.ac.uk/europepmc/webservices/rest/{src}/{eid}/fullTextXML"

def fetch_bytes(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()

def fetch_json(url, timeout=30):
    return json.loads(fetch_bytes(url, timeout).decode("utf-8", errors="replace"))

def fetch_text(url, timeout=30):
    return fetch_bytes(url, timeout).decode("utf-8", errors="replace")

def has_full_text(filename):
    """Check if a full-text TXT/PDF already exists with body content."""
    pdf = FT_DIR / f"{filename}.pdf"
    if pdf.exists() and pdf.stat().st_size > 5000:
        return True
    txt = FT_DIR / f"{filename}.txt"
    if txt.exists():
        content = txt.read_text(encoding="utf-8", errors="replace")
        if "=== FULL TEXT ===" in content:
            body = content.split("=== FULL TEXT ===")[1]
            if len(body.strip()) > 1000 and "[Full text not redistributable" not in body:
                return True
    return False

def try_unpaywall(doi, filename):
    try:
        data = fetch_json(UNPAYWALL.format(doi=urllib.parse.quote(doi)))
    except Exception as e:
        return None, f"unpaywall_err:{type(e).__name__}"
    if not data.get("is_oa"):
        return None, "unpaywall_not_oa"
    best = data.get("best_oa_location") or {}
    pdf_url = best.get("url_for_pdf")
    if not pdf_url:
        # Try other OA locations
        for loc in data.get("oa_locations", []):
            if loc.get("url_for_pdf"):
                pdf_url = loc["url_for_pdf"]
                break
    if not pdf_url:
        return None, "unpaywall_no_pdf"
    try:
        pdf_data = fetch_bytes(pdf_url, timeout=120)
        if len(pdf_data) < 5000:
            return None, f"unpaywall_pdf_too_small:{len(pdf_data)}"
        if not pdf_data.startswith(b"%PDF"):
            return None, "unpaywall_not_pdf_content"
        (FT_DIR / f"{filename}.pdf").write_bytes(pdf_data)
        return "unpaywall_pdf_ok", f"size={len(pdf_data)}"
    except Exception as e:
        return None, f"unpaywall_download_err:{type(e).__name__}"

def try_europepmc(doi, filename):
    try:
        search = fetch_json(EUROPEPMC_SEARCH.format(doi=urllib.parse.quote(doi)))
    except Exception as e:
        return None, f"epmc_search_err:{type(e).__name__}"
    hits = (search.get("resultList") or {}).get("result", [])
    if not hits:
        return None, "epmc_not_found"
    hit = hits[0]
    if hit.get("isOpenAccess") != "Y" and hit.get("hasTextMinedTerms") != "Y" and not hit.get("inEPMC") == "Y":
        return None, "epmc_not_oa"
    src = hit.get("source", "MED")
    eid = hit.get("id")
    if not eid:
        return None, "epmc_no_id"
    try:
        xml_data = fetch_text(EUROPEPMC_FULL.format(src=src, eid=eid), timeout=60)
        if "<article" in xml_data and "<body>" in xml_data:
            (FT_DIR / f"{filename}.xml").write_text(xml_data, encoding="utf-8")
            return "epmc_xml_ok", f"size={len(xml_data)}"
        return None, "epmc_no_body"
    except Exception as e:
        return None, f"epmc_full_err:{type(e).__name__}"

def main():
    with open(CSV_PATH, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    needs_recovery = [r for r in rows if r["doi"] and not has_full_text(r["filename"])]
    print(f"Articles needing OA recovery: {len(needs_recovery)}")

    log_rows = []
    success = 0
    for i, row in enumerate(needs_recovery, 1):
        doi = row["doi"]
        fname = row["filename"]
        # Try Unpaywall first (best for paywalled articles)
        status, info = try_unpaywall(doi, fname)
        method = "unpaywall"
        if status is None:
            # Try Europe PMC
            status2, info2 = try_europepmc(doi, fname)
            if status2:
                status, info = status2, info2
                method = "europepmc"
            else:
                info = f"unpaywall:{info} | epmc:{info2}"
                method = "both_failed"
        if status:
            success += 1
        log_rows.append({"filename": fname, "doi": doi, "method": method, "status": status or "fail", "info": info})
        print(f"[{i}/{len(needs_recovery)}] {fname}: {method} -> {status or 'fail'} ({info})")
        time.sleep(0.5)

    with open(LOG_PATH, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["filename", "doi", "method", "status", "info"])
        w.writeheader()
        w.writerows(log_rows)

    print(f"\n=== Summary ===")
    print(f"Tried: {len(needs_recovery)}")
    print(f"Recovered: {success}")
    print(f"Log: {LOG_PATH}")

if __name__ == "__main__":
    main()
