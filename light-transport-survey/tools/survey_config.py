"""Portable paths and optional networking settings for survey scripts."""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# With no override, requests uses the standard HTTP(S)_PROXY / NO_PROXY settings.
_proxy = os.environ.get("SURVEY_PROXY", "").strip()
PROXIES = {"http": _proxy, "https": _proxy} if _proxy else {}
