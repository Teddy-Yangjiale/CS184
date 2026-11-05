"""Probe GitHub for reference implementations of each surveyed paper."""
import json
import time
from pathlib import Path

import requests

from survey_config import ROOT
from survey_config import PROXIES
H = {"User-Agent": "survey-bot/0.1", "Accept": "application/vnd.github+json"}

QUERIES = {
    "nrc-2021": "neural radiance caching",
    "ntmc-2024": "neural two-level monte carlo",
    "specular-prefilter-2026": "prefiltered radiance neural caching",
    "neural-visibility-cache-2025": "neural visibility cache",
    "lt3d-embedding-2025": "light transport embedding",
    "restir-mcmc-2022": "restir mcmc",
    "tof-restir-2026": "tof restir",
    "ddgi-resampling-2021": "ddgi resampling",
    "renderformer-2025": "renderformer",
    "renderformer-v2-2026": "renderformer",
    "renderformer-plus-2026": "renderformer",
    "let-there-be-light-2026": "neural operator light transport",
    "caustic-surface-light-2025": "caustic design",
    "active-caustics-2023": "active caustics",
    "double-freeform-2026": "freeform lens design",
    "plateau-diffpt-2022": "differentiable path tracing plateau",
    "diff-light-tracing-2026": "differentiable light tracing",
    "wave-ray-2023": "wave optics rendering",
    "wave-tracing-2025": "wave tracing path integral",
    "gratnet-2025": "gratnet diffractive",
    "photon-guiding-caustics-2024": "photon guiding caustics",
    "sobolev-2017": "sobolev training",
    "neural-integral-operators-2025": "neural integral operator parametric integration",
    "npm-path-guiding-2025": "neural parametric mixtures path guiding",
    "plasmonic-stiffness-2021": "optical trap stiffness",
    "stiffness-polarization-2015": "optical tweezers stiffness polarization",
}


def search(q: str):
    url = "https://api.github.com/search/repositories"
    params = {"q": q, "sort": "stars", "order": "desc", "per_page": 4}
    try:
        r = requests.get(url, params=params, headers=H, proxies=PROXIES, timeout=40)
        if r.status_code == 403:
            return None, "rate-limited"
        r.raise_for_status()
        items = r.json().get("items", [])
        return [{"full_name": it["full_name"], "stars": it["stargazers_count"],
                 "pushed_at": it["pushed_at"][:10], "desc": (it["description"] or "")[:120],
                 "url": it["html_url"]} for it in items], "ok"
    except Exception as e:  # noqa: BLE001
        return None, f"{type(e).__name__}: {e}"


def main() -> None:
    out = {}
    for slug, q in QUERIES.items():
        repos, status = search(q)
        out[slug] = {"query": q, "status": status, "repos": repos}
        print(f"{slug:32s} {status:12s} " +
              ("" if not repos else f"top={repos[0]['full_name']} ({repos[0]['stars']}*)"), flush=True)
        time.sleep(6.5)
    (ROOT / "meta" / "github_probe.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
