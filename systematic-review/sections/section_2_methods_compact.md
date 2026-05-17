# 2. Methods

This review was designed, conducted and reported in accordance with PRISMA 2020 [Page 2021], the PRISMA-S extension [Rethlefsen 2021] and the Synthesis Without Meta-analysis (SWiM) guideline [Campbell 2020]. The completed PRISMA 2020 checklist is provided as Supplementary S1.

## 2.1 Protocol and registration

The review followed a prospectively developed protocol drafted before screening commenced and archived at `/01-protocol.md`. The protocol specifies the review question, eligibility criteria, information sources, search strategy, screening procedure, data-extraction items, risk-of-bias instruments, synthesis approach and reporting framework. Prospective PROSPERO registration is to be added at submission.

## 2.2 Eligibility criteria

Records were eligible if they reported original or peer-reviewed review research on *A. baumannii* (reference strains ATCC 17978, ATCC 19606, AB5075, LAC-4; clinical isolates of any resistance phenotype; environmental isolates), examined QS or QS-related signalling, and reported at least one quantitative QS-relevant outcome (biofilm mass or architecture, motility, virulence-factor expression, MIC/MBEC/FIC, QS-network gene or protein expression, in vivo bacterial burden, host survival, or clinical correlates). Eligible designs were in vitro, in vivo animal, in silico, omics, ex vivo and clinical studies. Language was English; publication window 1 May 2003 to 17 May 2025; peer-reviewed full-text only. Records were excluded if they were conference abstracts, theses, editorials or letters without primary data; reported genus-level data without separable *A. baumannii* findings; used *A. baumannii* solely as a comparator; had been formally retracted; or were not retrievable in full text after three attempts. Purely in silico studies without experimental or curated-dataset support were retained but tabulated separately for sensitivity analysis.

## 2.3 Information sources

MEDLINE/PubMed was searched on 17 May 2026 as the principal bibliographic source. The search was supplemented by complementary queries of **OpenAlex** and **Crossref** via their public APIs to maximise coverage of indexed and open-scholarship literature, including preprints, non-MEDLINE journals and records indexed with non-standard MeSH terms. The three sources were merged and de-duplicated by DOI, PMID and fuzzy title-plus-year matching. Scopus, Web of Science, Embase and Cochrane Library queries were not included; the implications are addressed in §4.6 (Limitations). The complete database query syntaxes are provided in Supplementary S2.

## 2.4 Search strategy

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

## 2.5 Study selection

Records identified by PubMed (n = 340), OpenAlex (n = 351) and Crossref (n = 3,060) were imported into a structured catalogue and de-duplicated, yielding 3,313 unique records (Figure 1). Screening proceeded in two stages: (i) title and abstract screening to remove records outside population, exposure or design scope; (ii) full-text assessment of records meeting initial criteria. Eligibility decisions were verified against full-text content where available, with structured cross-checks against the data-extraction form and master catalogue. Reasons for full-text exclusion were recorded against a pre-defined list (wrong population, wrong exposure, wrong outcome, wrong design, full text unavailable, retraction). Cross-database corroboration is reported in §3.1 as a validation metric for indexing coverage.

## 2.6 Data extraction

A standardised data-extraction form (`/04-data-extraction-form.md`) was piloted on ten records spanning all study types. The form comprises: (A) bibliographic identifiers and funding/COI; (B) study design and population; (C) study-type-specific items (assay methods and gene-expression targets for in vitro work; docking software, binding-energy reporting and MD duration for in silico; species, model, inoculum, regimen, endpoints and ARRIVE 2.0 compliance for animal studies; modality, replicates, deposited accession and pipeline for omics; design, sample size and IRB approval for clinical); (D) risk-of-bias items (§2.7); and (E) primary outcome measure, effect size, statistical test, replicability and single-sentence summary. Extraction used a structured protocol with multi-pass categorisation, validation against the master catalogue, and reconciliation of conflicting entries against full text.

## 2.7 Risk of bias and methodological quality

Methodological quality and risk of bias were appraised at the field level using design-appropriate frameworks as reference standards: a modified CRIS checklist for in vitro studies [Krithikadatta 2014]; SYRCLE [Hooijmans 2014] supplemented by ARRIVE 2.0 [Percie 2020] for animal studies; JBI Critical Appraisal Checklists [JBI 2020] and Newcastle-Ottawa Scale [Wells 2014] for observational clinical work; a CHARMS-modified checklist [Moons 2014] for in silico studies; and MIQE [Bustin 2009] plus MINSEQE-aligned criteria for omics. Cochrane RoB 2.0 [Sterne 2019] was not applied because no randomised trial of a QS-targeting agent in *A. baumannii* was identified. Field-level patterns are summarised in §3.9 and visualised in Figure 5.

## 2.8 Effect measures and synthesis

Primary outcomes were biofilm inhibition (percent reduction at a defined concentration); MIC/MBEC fold-change of an antibiotic with a QS-targeting agent; reduction in virulence factor activity or expression; and in vivo bacterial burden (log10 CFU reduction) and host survival. Secondary outcomes included AHL quantitation, QS-regulon gene-expression fold-change, cytotoxicity (IC50, selectivity index) and synergy classification (FIC index). Studies were grouped a priori by intervention class crossed with outcome domain and experimental system. The synthesis is narrative with structured outcome tabulation per SWiM [Campbell 2020]; heterogeneity in strain background, intervention concentrations, assays and outcome definitions precluded formal pooled meta-analysis. Effect sizes are summarised by intervention class in Table 2 and aggregated by outcome domain in §3.8.

## 2.9 Publication bias

Funnel-plot asymmetry was considered for the largest outcome subgroup (biofilm inhibition); heterogeneity of effect-size metrics, sub-MIC concentration choices and assay formats precluded construction of a comparable effect-estimate set sufficient for Egger's regression [Egger 1997]. Small-study effects, positive-result skew and selective reporting are assessed narratively in §3.9.2 and §4.6.

## 2.10 Reporting framework

The review is reported per PRISMA 2020 [Page 2021], PRISMA-S [Rethlefsen 2021] and SWiM [Campbell 2020]. The PRISMA-NMA extension was not applicable. Formal GRADE certainty grading was not applied at the body-of-evidence level because heterogeneity precluded quantitative pooling; certainty of mechanistic, preclinical and translational claims is discussed narratively in §4. All data-extraction forms, code, search logs and intermediate datasets are deposited on the project repository.
