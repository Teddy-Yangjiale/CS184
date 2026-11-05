"""Second, more targeted arXiv pass."""
import json, sys, time, urllib.parse
import requests
import xml.etree.ElementTree as ET

from survey_config import ROOT, PROXIES
NS = {"a": "http://www.w3.org/2005/Atom"}

QUERIES = [
    ("restir-ti", 'ti:"ReSTIR"'),
    ("mitsuba", 'ti:"Mitsuba"'),
    ("wave-tracing", 'abs:"wave tracing" OR ti:"wave tracing"'),
    ("cloth-wave", 'abs:"cloth" AND (abs:"wave" OR abs:"diffraction") AND cat:cs.GR'),
    ("nrp", 'abs:"render proxy"'),
    ("robust-optics", '(abs:"robust" OR abs:"tolerance") AND abs:"freeform" AND abs:"optics"'),
    ("tweezers", 'abs:"optical tweezers" AND abs:"stiffness"'),
    ("reparam", 'abs:"reparameterization" AND abs:"differentiable rendering"'),
    ("path-guiding", 'ti:"path guiding"'),
    ("lt-operator", 'abs:"light transport" AND abs:"operator" AND abs:"neural"'),
    ("svbrdf-relight", 'abs:"SVBRDF" AND abs:"relighting"'),
    ("caustic-design", 'abs:"caustic design" OR abs:"inverse caustics"'),
]


def search(q, n=10):
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": q, "start": 0, "max_results": n, "sortBy": "relevance"})
    for attempt in range(3):
        try:
            r = requests.get(url, proxies=PROXIES, timeout=45,
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
        out.append({
            "id": eid.rsplit("/", 1)[-1],
            "title": " ".join(entry.findtext("a:title", default="", namespaces=NS).split()),
            "published": entry.findtext("a:published", default="", namespaces=NS)[:10],
            "abstract": " ".join(entry.findtext("a:summary", default="", namespaces=NS).split()),
        })
    return out


def main():
    result = {}
    for tag, q in QUERIES:
        print(f"[query] {tag}", file=sys.stderr)
        items = parse(search(q))
        result[tag] = items
        for it in items:
            print(f"{tag:16s} {it['published']}  {it['id']:14s} {it['title'][:90]}",
                  file=sys.stderr)
        time.sleep(3.2)
    with open(ROOT / "meta" / "arxiv_candidates2.json", "w",
              encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
