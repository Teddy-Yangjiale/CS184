"""Download the curated PDF set using environment-configured networking, with validation."""
import json
import sys
import time
from pathlib import Path

import fitz
import requests

from survey_config import ROOT
PDF_DIR = ROOT / "pdf"
from survey_config import PROXIES
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) survey/0.1"}


def download(url: str, dest: Path) -> tuple[bool, str]:
    if dest.exists() and dest.stat().st_size > 20000:
        try:
            with fitz.open(dest) as d:
                return True, f"cached pages={d.page_count}"
        except Exception:  # noqa: BLE001
            dest.unlink(missing_ok=True)
    for attempt in range(3):
        try:
            r = requests.get(url, proxies=PROXIES, headers=HEADERS, timeout=90,
                             allow_redirects=True)
            if r.status_code == 200 and r.content[:5] == b"%PDF-":
                dest.write_bytes(r.content)
                with fitz.open(dest) as d:
                    return True, f"pages={d.page_count} bytes={len(r.content)}"
            elif r.status_code == 200:
                return False, f"not-pdf first12={r.content[:12]!r}"
            else:
                last = f"http {r.status_code}"
        except Exception as e:  # noqa: BLE001
            last = f"{type(e).__name__}: {e}"
        time.sleep(2 + attempt * 2)
    return False, last


def main() -> None:
    spec = json.loads((ROOT / "meta" / "papers.json").read_text(encoding="utf-8"))
    rows, ok, bad = [], 0, 0
    for p in spec["papers"]:
        url = f"https://arxiv.org/pdf/{p['arxiv']}"
        dest = PDF_DIR / f"{p['slug']}.pdf"
        print(f"[{p['slug']:32s}] {url}", end=" ... ", flush=True)
        good, msg = download(url, dest)
        print(("OK  " if good else "FAIL ") + msg, flush=True)
        rows.append({"slug": p["slug"], "arxiv": p["arxiv"], "cluster": p["cluster"],
                     "note": p["note"], "url": url, "ok": good, "detail": msg,
                     "bytes": dest.stat().st_size if dest.exists() else 0})
        ok += good
        bad += not good
        time.sleep(1.2)
    with open(ROOT / "meta" / "download_log.json", "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
    print(f"\n== done: {ok} ok, {bad} failed ==", file=sys.stderr)
    for r in rows:
        if not r["ok"]:
            print("FAILED:", r["slug"], r["detail"], file=sys.stderr)


if __name__ == "__main__":
    main()
