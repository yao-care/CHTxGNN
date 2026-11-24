#!/usr/bin/env python3
"""市場段落的許可證表由程式產生（2026-11-24，用戶決定「程式產生許可證表」；範本 DETxGNN 同名檔、UkTxGNN／SgTxGNN）。

為什麼：市場段落（「## / ### Marktinformationen Schweiz」）的許可證表原本是 AI 寫的表（多數表頭
「Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation」，少數另有 Zulassungsinhaberin／Status 欄），
沒有狀態欄或狀態寫死；Swissmedic 清單每週變，AI 表不會跟著改。改成程式依證據包（data/bundles 的 tfda.records＝
Swissmedic 核准包裝，一張許可可有多個包裝與劑量）產生，每週排程（license_adapter.sync_tables）自動同步。

表的內容（全程不用 AI；文字照 Swissmedic 清單原文，不翻譯）：
  | Zulassungsnummer | Produktname | Kategorie (Heilmittelcode) | Anwendungsgebiet (Swissmedic) | Status |
  一張許可一列（同一許可號的多個包裝取第一筆，跟 reviewer._local_regulatory 的去重一樣）；同一許可有其他品名（劑量）時
  品名後加「(+N weitere Bezeichnung[en])」。舊表的「Darreichungsform」欄放的其實是 Swissmedic 的 Heilmittelcode
  （Synthetika、Biotechnologika…），照實改名。
  狀態欄＝事實層（reviewer._local_regulatory 的規則：license_status、狀態字、有效期限已過→Erloschen，其餘 Gültig）。
  排序：有效在前，同狀態依許可號；最多 MAX_ROWS 列。證據包只收了部分包裝（事實層 partial）時加 PARTIAL 句。
  表後一行來源句（SOURCE）；本藥沒有紀錄時整個區塊只有 NONE_LINE 一行。
  區塊前後各一行 <!-- licenses:begin --> <!-- licenses:end -->（查核紀錄、刪句工具與 gate 用來分辨程式寫的字）。
放在哪：本頁標題含「Marktinformationen」的段落（## 或 ###），取代段落裡第一張許可證表（表頭含「Zulassung」）；
  段落裡沒有表時放在段落開頭（標題下）。沒有這種段落的頁不加（「Grundlegende Informationen」是概覽表、
  「Bekannte Anwendungen und Marktstatus」是已知用途頁，都不放）。表以外的文字不動（正文張數由 scripts/rewrite_license_counts.py 改寫）。
資料來源：預設讀快照 snapshots/ch_licenses.json.gz 的 rows／total／partial（scripts/build_license_snapshot.py 依證據包算好，
  用 rows_of）；--bundles 改讀 data/bundles（每週排程在建新快照前用）。gate（scripts/check_seo_docs.py 的許可證項）
  檢查程式區塊＝快照重算的結果。
誰會跑：scripts/apply_drug_reviews.py（非 --check）結尾、scripts/build_license_snapshot.py 結尾、每週排程
  license_adapter.sync_tables（--bundles）。sync_notes_to_docs.py 整頁重寫後會跑 apply_drug_reviews.py，所以也會重新產生。
用法（repo 根目錄）：python3 scripts/sync_license_tables.py [--bundles] [--check] [頁 ...]
"""
import datetime as _dt
import gzip
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAP = ROOT / "snapshots" / "ch_licenses.json.gz"
SEC_RE = re.compile(r"Marktinformationen")
BEGIN = "<!-- licenses:begin -->"
END = "<!-- licenses:end -->"
HEAD = ["| Zulassungsnummer | Produktname | Kategorie (Heilmittelcode) | Anwendungsgebiet (Swissmedic) | Status |",
        "|------|------|------|------|------|"]
SOURCE = ("Quelle: Swissmedic – Zugelassene Packungen und Zugelassene Arzneimittel (Humanarzneimittel); Produktname, Kategorie "
          "und Anwendungsgebiet im Wortlaut der Swissmedic-Listen. „Erloschen“: Gültigkeitsdauer der Zulassung abgelaufen oder "
          "in den aktuellen Swissmedic-Listen nicht mehr aufgeführt.")
PARTIAL = "Die ausgewerteten Daten enthalten nur einen Teil der Packungen dieses Wirkstoffs; die Liste kann unvollständig sein."
NONE_LINE = "In den ausgewerteten Swissmedic-Daten ist für diesen Wirkstoff keine Zulassung erfasst."
MAX_ROWS = 20
ST_LABEL = {"valid": "Gültig", "cancelled": "Erloschen"}
_CANCELLED = re.compile(r"cancel|revok|withdraw|erlosch|widerruf|註銷|撤銷|取消", re.I)  # 只在狀態欄有字時用（CH 的 status 都是空字串）
# 每週排程 3b 的自我檢查（license_refresh）：改到的行除了表格列只能是這些（license_adapter.PAGE_NOTE 用同一份）
# 2026-11-24 第三輪（用戶決定）：公開頁沒有 Marktinformationen 段落、證據包卻有紀錄的，補一個段落放程式表（add_section）。
# 位置：「Sicherheitshinweise」標題之前（預測頁的固定順序，同級標題）；沒有就「Fazit und nächste Schritte」之前；再沒有就「Haftungsausschluss」之前。
# noindex 頁與證據包沒有紀錄的頁不補。段落後補一行「---」分隔（本站各段之間的寫法）。
ADD_TITLE = "Marktinformationen Schweiz"
ADD_BEFORE = ("Sicherheitshinweise", "Fazit und nächste Schritte", "Haftungsausschluss")
PAGE_NOTE = (r"^(" + "|".join(re.escape(x) for x in (BEGIN, END, SOURCE, PARTIAL, NONE_LINE)) + r"|#{2,3} "
             + re.escape(ADD_TITLE) + r"|---)$")


def cell(x, n=90):
    t = re.sub(r"\s+", " ", str(x or "").replace("|", "/")).strip()
    return (t if len(t) <= n else t[:n - 1].rstrip() + "…") or "–"


def rec_status(r):
    """跟 chtxgnn.reviewer.drug_evidence_pack._local_regulatory_impl 同一套規則（事實層就是用它算的）"""
    st = r.get("license_status") or ("cancelled" if _CANCELLED.search(str(r.get("status") or "")) else "valid")
    exp = re.sub(r"[^0-9]", "", str(r.get("expiry_date") or ""))[:8]
    if st == "valid" and not r.get("status") and len(exp) == 8 and exp < _dt.date.today().strftime("%Y%m%d"):
        st = "cancelled"
    return st


def rows_of(tf, fc=None):
    """證據包 tfda → (表格列, 許可張數, partial)。狀態優先用事實層 fc['licenses']（同一套規則算的），沒有就照紀錄算。"""
    lic = (fc or {}).get("licenses") or {}
    first, names = {}, {}
    for r in tf.get("records") or []:
        k = str(r.get("license_id") or "").strip()
        if not k:
            continue
        nm = cell(r.get("brand_name_zh") or r.get("brand_name_en"), 200)
        if k not in first:
            first[k] = r
            names[k] = [nm]
        elif nm not in names[k]:
            names[k].append(nm)
    valid, other = [], []
    for k, r in first.items():
        st = lic.get(k) or rec_status(r)
        nm = cell(names[k][0], 70)
        more = len(names[k]) - 1
        if more:
            nm += f" (+{more} weitere Bezeichnung{'en' if more > 1 else ''})"
        row = (int(k) if k.isdigit() else 10 ** 9, k,
               f"| {k} | {nm} | {cell(r.get('dosage_form'), 40)} | {cell(r.get('indication'), 110)} | {ST_LABEL.get(st, st)} |")
        (valid if st == "valid" else other).append(row)
    rows = [x[2] for x in sorted(valid)] + [x[2] for x in sorted(other)]
    partial = int(tf.get("total_matches") or 0) > len(tf.get("records") or [])
    return rows, len(rows), partial


def program_block(rows, total, partial=False):
    if not rows:
        return [NONE_LINE]
    out = HEAD + rows[:MAX_ROWS] + [""]
    if partial or total > min(len(rows), MAX_ROWS):
        out += [PARTIAL, ""]
    return out + [SOURCE]


def wrap(block):
    return [BEGIN, ""] + block + ["", END]


def _is_license_table_head(lines, k):
    return lines[k].startswith("|") and (k == 0 or not lines[k - 1].startswith("|")) and "Zulassung" in lines[k] \
        and k + 1 < len(lines) and re.match(r"\|\s*:?-", lines[k + 1])


def sections(lines):
    """標題含 Marktinformationen 的段落 (標題行, 結束)；段落到下一個同級或更高級標題為止"""
    out = []
    for i, ln in enumerate(lines):
        m = re.match(r"(#{2,3}) ", ln)
        if m and SEC_RE.search(ln):
            lev = len(m.group(1))
            j = next((k for k in range(i + 1, len(lines)) if re.match(r"#{1,%d} " % lev, lines[k])), len(lines))
            out.append((i, j))
    return out


def _splice(lines, x, y, blk):
    """lines[x:y] 換成 blk，前後各留恰好一行空行（只動接縫處的空行）"""
    head, tail = lines[:x], lines[y:]
    while head and not head[-1].strip():
        head.pop()
    while tail and not tail[0].strip():
        tail.pop(0)
    return head + [""] + blk + ([""] + tail if tail else [""])


def process(text, rows, total, partial=False):
    """回傳新內容（沒有市場段落時原樣）。可重複執行。"""
    lines = text.replace("\r\n", "\n").split("\n")
    blk = wrap(program_block(rows, total, partial))
    if BEGIN in lines and END in lines:
        return "\n".join(_splice(lines, lines.index(BEGIN), lines.index(END) + 1, blk))
    secs = sections(lines)
    for a, b in secs:
        tb = [k for k in range(a + 1, b) if _is_license_table_head(lines, k)]
        if tb:
            y = tb[0]
            while y + 1 < b and lines[y + 1].startswith("|"):
                y += 1
            return "\n".join(_splice(lines, tb[0], y + 1, blk))
    if not secs:
        return add_section(lines, blk, total) or text
    a = secs[0][0]
    k = a + 1
    while k < len(lines) and lines[k].startswith("{:"):  # 標題下的 kramdown 屬性行
        k += 1
    return "\n".join(_splice(lines, k, k, blk))


def is_noindex(lines):
    fm = []
    if lines and lines[0].strip() == "---":
        for ln in lines[1:]:
            if ln.strip() == "---":
                break
            fm.append(ln)
    return any(re.match(r"noindex:\s*true\b", ln) for ln in fm)


def add_section(lines, blk, total):
    """沒有市場段落的公開頁補段落（見 ADD_BEFORE）；不補回 None"""
    if not total or is_noindex(lines):
        return None
    heads = {}
    for i, ln in enumerate(lines):
        m = re.match(r"^(#{2,3}) (.+?)\s*$", ln)
        if m and m.group(2) not in heads:
            heads[m.group(2)] = (i, len(m.group(1)))
    at = next((heads[h] for h in ADD_BEFORE if h in heads), None)
    if at is None:
        return None
    i, lev = at
    head = lines[:i]
    while head and not head[-1].strip():
        head.pop()
    sec = ["#" * lev + " " + ADD_TITLE, ""] + blk + ["", "---", ""]
    return "\n".join(head + [""] + sec + lines[i:])


def _snapshot():
    return json.loads(gzip.open(SNAP).read().decode("utf-8")).get("drugs", {}) if SNAP.exists() else {}


def _bundle(stem):
    for key in (stem, stem.replace("-", "_"), stem.replace("_", "-")):
        f = ROOT / "data/bundles" / key / "drug_bundle.json"
        if f.exists():
            return json.loads(f.read_text(encoding="utf-8"))
    return None


def is_redirect(text):
    h = text[:3000]
    return 'http-equiv="refresh"' in h or bool(re.search(r"^layout:\s*id_redirect", h, re.M))


def run(from_bundles=False, check=False, only=None):
    """回傳改到的頁（檔名）。快照或證據包沒有的頁不動。"""
    snap = {} if from_bundles else _snapshot()
    changed = []
    for p in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if only and p.name not in only and p.stem not in only:
            continue
        raw = p.read_bytes().decode("utf-8")
        if is_redirect(raw):
            continue
        if from_bundles:
            b = _bundle(p.stem)
            if b is None:
                continue
            rows, total, partial = rows_of(b.get("tfda") or {})
        else:
            e = snap.get(p.stem)
            if not e or "rows" not in e:
                continue
            rows, total, partial = e["rows"], e["total"], e.get("partial", False)
        crlf = "\r\n" in raw[:500]
        t0 = raw.replace("\r\n", "\n")
        new = process(t0, rows, total, partial)
        if new != t0:
            changed.append(p.name)
            if not check:
                p.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
    return changed


def block_problems(lines, entry):
    """gate 用：頁面上的程式區塊＝快照重算的結果；有 Marktinformationen 段落卻沒有程式區塊也算（licenses.page_problems 呼叫）"""
    has_b, has_e = BEGIN in lines, END in lines
    if has_b != has_e:
        return ["程式許可證區塊標記不成對"]
    if "rows" not in entry:
        return []
    if not has_b:
        if sections(lines):
            return ["市場段落沒有程式許可證表（跑 python3 scripts/sync_license_tables.py）"]
        # 2026-11-24 第三輪：公開頁有證據包紀錄卻沒有市場段落（add_section 會補）
        return ["公開頁有證據包紀錄卻沒有 Marktinformationen 段落（跑 python3 scripts/sync_license_tables.py）"] \
            if entry.get("total") and not is_noindex(lines) else []
    i, j = lines.index(BEGIN), lines.index(END)
    if not any(a < i < b for a, b in sections(lines)):
        return ["程式許可證區塊不在 Marktinformationen 段落裡"]
    got = [x for x in lines[i + 1:j] if x.strip()]
    want = [x for x in program_block(entry["rows"], entry["total"], entry.get("partial", False)) if x.strip()]
    if got != want:
        k = next((k for k, (x, y) in enumerate(zip(got, want)) if x != y), min(len(got), len(want)))
        return [f"程式許可證區塊第 {k + 1} 行跟快照重算的結果不同（程式表被手改或資料已更新：跑 python3 scripts/sync_license_tables.py）"]
    return []


if __name__ == "__main__":
    a = sys.argv[1:]
    only = {x for x in a if not x.startswith("--")} or None
    ch = run(from_bundles="--bundles" in a, check="--check" in a, only=only)
    print(f"程式許可證表：{'待改' if '--check' in a else '改'} {len(ch)} 頁")
    if "--check" in a:
        sys.exit(1 if ch else 0)
