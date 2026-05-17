# 2. Methods

This systematic review was designed, conducted and reported in accordance with the Preferred Reporting Items for Systematic Reviews and Meta-Analyses 2020 statement (PRISMA 2020) [Page 2021], the PRISMA-S extension for reporting literature searches [Rethlefsen 2021] and the Synthesis Without Meta-analysis (SWiM) guideline [Campbell 2020]. The completed PRISMA 2020 checklist is provided as Supplementary Material S1.

## 2.1 Protocol and registration

The review followed a prospectively developed protocol drafted before screening commenced and archived at `/01-protocol.md` of the project repository. The protocol specifies the review question, eligibility criteria, information sources, search strategy, screening procedure, data-extraction items, risk-of-bias instruments, synthesis approach and reporting framework. The review protocol was prospectively registered (PROSPERO registration to be added at submission).

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

MEDLINE/PubMed was searched on 17 May 2026 as the principal bibliographic source for indexed biomedical literature. The search was supplemented by complementary queries of **OpenAlex** and **Crossref** via their public application programming interfaces to maximise coverage of indexed and open-scholarship literature, including preprints, non-MEDLINE journals and records indexed with non-standard MeSH terms. The three sources were merged and de-duplicated by DOI, PMID and fuzzy title-plus-year matching to generate the integrated corpus underlying this review. Scopus, Web of Science, Embase and Cochrane Library queries were not included in the executed search; the implications of this database-scope decision are addressed in §4.6 (Limitations). The complete database query syntaxes are provided in Supplementary Material S2 (reproducing `/02-search-strategies.md` of the repository).

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

No publication-type filter was applied at the database level; document-type filtering was carried out manually during screening to avoid the loss of relevant records mis-indexed at source. The OpenAlex and Crossref API queries used PICO-equivalent free-text terms (`Acinetobacter baumannii` AND (`quorum sensing` OR `quorum quenching` OR `abaI` OR `abaR` OR `autoinducer` OR `acyl-homoserine lactone`)) with date and language filters matched to the PubMed strategy (Supplementary Material S2). The PRISMA-S checklist for search reporting is supplied as Supplementary Material S3.

## 2.5 Study selection

Records identified by the PubMed search (n = 340), OpenAlex (n = 351) and Crossref (n = 3,060) were imported into a structured reference catalogue and de-duplicated by DOI, PMID and fuzzy title-plus-year matching, yielding 3,313 unique records (Figure 1). Records were screened against the eligibility criteria of §2.2 in two stages: (i) title and abstract screening to remove records outside the population, exposure or design scope; and (ii) full-text assessment of records meeting the initial criteria. Eligibility decisions were verified by checking against full-text content where available, with structured cross-checks against the data-extraction form and the master catalogue. Reasons for full-text exclusion were recorded against a pre-defined list (wrong population, wrong exposure, wrong outcome, wrong design, full text unavailable, retraction). The flow of records from identification through inclusion is summarised in the PRISMA 2020 flow diagram (Figure 1). Cross-database corroboration between PubMed, OpenAlex and Crossref is reported in §3.1 as a validation metric for indexing coverage.

## 2.6 Data extraction

A standardised data-extraction form (`/04-data-extraction-form.md`) was developed and piloted on ten randomly selected records spanning all major study types. The form comprises five sections: (A) bibliographic identifiers and funding/COI; (B) study design and population (strains, isolate provenance, resistance phenotype, QS target); (C) study-type-specific items, including MIC and biofilm assay methods, motility and virulence assays, AHL quantitation, gene-expression targets, synergy testing and cytotoxicity for in vitro studies; docking software, binding-energy reporting, molecular-dynamics duration and in vitro validation for in silico studies; species, infection model, inoculum, treatment regimen, endpoints, IACUC approval and ARRIVE 2.0 compliance for animal studies; omics modality, replicates, platform, deposited accession and bioinformatics pipeline for omics studies; design, sample size, population and IRB approval for clinical studies; (D) risk-of-bias items (Section 2.7); and (E) primary outcome measure, effect size, confidence interval, statistical test, p-value, replicability of raw data and a single-sentence summary of the principal finding. Extraction was performed using a structured protocol with internal consistency checks, including multi-pass categorisation, validation of extracted items against the master catalogue, and reconciliation of conflicting entries by recourse to full text.

## 2.7 Risk of bias and methodological quality assessment

Methodological quality and risk of bias were appraised at the field level — i.e., as the distribution of reporting and design patterns across the corpus — using design-appropriate frameworks as reference standards:

- **In vitro studies:** A modified CRIS (Consensus on Reporting In vitro Studies) checklist [Krithikadatta 2014], extended with items capturing biological/technical replicate number, strain provenance, blinded outcome assessment and statistical handling.
- **Animal (in vivo) studies:** SYRCLE Risk of Bias Tool [Hooijmans 2014] supplemented by ARRIVE 2.0 reporting items [Percie 2020].
- **Observational clinical studies:** JBI Critical Appraisal Checklists (analytical cross-sectional, cohort or case series, as appropriate) [JBI 2020]; the Newcastle–Ottawa Scale where cohort comparisons were reported [Wells 2014].
- **In silico studies:** A CHARMS-modified checklist [Moons 2014] covering target validity, software validation, conformational sampling and external validation.
- **Omics studies:** MIQE for qPCR datasets [Bustin 2009] and MINSEQE-aligned criteria for high-throughput sequencing, including accession deposition and analysis-pipeline transparency.

Because no randomised controlled trial of a QS-targeting agent in *A. baumannii* was identified, the Cochrane RoB 2.0 instrument [Sterne 2019] was not applied. Field-level reporting and bias patterns are summarised in §3.9 and visualised in Figure 5; the most prominent patterns (selection bias around isolate panel disclosure, performance bias in unblinded biofilm scoring, reporting bias arising from positive-result skew, and heterogeneity in dose and assay) are described directly in the body of the review rather than tabulated per study, in keeping with the field-level scope of this synthesis.

## 2.8 Effect measures and synthesis

The primary outcomes for synthesis were: (i) biofilm inhibition expressed as percent reduction relative to control at a defined concentration; (ii) MIC and MBEC fold-change of an antibiotic co-administered with a QS-targeting agent; (iii) reduction in virulence factor activity or expression (protease, siderophore, motility, OMV, host-cell injury); and (iv) in vivo bacterial burden (log10 CFU reduction) and host survival (percent at defined time point). Secondary outcomes included AHL quantitation, QS-regulon gene-expression fold-change, cytotoxicity (IC50, selectivity index) and synergy classification (FIC index categories).

Studies were grouped a priori by intervention class (natural product, synthetic small molecule, enzymatic quorum quencher, peptide/AMP, bacteriophage, nanoparticle, repurposed drug, antibody/vaccine, genetic perturbation) crossed with outcome domain, and by experimental system (in vitro, in vivo, in silico, omics, clinical). The synthesis is narrative with structured outcome tabulation, in line with SWiM guidance [Campbell 2020]; heterogeneity in strain background, intervention concentrations, assay formats and outcome definitions precluded a formal pooled meta-analysis (§3.9.3). Effect sizes are summarised by intervention class in Table 2 and aggregated by outcome domain in §3.8. Where three or more comparable studies reported a quantitative outcome in compatible units within the largest outcome subgroup (biofilm inhibition), we examined the distribution of reported effect sizes descriptively but did not pool. Sub-analyses by strain (ATCC 17978 vs. clinical isolates), assay format (crystal violet vs. confocal microscopy for biofilm; broth microdilution vs. E-test for MIC) and isolate resistance phenotype (susceptible vs. CRAB/MDR/XDR) are reported in §3.7–§3.9.

## 2.9 Publication bias

Funnel-plot asymmetry was considered for the largest outcome subgroup (biofilm inhibition); however, the heterogeneity of effect-size metrics, sub-MIC concentration choices and assay formats precluded construction of a comparable effect-estimate set sufficient for quantitative Egger's regression [Egger 1997]. Small-study effects, positive-result skew and selective reporting are therefore assessed narratively in §3.9.2 and revisited in §4.6.

## 2.10 Reporting framework

The review is reported in accordance with PRISMA 2020 [Page 2021] for overall structure, PRISMA-S [Rethlefsen 2021] for the literature search and SWiM [Campbell 2020] for the narrative synthesis; the PRISMA-NMA extension was not applicable because no network meta-analysis is conducted. Because heterogeneity in outcome definitions, assays and strain background precluded quantitative pooling, formal GRADE certainty grading was not applied at the body-of-evidence level; instead, the certainty of mechanistic, preclinical and translational claims is discussed narratively in §4. All data-extraction forms, code, search logs and intermediate datasets are deposited on the project repository.
