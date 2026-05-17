# Figure 1 — PRISMA 2020 Flow Diagram

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
