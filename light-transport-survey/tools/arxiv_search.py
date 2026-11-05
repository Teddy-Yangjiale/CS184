"""Query arXiv API using environment-configured networking and dump candidates for curation."""
import json
import sys
import time
import urllib.parse

import requests
import xml.etree.ElementTree as ET

from survey_config import ROOT, PROXIES
NS = {"a": "http://www.w3.org/2005/Atom"}

QUERIES = [
    ("nrc", 'ti:"neural radiance caching"'),
    ("restir", 'abs:"ReSTIR"'),
    ("renderformer", 'ti:"RenderFormer"'),
    ("nrp", 'abs:"neural render proxy" OR abs:"neural render proxies"'),
    ("caustics", 'ti:"caustics" OR ti:"caustic"'),
    ("wave-optics", 'abs:"wave optics" AND abs:"rendering"'),
    ("sobolev", 'ti:"Sobolev training"'),
    ("relight-neural", 'abs:"neural" AND abs:"relighting" AND abs:"light transport"'),
    ("diff-render-caustic", 'abs:"differentiable rendering" AND abs:"caustics"'),
    ("neural-light-cache", 'abs:"neural" AND abs:"path tracing" AND abs:"cache"'),
    ("dynamic-light", 'abs:"dynamic lighting" AND abs:"neural rendering"'),
    ("tog-2025", 'abs:"global illumination" AND abs:"neural" AND cat:cs.GR'),
]


def search(q, n=12):
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": q, "start": 0, "max_results": n, "sortBy": "relevance"}
    )
    for attempt in range(3):
        try:
            r = requests.get(url, proxies=PROXIES, timeout=40,
                             headers={"User-Agent": "survey-bot/0.1"})
            if r.status_code == 200:
                return r.text
        except Exception as e:  # noqa: BLE001
            print(f"  retry {attempt}: {e}", file=sys.stderr)
        time.sleep(3)
    return ""


def parse(xml_text):
    out = []
    if not xml_text.strip():
        return out
    root = ET.fromstring(xml_text)
    for entry in root.findall("a:entry", NS):
        eid = entry.findtext("a:id", default="", namespaces=NS)
        title = " ".join(entry.findtext("a:title", default="", namespaces=NS).split())
        pub = entry.findtext("a:published", default="", namespaces=NS)[:10]
        summ = " ".join(entry.findtext("a:summary", default="", namespaces=NS).split())
        out.append({"id": eid.rsplit("/", 1)[-1], "title": title, "published": pub,
                    "abstract": summ})
    return out


def main():
    result = {}
    for tag, q in QUERIES:
        print(f"[query] {tag}: {q}", file=sys.stderr)
        items = parse(search(q))
        result[tag] = items
        for it in items:
            print(f"{tag:20s} {it['published']}  {it['id']:14s} {it['title'][:95]}",
                  file=sys.stderr)
        time.sleep(3.2)
    with open(ROOT / "meta" / "arxiv_candidates.json", "w",
              encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print("saved", sum(len(v) for v in result.values()), "entries", file=sys.stderr)


if __name__ == "__main__":
    main()
