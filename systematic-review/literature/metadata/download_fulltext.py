#!/usr/bin/env python3
"""Download PMC OA full-text PDFs (and XML fallback) for articles with PMC IDs."""
import csv
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent
CSV_PATH = ROOT / "master_catalog.csv"
FT_DIR = ROOT / "full-text"
FT_DIR.mkdir(parents=True, exist_ok=True)
LOG_PATH = ROOT / "download_log.csv"

USER_AGENT = "AcademicSystematicReview/1.0 (mailto:researcher@example.com)"
OA_URL = "https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id={}"
EFETCH_PMC = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id={}&rettype=xml&retmode=xml"

def fetch(url, binary=False, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()
        return data if binary else data.decode("utf-8", errors="replace")

def http_to_https(u):
    return u.replace("ftp://", "https://").replace("http://ftp.", "https://ftp.") if u else u

def download_pmc_oa(pmcid):
    """Return list of (format, local_path) for downloaded files, or [] on failure."""
    results = []
    try:
        xml_resp = fetch(OA_URL.format(pmcid))
    except Exception as e:
        return [("error", f"OA service error: {e}")]
    try:
        root = ET.fromstring(xml_resp)
    except ET.ParseError as e:
        return [("error", f"OA XML parse error: {e}")]
    error_el = root.find(".//error")
    if error_el is not None:
        return [("error", error_el.get("code", "unknown") + ": " + (error_el.text or ""))]
    return results, root

def main():
    log_rows = []
    with open(CSV_PATH, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    pmc_rows = [r for r in rows if r["pmcid"]]
    print(f"Articles with PMC IDs: {len(pmc_rows)}")

    for i, row in enumerate(pmc_rows, 1):
        pmcid = row["pmcid"]
        fname = row["filename"]
        status = ""
        # 1) Try OA service first (gives PDF/tgz)
        pdf_path = FT_DIR / f"{fname}.pdf"
        xml_path = FT_DIR / f"{fname}.xml"
        if pdf_path.exists() or xml_path.exists():
            status = "already_downloaded"
            log_rows.append({"filename": fname, "pmcid": pmcid, "status": status})
            print(f"[{i}/{len(pmc_rows)}] {fname}: {status}")
            continue

        oa_ok = False
        try:
            xml_resp = fetch(OA_URL.format(pmcid))
            oa_root = ET.fromstring(xml_resp)
            err = oa_root.find(".//error")
            if err is not None:
                status = f"OA_unavailable:{err.get('code','?')}"
            else:
                pdf_link = None
                tgz_link = None
                for link in oa_root.findall(".//link"):
                    fmt = link.get("format", "")
                    href = http_to_https(link.get("href", ""))
                    if fmt == "pdf" and href and not pdf_link:
                        pdf_link = href
                    elif fmt == "tgz" and href and not tgz_link:
                        tgz_link = href
                if pdf_link:
                    try:
                        data = fetch(pdf_link, binary=True, timeout=120)
                        pdf_path.write_bytes(data)
                        status = "pdf_ok"
                        oa_ok = True
                    except Exception as e:
                        status = f"pdf_download_err:{type(e).__name__}"
        except Exception as e:
            status = f"OA_error:{type(e).__name__}"

        # 2) Fall back to PMC XML via efetch
        if not oa_ok:
            try:
                xml_data = fetch(EFETCH_PMC.format(pmcid.lstrip("PMC")), timeout=60)
                if "<article" in xml_data or "<pmc-article" in xml_data:
                    xml_path.write_text(xml_data, encoding="utf-8")
                    status = (status + "; xml_ok") if status else "xml_ok"
                else:
                    status = (status + "; xml_empty") if status else "xml_empty"
            except Exception as e:
                status = (status + f"; xml_err:{type(e).__name__}") if status else f"xml_err:{type(e).__name__}"

        log_rows.append({"filename": fname, "pmcid": pmcid, "status": status})
        print(f"[{i}/{len(pmc_rows)}] {fname}: {status}")

        # Rate limit: ~3 req/sec without API key
        time.sleep(0.4)

    # Write log
    with open(LOG_PATH, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["filename", "pmcid", "status"])
        w.writeheader()
        w.writerows(log_rows)

    # Summary
    pdf_ok = sum(1 for r in log_rows if "pdf_ok" in r["status"])
    xml_ok = sum(1 for r in log_rows if "xml_ok" in r["status"])
    print(f"\n=== Summary ===")
    print(f"PDF downloaded: {pdf_ok}")
    print(f"XML downloaded: {xml_ok}")
    print(f"Log: {LOG_PATH}")

if __name__ == "__main__":
    main()
