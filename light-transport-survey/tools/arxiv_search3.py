import time
import urllib.parse
import xml.etree.ElementTree as ET

import requests

from survey_config import ROOT, PROXIES as P
NS = {"a": "http://www.w3.org/2005/Atom"}

QS = {
    "cloth-diff": 'abs:"cloth" AND abs:"diffraction"',
    "cloth-wave": 'abs:"fiber" AND abs:"wave optics"',
    "reservoir-pt": 'abs:"reservoir" AND abs:"path tracing"',
    "nrp2": 'abs:"render proxies"',
    "caustic-gr": 'abs:"caustic" AND cat:cs.GR',
    "neural-btf": 'abs:"neural" AND abs:"BTF"',
    "dynamic-relight": 'abs:"relighting" AND abs:"dynamic" AND cat:cs.GR',
}

for k, q in QS.items():
    u = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": q, "max_results": 8, "sortBy": "relevance"})
    try:
        r = requests.get(u, proxies=P, timeout=45, headers={"User-Agent": "survey/0.1"})
        root = ET.fromstring(r.text)
        print("###", k, len(root.findall("a:entry", NS)))
        for e in root.findall("a:entry", NS):
            print("  ", e.findtext("a:published", default="", namespaces=NS)[:10],
                  e.findtext("a:id", default="", namespaces=NS).rsplit("/", 1)[-1],
                  " ".join(e.findtext("a:title", default="", namespaces=NS).split())[:88])
    except Exception as ex:  # noqa: BLE001
        print("###", k, "ERR", ex)
    time.sleep(3.2)
