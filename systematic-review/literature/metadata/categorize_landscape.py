#!/usr/bin/env python3
"""
Literature landscape categorization for 340 QS-A. baumannii abstracts.

Reads:  literature/abstracts-only/*.txt (340 abstracts)
        literature/full-text/*.xml      (~218 PMC XML, optional enrichment)
        literature/master_catalog.csv   (metadata)

Classifies each paper by:
  - Study type  (in_vitro, in_silico, animal_model, clinical, omics, review, methodology, other)
  - Topic tags  (multi-label, from a curated taxonomy)
  - Organism focus (a_baumannii_only, multi_species, eskape)
  - Intervention type (natural_product, synthetic_compound, phage, repurposed_drug,
                      nanoparticle, peptide, enzyme_qq, none)

Outputs:
  literature/categorized.csv
  systematic-review/03-literature-landscape.md
"""
import csv
import re
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from collections import Counter, defaultdict

LIT = Path(__file__).resolve().parent.parent
ROOT = LIT.parent
ABS_DIR = LIT / "abstracts-only"
FT_DIR = LIT / "full-text"
CATALOG = LIT / "master_catalog.csv"

# -------- Taxonomy --------
# Priority order matters: first match wins.
# Refined: clinical demoted, in_vitro promoted; "clinical isolates" alone is NOT clinical.
STUDY_TYPE_PATTERNS = [
    ("review",          [r"\bsystematic review\b", r"\bnarrative review\b", r"\bmini[- ]?review\b",
                         r"\bcritical review\b", r"\b(in )?this review\b", r"\bscoping review\b",
                         r"\bmeta[- ]?analysis\b", r"\bbibliometric\b"]),
    ("animal_model",    [r"\bmurine model\b", r"\bmouse model\b", r"\binfection model in mice\b",
                         r"\b(Galleria mellonella|G\. mellonella|wax[- ]?worm)\b",
                         r"\b(zebrafish|Danio rerio) (model|infection)",
                         r"\bC\. elegans (model|infection)\b",
                         r"\bin vivo (study|experiment|model|infection)"]),
    ("omics",           [r"\b(transcriptom(e|ic|ics)|RNA[- ]?seq|RNA sequencing)\b",
                         r"\bproteom(e|ic|ics)\b", r"\bmetabolom(e|ic|ics)\b",
                         r"\b(whole[- ]?genome sequenc|WGS)\b", r"\bcomparative genomic",
                         r"\b(pan[- ]?genom|core[- ]?genom)", r"\bmetagenom",
                         r"\bChIP[- ]?seq\b", r"\bATAC[- ]?seq\b"]),
    ("clinical",        [r"\b(case report|case series)\b",
                         r"\b(retrospective|prospective) (cohort|study|analysis)\b",
                         r"\b(cohort study|cross[- ]?sectional study)\b",
                         r"\b(treatment|clinical) outcomes?\b",
                         r"\bmortality rate\b", r"\b30[- ]?day mortality\b",
                         r"\b(randomi[sz]ed|clinical) trial\b",
                         r"\b(surveillance|epidemiologic(al)?) (study|analysis|investigation)\b",
                         r"\boutbreak (investigation|analysis|report)\b",
                         r"\b(hospital[- ]?acquired|nosocomial) (infection|pneumonia)\b.*\b(patient|incidence|outcome)",
                         r"\bventilator[- ]?associated pneumonia\b.*\b(patient|outcome)"]),
    ("in_silico",       [r"\bin silico\b", r"\bmolecular docking\b", r"\bmolecular dynamic",
                         r"\bMD simulation", r"\bvirtual screening\b",
                         r"\b(ADMET|DFT|QSAR)\b", r"\bhomology model",
                         r"\bpharmacophore\b", r"\b(computational|bioinformatic) (study|analysis|approach)"]),
    ("methodology",     [r"\b(novel method|new method|method development|protocol|assay development)\b",
                         r"\b(biosensor|reporter (strain|construct))\b",
                         r"\b(diagnostic|detection|identification) (method|tool|kit|assay)\b"]),
    ("in_vitro",        [r"\bin vitro\b", r"\bMIC\b", r"\bminimum inhibitory concentration\b",
                         r"\bbiofilm (formation|assay|inhibition|eradication)\b",
                         r"\bcrystal violet\b", r"\bcheckerboard\b", r"\bgrowth (curve|kinetics)\b",
                         r"\b(qRT[- ]?PCR|RT[- ]?qPCR)\b", r"\bantibiofilm activit",
                         r"\bantibacterial activit", r"\bisolated (from|colonies)\b"]),
]

TOPIC_PATTERNS = {
    "qsi_discovery": [r"\bquorum[- ]sensing inhibitor", r"\bQSI\b", r"\binhibits? (the )?quorum",
                      r"\battenuat(e|es|ed|ing).*virulence", r"\banti[- ]?quorum"],
    "quorum_quenching": [r"\bquorum[- ]?quench", r"\bQQ\b", r"\blactonase\b", r"\bacylase\b",
                         r"\baiiA\b", r"\bAHL[- ]?degrad"],
    "abaI_abaR_axis": [r"\babaI\b", r"\babaR\b", r"\babaM\b", r"\bLuxI[- /]?LuxR\b"],
    "ahl_chemistry": [r"\b(N[- ]?acyl[- ]?homoserine lactone|acyl[- ]?HSL|AHL)\b",
                      r"\b3[- ]?(OH[- ]?C12|hydroxy[- ]?dodecanoyl)",
                      r"\bautoinducer", r"\bsignal(ing|ling)? molecules?"],
    "biofilm": [r"\bbiofilm", r"\b(adhesion|attachment) to (surface|substrate)",
                r"\bextracellular polymeric substance", r"\bEPS\b", r"\bpellicle\b"],
    "virulence_factors": [r"\bvirulence (factor|gene|determinant)", r"\bmotility\b",
                          r"\b(twitching|swarming|swimming) motility", r"\bouter membrane vesicles?\b",
                          r"\bOMV\b", r"\bcapsul(e|ar)", r"\bsurface[- ]?associated motility\b",
                          r"\b(siderophore|acinetobactin)\b"],
    "antibiotic_resistance": [r"\b(carbapenem|colistin|tigecycline)[- ]?resistant",
                              r"\bMDR\b", r"\bXDR\b", r"\bpan[- ]?drug[- ]?resistant",
                              r"\bantibiotic resistance", r"\bcarbapenem(ase)?", r"\b(OXA|NDM|KPC)[- ]?\d+",
                              r"\bbla[A-Z]+\b", r"\befflux pump"],
    "gene_regulation": [r"\b(transcription(al)? regulat|two[- ]?component system|TCS\b|BfmR|BfmS|RstA|RstB)",
                        r"\bsigma factor\b", r"\bsmall RNA\b", r"\bsRNA\b", r"\bglobal regulator"],
    "phage_therapy": [r"\b(bacteriophage|phage)\b.*(therap|cocktail|lytic)", r"\bphage[- ]?antibiotic synerg",
                      r"\bphage therapy\b"],
    "nanoparticle": [r"\bnano(particle|composite|formulation|emulsion|capsule|sphere)",
                     r"\b(AgNP|AuNP|ZnO[- ]?NP)\b", r"\bniosom", r"\bliposom"],
    "natural_product": [r"\b(essential oil|plant extract|phytochemical|medicinal plant|herbal|secondary metabolite)",
                        r"\b(flavonoid|alkaloid|terpene|polyphenol|tannin|saponin|coumarin)\b",
                        r"\b(eugenol|carvacrol|thymol|curcumin|resveratrol|cinnamaldehyde|berberine|allicin)\b"],
    "peptide_amp": [r"\bantimicrobial peptide", r"\bAMP\b", r"\bdefensin\b", r"\bcathelicidin\b",
                    r"\bbacteriocin\b"],
    "drug_repurposing": [r"\b(repurpos|repositioning|drug repurpos)", r"\bFDA[- ]?approved drug"],
    "vaccine_immune": [r"\bvaccin", r"\bimmun(ization|ization|isation)\b", r"\bantibody\b",
                       r"\bantigen\b", r"\bimmune response"],
    "second_messenger": [r"\b(cyclic di[- ]?GMP|c[- ]?di[- ]?GMP|cdi GMP|cyclic[- ]?di[- ]?AMP|c[- ]?di[- ]?AMP|ppGpp|stringent response)"],
    "polymicrobial": [r"\b(polymicrobial|interspecies|inter[- ]?kingdom|co[- ]?culture|mixed[- ]?species)\b"],
    "iron_metabolism": [r"\b(iron acquisition|siderophore|acinetobactin|iron[- ]?limit|heme uptake)\b"],
    "epidemiology": [r"\b(epidemiolog|surveillance|outbreak|prevalence|antibiogram|ST\d+)\b"],
    "review_synthesis": [],  # filled if study_type == review
}

INTERVENTION_PATTERNS = {
    "natural_product":   [r"\b(essential oil|plant extract|phytochemical|herbal|medicinal plant)",
                          r"\b(eugenol|carvacrol|thymol|curcumin|berberine|allicin|cinnamaldehyde|catechin|quercetin|baicalin)\b"],
    "synthetic_compound":[r"\b(synthes(is|ized) (analog|derivative|compound)|small molecule)",
                          r"\b(novel compound|chemical synthesis|structure[- ]?activity)"],
    "phage":             [r"\b(bacteriophage|phage)\b"],
    "repurposed_drug":   [r"\b(repurpos|repositioning)", r"\bFDA[- ]?approved\b.*\bdrug"],
    "nanoparticle":      [r"\bnano(particle|composite|formulation|emulsion|capsule|sphere)",
                          r"\b(AgNP|AuNP|ZnO[- ]?NP)\b", r"\bniosom", r"\bliposom"],
    "peptide":           [r"\bantimicrobial peptide", r"\bAMP\b"],
    "enzyme_qq":         [r"\blactonase\b", r"\bacylase\b", r"\baiiA\b"],
    "antibody_vaccine":  [r"\bvaccin", r"\bmonoclonal antibody", r"\bmAb\b"],
}

ORGANISM_PATTERNS = {
    "multi_species": [r"\bESKAPE\b", r"\bmulti[- ]?species\b", r"\b(co|poly)[- ]?microbial",
                      r"\b(P\.|Pseudomonas) aeruginosa\b.*\b(A\.|Acinetobacter) baumannii\b",
                      r"\b(A\.|Acinetobacter) baumannii\b.*\b(P\.|Pseudomonas) aeruginosa\b",
                      r"\bgram[- ]?negative (pathogen|bacteri)"],
    "a_baumannii_only": [],  # default
}

# -------- Text extraction --------

def extract_xml_text(xml_path):
    """Extract abstract + body text from PMC XML."""
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        # Collect text from abstract, body sections
        parts = []
        for elem in root.iter():
            tag = elem.tag.split('}')[-1] if '}' in elem.tag else elem.tag
            if tag in ('abstract', 'body', 'kwd'):
                text = ''.join(elem.itertext())
                parts.append(text)
        return '\n'.join(parts)
    except Exception:
        return ""

def read_abstract(stem):
    path = ABS_DIR / f"{stem}.txt"
    if path.exists():
        return path.read_text(encoding="utf-8", errors="replace")
    return ""

def read_fulltext(stem):
    """Prefer XML > TXT > nothing."""
    xml = FT_DIR / f"{stem}.xml"
    if xml.exists():
        return extract_xml_text(xml)
    txt = FT_DIR / f"{stem}.txt"
    if txt.exists():
        return txt.read_text(encoding="utf-8", errors="replace")
    return ""

# -------- Classification --------

def match_any(patterns, text):
    return any(re.search(p, text, re.IGNORECASE) for p in patterns)

def classify_study_type(text):
    """Return primary study type (first match in priority order)."""
    matches = []
    for stype, patterns in STUDY_TYPE_PATTERNS:
        if match_any(patterns, text):
            matches.append(stype)
    if not matches:
        return "other", []
    # Priority: review > in_silico+in_vitro combo allowed; clinical/omics separately
    primary = matches[0]
    return primary, matches

def classify_topics(text):
    tags = []
    for topic, patterns in TOPIC_PATTERNS.items():
        if patterns and match_any(patterns, text):
            tags.append(topic)
    return tags

def classify_intervention(text):
    interventions = []
    for itype, patterns in INTERVENTION_PATTERNS.items():
        if match_any(patterns, text):
            interventions.append(itype)
    return interventions

def classify_organism(text):
    if match_any(ORGANISM_PATTERNS["multi_species"], text):
        return "multi_species"
    return "a_baumannii_only"

# -------- Main --------

def main():
    # Load catalog metadata
    catalog = {}
    with open(CATALOG, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            catalog[r["filename"]] = r

    print(f"Loaded {len(catalog)} catalog entries")
    print(f"Abstracts available: {len(list(ABS_DIR.glob('*.txt')))}")
    print(f"Full text XML: {len(list(FT_DIR.glob('*.xml')))}")
    print()

    rows = []
    for stem, meta in catalog.items():
        abstract = read_abstract(stem)
        fulltext = read_fulltext(stem)
        # Prefer full text if substantial, else abstract
        text_for_classification = (abstract + "\n" + fulltext) if abstract else fulltext
        if not text_for_classification.strip():
            # No content — flag and skip classification
            rows.append({
                "filename": stem, "year": meta.get("year", ""),
                "title": meta.get("title", ""), "journal": meta.get("journal", ""),
                "has_fulltext": "no", "study_type": "no_text",
                "study_type_all": "", "topics": "", "interventions": "",
                "organism_focus": "", "n_topics": 0,
            })
            continue

        study_type, all_types = classify_study_type(text_for_classification)
        topics = classify_topics(text_for_classification)
        interventions = classify_intervention(text_for_classification)
        organism = classify_organism(text_for_classification)
        if study_type == "review":
            topics.append("review_synthesis")

        rows.append({
            "filename": stem,
            "year": meta.get("year", ""),
            "title": meta.get("title", "")[:200],
            "journal": meta.get("journal", ""),
            "doi": meta.get("doi", ""),
            "pmid": meta.get("pmid", ""),
            "has_fulltext": "yes" if fulltext else "abstract_only",
            "study_type": study_type,
            "study_type_all": "|".join(all_types),
            "topics": "|".join(topics),
            "interventions": "|".join(interventions),
            "organism_focus": organism,
            "n_topics": len(topics),
        })

    # Write categorized CSV
    out_csv = LIT / "categorized.csv"
    fieldnames = ["filename", "year", "title", "journal", "doi", "pmid",
                  "has_fulltext", "study_type", "study_type_all",
                  "topics", "interventions", "organism_focus", "n_topics"]
    with open(out_csv, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print(f"Categorized: {out_csv} ({len(rows)} rows)")

    # ---- Summary statistics ----
    n_total = len(rows)
    n_with_fulltext = sum(1 for r in rows if r["has_fulltext"] == "yes")
    n_no_text = sum(1 for r in rows if r["study_type"] == "no_text")

    study_type_counts = Counter(r["study_type"] for r in rows if r["study_type"] != "no_text")
    topic_counts = Counter()
    for r in rows:
        for t in r["topics"].split("|"):
            if t:
                topic_counts[t] += 1
    intervention_counts = Counter()
    for r in rows:
        for i in r["interventions"].split("|"):
            if i:
                intervention_counts[i] += 1
    organism_counts = Counter(r["organism_focus"] for r in rows if r["organism_focus"])
    year_counts = Counter(r["year"] for r in rows if r["year"])
    journal_counts = Counter(r["journal"] for r in rows if r["journal"])

    # Cross-tabulation: study_type × top topics
    crosstab = defaultdict(lambda: Counter())
    for r in rows:
        if r["study_type"] == "no_text":
            continue
        for t in r["topics"].split("|"):
            if t:
                crosstab[r["study_type"]][t] += 1

    # ---- Generate markdown landscape report ----
    md = []
    md.append("# Literatür Haritası — QS in *A. baumannii*")
    md.append("")
    md.append(f"> Otomatik kategorizasyon (anahtar-kelime tabanlı NLP) ile **{n_total} makale** taranmıştır.")
    md.append(f"> Bu rapor sistematik review için **karakteristik tablosu taslağı** olarak hizmet eder ve veri çıkarım formu tasarımını bilgilendirir.")
    md.append("")
    md.append("## Genel Sayılar")
    md.append("")
    md.append(f"- **Toplam makale:** {n_total}")
    md.append(f"- **Tam metin (XML/PDF/TXT):** {n_with_fulltext} ({100*n_with_fulltext/n_total:.0f}%)")
    md.append(f"- **Sadece abstract:** {n_total - n_with_fulltext - n_no_text}")
    md.append(f"- **Hiç metin yok (klasifikasyon dışı):** {n_no_text}")
    md.append("")

    md.append("## Yıl Dağılımı")
    md.append("")
    md.append("| Yıl | Makale | Trend |")
    md.append("|---|---|---|")
    for y in sorted(year_counts.keys(), reverse=True)[:20]:
        bar = "█" * year_counts[y]
        md.append(f"| {y} | {year_counts[y]} | {bar} |")
    md.append("")

    md.append("## Çalışma Tipi Dağılımı")
    md.append("")
    md.append("> Birincil sınıflandırma — bir makale birden fazla tipte olsa bile (örn. in vitro + in silico) en yüksek-öncelikli tipe atanır.")
    md.append("")
    md.append("| Çalışma Tipi | Makale | % |")
    md.append("|---|---|---|")
    for stype, n in study_type_counts.most_common():
        md.append(f"| `{stype}` | {n} | {100*n/n_total:.1f}% |")
    md.append("")

    md.append("## Konu Etiketleri (multi-label)")
    md.append("")
    md.append("> Bir makale birden fazla etikete sahip olabilir. Yüzde, etiket var olan makalelerin oranıdır.")
    md.append("")
    md.append("| Konu | Makale | % |")
    md.append("|---|---|---|")
    for topic, n in topic_counts.most_common():
        md.append(f"| `{topic}` | {n} | {100*n/n_total:.1f}% |")
    md.append("")

    md.append("## Müdahale (Intervention) Tipi")
    md.append("")
    md.append("> Hangi tip ajanların QS'i hedeflediği. PICO çerçevesi için kritik.")
    md.append("")
    md.append("| Müdahale | Makale | % |")
    md.append("|---|---|---|")
    for itype, n in intervention_counts.most_common():
        md.append(f"| `{itype}` | {n} | {100*n/n_total:.1f}% |")
    md.append("")

    md.append("## Organizma Odağı")
    md.append("")
    md.append("| Odak | Makale | % |")
    md.append("|---|---|---|")
    for org, n in organism_counts.most_common():
        md.append(f"| `{org}` | {n} | {100*n/n_total:.1f}% |")
    md.append("")

    md.append("## En Sık Dergi (Top 15)")
    md.append("")
    md.append("| Dergi | Makale |")
    md.append("|---|---|")
    for j, n in journal_counts.most_common(15):
        md.append(f"| {j} | {n} |")
    md.append("")

    md.append("## Çapraz Tablo: Çalışma Tipi × Konu")
    md.append("")
    md.append("> Hangi konuda hangi çalışma tipi baskın? Veri sentezi alt-grupları için önemli.")
    md.append("")
    # Top 8 topics × all study types
    top_topics = [t for t, _ in topic_counts.most_common(10)]
    header = "| Çalışma Tipi \\ Konu | " + " | ".join(top_topics) + " |"
    md.append(header)
    md.append("|" + "---|" * (len(top_topics) + 1))
    for stype in [s for s, _ in study_type_counts.most_common()]:
        row = [f"`{stype}`"]
        for t in top_topics:
            row.append(str(crosstab[stype][t]))
        md.append("| " + " | ".join(row) + " |")
    md.append("")

    # PICO summary section
    md.append("## PICO Çerçevesi Özeti")
    md.append("")
    md.append("Bu kategorizasyon, IJAA için PICO unsurlarını ön-doldurmamıza yardım eder:")
    md.append("")
    md.append("- **P (Population):** *A. baumannii* — klinik izolatlar ({} makale), ESKAPE/çoklu-tür bağlamı ({} makale)".format(
        sum(1 for r in rows if r["study_type"] == "clinical"),
        organism_counts.get("multi_species", 0)
    ))
    md.append(f"- **I (Intervention):** QSI/QQ ajanları — doğal ürünler ({intervention_counts.get('natural_product', 0)}), sentetik bileşikler ({intervention_counts.get('synthetic_compound', 0)}), fajlar ({intervention_counts.get('phage', 0)}), nanopartiküller ({intervention_counts.get('nanoparticle', 0)}), enzim QQ ({intervention_counts.get('enzyme_qq', 0)}), repurposed ilaç ({intervention_counts.get('repurposed_drug', 0)})")
    md.append(f"- **C (Comparator):** Çoğunlukla kontrol (DMSO, untreated) veya monoterapi vs kombinasyon")
    md.append(f"- **O (Outcome):** Biyofilm inhibisyonu ({topic_counts.get('biofilm', 0)}), virülans azalması ({topic_counts.get('virulence_factors', 0)}), gen ekspresyonu ({topic_counts.get('gene_regulation', 0)}), MIC değişimi ({topic_counts.get('antibiotic_resistance', 0)})")
    md.append("")

    # Save
    out_md = ROOT / "03-literature-landscape.md"
    out_md.write_text("\n".join(md), encoding="utf-8")
    print(f"Landscape report: {out_md}")

    # ---- JSON summary for downstream use ----
    summary = {
        "n_total": n_total, "n_with_fulltext": n_with_fulltext,
        "study_type": dict(study_type_counts),
        "topics": dict(topic_counts),
        "interventions": dict(intervention_counts),
        "organism_focus": dict(organism_counts),
        "year_distribution": dict(year_counts),
        "top_journals": dict(journal_counts.most_common(20)),
    }
    (LIT / "landscape_summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Summary JSON: {LIT / 'landscape_summary.json'}")

if __name__ == "__main__":
    main()
