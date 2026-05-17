#!/usr/bin/env python3
"""
Build Vancouver-style bibliography mapping for all 340 papers.

Output:
  systematic-review/bibliography.json — {study_id: {citation_number, vancouver_full}}
  systematic-review/bibliography.md — numbered reference list

Vancouver format:
  Author AB, Author CD, Author EF. Title. Journal. Year;Volume(Issue):Pages.
  doi: ...

PubMed XML or NLM citation builder would be ideal, but we work with what we have:
  - master_catalog.csv columns: filename, pmid, first_author, year, title, journal, doi, ...

We can fetch full author list and pagination via NCBI EFetch for each PMID
(but that's 340 API calls — use cached PMC XML where available, otherwise build
abbreviated Vancouver from catalog metadata).
"""
import csv
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

LIT = Path(__file__).resolve().parent.parent
ROOT = LIT.parent
FT_DIR = LIT / "full-text"
CATALOG = LIT / "master_catalog.csv"

# Order alphabetically by study_id for stable numbering
# (Alternative: by first-citation order in manuscript — too complex without a finished draft)

def extract_authors_from_xml(xml_path):
    """Extract author list (surname + initials) from PMC XML."""
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        authors = []
        for contrib in root.iter():
            tag = contrib.tag.split('}')[-1] if '}' in contrib.tag else contrib.tag
            if tag != 'contrib': continue
            if contrib.get('contrib-type') != 'author': continue
            surname = ''
            initials = ''
            for c in contrib.iter():
                ctag = c.tag.split('}')[-1] if '}' in c.tag else c.tag
                if ctag == 'surname' and c.text:
                    surname = c.text.strip()
                if ctag == 'given-names':
                    if c.get('initials'):
                        initials = c.get('initials')
                    elif c.text:
                        # Compute initials from given name
                        initials = ''.join(p[0].upper() for p in re.split(r'[\s-]+', c.text) if p)
            if surname:
                authors.append(f"{surname} {initials}".strip())
        return authors
    except Exception:
        return []

def extract_pages_volume_issue(xml_path):
    """Extract volume, issue, fpage, lpage from PMC XML."""
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        info = {"volume": "", "issue": "", "fpage": "", "lpage": "", "elocation": ""}
        for elem in root.iter():
            tag = elem.tag.split('}')[-1] if '}' in elem.tag else elem.tag
            if tag == 'volume' and not info["volume"] and elem.text:
                info["volume"] = elem.text.strip()
            elif tag == 'issue' and not info["issue"] and elem.text:
                info["issue"] = elem.text.strip()
            elif tag == 'fpage' and not info["fpage"] and elem.text:
                info["fpage"] = elem.text.strip()
            elif tag == 'lpage' and not info["lpage"] and elem.text:
                info["lpage"] = elem.text.strip()
            elif tag == 'elocation-id' and not info["elocation"] and elem.text:
                info["elocation"] = elem.text.strip()
        return info
    except Exception:
        return {"volume": "", "issue": "", "fpage": "", "lpage": "", "elocation": ""}

def fallback_authors(first_author, study_id):
    """Build approximate author entry when XML unavailable."""
    # Try to parse first_author field
    if not first_author:
        return [study_id.replace("_", " ") + " et al"]
    # If "et al" already present, return as is
    if "et al" in first_author.lower():
        return [first_author]
    return [first_author + " et al"]

def build_vancouver(study_id, first_author_csv, year, title, journal, doi, pmid, pmcid):
    """Construct Vancouver-style reference string."""
    xml_path = FT_DIR / f"{study_id}.xml"
    if xml_path.exists():
        authors = extract_authors_from_xml(xml_path)
        meta = extract_pages_volume_issue(xml_path)
    else:
        authors = fallback_authors(first_author_csv, study_id)
        meta = {"volume": "", "issue": "", "fpage": "", "lpage": "", "elocation": ""}

    # Author block: list up to 6, then "et al."
    if not authors:
        authors = fallback_authors(first_author_csv, study_id)
    if len(authors) > 6:
        author_str = ", ".join(authors[:6]) + ", et al"
    else:
        author_str = ", ".join(authors)

    # Title — preserve final period
    title_str = title.strip().rstrip(".") + "."

    # Journal — italics in markdown
    journal_str = journal.strip().rstrip(".") if journal else ""

    # Pagination block
    page_block = ""
    if meta["volume"]:
        page_block = meta["volume"]
        if meta["issue"]:
            page_block += f"({meta['issue']})"
        if meta["fpage"]:
            page_block += f":{meta['fpage']}"
            if meta["lpage"] and meta["lpage"] != meta["fpage"]:
                page_block += f"-{meta['lpage']}"
    elif meta["elocation"]:
        page_block = meta["elocation"]

    if year and journal_str:
        if page_block:
            citation_core = f"{author_str}. {title_str} *{journal_str}*. {year};{page_block}."
        else:
            citation_core = f"{author_str}. {title_str} *{journal_str}*. {year}."
    elif journal_str:
        citation_core = f"{author_str}. {title_str} *{journal_str}*."
    else:
        citation_core = f"{author_str}. {title_str} {year}."

    # Identifiers
    ids = []
    if doi:
        ids.append(f"doi:{doi}")
    if pmid:
        ids.append(f"PMID:{pmid}")
    if pmcid:
        ids.append(f"PMCID:{pmcid}")
    id_str = " " + " ".join(ids) if ids else ""

    return citation_core + id_str

def main():
    with open(CATALOG, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    # Alphabetical sort by filename (stable, predictable)
    rows.sort(key=lambda r: r["filename"].lower())

    bib = {}
    md_lines = ["# Bibliography — Numbered Reference List (Vancouver Style)\n",
                "Generated automatically from master catalog. Authors extracted from PMC XML where available; abbreviated where not.\n",
                "References cited as `[N]` in the manuscript.\n"]

    for i, row in enumerate(rows, 1):
        sid = row["filename"]
        citation = build_vancouver(
            study_id=sid,
            first_author_csv=row.get("first_author", ""),
            year=row.get("year", ""),
            title=row.get("title", ""),
            journal=row.get("journal", ""),
            doi=row.get("doi", ""),
            pmid=row.get("pmid", ""),
            pmcid=row.get("pmcid", ""),
        )
        bib[sid] = {"n": i, "vancouver": citation}
        md_lines.append(f"{i}. {citation}")

    # Save JSON map
    (ROOT / "bibliography.json").write_text(json.dumps(bib, indent=2, ensure_ascii=False), encoding="utf-8")
    # Save numbered markdown
    (ROOT / "bibliography.md").write_text("\n".join(md_lines), encoding="utf-8")

    print(f"Bibliography built: {len(bib)} entries")
    print(f"  - {ROOT / 'bibliography.json'}")
    print(f"  - {ROOT / 'bibliography.md'}")

    # Spot-check
    print("\nSample entries:")
    for sid in ["Niu_2008", "Bhargava_2010", "Cui_2025", "Beasley_2025", "Carpenito_2025"]:
        if sid in bib:
            print(f"  [{bib[sid]['n']}] {sid}: {bib[sid]['vancouver'][:150]}")

if __name__ == "__main__":
    main()
