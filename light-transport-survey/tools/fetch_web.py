"""Fetch a handful of implementation / project pages using environment-configured networking and
record whether they are real, with title + a short text digest."""
import json
import re
from pathlib import Path

import requests

from survey_config import ROOT
OUT = ROOT / "meta" / "web"
OUT.mkdir(parents=True, exist_ok=True)
from survey_config import PROXIES
H = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"}

URLS = {
    "rtxdi_readme": "https://raw.githubusercontent.com/NVIDIA-RTX/RTXDI/main/README.md",
    "rtxdi_restirpt_doc": "https://raw.githubusercontent.com/NVIDIA-RTX/RTXDI/main/Doc/RestirPT.md",
    "eg_neural_render_proxies": "https://diglib.eg.org/items/55363661-e76b-4d9d-8bc0-d8835ccec2e7",
    "nvidia_restirpt_enhanced": "https://research.nvidia.com/labs/rtr/publication/lin2026restirptenhanced/",
    "renderformer_v2_site": "https://renderformer.github.io/v2/",
    "renderformer_site": "https://microsoft.github.io/renderformer/",
    "mitsuba_caustics": "https://mitsuba.readthedocs.io/en/latest/src/inverse_rendering/caustics_optimization.html",
    "renderformer_msr_pdf": "https://www.microsoft.com/en-us/research/wp-content/uploads/2025/08/rt.pdf",
}

rows = []
for name, url in URLS.items():
    rec = {"name": name, "url": url}
    try:
        r = requests.get(url, proxies=PROXIES, headers=H, timeout=60, allow_redirects=True)
        rec["status"] = r.status_code
        rec["content_type"] = r.headers.get("content-type", "")
        rec["bytes"] = len(r.content)
        if "pdf" in rec["content_type"]:
            (OUT / f"{name}.pdf").write_bytes(r.content)
            rec["note"] = "pdf saved"
        else:
            txt = r.text
            title = re.search(r"<title[^>]*>(.*?)</title>", txt, re.S | re.I)
            rec["title"] = " ".join(title.group(1).split())[:160] if title else ""
            body = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", txt)
            body = re.sub(r"(?s)<[^>]+>", " ", body)
            body = re.sub(r"\s+", " ", body).strip()
            rec["digest"] = body[:1200]
            (OUT / f"{name}.txt").write_text(body, encoding="utf-8")
    except Exception as e:  # noqa: BLE001
        rec["status"] = "ERR"
        rec["note"] = f"{type(e).__name__}: {e}"
    rows.append(rec)
    print(f"{name:30s} {str(rec.get('status')):5s} {rec.get('title', rec.get('note',''))[:70]}",
          flush=True)

(ROOT / "meta" / "web_probe.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
