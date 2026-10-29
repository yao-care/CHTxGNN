"""CH（Swissmedic）許可證下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：Swissmedic「Zugelassene Packungen」人用藥清單 xlsx（免金鑰；網址沿用站上 process_fda_data.py，兩個備用網址）。
清單只列現行許可的包裝、沒有狀態欄，但有「Gültigkeitsdauer der Zulassung」（許可有效期限，unbegrenzt＝無限期）。
寫回：只在狀態會翻轉時改紀錄的 expiry_date（YYYYMMDD；無限期寫空字串），status 不動（保持空白）。
reviewer 在 status 空白時以 expiry_date 判定：已過期算註銷。清單裡沒有的許可號保留原狀態（不推定為註銷）。
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


def _download():
    last = None
    for url in URLS:
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
    return out


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
