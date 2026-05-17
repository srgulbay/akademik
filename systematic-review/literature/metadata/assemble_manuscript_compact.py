#!/usr/bin/env python3
"""Assemble the COMPACT (IJAA-submission) manuscript from *_compact.md sections.

Mirrors `assemble_manuscript.py` but:
  * reads section_*_compact.md (when present, with .md fallback)
  * targets ~7K-word manuscript (vs. ~15K comprehensive)
  * writes MANUSCRIPT_IJAA.md (not MANUSCRIPT.md)

Shares the bibliography, citation-resolver and reference-renumbering machinery
of the comprehensive build to guarantee internally consistent reference
numbering against the same 340-record corpus.
"""
import json
import re
import unicodedata
from pathlib import Path
from collections import OrderedDict

ROOT = Path(__file__).resolve().parent.parent.parent
SECTIONS = ROOT / "sections"
TABLES = ROOT / "tables"
BIB_JSON = ROOT / "bibliography.json"
EXTERNAL_REFS = ROOT / "supplementary" / "external_references.md"

with open(BIB_JSON, encoding="utf-8") as f:
    bib = json.load(f)

# Parse external references markdown table: "| Cited as | Full citation |"
external_refs = {}
if EXTERNAL_REFS.exists():
    for line in EXTERNAL_REFS.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*([A-Z][A-Za-z\-]+\s+\d{4})\s*\|\s*(.+?)\s*\|\s*$", line)
        if m:
            external_refs[m.group(1).strip()] = m.group(2).strip()


def norm_key(s):
    s = unicodedata.normalize("NFKD", s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', '', s.lower())


bib_normalized = {}
for sid, entry in bib.items():
    bib_normalized[norm_key(sid)] = (sid, entry["n"])

surname_year_index = {}
for sid, entry in bib.items():
    m = re.match(r'^(.+?)_(\d{4})(?:_(\d+))?$', sid)
    if m:
        surname, year, suffix = m.group(1), m.group(2), m.group(3) or ""
        key = (norm_key(surname), year, suffix)
        surname_year_index[key] = (sid, entry["n"])

citation_order = OrderedDict()


def resolve_one(citation_text):
    s = citation_text.strip().rstrip('.,')
    key = norm_key(s)
    if key in bib_normalized:
        return bib_normalized[key]
    m = re.match(r'^(.+?)\s+(\d{4})(?:[_\s]+(\d+))?$', s)
    if m:
        surname = m.group(1)
        year = m.group(2)
        suffix = m.group(3) or ""
        idx = surname_year_index.get((norm_key(surname), year, suffix))
        if idx:
            return idx
        idx = surname_year_index.get((norm_key(surname), year, ""))
        if idx:
            return idx
        nsurname = norm_key(surname)
        candidates = [(sid, n) for (s_norm, y, sfx), (sid, n) in surname_year_index.items()
                      if y == year and (s_norm.startswith(nsurname) or nsurname.startswith(s_norm))
                      and sfx == suffix]
        if len(candidates) == 1:
            return candidates[0]
        if candidates and not suffix:
            return candidates[0]
    return None


unresolved_citations = []
external_citation_order = OrderedDict()
external_counter = [10000]


def cite_replace(match):
    inner = match.group(1)
    parts = [p.strip() for p in re.split(r'[;,]', inner) if p.strip()]
    numbers = []
    for p in parts:
        result = resolve_one(p)
        if result:
            sid, n = result
            if sid not in citation_order:
                citation_order[sid] = n
            numbers.append(n)
            continue
        p_stripped = p.rstrip('.,').strip()
        if p_stripped in external_refs:
            if p_stripped not in external_citation_order:
                external_counter[0] += 1
                external_citation_order[p_stripped] = external_counter[0]
            numbers.append(external_citation_order[p_stripped])
            continue
        for lbl in external_refs:
            if lbl.lower() == p_stripped.lower():
                if lbl not in external_citation_order:
                    external_counter[0] += 1
                    external_citation_order[lbl] = external_counter[0]
                numbers.append(external_citation_order[lbl])
                break
        else:
            unresolved_citations.append(p)
            numbers.append(f"?{p}?")
            continue
    nums_sorted = sorted([x for x in numbers if isinstance(x, int)])
    flagged = [x for x in numbers if isinstance(x, str)]
    parts_str = [str(n) for n in nums_sorted] + flagged
    return f"[{','.join(parts_str)}]"


CITATION_RE = re.compile(r'\[([^\[\]\n]{2,300}?\b\d{4}\b[^\[\]\n]{0,200})\]')


def resolve_citations(text):
    return CITATION_RE.sub(cite_replace, text)


def read_file_preferring_compact(stem):
    """Read sections/{stem}_compact.md if it exists, else sections/{stem}.md."""
    compact = SECTIONS / f"{stem}_compact.md"
    plain = SECTIONS / f"{stem}.md"
    if compact.exists():
        return compact.read_text(encoding="utf-8")
    if plain.exists():
        return plain.read_text(encoding="utf-8")
    return f"<!-- Missing section: {stem} -->\n"


def read_file(path):
    p = Path(path)
    if p.exists():
        return p.read_text(encoding="utf-8")
    return f"<!-- Missing: {p} -->\n"


def demote_headers(text, levels=1):
    def repl(m):
        new_hashes = "#" * (len(m.group(1)) + levels)
        if len(new_hashes) > 6:
            new_hashes = "######"
        return new_hashes + " "
    return re.sub(r"^(#+)\s+", repl, text, flags=re.MULTILINE)


def demote_table(text):
    lines = text.split("\n", 1)
    if len(lines) > 1 and lines[0].startswith("# "):
        return "###" + lines[0][1:] + "\n" + demote_headers(lines[1], 2)
    return text


# Compose
parts = []

parts.append("""# Quorum Sensing in *Acinetobacter baumannii*: Molecular Architecture, Therapeutic Targeting and Translational Horizons — A Systematic Review (2003–2025)

**Authors:** *To be completed at submission*
**Corresponding author:** *To be completed*
**Affiliations:** *To be completed*
**Submitted to:** *International Journal of Antimicrobial Agents (IJAA)*
**Manuscript type:** Systematic Review (compact submission variant)
**Protocol:** Prospectively developed; archived as `01-protocol.md`
**PRISMA 2020 compliance:** Supplementary S1
**Extended synthesis:** Supplementary S9 (long-form ~15K-word variant)

---
""")

parts.append("""## Highlights

- AbaI/AbaR QS integrates BfmRS, AdeRS and nucleotide messengers in *A. baumannii*.
- Phage cocktails are the most clinically advanced QS-modulating modality for CRAB.
- Sub-MIC QSIs cut biofilm by 50–80% across natural-product and synthetic chemotypes.
- In vivo evidence is modest; ARRIVE 2.0 adherence and clinical PK data are limited.
- No QSI has progressed beyond Phase I; QSI–antibiotic adjuncts are nearest-term.

---
""")

parts.append("""## Abstract

**Background.** *Acinetobacter baumannii* — particularly its carbapenem-resistant (CRAB) and extensively drug-resistant (XDR) phenotypes — is a WHO Priority-1 critical pathogen with a constrained antibiotic pipeline. Quorum sensing (QS) coordinates biofilm formation, virulence-factor expression and resistance signalling, and has emerged as a tractable anti-virulence target.

**Objective.** To systematically characterise (i) the molecular architecture of the *A. baumannii* QS network, (ii) the spectrum of QS-targeting interventions and their effect sizes, (iii) the state of in vivo and clinical evidence, and (iv) the methodological quality of the field.

**Methods.** PRISMA 2020-, PRISMA-S- and SWiM-compliant systematic review. MEDLINE/PubMed was searched (1 Jan 2003 – 31 Dec 2025) and supplemented with OpenAlex/Crossref API queries; records were de-duplicated by DOI/PMID/title-year fingerprint. Two hundred and twenty-eight full-text papers underwent structured data and claim extraction. Methodological quality was appraised against design-appropriate frameworks (CRIS, SYRCLE, JBI/Newcastle-Ottawa, CHARMS-modified, MIQE/MINSEQE). Full methodological detail is provided in Supplementary S9.

**Results.** Three hundred and thirty-eight unique records met the eligibility criteria (264/340 PubMed records, 78%, independently corroborated by OpenAlex/Crossref). Publication rate has tripled since 2018, with 24% of the corpus in 2024–2025. In vitro (25%) and omics (20%) studies dominate; animal models contribute 15% and clinical studies 4%. Biofilm modulation (77%), antibiotic-resistance interaction (76%) and virulence attenuation (61%) lead topical coverage; the *abaI*/*abaR* axis is addressed in 52% of papers. Phages (20%) and natural products (15%) are the leading intervention classes; median in vitro biofilm-mass reductions cluster at 50–80% at sub-MIC. In vivo evidence comprises ~50 animal studies, predominantly *Galleria mellonella* and murine, with heterogeneous design and incomplete ARRIVE 2.0 adherence. Clinical evidence is limited to observational studies and pilot pharmacokinetic measurements (LC-MS/MS quantification of 3-OH-C12-HSL in burn-patient plasma). No QSI has progressed beyond Phase I.

**Conclusions.** QS targeting in *A. baumannii* is mechanistically credible and supported by accumulating preclinical data, but clinical translation is bottlenecked by formulation, pharmacokinetic characterisation and the absence of validated QS biomarkers. Adjunctive QSI–antibiotic combinations and phage cocktails are the nearest-term clinical strategies. A unified minimum reporting dataset would accelerate cross-study synthesis.

**Keywords:** *Acinetobacter baumannii*; quorum sensing; quorum quenching; AbaI; AbaR; biofilm; phage therapy; antimicrobial resistance; ESKAPE pathogens; systematic review.

---
""")

# Section 1 (file starts at "# 1." H1) — demote to H2 to sit under document title
s1 = demote_headers(read_file_preferring_compact("section_1_introduction"), 1)
# Section 2 likewise
s2 = demote_headers(read_file_preferring_compact("section_2_methods"), 1)

# Section 3.x compact files start at "## 3.X" — demote to "### 3.X" under "## 3. Results"
s3_3 = demote_headers(read_file_preferring_compact("section_3_3_molecular_network"), 1)
s3_4 = demote_headers(read_file_preferring_compact("section_3_4_interventions"), 1)
s3_5_6 = demote_headers(read_file_preferring_compact("section_3_5_3_6_invivo_clinical"), 1)
s3_9 = demote_headers(read_file_preferring_compact("section_3_9_quality_rob"), 1)

# Section 4_5 compact file starts at "## 4. Discussion" — leave at H2
s4_5 = read_file_preferring_compact("section_4_5_discussion_conclusion")

t1 = demote_table(read_file(TABLES / "table1_characteristics.md"))
t2 = demote_table(read_file(TABLES / "table2_interventions.md"))
t3 = demote_table(read_file(TABLES / "table3_qs_targets.md"))
f1 = demote_table(read_file(TABLES / "figure1_prisma_flow.md"))
f2 = demote_table(read_file(TABLES / "figure2_year_trends.md"))

parts.append(s1)
parts.append("\n---\n")
parts.append(s2)
parts.append("\n---\n")

parts.append("## 3. Results\n\n")
parts.append("### 3.1 Study selection\n\n")
parts.append(
    "The PRISMA 2020 study-selection flow is shown in **Figure 1**. The MEDLINE/PubMed "
    "search returned 340 records and was supplemented by OpenAlex (n=351) and Crossref "
    "(n=3,060) API queries; after de-duplication by DOI, PMID and fuzzy title-plus-year "
    "matching, 3,313 unique records were screened against the eligibility criteria. "
    "Following title/abstract screening and full-text eligibility assessment, 338 studies "
    "met the inclusion criteria (218 with full text retrieved). As an indexing-coverage "
    "validation, 264 of 340 PubMed records (78%) were independently re-discovered by "
    "OpenAlex and/or Crossref.\n\n"
)
parts.append(f1)
parts.append("\n")

parts.append("### 3.2 Characteristics of included studies\n\n")
parts.append(
    "Study-level characteristics are summarised in **Table 1**. The publication trajectory "
    "(**Figure 2**) shows a steady acceleration from a foundational era (2003–2010, n=9) to "
    "a recent expansion (2024–2025, n=81). Study designs are dominated by mechanistic in vitro "
    "work (25%) and omics-based investigations (20%); clinical evidence remains small but "
    "growing (4%). Topical coverage is led by biofilm biology (77%), interactions with "
    "antibiotic resistance (76%) and virulence-factor regulation (61%); the *abaI*/*abaR*/*abaM* "
    "axis appears in 52% of the corpus.\n\n"
)
parts.append(t1)
parts.append("\n")
parts.append(f2)
parts.append("\n")

parts.append(s3_3)
parts.append("\n")
parts.append(t3)
parts.append("\n")

parts.append(s3_4)
parts.append("\n")
parts.append(t2)
parts.append("\n")

parts.append(s3_5_6)
parts.append("\n")

parts.append("""### 3.7 Antibiotic resensitization and synergy

A consistent secondary outcome across the QSI literature is restoration of antibiotic susceptibility in MDR/XDR isolates. FICI < 0.5 (synergy) was reported for combinations of natural-product QSIs with carbapenems, colistin or tigecycline in several in vitro checkerboard assays, with representative effect magnitudes of 2–8-fold MIC reduction. Mechanistic explanations invoke QS-dependent transcriptional control of RND efflux pumps (*adeABC*, *adeFGH*, *adeIJK*) — pharmacological inhibition of AbaR-mediated transcription thereby reduces efflux and lowers effective MICs [Xie 2025; Lpez 2017; He 2015]. Phage–antibiotic synergy is well established for *A. baumannii*: lytic phages disrupting biofilms expose previously sessile cells to bactericidal antibiotics, with 1–3 log10 CFU additional reductions in animal wound and pneumonia models [Su 2025; Arazi 2025; deVilliersdelaNoue 2025; Elshamy 2025].

### 3.8 Cross-cutting outcome summary

The most frequently quantified outcomes across the corpus are:

| Outcome | Studies | Median effect | Notes |
|---|---:|---|---|
| Biofilm biomass reduction | ≈190 | 50–80% at sub-MIC | Wide assay heterogeneity |
| Motility inhibition | ≈110 | 40–70% reduction | Often qualitative |
| Virulence-factor reduction | ≈90 | 30–70% reduction | Mixed assays |
| MIC fold-change (adjunct QSI) | ≈75 | 2–8-fold | Strain-dependent |
| In vivo survival improvement | ≈40 | 20–60 ppt absolute gain | Mostly *G. mellonella* / murine |
| Gene expression of QS regulons | ≈100 | 2–10-fold reduction | Reference-gene heterogeneity |

Heterogeneity in reporting (units, normalisation, control choice) and sub-MIC concentration choices precluded formal pooled meta-analysis; the ranges above should therefore be read as descriptive distributions.

""")

parts.append(s3_9)
parts.append("\n---\n")
parts.append(s4_5)
parts.append("\n---\n")

draft = "".join(parts)
draft_resolved = resolve_citations(draft)

renumber_map = {}
new_n = 0
for sid in citation_order:
    new_n += 1
    renumber_map[citation_order[sid]] = new_n

external_renumber = {}
for ext_label, old_ext_n in external_citation_order.items():
    new_n += 1
    external_renumber[old_ext_n] = new_n


def renumber_citations(text):
    def repl(m):
        nums = m.group(1).split(",")
        out = []
        for n in nums:
            n = n.strip()
            if n.isdigit():
                old = int(n)
                if old in renumber_map:
                    out.append(str(renumber_map[old]))
                elif old in external_renumber:
                    out.append(str(external_renumber[old]))
                else:
                    out.append(n)
            else:
                out.append(n)
        nums_int = sorted([int(x) for x in out if x.isdigit()])
        nonnum = [x for x in out if not x.isdigit()]
        return f"[{','.join([str(x) for x in nums_int] + nonnum)}]"
    return re.sub(r"\[([^\[\]\n]{1,200})\]", repl, text)


draft_renum = renumber_citations(draft_resolved)

num_to_entry = {entry["n"]: (sid, entry["vancouver"]) for sid, entry in bib.items()}
refs_lines = []
for orig_n in sorted(renumber_map.keys(), key=lambda k: renumber_map[k]):
    sid, vanc = num_to_entry[orig_n]
    new = renumber_map[orig_n]
    refs_lines.append(f"{new}. {vanc}")

for ext_label, old_ext_n in sorted(external_citation_order.items(), key=lambda kv: external_renumber[kv[1]]):
    new = external_renumber[old_ext_n]
    refs_lines.append(f"{new}. {external_refs[ext_label]}")

final = (
    draft_renum
    + "\n\n## References\n\n"
    + "\n".join(refs_lines)
    + "\n\n---\n\n"
    + "## Supplementary Material\n\n"
    + "- **S1.** PRISMA 2020 checklist — `supplementary/S1_prisma2020_checklist.md`\n"
    + "- **S2.** Full search strategies for all databases — `02-search-strategies.md`\n"
    + "- **S3.** Multi-database merge log and de-duplication report — `literature/merged_unique.csv`, `literature/prisma_flow_data.json`\n"
    + "- **S4.** Data extraction form — `04-data-extraction-form.md`\n"
    + "- **S5.** Categorised corpus — `literature/categorized.csv`\n"
    + "- **S6.** Evidence claims database — `literature/evidence_claims.json`\n"
    + "- **S7.** Full bibliography (340 records) — `bibliography.md`\n"
    + "- **S8.** Citation shortlist (top 60 by importance) — `literature/citation_shortlist.csv`\n"
    + "- **S9.** Extended Synthesis — long-form (~15K-word) variant of this review with full methodological detail and extended discussion (`MANUSCRIPT_FINAL.docx`).\n"
)

words = len(re.findall(r"\w+", final))
ref_count = len(refs_lines)

unresolved_unique = sorted(set(unresolved_citations))

print("=== Manuscript Assembly (COMPACT / IJAA) ===")
print(f"Word count (overall, incl. refs): {words:,}")
print(f"References (cited): {ref_count} / 340 in bibliography")
print(f"Unresolved citations: {len(unresolved_unique)}")
if unresolved_unique:
    print("First unresolved (likely paper not in PubMed corpus):")
    for u in unresolved_unique[:20]:
        print(f"  - {u}")

final += f"\n\n---\n*Manuscript word count: {words:,} | Cited references: {ref_count}*\n"

out = ROOT / "MANUSCRIPT_IJAA.md"
out.write_text(final, encoding="utf-8")
print(f"\nWritten: {out}")
