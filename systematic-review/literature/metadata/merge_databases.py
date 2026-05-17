#!/usr/bin/env python3
"""
Merge & deduplicate records from PubMed + Scopus + Web of Science + Embase + Cochrane.

Expected input files (use whichever exist):
  literature/master_catalog.csv               (PubMed — already in our format)
  literature/external/scopus/*.csv            (Scopus standard CSV export)
  literature/external/wos/*.txt               (WoS tab-delimited export)
  literature/external/wos/*.bib               (WoS BibTeX, alternative)
  literature/external/embase/*.csv            (Embase CSV)
  literature/external/cochrane/*.csv|*.txt    (Cochrane)

Deduplication priority:
  1) DOI (normalized lowercase, doi.org/ stripped)
  2) PMID
  3) Title fingerprint (lowercase, non-alphanum stripped) + year

Outputs:
  literature/merged_unique.csv
  literature/prisma_flow_data.json
"""
import csv
import json
import re
import sys
from pathlib import Path
from collections import defaultdict

HERE = Path(__file__).parent
ROOT = HERE.parent

def norm_doi(s):
    if not s:
        return ""
    s = s.strip().lower()
    s = re.sub(r"^https?://(dx\.)?doi\.org/", "", s)
    s = re.sub(r"\s+", "", s)
    return s

def norm_title(s):
    if not s:
        return ""
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "", s)
    return s[:120]

def make_key(rec):
    """Return a tuple of dedup keys."""
    return {
        "doi": norm_doi(rec.get("doi", "")),
        "pmid": (rec.get("pmid") or "").strip(),
        "title_year": norm_title(rec.get("title", "")) + "|" + (rec.get("year") or ""),
    }

# ---------- Source readers ----------

def read_pubmed(path):
    if not path.exists():
        return []
    out = []
    with open(path, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            out.append({
                "source": "PubMed",
                "doi": r.get("doi", ""),
                "pmid": r.get("pmid", ""),
                "title": r.get("title", ""),
                "year": r.get("year", ""),
                "authors": r.get("first_author", ""),
                "journal": r.get("journal", ""),
                "pmcid": r.get("pmcid", ""),
                "filename": r.get("filename", ""),
            })
    return out

def read_scopus(dir_path):
    out = []
    if not dir_path.exists():
        return out
    for csv_path in dir_path.glob("*.csv"):
        with open(csv_path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                # Scopus column names (standard 2024 export)
                doi = r.get("DOI") or ""
                # PMID rarely present in Scopus
                pmid = ""
                # Title
                title = r.get("Title") or ""
                year = (r.get("Year") or "").strip()
                authors_field = r.get("Authors") or ""
                first_author = authors_field.split(";")[0].split(",")[0].strip() if authors_field else ""
                journal = r.get("Source title") or r.get("Source") or ""
                out.append({
                    "source": "Scopus",
                    "doi": doi,
                    "pmid": pmid,
                    "title": title,
                    "year": year,
                    "authors": first_author,
                    "journal": journal,
                    "scopus_eid": r.get("EID") or "",
                })
    return out

def read_wos(dir_path):
    out = []
    if not dir_path.exists():
        return out
    # Tab-delimited
    for txt_path in dir_path.glob("*.txt"):
        with open(txt_path, encoding="utf-8", errors="replace") as f:
            reader = csv.DictReader(f, delimiter="\t")
            for r in reader:
                # WoS field codes
                doi = r.get("DI") or r.get("DOI") or ""
                pmid = r.get("PM") or ""
                title = r.get("TI") or r.get("Article Title") or ""
                year = (r.get("PY") or r.get("Publication Year") or "").strip()
                authors_field = r.get("AU") or r.get("Authors") or ""
                first_author = authors_field.split(";")[0].strip() if authors_field else ""
                journal = r.get("SO") or r.get("Source Title") or ""
                out.append({
                    "source": "WoS",
                    "doi": doi,
                    "pmid": pmid,
                    "title": title,
                    "year": year,
                    "authors": first_author,
                    "journal": journal,
                    "wos_ut": r.get("UT") or "",
                })
    # BibTeX (fallback)
    for bib_path in dir_path.glob("*.bib"):
        text = bib_path.read_text(encoding="utf-8", errors="replace")
        for entry in re.split(r"\n@", text):
            if not entry.strip():
                continue
            def field(name):
                m = re.search(rf"{name}\s*=\s*[{{\"]+(.*?)[}}\"]+\s*,?\s*\n", entry, re.IGNORECASE | re.DOTALL)
                return m.group(1).strip().replace("\n", " ") if m else ""
            doi = field("doi")
            title = field("title")
            year = field("year")
            journal = field("journal")
            authors = field("author")
            first_author = authors.split(" and ")[0].split(",")[0].strip() if authors else ""
            if title:
                out.append({"source": "WoS-bib", "doi": doi, "pmid": "", "title": title, "year": year,
                            "authors": first_author, "journal": journal})
    return out

def read_embase(dir_path):
    out = []
    if not dir_path.exists():
        return out
    for csv_path in dir_path.glob("*.csv"):
        with open(csv_path, encoding="utf-8", errors="replace") as f:
            reader = csv.DictReader(f)
            for r in reader:
                # Embase column names (newest export 2024+)
                doi = r.get("Article DOI") or r.get("DOI") or ""
                pmid = r.get("Medline PUI") or r.get("Pubmed ID") or ""
                title = r.get("Title") or r.get("Article Title") or ""
                year = (r.get("Year of Publication") or r.get("Year") or "").strip()
                authors_field = r.get("Author Names") or r.get("Authors") or ""
                first_author = authors_field.split(";")[0].split(",")[0].strip() if authors_field else ""
                journal = r.get("Source title") or r.get("Source") or r.get("Journal") or ""
                out.append({
                    "source": "Embase",
                    "doi": doi,
                    "pmid": pmid,
                    "title": title,
                    "year": year,
                    "authors": first_author,
                    "journal": journal,
                    "embase_pui": r.get("Embase Accession ID") or "",
                })
    return out

def read_openalex(dir_path):
    out = []
    if not dir_path.exists():
        return out
    for csv_path in dir_path.glob("*.csv"):
        with open(csv_path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                doi = r.get("DOI") or ""
                title = r.get("Title") or ""
                year = (r.get("Year") or "").strip()
                authors_field = r.get("Authors") or ""
                first_author = authors_field.split(";")[0].split(",")[0].strip() if authors_field else ""
                journal = r.get("Source title") or ""
                out.append({
                    "source": "OpenAlex",
                    "doi": doi,
                    "pmid": "",
                    "title": title,
                    "year": year,
                    "authors": first_author,
                    "journal": journal,
                    "openalex_id": r.get("OpenAlexID") or "",
                })
    return out


def read_crossref(dir_path):
    out = []
    if not dir_path.exists():
        return out
    for csv_path in dir_path.glob("*.csv"):
        with open(csv_path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                doi = r.get("DOI") or ""
                title = r.get("Title") or ""
                year = (r.get("Year") or "").strip()
                authors_field = r.get("Authors") or ""
                first_author = authors_field.split(";")[0].split(",")[0].strip() if authors_field else ""
                journal = r.get("Source title") or ""
                out.append({
                    "source": "Crossref",
                    "doi": doi,
                    "pmid": "",
                    "title": title,
                    "year": year,
                    "authors": first_author,
                    "journal": journal,
                })
    return out


def read_cochrane(dir_path):
    out = []
    if not dir_path.exists():
        return out
    for path in list(dir_path.glob("*.csv")) + list(dir_path.glob("*.txt")):
        # Try CSV first
        try:
            with open(path, encoding="utf-8", errors="replace") as f:
                reader = csv.DictReader(f)
                for r in reader:
                    out.append({
                        "source": "Cochrane",
                        "doi": r.get("DOI", ""),
                        "pmid": "",
                        "title": r.get("Title") or r.get("Article Title", ""),
                        "year": r.get("Year") or r.get("Published Year", ""),
                        "authors": (r.get("Authors") or "").split(";")[0].split(",")[0].strip(),
                        "journal": r.get("Journal") or r.get("Source", ""),
                    })
        except Exception:
            continue
    return out

# ---------- Deduplication ----------

def dedup(records):
    """Return (unique_records, duplicates_log)."""
    by_doi = {}
    by_pmid = {}
    by_title_year = {}
    unique = []
    dup_log = []

    for rec in records:
        keys = make_key(rec)
        matched_idx = None
        match_kind = None
        if keys["doi"] and keys["doi"] in by_doi:
            matched_idx = by_doi[keys["doi"]]
            match_kind = "doi"
        elif keys["pmid"] and keys["pmid"] in by_pmid:
            matched_idx = by_pmid[keys["pmid"]]
            match_kind = "pmid"
        elif keys["title_year"] and keys["title_year"] in by_title_year:
            matched_idx = by_title_year[keys["title_year"]]
            match_kind = "title_year"

        if matched_idx is not None:
            # Merge sources
            unique[matched_idx]["sources"].add(rec["source"])
            # Fill missing fields
            for k in ("doi", "pmid", "pmcid", "scopus_eid", "wos_ut", "embase_pui", "filename", "openalex_id"):
                if not unique[matched_idx].get(k) and rec.get(k):
                    unique[matched_idx][k] = rec[k]
            dup_log.append({"source": rec["source"], "title": rec.get("title", "")[:80],
                             "match_kind": match_kind, "matched_with": unique[matched_idx].get("title", "")[:80]})
            continue

        new_rec = dict(rec)
        new_rec["sources"] = {rec["source"]}
        idx = len(unique)
        unique.append(new_rec)
        if keys["doi"]:
            by_doi[keys["doi"]] = idx
        if keys["pmid"]:
            by_pmid[keys["pmid"]] = idx
        if keys["title_year"]:
            by_title_year[keys["title_year"]] = idx

    return unique, dup_log

def main():
    sources = {
        "PubMed": read_pubmed(ROOT / "master_catalog.csv"),
        "Scopus": read_scopus(ROOT / "external" / "scopus"),
        "WoS": read_wos(ROOT / "external" / "wos"),
        "Embase": read_embase(ROOT / "external" / "embase"),
        "Cochrane": read_cochrane(ROOT / "external" / "cochrane"),
        "OpenAlex": read_openalex(ROOT / "external" / "openalex"),
        "Crossref": read_crossref(ROOT / "external" / "crossref"),
    }

    print("=== Per-source counts ===")
    all_records = []
    for src, recs in sources.items():
        print(f"  {src}: {len(recs)}")
        all_records.extend(recs)
    print(f"  TOTAL (with duplicates): {len(all_records)}")

    unique, dup_log = dedup(all_records)
    print(f"\n=== After deduplication ===")
    print(f"  Unique records: {len(unique)}")
    print(f"  Duplicates removed: {len(dup_log)}")

    # Write merged_unique.csv
    out_path = ROOT / "merged_unique.csv"
    fieldnames = ["doi", "pmid", "pmcid", "year", "authors", "title", "journal",
                  "sources", "scopus_eid", "wos_ut", "embase_pui", "openalex_id", "filename"]
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(fieldnames)
        for u in unique:
            w.writerow([
                u.get("doi", ""), u.get("pmid", ""), u.get("pmcid", ""),
                u.get("year", ""), u.get("authors", ""), u.get("title", ""),
                u.get("journal", ""),
                "; ".join(sorted(u.get("sources", set()))),
                u.get("scopus_eid", ""), u.get("wos_ut", ""), u.get("embase_pui", ""),
                u.get("openalex_id", ""), u.get("filename", ""),
            ])
    print(f"  Written: {out_path}")

    # PRISMA flow data
    flow = {
        "identification": {src: len(recs) for src, recs in sources.items()},
        "total_identified": len(all_records),
        "duplicates_removed": len(dup_log),
        "after_dedup": len(unique),
    }
    # Cross-database overlap
    overlap = defaultdict(int)
    for u in unique:
        srcs = "+".join(sorted(u.get("sources", set())))
        overlap[srcs] += 1
    flow["source_overlap"] = dict(overlap)

    with open(ROOT / "prisma_flow_data.json", "w", encoding="utf-8") as f:
        json.dump(flow, f, indent=2, ensure_ascii=False)
    print(f"  PRISMA data: {ROOT / 'prisma_flow_data.json'}")

if __name__ == "__main__":
    main()
