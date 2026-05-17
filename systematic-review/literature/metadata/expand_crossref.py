#!/usr/bin/env python3
"""
Expand literature coverage via the Crossref API.

Conceptual query: "Acinetobacter baumannii" AND ("quorum sensing" OR abaI OR abaR OR autoinducer OR AHL)
Crossref's `query` is a simple full-text relevance search; we issue several
sub-queries and merge by DOI to approximate the boolean.

Filter: from-pub-date:2003, until-pub-date:2025-12-31, type=journal-article
Pagination: cursor (rows=100)
Polite pool: mailto in User-Agent + ?mailto=
Output: /home/user/akademik/systematic-review/literature/external/crossref/crossref_export.csv
"""
import csv
import json
import sys
import time
from pathlib import Path

try:
    import requests
    HAVE_REQUESTS = True
except ImportError:
    HAVE_REQUESTS = False
    import urllib.request
    import urllib.parse

HERE = Path(__file__).parent
ROOT = HERE.parent
OUT_DIR = ROOT / "external" / "crossref"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_CSV = OUT_DIR / "crossref_export.csv"
CHECKPOINT = OUT_DIR / "crossref_checkpoint.json"

MAILTO = "review.acinetobacter.qs@example.org"
UA = f"AcinetobacterQS-SystematicReview/1.0 (mailto:{MAILTO})"

BASE = "https://api.crossref.org/works"
ROWS = 100
SLEEP = 0.2

# Sub-queries: each is "Acinetobacter baumannii" PLUS a quorum-sensing-related term.
# Crossref `query` is relevance-ranked free text, so AND must be emulated by combining terms.
SUBQUERIES = [
    'Acinetobacter baumannii quorum sensing',
    'Acinetobacter baumannii abaI',
    'Acinetobacter baumannii abaR',
    'Acinetobacter baumannii autoinducer',
    'Acinetobacter baumannii AHL acyl homoserine lactone',
]

FILTER = "from-pub-date:2003,until-pub-date:2025-12-31,type:journal-article"


def http_get_json(url, params):
    if HAVE_REQUESTS:
        r = requests.get(url, params=params,
                         headers={"User-Agent": UA, "Accept": "application/json"},
                         timeout=60)
        r.raise_for_status()
        return r.json()
    qs = urllib.parse.urlencode(params)
    full = f"{url}?{qs}"
    req = urllib.request.Request(full, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def normalize_doi(doi):
    if not doi:
        return ""
    s = str(doi).strip()
    for prefix in ("https://doi.org/", "http://doi.org/", "https://dx.doi.org/", "http://dx.doi.org/"):
        if s.lower().startswith(prefix):
            s = s[len(prefix):]
            break
    return s.lower()


def first_author(authors):
    if not authors:
        return ""
    a = authors[0]
    given = a.get("given", "")
    family = a.get("family", "")
    if family and given:
        return f"{family}, {given}"
    return family or given or a.get("name", "")


def year_from(rec):
    for key in ("published-print", "published-online", "issued", "created"):
        v = rec.get(key) or {}
        parts = v.get("date-parts") or []
        if parts and parts[0]:
            return str(parts[0][0])
    return ""


def extract(rec):
    title_list = rec.get("title") or []
    title = title_list[0] if title_list else ""
    container = rec.get("container-title") or []
    journal = container[0] if container else ""
    return {
        "DOI": normalize_doi(rec.get("DOI", "")),
        "Title": title,
        "Year": year_from(rec),
        "Source title": journal,
        "Authors": first_author(rec.get("author") or []),
        "Type": rec.get("type", "") or "",
        "Abstract": rec.get("abstract", "") or "",
    }


FIELDNAMES = ["DOI", "Title", "Year", "Source title", "Authors", "Type", "Abstract"]


ACINETO_TERMS = ("acinetobacter", "baumannii")


def is_relevant(rec):
    """Soft relevance filter: keep records whose title or abstract mentions
    Acinetobacter/baumannii. Crossref's keyword search returns many off-topic
    records because it OR-joins query terms across all fields; this is the
    cheapest way to prune the long tail while keeping all plausibly on-topic
    work. Final topic relevance is decided at the screening stage."""
    blob = ((rec.get("Title") or "") + " " + (rec.get("Abstract") or "")).lower()
    if not blob.strip():
        return False
    return any(t in blob for t in ACINETO_TERMS)


def save_records(records_by_doi, path):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDNAMES)
        w.writeheader()
        for r in records_by_doi.values():
            if is_relevant(r):
                w.writerow(r)


def main():
    print(f"Crossref filter: {FILTER}")
    print(f"Out: {OUT_CSV}")

    records_by_doi = {}
    select_fields = "DOI,title,container-title,author,issued,published-print,published-online,created,type,abstract"

    for q in SUBQUERIES:
        print(f"\n=== Sub-query: {q} ===")
        cursor = "*"
        page = 0
        before = len(records_by_doi)

        while cursor:
            page += 1
            params = {
                "query": q,
                "filter": FILTER,
                "rows": str(ROWS),
                "cursor": cursor,
                "select": select_fields,
                "mailto": MAILTO,
            }
            try:
                data = http_get_json(BASE, params)
            except Exception as e:
                print(f"  [page {page}] ERROR: {e}")
                time.sleep(2.0)
                try:
                    data = http_get_json(BASE, params)
                except Exception as e2:
                    print(f"  [page {page}] RETRY FAILED: {e2}. Skipping subquery.")
                    break

            msg = data.get("message") or {}
            items = msg.get("items") or []
            total = msg.get("total-results")
            new = 0
            for rec in items:
                doi = normalize_doi(rec.get("DOI", ""))
                if not doi:
                    continue
                if doi in records_by_doi:
                    continue
                records_by_doi[doi] = extract(rec)
                new += 1

            next_cursor = msg.get("next-cursor")
            print(f"  page {page}: items={len(items)} new={new} total_for_q={total} cumulative_unique={len(records_by_doi)}")

            # Checkpoint every ~200 added
            if (len(records_by_doi) // 200) != ((len(records_by_doi) - new) // 200):
                save_records(records_by_doi, OUT_CSV)
                with open(CHECKPOINT, "w") as f:
                    json.dump({"query": q, "page": page, "count": len(records_by_doi)}, f)

            if not items:
                break
            # Stop on last page (Crossref returns the same cursor across calls in a scroll;
            # only the items array shrinks to <ROWS when the scroll is exhausted).
            if len(items) < ROWS:
                break
            if not next_cursor:
                break
            cursor = next_cursor
            # Polite cap: don't drift too deep into irrelevant tail; subqueries are noisy
            # and relevance ranking puts on-topic results first. 30 pages * 100 = 3000.
            if page >= 30:
                print(f"  Page cap reached for sub-query; stopping.")
                break
            time.sleep(SLEEP)

        gained = len(records_by_doi) - before
        print(f"  Sub-query gained {gained} new unique DOIs.")

    save_records(records_by_doi, OUT_CSV)
    print(f"\nDone. {len(records_by_doi)} unique DOIs saved to {OUT_CSV}")


if __name__ == "__main__":
    main()
