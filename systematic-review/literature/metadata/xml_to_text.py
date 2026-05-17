#!/usr/bin/env python3
"""Convert PMC JATS XML full-texts to readable .txt files for screening."""
import xml.etree.ElementTree as ET
import csv
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent
FT_DIR = ROOT / "full-text"

def text(el):
    if el is None:
        return ""
    return "".join(el.itertext()).strip()

def render(el, depth=0):
    """Render JATS element to plain text with simple structure."""
    out = []
    tag = el.tag
    if tag == "title":
        t = text(el)
        if t:
            prefix = "\n\n" + ("#" * (depth + 1)) + " "
            out.append(prefix + t + "\n")
        return "".join(out)
    if tag == "sec":
        # Render title first then children
        title_el = el.find("title")
        if title_el is not None:
            out.append(render(title_el, depth))
        for child in el:
            if child.tag != "title":
                out.append(render(child, depth + 1))
        return "".join(out)
    if tag == "p":
        out.append("\n" + text(el) + "\n")
        return "".join(out)
    if tag in ("abstract", "body"):
        for child in el:
            out.append(render(child, depth))
        return "".join(out)
    if tag == "fig":
        cap = el.find(".//caption")
        out.append(f"\n[FIGURE: {text(cap)}]\n")
        return "".join(out)
    if tag == "table-wrap":
        cap = el.find(".//caption")
        out.append(f"\n[TABLE: {text(cap)}]\n")
        return "".join(out)
    # Default: recurse
    for child in el:
        out.append(render(child, depth))
    return "".join(out)

inventory = []
for xml_path in sorted(FT_DIR.glob("*.xml")):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
    except ET.ParseError:
        inventory.append({"file": xml_path.name, "status": "parse_error", "has_body": "no", "size": xml_path.stat().st_size})
        continue
    article = root.find(".//article") or root
    # Pull metadata
    title = text(article.find(".//article-title"))
    abstract_el = article.find(".//abstract")
    body_el = article.find(".//body")
    pmid_el = article.find('.//article-id[@pub-id-type="pmid"]')
    pmcid_el = article.find('.//article-id[@pub-id-type="pmc"]')
    doi_el = article.find('.//article-id[@pub-id-type="doi"]')

    parts = []
    parts.append(f"Title: {title}\n")
    parts.append(f"PMID: {text(pmid_el)}\n")
    parts.append(f"PMCID: PMC{text(pmcid_el)}\n")
    parts.append(f"DOI: {text(doi_el)}\n")
    parts.append("\n=== ABSTRACT ===\n")
    if abstract_el is not None:
        parts.append(render(abstract_el).strip() + "\n")
    else:
        parts.append("[Not available in XML]\n")
    parts.append("\n=== FULL TEXT ===\n")
    if body_el is not None:
        body_text = render(body_el).strip()
        parts.append(body_text + "\n")
        has_body = "yes"
    else:
        parts.append("[Full text not redistributable via PMC OA — use DOI link]\n")
        has_body = "no"

    txt_path = xml_path.with_suffix(".txt")
    txt_path.write_text("".join(parts), encoding="utf-8")
    inventory.append({
        "file": xml_path.stem,
        "status": "ok",
        "has_body": has_body,
        "size": xml_path.stat().st_size,
    })

# Write inventory CSV
INV_PATH = ROOT / "fulltext_inventory.csv"
with open(INV_PATH, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["file", "status", "has_body", "size"])
    w.writeheader()
    w.writerows(inventory)

# Summary
with_body = sum(1 for r in inventory if r["has_body"] == "yes")
without_body = sum(1 for r in inventory if r["has_body"] == "no")
print(f"Total XML converted: {len(inventory)}")
print(f"With full body text: {with_body}")
print(f"Without body (abstract-only on PMC): {without_body}")
print(f"Inventory: {INV_PATH}")
