# IJAA Submission Compliance Audit

**Manuscript:** *Quorum Sensing in Acinetobacter baumannii: Molecular Architecture, Therapeutic Targeting and Translational Horizons — A Systematic Review (2003–2025)*
**Target journal:** International Journal of Antimicrobial Agents (IJAA), Elsevier
**Audit date:** 2026-05-17
**Auditor:** Submission compliance specialist (automated audit, pre-submission review)
**Audited file:** `/home/user/akademik/systematic-review/MANUSCRIPT.md`

---

## Summary

Total items checked: 22
- **PASS:** 11
- **WARN:** 7
- **FAIL:** 4

The manuscript is structurally sound and aligns with IJAA's preferences for systematic reviews. Substantive blockers before submission are (a) the unfinished author/affiliation block, (b) the Highlights bullets all exceeding the 85-character ceiling, and (c) the Abstract exceeding 300 words. Several formatting issues are easily remediable (ASCII-art figures need to be replaced with their PNG/TIFF equivalents already present in `/figures/`; table numbering is non-contiguous).

---

## Detailed Findings

### 1. Title — character length

- **Item:** Title ≤ 150 characters (IJAA preference; hard cap ~200).
- **Current state:** 149 characters (including spaces, excluding markdown emphasis).
- **Status:** PASS (just inside the soft ceiling).
- **Recommendation:** No change required. Title is within preferred length and contains the population, intervention area, study type and review period — strong PICO signal for editorial triage.

### 2. Title — content and study-type signalling

- **Item:** Title should declare the study type for systematic reviews.
- **Current state:** Title contains "A Systematic Review (2003–2025)".
- **Status:** PASS.
- **Recommendation:** None.

### 3. Highlights — count

- **Item:** 3–5 bullets.
- **Current state:** 5 bullets.
- **Status:** PASS.
- **Recommendation:** None.

### 4. Highlights — per-bullet length (≤ 85 characters including spaces)

- **Item:** Each highlight ≤ 85 characters.
- **Current state:** All five highlights exceed the ceiling (lengths: 307, 220, 194, 180, 195 characters).
- **Status:** FAIL.
- **Recommendation:** Rewrite each bullet as a single declarative sentence with strict ≤ 85-character budget. Suggested rewrites:
  1. "AbaI/AbaR is the core QS axis in *A. baumannii*, integrating two-component systems." (84)
  2. "Seven anti-virulence intervention classes characterised across 340 primary studies." (82)
  3. "Biofilm modulation is reported in >75% of studies; effect sizes 50–80% at sub-MIC." (82)
  4. "In vivo evidence is modest (~15%); ARRIVE 2.0 adherence and PK data are limited." (80)
  5. "Phage cocktails are the most clinically advanced QS-modulating modality to date." (80)

### 5. Abstract — structure (Background/Objective/Methods/Results/Conclusions)

- **Item:** Structured abstract with five labelled sections.
- **Current state:** All five labels present and correctly ordered.
- **Status:** PASS.
- **Recommendation:** None.

### 6. Abstract — word count (≤ 300 words)

- **Item:** Abstract ≤ 300 words.
- **Current state:** 391 words.
- **Status:** FAIL.
- **Recommendation:** Trim to ≤ 300. The Results paragraph (≈ 200 words) carries the most surplus. Suggested cuts: collapse the database list to "MEDLINE/PubMed with OpenAlex/Crossref cross-validation"; remove the explicit numeric breakdown of study designs (retain only the dominant categories); drop the LC-MS/MS detail (move to main text); compress the methodological quality sentence.

### 7. Keywords — count (4–7)

- **Item:** 4–7 keywords.
- **Current state:** 10 keywords.
- **Status:** WARN.
- **Recommendation:** Trim to 6: *Acinetobacter baumannii*; quorum sensing; quorum quenching; biofilm; phage therapy; antimicrobial resistance. Drop "AbaI", "AbaR", "ESKAPE pathogens" and "systematic review" (latter is captured by the article type metadata in Editorial Manager).

### 8. Main text word count

- **Item:** Systematic reviews typically 6,000–10,000 words; IJAA accepts longer reviews with justification.
- **Current state:** ≈ 18,020 words for main text including figures/tables/legends (≈ 23,126 words per author's own count including references).
- **Status:** FAIL.
- **Recommendation:** Substantial trim required. Target ≤ 10,000 words (excluding references, tables, legends). Candidate reductions: (i) condense Section 3.3 (Molecular Network) — currently ~3,500 words — by ~30%; (ii) move detailed per-phage and per-compound descriptions in Section 3.4 to a Supplementary "Intervention dossier"; (iii) condense Section 3.9 (Methodological Quality) into one tighter sub-section and move the MIQSAb proposal to a free-standing supplementary box. Alternatively, request the editorial office's permission for a long-form review at submission and justify in the cover letter.

### 9. References — style (Vancouver, numbered in order of appearance)

- **Item:** Numbered Vancouver style with sequential appearance numbering and Index Medicus journal abbreviations.
- **Current state:** Numbered list (n = 93). Mixed citation styles in the body text: bracketed numerics (e.g. `[1]`, `[76]`) coexist with named-anchor citations (e.g. `[Cui_2025]`, `[Niu_2008]`).
- **Status:** FAIL.
- **Recommendation:** Convert all named-anchor citations to numbered references that match the reference list ordering. A single citation processor pass (e.g. pandoc + CSL Vancouver) against `bibliography.json` should resolve this; ensure the first citation of each reference in the text corresponds to its number in the list.

### 10. References — count and IJAA expectations

- **Item:** Systematic reviews typically cite 50–150 references; IJAA does not impose a hard ceiling.
- **Current state:** 93 references.
- **Status:** PASS.
- **Recommendation:** None.

### 11. References — journal abbreviations

- **Item:** Index Medicus abbreviations.
- **Current state:** Mix of full names ("Journal of bacteriology") and shorter forms ("BMJ").
- **Status:** WARN.
- **Recommendation:** Standardise all journal names to NLM/Index Medicus abbreviations (e.g. "J Bacteriol", "Antimicrob Agents Chemother", "Clin Microbiol Infect"). A CSL "Vancouver-superscript" style will produce this automatically.

### 12. Tables — count and presentation

- **Item:** ≤ 6 main-text tables.
- **Current state:** Three numbered tables in text (Table 1, Table 2, Table 3). Numbering is non-contiguous in the section order (Table 1 in Results 3.2, Table 3 in Results 3.3, Table 2 in Results 3.4) — Table 3 is introduced before Table 2.
- **Status:** WARN.
- **Recommendation:** Re-number to match order of first mention (current Table 3 → Table 2; current Table 2 → Table 3) or re-order their introduction.

### 13. Figures — count, format and resolution

- **Item:** ≤ 8 figures; ≥ 300 DPI; vector format preferred.
- **Current state:** Two figures referenced in text (Figure 1 PRISMA, Figure 2 publication trends), but the manuscript renders both as ASCII art. The repository `/figures/` directory contains six figures (`figure1_prisma_flow.{png,svg}`, `figure2_trends.{png,svg}`, `figure3a_qs_circuit.{png,svg}`, `figure3b_second_messengers.{png,svg}`, `figure4_interventions.{png,svg}`, `figure5_rob_heatmap.{png,svg}`, `figure6_network.{png,svg}`) that are not cited in the manuscript.
- **Status:** FAIL.
- **Recommendation:** Replace ASCII-art block diagrams with the PNG/SVG renderings already on disk and cite Figures 3A/3B (referenced inline as "suggested schemas" in §3.3.1 and §3.3.5), Figure 4 (intervention landscape), Figure 5 (RoB heatmap) and Figure 6 (network). At submission, supply 300 DPI TIFF or PDF for each figure with text in editable vector layers where possible.

### 14. Supplementary materials — PRISMA checklist

- **Item:** PRISMA 2020 checklist mandatory for SRs.
- **Current state:** Present at `/supplementary/S1_prisma2020_checklist.md` and `.docx`.
- **Status:** PASS.
- **Recommendation:** None.

### 15. Supplementary materials — search strategies and PRISMA flow

- **Item:** Search strategies and PRISMA flow data should accompany the SR.
- **Current state:** Search strategies in `02-search-strategies.md` and an integrated literature merge log under `/literature/`.
- **Status:** PASS.
- **Recommendation:** None; ensure both are renamed and re-numbered consistently (S2, S3) at submission packaging.

### 16. Supplementary materials — declared inventory

- **Item:** Supplementary list at end of manuscript matches files on disk.
- **Current state:** 8 supplementary items declared (S1–S8). The repository contains the underlying files. Figure source files are not yet packaged as a Supplementary unit.
- **Status:** WARN.
- **Recommendation:** Add an explicit "S9 — figure source files" or fold figure source files into S8.

### 17. Title page — required elements

- **Item:** Title, authors, affiliations, corresponding author with email, word count, conflicts of interest, funding, ethical approval, keywords, author contributions.
- **Current state:** Author block reads "*To be completed at submission*". No standalone title page exists.
- **Status:** FAIL.
- **Recommendation:** A title page template has been generated at `/submission/title_page.md` (and `.docx`). Authors must complete the placeholder fields before submission.

### 18. Author contributions — CRediT taxonomy

- **Item:** Author contributions per CRediT.
- **Current state:** No CRediT statement in the manuscript text.
- **Status:** FAIL.
- **Recommendation:** A CRediT scaffold is included in the title page template at `/submission/title_page.md`. Each author should be mapped against the 14 CRediT roles.

### 19. Cover letter

- **Item:** Cover letter is mandatory at submission.
- **Current state:** Not present at start of audit.
- **Status:** PASS (created at `/submission/cover_letter.md` and `.docx` as part of this submission package).
- **Recommendation:** Authors should personalise placeholders before submission.

### 20. Reporting guideline — PRISMA 2020

- **Item:** PRISMA 2020 must be followed for SRs.
- **Current state:** Manuscript states adherence and provides Supplementary S1 (PRISMA 2020 checklist). Section 2 documents the PRISMA-S and SWiM extensions.
- **Status:** PASS.
- **Recommendation:** None.

### 21. Protocol registration (PROSPERO)

- **Item:** Prospective protocol registration expected for SRs.
- **Current state:** Manuscript indicates "PROSPERO CRD pending" with the protocol document on file. Registration not yet completed.
- **Status:** WARN.
- **Recommendation:** Either complete PROSPERO registration before submission and update the manuscript with the CRD number, or transparently disclose retrospective/staggered registration in the methods and cover letter (PROSPERO accepts retrospective registration of completed reviews on an exceptions basis).

### 22. Data and code availability

- **Item:** IJAA expects a Data Availability Statement.
- **Current state:** No standalone statement in main manuscript; data are listed in the Supplementary section.
- **Status:** WARN.
- **Recommendation:** Insert the dedicated Data Availability Statement (`/submission/data_availability_statement.md`) at the end of the main manuscript, before the references, and reference Zenodo DOI placeholder.

### 23. Manuscript file format

- **Item:** .doc/.docx submission required.
- **Current state:** `MANUSCRIPT_FINAL.docx` exists alongside the .md source.
- **Status:** PASS.
- **Recommendation:** Confirm final .docx is generated from the corrected source after Highlights/Abstract/word-count fixes.

### 24. Manuscript formatting — double spacing and line numbers

- **Item:** Double-spaced text with continuous line numbers preferred for review.
- **Current state:** Unknown for the current `MANUSCRIPT_FINAL.docx`; the Markdown source carries no formatting state.
- **Status:** WARN.
- **Recommendation:** When generating the submission `.docx`, apply double line spacing (Word "Line spacing → 2.0") and continuous line numbering (Layout → Line Numbers → Continuous).

---

## Top 3 must-fix issues (blocking submission)

1. **Highlights all exceed 85 characters (item 4).** Editorial pre-screening at Elsevier journals catches this automatically and returns the manuscript unread.
2. **Abstract exceeds 300 words (item 6).** Same auto-screen risk.
3. **Citation style is inconsistent (item 9) and the author/affiliation block is empty (item 17).** Both must be resolved before the submission portal will accept the file.

## High-priority issues (do before submission)

- Replace ASCII figures with TIFF/PDF (item 13) and cite the additional figures already on disk.
- Reduce main text from ~18,000 to ≤ 10,000 words, or pre-clear an extended length with the editorial office (item 8).
- Re-number tables to match order of appearance (item 12).
- Complete CRediT statement (item 18).
- Complete or formally disclose PROSPERO registration status (item 21).

## Lower-priority polish

- Trim keywords to 6 (item 7).
- Standardise journal abbreviations (item 11).
- Add a free-standing Data Availability Statement at end of main text (item 22).
- Confirm double spacing and line numbering in the final .docx (item 24).
