#!/usr/bin/env python3
"""Parse PubMed EFetch XML into a master CSV catalog + per-article abstract files."""
import xml.etree.ElementTree as ET
import csv
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
OUT_DIR = HERE.parent
ABSTRACT_DIR = OUT_DIR / "abstracts-only"
ABSTRACT_DIR.mkdir(parents=True, exist_ok=True)
CSV_PATH = OUT_DIR / "master_catalog.csv"

def slug(s: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "", s)
    return s or "Unknown"

def text(el):
    return "".join(el.itertext()).strip() if el is not None else ""

rows = []
seen_names = {}

for xml_file in sorted(HERE.glob("efetch_batch*.xml")):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for art in root.findall(".//PubmedArticle"):
        # Use SPECIFIC paths to avoid picking up data from ReferenceList
        medline = art.find("./MedlineCitation")
        article = medline.find("./Article") if medline is not None else None
        if article is None:
            continue
        pmid = text(medline.find("./PMID"))
        title = text(article.find("./ArticleTitle"))
        journal = text(article.find("./Journal/Title"))
        # Year — only from this article's own dates
        year = ""
        for path in ["./ArticleDate/Year", "./Journal/JournalIssue/PubDate/Year", "./Journal/JournalIssue/PubDate/MedlineDate"]:
            y = article.find(path)
            if y is not None and text(y):
                m = re.search(r"(19|20)\d{2}", text(y))
                if m:
                    year = m.group(0)
                    break
        # Authors — ONLY this article's AuthorList (direct child of Article)
        authors = []
        first_author_last = ""
        author_list = article.find("./AuthorList")
        if author_list is not None:
            for a in author_list.findall("./Author"):
                ln = text(a.find("LastName"))
                fn = text(a.find("ForeName"))
                if ln:
                    authors.append(f"{ln} {fn[:1] + '.' if fn else ''}".strip())
                    if not first_author_last:
                        first_author_last = ln
        # DOI + PMC — ONLY from PubmedData/ArticleIdList (NOT from ReferenceList!)
        doi = ""
        pmcid = ""
        ail = art.find("./PubmedData/ArticleIdList")
        if ail is not None:
            for aid in ail.findall("./ArticleId"):
                idtype = aid.get("IdType", "")
                val = text(aid)
                if idtype == "doi":
                    doi = val
                elif idtype == "pmc":
                    pmcid = val
        # Fallback: ELocationID may carry DOI if ArticleIdList didn't
        if not doi:
            for el in article.findall("./ELocationID"):
                if el.get("EIdType") == "doi":
                    doi = text(el)
                    break
        # Abstract — ONLY this article's abstract
        abstr_parts = []
        abs_el = article.find("./Abstract")
        if abs_el is not None:
            for ab in abs_el.findall("./AbstractText"):
                lbl = ab.get("Label")
                t = text(ab)
                if lbl:
                    abstr_parts.append(f"{lbl}: {t}")
                else:
                    abstr_parts.append(t)
        abstract = "\n\n".join(p for p in abstr_parts if p)
        # Publication types
        pub_types = [text(pt) for pt in article.findall("./PublicationTypeList/PublicationType")]
        # Filename: Author_Year(_n if collision)
        base = f"{slug(first_author_last) or 'Unknown'}_{year or 'XXXX'}"
        n = seen_names.get(base, 0) + 1
        seen_names[base] = n
        filename = base if n == 1 else f"{base}_{n}"
        # Save abstract file
        abs_path = ABSTRACT_DIR / f"{filename}.txt"
        with open(abs_path, "w", encoding="utf-8") as f:
            f.write(f"PMID: {pmid}\n")
            f.write(f"Title: {title}\n")
            f.write(f"Authors: {', '.join(authors)}\n")
            f.write(f"Journal: {journal}\n")
            f.write(f"Year: {year}\n")
            f.write(f"DOI: {doi}\n")
            f.write(f"PMC: {pmcid}\n")
            f.write(f"Publication types: {'; '.join(pub_types)}\n")
            f.write(f"URL: https://pubmed.ncbi.nlm.nih.gov/{pmid}/\n")
            if doi:
                f.write(f"DOI URL: https://doi.org/{doi}\n")
            if pmcid:
                f.write(f"PMC URL: https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/\n")
            f.write("\n--- Abstract ---\n")
            f.write(abstract or "[No abstract available]")
            f.write("\n")
        rows.append({
            "filename": filename,
            "pmid": pmid,
            "first_author": first_author_last,
            "year": year,
            "title": title,
            "journal": journal,
            "doi": doi,
            "pmcid": pmcid,
            "authors_count": len(authors),
            "pub_types": "; ".join(pub_types),
            "has_abstract": "yes" if abstract else "no",
            "open_access": "yes" if pmcid else "unknown",
        })

# Write CSV
with open(CSV_PATH, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

# Summary stats
total = len(rows)
with_pmc = sum(1 for r in rows if r["pmcid"])
with_doi = sum(1 for r in rows if r["doi"])
with_abs = sum(1 for r in rows if r["has_abstract"] == "yes")

print(f"Total articles parsed: {total}")
print(f"With PMC ID (likely OA full-text): {with_pmc}")
print(f"With DOI: {with_doi}")
print(f"With abstract: {with_abs}")
print(f"Master catalog: {CSV_PATH}")
print(f"Abstract files: {ABSTRACT_DIR}")
# Show year distribution
years = {}
for r in rows:
    years[r["year"]] = years.get(r["year"], 0) + 1
print("\nYear distribution:")
for y in sorted(years):
    print(f"  {y}: {years[y]}")
