# Arama Stratejileri — QS in *A. baumannii*

> Protokol Adım 7'nin detaylandırılmış versiyonu.
> PRISMA 2020 raporlama için her veri tabanının tam sentaksı belgelenir.

**Hedef:** PubMed dışındaki 3 veri tabanından (Scopus, Web of Science, Embase) ek makale yakalamak ve yayın yanlılığını azaltmak.

**Tarih filtresi (tüm aramalarda):** 2003-01-01 — 2025-12-31
**Dil filtresi:** İngilizce

---

## 1. PubMed (TAMAMLANDI — 2026-05-17)

**Sonuç:** 340 makale → `literature/master_catalog.csv`

```
("Acinetobacter baumannii"[MeSH] OR "Acinetobacter baumannii"[tiab] OR "A. baumannii"[tiab])
AND
("quorum sensing"[tiab] OR "quorum-sensing"[tiab] OR "quorum quenching"[tiab] OR "quorum-quenching"[tiab]
 OR "abaI"[tiab] OR "abaR"[tiab] OR "abaM"[tiab]
 OR "autoinducer"[tiab]
 OR "acyl homoserine lactone"[tiab] OR "acyl-homoserine lactone"[tiab] OR "N-acyl homoserine lactone"[tiab]
 OR "AHL"[tiab]
 OR "3-hydroxy-dodecanoyl-homoserine"[tiab] OR "3-OH-C12-HSL"[tiab]
 OR "LuxI"[tiab] OR "LuxR"[tiab])
AND ("2003/01/01"[PDAT] : "2025/12/31"[PDAT])
AND English[Language]
```

---

## 2. Scopus (Elsevier — EKUAL ✓)

**Erişim:** [www.scopus.com](https://www.scopus.com) → kurum hesabı ile giriş → Advanced Search.

**Tam sözdizim:**

```
( TITLE-ABS-KEY ( "Acinetobacter baumannii" OR "A. baumannii" ) )
AND
( TITLE-ABS-KEY ( "quorum sensing" OR "quorum-sensing" OR "quorum quenching" OR "quorum-quenching"
   OR "abaI" OR "abaR" OR "abaM"
   OR "autoinducer"
   OR "acyl homoserine lactone" OR "N-acyl homoserine lactone" OR "AHL"
   OR "3-OH-C12-HSL" OR "3-hydroxy-dodecanoyl-homoserine"
   OR "LuxI" OR "LuxR" ) )
AND PUBYEAR > 2002 AND PUBYEAR < 2026
AND ( LIMIT-TO ( LANGUAGE , "English" ) )
AND ( LIMIT-TO ( DOCTYPE , "ar" ) OR LIMIT-TO ( DOCTYPE , "re" ) OR LIMIT-TO ( DOCTYPE , "ch" ) )
```

**Dışlanan doctype'lar:** Editorial (ed), Letter (le), Note (no), Conference Paper (cp), Erratum (er).

**Export adımları:**
1. Arama sonuçları sayfasında `All` seç → `Export`
2. Format: **CSV** (veya RIS — EndNote/Zotero için)
3. Alanlar: ALL (`Citation Information`, `Abstract & Keywords`, `Funding details`, `Other Information`)
4. Dosya adı: `scopus_export_YYYYMMDD.csv` → `literature/external/scopus/` klasörüne koyun

> Scopus tek seferde 2000 kayıt export eder. 2000'in altında olacak (tahmin: 400-500).

---

## 3. Web of Science Core Collection (Clarivate — EKUAL ✓)

**Erişim:** [webofscience.com](https://www.webofscience.com) → kurum hesabı → Documents → Advanced Search.

**Tam sözdizim:**

```
TS=("Acinetobacter baumannii" OR "A. baumannii")
AND
TS=("quorum sensing" OR "quorum-sensing" OR "quorum quenching" OR "quorum-quenching"
    OR "abaI" OR "abaR" OR "abaM"
    OR autoinducer
    OR "acyl homoserine lactone" OR "N-acyl homoserine lactone" OR AHL
    OR "3-OH-C12-HSL" OR "3-hydroxy-dodecanoyl-homoserine"
    OR LuxI OR LuxR)
```

**TS** = Topic (title + abstract + author keywords + Keywords Plus).

**Filtre ayarları (sol panel):**
- Publication Years: **2003-2025**
- Document Types: Article, Review Article, Early Access
- Languages: English

**Export adımları:**
1. `All on page` veya `Records 1-1000` seç → `Export` → `Tab delimited file` veya `BibTeX`
2. Record Content: `Full Record` (abstract + keywords + DOI dahil)
3. Dosya: `wos_export_YYYYMMDD.txt` → `literature/external/wos/`

> WoS tek seferde 1000 kayıt; muhtemelen tek export yeterli.

---

## 4. Embase (Elsevier — EKUAL ✓ kurumsal abonelik)

**Erişim:** [www.embase.com](https://www.embase.com) → kurum hesabı → Advanced Search.

**Tam sözdizim (Emtree + free-text):**

```
('Acinetobacter baumannii'/exp OR 'acinetobacter baumannii':ti,ab,kw OR 'a baumannii':ti,ab,kw)
AND
('quorum sensing'/exp OR 'quorum sensing':ti,ab,kw OR 'quorum-sensing':ti,ab,kw
 OR 'quorum quenching':ti,ab,kw OR 'quorum-quenching':ti,ab,kw
 OR 'abaI':ti,ab,kw OR 'abaR':ti,ab,kw OR 'abaM':ti,ab,kw
 OR autoinducer:ti,ab,kw
 OR 'acyl homoserine lactone'/exp OR 'acyl homoserine lactone':ti,ab,kw OR AHL:ti,ab,kw
 OR '3-OH-C12-HSL':ti,ab,kw OR '3-hydroxy-dodecanoyl-homoserine':ti,ab,kw
 OR LuxI:ti,ab,kw OR LuxR:ti,ab,kw)
AND [english]/lim
AND [2003-2025]/py
AND ([article]/lim OR [review]/lim OR [article in press]/lim)
```

**Export adımları:**
1. Results → `Export` → Format: **CSV** veya **RIS**
2. Field Selection: `Full Record`
3. Dosya: `embase_export_YYYYMMDD.csv` → `literature/external/embase/`

> Embase'de Conference Abstract çok bulunur → filtre ile dışlandı. Hâlâ çok çıkarsa: `AND NOT [conference abstract]/lim` ekleyin.

---

## 5. Cochrane Library (Wiley — açık)

QS klinik çalışmalar nadirdir ama PRISMA bekler:

**Erişim:** [cochranelibrary.com](https://www.cochranelibrary.com) → Advanced Search.

```
Title Abstract Keyword: "Acinetobacter baumannii" OR "A. baumannii"
AND
Title Abstract Keyword: "quorum sensing" OR "quorum-sensing" OR "quorum quenching" OR autoinducer
   OR "acyl homoserine lactone" OR AHL OR abaI OR abaR
Publication Year: 2003-2025
```

Sonuçları **CRDS records** olarak indirin (CENTRAL trials).

---

## 6. Ek Kaynaklar (PRISMA önerir)

- **Google Scholar:** İlk 200 sonuç manuel taranır (gri literatür). Arama: `"Acinetobacter baumannii" "quorum sensing" OR "abaI" 2003..2025`
- **PROSPERO:** Devam eden veya tamamlanmış benzer review'ları kontrol — protokol "duplicate" değil
- **ClinicalTrials.gov:** `Acinetobacter baumannii` + `quorum` → faz I-IV var mı?
- **Snowballing:** Dahil edilen tüm makalelerin referans listeleri + onlara atıf yapan makaleler (forward & backward citation tracking)

---

## Birleştirme & Deduplication Akışı

1. Her veritabanından export'u `literature/external/{db}/` altına koyun
2. Aşağıdaki scripti çalıştırın → `merged_unique.csv` üretir
3. `master_catalog.csv` (PubMed) ile birleşik liste
4. DOI, PMID veya başlık+yıl uyumu ile duplikasyon

**Beklenen rakamlar (tahmini):**

| Veritabanı | Tahmini sonuç | Tahmini özgün |
|---|---|---|
| PubMed | 340 ✓ | 340 |
| Scopus | 400-500 | +80-120 |
| Web of Science | 350-450 | +30-60 |
| Embase | 450-550 | +40-80 |
| **Toplam (deduplike)** | | **~450-600** |

---

## Klasör Yapısı (Tamamlandığında)

```
literature/
├── master_catalog.csv             ← PubMed (mevcut)
├── external/
│   ├── scopus/scopus_export_YYYYMMDD.csv
│   ├── wos/wos_export_YYYYMMDD.txt
│   ├── embase/embase_export_YYYYMMDD.csv
│   └── cochrane/cochrane_export_YYYYMMDD.csv
├── merged_unique.csv              ← Sonraki script üretecek
└── prisma_flow_data.json          ← PRISMA akış şeması için sayılar
```
