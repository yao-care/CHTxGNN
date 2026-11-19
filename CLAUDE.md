# CHTxGNN - Claude CLI 使用指引

本 repo 的維運以母 repo（yao-care/txgnn）CLAUDE.md 為準；本檔只記本站自己的機制。

---

## 藥物頁查核機制（2026-11-12 起）

用戶 2026-11-12 決定：30 站各有自己的查核機制，核心流程比照 TwTxGNN（Tw 的 CLAUDE.md「藥物頁人工查核紀錄」兩節）與 UsTxGNN（第一個試做站）。
本站的規則與程式都在本 repo，頁面上的查核框與查核紀錄表用德文，依據是 Swissmedic 核准包裝清單（zugelassene Packungen）；在地字樣集中在 `src/chtxgnn/regulatory/site_config.py`。

| 環節 | 本站檔案 | 說明 |
|------|----------|------|
| 查核紀錄 | `docs/_data/drug_reviews.json` | 單一真實來源，欄位同 Tw（correct／annotate／rereview／rereview_result／header_level／description_level、history、status） |
| 套用 | `scripts/apply_drug_reviews.py` | 套到 `docs/_drugs/*.md`：查核框 `<!-- review:begin id -->`、免責聲明前的查核紀錄表；可重複執行；`--check` 只檢查、`--touch` 連 last_modified_at 一起改 |
| 頁首等級 | `src/chtxgnn/regulatory/page_format.py` | 頁首＝Quick Overview 等級格的**第一個**等級（主預測）；這是本站產線原本的行為（2026-11-12 實測，見 site_config 的 HEADER_RULE_NOTE），不照 Tw 整格取最高。頁首 N/A 且沒有預測的頁不重算 |
| 撤回預測 | `src/chtxgnn/regulatory/withdrawn.py` | verdict=withdraw 的預測不進證據監測（`scripts/extract_drug_list.py`）、搜尋索引與 FHIR（母目錄 `.claude/rebuild_search_index.py`、`.claude/sync_fhir_levels.py` 會讀本站這支） |
| 許可證 | `snapshots/ch_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/chtxgnn/regulatory/licenses.py` | 本站沒有程式產生的許可證表；gate 依快照驗市場段落表格的號碼屬於本藥、狀態列與張數列＝事實層、表格列狀態不跟事實相反 |
| 刪改轉紀錄 | `scripts/reviews_from_edits.py` | 依 git 前後版本（或改寫前後目錄）把正文刪改轉成 correct 紀錄；site_config 的 COMMITS／REGEN_COMMITS 是 2026-10-31～11-06 的刪改與 AI 重產提交 |
| 待查清單 | `docs/_data/drug_reviews_uncertain.json`、`scripts/check_original_indications.py` | 原適應症交叉驗證，只列待查、不改頁面 |
| gate | `scripts/check_seo_docs.py` 第 17–20 項 | 紀錄都已套用、許可證＝快照、頁首＝主預測等級、撤回預測沒有對外發布 |

原則（同 Tw）：基本事實照主管機關資料更正；模型預測原文不刪不改寫，只加註；證據等級與決策只經重審（rereview → rereview_result）變更。

改頁之後要跑：

```bash
python3 scripts/apply_drug_reviews.py          # 重套查核紀錄（sync_notes_to_docs.py、每週許可證排程結尾都會自動跑）
python3 scripts/build_license_snapshot.py --ws <工作目錄>   # 證據包或事實層變了才要（每週排程會自動跑）
python3 scripts/check_seo_docs.py              # 必須 exit 0
```

本站 2026-10-31～11-06 沒有刪改正文許可證子句的提交（許可證矛盾句掃描結果為 0 頁），所以紀錄從 0 筆開始；之後的更正、加註、重審都記在 `docs/_data/drug_reviews.json`。
原適應症交叉驗證 2026-11-12 列了 2 頁待查（alglucosidase_alfa、metamizole）：兩頁的原適應症跟 Swissmedic 資料一致，只是資料的適應症欄是法文或義大利文（Maladie de Pompe、Analgesico），德文詞組比不到；留在待查清單，人工對照後標 resolved。

## 新資料查不到的許可證（2026-11-17）

每週排程原本把「包裝清單（Zugelassene Packungen HAM）查不到」的許可號保留原狀態，CH 每週都因同一批 91 張超過 2% 開 issue。
2026-11-17 用戶要求確認實際狀態：下載 Swissmedic 全部現行清單逐號比對——20 張在藥品清單（Zugelassene Arzneimittel HAM）有、
包裝清單沒有，仍是現行許可；71 張 2026-03 的包裝清單還在、11 月所有現行清單都沒有（35 張效期已過，36 張效期未到但已撤回／放棄）。
- `scripts/license_adapter.py` 另下載藥品清單：只在藥品清單的號照它的有效期限算；兩份都沒有的號由 preprocess 標
  `license_status: cancelled`＋`swissmedic_not_listed`（第一次發現日），又出現在清單就取消；任一清單下載失敗不判定。
  `confirmed_absent()` 讓排程把這些列成「主管機關現行清單確認已不列」，不算「查不到」、不開 issue（母目錄 license_refresh 的掛鉤）。
- 48 頁狀態列／張數列照事實層同步；正文寫「全部有效」而相反的 3 頁以 `ch-lic-20261117-*` 更正；全部註銷的 4 頁依成分確認
  （bezlotoxumab、chloramphenicol、phenol 現行 0 個產品；ritonavir 單方 0、複方 Paxlovid／Kaletra 糖漿仍在）。
- 同日另修：pheniramine 正文主題跟主預測不一致（重產報告）；6 個公開頁補 FHIR（front matter 補 drugbank_id）、2 個藥刪掉不在 kept 的 ClinicalUseDefinition。


## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。
