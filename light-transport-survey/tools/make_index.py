"""Build SOURCES.md from the manifest + extraction stats."""
import json
from pathlib import Path

from survey_config import ROOT
spec = json.loads((ROOT / "meta" / "papers.json").read_text(encoding="utf-8"))


def page_stats(slug: str) -> dict:
    p = ROOT / "text" / f"{slug}.txt"
    if not p.exists():
        return {"pages": 0, "chars": 0}
    body = p.read_text(encoding="utf-8")
    return {"pages": body.count("=====") // 2, "chars": len(body)}


stats = {p["slug"]: page_stats(p["slug"]) for p in spec["papers"]}

clusters = spec["clusters"]
rows_by_cluster = {}
for p in spec["papers"]:
    rows_by_cluster.setdefault(p["cluster"], []).append(p)

lines = ["# 文献索引（light-transport-survey）", "",
         f"下载与提取日期：2026-11-06　|　共 {len(spec['papers'])} 篇", "",
         "所有 PDF 在 `pdf/`，全文纯文本在 `text/`（每页带 `===== slug | page i/N =====` 标记）。", ""]

for ckey, cname in clusters.items():
    items = rows_by_cluster.get(ckey, [])
    if not items:
        continue
    lines += [f"## {ckey} — {cname}", "",
              "| slug | 标题（提取自首页） | arXiv | 页 | 字符 |",
              "|---|---|---|---:|---:|"]
    for p in items:
        st = stats.get(p["slug"], {})
        tpath = ROOT / "text" / f"{p['slug']}.txt"
        title = p["note"]
        if tpath.exists():
            head = [l.strip() for l in tpath.read_text(encoding="utf-8").splitlines()
                    if l.strip() and not l.startswith("=====")][:12]
            cand = " ".join(head[:3])
            if len(cand) > 12:
                title = cand[:110]
        title = title.replace("|", "/")
        lines.append(f"| `{p['slug']}` | {title} | [{p['arxiv']}](https://arxiv.org/abs/{p['arxiv']}) "
                     f"| {st.get('pages','')} | {st.get('chars',0):,} |")
    lines.append("")

(ROOT / "SOURCES.md").write_text("\n".join(lines), encoding="utf-8")
print("wrote SOURCES.md", len(spec["papers"]), "papers")
