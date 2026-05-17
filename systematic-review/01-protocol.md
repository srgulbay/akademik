# Sistematik Review Protokolü (PRISMA-P 2015 / PRISMA 2020 uyumlu)

> **Çalışma başlığı (taslak):**
> *Quorum Sensing in Acinetobacter baumannii: Mechanistic Role in Biofilm, Virulence, Antimicrobial Resistance and Therapeutic Implications of Quorum Quenching — A Systematic Review*
>
> **Hedef dergi:** International Journal of Antimicrobial Agents (Elsevier)
> **Protokol durumu:** Taslak v0.2 — PROSPERO kaydı bekleniyor
>
> **Onaylı kararlar (v0.2 / 2026-05-17):**
> - Tarih aralığı: 2003–2025
> - Tür kapsamı: Yalnız *A. baumannii* (kompleks değil)
> - Tarayıcı: 2 bağımsız + 3. hakem
> - İlk PubMed taraması yapıldı: **340 makale** (bkz. `literature/README.md`)

---

## 1. Gerekçe (Rationale)

*Acinetobacter baumannii*, DSÖ "kritik öncelikli" patojen listesinin başında yer alan, çoklu ilaca dirençli (MDR) ve nozokomiyal enfeksiyonların önde gelen nedenlerinden bir Gram-negatif basildir. AbaI (LuxI homologu) — AbaR (LuxR homologu) tabanlı quorum sensing (QS) sistemi; biyofilm matürasyonu, motilite, virülans faktör ekspresyonu, ve antibiyotik direnç mekanizmaları (efluks pompaları, OmpA, sürme hareketi) ile ilişkilendirilmiştir. Son on yılda quorum quenching (QQ) ajanları (laktonazlar, asilaz, AHL analogları, doğal bileşikler) anti-virülans terapi olarak yoğun ilgi görmektedir. Ancak kanıtlar dağınık; sistematik bir sentez bulunmamaktadır.

## 2. Amaç (Objectives)

**Birincil amaç:** *A. baumannii*'de QS sistemlerinin biyofilm, virülans ve direnç fenotipleri üzerindeki nedensel rolünü değerlendirmek.

**İkincil amaçlar:**
1. AHL profili ve QS gen ekspresyonunun klinik izolatlarda dağılımı
2. QQ ajanlarının (doğal/sentetik) in vitro ve in vivo etkinliği
3. QQ + antibiyotik kombinasyonlarının sinerjistik potansiyeli
4. Konak yanıtı (sitokin, sağkalım) üzerine QQ etkisi

## 3. Araştırma Sorusu (PICOS)

| Bileşen | Tanım |
|---|---|
| **P** Population | *A. baumannii* (klinik izolat, çevresel izolat, referans suş — ATCC 17978, 19606, AB5075, LAC-4; tüm in vitro/in vivo modeller) |
| **I** Intervention/Exposure | QS aktif (yabanıl tip) durumu; QQ ajan uygulaması; QS gen mutasyonu/delesyonu |
| **C** Comparator | QS-mutant (ΔabaI, ΔabaR); QQ uygulanmayan kontrol; antibiyotik tek başına |
| **O** Outcomes | **Birincil:** Biyofilm kütlesi/yapısı (CV, CLSM, BioFlux), MIC/MBEC değişimi. **İkincil:** Motilite (sürme/yüzme), virülans gen/protein ekspresyonu (qPCR, proteomik), konak sağkalımı (Galleria/fare), sitokin profili, AHL kantitasyonu |
| **S** Study design | In vitro, in vivo hayvan, klinik izolat fenotipleme, ex vivo, omik çalışmalar |

## 4. Dahil Etme Kriterleri

- Tür: *Acinetobacter baumannii* (kompleks dahil — *A. nosocomialis*, *A. pittii* yorum amaçlı tartışılabilir ancak ana analize dahil edilmez)
- Çalışma tipi: Orijinal araştırma makaleleri (in vitro, in vivo, klinik izolat)
- Müdahale: QS sistemi, AHL, QQ ajanı, QS-related gen
- Sonuç: En az bir nicel sonuç (biyofilm, virülans, MIC, sağkalım, gen ekspresyonu)
- Dil: İngilizce
- Yayın tipi: Hakemli tam metin makaleler
- Tarih aralığı: 1 Ocak 2003 – 31 Aralık 2025 (AbaI ilk tanımlandığı yıl: 2003, Niu vd.)

## 5. Dışlama Kriterleri

- Konferans özetleri, tezler, ön yayın olmayan preprintler, editöre mektup, görüş yazıları
- *Acinetobacter* genus düzeyinde olup *A. baumannii*'yi spesifik raporlamayan çalışmalar
- Sadece in silico (deneysel doğrulama olmayan) çalışmalar (ayrı bir tabloda özetlenecek)
- Tam metni erişilemeyen makaleler (3 farklı yoldan denendikten sonra)
- Diğer türlerin verisi *A. baumannii* verisinden ayrıştırılamayan çalışmalar

## 6. Bilgi Kaynakları (Information Sources)

| Veri tabanı | Sağlayıcı | Erişim |
|---|---|---|
| **PubMed/MEDLINE** | NLM | Açık |
| **Scopus** | Elsevier | EKUAL |
| **Web of Science Core Collection** | Clarivate | EKUAL |
| **Embase** | Elsevier | EKUAL (kurumsal) |
| **Cochrane Library** | Wiley | Açık |
| **ScienceDirect** | Elsevier | EKUAL |

**Ek arama:**
- Google Scholar (ilk 200 sonuç — gri literatür için)
- Dahil edilen makalelerin referans listeleri (snowballing)
- ClinicalTrials.gov (klinik çalışma kaydı)
- PROSPERO (önceki/eşzamanlı review kontrolü)

## 7. Arama Stratejisi (Taslak — PubMed örnek)

```
("Acinetobacter baumannii"[MeSH] OR "Acinetobacter baumannii"[tiab] OR "A. baumannii"[tiab])
AND
("Quorum Sensing"[MeSH] OR "quorum sensing"[tiab] OR "quorum-sensing"[tiab]
 OR "quorum quenching"[tiab] OR "autoinducer"[tiab]
 OR "AHL"[tiab] OR "acyl homoserine lactone"[tiab] OR "N-acyl homoserine lactone"[tiab]
 OR "abaI"[tiab] OR "abaR"[tiab] OR "abaM"[tiab]
 OR "3-OH-C12-HSL"[tiab] OR "3-hydroxy-dodecanoyl-homoserine"[tiab]
 OR "LuxI"[tiab] OR "LuxR"[tiab]
 OR "biofilm"[tiab] AND "signaling"[tiab])
```

> Her veri tabanı için sentaks adapte edilecek (Emtree, Scopus syntax, vb.).
> Filtre: Tarih 2003–2025, dil İngilizce. **Tür/yayın filtresi uygulanmayacak** — manuel taranacak.

## 8. Çalışma Seçimi

- **Tarayıcı:** Rayyan veya Covidence
- İki bağımsız değerlendirici (R1, R2) başlık-özet tarayacak
- Uyuşmazlıklar tartışma; çözülmezse 3. değerlendirici (R3) karar verir
- Tam metin değerlendirmesi aynı yöntemle
- Kappa katsayısı raporlanacak (hedef κ ≥ 0.7)
- PRISMA 2020 akış şeması hazırlanacak

## 9. Veri Çıkarımı

Standart form (Excel/REDCap) ile aşağıdaki alanlar:

- Bibliyografik: Yazar, yıl, ülke, dergi
- Suş: Tür, kaynak, referans suş kodu, MDR/XDR durumu
- Yöntem: In vitro/in vivo/klinik, model, deney koşulları
- Müdahale: QS modülasyonu tipi (genetik, kimyasal), ajan adı, dozaj, süre
- Karşılaştırıcı: Kontrol tanımı
- Sonuçlar: Birincil ve ikincil outcome ölçümleri, etki büyüklüğü, p değeri
- Yan veri: AHL tipi, kantitasyon yöntemi, biyofilm yöntemi

## 10. Risk of Bias (Yanlılık Riski) Değerlendirmesi

| Çalışma tipi | Araç |
|---|---|
| In vitro | **QUIN tool** veya modifiye SYRCLE (in vitro modülü) |
| Hayvan in vivo | **SYRCLE RoB** |
| Klinik izolat fenotipleme | **JBI Critical Appraisal — Analytical Cross-sectional** |
| Klinik (insan) | **ROBINS-I** veya **RoB 2** (RCT varsa) |

İki bağımsız değerlendirici; her domain düşük/orta/yüksek/belirsiz olarak puanlanır.

## 11. Veri Sentezi

- **Narratif sentez** ana yöntem (heterojenlik beklendiği için)
- Tematik kategoriler:
  1. QS sistem biyolojisi (AbaI/AbaR yapısı, AHL profili, regülasyon)
  2. QS ve biyofilm
  3. QS ve virülans
  4. QS ve antibiyotik direnci
  5. QQ stratejileri ve terapötik potansiyel
- Meta-analiz: Sadece ≥3 homojen çalışma varsa (örn. biyofilm kütle değişimi standardize ortalama farkı)
- Heterojenlik: I² istatistiği
- Yayın yanlılığı: Funnel plot + Egger testi (≥10 çalışma varsa)
- **GRADE** kanıt kalitesi değerlendirmesi (her ana outcome için)

## 12. Etik ve Şeffaflık

- İkincil veri analizi — etik kurul onayı gerekmez
- Protokol PROSPERO'ya kaydedilecek (CRD numarası alındıktan sonra burada güncellenecek)
- Tüm veri çıkarım formları açık erişimle paylaşılacak (Zenodo/OSF)
- PRISMA 2020 checklist supplementary olarak verilecek

## 13. Zaman Çizelgesi (Tahmini)

| Aşama | Süre |
|---|---|
| Protokol + PROSPERO kaydı | 2 hafta |
| Veri tabanı taraması + tarayıcı kurulumu | 1 hafta |
| Başlık-özet tarama | 3-4 hafta |
| Tam metin tarama | 2-3 hafta |
| Veri çıkarımı + RoB | 4-6 hafta |
| Sentez + yazım | 6-8 hafta |
| İç gözden geçirme + revizyon | 2-3 hafta |
| **Toplam** | **~5-6 ay** |

## 14. Yazar Katkıları ve Çıkar Çatışması

- Yazarlar: [eklenecek]
- ICMJE kriterleri uygulanacak
- Çıkar çatışması beyanı her yazardan toplanacak
- Finansman: [belirtilecek]

---

**Versiyon notu:**
- v0.1 — İlk taslak ([tarih eklenecek])
