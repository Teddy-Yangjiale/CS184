"""Verify the tracked survey snapshot without third-party dependencies.

Run --write only after intentionally updating the survey snapshot. This hashes
files but does not assess scientific correctness or PDF extraction quality.
"""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "meta" / "file_manifest.json"
SKIP_PARTS = {"__pycache__", ".venv", "venv", ".git", ".ipynb_checkpoints"}


def included(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    return (path.is_file() and path != MANIFEST
            and not SKIP_PARTS.intersection(relative.parts)
            and path.suffix not in {".pyc", ".pyo"}
            and path.name != ".env" and not path.name.startswith(".env."))


def digest(path: Path) -> str:
    result = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(chunk)
    return result.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Replace the snapshot manifest")
    args = parser.parse_args()
    if args.write:
        rows = [{"path": p.relative_to(ROOT).as_posix(),
                 "bytes": p.stat().st_size, "sha256": digest(p)}
                for p in sorted(ROOT.rglob("*")) if included(p)]
        MANIFEST.parent.mkdir(parents=True, exist_ok=True)
        MANIFEST.write_text(json.dumps({"schema": 1, "files": rows},
                                      ensure_ascii=False, indent=2) + "\n",
                            encoding="utf-8", newline="\n")
        print(f"Recorded {len(rows)} files ({sum(r['bytes'] for r in rows):,} bytes)")
        return 0
    if not MANIFEST.exists():
        print("Missing meta/file_manifest.json")
        return 1
    rows = json.loads(MANIFEST.read_text(encoding="utf-8"))["files"]
    failures = []
    for row in rows:
        path = ROOT / row["path"]
        if not path.is_file():
            failures.append(f"missing: {row['path']}")
        elif path.stat().st_size != row["bytes"] or digest(path) != row["sha256"]:
            failures.append(f"changed or incomplete: {row['path']}")
    expected = {r["path"] for r in rows}
    extra = [p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*")
             if included(p) and p.relative_to(ROOT).as_posix() not in expected]
    for failure in failures:
        print(failure)
    if extra:
        print(f"Additional local files (not in snapshot): {len(extra)}")
    if failures:
        print("Verification failed. For PDF pointer files, run git lfs pull and retry.")
        return 1
    print(f"Verified {len(rows)} files ({sum(r['bytes'] for r in rows):,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
