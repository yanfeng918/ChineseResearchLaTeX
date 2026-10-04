"""Read-only reference audit against Crossref DOI registration metadata."""
import concurrent.futures
import datetime
import difflib
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import quote

import requests

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
text = (ROOT / "references/myexample.bib").read_text()
entries = []
for m in re.finditer(r"@(\w+)\{([^,]+),(.*?)\n\}", text, re.S):
    fields = dict(re.findall(r"^\s*(\w+)\s*=\s*\{(.*?)\}\s*,?\s*$", m[3], re.M))
    entries.append({"key": m[2], "type": m[1], "line": text[:m.start()].count("\n") + 1, "fields": fields})

def norm(s):
    return re.sub(r"[^\w]", "", unicodedata.normalize("NFKC", s).casefold())

def check(e):
    doi = e["fields"].get("doi")
    if not doi:
        return {**e, "status": "no_doi", "metadata": None}
    url = "https://api.crossref.org/works/" + quote(doi, safe="")
    try:
        r = requests.get(url, timeout=(6, 15), headers={"User-Agent": "BibliographicAudit/1.0 (read-only)"})
        r.raise_for_status()
        meta = r.json()["message"]
    except Exception as exc:
        return {**e, "status": "uncertain", "source": url, "error": str(exc)}
    f = e["fields"]
    observed = {"title": meta.get("title", [""])[0], "author": meta.get("author", []),
        "container-title": meta.get("container-title", []), "volume": meta.get("volume"),
        "issue": meta.get("issue"), "page": meta.get("page"), "article-number": meta.get("article-number"),
        "published": meta.get("published"), "published-print": meta.get("published-print"),
        "published-online": meta.get("published-online"), "DOI": meta.get("DOI"), "URL": meta.get("URL"),
        "publisher": meta.get("publisher"), "type": meta.get("type")}
    flags = []
    if norm(f["title"]) != norm(observed["title"]):
        flags.append({"field": "title", "local": f["title"], "remote": observed["title"], "similarity": difflib.SequenceMatcher(None,norm(f["title"]),norm(observed["title"])).ratio()})
    for a,b in [("volume", "volume"),("number", "issue"),("pages", "page")]:
        if f.get(a) and observed.get(b) and norm(f[a]) != norm(observed[b]):
            flags.append({"field": a, "local": f[a], "remote": observed[b]})
    years = [str(observed[k]["date-parts"][0][0]) for k in ("published","published-print","published-online") if observed.get(k)]
    if years and f["year"] not in years:
        flags.append({"field": "year", "local": f["year"], "remote": years})
    return {**e, "status": "registered", "source": url, "metadata": observed, "flags": flags}

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
    results = list(pool.map(check, entries))

keys = [e["key"] for e in entries]
cites = []
for file in [ROOT / "main.tex", *(ROOT / "extraTex").glob("*.tex")]:
    content = file.read_text()
    for m in re.finditer(r"\\cite\w*\*?(?:\[[^\]]*\]){0,2}\{([^}]+)\}", content):
        for key in m[1].split(","):
            cites.append({"key": key.strip(), "file": str(file.relative_to(ROOT)), "line": content[:m.start()].count("\n")+1})
summary = {"utc_checked": datetime.datetime.now(datetime.timezone.utc).isoformat(), "entry_count": len(entries),
    "status_counts": {s: sum(r["status"] == s for r in results) for s in {r["status"] for r in results}},
    "citation_occurrences": len(cites), "cited_keys": len({c["key"] for c in cites}),
    "missing_cited_keys": sorted({c["key"] for c in cites} - set(keys)), "uncited_keys": sorted(set(keys)-{c["key"] for c in cites}),
    "duplicate_keys": sorted({k for k in keys if keys.count(k)>1}), "results": results, "citations": cites}
(HERE / "crossref-evidence.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2))
print(json.dumps({k:v for k,v in summary.items() if k not in ("results", "citations")}, ensure_ascii=False, indent=2))
for r in results:
    if r.get("flags") or r["status"] != "registered":
        print(json.dumps({k:v for k,v in r.items() if k not in ("fields","metadata")}, ensure_ascii=False))
