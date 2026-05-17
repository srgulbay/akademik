# 2. Methods

This systematic review was designed, conducted and reported in accordance with the Preferred Reporting Items for Systematic Reviews and Meta-Analyses 2020 statement (PRISMA 2020) [Page 2021], the PRISMA-S extension for reporting literature searches [Rethlefsen 2021] and, for the planned narrative synthesis, the Synthesis Without Meta-analysis (SWiM) guideline [Campbell 2020]. The completed PRISMA 2020 checklist is provided as Supplementary Material S1.

## 2.1 Protocol and registration

The review protocol was drafted before screening commenced and is archived at `/01-protocol.md` of the project repository (version v0.2, 17 May 2026). The protocol specifies the review question, eligibility criteria, information sources, search strategy, screening procedure, data-extraction items, risk-of-bias instruments, synthesis approach and reporting framework. Registration of the protocol on the International Prospective Register of Systematic Reviews (PROSPERO) is planned; the CRD identifier will be inserted at the time of journal submission. Substantive deviations from the protocol — most importantly, the current restriction of the executed search to a single bibliographic database — are flagged explicitly throughout this section and are summarised in Supplementary Table S2.

## 2.2 Eligibility criteria

Records were eligible for inclusion if they met all of the following criteria:

- **Population:** *Acinetobacter baumannii*, including reference strains (e.g. ATCC 17978, ATCC 19606, AB5075, LAC-4), clinical isolates of any resistance phenotype, and environmental isolates.
- **Exposure/intervention:** Any investigation of QS or QS-related signalling in *A. baumannii*, including descriptive (e.g. AHL profiling, *abaI/abaR/abaM* expression, comparative genomics), mechanistic (e.g. gene-deletion, complementation, transcriptomic/proteomic perturbation) or interventional (small-molecule QSI, natural product, synthetic compound, peptide, antimicrobial peptide, enzymatic quorum quencher, QS-targeting bacteriophage, nanoparticle-delivered agent, repurposed drug, antibody, vaccine) studies.
- **Outcome:** At least one quantitative outcome relevant to QS biology or QS-targeting therapy, including biofilm mass or architecture, motility, virulence-factor expression or activity, MIC/MBEC/FIC, gene or protein expression of QS-network components, in vivo bacterial burden or host survival, or clinical correlates.
- **Study design:** Original research (in vitro, in vivo animal, in silico, omics, ex vivo, clinical) or peer-reviewed review/meta-analysis.
- **Language:** English.
- **Publication date:** 1 May 2003 to 17 May 2025.
- **Publication type:** Peer-reviewed full-text article.

Records were excluded if they (i) were conference abstracts, theses, editorials, letters without primary data, or pre-prints not subsequently peer-reviewed; (ii) reported *Acinetobacter* genus-level data without separable *A. baumannii* findings; (iii) addressed QS in other species using *A. baumannii* only as a comparator without species-specific QS outcomes; (iv) had been formally retracted; or (v) were not retrievable in full text after three documented attempts via the publisher, PubMed Central and institutional interlibrary loan. Purely in silico studies without any experimental or curated-dataset support were retained but tabulated separately for sensitivity analysis.

## 2.3 Information sources

The protocol specifies a four-database core search (PubMed/MEDLINE, Scopus, Web of Science Core Collection, Embase) with Cochrane Library as a confirmatory search for controlled trials. In the present version (v1) the executed search was restricted to **PubMed/MEDLINE**, queried on 17 May 2026; the resulting 340 records constitute the corpus analysed here. The decision to release v1 with a single database reflects the technical maturity of the PubMed search and the desire to allow community feedback on the synthesis framework before extending. The remaining three core databases plus Cochrane Library will be searched, and the merged corpus deduplicated and re-screened, for the v2 submission; the complete syntaxes for each database are provided in Supplementary Material S2 (reproducing `/02-search-strategies.md` of the repository). As supplementary information sources we additionally interrogated the **OpenAlex** and **Crossref** application programming interfaces to cross-validate metadata and to capture records indexed with non-standard MeSH terms; these queries were used for metadata enrichment and reference-list reconstruction rather than as primary identification sources, and are documented in the search log. Forward and backward citation chasing of all included studies (Web of Science "Cited Reference Search" plus OpenAlex citation network) is planned in v2.

## 2.4 Search strategy

The PubMed strategy combined controlled vocabulary (MeSH) with title/abstract free-text terms for the population and intervention concepts, joined by Boolean operators. The full query as executed was:

```
("Acinetobacter baumannii"[MeSH] OR "Acinetobacter baumannii"[tiab] OR "A. baumannii"[tiab])
AND
("quorum sensing"[tiab] OR "quorum-sensing"[tiab] OR "quorum quenching"[tiab]
 OR "quorum-quenching"[tiab] OR "abaI"[tiab] OR "abaR"[tiab] OR "abaM"[tiab]
 OR "autoinducer"[tiab]
 OR "acyl homoserine lactone"[tiab] OR "acyl-homoserine lactone"[tiab]
 OR "N-acyl homoserine lactone"[tiab] OR "AHL"[tiab]
 OR "3-hydroxy-dodecanoyl-homoserine"[tiab] OR "3-OH-C12-HSL"[tiab]
 OR "LuxI"[tiab] OR "LuxR"[tiab])
AND ("2003/01/01"[PDAT] : "2025/12/31"[PDAT])
AND English[Language]
```

No publication-type filter was applied at the database level; document-type filtering was carried out manually during screening to avoid the loss of relevant records mis-indexed at source. For Scopus, Web of Science, Embase and Cochrane (v2), the PICO concepts and Boolean structure are preserved while syntax, controlled vocabulary (Emtree, Keywords Plus) and field tags are adapted database-by-database (Supplementary Material S2). The PRISMA-S checklist for search reporting is supplied as Supplementary Material S3.

## 2.5 Study selection

Records identified by the PubMed search (n = 340) were imported into a reference manager and de-duplicated by DOI and PMID followed by fuzzy title-plus-year matching (2 duplicates removed; 338 unique records advanced). In v1 the screening was performed by a single reviewer with structured cross-checks against the data-extraction form; this design limitation is acknowledged and addressed in Section 5 (Limitations). In v2, screening will be performed in duplicate and independently by two reviewers (R1, R2) using Rayyan or Covidence at both the title/abstract and full-text stages. Inter-rater agreement will be assessed by Cohen's κ with a calibration target of κ ≥ 0.75 prior to formal screening; disagreements will be resolved by discussion and, where necessary, by adjudication from a third reviewer (R3). Reasons for full-text exclusion will be recorded against a pre-defined list (wrong population, wrong exposure, wrong outcome, wrong design, full text unavailable, retraction). The flow of records from identification through inclusion is summarised in the PRISMA 2020 flow diagram (Figure 1).

## 2.6 Data extraction

A standardised data-extraction form (`/04-data-extraction-form.md`, v1.0, 17 May 2026) was developed and piloted on ten randomly selected records spanning all major study types. The form comprises five sections: (A) bibliographic identifiers and funding/COI; (B) study design and population (strains, isolate provenance, resistance phenotype, QS target); (C) study-type-specific items, including MIC and biofilm assay methods, motility and virulence assays, AHL quantitation, gene-expression targets, synergy testing and cytotoxicity for in vitro studies; docking software, binding-energy reporting, molecular-dynamics duration and in vitro validation for in silico studies; species, infection model, inoculum, treatment regimen, endpoints, IACUC approval and ARRIVE 2.0 compliance for animal studies; omics modality, replicates, platform, deposited accession and bioinformatics pipeline for omics studies; design, sample size, population and IRB approval for clinical studies; (D) risk-of-bias items (Section 2.7); and (E) primary outcome measure, effect size, confidence interval, statistical test, p-value, replicability of raw data and a single-sentence summary of the principal finding. In v1, extraction was performed by a single reviewer; for v2, dual independent extraction with discrepancy adjudication will be implemented, and inter-rater reliability (Cohen's κ for categorical items, intraclass correlation for continuous items) reported.

## 2.7 Risk of bias and methodological quality assessment

Risk of bias was assessed using design-appropriate instruments:

- **In vitro studies:** A modified CRIS (Consensus on Reporting In vitro Studies) checklist [Krithikadatta 2014], extended with items capturing biological/technical replicate number, strain provenance, blinded outcome assessment and statistical handling.
- **Animal (in vivo) studies:** SYRCLE Risk of Bias Tool [Hooijmans 2014] supplemented by ARRIVE 2.0 reporting items [Percie 2020].
- **Observational clinical studies:** JBI Critical Appraisal Checklists (analytical cross-sectional, cohort or case series, as appropriate) [JBI 2020]; the Newcastle–Ottawa Scale will be used where cohort comparisons are reported [Wells 2014].
- **Randomised clinical trials:** Cochrane RoB 2.0 [Sterne 2019]. Given the topic, RCTs are not anticipated in the v1 corpus.
- **In silico studies:** A CHARMS-modified checklist [Moons 2014] covering target validity, software validation, conformational sampling and external validation.
- **Omics studies:** MIQE for qPCR datasets [Bustin 2009] and MINSEQE-aligned criteria for high-throughput sequencing, including accession deposition and analysis-pipeline transparency.

Each study will be appraised independently by two reviewers in v2, with disagreements resolved by a third reviewer; in v1, a single reviewer's judgement is reported and explicitly flagged. Domain-level judgements are summarised as low, some-concerns or high risk of bias and tabulated in Supplementary Tables S4–S9.

## 2.8 Effect measures and synthesis

The primary outcomes for synthesis are: (i) biofilm inhibition expressed as percent reduction relative to control at a defined concentration; (ii) MIC and MBEC fold-change of an antibiotic co-administered with a QS-targeting agent; (iii) reduction in virulence factor activity or expression (protease, siderophore, motility, OMV, host-cell injury); and (iv) in vivo bacterial burden (log10 CFU reduction) and host survival (percent at defined time point). Secondary outcomes include AHL quantitation, QS-regulon gene-expression fold-change, cytotoxicity (IC50, selectivity index) and synergy classification (FIC index categories).

Studies are grouped a priori by intervention class (natural product, synthetic small molecule, enzymatic quorum quencher, peptide/AMP, bacteriophage, nanoparticle, repurposed drug, antibody/vaccine, genetic perturbation) crossed with outcome domain, and by experimental system (in vitro, in vivo, in silico, omics, clinical). The synthesis is primarily narrative because of heterogeneity in strains, intervention concentrations, assay formats and outcome definitions, in line with SWiM guidance [Campbell 2020]. Where three or more comparable studies report a quantitative outcome in compatible units, we will explore random-effects meta-analysis using the DerSimonian–Laird estimator with Hartung–Knapp adjustment, presenting pooled standardised mean differences (Hedges' g) with 95% confidence intervals. Between-study heterogeneity will be quantified by τ² and I². Pre-specified sensitivity analyses include restriction by strain (ATCC 17978 only; clinical isolates only), assay format (crystal violet vs. confocal microscopy for biofilm; broth microdilution vs. E-test for MIC) and risk-of-bias judgement (excluding high-risk studies). Pre-specified subgroup analyses examine intervention class, isolate resistance phenotype (susceptible vs. CRAB/MDR/XDR) and exposure duration.

## 2.9 Publication bias

For any outcome with ten or more eligible studies in a meta-analytic pool, funnel-plot asymmetry will be assessed visually and tested by Egger's regression [Egger 1997]. With fewer than ten studies, small-study effects will be evaluated narratively, considering precision-weighted distributions, evidence of selective reporting within studies and the availability of pre-registered protocols.

## 2.10 Certainty of evidence and reporting

The certainty of the body of evidence for each principal outcome will be rated using the GRADE framework [Guyatt 2008], with downgrading for risk of bias, inconsistency, indirectness, imprecision and publication bias, and upgrading for large effect, dose–response gradient or plausible residual confounding favouring the null. The review is reported in accordance with PRISMA 2020 [Page 2021] for overall structure, PRISMA-S [Rethlefsen 2021] for the literature search and SWiM [Campbell 2020] for the narrative synthesis; the PRISMA-NMA extension was not applicable because no network meta-analysis is conducted. All data-extraction forms, code, search logs and intermediate datasets are deposited on Zenodo (DOI to be issued at acceptance) and on the project repository.

## 2.11 Summary of v1 versus v2 scope

To assist the reader and reviewers, Table 1 (Supplementary Material S2) summarises the items that differ between the present v1 manuscript and the planned v2 update: extension of the search from PubMed to PubMed + Scopus + Web of Science + Embase + Cochrane, transition from single-reviewer to dual-reviewer screening and extraction with κ reporting, addition of forward/backward citation chasing of included studies, formal PROSPERO registration and full GRADE assessment of all principal outcomes. The synthesis framework, eligibility criteria and risk-of-bias instruments are unchanged between versions.
