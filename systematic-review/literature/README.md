# Literature Library — QS in *A. baumannii*

Bu klasör, sistematik review için PubMed taramasından elde edilen 340 makalenin meta verisi ve erişilebilen tam metinlerini içerir.

## Tarama Özeti

| Metrik | Değer |
|---|---|
| **Tarama tarihi** | 2026-05-17 |
| **Veri tabanı** | PubMed/MEDLINE |
| **Tarih filtresi** | 2003-01-01 — 2025-12-31 |
| **Dil filtresi** | İngilizce |
| **Sonuç sayısı (ham)** | 363 |
| **Filtre sonrası** | **340** |
| **Abstract mevcut** | 336 |
| **DOI'li** | 336 |
| **PMC kaydı olan** | 218 |
| **PMC üzerinden TAM metin (XML body)** | **185** |
| **PMC abstract-only (XML var, body yok)** | 30 |
| **OpenAlex/Repository üzerinden PDF kurtarıldı** | **10** |
| **Toplam erişilebilir tam metin** | **195 (% 57)** |
| **Manuel indirme gerekir (EKUAL ile)** | **145** |

## Klasör Yapısı

```
literature/
├── README.md                        ← bu dosya
├── master_catalog.csv               ← 340 makalenin master kataloğu
├── fulltext_inventory.csv           ← İndirilen tam metinlerin envantarı
├── download_log.csv                 ← İndirme log'u
├── abstracts-only/                  ← 340 dosya — her makale için abstract + bibliyografi
│   └── {Yazar}_{Yıl}.txt
├── full-text/                       ← 233 dosya XML + 233 TXT
│   ├── {Yazar}_{Yıl}.xml            ← Ham JATS XML
│   └── {Yazar}_{Yıl}.txt            ← Okunabilir düz metin
└── metadata/
    ├── esearch.json                 ← PubMed arama yanıtı
    ├── efetch_batch1.xml            ← Ham metadata (1-200)
    ├── efetch_batch2.xml            ← Ham metadata (201-340)
    ├── parse_metadata.py            ← XML → CSV parser
    ├── download_fulltext.py         ← PMC tam-metin indirici
    └── xml_to_text.py               ← XML → TXT dönüştürücü
```

## Dosya Adlandırma

Format: **`{Yazar(soyad)}_{Yıl}.{uzantı}`**

Aynı yazar/yıl çakışmalarında `_2`, `_3` eki eklenir (örn. `Lpez_2018_2.txt`).

> Soyadlardaki diyakritik işaretler kaldırılır (López → Lpez).

## Manuel İndirme Gerekenler

EKUAL erişiminizle elde etmeniz gereken **toplam 145 makale** var. Detaylı liste: **`NEEDS_MANUAL_DOWNLOAD.csv`**.

- **115 makale:** PMC kaydı yok ve OpenAlex de yasal OA kopya bulamadı (Elsevier, Wiley, ASM, ACS paywall'ı)
- **30 makale:** PMC kaydı var ama tam metin redistributable değil — XML'de sadece abstract var

**Otomatik denenen yollar (başarısız):**
- PMC OA service (idIsNotOpenAccess hatası)
- Unpaywall API (placeholder email reddediliyor)
- Europe PMC (çoğu için inEPMC=N)
- OpenAlex direkt PDF linki (publisher 403 Forbidden)
- Repository landing page scraping (sınırlı başarı)

> **Not:** Publisher PDF erişimleri sandbox IP'sinden 403 dönüyor. Üniversite ağınızdan veya VPN ile aynı linkler açılıyor. Sci-Hub vb. gri-alan yöntemler etik nedenlerle kullanılmadı.

**Pratik yöntem:**
1. `master_catalog.csv`'yi açın
2. `pmcid` boş **VEYA** `fulltext_inventory.csv`'de `has_body=no` olanları filtreleyin
3. `doi` sütunundaki linkten EKUAL üzerinden indirin
4. `full-text/{Yazar_Yıl}.pdf` adıyla aynı klasöre koyun

## Yıllara Göre Dağılım

| Yıl | n |
|---|---|
| 2005 | 1 |
| 2008 | 3 |
| 2009 | 2 |
| 2010 | 2 |
| 2011 | 8 |
| 2012 | 11 |
| 2013 | 13 |
| 2014 | 9 |
| 2015 | 12 |
| 2016 | 16 |
| 2017 | 11 |
| 2018 | 17 |
| 2019 | 21 |
| 2020 | 29 |
| 2021 | 32 |
| 2022 | 41 |
| 2023 | 31 |
| 2024 | 38 |
| 2025 | 43 |

> Alan son 5 yılda hızla büyümüş: makalelerin %50'si 2021 sonrası.

## Sonraki Adımlar

1. **Scopus / WoS / Embase** taraması (henüz yapılmadı — protokolde planlandı)
2. Eksik 194 tam metnin manuel indirilmesi (EKUAL üzerinden)
3. Rayyan/Covidence'a import edilip başlık-özet taramasına başlanması

---

**Tarama scripti versiyonu:** v0.1 (2026-05-17)
