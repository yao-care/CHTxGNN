"""藥物頁許可證資訊的驗證（2026-11-12 建，本站查核機制；比照 TwTxGNN gate 第 6 項、UsTxGNN 同名檔）。

依 snapshots/<站碼>_licenses.json.gz（scripts/build_license_snapshot.py 產生）檢查，不需要 data/：
  1. 市場段落（site_config.MARKET_RE 的標題底下）表格第一欄的許可證號都屬於本藥（快照 own）；
     正文的數字不比對（本站許可證號是純數字時會跟 PMID、年份、張數混在一起）；site_config.PROSE_ID_RE 有設時
     （格式不會跟其他數字混淆，例 EMEA/H/C/000000），正文裡的號碼也比對。
  2. 概覽表的狀態列與張數列＝事實層的寫法：用本站 tools/txgnn/.claude/check_drug_page.py 的函式，
     分支照 checker M1／M4（Marketed／Approved, not marketed／Status unknown／Not marketed＋VET_ONLY／NO_CENTRAL）。
  3. 表格列寫的狀態不得跟事實相反（checker row_status_conflicts）。
本站沒有程式產生的許可證表（表格是模型寫的、狀態格由排程同步），所以不驗表格內容是否等於程式結果。
修法：資料變了→跑每週排程（或 scripts/build_license_snapshot.py 重建快照）；正文提到的號碼、狀態不對→寫查核紀錄
（docs/_data/drug_reviews.json）再跑 scripts/apply_drug_reviews.py。
"""
from __future__ import annotations

import gzip
import importlib.util
import json
import re
import sys
from functools import lru_cache
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from site_config import C  # type: ignore
else:
    from .site_config import C

ROOT = Path(__file__).resolve().parents[3]
SNAP = ROOT / "snapshots" / C["SNAPSHOT"]
SITE = C["SITE"]
MARKET_RE = re.compile(C["MARKET_RE"])
ID_RE = re.compile(C["ID_RE"])
PROSE_ID_RE = re.compile(C["PROSE_ID_RE"]) if C.get("PROSE_ID_RE") else None


@lru_cache(maxsize=None)
def CK():
    p = ROOT / "tools" / "txgnn" / ".claude" / "check_drug_page.py"
    s = importlib.util.spec_from_file_location(f"{SITE}_check_drug_page", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


@lru_cache(maxsize=None)
def snapshot() -> dict:
    if not SNAP.exists():
        return {}
    return json.loads(gzip.open(SNAP).read().decode("utf-8"))


def norm(x: str) -> str:
    return CK().mv2.norm_id(x)


def _sections(lines):
    """市場段落（可能不只一個）的 (開始, 結束)"""
    out = []
    for i, ln in enumerate(lines):
        if ln.startswith("## ") and MARKET_RE.search(ln[3:]):
            j = next((k for k in range(i + 1, len(lines)) if lines[k].startswith("## ")), len(lines))
            out.append((i + 1, j))
    return out


def _tables(lines):
    out, cur = [], []
    for ln in lines + [""]:
        if ln.startswith("|"):
            cur.append(ln)
        elif cur:
            out.append(cur)
            cur = []
    return out


def _rows(tbl):
    return [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in tbl[2:]]


def _cell_id(cell):
    """表格第一欄 → 許可證號（去掉 markdown、括號附註、「Registro」等前綴）；不像號碼回 None"""
    s = re.sub(r"\*\*|`|\[([^\]]*)\]\([^)]*\)", r"\1", cell or "").strip()
    m = ID_RE.search(s)
    return m.group(0) if m else None


def expected_status(fc):
    ck, lang = CK(), CK().LANG.get(SITE, "en")
    ms, v, n, partial = fc.get("market_status"), fc.get("valid"), fc.get("total"), fc.get("partial")
    if ms == "Marketed":
        return ck.marketed_text(SITE, lang, v, n, partial, fc)
    if ms == "Approved, not marketed":
        return ck.not_marketed_text(SITE, lang, fc)
    if ms == "Status unknown" and SITE in ck.UNKNOWN_ST:
        return ck.unknown_status_text(SITE, lang, fc)
    if ms == "Not marketed" and SITE in ck.VET_ONLY:
        return ck.not_reg_text(SITE, lang, fc)
    if ms == "Not marketed" and SITE in getattr(ck, "NO_CENTRAL", {}):
        return ck.NO_CENTRAL[SITE]
    return None


def page_problems(stem: str, text: str) -> list[str]:
    e = (snapshot().get("drugs") or {}).get(stem)
    if e is None:
        return []  # 快照沒有的頁（沒有證據包）：不驗
    ck = CK()
    body = re.sub(r"<!-- review:begin (\S+) -->.*?<!-- review:end \1 -->", "", text, flags=re.S)
    lines = body.replace("\r\n", "\n").split("\n")
    errs = []
    own = {norm(x) for x in e["own"]}
    fc = e.get("facts") or {}
    lic = {norm(k): v for k, v in (fc.get("licenses") or {}).items()}
    for a, b in _sections(lines):
        for t in _tables(lines[a:b]):
            bad = sorted({i for r in _rows(t) for i in [_cell_id(r[0] if r else "")] if i and norm(i) not in own})
            if bad:
                errs.append(f"市場段落許可證表的號碼不屬於本藥：{', '.join(bad[:5])}")
            if lic:
                for code, d in ck.row_status_conflicts(SITE, _rows(t), lic):
                    errs.append(f"許可證表列的狀態跟事實相反：{d}")
        if PROSE_ID_RE:
            for ln in lines[a:b]:
                if ln.startswith("|"):
                    continue
                bad = sorted({m.group(0) for m in PROSE_ID_RE.finditer(ln)} - set(e["own"]))
                bad = [x for x in bad if norm(x) not in own]
                if bad:
                    errs.append(f"市場段落正文的許可證號不屬於本藥：{', '.join(bad[:5])}")
    if fc:
        all_rows = [r for t in _tables(lines) for r in _rows(t)]
        st = ck.status_row(SITE, all_rows)
        want_s = expected_status(fc)
        if st is not None and want_s and st[1] != want_s:
            errs.append(f"狀態列「{st[1][:50]}」≠ 事實層寫法「{want_s}」")
        cr = ck.count_row(SITE, all_rows)
        if cr is not None and (fc.get("total") is not None or fc.get("partial")):
            want_c = ck.count_text(SITE, ck.LANG.get(SITE, "en"), fc)
            if cr[1] != want_c:
                errs.append(f"張數列「{cr[1][:50]}」≠ 事實層寫法「{want_c}」")
    return errs


def site_problems(drugs_dir: Path | None = None) -> list[str]:
    drugs_dir = drugs_dir or ROOT / "docs" / "_drugs"
    if not snapshot():
        return [f"找不到 snapshots/{C['SNAPSHOT']}（跑 scripts/build_license_snapshot.py）"]
    out = []
    for f in sorted(drugs_dir.glob("*.md")):
        t = f.read_text(encoding="utf-8")
        if 'http-equiv="refresh"' in t[:3000] or re.search(r"^layout:\s*id_redirect", t[:3000], re.M):
            continue
        out += [f"{f.name}：{x}" for x in page_problems(f.stem, t)]
    return out


if __name__ == "__main__":
    errs = site_problems()
    for x in errs[:50]:
        print("  ✗", x)
    print(f"許可證檢查：{'✗' if errs else '✓'} {len(errs)} 項")
    sys.exit(1 if errs else 0)
