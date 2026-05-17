# Veri Çıkarım Formu — QS in *A. baumannii* Sistematik Review

> Bu form, literatür haritasındaki çalışma tipi dağılımına göre tasarlanmıştır
> (%25 in vitro, %20 omics, %15 animal model, %9 in silico, %8 review, %4 clinical).
> Her dahil edilen makale için **iki bağımsız ekstraktör** doldurur, üçüncü hakem
> uyuşmazlıkları çözer (Cohen's κ ≥ 0.75 hedef).

**Form versiyonu:** v1.0 — 2026-05-17
**Pilot:** İlk 10 makalede kalibre edilecek; gerekli değişiklikler v1.1 olarak işaretlenir.

---

## Bölüm A — Bibliyografik Bilgi (tüm makaleler)

| Alan | Tip | Açıklama |
|---|---|---|
| `study_id` | string | `İlkYazar_Yıl` (örn. `Beasley_2025`) |
| `extractor` | string | Ekstraktörün baş harfleri |
| `extraction_date` | date | YYYY-MM-DD |
| `doi` | string | DOI (zorunlu) |
| `pmid` | string | PubMed ID |
| `first_author` | string | Birinci yazar (soyad, ad baş harfi) |
| `corresponding_author` | string | Sorumlu yazar + kurum |
| `country` | string | Sorumlu yazarın ülkesi |
| `year` | int | Yayın yılı |
| `journal` | string | Tam dergi adı |
| `journal_impact_factor` | float | Yayın yılındaki JCR IF (varsa) |
| `funding_source` | string | Fonlama kaynakları (COI değerlendirmesi için) |
| `coi_declared` | yes/no/none | Çıkar çatışması beyanı |

---

## Bölüm B — Çalışma Tasarımı Sınıflandırması (tüm makaleler)

| Alan | Tip | Açıklama |
|---|---|---|
| `study_type_primary` | enum | `in_vitro` / `in_silico` / `animal_model` / `omics` / `clinical` / `methodology` / `review` / `mixed` |
| `study_type_secondary` | enum[] | Birden fazla yöntem varsa (örn. in vitro + in silico kombinasyonu) |
| `organism_strains` | string | Kullanılan suşlar (`ATCC 17978`, `ATCC 19606`, `AB5075`, klinik izolatlar, vs.) |
| `n_isolates` | int | Test edilen izolat/suş sayısı |
| `clinical_source` | enum | `lab_strain_only` / `clinical_isolates` / `mixed` |
| `resistance_phenotype` | enum[] | `MDR` / `XDR` / `PDR` / `carbapenem_R` / `colistin_R` / `susceptible` / `not_specified` |
| `qs_target` | enum[] | `abaI` / `abaR` / `abaM` / `BfmRS` / `RstAB` / `general_QS_network` / `other` |
| `intervention_type` | enum | `natural_product` / `synthetic_compound` / `phage` / `nanoparticle` / `peptide` / `enzyme_qq` / `repurposed_drug` / `antibody_vaccine` / `none` |
| `intervention_name` | string | Ajan adı (`carnosol`, `berberine`, `vB-AbaM-fThrA`, vs.) |
| `intervention_source` | string | Doğal kaynak (bitki, mikroorganizma) veya sentetik |
| `comparator` | string | Kontrol (DMSO, vehicle, untreated, antibiyotik tek başına, vs.) |

---

## Bölüm C — Çalışma Tipine Özgü Bölümler

### C1. In Vitro Çalışmalar (~85 makale beklenir)

| Alan | Tip | Açıklama |
|---|---|---|
| `mic_method` | enum | `broth_microdilution` / `agar_dilution` / `e_test` / `disk_diffusion` / `time_kill` |
| `mic_baseline_µg_ml` | float | Ajanın tek başına MIC değeri |
| `sub_mic_used` | float | QS deneylerinde kullanılan alt-MIC konsantrasyon |
| `biofilm_assay` | enum | `crystal_violet` / `xtt` / `mtt` / `confocal_microscopy` / `congo_red` / `other` |
| `biofilm_inhibition_pct` | float | % inhibisyon (test konsantrasyonunda) |
| `biofilm_eradication_tested` | yes/no | Pre-formed biofilm üzerinde test edildi mi? |
| `motility_assays` | enum[] | `swimming` / `swarming` / `twitching` / `surface_associated` |
| `qs_signal_quantified` | yes/no | AHL/diğer sinyal molekülü ölçüldü mü? |
| `qs_signal_method` | enum | `lc_ms` / `gc_ms` / `biosensor_strain` / `tlc` / `none` |
| `gene_expression_targets` | string | qPCR ile bakılan genler (örn. `abaI, csuA/B, bap, ompA`) |
| `virulence_factors_measured` | enum[] | `protease` / `lipase` / `siderophore` / `pyoverdine` / `capsule` / `OMV` / `other` |
| `synergy_tested` | yes/no | Antibiyotik ile kombinasyon? |
| `synergy_method` | enum | `checkerboard` / `time_kill` / `e_test_strip` / `none` |
| `fic_index` | float | FIC indeksi (varsa) |
| `synergy_classification` | enum | `synergy` / `additive` / `indifferent` / `antagonism` |
| `cytotoxicity_tested` | yes/no | İnsan/memeli hücresinde sitotoksisite? |
| `cytotoxicity_ic50` | float | IC50 (varsa, µg/mL veya µM) |
| `selectivity_index` | float | IC50/MIC (varsa) |

### C2. In Silico Çalışmalar (~30 makale)

| Alan | Tip | Açıklama |
|---|---|---|
| `target_protein` | string | Hedef (örn. `AbaR`, `BfmR`, `LasR-homolog`) |
| `target_pdb_id` | string | PDB ID veya homoloji modeli kaynağı |
| `docking_software` | enum | `AutoDock_Vina` / `Glide` / `GOLD` / `SwissDock` / `other` |
| `n_compounds_screened` | int | Taranan bileşik sayısı |
| `top_hits_n` | int | Bildirilen top-hit sayısı |
| `binding_energy_kcal_mol` | float | En iyi skor (kcal/mol) |
| `md_simulation_done` | yes/no | MD simülasyonu yapıldı mı? |
| `md_duration_ns` | float | MD süresi (ns) |
| `rmsd_stable` | yes/no | Trajektör stabil mi? |
| `admet_evaluated` | yes/no | ADMET tahmini? |
| `in_vitro_validation` | yes/no | Hesaplama sonrası deneysel doğrulama? |

### C3. Hayvan Modeli / In Vivo (~50 makale)

| Alan | Tip | Açıklama |
|---|---|---|
| `model_organism` | enum | `mouse_C57BL_6` / `mouse_BALB_c` / `rat` / `Galleria_mellonella` / `zebrafish` / `C_elegans` / `other` |
| `infection_route` | enum | `intraperitoneal` / `intranasal` / `intratracheal` / `wound` / `bloodstream` / `other` |
| `inoculum_cfu` | string | CFU dozu |
| `treatment_route` | enum | `oral` / `iv` / `ip` / `topical` / `inhaled` |
| `treatment_dose` | string | mg/kg veya mg/L |
| `endpoint` | enum[] | `survival` / `bacterial_burden` / `histopathology` / `cytokines` / `weight_loss` |
| `survival_pct_treated_vs_control` | string | `% / %` formatında |
| `bacterial_burden_log_reduction` | float | Log10 CFU azalması |
| `iacuc_approval` | yes/no | Etik kurul onayı belirtildi mi? |
| `arrive_compliance` | yes/no | ARRIVE 2.0 raporlama kriterleri karşılanıyor mu? |

### C4. Omics Çalışmaları (~69 makale)

| Alan | Tip | Açıklama |
|---|---|---|
| `omics_type` | enum[] | `RNA_seq` / `proteomics` / `metabolomics` / `WGS` / `comparative_genomics` / `metagenomics` |
| `condition_compared` | string | Örn. `wild-type vs ΔabaI`, `untreated vs carnosol-treated` |
| `n_replicates` | int | Biyolojik tekrar sayısı |
| `platform` | string | `Illumina_NovaSeq`, `Nanopore_GridION`, `Q_Exactive`, vs. |
| `degs_count` | int | Diferansiyel ekspresyon gen/protein sayısı |
| `qs_related_degs` | string | QS-ilişkili sinyal genleri (liste) |
| `data_deposited` | yes/no | Veri public repository'de mi (SRA, PRIDE)? |
| `accession_numbers` | string | GEO/SRA/PRIDE accession'ları |
| `bioinformatics_pipeline` | string | DESeq2, edgeR, MaxQuant, Prokka, vs. |

### C5. Klinik Çalışmalar (~15 makale)

| Alan | Tip | Açıklama |
|---|---|---|
| `clinical_study_design` | enum | `case_report` / `case_series` / `retrospective_cohort` / `prospective_cohort` / `cross_sectional` / `surveillance` |
| `n_patients` | int | Hasta sayısı |
| `setting` | string | Hastane/ICU/ülke |
| `patient_population` | string | Yaş, komorbidite, infeksiyon tipi |
| `qs_biomarker_measured` | string | Hangi QS molekülü ölçüldü? (örn. `3-OH-C12-HSL plasma`) |
| `clinical_outcome` | string | Mortalite, hastanede kalış süresi, vs. |
| `correlation_qs_outcome` | string | QS düzeyi ile sonuç arasındaki korelasyon |
| `irb_approval` | yes/no | Etik onay belirtildi mi? |

---

## Bölüm D — Kalite Değerlendirmesi (study type'a göre)

| Çalışma Tipi | Araç | Min. madde |
|---|---|---|
| `in_vitro` | **CRIS** (Consensus on Reporting In vitro Studies) — modifiye | 12 |
| `animal_model` | **SYRCLE Risk of Bias Tool** | 10 |
| `clinical_observational` | **JBI Critical Appraisal** veya **Newcastle-Ottawa Scale** | 9 |
| `clinical_trial` | **Cochrane RoB 2.0** | 7 |
| `in_silico` | **CHARMS** + bizim modifiye check-list | 8 |
| `omics` | **MIQE** (qPCR) / **MINSEQE** (sequencing) | değişken |

| Alan | Tip | Açıklama |
|---|---|---|
| `quality_tool_used` | enum | Yukarıdaki listeden |
| `quality_score` | int | Karşılanan madde sayısı |
| `quality_judgment` | enum | `low_RoB` / `some_concerns` / `high_RoB` |
| `quality_notes` | string | Önemli zayıflıklar |

---

## Bölüm E — Sonuç ve Sentez Verileri (tüm makaleler)

| Alan | Tip | Açıklama |
|---|---|---|
| `primary_outcome_measure` | string | Çalışmanın birincil sonuç ölçütü |
| `primary_outcome_value` | string | Sayısal sonuç (örn. `% biofilm reduction = 78.3 at 64 µg/mL`) |
| `effect_size_reported` | yes/no | Hesaplanabilir/raporlanmış effect size var mı? |
| `effect_size` | float | Cohen's d, OR, RR, vs. |
| `ci_95` | string | %95 CI |
| `statistical_test` | string | Kullanılan test |
| `p_value` | float | p değeri |
| `replicability_data_available` | yes/no | Ham veri/protokol paylaşıldı mı? |
| `key_finding_one_sentence` | string | Yazarın ana bulgusunun tek-cümle özeti |
| `limitations_per_authors` | string | Yazarların belirttiği kısıtlamalar |
| `extractor_concerns` | string | Ekstraktörün ek notları/şüpheleri |

---

## Form Çıktısı (CSV Yapısı)

Form dolduruldukça verileri tek bir wide-format CSV'ye yazacağız:

```
literature/extraction/
├── form_template.csv          ← bu form'un boş template'i
├── extracted_2_reviewers.csv  ← iki ekstraktörün dolduğu veriler
└── adjudication_log.csv       ← uyuşmazlık çözümleri
```

`form_template.csv` kolon adları, Bölüm A-E'deki tüm `field_name`'lerin tam listesidir.

---

## Pilot Kalibrasyon Protokolü

1. **Rastgele 10 makale seç** (5 in vitro + 2 in silico + 1 omics + 1 animal + 1 clinical).
2. İki ekstraktör bağımsız doldursun.
3. Her alan için kategorik veri → **Cohen's κ**, sürekli veri → **ICC** hesapla.
4. κ < 0.6 olan alanlar → form revize, alan tanımları netleştir.
5. Pilot raporunu `literature/extraction/pilot_calibration_report.md` olarak kaydet.
6. v1.1 formu ile asıl ekstraksiyon başlasın.

---

## Otomasyon

Pilot sonrası onaylanmış form için Python parser yazacağız:
- `parse_extraction_csv.py` — form doğrulama, eksik alan kontrolü
- `compute_irr.py` — inter-rater reliability (κ, ICC)
- `summarize_extraction.py` — kategorik tablolar + meta-analiz hazırlığı (forest plot için gerekli sütunlar)
