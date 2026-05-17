#!/usr/bin/env python3
"""
Extract structured evidence claims from categorized literature.

For each paper, attempts to extract:
  - Key sentence(s) about the QS target, intervention, outcome
  - Quantitative findings (% reductions, MIC values, fold changes)
  - Mechanistic claims (gene/protein names mentioned)
  - Strain/model information

Strategy:
  1. Identify "must-cite" papers (seminal pre-2012, all 2024-2025, representative of each intervention)
  2. For each, parse abstract + (if available) full-text intro/results/conclusion sections
  3. Extract sentences containing key quantitative phrases
  4. Save as evidence_claims.json keyed by study_id

Outputs:
  literature/evidence_claims.json
  literature/citation_shortlist.csv (~50 papers ranked by importance)
"""
import csv
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from collections import defaultdict

LIT = Path(__file__).resolve().parent.parent
ABS_DIR = LIT / "abstracts-only"
FT_DIR = LIT / "full-text"
CATEGORIZED = LIT / "categorized.csv"
CATALOG = LIT / "master_catalog.csv"

# ---- Importance ranking ----
def importance_score(row):
    """Heuristic ranking — higher = more important to cite."""
    score = 0
    year = int(row["year"]) if row.get("year", "").isdigit() else 0

    # Foundational papers (2003-2012)
    if 2003 <= year <= 2012:
        score += 50

    # Very recent (last 2 years)
    if year >= 2024:
        score += 30

    # Review papers — important for synthesis context
    if row["study_type"] == "review":
        score += 20

    # Animal model / in vivo (rare and valuable)
    if row["study_type"] == "animal_model":
        score += 25

    # Omics (mechanistic depth)
    if row["study_type"] == "omics":
        score += 15

    # Clinical (rarest, most translational)
    if row["study_type"] == "clinical":
        score += 25

    # Topic richness — papers covering abaI/abaR + biofilm + virulence are central
    topics = row["topics"].split("|") if row["topics"] else []
    if "abaI_abaR_axis" in topics:
        score += 10
    if "biofilm" in topics and "virulence_factors" in topics:
        score += 5
    if "qsi_discovery" in topics:
        score += 8
    if "quorum_quenching" in topics:
        score += 5
    if "phage_therapy" in topics:
        score += 3

    # High-impact journals (rough proxy)
    journal = row.get("journal", "").lower()
    high_impact = ["nature", "cell", "lancet", "nejm", "pnas",
                   "nature communications", "nucleic acids research",
                   "antimicrob agents chemother", "antimicrobial agents and chemotherapy",
                   "international journal of antimicrobial",
                   "clinical microbiology reviews", "lancet infect"]
    for hi in high_impact:
        if hi in journal:
            score += 15
            break

    # Has full text → easier to verify claims
    if row["has_fulltext"] == "yes":
        score += 5

    return score

# ---- XML parsing ----
def get_xml_sections(xml_path):
    """Return dict with abstract, intro_text, results_text, conclusion_text."""
    sections = {"abstract": "", "intro": "", "results": "", "conclusion": ""}
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        for elem in root.iter():
            tag = elem.tag.split('}')[-1] if '}' in elem.tag else elem.tag
            if tag == 'abstract':
                sections["abstract"] += ' '.join(elem.itertext())
            elif tag == 'sec':
                sec_title = ''
                for c in elem:
                    ctag = c.tag.split('}')[-1] if '}' in c.tag else c.tag
                    if ctag == 'title':
                        sec_title = ' '.join(c.itertext()).lower()
                        break
                txt = ' '.join(elem.itertext())
                if any(w in sec_title for w in ('introduction', 'background')):
                    sections["intro"] += txt + '\n'
                elif any(w in sec_title for w in ('result', 'finding')):
                    sections["results"] += txt + '\n'
                elif any(w in sec_title for w in ('conclusion', 'discussion', 'summary')):
                    sections["conclusion"] += txt + '\n'
    except Exception as e:
        pass
    return sections

def read_text(stem):
    """Read available text for paper. Prefer XML sections, fall back to txt/abstract."""
    sections = {"abstract": "", "intro": "", "results": "", "conclusion": ""}
    xml_path = FT_DIR / f"{stem}.xml"
    if xml_path.exists():
        sections.update(get_xml_sections(xml_path))
    if not sections["abstract"]:
        abs_path = ABS_DIR / f"{stem}.txt"
        if abs_path.exists():
            sections["abstract"] = abs_path.read_text(encoding="utf-8", errors="replace")
    return sections

# ---- Claim extraction ----
QUANT_PATTERNS = [
    r"\b\d+\.?\d*\s*[-–]\s*\d+\.?\d*\s*(%|fold|mg/L|µg/m[lL]|ug/m[lL]|nM|µM|uM|mM|µg/mL)\b",
    r"\b\d+\.?\d*\s*(%|fold|mg/L|µg/m[lL]|ug/m[lL]|nM|µM|uM|mM|µg/mL)\b",
    r"\bMIC\b[^.]{0,80}\b\d+\.?\d*\s*(µg/m[lL]|ug/m[lL]|mg/L)",
    r"\b(reduc|inhibit|decreas|attenuat|suppress|abolish)[^.]{0,80}\b\d+\.?\d*\s*(%|fold|log)",
    r"\bp\s*[<=]\s*0\.\d+",
    r"\b(IC50|EC50|FIC|FICI)\b[^.]{0,60}\d+\.?\d*",
]

GENE_PATTERN = r"\b(abaI|abaR|abaM|bfmR|bfmS|rstA|rstB|csuA|csuB|csuC|csuD|csuE|ompA|bap|adeR|adeS|adeABC|adeFGH|adeIJK|pmrA|pmrB|hms|ata|pgaABCD)\b"

def extract_quant_claims(text):
    """Find sentences with quantitative results."""
    if not text:
        return []
    sentences = re.split(r'(?<=[.!?])\s+', text)
    claims = []
    for s in sentences:
        s = s.strip()
        if len(s) < 20 or len(s) > 400:
            continue
        for pat in QUANT_PATTERNS:
            if re.search(pat, s, re.IGNORECASE):
                claims.append(s)
                break
    # Deduplicate
    seen = set()
    out = []
    for c in claims:
        key = re.sub(r'\s+', '', c.lower())[:80]
        if key not in seen:
            seen.add(key)
            out.append(c)
    return out[:5]

def extract_genes_mentioned(text):
    """Find which QS-related genes are mentioned."""
    if not text:
        return []
    matches = re.findall(GENE_PATTERN, text, re.IGNORECASE)
    return sorted(set(m.lower() for m in matches))

def extract_strains(text):
    """Find strain names."""
    if not text:
        return []
    patterns = [
        r"\b(ATCC[\s-]?\d+)\b",
        r"\b(AB[\s-]?\d+)\b",
        r"\b(M\d{4}|ACICU|AYE|17978|19606|5075)\b",
    ]
    strains = []
    for p in patterns:
        strains.extend(re.findall(p, text))
    return sorted(set(strains))

def extract_one_sentence_summary(text, max_words=40):
    """Try to find the most informative single sentence (results+conclusion-like)."""
    if not text:
        return ""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    best = ""
    best_score = -1
    keywords = ["quorum sensing", "biofilm", "abaI", "inhibit", "reduce", "treatment",
                "demonstrate", "conclude", "show that", "result"]
    for s in sentences:
        s = s.strip()
        words = s.split()
        if not (10 <= len(words) <= max_words):
            continue
        kw_count = sum(1 for k in keywords if k in s.lower())
        if kw_count > best_score:
            best_score = kw_count
            best = s
    return best

# ---- Main ----
def main():
    # Load categorized data
    with open(CATEGORIZED, encoding="utf-8") as f:
        all_rows = list(csv.DictReader(f))

    # Score and rank
    for r in all_rows:
        r["importance"] = importance_score(r)

    all_rows.sort(key=lambda r: (-r["importance"], r["year"]))

    # Write citation shortlist (top 60)
    shortlist = all_rows[:60]
    with open(LIT / "citation_shortlist.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["rank", "filename", "year", "journal", "study_type", "topics",
                    "importance", "title"])
        for i, r in enumerate(shortlist, 1):
            w.writerow([i, r["filename"], r["year"], r["journal"], r["study_type"],
                         r["topics"], r["importance"], r["title"]])
    print(f"Citation shortlist: top 60 papers written to citation_shortlist.csv")

    # Extract claims for shortlist + a few more (focus on full-text-available)
    extract_targets = [r for r in all_rows if r["importance"] >= 25 or r["year"] in ("2024", "2025")]
    # Also force-include seminal pre-2010
    seminal = [r for r in all_rows if r["year"] and r["year"].isdigit() and int(r["year"]) <= 2012]
    extract_targets = list({r["filename"]: r for r in extract_targets + seminal}.values())

    print(f"Extracting claims for {len(extract_targets)} priority papers...")

    claims_db = {}
    for r in extract_targets:
        stem = r["filename"]
        sections = read_text(stem)
        full_text = " ".join(sections.values())

        claims_db[stem] = {
            "year": r["year"],
            "journal": r["journal"],
            "title": r["title"],
            "doi": r.get("doi", ""),
            "pmid": r.get("pmid", ""),
            "study_type": r["study_type"],
            "topics": r["topics"].split("|") if r["topics"] else [],
            "interventions": r["interventions"].split("|") if r["interventions"] else [],
            "importance": r["importance"],
            "has_fulltext": r["has_fulltext"],
            "one_sentence": extract_one_sentence_summary(sections.get("abstract", "") or full_text),
            "quantitative_claims": extract_quant_claims(full_text),
            "genes_mentioned": extract_genes_mentioned(full_text),
            "strains_mentioned": extract_strains(full_text),
        }

    out_path = LIT / "evidence_claims.json"
    out_path.write_text(json.dumps(claims_db, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Evidence claims: {out_path} ({len(claims_db)} papers)")

    # Summary stats
    n_with_quant = sum(1 for c in claims_db.values() if c["quantitative_claims"])
    n_with_genes = sum(1 for c in claims_db.values() if c["genes_mentioned"])
    print(f"  - Papers with extracted quantitative claims: {n_with_quant}")
    print(f"  - Papers with QS gene mentions: {n_with_genes}")

    # Most-mentioned genes across the dataset
    gene_counts = defaultdict(int)
    for c in claims_db.values():
        for g in c["genes_mentioned"]:
            gene_counts[g] += 1
    print(f"\nTop QS genes/regulators mentioned across {len(claims_db)} priority papers:")
    for g, n in sorted(gene_counts.items(), key=lambda x: -x[1])[:15]:
        print(f"  {g:15s} {n}")

if __name__ == "__main__":
    main()
