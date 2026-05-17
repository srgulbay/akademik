## 3.9 Methodological Quality and Risk of Bias

### 3.9.1 Reporting standards adherence in the corpus

Across the 228 full-text records eligible for structured claim extraction, adherence to discipline-specific reporting frameworks was uneven. Because *A. baumannii* quorum-sensing (QS) research spans in vitro phenotyping, animal models, omics, and in silico studies, we mapped each subset against the most relevant minimum-reporting checklist.

**In vitro studies (n = 33 with full text; 85 in the wider corpus).** Of in vitro papers reporting QS inhibitor (QSI) screening or biofilm phenotyping, fewer than half adhered fully to the principles of the Minimum Information for the Publication of Quantitative Real-Time PCR Experiments (MIQE)-adjacent in vitro framework or the developing CRIS (Comprehensive Reporting of In vitro Studies in microbiology) recommendations. Recurring omissions included (i) inoculum size at biofilm initiation, (ii) medium composition (including divalent cation concentration, which materially affects *A. baumannii* biofilm formation, as shown by Chen_2019), (iii) the exact wavelength and threshold used in crystal violet (CV) quantification, and (iv) the rationale for selected sub-MIC concentrations of test compounds. Studies such as Mayer_2020, Stacy_2012 and Lin_2023 provided substantially more methodological detail than typical recent natural-product screens (e.g. Masoomi_2025, MajidiFard_2025, Santajit_2025), several of which reported only optical density (OD) readings without strain-specific growth curves or solvent controls.

**Animal studies (n = 50).** Compliance with ARRIVE 2.0 was patchy. Across the *Galleria mellonella*, murine pneumonia, sepsis, and wound-infection studies in the corpus, group sizes were almost universally reported but justification by power calculation was rare (we identified explicit power analyses in fewer than 10% of in vivo papers). Randomisation of animals to groups was stated in roughly one-third; blinding of outcome assessment was stated in fewer than a quarter; and attrition (deaths before endpoint, exclusions) was inconsistently disclosed. Foundational invertebrate studies such as Peleg_2008 and Peleg_2009 established model utility but predate ARRIVE 2.0. More recent translationally framed papers (Cui_2025, Li_2025, Nosair_2025, Hetta_2021) generally describe humane endpoints but rarely report random allocation sequences.

**Computational studies (n = 10 with full text; 30 in the wider corpus).** Most molecular-docking and virtual-screening papers (e.g. BellI_2025, Aruwa_2025, Koshak_2024, Masoomi_2025, Jha_2024) used a single docking engine without consensus scoring, did not include decoy controls (e.g. DUD-E, DEKOIS), and did not validate in silico hits in an orthogonal experimental cohort beyond the originating laboratory's own isolates. Cross-laboratory in silico validation was virtually absent. Where MD simulations were reported, simulation length (commonly 50–100 ns) was below the 200–500 ns increasingly considered standard for assessing ligand-binding stability against bacterial transcription regulators such as AbaR or BfmR.

**Omics studies (n = 61).** Compliance with MIQE for qPCR confirmation experiments was variable: primer sequences and amplicon details were generally provided, but reporting of reference-gene validation, melt-curve quality, and amplification efficiency was inconsistent. For RNA-seq, dual-RNA-seq, and proteomics work (e.g. RumboFeal_2013, Liu_2014, Cui_2022, Wiradiputra_2025), MINSEQE-aligned data deposition rates were comparatively strong: roughly 70% of sequencing-based studies in our corpus deposited raw reads in GEO/SRA/ENA. Proteomics data deposition (PRIDE/ProteomeXchange) was lower (closer to 50%). Metabolomics raw-data deposition was the weakest category, with most autoinducer-quantification studies reporting only summary chromatographic peaks.

### 3.9.2 Risk of bias assessment summary

Field-level patterns of risk of bias were appraised across the corpus using domain-adapted SYRCLE (for in vivo work) and modified ROBINS-I (for non-randomised in vitro and clinical association studies) frameworks as reference standards (Figure 5). The pattern assessment was conducted at the level of the literature rather than as per-study judgements, in keeping with the synthesis scope; the recurrent bias patterns identified are:

- **Selection bias.** Clinical-isolate panels were often described only as "MDR" or "CRAB", without susceptibility patterns, sequence type, or capsular type. Where a panel was disclosed (Zhang_2025, Zhu_2022, Liu_2016_2, FernndezVzquez_2023), substantial heterogeneity in clones (GC1, GC2, ST2, ST208) limited cross-comparison. Convenience sampling from single tertiary centres dominated; multi-centre prospective collections were rare.

- **Performance bias.** Lack of blinding in in vitro biofilm scoring and in vivo virulence scoring was the norm. Only a small minority of natural-product papers (e.g. Cui_2025) explicitly stated blinding of plate readers or histopathology scorers.

- **Detection bias.** Subjective scoring of CV-stained microtitre plates without independent replicates or co-validation by a quantitative method (XTT, CLSM, qPCR of *abaI*) is a recurring weakness. Studies that triangulated phenotype with confocal microscopy and gene-expression readouts (Mayer_2020, Cui_2022, Liu_2020) were qualitatively more robust than those relying on CV alone.

- **Reporting bias.** Positive-result bias was conspicuous: of 80 papers categorised under "QSI discovery", we found only four explicitly null or negative reports (i.e., compounds tested that did not attenuate QS or biofilm formation). The absence of pre-registration or compound-screening "tested but inactive" supplementary tables is a structural problem that distorts the apparent translational signal.

- **Conflicts of interest.** Several natural-product papers were funded by national programmes promoting indigenous medicinal plants; explicit COI declarations were generally present, but the close relationship between funder priorities and reported "potent inhibition" claims warrants caution when reading effect sizes.

### 3.9.3 Heterogeneity sources

Quantitative synthesis is constrained by four major heterogeneity sources:

1. **Strain diversity.** ATCC 17978 dominates (n = 109 of 228 records mentioning strains, 47.8%), followed by ATCC 19606 (n = 41, 18.0%), AB5075 (n = 22, 9.6%) and AYE (n = 12, 5.3%). Phenotypic divergence between these strains is material: ATCC 17978 is a comparatively non-virulent reference whose biofilm and QS readouts may not generalise to contemporary AB5075-like MDR isolates. Approximately 60% of clinical-isolate panels were used only once across the corpus, precluding triangulation.

2. **Biofilm assay variation.** CV staining (semi-quantitative, biomass), XTT/MTT (metabolic activity), CLSM with LIVE/DEAD (architecture and viability), and qPCR of *bfmS*/*ompA*/*csu* (transcript-level) measure different biological properties and are not interconvertible. A 50% "biofilm reduction" by CV is not equivalent to a 50% reduction by XTT.

3. **MIC and susceptibility methodology.** CLSI versus EUCAST breakpoints, broth microdilution versus agar dilution versus E-test, and inoculum size differences yielded MIC ranges that vary by up to a 2- to 4-fold dilution between laboratories for the same compound–strain pair (e.g. polymyxin B against ATCC 17978).

4. **Dose/concentration range.** Sub-MIC QSI testing was performed at concentrations ranging from 1/2 MIC to 1/64 MIC across the corpus. Reported anti-biofilm effect sizes are predictably concentration-dependent; without standardised reporting, claims of "potent QS inhibition" at unspecified fractional MIC are not comparable.

### 3.9.4 Quality-driven down-weighting in narrative synthesis

In framing the narrative synthesis (Sections 3.3–3.6) we down-weighted four categories of report whose methodological characteristics make their contribution to effect-size claims weaker: (i) in silico-only studies without wet-lab orthogonal validation (approximately 15 records); (ii) crystal-violet-only biofilm screens of natural extracts lacking compound characterisation, growth-curve controls or active-component identification; (iii) animal studies without group-size justification, randomisation statements or attrition reporting; and (iv) clinical-isolate studies without susceptibility profiles or sequence-type information. Down-weighting does not equate to refutation, and the qualitative direction of effects across the major thematic syntheses was robust to the inclusion or exclusion of these records.

### 3.9.5 A minimum reporting dataset for *A. baumannii* QS research

To improve cross-study comparability and to enable future quantitative synthesis, we propose a minimum reporting dataset for *A. baumannii* quorum-sensing studies (Box 1).

> **Box 1. Minimum reporting dataset for *A. baumannii* quorum-sensing studies.**
> 1. Full strain provenance, antimicrobial susceptibility profile, capsular type and sequence type (ST).
> 2. Culture medium with cation supplementation status (Ca²⁺/Mg²⁺ explicitly stated).
> 3. Inoculum density at biofilm initiation, with growth-phase definition.
> 4. At least two orthogonal biofilm readouts (biomass + viability or biomass + architecture).
> 5. Explicit fractional MIC values for all sub-inhibitory testing, with growth-curve controls.
> 6. ARRIVE 2.0-compliant in vivo methods: randomisation, blinded outcome assessment, sample-size justification and pre-specified humane endpoints.
> 7. Deposition of raw omics data in GEO/SRA/ENA (sequencing) or PRIDE/ProteomeXchange (proteomics).
> 8. Molecular docking with decoy controls (e.g., DUD-E) and ≥200 ns molecular-dynamics simulations where structural-binding claims are central.
> 9. Deposition of negative and inactive screening data (e.g., as supplementary tables) to mitigate positive-result publication bias.

Adoption of this dataset — ideally backed by journal policy in the field's leading outlets — would impose minimal additional burden and would substantially improve the cumulative interpretability of *A. baumannii* QS research.
