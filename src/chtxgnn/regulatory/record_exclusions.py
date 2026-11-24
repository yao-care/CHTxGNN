"""證據包收錯品項的排除規則（2026-11-24 第三輪，用戶決定；規則與依據在 config/bundle_record_exclusions.json）。

drug_mapping.csv 依 DrugBank ID 對照許可證，同一個 ID 底下的另一個有效成分（例 scopolamini hydrobromidum 被收進
scopolamini butylbromidum 的證據包）會被收進來。規則：證據包名在規則的 bundles 裡，紀錄成分欄（「, 」分隔）有一段
符合 family、卻沒有一段符合 keep → 排除。scripts/exclude_mismatched_records.py 與 collectors/chfda.py 共用。
"""
from __future__ import annotations

import json
import re
import unicodedata
from functools import lru_cache
from pathlib import Path

CONF = Path(__file__).resolve().parents[3] / "config" / "bundle_record_exclusions.json"


def _norm(s) -> str:
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", s).strip()


def bundle_key(name) -> str:
    return re.sub(r"[^a-z0-9]+", "_", _norm(name)).strip("_")


@lru_cache(maxsize=None)
def rules() -> dict:
    """證據包名 → [規則]"""
    out = {}
    for r in json.loads(CONF.read_text(encoding="utf-8")).get("rules") or []:
        for b in r["bundles"]:
            out.setdefault(bundle_key(b), []).append(r)
    return out


def components(ingredients) -> list:
    return [_norm(c) for c in re.split(r",\s*", str(ingredients or "")) if c.strip()]


def match(bundle, rec):
    """這筆紀錄依規則該排除就回傳規則，否則 None"""
    comps = components(rec.get("ingredients"))
    for r in rules().get(bundle_key(bundle), ()):
        fam, keep = re.compile(r["family"]), re.compile(r["keep"])
        if any(fam.search(c) for c in comps) and not any(keep.search(c) for c in comps):
            return r
    return None
