"""Extract full text from the downloaded PDFs.

Strategy: PyMuPDF text layer first (born-digital PDFs). Any page whose text layer
is essentially empty is rendered and passed through the locally installed
rapidocr_onnxruntime engine (no downloads, CPU ONNX).
"""
import json
import sys
import time
from pathlib import Path

import fitz
import numpy as np

from survey_config import ROOT
PDF_DIR, TXT_DIR = ROOT / "pdf", ROOT / "text"
MIN_CHARS = 120


def ocr_page(page: fitz.Page, engine) -> str:
    pix = page.get_pixmap(dpi=200)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
    if pix.n == 4:
        img = img[:, :, :3]
    res, _ = engine(img)
    if not res:
        return ""
    return "\n".join(item[1] for item in res)


def main() -> None:
    engine = None
    rows = []
    pdfs = sorted(PDF_DIR.glob("*.pdf"))
    for pdf in pdfs:
        slug = pdf.stem
        doc = fitz.open(pdf)
        parts, ocr_pages, empty_pages = [], [], []
        for i, page in enumerate(doc, start=1):
            txt = page.get_text("text")
            if len(txt.strip()) < MIN_CHARS:
                try:
                    if engine is None:
                        from rapidocr_onnxruntime import RapidOCR
                        engine = RapidOCR()
                    txt = ocr_page(page, engine)
                    ocr_pages.append(i)
                except Exception as e:  # noqa: BLE001
                    print(f"  OCR fail p{i}: {e}", file=sys.stderr)
            if not txt.strip():
                empty_pages.append(i)
            parts.append(f"\n\n===== {slug} | page {i}/{doc.page_count} =====\n\n{txt}")
        doc.close()
        out = TXT_DIR / f"{slug}.txt"
        body = "".join(parts)
        out.write_text(body, encoding="utf-8")
        nchars = len(body)
        rows.append({"slug": slug, "pages": len(parts), "chars": nchars,
                     "ocr_pages": ocr_pages, "empty_pages": empty_pages,
                     "txt": out.relative_to(ROOT).as_posix()})
        print(f"{slug:32s} pages={len(parts):3d} chars={nchars:7d} "
              f"ocr={ocr_pages} empty={empty_pages}", flush=True)
        time.sleep(0.2)
    (ROOT / "meta" / "extract_stats.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    total = sum(r["chars"] for r in rows)
    print(f"\n== {len(rows)} docs, {total/1e6:.2f} M chars ==", file=sys.stderr)


if __name__ == "__main__":
    main()
