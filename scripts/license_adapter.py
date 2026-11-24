"""CH（Swissmedic）許可證下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：Swissmedic「Zugelassene Packungen」人用藥清單 xlsx（免金鑰；網址沿用站上 process_fda_data.py，兩個備用網址）。
清單只列現行許可的包裝、沒有狀態欄，但有「Gültigkeitsdauer der Zulassung」（許可有效期限，unbegrenzt＝無限期）。
寫回：只在狀態會翻轉時改紀錄的 expiry_date（YYYYMMDD；無限期寫空字串），status 不動（保持空白）。
reviewer 在 status 空白時以 expiry_date 判定：已過期算註銷。
2026-11-17（用戶要求確認查不到的許可證）：另下載「Zugelassene Arzneimittel HAM」（藥品層級的現行許可清單）。
只在藥品清單、不在包裝清單的許可號照藥品清單的有效期限算（2026-11-17 有 20 張）；兩份現行清單都沒有的許可號
＝Swissmedic 已不列為現行許可（2026-03 還在、11 月不在的 71 張：35 張效期已過、36 張效期未到但已撤回／放棄），
preprocess 標 license_status＝cancelled 與 swissmedic_not_listed（第一次發現的日期）；之後又出現在清單就取消標記。
兩份清單任一份下載失敗或筆數過少時不做這個判定（維持原狀態）。
同一許可號多個包裝取最晚的期限。
"""
import io
import re
import time

import openpyxl
import requests

RAW_FILE = "raw/swissmedic_gueltigkeit.json"
URLS = [
    "https://www.swissmedic.ch/dam/swissmedic/de/dokumente/internetlisten/zugelassene_packungen_human.xlsx.download.xlsx/zugelassene_packungen_ham.xlsx",
    "https://www.swissmedic.ch/dam/swissmedic/de/dokumente/internetlisten/zugelassene_packungen_ham.xlsx.download.xlsx/zugelassene_packungen_ham.xlsx",
]
PRODUCT_URLS = [
    "https://www.swissmedic.ch/dam/swissmedic/de/dokumente/internetlisten/zugelassene_arzneimittel_ham_ind.xlsx.download.xlsx/Zugelassene_Arzneimittel_HAM.xlsx",
]
CURRENT: set = set()   # fetch() 填：包裝清單＋藥品清單的現行許可號；空的就不做「不在清單」判定
MIN_CURRENT = 5000     # 現行許可號少於這個數＝下載或格式有問題，不判定


def _download(urls=None):
    last = None
    for url in (urls or URLS):
        for attempt in range(3):
            try:
                r = requests.get(url, timeout=180, headers={"User-Agent": "Mozilla/5.0 (compatible; TxGNN/1.0; research)"})
                r.raise_for_status()
                if r.content[:2] == b"PK":
                    return r.content
                last = RuntimeError(f"{url} 回傳的不是 xlsx")
                break
            except Exception as e:
                last = e
                time.sleep(10 * (attempt + 1))
    raise last


def _day(v):
    if v is None:
        return None
    if hasattr(v, "strftime"):
        return v.strftime("%Y%m%d")
    s = str(v).strip()
    if s.lower().startswith("unbegrenzt"):
        return ""
    m = re.match(r"(\d{1,2})\.(\d{1,2})\.(\d{4})", s) or None
    if m:
        return f"{m.group(3)}{int(m.group(2)):02d}{int(m.group(1)):02d}"
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", s)
    return f"{m.group(1)}{m.group(2)}{m.group(3)}" if m else None


def fetch():
    ws = openpyxl.load_workbook(io.BytesIO(_download()), read_only=True).active
    head, out = None, []
    for row in ws.iter_rows(values_only=True):
        if head is None:
            if row and row[0] and str(row[0]).startswith("Zulassungs"):
                head = [str(x or "").split("\n")[0].strip().rstrip("*").strip() for x in row]
            continue
        rec = dict(zip(head, row))
        k = str(rec.get("Zulassungs-nummer") or "").strip()
        if k:
            out.append({"zulassung": k, "gueltig": _day(rec.get("Gültigkeitsdauer der Zulassung"))})
    if head is None or "Gültigkeitsdauer der Zulassung" not in head:
        raise RuntimeError(f"找不到表頭或有效期限欄：{head}")
    in_pack = {r["zulassung"] for r in out}
    prod = _fetch_products()
    out += [r for r in prod if r["zulassung"] not in in_pack]  # 只在藥品清單的許可號（沒有包裝列）
    CURRENT.clear()
    if prod and len(in_pack | {r["zulassung"] for r in prod}) >= MIN_CURRENT:
        CURRENT.update(in_pack | {r["zulassung"] for r in prod})
    return out


def _fetch_products():
    """藥品層級的現行許可清單；失敗回空清單（就不做「不在清單」判定，也不補藥品清單的期限）"""
    try:
        ws = openpyxl.load_workbook(io.BytesIO(_download(PRODUCT_URLS)), read_only=True).active
    except Exception as e:
        print(f"Zugelassene Arzneimittel HAM 下載失敗，不判定不在清單的許可號：{e}")
        return []
    head, out = None, []
    for row in ws.iter_rows(values_only=True):
        if head is None:
            if row and row[0] and str(row[0]).startswith("Zulassungs"):
                head = [str(x or "").split("\n")[0].strip().rstrip("*").strip() for x in row]
            continue
        rec = dict(zip(head, row))
        k = str(rec.get("Zulassungs-") or rec.get("Zulassungs-nummer") or "").strip()
        if k.isdigit():
            out.append({"zulassung": k, "gueltig": _day(rec.get("Gültigkeitsdauer der Zulassung"))})
    if head is None or "Gültigkeitsdauer der Zulassung" not in head:
        print(f"Zugelassene Arzneimittel HAM 找不到表頭或有效期限欄：{head}")
        return []
    return out


def confirmed_absent(lid):
    """給 license_refresh：兩份現行清單都沒有（而且清單有成功下載）＝確認已不是現行許可"""
    return bool(CURRENT) and str(lid).strip().isdigit() and str(lid).strip() not in CURRENT


def preprocess(bundle):
    """兩份現行清單都沒有的許可號標 cancelled（swissmedic_not_listed＝第一次發現日）；又出現的取消標記。有改回 True"""
    if not CURRENT:
        return False
    today = time.strftime("%Y-%m-%d")
    ch = False
    for r in (bundle.get("tfda") or {}).get("records") or []:
        lid = str(r.get("license_id") or "").strip()
        if not lid.isdigit():
            continue
        if lid in CURRENT:
            if r.get("swissmedic_not_listed"):
                r.pop("swissmedic_not_listed", None)
                r.pop("license_status", None)
                ch = True
        elif not r.get("swissmedic_not_listed"):
            r["swissmedic_not_listed"] = today
            r["license_status"] = "cancelled"
            ch = True
    return ch


def validate(new, old):
    p = []
    if len(new) < 8000:
        p.append(f"只解析出 {len(new)} 個包裝，疑似格式改變")
    bad = sum(1 for r in new if r["gueltig"] is None)
    if bad > 0.01 * max(1, len(new)):
        p.append(f"{bad} 筆有效期限無法解析")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    idx = {}
    for r in new:
        g = r["gueltig"]
        if g is None:
            continue
        cur = idx.get(r["zulassung"])
        # 無限期（""）最大；否則取最晚日期
        if cur is None or cur != "" and (g == "" or g > cur):
            idx[r["zulassung"]] = g
    return idx


def record_id(rec):
    return str(rec.get("license_id") or "").strip()


def update(rec, new):
    """只在狀態會翻轉時寫：新期限已過（→註銷），或原本寫了已過期限、現在清單上仍有效（→有效）。
    單純補上未來期限不算變動（意義沒變，也不改證據包）。"""
    today = time.strftime("%Y%m%d")
    old = re.sub(r"[^0-9]", "", str(rec.get("expiry_date") or ""))[:8]
    old_past = len(old) == 8 and old < today
    new_past = bool(new) and new < today
    if old_past == new_past:
        return False
    rec["expiry_date"] = new
    return True


# 2026-11-24（用戶決定「程式產生許可證表」）：每週排程（license_refresh_20261029.py 的 sync_tables 掛鉤）在概覽表同步之後，
# 依證據包把 Marktinformationen 段落的程式許可證表重排（scripts/sync_license_tables.py --bundles；只寫有變的頁）。
# PAGE_NOTE：排程 3b 自我檢查允許的非表格列（程式區塊標記、來源句、部分紀錄句、沒有紀錄的說明句）。
def _slt(site_dir):
    import importlib.util
    from pathlib import Path
    s = importlib.util.spec_from_file_location("sync_license_tables", Path(site_dir) / "scripts" / "sync_license_tables.py")
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def sync_tables(site_dir, bundles):
    """回傳 [(頁, 欄位, 前值, 後值)]；所有有證據包的頁都比對（只寫內容有變的），不只 bundles 列出的藥"""
    import difflib
    from pathlib import Path
    m = _slt(site_dir)
    drugs = Path(site_dir) / "docs" / "_drugs"
    before = {p.name: p.read_text(encoding="utf-8") for p in drugs.glob("*.md")}
    out = []
    for name in m.run(from_bundles=True):
        new = (drugs / name).read_text(encoding="utf-8")
        for l in difflib.unified_diff(before[name].split("\n"), new.split("\n"), lineterm="", n=0):
            if l[:1] in "+-" and not l.startswith(("+++", "---")) and l[1:].startswith("|"):
                out.append((name[:-3], "Zulassungstabelle (programmatisch)", l[1:] if l[0] == "-" else "", l[1:] if l[0] == "+" else ""))
    return out


try:
    import importlib.util as _ilu
    from pathlib import Path as _P
    _s = _ilu.spec_from_file_location("_slt_note", _P(__file__).resolve().parent / "sync_license_tables.py")
    _m = _ilu.module_from_spec(_s)
    _s.loader.exec_module(_m)
    PAGE_NOTE = _m.PAGE_NOTE
except Exception:  # 站上的 license_adapter 被母目錄當模組載入時，路徑一定在 scripts/ 下；這裡只防萬一
    PAGE_NOTE = r"^<!-- licenses:(begin|end) -->$"
