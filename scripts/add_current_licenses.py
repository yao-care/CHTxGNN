#!/usr/bin/env python3
"""補收 Swissmedic 現行清單上、2026-03 之後才出現的本藥許可（2026-11-25 第五輪，用戶決定）。

證據包的 tfda 區塊是 collectors/chfda.py 依 2026-03 的包裝清單（data/raw/ch_fda_drugs.json）與
data/processed/drug_mapping.csv（品目成分→DrugBank ID）收的；之後才核准的許可（多為生物相似藥、學名藥）不在
drug_mapping，每週排程只更新既有號碼的狀態，永遠收不進來。

規則（照原收集器，不放寬）：
- 本藥的 DrugBank ID＝證據包 tfda.drugbank_ids（原收集器存下的）。
- 現行包裝清單（Zugelassene Packungen HAM）每個許可號的 DrugBank ID：
  2026-03 清單有的號碼照 drug_mapping.csv（同原收集器）；2026-03 之後才出現的號碼，成分欄原文跟 drug_mapping 某列
  original_ingredient 完全相同就沿用那列的對照（含 2026-10-12 的複方補救結果），否則用本站同一支
  mapping.drugbank_mapper.map_fda_drugs_to_drugbank 對照（產生 drug_mapping 的同一支）。
- 跟證據包 DrugBank ID 有交集、2026-03 清單沒有、證據包也沒有（records、records_not_stored、excluded_records）的號碼補進來；
  config/bundle_record_exclusions.json 判為「另一個有效成分」的不收（record_exclusions.match，同收集器）。
- 一個包裝一筆紀錄（同原收集器；欄位照 chfda._format），記 source（清單日期與規則）、added（補收日）；
  records 照原收集器最多存 20 筆（先每個新許可號存一個包裝，有空位再存其餘），超過的包裝只記在 records_not_stored
  （號碼、包裝數、license_listed＝同號已有包裝存在 records），並算進 total_matches。reviewer._local_regulatory 與
  sync_license_tables.rows_of 判 partial 時不算 license_listed 的包裝（許可號清單仍完整）。
- 證據包是 2026-03-29 收的（當時的 drug_mapping＝drug_mapping.csv.bak_20261012，複方整串對不到）或 2026-10-12 重收的
  （現行 drug_mapping.csv），新許可號照該證據包收集當時那一版的規則對照。
- 原收集器退回成分欄比對（證據包沒有 DrugBank ID）的證據包不處理。
- 停損：證據包的 total_matches 跟「2026-03 清單照原規則重算的包裝數－已移出筆數＋本程式補過的包裝數」不符的不補、列出。
只加不刪、可重複執行（第二次跑 0 筆）。每週 license-refresh.yml 在 license_refresh 前以 --download 跑。
用法（repo 根目錄，先還原 data/）：
  python3 scripts/add_current_licenses.py [--download | --xlsx <zugelassene_packungen_ham.xlsx>] [--dry-run] [--report out.tsv]
"""
from __future__ import annotations

import argparse
import collections
import csv
import io
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

CUR_COPY = ROOT / "data" / "raw" / "swissmedic_packungen_current.xlsx"   # 下載的現行清單存一份（Release 帶著）
MAX_RECORDS = 20
MIN_ROWS = 8000


def _hdr(x):
    return str(x or "").split("\n")[0].strip().rstrip("*").strip()


def load_current(xlsx_bytes):
    import openpyxl
    ws = openpyxl.load_workbook(io.BytesIO(xlsx_bytes), read_only=True).active
    head, rows, stand = None, [], ""
    for row in ws.iter_rows(values_only=True):
        if head is None:
            for x in row or ():
                m = re.search(r"Stand\s*/\s*Etat au:\s*([0-9.]+)", str(x or ""))
                if m:
                    stand = m.group(1)
            if row and row[0] and str(row[0]).startswith("Zulassungs"):
                head = [_hdr(x) for x in row]
            continue
        rec = dict(zip(head, row))
        k = str(rec.get("Zulassungs-nummer") or "").strip()
        if k:
            rows.append(rec)
    if head is None or "Wirkstoff(e)" not in head:
        raise RuntimeError(f"找不到表頭或成分欄：{head}")
    return rows, stand


def _s(v):
    if v is None:
        return ""
    if hasattr(v, "strftime"):
        return v.strftime("%Y-%m-%d %H:%M:%S")
    return str(v).strip()


def record_of(rec, src, today):
    g = lambda k: _s(rec.get(k))  # noqa: E731
    return {
        "license_id": g("Zulassungs-nummer"),
        "brand_name_zh": g("Bezeichnung des Arzneimittels"),
        "brand_name_en": g("Wirkstoff(e)"),
        "ingredients": g("Wirkstoff(e)"),
        "indication": g("Anwendungsgebiet Arzneimittel"),
        "dosage_form": g("Heilmittelcode"),
        "manufacturer": g("Zulassungsinhaberin"),
        "license_holder": g("Zulassungsinhaberin"),
        "approval_date": g("Erstzul.datum Arzneimittel"),
        "expiry_date": "",
        "status": "",
        "source": src,
        "added": today,
    }


def mapping(fname):
    """drug_mapping.csv（或收集當時的版本）→ (許可號→DB IDs, 成分原文→DB IDs)；同原收集器只收 mapping_success 的列"""
    lic2db, ing2db = collections.defaultdict(set), collections.defaultdict(set)
    with open(ROOT / "data" / "processed" / fname, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            db = str(r.get("drugbank_id") or "").strip().upper()
            if not db or str(r.get("mapping_success")).strip().lower() not in ("true", "1", "yes"):
                continue
            lic2db[str(r["license_id"]).strip()].add(db)
            ing2db[str(r["original_ingredient"]).strip()].add(db)
    return lic2db, ing2db


def _mapper(strings):
    """本站產生 drug_mapping 的同一支（整串成分原文對 DrugBank；複方整串對不到就是對不到）"""
    import pandas as pd
    from chtxgnn.mapping.drugbank_mapper import map_fda_drugs_to_drugbank
    out = {s: set() for s in strings}
    if not strings:
        return out
    df = pd.DataFrame([{"lid": i, "ing": v} for i, v in enumerate(strings)])
    mp = map_fda_drugs_to_drugbank(df, field_mapping={"license_id": "lid", "brand_name": "lid", "ingredients": "ing"})
    for _, r in mp.iterrows():
        if r["mapping_success"] and r["drugbank_id"]:
            out[strings[int(r["license_id"])]].add(str(r["drugbank_id"]).upper())
    return out


def map_new(new_rows, gens):
    """2026-03 之後才出現的許可號 → {世代: DB IDs}。
    v0312（2026-03-29 收集的證據包，drug_mapping.csv.bak_20261012）：整串成分原文對照，同原文沿用、否則用同一支 mapper；
    v1012（2026-10-12 重收的證據包，現行 drug_mapping.csv，含當日的複方補救）：整串同上；複方另逐成分（「, 」）沿用
    現行 drug_mapping 裡同一段原文已對到的 ID（2026-10-12 的補救結果），沒出現過的成分不對。"""
    ings = {lid: _s(recs[0].get("Wirkstoff(e)")) for lid, recs in new_rows.items()}
    whole = {}
    for gen, (_, ing2db) in gens.items():
        need = sorted({v for v in ings.values() if v not in ing2db})
        mp = _mapper(need)
        whole[gen] = {lid: set(ing2db.get(v) or mp.get(v) or ()) for lid, v in ings.items()}
    out = {lid: {g: set(whole[g][lid]) for g in gens} for lid in ings}
    cur_ing = gens["v1012"][1]
    for lid, v in ings.items():
        parts = [p.strip() for p in re.split(r",\s*", v) if p.strip()]
        if len(parts) > 1:
            for p in parts:
                out[lid]["v1012"] |= cur_ing.get(p, set())
    return out


def _download():
    import license_adapter as LA
    return LA._download()


def run(xlsx_bytes, dry=False, report=None):
    from chtxgnn.regulatory import record_exclusions as RX
    today = time.strftime("%Y-%m-%d")
    cur, stand = load_current(xlsx_bytes)
    if len(cur) < MIN_ROWS:
        print(f"✗ 現行清單只有 {len(cur)} 列，疑似下載或格式有問題，不補收")
        return 2
    base = json.loads((ROOT / "data" / "raw" / "ch_fda_drugs.json").read_text(encoding="utf-8"))
    base_pk = collections.Counter(str(r["Zulassungs-nummer"]).strip() for r in base)
    cur_by = collections.defaultdict(list)
    for r in cur:
        cur_by[str(r["Zulassungs-nummer"]).strip()].append(r)
    gens = {"v0312": mapping("drug_mapping.csv.bak_20261012"), "v1012": mapping("drug_mapping.csv")}
    newmap = map_new({k: v for k, v in cur_by.items() if k not in base_pk}, gens)
    db2new = {g: collections.defaultdict(set) for g in gens}
    db2base = {g: collections.defaultdict(set) for g in gens}
    for g in gens:
        for lid, d in newmap.items():
            for db in d[g]:
                db2new[g][db].add(lid)
        for lid in base_pk:
            for db in gens[g][0].get(lid, ()):
                db2base[g][db].add(lid)
    src = f"Swissmedic Zugelassene Packungen HAM (Stand {stand}); matched by DrugBank ID, same rule as collectors/chfda.py"
    added_b, added_pk, stored, skipped, rep = 0, 0, 0, [], []
    for f in sorted((ROOT / "data" / "bundles").glob("*/drug_bundle.json")):
        name = f.parent.name
        b = json.loads(f.read_text(encoding="utf-8"))
        t = b.get("tfda") or {}
        ids = {str(x).upper() for x in t.get("drugbank_ids") or []}
        if not ids:
            continue
        q = [x.get("queried_at", "")[:10] for x in b.get("collection_log") or [] if x.get("source") == "tfda"]
        gen = "v1012" if q and q[0] >= "2026-10-12" else "v0312"   # 收集當時的 drug_mapping 版本
        cand = set().union(*(db2new[gen].get(d, set()) for d in ids))
        recs = t.get("records") or []
        have = {str(r.get("license_id")) for r in recs}
        ns = t.get("records_not_stored") or []
        have |= {str(x.get("license_id")) for x in ns}
        excl = t.get("excluded_records") or []
        have |= {str(r.get("license_id")) for r in excl}
        todo = []
        for lid in sorted(cand - have, key=lambda x: int(x) if x.isdigit() else 0):
            pk = [r for r in cur_by[lid] if not RX.match(name, {"ingredients": _s(r.get("Wirkstoff(e)"))})]
            if pk:
                todo.append((lid, pk))
        if not todo:
            continue
        # 停損：total_matches＝2026-03 原規則包裝數－已移出（原本算過的）＋本程式補過的包裝數
        base_lics = set().union(*(db2base[gen].get(d, set()) for d in ids))
        n_base = sum(base_pk[l] for l in base_lics)
        n_excl_old = sum(1 for r in excl if str(r.get("license_id")) in base_pk)
        n_mine = sum(1 for r in recs if r.get("added") and str(r.get("source", "")).startswith("Swissmedic Zugelassene Packungen")) \
            + sum(int(x.get("packages") or 0) for x in ns)
        expect = n_base - n_excl_old + n_mine
        tm = int(t.get("total_matches") or 0)
        if tm != expect:
            skipped.append((name, tm, expect, [l for l, _ in todo], gen))
            continue
        # 先每個許可號存一個包裝（讓許可號列得出來），有空位再存其餘包裝
        keep = {lid: [] for lid, _ in todo}
        for rnd in (0, 1):
            for lid, pk in todo:
                for r in (pk[:1] if rnd == 0 else pk[1:]):
                    if len(recs) < MAX_RECORDS:
                        recs.append(record_of(r, src, today))
                        keep[lid].append(r)
        for lid, pk in todo:
            kept = len(keep[lid])
            if kept < len(pk):
                # license_listed：這個許可號已有包裝存在 records，沒存的包裝不影響「許可號清單是否完整」（事實層 partial 不算它們）
                ns.append({"license_id": lid, "packages": len(pk) - kept, "license_listed": kept > 0,
                           "brand_name": _s(pk[0].get("Bezeichnung des Arzneimittels")),
                           "ingredients": _s(pk[0].get("Wirkstoff(e)")), "source": src, "added": today})
            t["total_matches"] = int(t.get("total_matches") or 0) + len(pk)
            added_pk += len(pk)
            stored += kept
            rep.append((name, gen, lid, len(pk), kept, _s(pk[0].get("Bezeichnung des Arzneimittels")), _s(pk[0].get("Wirkstoff(e)"))))
        added_b += 1
        if ns:
            t["records_not_stored"] = ns
        t["records"] = recs
        t["found"] = bool(recs)
        b["tfda"] = t
        if not dry:
            f.write_text(json.dumps(b, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for s in skipped:
        print(f"  ✗ 停損 {s[0]}：total_matches {s[1]} ≠ 原規則重算 {s[2]}，不補 {', '.join(s[3])}（{s[4]}）")
    if report:
        with open(report, "w", encoding="utf-8") as fo:
            fo.write("bundle\tgen\tlicense\tpackages\tstored\tname\tingredients\n")
            for r in rep:
                fo.write("\t".join(map(str, r)) + "\n")
    nl = len({(r[0], r[2]) for r in rep})
    print(f"Swissmedic 新許可補收（Stand {stand}）：{added_b} 個證據包補 {nl} 個許可號、{added_pk} 個包裝（存進 records {stored}）；停損 {len(skipped)} 個證據包{'（試跑，沒寫檔）' if dry else ''}")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--download", action="store_true")
    ap.add_argument("--xlsx")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--report")
    a = ap.parse_args()
    if a.xlsx:
        data = Path(a.xlsx).read_bytes()
    elif a.download:
        data = _download()
        if not a.dry_run:
            CUR_COPY.write_bytes(data)
    elif CUR_COPY.exists():
        data = CUR_COPY.read_bytes()
    else:
        sys.exit("沒有現行清單：給 --download 或 --xlsx")
    sys.exit(run(data, dry=a.dry_run, report=a.report))


if __name__ == "__main__":
    main()
