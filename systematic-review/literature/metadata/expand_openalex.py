#!/usr/bin/env python3
"""
Expand literature coverage via the OpenAlex API.

Query (equivalent):
  "Acinetobacter baumannii" AND ("quorum sensing" OR "abaI" OR "abaR" OR "autoinducer" OR "AHL")

Filters: publication_year 2003-2025, type=article|review, language=en
Pagination: cursor-based
Output: /home/user/akademik/systematic-review/literature/external/openalex/openalex_export.csv

Polite usage: User-Agent with mailto, ~0.2s between page calls.
Intermediate checkpoint every 200 records.
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
OUT_DIR = ROOT / "external" / "openalex"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_CSV = OUT_DIR / "openalex_export.csv"
CHECKPOINT = OUT_DIR / "openalex_checkpoint.json"

MAILTO = "review.acinetobacter.qs@example.org"
UA = f"AcinetobacterQS-SystematicReview/1.0 (mailto:{MAILTO})"

# OpenAlex's free-text `search` uses relevance ranking that ignores explicit AND/OR.
# We emulate the boolean by issuing one sub-query per QS-related term combined with
# the species, using the `title_and_abstract.search` filter (stricter than `search`).
# Each sub-query yields ~tens to ~hundreds of records; we de-duplicate by OpenAlex ID.
SUBQUERIES = [
    "Acinetobacter baumannii quorum sensing",
    "Acinetobacter baumannii abaI",
    "Acinetobacter baumannii abaR",
    "Acinetobacter baumannii autoinducer",
    "Acinetobacter baumannii AHL",
    "Acinetobacter baumannii acyl homoserine lactone",
]

# Filters (always applied):
BASE_FILTER = ",".join([
    "from_publication_date:2003-01-01",
    "to_publication_date:2025-12-31",
    "type:article|review",
    "language:en",
])

BASE = "https://api.openalex.org/works"
PER_PAGE = 100
SLEEP = 0.5


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


def reconstruct_abstract(inverted_index):
    """Reconstruct an abstract string from OpenAlex's word->positions index."""
    if not inverted_index:
        return ""
    try:
        positions = []
        for word, idxs in inverted_index.items():
            for i in idxs:
                positions.append((i, word))
        positions.sort(key=lambda x: x[0])
        return " ".join(w for _, w in positions)
    except Exception:
        return ""


def first_author(authorships):
    if not authorships:
        return ""
    a0 = authorships[0]
    if isinstance(a0, dict):
        au = a0.get("author") or {}
        return au.get("display_name", "") or ""
    return ""


def normalize_doi(doi):
    if not doi:
        return ""
    s = str(doi).strip()
    for prefix in ("https://doi.org/", "http://doi.org/", "https://dx.doi.org/", "http://dx.doi.org/"):
        if s.lower().startswith(prefix):
            s = s[len(prefix):]
            break
    return s


def host_venue_name(rec):
    """OpenAlex moved 'host_venue' to 'primary_location.source' in newer responses; support both."""
    hv = rec.get("host_venue") or {}
    name = hv.get("display_name") or ""
    if name:
        return name
    pl = rec.get("primary_location") or {}
    src = pl.get("source") or {}
    return src.get("display_name", "") or ""


def concept_tag_list(rec):
    cs = rec.get("concepts") or []
    out = []
    for c in cs[:8]:
        n = c.get("display_name")
        if n:
            out.append(n)
    return "; ".join(out)


def extract(rec):
    return {
        "DOI": normalize_doi(rec.get("doi", "")),
        "Title": rec.get("title", "") or rec.get("display_name", "") or "",
        "Year": str(rec.get("publication_year", "") or ""),
        "Source title": host_venue_name(rec),
        "Authors": first_author(rec.get("authorships") or []),
        "Abstract": reconstruct_abstract(rec.get("abstract_inverted_index")),
        "Concepts": concept_tag_list(rec),
        "CitedByCount": str(rec.get("cited_by_count", "") or ""),
        "Type": rec.get("type", "") or "",
        "OpenAlexID": rec.get("id", "") or "",
        "EID": "",  # placeholder for Scopus column compatibility
    }


FIELDNAMES = ["DOI", "Title", "Year", "Source title", "Authors", "Abstract",
              "Concepts", "CitedByCount", "Type", "OpenAlexID", "EID"]


def save_records(records, path):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDNAMES)
        w.writeheader()
        for r in records:
            w.writerow(r)


def main():
    print(f"OpenAlex base filter: {BASE_FILTER}")
    print(f"Out: {OUT_CSV}")

    records_by_id = {}  # de-dup by OpenAlex ID

    for q in SUBQUERIES:
        print(f"\n=== Sub-query: title_and_abstract.search:{q} ===")
        cursor = "*"
        page = 0
        before = len(records_by_id)
        sub_total = None

        while cursor:
            page += 1
            f_str = f"title_and_abstract.search:{q},{BASE_FILTER}"
            params = {
                "filter": f_str,
                "per-page": str(PER_PAGE),
                "cursor": cursor,
                "mailto": MAILTO,
            }
            data = None
            for attempt in range(5):
                try:
                    data = http_get_json(BASE, params)
                    break
                except Exception as e:
                    wait = 2 ** attempt
                    print(f"  [page {page}] attempt {attempt+1} ERROR: {e}. Retry in {wait}s")
                    time.sleep(wait)
            if data is None:
                print(f"  [page {page}] All retries failed. Skipping subquery.")
                break

            meta = data.get("meta") or {}
            if sub_total is None:
                sub_total = meta.get("count")
                print(f"  Sub-query total: {sub_total}")

            results = data.get("results") or []
            new = 0
            for rec in results:
                rid = rec.get("id") or rec.get("doi") or ""
                if not rid:
                    continue
                if rid in records_by_id:
                    continue
                records_by_id[rid] = extract(rec)
                new += 1

            next_cursor = meta.get("next_cursor")
            print(f"  page {page}: fetched={len(results)} new={new} cumulative_unique={len(records_by_id)}")

            # Checkpoint every ~200 new records
            if (len(records_by_id) // 200) != ((len(records_by_id) - new) // 200):
                save_records(list(records_by_id.values()), OUT_CSV)
                with open(CHECKPOINT, "w") as f:
                    json.dump({"query": q, "page": page, "count": len(records_by_id)}, f)

            if not results:
                break
            if not next_cursor or next_cursor == cursor:
                break
            cursor = next_cursor
            time.sleep(SLEEP)

        gained = len(records_by_id) - before
        print(f"  Sub-query gained {gained} new unique records.")

    save_records(list(records_by_id.values()), OUT_CSV)
    print(f"\nDone. {len(records_by_id)} unique records saved to {OUT_CSV}")


if __name__ == "__main__":
    main()
