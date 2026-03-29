#!/usr/bin/env python3
"""處理瑞士 Swissmedic 藥品資料

從 Swissmedic 下載 XLSX 藥品清單並轉換為 JSON 格式。

使用方法:
    uv run python scripts/process_fda_data.py

資料來源:
    清單頁: https://www.swissmedic.ch/swissmedic/en/home/services/listen_neu.html
    直接下載: https://www.swissmedic.ch/dam/swissmedic/de/dokumente/internetlisten/zugelassene_packungen_human.xlsx.download.xlsx/zugelassene_packungen_ham.xlsx

產生檔案:
    data/raw/ch_fda_drugs.json
"""

import json
from pathlib import Path

import pandas as pd
import requests
import yaml


def load_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def download_swissmedic_data(output_path: Path) -> Path:
    """從 Swissmedic 下載藥品清單 XLSX

    Swissmedic 公開「Zugelassene Packungen HAM」(授權人用藥品包裝清單) XLSX。
    此 URL 於 2026-03 驗證可正確下載 3.1 MB XLSX 檔案。

    Args:
        output_path: XLSX 輸出路徑

    Returns:
        下載的檔案路徑
    """
    config = load_config()
    info_url = config["data_source"]["url"]

    print("正在嘗試從 Swissmedic 下載藥品清單 XLSX...")
    print(f"清單頁: {info_url}")
    print()
    print("注意: Swissmedic 的 XLSX 下載連結可能變動。")
    print("若自動下載失敗，請：")
    print(f"  1. 前往 {info_url}")
    print("  2. 下載「Zugelassene Packungen HAM」Excel 檔案")
    print(f"  3. 將 .xlsx 檔案放置於: {output_path}")

    # Swissmedic 的實際 XLSX 下載 URL
    # 2026-03 驗證有效，下載 3.1 MB XLSX
    # 注意: 路徑中的 "zugelassene_packungen_human" 與舊版 "zugelassene_packungen_ham" 不同
    xlsx_urls = [
        # 主要 URL（2026-03 驗證有效）
        "https://www.swissmedic.ch/dam/swissmedic/de/dokumente/internetlisten/zugelassene_packungen_human.xlsx.download.xlsx/zugelassene_packungen_ham.xlsx",
        # 備用 URL（舊版路徑）
        "https://www.swissmedic.ch/dam/swissmedic/de/dokumente/internetlisten/zugelassene_packungen_ham.xlsx.download.xlsx/zugelassene_packungen_ham.xlsx",
    ]

    last_error = None
    for xlsx_url in xlsx_urls:
        try:
            print(f"嘗試下載: {xlsx_url}")
            response = requests.get(xlsx_url, timeout=120, headers={
                "User-Agent": "Mozilla/5.0 (compatible; TxGNN/1.0; research)",
            })
            response.raise_for_status()

            # 確認是 XLSX 而非 HTML 錯誤頁
            content_type = response.headers.get("Content-Type", "")
            if "text/html" in content_type:
                print(f"  跳過: 伺服器回傳 HTML (Content-Type: {content_type})")
                continue

            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(response.content)

            file_size_mb = output_path.stat().st_size / 1024 / 1024
            print(f"下載完成: {output_path}")
            print(f"檔案大小: {file_size_mb:.1f} MB")

            # 基本驗證: XLSX (ZIP) 以 PK 開頭
            with open(output_path, "rb") as f:
                magic = f.read(4)
            if magic[:2] != b"PK":
                output_path.unlink(missing_ok=True)
                print("  跳過: 檔案不是有效的 XLSX (ZIP) 格式")
                continue

            return output_path
        except requests.RequestException as e:
            last_error = e
            print(f"  下載失敗: {e}")
            continue

    raise FileNotFoundError(
        f"需要手動下載 Swissmedic XLSX\n"
        f"請前往: {info_url}\n"
        f"下載「Zugelassene Packungen HAM」XLSX 檔案並存至: {output_path}\n"
        f"最後錯誤: {last_error}"
    )


def process_swissmedic_xlsx(xlsx_path: Path, output_path: Path) -> Path:
    """處理 Swissmedic XLSX 並轉換為 JSON

    使用 openpyxl 引擎讀取 Excel 檔案。

    Args:
        xlsx_path: XLSX 檔案路徑
        output_path: JSON 輸出路徑

    Returns:
        輸出檔案路徑
    """
    config = load_config()

    print(f"讀取 XLSX 檔案: {xlsx_path}")

    # Swissmedic XLSX 前幾列為標題/說明文字，實際欄位標題位於 row 5 (0-indexed)
    # 自動偵測表頭列：找到包含 'Zulassungs' 的列
    df_probe = pd.read_excel(
        xlsx_path, engine="openpyxl", dtype=str, sheet_name=0, header=None, nrows=15,
    )
    header_row = 5  # 預設值
    for i in range(min(15, len(df_probe))):
        row_vals = df_probe.iloc[i].astype(str).str.cat()
        if "Zulassungs" in row_vals and "nummer" in row_vals:
            header_row = i
            break
    print(f"  偵測到表頭列: row {header_row}")

    # 使用 openpyxl 引擎讀取 Excel，跳過元資料列
    df = pd.read_excel(
        xlsx_path,
        engine="openpyxl",
        dtype=str,
        sheet_name=0,  # 讀取第一個工作表
        header=header_row,
    )

    # 清理多行欄位名稱：只取第一行（德文名稱）
    df.columns = [c.strip().split("\n")[0].strip() for c in df.columns]

    # 移除全空白列（表頭上方的說明列有時殘留）
    df = df.dropna(how="all")

    print(f"原始資料筆數: {len(df)}")
    print(f"欄位: {', '.join(df.columns.tolist())}")

    # 清理資料
    df = df.fillna("")

    # 轉換為 JSON
    data = df.to_dict(orient="records")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"儲存至: {output_path}")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"完成！共 {len(data)} 筆藥品資料")

    # 顯示統計
    print_statistics(df, config)

    return output_path


def print_statistics(df: pd.DataFrame, config: dict):
    """印出資料統計"""
    fm = config["field_mapping"]
    status_field = fm["status"]
    ingredients_field = fm["ingredients"]

    print("\n" + "=" * 50)
    print("資料統計")
    print("=" * 50)

    if status_field in df.columns:
        print(f"\n註冊狀態分布:")
        status_counts = df[status_field].value_counts()
        for status, count in status_counts.items():
            print(f"  {status}: {count:,}")

    if ingredients_field in df.columns:
        with_ingredients = (df[ingredients_field] != "").sum()
        print(f"\n有活性成分: {with_ingredients:,} ({with_ingredients/len(df)*100:.1f}%)")


def main():
    print("=" * 60)
    print("處理瑞士 Swissmedic 藥品資料")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    raw_dir = base_dir / "data" / "raw"
    xlsx_path = raw_dir / "swissmedic_packungen.xlsx"
    output_path = raw_dir / "ch_fda_drugs.json"

    # 確保 raw 目錄存在
    raw_dir.mkdir(parents=True, exist_ok=True)

    # 尋找已下載的 XLSX
    if not xlsx_path.exists():
        existing_xlsx = list(raw_dir.glob("*.xlsx"))
        if existing_xlsx:
            xlsx_path = existing_xlsx[0]
            print(f"使用已存在的 XLSX 檔案: {xlsx_path}")
        else:
            download_swissmedic_data(xlsx_path)
    else:
        print(f"使用已存在的 XLSX 檔案: {xlsx_path}")

    # 處理 XLSX
    process_swissmedic_xlsx(xlsx_path, output_path)

    print()
    print("下一步: 準備詞彙表資料")
    print("  uv run python scripts/prepare_external_data.py")


if __name__ == "__main__":
    main()
