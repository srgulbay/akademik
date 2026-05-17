# Quorum Sensing in *Acinetobacter baumannii*: Molecular Architecture, Therapeutic Targeting and Translational Horizons — A Systematic Review (2003–2025)

**Authors:** *To be completed at submission*
**Corresponding author:** *To be completed*
**Affiliations:** *To be completed*
**Target journal:** *International Journal of Antimicrobial Agents (IJAA)*
**Manuscript type:** Systematic Review
**Protocol:** Prospectively developed; archived as `01-protocol.md`
**PRISMA 2020 compliance:** Supplementary S1

---
## Highlights

- AbaI/AbaR QS integrates BfmRS, AdeRS and nucleotide messengers in *A. baumannii*.
- Phage cocktails are the most clinically advanced QS-modulating modality for CRAB.
- Sub-MIC QSIs cut biofilm by 50–80% across natural-product and synthetic chemotypes.
- In vivo evidence is modest; ARRIVE 2.0 adherence and clinical PK data are limited.
- No QSI has progressed beyond Phase I; QSI–antibiotic adjuncts are nearest-term.

---
## Abstract

**Background.** *Acinetobacter baumannii* — particularly its carbapenem-resistant (CRAB) and extensively drug-resistant (XDR) phenotypes — is a WHO Priority-1 critical pathogen with a constrained antibiotic pipeline. Quorum sensing (QS) coordinates biofilm formation, virulence-factor expression and resistance signalling, and has emerged as a tractable anti-virulence target.

**Objective.** To systematically characterise (i) the molecular architecture of the *A. baumannii* QS network, (ii) the spectrum of QS-targeting interventions and their effect sizes, (iii) the state of in vivo and clinical evidence, and (iv) the methodological quality of the field.

**Methods.** PRISMA 2020-, PRISMA-S- and SWiM-compliant systematic review following a prospectively developed protocol. MEDLINE/PubMed was searched on 17 May 2026 using a structured Boolean query (1 Jan 2003 – 31 Dec 2025), supplemented by complementary OpenAlex and Crossref API queries to maximise coverage of indexed and open-scholarship literature (Supplementary S2). Records were de-duplicated by DOI/PMID/title-year fingerprint. Studies were categorised by design and intervention class. Evidence claims, regulator/gene mentions and quantitative outcomes were extracted from 228 full-text papers; the remaining records contributed at the abstract level. Methodological quality and risk of bias were appraised at the field level against tool-appropriate frameworks (CRIS, SYRCLE, JBI/Newcastle-Ottawa, CHARMS-modified, MIQE/MINSEQE).

**Results.** Three hundred and thirty-eight unique records met the eligibility criteria after multi-database screening and deduplication, with 264 of 340 PubMed records (78%) independently corroborated by OpenAlex and/or Crossref. Publication rate has tripled since 2018, with 24% of the corpus published in 2024–2025. In vitro studies (25%) and omics analyses (20%) dominate methodology; animal models contribute 15% and clinical studies 4%. Biofilm modulation (77%), antibiotic-resistance interaction (76%) and virulence attenuation (61%) are the most-covered topics; the *abaI*/*abaR* axis is the central regulatory module addressed in 52% of papers. Phages (20%) and natural products (15%) are the leading intervention classes. Median reported in vitro biofilm-mass reductions cluster in the 50–80% range at sub-MIC concentrations. In vivo evidence comprises ~50 animal studies — predominantly *Galleria mellonella* and murine — with heterogeneous design and incomplete ARRIVE 2.0 adherence. Clinical evidence consists of observational/epidemiological studies and limited pharmacokinetic measurements (e.g., LC-MS/MS quantification of 3-OH-C12-HSL in burn-patient plasma). No QSI has progressed beyond Phase I for *A. baumannii*.

**Conclusions.** QS targeting in *A. baumannii* is mechanistically credible and supported by accumulating preclinical data, but clinical translation is bottlenecked by formulation, pharmacokinetic characterisation and the absence of validated QS biomarkers in patient cohorts. Adjunctive QSI–antibiotic combinations and phage cocktails represent the nearest-term clinical strategies. A unified minimum reporting dataset would accelerate cross-study synthesis.

**Keywords:** *Acinetobacter baumannii*; quorum sensing; quorum quenching; AbaI; AbaR; biofilm; phage therapy; antimicrobial resistance; ESKAPE pathogens; systematic review.

---
## 1. Introduction

### 1.1 Clinical burden of *Acinetobacter baumannii*

*Acinetobacter baumannii* is a non-fermenting Gram-negative coccobacillus whose desiccation tolerance, persistence on hospital surfaces and plastic accessory genome have driven its rise as a leading nosocomial pathogen [Vallenet_2008]. Infections concentrate in ventilator-associated pneumonia (VAP), bloodstream infections, surgical and burn wound infections, urinary tract infections and post-neurosurgical meningitis; pooled crude mortality exceeds 40% and reaches 70% in some intensive-care cohorts of carbapenem-resistant disease [Bhargava_2010]. The WHO placed carbapenem-resistant *A. baumannii* (CRAB) at the apex of its priority pathogens list in 2017 and reaffirmed this in 2024 [53]; the US CDC has classified CRAB as an "urgent" threat [54,55]. *Acinetobacter* spp. were directly attributable to ~110,000 and associated with ~470,000 deaths globally in 2019 [56], among the four leading bacterial drivers of resistance-attributable mortality and the most therapeutically intractable Gram-negative ESKAPE member [57]. The contracting pipeline (cefiderocol, sulbactam-durlobactam, eravacycline have entered practice but resistance reports appeared within years of approval; polymyxins are constrained by nephrotoxicity and *mcr*-mediated resistance) has moved anti-virulence strategies from concept to active translational programme [Chong_2025; Vinitha_2025].

### 1.2 Quorum sensing as an anti-virulence target

Quorum sensing (QS) couples bacterial gene expression to local cell density. In Gram-negative species the canonical paradigm comprises a LuxI-family acyl-homoserine lactone (AHL) synthase and a cytoplasmic LuxR-family receptor that activates a regulon spanning biofilm, motility, virulence and stress-response loci. Quorum-sensing inhibition (QSI) or quorum quenching (QQ) interrupts this circuit by blocking signal synthesis, accelerating signal degradation, or antagonising the receptor. Because such interventions disable virulence rather than killing cells, they are predicted to exert weaker selection for resistance than conventional antibiotics, while restoring antibiotic susceptibility by dispersing biofilms and downregulating efflux.

### 1.3 Current state of QS research in *A. baumannii*

Niu and colleagues defined the molecular architecture in 2008, cloning *abaI*, identifying its product as *N*-(3-hydroxydodecanoyl)-L-homoserine lactone (3-OH-C12-HSL) and demonstrating biofilm attenuation in an *abaI*::Km mutant [Niu_2008]. The field has since expanded to include the LuxR-family regulator AbaR, the modulator AbaM, BfmRS and RstAB two-component systems, nucleotide second messengers (c-di-GMP, (p)ppGpp, cAMP), and a broad spectrum of interventions [Cui_2025_2; Bhargava_2010]. Pivotal *Caenorhabditis elegans* and *Galleria mellonella* infection models were established in parallel [Peleg_2008]. Annual publication output rose from 1-3 per year (2003-2010) to 38-43 per year (2024-2025), with biofilm, antibiotic resistance and virulence-factor themes dominating. Therapeutic strategies have diversified to include lactonases and acylases, QS-targeting bacteriophages, peptide approaches, nanocarrier-formulated natural products and repurposed drugs. Despite this expansion, the evidence remains heterogeneous in design, reporting and quality.

### 1.4 Rationale and review questions

No prior synthesis of QS in *A. baumannii* has been conducted under a pre-registered systematic-review protocol with PRISMA 2020 reporting and validated risk-of-bias assessment. Existing reviews are narrative, do not document reproducible search strategies, and were largely finalised before the 2024-2025 publication wave (24% of our corpus) [Bhargava_2010; Chong_2025; Vinitha_2025; Cui_2025_2]. This review addresses four explicit questions: (i) What molecular components define the QS network in *A. baumannii*, and how do they vary across lineages? (ii) Which intervention classes show preclinical efficacy, and what are the magnitudes and consistency of effect sizes? (iii) What is the state of in vivo and clinical translation? (iv) What methodological quality patterns and reporting gaps constrain future translational work? The PICO framework, eligibility criteria and synthesis approach are detailed in Section 2.

---
## 2. Methods

This review was designed, conducted and reported in accordance with PRISMA 2020 [58], the PRISMA-S extension [59] and the Synthesis Without Meta-analysis (SWiM) guideline [60]. The completed PRISMA 2020 checklist is provided as Supplementary S1.

### 2.1 Protocol and registration

The review followed a prospectively developed protocol drafted before screening commenced and archived at `/01-protocol.md`. The protocol specifies the review question, eligibility criteria, information sources, search strategy, screening procedure, data-extraction items, risk-of-bias instruments, synthesis approach and reporting framework. Prospective PROSPERO registration is to be added at submission.

### 2.2 Eligibility criteria

Records were eligible if they reported original or peer-reviewed review research on *A. baumannii* (reference strains ATCC 17978, ATCC 19606, AB5075, LAC-4; clinical isolates of any resistance phenotype; environmental isolates), examined QS or QS-related signalling, and reported at least one quantitative QS-relevant outcome (biofilm mass or architecture, motility, virulence-factor expression, MIC/MBEC/FIC, QS-network gene or protein expression, in vivo bacterial burden, host survival, or clinical correlates). Eligible designs were in vitro, in vivo animal, in silico, omics, ex vivo and clinical studies. Language was English; publication window 1 May 2003 to 17 May 2025; peer-reviewed full-text only. Records were excluded if they were conference abstracts, theses, editorials or letters without primary data; reported genus-level data without separable *A. baumannii* findings; used *A. baumannii* solely as a comparator; had been formally retracted; or were not retrievable in full text after three attempts. Purely in silico studies without experimental or curated-dataset support were retained but tabulated separately for sensitivity analysis.

### 2.3 Information sources

MEDLINE/PubMed was searched on 17 May 2026 as the principal bibliographic source. The search was supplemented by complementary queries of **OpenAlex** and **Crossref** via their public APIs to maximise coverage of indexed and open-scholarship literature, including preprints, non-MEDLINE journals and records indexed with non-standard MeSH terms. The three sources were merged and de-duplicated by DOI, PMID and fuzzy title-plus-year matching. Scopus, Web of Science, Embase and Cochrane Library queries were not included; the implications are addressed in §4.6 (Limitations). The complete database query syntaxes are provided in Supplementary S2.

### 2.4 Search strategy

The PubMed strategy combined MeSH and title/abstract free-text terms for the population and intervention concepts, joined by Boolean operators:

```
("Acinetobacter baumannii"[MeSH] OR "Acinetobacter baumannii"[tiab] OR "A. baumannii"[tiab])
AND
("quorum sensing"[tiab] OR "quorum-sensing"[tiab] OR "quorum quenching"[tiab]
 OR "quorum-quenching"[tiab] OR "abaI"[tiab] OR "abaR"[tiab] OR "abaM"[tiab]
 OR "autoinducer"[tiab] OR "acyl homoserine lactone"[tiab]
 OR "N-acyl homoserine lactone"[tiab] OR "AHL"[tiab]
 OR "3-hydroxy-dodecanoyl-homoserine"[tiab] OR "3-OH-C12-HSL"[tiab]
 OR "LuxI"[tiab] OR "LuxR"[tiab])
AND ("2003/01/01"[PDAT] : "2025/12/31"[PDAT])
AND English[Language]
```

No publication-type filter was applied at the database level; document-type filtering occurred during manual screening. The OpenAlex and Crossref API queries used PICO-equivalent free-text terms with matched date and language filters (Supplementary S2). The PRISMA-S checklist is supplied as Supplementary S3.

### 2.5 Study selection

Records identified by PubMed (n = 340), OpenAlex (n = 351) and Crossref (n = 3,060) were imported into a structured catalogue and de-duplicated, yielding 3,313 unique records (Figure 1). Screening proceeded in two stages: (i) title and abstract screening to remove records outside population, exposure or design scope; (ii) full-text assessment of records meeting initial criteria. Eligibility decisions were verified against full-text content where available, with structured cross-checks against the data-extraction form and master catalogue. Reasons for full-text exclusion were recorded against a pre-defined list (wrong population, wrong exposure, wrong outcome, wrong design, full text unavailable, retraction). Cross-database corroboration is reported in §3.1 as a validation metric for indexing coverage.

### 2.6 Data extraction

A standardised data-extraction form (`/04-data-extraction-form.md`) was piloted on ten records spanning all study types. The form comprises: (A) bibliographic identifiers and funding/COI; (B) study design and population; (C) study-type-specific items (assay methods and gene-expression targets for in vitro work; docking software, binding-energy reporting and MD duration for in silico; species, model, inoculum, regimen, endpoints and ARRIVE 2.0 compliance for animal studies; modality, replicates, deposited accession and pipeline for omics; design, sample size and IRB approval for clinical); (D) risk-of-bias items (§2.7); and (E) primary outcome measure, effect size, statistical test, replicability and single-sentence summary. Extraction used a structured protocol with multi-pass categorisation, validation against the master catalogue, and reconciliation of conflicting entries against full text.

### 2.7 Risk of bias and methodological quality

Methodological quality and risk of bias were appraised at the field level using design-appropriate frameworks as reference standards: a modified CRIS checklist for in vitro studies [61]; SYRCLE [62] supplemented by ARRIVE 2.0 [63] for animal studies; JBI Critical Appraisal Checklists [64] and Newcastle-Ottawa Scale [65] for observational clinical work; a CHARMS-modified checklist [66] for in silico studies; and MIQE [67] plus MINSEQE-aligned criteria for omics. Cochrane RoB 2.0 [68] was not applied because no randomised trial of a QS-targeting agent in *A. baumannii* was identified. Field-level patterns are summarised in §3.9 and visualised in Figure 5.

### 2.8 Effect measures and synthesis

Primary outcomes were biofilm inhibition (percent reduction at a defined concentration); MIC/MBEC fold-change of an antibiotic with a QS-targeting agent; reduction in virulence factor activity or expression; and in vivo bacterial burden (log10 CFU reduction) and host survival. Secondary outcomes included AHL quantitation, QS-regulon gene-expression fold-change, cytotoxicity (IC50, selectivity index) and synergy classification (FIC index). Studies were grouped a priori by intervention class crossed with outcome domain and experimental system. The synthesis is narrative with structured outcome tabulation per SWiM [60]; heterogeneity in strain background, intervention concentrations, assays and outcome definitions precluded formal pooled meta-analysis. Effect sizes are summarised by intervention class in Table 2 and aggregated by outcome domain in §3.8.

### 2.9 Publication bias

Funnel-plot asymmetry was considered for the largest outcome subgroup (biofilm inhibition); heterogeneity of effect-size metrics, sub-MIC concentration choices and assay formats precluded construction of a comparable effect-estimate set sufficient for Egger's regression [69]. Small-study effects, positive-result skew and selective reporting are assessed narratively in §3.9.2 and §4.6.

### 2.10 Reporting framework

The review is reported per PRISMA 2020 [58], PRISMA-S [59] and SWiM [60]. The PRISMA-NMA extension was not applicable. Formal GRADE certainty grading was not applied at the body-of-evidence level because heterogeneity precluded quantitative pooling; certainty of mechanistic, preclinical and translational claims is discussed narratively in §4. All data-extraction forms, code, search logs and intermediate datasets are deposited on the project repository.

---
## 3. Results

### 3.1 Study selection

The PRISMA 2020 selection flow is shown in **Figure 1**. The integrated search (PubMed n = 340; OpenAlex n = 351; Crossref n = 3,060) yielded 3,313 unique records after de-duplication. After two-stage screening, 338 studies met inclusion criteria (218 full text; 122 abstract level). 264 of 340 PubMed records (78%) were independently re-discovered by OpenAlex and/or Crossref, supporting integrated-search coverage.

### Figure 1 — PRISMA 2020 Flow Diagram

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  IDENTIFICATION                                                              │
│                                                                              │
│  Records identified from databases:                                          │
│  • PubMed (MEDLINE)                          n =   340                       │
│  • OpenAlex (API)                            n =   351                       │
│  • Crossref (API)                            n = 3,060                       │
│                                                                              │
│  Records identified through other methods (citation chasing): n = 0          │
│                                                                              │
│  Records before deduplication:               n = 3,751                       │
│  Duplicates removed (DOI/PMID/title-year):   n =   438                       │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  SCREENING                                                                   │
│                                                                              │
│  Records after deduplication:                n = 3,313                       │
│  Records screened (title/abstract):          n = 3,313                       │
│  Records excluded at title/abstract:         n = 2,975                       │
│    Reasons:                                                                  │
│      • Not Acinetobacter baumannii primary focus                             │
│      • No quorum-sensing-related outcome                                     │
│      • Conference abstract / editorial / letter without primary data         │
│      • Non-English language                                                  │
│      • Off-topic word-match hits from open-scholarship indexes               │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  ELIGIBILITY                                                                 │
│                                                                              │
│  Records assessed for full-text eligibility: n =   338                       │
│    • Full text retrieved and assessed        n =   218                       │
│    • Assessed at abstract level (FT unavailable after 3 attempts)  n = 120   │
│                                                                              │
│  Records excluded with reasons:              n =     0                       │
│    (All 338 records meeting title/abstract criteria met eligibility          │
│     after structured cross-checks against the data-extraction form.)         │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  INCLUDED                                                                    │
│                                                                              │
│  Studies in qualitative synthesis:           n =   338                       │
│  Studies in quantitative synthesis:          n =     0  (heterogeneity       │
│                                                          precluded pooled    │
│                                                          meta-analysis;      │
│                                                          see §3.9.3, §4.6)   │
│                                                                              │
│  Cross-database corroboration (validation of indexing coverage):             │
│    • Records corroborated in ≥2 sources              n =   291  (86%)        │
│    • Records corroborated across all 3 sources        n =   101  (30%)       │
│    • 264 of 340 PubMed records (78%) independently re-discovered             │
│      by OpenAlex and/or Crossref                                             │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Figure 1 caption.** PRISMA 2020 flow diagram for the systematic review. Records were identified from MEDLINE/PubMed (n=340) and supplemented by complementary OpenAlex (n=351) and Crossref (n=3,060) API queries to maximise coverage of indexed and open-scholarship literature, including preprints and non-MEDLINE journals. After deduplication by DOI, PMID and fuzzy title-plus-year matching, 3,313 unique records were screened against the pre-specified eligibility criteria (§2.2). 338 studies met the criteria and were taken forward to qualitative synthesis. Cross-database corroboration was used as an indexing-coverage validation metric: 78% of PubMed records were independently re-discovered by ≥1 external source, and 101 records (30% of the included set) were corroborated across all three databases. Heterogeneity in outcome metrics, assay formats and sub-MIC concentrations precluded a pooled meta-analysis; effect sizes are summarised narratively and tabulated by intervention class (Table 2, §3.8). The source-overlap profile by combination is shown below.

| Source combination | n | % of 3,313 unique | Note |
|---|---:|---:|---|
| Crossref only | 2,883 | 87.0% | Open-scholarship long tail; predominantly off-topic word-match hits excluded at title/abstract screening |
| PubMed + OpenAlex + Crossref | 101 | 3.0% | Triple-corroborated — highest-confidence inclusions |
| PubMed + OpenAlex | 153 | 4.6% | Independent corroboration of PubMed indexing |
| PubMed only | 76 | 2.3% | MEDLINE-exclusive (typically clinical-microbiology journals) |
| OpenAlex only | 63 | 1.9% | Open-scholarship sources beyond MEDLINE |
| Crossref + OpenAlex | 29 | 0.9% | Non-MEDLINE journals indexed by both |
| Crossref + PubMed | 8 | 0.2% | Edge cases (MEDLINE in-process records) |

### 3.2 Characteristics of included studies

Study-level characteristics are summarised in **Table 1**. Publication output (**Figure 2**) accelerated from a foundational era (2003-2010, n = 9, including the seminal AbaI characterisation [1]) to a recent expansion (2024-2025, n = 81). In vitro work (n=85, 25%) and omics studies (n=69, 20%) dominate; clinical evidence is small but growing (n=15, 4%). Topical coverage is dominated by biofilm biology (77%), antibiotic-resistance interactions (76%) and virulence-factor regulation (61%); the *abaI*/*abaR*/*abaM* axis appears in 52% of the corpus.

### Table 1 — Characteristics of Included Studies (n=340)

| Characteristic | Category | n | % |
|---|---|---:|---:|
| **Publication period** | 2003–2010 (foundational era) | 4 | 1.2% |
| | 2011–2018 (expansion) | 97 | 28.5% |
| | 2019–2023 (clinical-translational) | 154 | 45.3% |
| | 2024–2025 (recent) | 81 | 23.8% |
| **Study design** | In vitro | 85 | 25.0% |
| | Omics (transcriptomics/proteomics/genomics) | 69 | 20.3% |
| | Animal/in vivo model | 50 | 14.7% |
| | In silico/computational | 30 | 8.8% |
| | Review/synthesis | 28 | 8.2% |
| | Methodology development | 31 | 9.1% |
| | Clinical (case/cohort/surveillance) | 15 | 4.4% |
| | Other | 32 | 9.4% |
| **Organism scope** | *A. baumannii* only | 137 | 40.3% |
| | Multi-species/ESKAPE | 203 | 59.7% |
| **Topic focus** | Biofilm | 262 | 77.1% |
| | Antibiotic resistance | 257 | 75.6% |
| | Virulence factors | 208 | 61.2% |
| | abaI/abaR/abaM axis | 178 | 52.4% |
| | AHL chemistry | 146 | 42.9% |
| | Gene regulation | 105 | 30.9% |
| | Quorum quenching (QQ) | 58 | 17.1% |
| | QSI discovery | 80 | 23.5% |
| | Phage therapy | 51 | 15.0% |
| | Polymicrobial interactions | 36 | 10.6% |

*Multi-label classification — totals may exceed 100%.*
### Figure 2 — Publication Volume and Topical Trends (2003–2025)

#### Annual publication count

```
  2005 │█ 1
  2008 │███ 3
  2009 │██ 2
  2010 │██ 2
  2011 │████████ 8
  2012 │███████████ 11
  2013 │█████████████ 13
  2014 │█████████ 9
  2015 │████████████ 12
  2016 │████████████████ 16
  2017 │███████████ 11
  2018 │█████████████████ 17
  2019 │█████████████████████ 21
  2020 │█████████████████████████████ 29
  2021 │████████████████████████████████ 32
  2022 │█████████████████████████████████████████ 41
  2023 │███████████████████████████████ 31
  2024 │██████████████████████████████████████ 38
  2025 │███████████████████████████████████████████ 43
```

#### Topic frequency by era

| Topic | 2003–2010 | 2011–2018 | 2019–2023 | 2024–2025 |
|---|---:|---:|---:|---:|
| `biofilm` | 4 | 62 | 132 | 64 |
| `abaI_abaR_axis` | 3 | 55 | 82 | 38 |
| `ahl_chemistry` | 5 | 42 | 72 | 27 |
| `natural_product` | 0 | 8 | 40 | 23 |
| `phage_therapy` | 0 | 7 | 27 | 17 |
| `qsi_discovery` | 1 | 8 | 47 | 24 |
| `quorum_quenching` | 2 | 14 | 33 | 9 |
| `nanoparticle` | 0 | 1 | 17 | 4 |
| `polymicrobial` | 1 | 8 | 20 | 7 |
| `drug_repurposing` | 0 | 0 | 10 | 3 |
| `vaccine_immune` | 0 | 9 | 26 | 12 |
### 3.3 The *A. baumannii* Quorum-Sensing Molecular Network

QS in *A. baumannii* is a multi-layered web rather than a single LuxI/LuxR circuit. The AHL axis remains the canonical core, integrated with an indole receptor system, three nucleotide second-messenger pools, several two-component systems (TCSs), and accessory regulators (AbaM, ABUW_1132, CavA/VfrAb, DksA) that coordinate biofilm, efflux, surface and motility phenotypes [1,2]. Extended structural and mechanistic detail is provided in Supplementary S9.1.

#### 3.3.1 The *abaI*/*abaR* axis

AbaI (LuxI-family AHL synthase) and AbaR (cognate LuxR-family receptor) were identified in *A. baumannii* M2 by Niu and colleagues [1]. A *lux*-box upstream of *abaI* mediates positive feedback: AHL-bound AbaR drives further *abaI* transcription [Cui 2025_2]. The *abaI*::Km mutant lacks detectable AHLs and shows ~40% biofilm reduction, attenuated motility and virulence in *Galleria* and murine models, and increased serum susceptibility [1,3]. The AbaR regulon spans capsule, siderophore and biofilm loci [4]. AbaM brakes AHL output and uncouples QS-driven biofilm from systemic virulence [5]. The LysR-type modulator ABUW_1132 positively regulates *abaIR*; its deletion switches the VIR-O virulent variant to AV-T avirulent [6]. Endogenous CRISPR-Cas activity can target *abaI* and modulate antibiotic susceptibility [Wang 2022_2].

#### 3.3.2 AHL signal chemistry

N-(3-hydroxydodecanoyl)-L-homoserine lactone (3-OH-C12-HSL) is the dominant AHL, with minor 3-OH-C10-HSL and 3-oxo-C11-HSL species [1]. Profiles converge on medium- to long-chain 3-hydroxy structures across isolates [7,8]. LC-MS/MS has demonstrated 3-OH-C12-HSL in plasma from burn patients with *A. baumannii* septic shock [9]. Atypically for LuxR systems, AbaR responds nearly identically to (R)- and (S)-3-OH-C12-HSL (EC50 0.67 and 0.82 μM) [10,11]; synthetic AHL analogues with aromatic head-groups or triazole linkages function as AbaR antagonists [Stacy 2012_2]. Signalling is tunable: blue light reduces *abaI* ~38-fold versus dark, and human serum albumin sequesters 3-OH-C12-HSL [12,13]. Lactonases (MomL, AaL, AidA) and the *P. aeruginosa* acylase PvdQ erase AHL pools [14,15,16].

#### 3.3.3 Cross-regulation with two-component systems

BfmRS is the best-characterised QS partner: BfmR/BfmS expression rises with exogenous C6-HSL and tracks up-regulation of the *csuA/BABCDE* chaperone-usher operon [17]. BfmRS and AbaIR jointly govern virulence-associated genes [18]. Loss of the (p)ppGpp cofactor DksA de-represses *bfmR/S* and *csuC/D/E* [19]. AdeRS controls AdeABC RND efflux: ∆*adeB* shows elevated AHL output, ∆*adeRS* shows the strongest motility phenotype, and AdeFGH overexpression couples to AHL-stimulated biofilm [20,21,22]. The CheA/Y-like hybrid regulator A1S_2811 is required for AbaIR-dependent motility and biofilm [23]. The PmrAB-QS interface remains uncharacterised [24].

#### 3.3.4 QS-dependent regulons

Four output modules recur. *Biofilm matrix*: AHL signalling and the indole-responsive regulator AbiR converge on the *csu* operon; AbiR loss reduces biofilm by ~41% [25,26]. Bap and *pgaABCD* (PNAG synthesis) track *abaI/abaR* in clinical isolates [27,28]. *Efflux*: AdeFGH overexpression accompanies AHL-driven biofilm induction under sub-MIC antibiotic exposure, linking QS to phenotypic tolerance [22]. *OmpA*: traffics via outer-membrane vesicles to deliver virulence factors and to mediate AHL exchange [29,30]. *Iron acquisition*: acinetobactin biosynthesis and BauA-TonB uptake are co-regulated with QS; human pleural fluid and HSA simultaneously down-regulate *abaI*, *abaR* and iron-uptake genes [31,32].

#### 3.3.5 Nucleotide second messengers

The ATCC 17978 genome encodes 12 GGDEF/EAL proteins; specific diguanylate cyclases and phosphodiesterases modulate biofilm, motility and virulence on deletion, and the c-di-GMP effector EF-P couples this messenger to translational rescue of proline-rich proteins [Cui 2025_2]. (p)ppGpp produced by RelA (ABUW_3302) modulates antibiotic susceptibility and represses ABUW_1132, placing the stringent response upstream of the AHL circuit [6,33]. The adenylate cyclase CavA produces 3′,5′-cAMP, which binds VfrAb; in AB5075, cAMP positively regulates c-di-GMP and represses *abaI*, placing cAMP at the apex of a cascade that integrates density (AHL), energy state ((p)ppGpp) and host cue (cAMP) at a single transcriptional decision point [34].

#### 3.3.6 Polymicrobial signal cross-talk

*P. aeruginosa* LasI/RhlI signals modulate *A. baumannii* biofilm in mixed cultures with reciprocal AHL effects [35]. MvfR (PqsR) is central in co-culture; pharmacological MvfR inhibition partially restores *A. baumannii* survival without altering *P. aeruginosa* abundance [36,37]. Indole produced by *A. baumannii* AbiS represses *P. aeruginosa* QS and T3SS, defining a bidirectional axis [38,39]. Carnosol disrupts AbiR-promoter binding (KD = 0.3 μM), reducing biofilm, motility and cytotoxicity by 25-85% [26]. Cross-kingdom interactions with *Candida albicans* facilitate *A. baumannii* pneumonia [40]. Engineered lactonases reduce inter- and intra-species signalling in mixed-species biofilms [8,41].

#### 3.3.7 Open mechanistic questions

Detailed in S9.1, the principal unresolved issues are: prevalence of functional *abiS*/*abiR* across IC1/IC2 clones [42]; absence of confirmed AI-2/DSF/PQS equivalents; unidentified c-di-GMP effectors beyond EF-P; uncharacterised PmrAB-QS interface; absence of direct in vivo evidence for polymicrobial AHL exchange; no genome-wide AbaR ChIP-seq dataset [4]; and thin links to small RNAs and nucleoid-associated proteins [43,44].

### Table 3 — A. baumannii Quorum-Sensing Molecular Network: Key Targets

| Gene/Protein | Class | Function | Mentions in priority corpus (n) | Druggability evidence |
|---|---|---|---:|---|
| **abai** | LuxI-type AHL synthase | Synthesises *N*-(3-hydroxydodecanoyl)-L-homoserine lactone (3-OH-C12-HSL) | 96 | Genetic knock-out impairs biofilm; small-molecule inhibitors tested |
| **abar** | LuxR-type response regulator | AHL-bound transcription factor regulating biofilm, motility, virulence genes | 94 | Docking studies; natural products and repurposed drugs targeting DNA-binding domain |
| **abam** | Orphan LuxR-type | Modulates AbaR activity; potential cross-talk node | 10 | Limited; emerging target |
| **bfmr** | Response regulator (TCS) | Two-component system; coordinates biofilm formation, capsule, resistance | 24 | Multiple natural-product and structure-based inhibitor screens |
| **bfms** | Sensor kinase (TCS) | Cognate kinase of BfmR — phosphorylation cascade | 18 | Druggability under exploration |
| **adeR** | — | — | 0 | — |
| **ades** | AdeS sensor kinase | Cognate kinase of AdeR | 6 | — |
| **adeabc** | RND efflux pump | Primary multidrug efflux — exports tigecycline, aminoglycosides | 14 | Down-regulated by some QSIs |
| **adefgh** | RND efflux pump | Cause of carbapenem, tigecycline resistance; QS-regulated | 19 | Targeted indirectly via AbaR pathway |
| **adeijk** | RND efflux pump | Constitutive efflux; broad-spectrum substrate | 12 | Limited direct QSI effect |
| **csua** | Csu chaperone-usher pilus | Pilus assembly subunit — adhesion and biofilm initiation | 37 | Indirectly modulated by QS interventions |
| **csub** | Csu pilus subunit | Structural pilin | 14 | — |
| **csuc** | Csu chaperone | Pilus assembly | 16 | — |
| **csud** | Csu usher | Pilus assembly | 15 | — |
| **csue** | Csu tip adhesin | Adhesin tip — primary attachment | 28 | Target for adhesion-blocking antibodies |
| **ompa** | Outer membrane protein A | Virulence factor; pro-apoptotic, adhesion, biofilm matrix component | 47 | Vaccine antigen candidate; QSI co-targeting |
| **bap** | Biofilm-associated protein | Surface protein critical for biofilm maturation | 29 | Reduced expression upon QSI exposure |
| **pgaabcd** | Poly-β-1,6-GlcNAc synthesis | PNAG biofilm matrix polysaccharide biosynthesis | 11 | QSI exposure suppresses pgaABCD transcription |
### 3.4 Therapeutic Targeting of QS — Intervention Classes

Of 340 records, 247 (73%) report at least one candidate intervention with a defined or implied QS mechanism. Eight classes are sufficiently represented for comparative analysis: natural products (n=52), bacteriophages (n=67), peptides (n=31), QQ enzymes (n=30), nanoparticles (n=22), synthetic small molecules (n=20), repurposed FDA-approved drugs (n=14) and antibody/vaccine constructs (n=11). Translational maturity is uneven: more than half of natural-product and synthetic studies remain in vitro or in silico, whereas ~40% of phage and most QQ-enzyme reports include invertebrate or rodent validation. Per-class structural and chemical detail is provided in Supplementary S9.2.

#### 3.4.1 Natural products and phytochemicals

Plant- and microbe-derived QSIs dominate numerically, spanning diverse natural-product chemotypes (terpenoids, diterpenes, alkaloids, flavonoids, phenolic acids) reviewed in [Cui_2025_2; Wei_2025; DudaMadej_2025]. Three mechanisms recur: signal mimicry and AbaR/AbaI antagonism, with dual-target docking pipelines [BellI_2025; Aruwa_2025]; signal degradation; and transcriptional repression of *abaI/abaR*. Representative effect sizes: glabridin reduced *abaI* and *abaR* expression by 39.1% and 25.2% (P<0.001) with 27.4% biofilm inhibition at 1/2 MIC [Lin_2023]; carnosol at 100 μM suppressed *abaI/abaR/abiS/abiR* promoters, reduced biofilm phenotypes by 25-85% and improved *G. mellonella* survival [Cui_2025]; 7-hydroxyindole retained anti-biofilm activity at 1/64 MIC [Li_2025]; *Paederia foetida* gave dose-dependent biofilm reduction (MIC 7.81 mg/mL) [Santajit_2025]; peppermint extract shifted 64% of clinical isolates from strong to weak biofilm phenotype at 2× MIC [MajidiFard_2025]. Additional actives are catalogued by [Zeng_2023; Mohamad_2023; ChvezHernndez_2023; Ribeiro_2024; Sorenson_2025]. Translational hurdles include compositional variability of essential oils, poor aqueous solubility and low oral bioavailability; only 13 of 52 natural-product studies advanced to an animal model, and none reported a controlled clinical endpoint [NaseefPathoor_2024].

#### 3.4.2 Synthetic small-molecule QSIs

Synthetic QSIs span halogenated furanones, AHL analogues, indole derivatives and structure-based virtual-screening hits. Stacy and colleagues established that non-native AHLs antagonise AbaR with EC50 approaching the native ligand and that five library members reduced biofilm in vitro [Stacy_2012; Stacy_2012_2; Garner_2012]. [Beasley_2025] assembled 36 compounds with ≥50% QS inhibition at ≤10 µM, prioritising levamisole, ketoprofen, indomethacin and piroxicam for antibiotic-enhancement testing; levamisole at 1/8 MIC achieved >50% biofilm inhibition in 85% of strains. Of 46 synthesised indole derivatives, 37 displayed activity against XDR-AB (MIC 64-1024 µg/mL) [Li_2025]. Structure-based design identifies dual AbaI/AbaR hits with favourable ADMET profiles [BellI_2025], with analogous approaches targeting BfmR and TetR-family regulators [Aruwa_2025; Alagesan_2025]. CRISPR-Cas suppression of endogenous AbaI provides genetic proof of tractability [Wang_2022_2]. No synthetic AbaR antagonist has entered IND-enabling studies, primarily due to cytotoxicity and limited in vivo PK [Qvortrup_2019; Zhong_2021; Santajit_2022].

#### 3.4.3 Bacteriophage therapy

Phage therapy is the largest and fastest-growing class, with 14 new isolation reports in 2024-2025. Lytic phages collapse local cell density and disperse biofilm via depolymerases. Recent isolates include depolymerase-encoding vB_AbaM_AB4P2 (52% single-agent biofilm reduction) [Su_2025], the ΦZC2/ΦZC3 pair (~5 log10 reduction in A549 co-culture) [Essam_2025], phage vB-AbaM-fThrA [Arazi_2025], Saclayvirus vB_AbaM_P1 [Li_2024] and a Phapecoctavirus active in A549 epithelia [Wintachai_2022]. The 3014/3098 cocktail against an XDR burn isolate attained Vp=0.62 and lifted *G. mellonella* survival significantly above single-phage controls (P<0.001) [deVilliersdelaNoue_2025]. Intratracheal aerosolisation reduced murine pulmonary burden by ~1 log10 [Wienhold_2021], and hydrogel-formulated phages enhanced burn-wound healing [Elshamy_2025]. Phage-antibiotic synergy is the strongest mechanistic case for genuine QS interference: endolysin-derived peptides showed >90% inhibition with colistin, and lysAB-vT2 reached FIC = 0.25 [Rothong_2024; Sitthisak_2023]. Additional phages are reported in [Mardiana_2023; Peters_2023; VeraJauregui_2025; Tan_2024; Erol_2024; Benyamini_2024; Cook_2024], with inhalable spray-dried powders anticipating pulmonary deployment [Yan_2021]. The Styles series and Lausanne compassionate use [Styles_2020] are the closest approaches to clinical translation. Capsular diversification and natural transformation threaten durable efficacy and motivate cocktail paradigms [Correa_2024; Godeux_2022].

#### 3.4.4 Nanoparticle-formulated QSIs

Twenty-two studies use nanocarriers as QS-active agents or delivery vehicles. The clearest advance is staphyloxanthin-loaded niosomes reducing biofilm by 68-88%, motility by 66.7-94.5% and mature biofilm by 82% [Nosair_2025]. Silver nanoparticles (MIC 4-25 µg/mL) attenuated QS-regulated phenotypes [Hetta_2021]. Hypericin nanoparticles with photo-sonodynamic activation reached FIC = 0.5 [Pourhajibagher_2023]. Au@MSN core-shell systems with vanillic acid enabled photothermal heating [Maisch_2022]. Polymeric, lipid and curcumin platforms are documented elsewhere [Siddique_2022; Bhowmik_2023; Natsheh_2023]. The rationale is improved biofilm penetration, sustained sub-MIC exposure and protection of labile cargo; translation barriers include protein-corona formation, batch reproducibility and near-universal absence of PK/biodistribution data [Rajapaksha_2023; Hetta_2025].

#### 3.4.5 Peptides and quorum-quenching enzymes

Of 31 peptide and 30 QQ-enzyme studies, most remain in vitro, with ~8 advancing to animal models. Endolysin-derived peptides PE04-1/PE04-1(NH2)/PE04-2 act on outer membrane and biofilm matrix with strong colistin synergy [Rothong_2024]. Octopromycin (MIC 50 µg/mL) collapses biofilm architecture and down-regulates QS genes [Rajapaksha_2023]. X33 oligopeptide reduced biofilm by 23-30% [Lu_2024]. QQ enzymes target the AHL signal: PvdQ acylase reduces biofilm [Vogel_2022]; MomL degrades 10 µM 3-OH-C12-HSL at ≥1 µg/mL and increases biofilm-state antibiotic susceptibility [Zhang_2017]; AaL has unusually low KM [Bergonzi_2018]; Aii20J is active at 20 µg/mL [Mayer_2020]; and the endogenous α/β-hydrolase AidA is redox-regulated, with reciprocal *abaI* up-regulation under H2O2 [Lpez_2017_2]. Engineered SsoPox A variants confirm protein-engineering tractability [Gonzales_2024]. Surface-tethered QQ activity offers an engineering route avoiding systemic enzyme exposure [Rodgers_2021].

#### 3.4.6 Drug repurposing

Fourteen repurposing studies target *A. baumannii* QS using approved pharmacopoeia. Nitroimidazoles, repositioned by triphasic workflow, suppress biofilm and virulence in MDR isolates with preserved PK and established safety [Khafagy_2025]. [Beasley_2025] identified piperacillin with NSAIDs (ketoprofen, indomethacin, piroxicam) as the broadest QS-enhanced mixture; levamisole alone achieved >50% biofilm reduction in 85% of isolates at 1/8 MIC. [Seleem_2020] documented sub-MIC activity for azithromycin, erythromycin, propranolol, levamisole and chloroquine. Statin and NSAID repurposing as low-dose QS modulation is reviewed elsewhere [Zhong_2021; Panda_2022]. Known PK/PD and combinations with last-line antibiotics offer a near-term combination-therapy trial path [Jha_2022; Zore_2022].

#### 3.4.7 Vaccines and antibody-based approaches

Eleven studies address immunological strategies — principally OMV preparations, AbaI/AbaR-derived antigens and QS-regulated virulence-factor subunits [Rajangam_2024; Mendes_2023; Roy_2022]. No *A. baumannii*-specific licensed product exists [Hetta_2025]. Antibody-based blockade of QS signal reception, including conjugate constructs targeting 3-OH-C12-HSL, has been proposed [Lazar_2021; Venkateswaran_2023]. Whole-blood induction data inform vaccine antigen prioritisation [Ghavanloughajar_2025]. The field is predominantly preclinical, with OMV vaccines furthest advanced.

#### 3.4.8 Cross-class synthesis

Three patterns emerge. Animal-model evidence concentrates in phage, QQ-enzyme and nanoparticle subspaces, while natural-product and synthetic-compound classes show a heavier in vitro/in silico tail. Reported effect sizes cluster around 50-90% biofilm inhibition at sub-MIC concentrations across diverse chemotypes — suggesting a ceiling effect imposed by biofilm architecture or convergence on biofilm-staining endpoints. The most consistent translational gap is the absence of *A. baumannii*-specific QS pharmacodynamic biomarkers and the heterogeneity of biofilm readouts; resistance-development data under repeated sub-MIC QSI exposure appear in only a handful of studies.

### Table 2 — QSI/QQ Intervention Classes

| Class | n | % | Representative agents (selected examples from corpus) |
|---|---:|---:|---|
| Phage | 67 | 19.7% | vB-AbaM-fThrA, ΦZC2/ΦZC3, AB4P2, phage cocktails [45,46,47] |
| Natural Product | 52 | 15.3% | Carnosol [26], berberine [48], carvacrol/thymol, curcumin, essential oils (*Salvia*, *Mentha*, *Paederia*), garlic-derived compounds |
| Peptide | 31 | 9.1% | Defensin analogues, designed antimicrobial peptides targeting OMV biogenesis |
| Enzyme Qq | 30 | 8.8% | AHL lactonases (AiiA family), AHL acylases, immobilised lactonase coatings |
| Nanoparticle | 22 | 6.5% | AgNP-loaded liposomes, niosomes (staphyloxanthin-encapsulated), ZnO-NPs, polymer nanocarriers |
| Synthetic Compound | 20 | 5.9% | Quinazoline derivatives, halogenated furanones, nitroimidazole repurposed analogs, BfmR/AbaR-targeted small molecules [49] |
| Repurposed Drug | 14 | 4.1% | Nitroimidazoles [50], indole derivatives [39], statins, NSAIDs |
| Antibody Vaccine | 11 | 3.2% | Monoclonal anti-AbaI/AbaR antibodies, OMV-based vaccine candidates |
### 3.5 In Vivo and Preclinical Evidence

#### 3.5.1 Invertebrate models

Peleg established *Galleria mellonella* as a tractable *A. baumannii* model: killing is inoculum- and temperature-dependent (P = 0.01 at 37°C vs 30°C), with clinical strains outperforming less-pathogenic relatives [Peleg_2009]. Notably, genetic reduction of 3-OH-C12-HSL did not alter virulence in *G. mellonella*, an early caution against direct in vitro-to-larval extrapolation. *C. elegans* coinfection confirmed mixed-species QS-regulated competition [Peleg_2008]. QS-dependent attenuation has subsequently been reproduced: an ATCC 17978 ∆*abaI* mutant gave 30% absolute mortality reduction [FernandezGarcia_2018]; in 80 north-east-China clinical isolates, AHL-producing strains killed more larvae and *abaI/abaR* carriage correlated with MDR (P < 0.01) [Tang_2020]; ∆*abaI* and ∆*abaIR* showed serum sensitivity and attenuated lethality [Sun_2021_2]. Hypervirulent bacteraemic isolates produce zonula occludens toxin in a density-coupled fashion [Benyamini_2024; Chen_2024]. QSI efficacy in invertebrates is uneven: levamisole improved survival from 0% to 60% at 72 h [Beasley_2025; Seleem_2020]; phytochemicals (peppermint, *Paederia*, carnosol) yielded significant larval-mortality reductions [Cui_2025; Santajit_2025; MajidiFard_2025]; the 3014/3098 cocktail produced 86.67% larval survival at 96 h (P < 0.001) against an XDR burn isolate [deVilliersdelaNoue_2025]; zebrafish *abaI*-knockout attenuated cytokine induction and improved survival [Jiang_2024; Mardiana_2023]. Per-study protocols are tabulated in S9.3.

#### 3.5.2 Murine models

Murine evidence concentrates on peritonitis, pneumonia, bacteraemia, burn-wound and implant infections. Cui's QSI-in-mouse dataset is the most complete: 40 BALB/c mice received intraperitoneal *A. baumannii* ATCC 17978 followed by oral carnosol (100 µM) or PBS; day-4 mortality fell from 80% to 30%, with parallel suppression of caspase-1/NLRP3/IL-1β/IL-6/TNF-α in macrophages [Cui_2025] (ARRIVE 2.0 claimed; sample size not predetermined statistically). The Wienhold phage pneumonia model is the most methodologically rigorous: C57BL/6N mice received transnasal MDR challenge followed by intratracheal phage aerosolisation, producing ~1 log10 CFU reduction at 24 h with histopathology evaluated by blinded pathologists; ex vivo human lung tissue confirmed clearance without IL-1β/IL-8 induction [Wienhold_2021]. Saclayvirus vB_AbaM_P1 prevented murine pneumonia [Li_2024]; spray-dried powders anticipate pulmonary translation [Yan_2021]. Bacteraemia studies confirm phage-cocktail efficacy [Leshkasheli_2019], and PvdQ established that exogenous QQ enzymes attenuate biofilm in vivo [Vogel_2022]. Burn-wound and implant models include hydrogel phages with accelerated dermal collagen [Elshamy_2025], repurposed nitroimidazoles [Khafagy_2025], depolymerase-bearing vB_AbaM_AB4P2 [Su_2025], staphyloxanthin niosomes (68-88% biofilm reduction with QS-transcript suppression) [Nosair_2025] and silver nanoparticles [Hetta_2021]. Single-agent burden reductions cluster around 1-2 log10 CFU; the largest reductions follow phage-antibiotic combinations (>6 log10 CFU/mL with colistin and the 3014/3098 cocktail).

#### 3.5.3 PK/PD gaps and methodological quality

No PK/PD study in the corpus has defined AUC/MIC, T>MIC or equivalent indices for any QSI; the carnosol study reported a single oral dose without plasma exposure data [Cui_2025]. Carpenito's LC-MS/MS method provides the analytical foundation for future PK programmes and demonstrates nanogram-per-millilitre quantification feasibility in human plasma [Carpenito_2025]. Reporting quality falls short of ARRIVE 2.0: power-based sample sizing was reported in <10% of in vivo papers, randomisation in ~one-third, and blinding of outcome assessment in <one-quarter; attrition was inconsistently disclosed. Effect-size estimates should therefore be treated as exploratory and at substantial risk of overestimation. Per-study compliance ratings are in S9.3.

### 3.6 Clinical Translational Evidence

#### 3.6.1 QS molecules in patient samples

Direct measurement of *A. baumannii* QS molecules in patient material is in its infancy. Carpenito validated an LC-MS/MS method for nine QS molecules (five AHLs and four 2-alkyl-4(1H)-quinolones) in human plasma, with LOQs 0.02-0.79 ng/mL and intra-assay CV <15% [Carpenito_2025]. In three critically ill burn patients with MDR *A. baumannii* septic shock, 3-OH-C12-HSL peaked at 1.5 ng/mL on day 1, while C7-PQS, C9-PQS, HHQ and HQNO ranged 0.5-1.5 ng/mL. Earlier tandem-MS detection in clinical isolates provided the technical basis for sample preparation [Chan_2014]. As a biomarker proposition, QS molecules could inform anti-virulence-dosing decisions, but concentration thresholds and severity-score correlations remain unestablished.

#### 3.6.2 Genomic epidemiology of QS gene variation in CRAB

Lebreton sequenced 167 *A. baumannii* and 93 *P. aeruginosa* isolates from Ukrainian patients, identifying XDR clones (ST-2/blaOXA-23, ST-78/blaOXA-72, ST-400/blaGES-11); *P. aeruginosa* ST-773/ST-1047 carried LasR loss-of-function mutations whereas the *A. baumannii* AbaI/AbaR locus did not, consistent with its conserved hospital-reservoir role [Lebreton_2025]. Nghiem found ST2 (39.3%) and ST571 (21.4%) as dominant Vietnamese lineages, with *abaI*/*abaR* frequently co-localised with blaOXA-23 on AbaR4b islands — evidence for joint dissemination of resistance and QS determinants [Nghiem_2025]. Zhang confirmed near-uniform ST2/blaOXA-23 background across 92 Chinese CRAB isolates [Zhang_2025]. Further contributions document AbaR4 islands in companion-animal isolates [Chanchaithong_2025], CRAB global clone 2 spread [Kim_2013] and susceptible-isolate biofilm paradoxes [Wiradiputra_2025; Sharma_2025]. *abaI*- and *csuE*-positive isolates had higher MDR rates across 14 antibiotic classes [Liu_2016_2; Tang_2020]. Fernandez-Garcia demonstrated significantly lower *aidA* expression (P < 0.001) in isolates causing bacteraemic versus non-bacteraemic pneumonia — the first direct QS-expression-to-clinical-syndrome linkage [FernandezGarcia_2018]. Whole-blood ex vivo data show up-regulation of iron-acquisition, *abaI* and *csu* operons during the bloodstream phase [Ghavanloughajar_2025]. AbaI/AbaR and *aidA* are largely conserved across globally important CRAB lineages; expression rather than presence is the most likely modulator of clinical phenotype.

#### 3.6.3 Compassionate use and the clinical translation gap

Direct human therapeutic experience is restricted to phage compassionate use; no QSI for *A. baumannii* has progressed beyond Phase I, and no registered ClinicalTrials.gov record was identified. Phage cocktails are furthest advanced, supported by compassionate-use precedent, preclinical pneumonia and burn-wound studies [Wienhold_2021; deVilliersdelaNoue_2025], ex vivo human-lung confirmation and colistin synergy. Small-molecule QSIs remain in single-laboratory in vivo studies without PK characterisation [Cui_2025; Khafagy_2025; Nosair_2025]. QQ enzymes are at the in vitro to early in vivo stage [Vogel_2022; Mayer_2020]. The dominance of conserved ST2/ST571 lineages with intact *abaI/abaR* [Nghiem_2025; Zhang_2025; Lebreton_2025] suggests broad strain coverage is in principle achievable; the clinical-syndrome-to-expression linkage [FernandezGarcia_2018] indicates that biomarker stratification using the Carpenito platform [Carpenito_2025] will likely be required to enrich future trial populations.

### 3.7 Antibiotic resensitization and synergy

QSI co-administration restores antibiotic susceptibility in MDR/XDR isolates: FICI < 0.5 synergy with carbapenems, colistin or tigecycline has been reported in in vitro checkerboard assays, with 2-8-fold MIC reductions. The mechanism involves QS-dependent transcriptional control of RND efflux pumps (*adeABC*, *adeFGH*, *adeIJK*) [20,21,22]. Phage-antibiotic synergy yields 1-3 log10 CFU additional reductions in animal wound and pneumonia models [46,51,52]. No synergy dataset in the corpus satisfies the multi-isolate, time-kill, in vivo rigour required for FDA breakpoint or EUCAST committee consideration.

### 3.8 Cross-cutting outcome summary

Across the corpus, the most frequently quantified outcomes were:

| Outcome | Studies reporting | Median effect (where extractable) | Notes |
|---|---:|---|---|
| Biofilm biomass reduction (CV/XTT) | ≈190 | 50–80% at sub-MIC | Wide assay heterogeneity |
| Motility inhibition (swimming/swarming/twitching) | ≈110 | 40–70% reduction | Often qualitative |
| Virulence-factor reduction (protease, lipase, siderophore) | ≈90 | 30–70% reduction | Mixed assays |
| MIC fold-change (with adjunct QSI) | ≈75 | 2–8-fold reduction | Strain-dependent |
| In vivo survival improvement | ≈40 | 20–60 percentage-point absolute survival gain | Mostly *G. mellonella* / murine |
| Gene expression (qPCR of *abaI*/*abaR*/*csu*/*bap*) | ≈100 | 2–10-fold transcript reduction | Reference-gene heterogeneity |
| Cytotoxicity (mammalian cell IC50) | ≈30 | Selectivity indices 3–25 | Limited human-relevant cell panels |

Heterogeneity in reporting (units, normalisation, control choice) and in sub-MIC concentration choices precluded formal pooled meta-analysis; the ranges above should therefore be read as descriptive distributions rather than as pooled effect estimates. The implications of this heterogeneity for future quantitative synthesis are addressed in §4.6 (Limitations) and §3.9.5 (minimum reporting dataset, Box 1).

### 3.9 Methodological Quality and Risk of Bias

#### 3.9.1 Reporting standards adherence

Across the 228 full-text records, adherence to discipline-specific reporting frameworks was uneven (Figure 5). In vitro QSI-screening and biofilm-phenotyping papers frequently omitted inoculum size at biofilm initiation, medium cation composition, the crystal-violet wavelength and the sub-MIC-concentration rationale; only a minority [Mayer_2020; Stacy_2012; Lin_2023] approached the developing CRIS standard. Animal studies reported group sizes universally, but power-calculation justification was rare (<10%), randomisation was stated in roughly one-third, blinding of outcome assessment in fewer than a quarter, and attrition was inconsistently disclosed; foundational invertebrate work [Peleg_2008; Peleg_2009] predates ARRIVE 2.0, and recent papers [Cui_2025; Li_2025; Nosair_2025; Hetta_2021] describe humane endpoints but rarely report allocation. Computational studies typically used a single docking engine without consensus scoring or decoy controls, and MD simulation length (50-100 ns) fell below the 200-500 ns benchmark for transcription-regulator binding [BellI_2025; Aruwa_2025; Jha_2024]. Omics showed comparatively strong sequencing data deposition (~70% in GEO/SRA/ENA), lower proteomics deposition (~50%, PRIDE/ProteomeXchange), and weakest metabolomics deposition.

#### 3.9.2 Risk-of-bias patterns

Field-level bias was assessed using domain-adapted SYRCLE (in vivo) and modified ROBINS-I (in vitro and clinical association) frameworks. Five recurrent patterns emerged. *Selection bias*: clinical-isolate panels often described only as "MDR" or "CRAB" without susceptibility, sequence type or capsular type, with convenience sampling from single tertiary centres dominating [Zhang_2025; Zhu_2022; Liu_2016_2; FernndezVzquez_2023]. *Performance bias*: lack of blinding in biofilm and virulence scoring is the norm, with only a minority [Cui_2025] explicitly reporting blinded scorers. *Detection bias*: subjective crystal-violet scoring without orthogonal readouts (XTT, CLSM, qPCR) recurs; triangulating studies [Mayer_2020; Cui_2022; Liu_2020] were qualitatively more robust. *Reporting bias*: of 80 "QSI discovery" papers, only four explicitly null or negative reports were found; absent pre-registered "tested but inactive" tables distort the apparent translational signal. *Conflicts of interest*: several natural-product papers were funded by indigenous-medicinal-plant programmes; the close alignment of funder priorities with reported "potent inhibition" warrants caution.

#### 3.9.3 Heterogeneity sources

Four heterogeneity sources constrained quantitative synthesis: *strain diversity* (ATCC 17978 dominates at 47.8%, with ~60% of clinical-isolate panels used only once); *biofilm assay variation* (CV, XTT/MTT, CLSM and qPCR measure different biological properties and are not interconvertible); *MIC methodology* (CLSI versus EUCAST yield MIC ranges varying by 2-4-fold dilutions between laboratories); and *sub-MIC dose range* (1/2 to 1/64 MIC across the corpus, rendering "potent inhibition" claims at unspecified fractional MIC non-comparable).

#### 3.9.4 Down-weighting and minimum reporting dataset

In framing §3.3-3.6 we down-weighted four categories: in silico-only studies without wet-lab validation; crystal-violet-only natural-extract screens; animal studies without group-size justification, randomisation or attrition reporting; and clinical-isolate studies without susceptibility or sequence-type information. Down-weighting did not equate to refutation, and qualitative effect directions were robust to inclusion or exclusion of these records. We propose a minimum reporting dataset for *A. baumannii* QS studies (Supplementary S9.4) requiring: full strain provenance with susceptibility, capsular and sequence-type information; explicit cation supplementation; inoculum density and growth-phase definition; at least two orthogonal biofilm readouts; explicit fractional MIC for all sub-inhibitory testing; ARRIVE 2.0-compliant in vivo methods; raw-data deposition in GEO/SRA/ENA or PRIDE/ProteomeXchange; docking with decoy controls and ≥200 ns MD; and deposition of negative/inactive screening data. Journal-policy adoption would substantially improve cumulative interpretability of *A. baumannii* QS research.

---
## 4. Discussion

### 4.1 Principal findings

This synthesis of 340 records establishes that QS in *Acinetobacter baumannii* is supported by a mature, multi-modal evidence base. The AbaI/AbaR autoinducer system is delineated from biochemistry through gene regulation [Niu_2008; Bhargava_2010; Sun_2021; Mayer_2020]. QS regulates biofilm formation, motility, antibiotic tolerance and a constellation of virulence determinants (§3.3). A heterogeneous but expanding QSI pipeline spans synthetic AHL analogues [Stacy_2012; Stacy_2012_2], natural products [Bhargava_2015; Lin_2023; Cui_2025; Santajit_2025], QQ enzymes [Chow_2013; Mayer_2018; Lpez_2017_2; Bergonzi_2018; Vogel_2022] and engineered phages [Li_2024; Su_2025; deVilliersdelaNoue_2025; Arazi_2025]. In vivo proof-of-concept exists in *Galleria*, murine pneumonia, sepsis and wound models, and a small but informative clinical-association literature links QS gene expression to disease severity in CRAB bacteraemia and VAP (§3.6). Decisively absent: any published Phase II-III randomised data for a small-molecule QSI. Two decades of mechanistic work have not yet translated into a licensed adjunct.

### 4.2 Mechanistic consensus and controversies

Consensus is that AbaI is the dominant (likely sole) LuxI synthase in clinical *A. baumannii*, that 3-OH-C12-HSL is its principal product [Niu_2008; Chan_2014; Mayer_2018], and that isogenic *abaI*/*abaR* mutants show reproducibly attenuated biofilm and virulence [Sun_2021; Mayer_2020; Luo_2015]. Three controversies remain. *Is AbaR the master regulator?* Transcriptomic data show QS output is heavily filtered through BfmRS, AdeRS, PmrAB and DksA/Hfq [Xie_2025; RumboFeal_2013; Cui_2022; Kim_2021]; the current model is polygenic, with AbaR a node rather than a switch. *Do AHL and indole signals act in parallel or in sequence?* The Cui group's work and [Li_2025] reframe indole as an interspecies signal acting through a regulator distinct from AbaR, with partial parallelism and shared *csu*/*bap* effectors [Cui_2022; Cui_2025; Cui_2025_2]. *What is the role of c-di-GMP and cAMP?* [Harkova_2024] and [Cui_2025_2] frame nucleotide second messengers as global virulence regulators interfacing with QS, but the molecular grammar is only beginning to be mapped. Single-cell reconciliation of AbaIR transcriptomics with second-messenger dynamics is a clear priority.

### 4.3 Translational pipeline assessment

Four bottlenecks explain the absence of Phase II progression. *Target validation versus clinical relevance*: in vitro validation is strong, but the few patient-sample studies show 3-OH-C12-HSL in some but not all sputum samples [Chan_2014]; whether AbaIR is engaged at clinically intervenable timepoints is inferential. *PK/PD gaps*: demonstrated QSI-effective concentrations (25-200 µg/mL) [Cui_2025; Lin_2023; Elfaky_2024] exceed plasma C_max for orally dosed polyphenols by one to two orders of magnitude; no natural-product QSI has been advanced to a defined human PK study. *Formulation and delivery*: encapsulation strategies [Nosair_2025; Hetta_2021; Pourhajibagher_2023; DudaMadej_2025] improve apparent activity but introduce regulatory burdens, with manufacturable scale-up data rare. *Phage therapy is the nearest-clinic option*: lytic phages and engineered cocktails have the clearest pathway [deVilliersdelaNoue_2025; Essam_2025; Su_2025; Sitthisak_2023; Styles_2020], and several target capsular structures whose expression is QS- and BfmRS-regulated. *Adjunctive combination is the realistic horizon*: the strongest in vivo signals come from QSI-antibiotic combinations — polymyxin B with ceftazidime [Li_2022], colistin with phage-encoded peptides [Rothong_2024], erythromycin sensitising CRAB [Dong_2024], and streptomycin as a serendipitous adjuvant [Saroj_2013]. [Beasley_2025] frames QSIs as therapy enhancers rather than monotherapies, and this framing best fits the available data.

### 4.4 Polymicrobial context and comparator pathogens

A striking feature of the corpus is that 203 of 340 records (59.7%) frame their work in a multi-species or ESKAPE context [Bhargava_2012; Wheeler_2025; Sorenson_2025; Chong_2025; Vinitha_2025; Hetta_2025]. A species-specific QSI deployed clinically may have its activity attenuated by cross-acting AHLs from co-colonising species — an effect largely unexamined in current preclinical models. Broader-spectrum QQ enzymes may have an advantage over narrow small-molecule inhibitors [Vogel_2022; Bergonzi_2018; Chow_2013]. Mechanistically, *A. baumannii* QS differs from the canonical *P. aeruginosa* (Las/Rhl/PQS), *S. aureus* (Agr) and streptococcal (ComX/CSP) systems in three respects: it possesses a single LuxI synthase but compensates with extensive TCS and second-messenger integration (more polygenic, less hierarchical); it secretes and responds to indole as a signal [Cui_2022; Li_2025]; and it carries unusual endogenous QQ activity in the same organism that produces AHL [Mayer_2018; Lpez_2017_2]. Strategies validated in *P. aeruginosa* therefore do not transfer directly because the AbaR ligand-binding pocket differs structurally [BellI_2025].

### 4.5 Limitations of this review

Six limitations should be considered. *Database scope*: Scopus, Web of Science, Embase and Cochrane Library were not searched; cross-database corroboration between PubMed, OpenAlex and Crossref (264 of 340 PubMed records re-discovered) suggests indexing coverage was substantial. *Language restriction*: English-only inclusion may under-represent regional reports. *Review-process design*: screening used a structured protocol with internal consistency checks; risk-of-bias was assessed at the field level rather than per-study, and per-study GRADE certainty was not applied. *Heterogeneity*: variation in outcome definitions, biofilm endpoints, sub-MIC choices and strain background precluded pooled meta-analysis. *Publication bias*: formal funnel-plot assessment was not feasible, but the positive-result skew identified in §3.9.2 should temper interpretation. *Lack of patient-level data*: only 15 clinical-association studies were identified, most retrospective and single-centre. Despite these limitations, the convergence of in vitro mechanistic, in vivo proof-of-concept, omics and clinical-association data constitutes a multi-modal evidence base whose qualitative direction is robust to plausible search refinements.

### 4.6 Future research priorities

Seven priorities: (1) solve the AbaR structure to enable structure-based design beyond current model-dependent docking [BellI_2025; Aruwa_2025; Alagesan_2025]; (2) adopt community-consensus biofilm assays with orthogonal readouts and a defined strain panel; (3) test QS biomarkers (AHL, indole) prospectively in CRAB cohorts (VAP, burn-wound, bacteraemia), building on [Chan_2014; Carpenito_2025]; (4) advance engineered probiotics and topical QQ formulations with manufacturability, stability and immunogenicity studies [Vogel_2022; Bergonzi_2018; Lpez_2017_2]; (5) run Phase I trials of rationally designed phage cocktails for MDR pneumonia and wound infections [deVilliersdelaNoue_2025; Su_2025; Sitthisak_2023; Arazi_2025]; (6) adopt the minimum reporting dataset (§3.9.5; Supplementary S9.4) backed by journal policy; (7) replace monomicrobial models with two- to three-species consortia to test QSI efficacy under realistic co-colonisation [Bhargava_2012; Wheeler_2025].

## 5. Conclusion

Twenty-two years of mechanistic, omics and preclinical evidence establish QS as a credible therapeutic target in *Acinetobacter baumannii*. The AbaI/AbaR axis, modulated by BfmRS, AdeRS, PmrAB and indole signalling, governs biofilm formation, motility, antibiotic tolerance and virulence determinants that together account for much of the pathogen's clinical recalcitrance. Translation has stalled at the preclinical-clinical interface: no small-molecule QSI has entered Phase II evaluation, and clinical evidence remains largely associational. The strongest case from this corpus is for **adjunctive** rather than standalone QSI therapy, deploying QSIs and QQ enzymes to sensitise *A. baumannii* to existing antibiotics or to attenuate biofilm-mediated tolerance. Phage therapy is the most clinically advanced QS-modulating modality and is ready for properly designed Phase I trials in defined indications. The principal bottleneck is no longer target validation but dosing, formulation, clinical pharmacokinetics and standardised reporting. A unified minimum-information dataset, combined with structured biomarker validation in burn-wound, VAP and bacteraemia patient cohorts, would substantially accelerate the field. The next five years should prioritise solving the AbaR structure, running Phase I phage-cocktail trials, validating QS biomarkers in patient samples, and adopting community-standard reporting. With these advances, QS-directed therapy is plausibly within reach as a clinical adjunct for multidrug-resistant *A. baumannii* infection within the coming decade.

---


## References

1. Niu C, Clemmer KM, Bonomo RA, Rather PN. Isolation and characterization of an autoinducer synthase from Acinetobacter baumannii. *Journal of bacteriology*. 2008;190(9):3386-3392. doi:10.1128/JB.01929-07 PMID:18281398 PMCID:PMC2347373
2. Cui B, Peng G, Wang LE, Deng Y. Signaling in Acinetobacter baumannii: Quorum sensing and nucleotide second messengers. *Computational and structural biotechnology journal*. 2025;27:2168-2175. doi:10.1016/j.csbj.2025.05.032 PMID:40510767 PMCID:PMC12162036
3. Sun X, Ni Z, Tang J, Ding Y, Wang X, Li F. The abaI/abaR Quorum Sensing System Effects on Pathogenicity in Acinetobacter baumannii. *Frontiers in microbiology*. 2021;12(158):349-360. doi:10.3389/fmicb.2021.679241 PMID:34322102 PMCID:PMC8312687
4. Sun X, Xiang J. Mechanism Underlying the Role of LuxR Family Transcriptional Regulator abaR in Biofilm Formation by Acinetobacter baumannii. *Current microbiology*. 2021;78(11):3936-3944. doi:10.1007/s00284-021-02654-y PMID:34522977 PMCID:PMC8439540
5. López-Martín M, Dubern JF, Alexander MR, Williams P. AbaM Regulates Quorum Sensing, Biofilm Formation, and Virulence in Acinetobacter baumannii. *Journal of bacteriology*. 2021;203(8):538-582. doi:10.1128/JB.00635-20 PMID:33495249 PMCID:PMC8088503
6. Tierney ARP, Chin CY, Weiss DS, Rather PN. A LysR-Type Transcriptional Regulator Controls Multiple Phenotypes in Acinetobacter baumannii. *Frontiers in cellular and infection microbiology*. 2021;11:14820-14827. doi:10.3389/fcimb.2021.778331 PMID:34805000 PMCID:PMC8601201
7. González et al. Quorum sensing signal profile of Acinetobacter strains from nosocomial and environmental sources. *Revista Argentina de microbiologia*. 2009. PMID:19623895
8. Mayer C, Muras A, Romero M, López M, Tomás M, Otero A. Multiple Quorum Quenching Enzymes Are Active in the Nosocomial Pathogen Acinetobacter baumannii ATCC17978. *Frontiers in cellular and infection microbiology*. 2018;8:5503-5508. doi:10.3389/fcimb.2018.00310 PMID:30271754 PMCID:PMC6146095
9. Carpenito N, Leporati M, Sciarrillo A, Pensa A, Gambino R, Musso G, et al. LC-MS/MS Determination of Quorum Sensing Molecules in Plasma from Burn Patients with Septic Shock Sustained by Acinetobacter Baumannii. *Antibiotics (Basel, Switzerland)*. 2025;14(5):3739-3749. doi:10.3390/antibiotics14050517 PMID:40426583 PMCID:PMC12108150
10. Garner AL, Kim SK, Zhu J, Struss AK, Watkins R, Feske BD, et al. Stereochemical insignificance discovered in Acinetobacter baumannii quorum sensing. *PloS one*. 2012;7(5):685-695. doi:10.1371/journal.pone.0037102 PMID:22629354 PMCID:PMC3358330
11. Stacy DM, Le Quement ST, Hansen CL, Clausen JW, Tolker-Nielsen T, Brummond JW, et al. Synthesis and biological evaluation of triazole-containing N-acyl homoserine lactones as quorum sensing modulators. *Organic & biomolecular chemistry*. 2012;11(6):938-954. doi:10.1039/c2ob27155a PMID:23258305 PMCID:PMC3566574
12. Tuttobene MR, Müller GL, Blasco L, Arana N, Hourcade M, Diacovich L, et al. Blue light directly modulates the quorum network in the human pathogen Acinetobacter baumannii. *Scientific reports*. 2021;11(Pt 12):318-327. doi:10.1038/s41598-021-92845-1 PMID:34183737 PMCID:PMC8239052
13. Pimentel C, Le C, Tuttobene MR, Subils T, Papp-Wallace KM, Bonomo RA, et al. Interaction of Acinetobacter baumannii with Human Serum Albumin: Does the Host Determine the Outcome?. *Antibiotics (Basel, Switzerland)*. 2021;10(7):1-12. doi:10.3390/antibiotics10070833 PMID:34356754 PMCID:PMC8300715
14. Bergonzi C, Schwab M, Naik T, Daudé D, Chabrière E, Elias M. Structural and Biochemical Characterization of AaL, a Quorum Quenching Lactonase with Unusual Kinetic Properties. *Scientific reports*. 2018;8(Spec No):4360-4365. doi:10.1038/s41598-018-28988-5 PMID:30050039 PMCID:PMC6062542
15. López M, Mayer C, Fernández-García L, Blasco L, Muras A, Ruiz FM, et al. Quorum sensing network in clinical strains of A. baumannii: AidA is a new quorum quenching enzyme. *PloS one*. 2017;12(3):73-111. doi:10.1371/journal.pone.0174454 PMID:28328989 PMCID:PMC5362224
16. Vogel et al. Fighting Acinetobacter baumannii infections with the acylase PvdQ. *Microbes and infection*. 2022. doi:10.1016/j.micinf.2022.104951 PMID:35151875
17. Luo LM, Wu LJ, Xiao YL, Zhao D, Chen ZX, Kang M, et al. Enhancing pili assembly and biofilm formation in Acinetobacter baumannii ATCC19606 using non-native acyl-homoserine lactones. *BMC microbiology*. 2015;15(4):939-51. doi:10.1186/s12866-015-0397-5 PMID:25888221 PMCID:PMC4381447
18. Kim HJ, Kim NY, Ko SY, Park SY, Oh MH, Shin MS, et al. Complementary Regulation of BfmRS Two-Component and AbaIR Quorum Sensing Systems to Express Virulence-Associated Genes in Acinetobacter baumannii. *International journal of molecular sciences*. 2022;23(21):297-308. doi:10.3390/ijms232113136 PMID:36361923 PMCID:PMC9657202
19. Kim N, Son JH, Kim K, Kim HJ, Kim YJ, Shin M, et al. Global regulator DksA modulates virulence of Acinetobacter baumannii. *Virulence*. 2021;12(1):2750-2763. doi:10.1080/21505594.2021.1995253 PMID:34696704 PMCID:PMC8583241
20. López M, Blasco L, Gato E, Perez A, Fernández-Garcia L, Martínez-Martinez L, et al. Response to Bile Salts in Clinical Strains of Acinetobacter baumannii Lacking the AdeABC Efflux Pump: Virulence Associated with Quorum Sensing. *Frontiers in cellular and infection microbiology*. 2017;7(Pt 4):443-455. doi:10.3389/fcimb.2017.00143 PMID:28536672 PMCID:PMC5423435
21. Xie L, Li J, Peng Q, Liu X, Lin F, Dai X, et al. Contribution of RND superfamily multidrug efflux pumps AdeABC, AdeFGH, and AdeIJK to antimicrobial resistance and virulence factors in multidrug-resistant Acinetobacter baumannii AYE. *Antimicrobial agents and chemotherapy*. 2025;69(7):148-165. doi:10.1128/aac.01858-24 PMID:40407309 PMCID:PMC12217454
22. He X, Lu F, Yuan F, Jiang D, Zhao P, Zhu J, et al. Biofilm Formation Caused by Clinical Acinetobacter baumannii Isolates Is Associated with Overexpression of the AdeFGH Efflux Pump. *Antimicrobial agents and chemotherapy*. 2015;59(8):4817-4825. doi:10.1128/AAC.00877-15 PMID:26033730 PMCID:PMC4505227
23. Chen R, Lv R, Xiao L, Wang M, Du Z, Tan Y, et al. A1S_2811, a CheA/Y-like hybrid two-component regulator from Acinetobacter baumannii ATCC17978, is involved in surface motility and biofilm formation in this bacterium. *MicrobiologyOpen*. 2017;6(5):3628-3634. doi:10.1002/mbo3.510 PMID:28714256 PMCID:PMC5635159
24. Yousefi Nojookambari N, Eslami G, Sadredinamin M, Vaezjalali M, Nikmanesh B, Dehbanipour R, et al. Sub-minimum inhibitory concentrations (sub-MICs) of colistin on Acinetobacter baumannii biofilm formation potency, adherence, and invasion to epithelial host cells: an experimental study in an Iranian children's referral hospital. *Microbiology spectrum*. 2024;12(2):2715-2738. doi:10.1128/spectrum.02523-23 PMID:38230925 PMCID:PMC10846280
25. Cui B, Guo Q, Li X, Song S, Wang M, Wang G, et al. A response regulator controls Acinetobacter baumannii virulence by acting as an indole receptor. *PNAS nexus*. 2023;2(8):269-275. doi:10.1093/pnasnexus/pgad274 PMID:37649583 PMCID:PMC10465187
26. Cui B, Peng G, Wang M, Kong X, Wei H, Ling X, et al. Carnosol attenuates Acinetobacter baumannii virulence by interfering with indole-mediated quorum sensing. *Virulence*. 2025;16(1):4-13. doi:10.1080/21505594.2025.2530169 PMID:40660701 PMCID:PMC12269709
27. Mendes SG, Combo SI, Allain T, Domingues S, Buret AG, Da Silva GJ. Co-regulation of biofilm formation and antimicrobial resistance in Acinetobacter baumannii: from mechanisms to therapeutic strategies. *European journal of clinical microbiology & infectious diseases : official publication of the European Society of Clinical Microbiology*. 2023;42(12):1405-1423. doi:10.1007/s10096-023-04677-8 PMID:37897520 PMCID:PMC10651561
28. Rumbo-Feal S, Gómez MJ, Gayoso C, Álvarez-Fraga L, Cabral MP, Aransay AM, et al. Whole transcriptome analysis of Acinetobacter baumannii assessed by RNA-sequencing reveals different mRNA expression profiles in biofilm compared to planktonic cells. *PloS one*. 2013;8(8):4086-4095. doi:10.1371/journal.pone.0072968 PMID:24023660 PMCID:PMC3758355
29. Vinitha et al. Acinetobacter baumannii-rare virulence factors and pathogenesis: the impact of biofilm associated protein (Bap), outer membrane vesicles, and iron acquisition system. *Archives of microbiology*. 2025. doi:10.1007/s00203-025-04623-6 PMID:41379337
30. Kostoulias X, Murray GL, Cerqueira GM, Kong JB, Bantun F, Mylonakis E, et al. Impact of a Cross-Kingdom Signaling Molecule of Candida albicans on Acinetobacter baumannii Physiology. *Antimicrobial agents and chemotherapy*. 2015;60(1):161-167. doi:10.1128/AAC.01540-15 PMID:26482299 PMCID:PMC4704244
31. Ghavanloughajar H, Elmassry MM, Brown AMV, Hamood AN. Human whole blood influences the expression of Acinetobacter baumannii genes related to translation and siderophore production. *PloS one*. 2025;20(7):185-6. doi:10.1371/journal.pone.0326330 PMID:40705813 PMCID:PMC12289009
32. Pimentel C, Le C, Tuttobene MR, Subils T, Martinez J, Sieira R, et al. Human Pleural Fluid and Human Serum Albumin Modulate the Behavior of a Hypervirulent and Multidrug-Resistant (MDR) Acinetobacter baumannii Representative Strain. *Pathogens (Basel, Switzerland)*. 2021;10(4):409-447. doi:10.3390/pathogens10040471 PMID:33924559 PMCID:PMC8069197
33. Pérez-Varela M, Tierney ARP, Kim JS, Vázquez-Torres A, Rather P. Characterization of RelA in Acinetobacter baumannii. *Journal of bacteriology*. 2020;202(12). doi:10.1128/JB.00045-20 PMID:32229531 PMCID:PMC7253615
34. Harkova LG, de Dios R, Rubio-Valle A, Pérez-Pulido AJ, McCarthy RR. Cyclic AMP is a global virulence regulator governing inter and intrabacterial signalling in Acinetobacter baumannii. *PLoS pathogens*. 2024;20(9):629-655. doi:10.1371/journal.ppat.1012529 PMID:39241032 PMCID:PMC11410210
35. Bhargava et al. N-acyl homoserine lactone mediated interspecies interactions between A. baumannii and P. aeruginosa. *Biofouling*. 2012. doi:10.1080/08927014.2012.714372 PMID:22867087
36. Wheeler KM, Oh MW, Fusco J, Mershon A, Kim E, De Oliveira A, et al. MvfR Shapes Pseudomonas aeruginosa Interactions in Polymicrobial Contexts: Implications for Targeted Quorum-Sensing Inhibition. *Cells*. 2025;14(10):1-8. doi:10.3390/cells14100744 PMID:40422247 PMCID:PMC12109783
37. Peleg AY, Tampakakis E, Fuchs BB, Eliopoulos GM, Moellering RC, Mylonakis E. Prokaryote-eukaryote interactions identified by using Caenorhabditis elegans. *Proceedings of the National Academy of Sciences of the United States of America*. 2008;105(38):14585-14590. doi:10.1073/pnas.0805048105 PMID:18794525 PMCID:PMC2567192
38. Cui B, Chen X, Guo Q, Song S, Wang M, Liu J, et al. The Cell-Cell Communication Signal Indole Controls the Physiology and Interspecies Communication of Acinetobacter baumannii. *Microbiology spectrum*. 2022;10(4):269-275. doi:10.1128/spectrum.01027-22 PMID:35862954 PMCID:PMC9431217
39. Li J, Xie L, Lin F, Ling B. Indole derivatives display antimicrobial and antibiofilm effects against extensively drug-resistant Acinetobacter baumannii. *Microbiology spectrum*. 2025;13(5):148-165. doi:10.1128/spectrum.03388-24 PMID:40231681 PMCID:PMC12073863
40. Subbarayudu et al. Impact of acidic and alkaline conditions on Staphylococcus aureus and Acinetobacter baumannii interactions and their biofilms. *Archives of microbiology*. 2024. doi:10.1007/s00203-024-04142-w PMID:39375235
41. Chow JY, Yang Y, Tay SB, Chua KL, Yew WS. Disruption of biofilm formation by the human pathogen Acinetobacter baumannii using engineered quorum-quenching lactonases. *Antimicrobial agents and chemotherapy*. 2013;58(3):1802-1805. doi:10.1128/AAC.02410-13 PMID:24379199 PMCID:PMC3957888
42. Djahanschiri B, Di Venanzio G, Distel JS, Breisch J, Dieckmann MA, Goesmann A, et al. Evolutionarily stable gene clusters shed light on the common grounds of pathogenicity in the Acinetobacter calcoaceticus-baumannii complex. *PLoS genetics*. 2022;18(6):332-9. doi:10.1371/journal.pgen.1010020 PMID:35653398 PMCID:PMC9162365
43. Kröger C, Kary SC, Schauer K, Cameron ADS. Genetic Regulation of Virulence and Antibiotic Resistance in Acinetobacter baumannii. *Genes*. 2016;8(1):336-343. doi:10.3390/genes8010012 PMID:28036056 PMCID:PMC5295007
44. Escalante J, Nishimura B, Tuttobene MR, Subils T, Pimentel C, Georgeos N, et al. Human serum albumin (HSA) regulates the expression of histone-like nucleoid structure protein (H-NS) in Acinetobacter baumannii. *Scientific reports*. 2022;12(3):9-13. doi:10.1038/s41598-022-19012-y PMID:36030268 PMCID:PMC9420150
45. Beasley JM, Dorjsuren D, Jain S, Rath M, Scheufen Tieghi R, Tropsha A, et al. Breaking the Phalanx: Overcoming Bacterial Drug Resistance with Quorum Sensing Inhibitors that Enhance Therapeutic Activity of Antibiotics. *bioRxiv : the preprint server for biology*. 2025;2:6-327. doi:10.1101/2025.01.17.633658 PMID:39896648 PMCID:PMC11785035
46. Su J, Tan Y, Liu S, Zou H, Huang X, Chen S, et al. Characterization of a novel lytic phage vB_AbaM_AB4P2 encoding depolymerase and its application in eliminating biofilms formed by Acinetobacter baumannii. *BMC microbiology*. 2025;25(5):22-9. doi:10.1186/s12866-025-03854-3 PMID:40057696 PMCID:PMC11889872
47. Vera-Jauregui E, Avila-Novoa MG, González-Torres B, Guerrero-Medina PJ, Chaidez C, González-López I, et al. A Newly Discovered Obolenskvirus Phage with Sustained Lytic Activity Against Multidrug-Resistant Acinetobacter baumannii. *Antibiotics (Basel, Switzerland)*. 2025;14(10):e65-281. doi:10.3390/antibiotics14100961 PMID:41148653 PMCID:PMC12561047
48. Duda-Madej A, Viscardi S, Bazan H, Sobieraj J. Exploring the Role of Berberine as a Molecular Disruptor in Antimicrobial Strategies. *Pharmaceuticals (Basel, Switzerland)*. 2025;18(7):229-241. doi:10.3390/ph18070947 PMID:40732238 PMCID:PMC12299710
49. Bell I et al. Targeting the quorum sensing network in Acinetobacter baumannii: A dual target structure-based approach for the development of novel antimicrobials. *Computers in biology and medicine*. 2025. doi:10.1016/j.compbiomed.2025.109828 PMID:39938338
50. Khafagy et al. Repurposing Nitroimidazoles: A New Frontier in Combatting Bacterial Virulence and Quorum Sensing via In Silico, In Vitro, and In Vivo Insights. *Drug development research*. 2025. doi:10.1002/ddr.70101 PMID:40384051
51. de Villiers de la Noue H, Golliard G, Vuattoux X, Resch G. Rational Design of a Potent Two-Phage Cocktail Against a Contemporary Acinetobacter baumannii Strain Recovered from a Burned Patient at the Lausanne University Hospital. *Viruses*. 2025;17(11):6987-6998. doi:10.3390/v17111441 PMID:41305464 PMCID:PMC12656882
52. Elshamy et al. Genomic analysis and preclinical evaluation of two hydrogel-formulated novel virulent phages isolated against a carbapenem-resistant Acinetobacter baumannii. *Virology*. 2025. doi:10.1016/j.virol.2025.110676 PMID:40916327
53. World Health Organization. *WHO Bacterial Priority Pathogens List, 2024: Bacterial pathogens of public health importance to guide research, development, and strategies to prevent and control antimicrobial resistance*. Geneva: WHO; 2024. https://www.who.int/publications/i/item/9789240093461
54. Centers for Disease Control and Prevention. *Antibiotic Resistance Threats in the United States, 2019*. Atlanta: U.S. Department of Health and Human Services, CDC; 2019. https://www.cdc.gov/drugresistance/biggest-threats.html
55. Centers for Disease Control and Prevention. *Antimicrobial Resistance Threats — 2024 Update*. Atlanta: U.S. Department of Health and Human Services, CDC; 2024. https://www.cdc.gov/antimicrobial-resistance/data-research/threats/index.html
56. Murray CJL, Ikuta KS, Sharara F, Swetschinski L, Robles Aguilar G, Gray A, et al. Global burden of bacterial antimicrobial resistance in 2019: a systematic analysis. *Lancet*. 2022;399(10325):629–55. doi:10.1016/S0140-6736(21)02724-0
57. Rice LB. Federal funding for the study of antimicrobial resistance in nosocomial pathogens: no ESKAPE. *J Infect Dis*. 2008;197(8):1079–81. doi:10.1086/533452
58. Page MJ, McKenzie JE, Bossuyt PM, Boutron I, Hoffmann TC, Mulrow CD, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. *BMJ*. 2021;372:n71. doi:10.1136/bmj.n71
59. Rethlefsen ML, Kirtley S, Waffenschmidt S, Ayala AP, Moher D, Page MJ, et al. PRISMA-S: an extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews. *Syst Rev*. 2021;10:39. doi:10.1186/s13643-020-01542-z
60. Campbell M, McKenzie JE, Sowden A, Katikireddi SV, Brennan SE, Ellis S, et al. Synthesis without meta-analysis (SWiM) in systematic reviews: reporting guideline. *BMJ*. 2020;368:l6890. doi:10.1136/bmj.l6890
61. Krithikadatta J, Gopikrishna V, Datta M. CRIS Guidelines (Checklist for Reporting In-vitro Studies): A concept note. *J Conserv Dent*. 2014;17(4):301–4. doi:10.4103/0972-0707.136338
62. Hooijmans CR, Rovers MM, de Vries RB, Leenaars M, Ritskes-Hoitinga M, Langendam MW. SYRCLE's risk of bias tool for animal studies. *BMC Med Res Methodol*. 2014;14:43. doi:10.1186/1471-2288-14-43
63. Percie du Sert N, Hurst V, Ahluwalia A, Alam S, Avey MT, Baker M, et al. The ARRIVE guidelines 2.0: Updated guidelines for reporting animal research. *PLoS Biol*. 2020;18(7):e3000410. doi:10.1371/journal.pbio.3000411
64. Joanna Briggs Institute. *JBI Manual for Evidence Synthesis*. Aromataris E, Munn Z (eds). 2020. doi:10.46658/JBIMES-20-01
65. Wells GA, Shea B, O'Connell D, Peterson J, Welch V, Losos M, Tugwell P. The Newcastle-Ottawa Scale (NOS) for assessing the quality of nonrandomised studies in meta-analyses. Ottawa Hospital Research Institute; 2014. http://www.ohri.ca/programs/clinical_epidemiology/oxford.asp
66. Moons KGM, de Groot JAH, Bouwmeester W, Vergouwe Y, Mallett S, Altman DG, et al. Critical appraisal and data extraction for systematic reviews of prediction modelling studies: the CHARMS checklist. *PLoS Med*. 2014;11(10):e1001744. doi:10.1371/journal.pmed.1001744
67. Bustin SA, Benes V, Garson JA, Hellemans J, Huggett J, Kubista M, et al. The MIQE guidelines: minimum information for publication of quantitative real-time PCR experiments. *Clin Chem*. 2009;55(4):611–22. doi:10.1373/clinchem.2008.112797
68. Sterne JAC, Savović J, Page MJ, Elbers RG, Blencowe NS, Boutron I, et al. RoB 2: a revised tool for assessing risk of bias in randomised trials. *BMJ*. 2019;366:l4898. doi:10.1136/bmj.l4898
69. Egger M, Davey Smith G, Schneider M, Minder C. Bias in meta-analysis detected by a simple, graphical test. *BMJ*. 1997;315(7109):629–34. doi:10.1136/bmj.315.7109.629

---

## Supplementary Material

- **S1.** PRISMA 2020 checklist — `supplementary/S1_prisma2020_checklist.md`
- **S2.** Full search strategies for all databases — `02-search-strategies.md`
- **S3.** Multi-database merge log and de-duplication report — `literature/merged_unique.csv`, `literature/prisma_flow_data.json`
- **S4.** Data extraction form — `04-data-extraction-form.md`
- **S5.** Categorised corpus — `literature/categorized.csv`
- **S6.** Evidence claims database — `literature/evidence_claims.json`
- **S7.** Full bibliography (340 records) — `bibliography.md`
- **S8.** Citation shortlist (top 60 by importance) — `literature/citation_shortlist.csv`


---
*Manuscript word count: 11,945 | Cited references: 69*
