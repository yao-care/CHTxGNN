#!/usr/bin/env python3
"""產生許可證快照 snapshots/<站碼>_licenses.json.gz（2026-11-12 建，本站查核機制；比照 TwTxGNN、UsTxGNN）。

為什麼要有這支：概覽表的狀態列與張數列由程式依證據包（data/bundles，放在 Release）與事實層
（.claude/cache/license_facts，dump_license_facts 依證據包算）產生。gate（scripts/check_seo_docs.py）要在沒有 data/ 的環境
也能驗證頁面上的許可證號屬於本藥、狀態列與張數列跟事實一致，所以把驗證要用的部分存成快照放進 git。

內容（鍵＝藥物頁檔名去 .md）：
  facts：事實層那一筆（market_status、total、valid、cancelled、partial、licenses{號碼: 狀態} …）
  own：本藥證據包 tfda.records 的許可證號（license_id 或 registration_number）、事實層 licenses 的號碼，
       加上 config/license_own_extra.json（有的站才有）逐筆附依據的補充號碼
  meta：產生日、Release tag、比對規則所在檔案
什麼時候跑：證據包或事實層變了之後（每週許可證排程 license-refresh.yml 會在改頁後跑，並把 snapshots/ 跟 docs/ 一起 commit）。
用法（repo 根目錄，先還原 data/ 並在工作目錄跑 dump_license_facts）：
  python3 scripts/build_license_snapshot.py --ws <工作目錄> [--release-tag data-YYYYMMDD-HHMMSS]
"""
import datetime as dt
import gzip
import importlib as _il
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
_PKG = next(p.parent.parent.name for p in (ROOT / "src").glob("*/regulatory/site_config.py"))
C = _il.import_module(f"{_PKG}.regulatory.site_config").C
SITE = C["SITE"]
OUT = ROOT / "snapshots" / C["SNAPSHOT"]
EXTRA = ROOT / "config" / "license_own_extra.json"


def facts(ws):
    p = Path(ws) / ".claude/cache/license_facts" / f"{SITE}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def bundle_for(stem):
    for key in (stem, stem.replace("-", "_"), stem.replace("_", "-")):
        f = ROOT / "data/bundles" / key / "drug_bundle.json"
        if f.exists():
            return key, json.loads(f.read_text(encoding="utf-8"))
    return None, None


def build(ws, tag=""):
    fs = facts(ws)
    if not fs:
        sys.exit(f"找不到事實層 {Path(ws) / '.claude/cache/license_facts' / (SITE + '.json')}（先跑 dump_license_facts）")
    drugs = {}
    extra = json.loads(EXTRA.read_text(encoding="utf-8")).get("pages", {}) if EXTRA.exists() else {}
    for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
        head = page.read_text(encoding="utf-8", errors="replace")[:3000]
        if "layout: id_redirect" in head or 'http-equiv="refresh"' in head:
            continue
        key, b = bundle_for(page.stem)
        fc = fs.get(page.stem) or fs.get(page.stem.replace("-", "_")) or fs.get(page.stem.replace("_", "-"))
        if b is None and fc is None:
            continue
        own = {str(r.get("license_id") or r.get("registration_number") or "").strip()
               for r in ((b or {}).get("tfda") or {}).get("records") or []} - {""}
        own = sorted(own | set((fc or {}).get("licenses") or {}) | set(extra.get(page.stem) or {}))
        drugs[page.stem] = {"bundle": key, "facts": fc, "own": own}
    meta = {"built": dt.date.today().isoformat(), "release_tag": tag, "pages": len(drugs),
            "rule": "事實層：tools/txgnn/.claude/dump_license_facts_20261021.py；本藥號碼：證據包 tfda.records、事實層 licenses、config/license_own_extra.json"}
    OUT.parent.mkdir(exist_ok=True)
    raw = json.dumps({"meta": meta, "drugs": drugs}, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    with gzip.GzipFile(OUT, "wb", mtime=0) as fh:
        fh.write(raw)
    print(f"許可證快照：{len(drugs)} 頁 → {OUT.relative_to(ROOT)}（{OUT.stat().st_size // 1024} KB）")


if __name__ == "__main__":
    a = sys.argv[1:]
    ws = a[a.index("--ws") + 1]
    tag = a[a.index("--release-tag") + 1] if "--release-tag" in a else ""
    if not re.fullmatch(r"(data-[\w-]+)?", tag):
        sys.exit("--release-tag 要是 data-… 的 tag")
    build(ws, tag)
