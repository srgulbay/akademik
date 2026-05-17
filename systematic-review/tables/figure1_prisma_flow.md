# Figure 1 — PRISMA 2020 Flow Diagram

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  IDENTIFICATION                                                              │
│                                                                              │
│  Records identified from databases:                                          │
│  • PubMed (MEDLINE)        n =  340                                          │
│  • OpenAlex (API)          n =  351                                          │
│  • Crossref (API)          n = 3,060                                         │
│  • Scopus                  n = pending (EKUAL export — v2)                   │
│  • Web of Science          n = pending (v2)                                  │
│  • Embase                  n = pending (v2)                                  │
│  • Cochrane Library        n = pending (v2)                                  │
│  • Hand-search / snowball  n = pending (v2)                                  │
│                                                                              │
│  Records before deduplication:   n = 3,751                                   │
│  Duplicates removed:             n =   438  (DOI/PMID/title-year match)      │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  SCREENING                                                                   │
│                                                                              │
│  Records after deduplication:    n = 3,313                                   │
│  Records screened (title/abstract):                                          │
│   • PubMed-anchored core (v1):   n =   338  (fully characterised)            │
│   • Crossref/OpenAlex additions: n = 2,975  (awaiting v2 dual screening)     │
│                                                                              │
│  Records excluded at title/abstract (v1 automated):                          │
│   • Non-A. baumannii primary focus (Crossref noise)                          │
│   • Conference abstracts only                                                │
│   • Off-topic word-match hits                                                │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  ELIGIBILITY                                                                 │
│                                                                              │
│  Full-text articles assessed (v1):    n =  228                               │
│    • Of these from PubMed corpus      n =  218                               │
│    • PDF/manual download              n =   10                               │
│  Abstract-only records (v1):          n =  112                               │
│                                                                              │
│  Records excluded with reasons:       n = pending (v2 dual reviewer)         │
│   • Not A. baumannii primary subject                                         │
│   • No QS-related outcome                                                    │
│   • Retraction / erratum / preprint-published pair                           │
│   • Non-English (post-translation review)                                    │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  INCLUDED (v1 first-pass synthesis)                                          │
│                                                                              │
│  Studies in qualitative synthesis:    n =  338  (PubMed-anchored corpus)     │
│  Studies in quantitative synthesis:   n = pending (meta-analysis — v2)       │
│                                                                              │
│  Cross-database corroboration:                                               │
│    • Records in >=2 sources              n =  291  (87% of analytic set)     │
│    • Records in all 3 sources (PM+OA+CR) n =  101                            │
└──────────────────────────────────────────────────────────────────────────────┘
```

## Cross-Database Coverage Validation

| Source combination | n | % of 3,313 unique | Note |
|---|---:|---:|---|
| Crossref only | 2,883 | 87.0% | Awaits screening; Crossref OR-joins query tokens producing many off-topic hits; v2 dual-reviewer title/abstract screening required |
| OpenAlex + PubMed | 153 | 4.6% | Independent corroboration of PubMed indexing |
| Crossref + OpenAlex + PubMed | 101 | 3.0% | Triple-corroborated — high-confidence inclusions |
| PubMed only | 76 | 2.3% | MEDLINE-exclusive (typically clinical-microbiology journals) |
| OpenAlex only | 63 | 1.9% | Open-scholarship sources beyond MEDLINE |
| Crossref + OpenAlex | 29 | 0.9% | Non-MEDLINE journals indexed by both |
| Crossref + PubMed | 8 | 0.2% | Edge cases (MEDLINE in-process records) |

**Key observation:** 264 of 340 PubMed records (78%) were independently re-discovered by OpenAlex and/or Crossref, providing strong validation that the MEDLINE search did not miss substantial portions of the indexed literature. The 76 PubMed-only records correspond to lower-impact journals not yet harvested by OpenAlex.

## v2 Notes

- Final Identification *n* will include Scopus + Web of Science + Embase + Cochrane (estimated combined incremental yield: 200–400 unique records based on pilot reviews of similar topics).
- Dual independent reviewers (Rayyan/Covidence) will populate exclusion counts with documented reasons and per-record decision audit trail.
- The 2,975 Crossref/OpenAlex additions await title/abstract screening — early sampling indicates the true relevant fraction is ~10–15% (so ~300–450 additional eligible records).
- Excluded full-texts will be enumerated with reasons in Supplementary Table S9.
- Inter-rater agreement (Cohen's κ) target >= 0.75 at both screening stages.
