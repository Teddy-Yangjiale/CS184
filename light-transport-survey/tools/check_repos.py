import json
import re

import requests

from survey_config import ROOT, PROXIES as P
H = {"User-Agent": "Mozilla/5.0", "Accept": "application/vnd.github+json"}

REPOS = [
    "microsoft/renderformer",
    "ssteinberg/wave_tracer",
    "mfischer-ucl/prdpt",
    "bing-xu-graphics/light_transformer",
    "dylanmsu/fast_caustic_design",
    "NVIDIA-RTX/RTXDI",
    "mitsuba-renderer/mitsuba3",
]

out = {}
for repo in REPOS:
    try:
        r = requests.get(f"https://api.github.com/repos/{repo}", headers=H, proxies=P, timeout=30)
        if r.status_code != 200:
            out[repo] = {"error": r.status_code}
            continue
        j = r.json()
        c = requests.get(f"https://api.github.com/repos/{repo}/contents/", headers=H,
                         proxies=P, timeout=30)
        names = [x["name"] for x in c.json()][:25] if c.status_code == 200 else []
        rd = requests.get(f"https://raw.githubusercontent.com/{repo}/{j['default_branch']}/README.md",
                          headers={"User-Agent": "Mozilla/5.0"}, proxies=P, timeout=30)
        head = " ".join(rd.text.split())[:600] if rd.status_code == 200 else ""
        out[repo] = {"stars": j["stargazers_count"], "pushed": j["pushed_at"][:10],
                     "created": j["created_at"][:10], "license": (j["license"] or {}).get("spdx_id"),
                     "desc": j["description"], "root": names, "readme": head}
        print(f"{repo:42s} stars={j['stargazers_count']:5d} pushed={j['pushed_at'][:10]} "
              f"root={names[:6]}")
    except Exception as e:  # noqa: BLE001
        out[repo] = {"error": str(e)}
        print(repo, "ERR", e)

try:
    r2 = requests.get("https://renderformer.github.io/v2/", headers={"User-Agent": "Mozilla/5.0"},
                      proxies=P, timeout=30)
    links = sorted(set(re.findall(r'href="(https?://[^"]+)"', r2.text)))
    out["_v2_links"] = [l for l in links if "github" in l or "hugging" in l or "arxiv" in l]
    print("v2 links:", out["_v2_links"])
except Exception as e:  # noqa: BLE001
    print("v2 page ERR", e)

with open(ROOT / "meta" / "repo_status.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
