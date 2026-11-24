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


## 作用機轉段的資料來源與查核機制（2026-11-19）

用戶 2026-11-19 決定把 NZTxGNN 同日的作法推到各站（seo-ops 轉交：搜「<藥名> mechanism of action」落在藥物頁排名 30–99，因為頁面寫「作用機轉資料不可得」）。
2026-11-19 量測：本站公開藥物頁（排除 noindex、轉址頁）有 390 頁在正文章節寫這種句子（證據包 drugbank.source＝vocab_only、沒有作用機轉文字，AI 照實寫「沒有資料」；本站最常見的寫法：「Zum Wirkmechanismus liegen in den zusammengestellten Daten keine Angaben vor.」）。
作用機轉是藥物本身的基本藥理事實、不是模型預測，所以照查核機制補：每段都節錄官方仿單或資料庫原文、附可點的出處與取用日期，不自己寫。

- 來源（理由同 NZTxGNN/CLAUDE.md 同名一節）：美國 FDA 核准仿單（openFDA drug label，連結到 NLM DailyMed 同一份 SPL setid；FDA 仿單是美國政府公開資料），美國沒有仿單時用 ChEMBL drug mechanism 表（CC BY-SA 3.0）；證據包的 DrugBank 欄位只有 vocab，DrugBank 文字授權也不允許轉載，不用。
  2026-11-19 這次用 openFDA 的 drug label 全量下載檔（download.open.fda.gov，同一批資料，只留 human prescription 仿單；`--fda-bulk <目錄>`），不吃 API 每日 1,000 次配額；之後少量重跑可直接用 API（不給 `--fda-bulk`）。快取目錄各站共用。
- `scripts/build_mechanism_reviews.py --cache <目錄> [--fda-bulk <目錄>]`：掃公開頁正文章節（排除結論／下一步的待辦、安全性、摘要、總覽表、查核紀錄、免責聲明等）裡同時有「作用機轉」「資料」「沒有」字樣的短句（本站語言的字樣在檔內 L 的 KW／DATA／NEG／EXCL）→ 依 front matter monitor_inn（INN 另對 USAN，表在 US_NAME）查 openFDA，選仿單規則同 NZ：只用單一成分、主成分名（去鹽類；酯類要相同）跟本頁相同的處方藥仿單；排序全身給藥→節錄夠長→有 12.1→有品牌名→版本新；美國只有複方仿單的只節錄 12.1 裡講本藥成分的句子並寫明是複方；節錄照原文 2～4 句、不改寫。
  紀錄寫進 `docs/_data/drug_reviews.json`（action＝mechanism，id `ch-moa-<日期>-<藥>-1`，sources 附 url、accessed、excerpt、label_version、section、set_id 或 chembl_id）；仿單與 ChEMBL 都沒有的，列進 `docs/_data/drug_reviews_uncertain.json`（source＝mechanism of action，附原因）。已有紀錄或已列待查的頁不重抓。`--list` 只列仍寫「不可得」的頁。
- 替換句格式：本站語言（Deutsch）的出處句＋節錄的忠實翻譯（標明「非官方翻譯」）＋英文原文（照引、為準）＋DailyMed 連結、仿單版本、取用日期（用戶 2026-11-19 決定「當地語言摘要＋英文原文」）。只換「不可得」那一句（英文站句首子句後接 so／but 的後半句是 AI 推論，保留），不加框；查核紀錄表列原句與出處。模型預測與其他正文不動。
- 翻譯：節錄的翻譯是 AI 輔助的忠實翻譯（不增不減，藥名、基因與受體符號、數字、「[…]」照原文），2026-11-19 批次產生，存在紀錄 sources 的 translation（translation_lang、translation_note 註明非官方、英文原文為準）；頁面上同時列英文原文。`--translations <檔>` 讀翻譯、`--need <檔>` 列出還沒翻的節錄（這些頁那次不寫紀錄，gate 會擋，翻好再跑）。
- 2026-11-19 結果：347 頁寫入紀錄（美國仿單 314、ChEMBL 33），43 頁列待查（美國沒有單一成分處方藥仿單、仿單段落不是作用機轉，且 ChEMBL 沒有已核准分子的機轉紀錄；多是胺基酸、維生素、礦物質、賦形劑、生物製劑或只在別國上市的藥）。
- `scripts/apply_drug_reviews.py` 支援 mechanism；gate 第 21 項（`scripts/check_seo_docs.py`，函式在 build_mechanism_reviews.gate_errors）：公開頁仍寫「不可得」、既沒有 mechanism 紀錄也沒列待查的，擋下；有紀錄沒套上的由查核紀錄那一項擋。
- 注意：節錄的是美國仿單，劑型與適應症可能跟本站市場的產品不同（例如取到外用仿單）；文字上已寫明是美國 FDA 核准仿單。`sync_notes_to_docs.py` 整頁重寫後會重套紀錄（claim 是頁面原句）；報告重產、原句改寫後要再跑 build_mechanism_reviews.py。
- 2026-11-20 補做：程式更新：同頁不只一句「不可得」時每句各一筆紀錄（-1、-2…）；同頁別筆紀錄的更正文字、錨點與已套上的節錄不再當成「不可得」句；gate 改成公開頁仍寫「不可得」、又沒列待查就擋（不再只看該頁有沒有紀錄）；同頁第二句起補 17 筆紀錄（id 結尾 -2）；ChEMBL 譯文（詞組清單）後補句號 33 筆；同 id 重發，前版 replacement 存 history。
- 2026-11-20 試跑母目錄「交付前驗證」規則時補做：偵測改成原條件不動、另加新增寫法（L2，比中的再用 NOT 排除以缺資料為前提的模型推論），字樣用獨立、更寬的偵測全量掃出的候選句逐句標註校準（A 沒有漏、B 沒有誤中）；偵測漏抓的「不可得」句補 4 筆紀錄、2 頁列待查；節錄後面接著 AI 說明「上面描述依據」的句子（會讀成美國仿單的出處）20 筆改成那句在節錄前（原文不改，只換順序）；同頁重複引用同一段節錄的 17 筆改成指向上方節錄的一句（附同一個來源連結）；以上同 id 重發，前版存 history。程式另加 reorder_src_tail、同頁已引用同一段節錄時改指向上方（產生器 txgnn/.claude/moa_rollout_20261119/fix_20261120/）。

## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。

## 許可證表與正文張數由程式產生（2026-11-24）

用戶 2026-11-24 決定（各站同日；本站做表＋B）：每週許可證排程只改概覽表狀態列／張數列，AI 寫在市場段落的許可證表（沒有狀態欄）與正文張數句跟著 Swissmedic 清單過期；改成程式產生、每週自動同步。範本 DETxGNN 同名程式。
- A. 程式許可證表：`scripts/sync_license_tables.py`。標題含「Marktinformationen」的段落（本站多數是三級標題「### Marktinformationen Schweiz」，少數二級；段落到下一個同級或更高級標題）裡的第一張許可證表（表頭含 Zulassung）換成程式依證據包產生的表
  「| Zulassungsnummer | Produktname | Kategorie (Heilmittelcode) | Anwendungsgebiet (Swissmedic) | Status |」：一張許可一列（同號多個包裝取第一筆，同 reviewer._local_regulatory 去重；同許可另有品名／劑量時加「(+N weitere Bezeichnung[en])」）；
  舊表「Darreichungsform」欄放的其實是 Swissmedic 的 Heilmittelcode（Synthetika、Biotechnologika…），照實改名；狀態＝事實層（Gültig／Erloschen：效期已過或兩份現行清單都不列）；有效在前、依許可號；
  證據包只收了部分包裝（partial）時表下加「Die ausgewerteten Daten enthalten nur einen Teil der Packungen …」；表後來源句；沒有紀錄時一句 NONE_LINE。前後 `<!-- licenses:begin -->`／`<!-- licenses:end -->`。
  段落裡沒有表的頁補在標題下；「Grundlegende Informationen」（noindex 頁的概覽表）與「Bekannte Anwendungen und Marktstatus」段落不放。
  快照 `snapshots/ch_licenses.json.gz` 另存 rows／total／partial（`scripts/build_license_snapshot.py` 用 rows_of）；gate 第 18 項（src/chtxgnn/regulatory/licenses.py＋sync_license_tables.block_problems）擋「有 Marktinformationen 段落卻沒有程式區塊」「程式區塊≠快照重算」。
  licenses.py 的市場段落 2026-11-24 起也認三級標題（之前只認二級，484 頁的表格號碼與列狀態漏驗；改後改前都是 0 項問題）。
  每週排程由 `scripts/license_adapter.py` 的 `sync_tables`（--bundles）重排，`PAGE_NOTE` 讓 3b 自我檢查接受區塊標記與說明句。
- B. 正文張數改寫：`scripts/rewrite_license_counts.py`＋`src/chtxgnn/regulatory/count_prose.py`（從 DETxGNN 移植；本站範圍是 Swissmedic，「Schweiz／Swissmedic」不算保留，EMA／EU／Deutschland／FDA 才算；
  另補「X der Y Zulassungen」「… und N gelöscht」、「alle N … gültig」數字對得上有效數但有效≠總數時列 premise、改完變成「fünf der fünf」列 grammar）。單方／複方句不動（事實層單方張數用「;;」切成分，本站成分欄是「, 」，算不準）。
  partial 頁（141 頁）整頁不動。不寫查核框；gate 第 22 項擋「再跑一次會變」。
- 誰會跑：`scripts/apply_drug_reviews.py`（非 --check）結尾依快照跑 A、B；`scripts/build_license_snapshot.py` 寫完快照再跑一次（`--no-rewrite` 不跑）。
- 2026-11-24 套用（資料 data-20261117-090726）：程式表 576 頁（公開頁 627 頁中有 Marktinformationen 段落的全部：AI 表 564 頁取代、段落裡沒有表的 12 頁補上；noindex 192 頁只有概覽段落、不放；51 個公開頁沒有市場段落），
  表上 65 列 Erloschen（51 頁）；正文張數程式改寫 0 句、判斷不了 0 句（本站正文多是「mindestens N」「Die Liste kann unvollständig sein」這類保留句與 partial 頁）。被取代的表上沒有錨著的查核紀錄（沒有 superseded）。
  另寫的寬偵測（同句有 Zulassung 與數字或全稱字樣、跟事實層不符）全量掃公開頁：找到 4 句在 partial 頁、說「全部有效」或張數跟 11-17 標註的不在清單許可相反（azithromycinum、bisoprololi_fumaras、metoprololi_tartras、ticagrelorum），
  以 4 筆 `ch-lic-20261124-*` 更正；複查剩 2 句都是誤中（sapropterin「bereits eine Zulassung besteht」講適應症、topotecan 依持有人拆分的張數正確）。checker 全量前後都是 0；gate exit 0；正文有變的 576 頁 last_modified_at 改 2026-11-24。
- 母目錄 `.claude/license_labels/CHTxGNN.json` 只有「Gültig」，程式表會寫「Erloschen」，要加 `"Erloschen": "cancelled"`（母目錄的檔，本站不改）。

## 第二輪：舊錯句、劑型說法與紀錄說明的張數（2026-11-24）

用戶 2026-11-24 第二輪決定（程式許可證表與正文張數改寫上線後，處理程式管不到的舊錯句）。本站第一輪沒有列進待查的 open 項目，所以逐類全量掃（證據包 data-20261117-090726、快照事實層）：
- 有效 0 張的公開頁（chloramphenicol、phenol、aliskiren、bezlotoxumab、reboxetin、ritonavir）正文說「在瑞士核准／在市」的：chloramphenicol（摘要「ist in der Schweiz als Augentropfen … zugelassen」、結論「bereits zugelassenen Anwendung」）、phenol（摘要「ist in der Schweiz … zugelassen」）以 3 筆 `ch-lic-20261124b-*` 改成過去式並註明許可已不在現行清單（依成分對現行清單 0 個產品，11-17 已查）；其他 4 頁寫法本來就跟事實一致。
- 市場段落句子對事實層：docetaxel「Mindestens sieben … gültig」（53262、62120 已不在現行清單）、tamsulosin「davon 7 gültig」（57160、57637）更正；寬偵測（有註銷的頁說「alle／beide … gültig」、全部有效的頁說已失效）全量複查 0 句。
- 單方／複方：dextromethorphan「alle … einzigem Wirkstoff」不成立（41799 Vicks Medinait 是複方），併進 11-17 那筆同 id 重發；其他 Einzel／Kombination 說法逐句對證據包成分欄都成立。
- 劑型／成分說法全站掃（「als Tablette／Augentropfen … im Handel」「nur … zugelassen」64 句）逐句對證據包全部品項的產品名：scopolamini_butylbromidum「in einer Augentropfen-Zubereitung」不成立（29804 Scopolamine Dispersa 的成分是 scopolamini hydrobromidum），以 1 筆紀錄更正；其餘成立、不改。29804 被收進 butylbromide 的證據包與程式表（drug_mapping 依 DrugBank ID 對到），是收集規則的事，沒動。
- 紀錄說明樣板（site_config `T["figures"]`）改成不寫數字；既有紀錄沒有用到它。更正文字寫死張數或舊表筆數的 6 筆（azathioprinum、dextromethorphanum、azithromycinum、bisoprololi_fumaras、metoprololi_tartras、ticagrelorum）同 id 重發，改成指向程式表，哪張失效的事實保留，前版存 history。
- partial 頁市場段落裡跟程式表說明句「Die ausgewerteten Daten enthalten nur einen Teil …; die Liste kann unvollständig sein.」重複的 AI 保留句（只講「清單可能不完整」＋「mindestens N Zulassungen」的句子，與緊鄰的單純筆數句）：比照第一輪移除舊表說明句的做法直接刪掉，不寫查核框，69 頁 73 句（工具在 scratchpad CHTxGNN-r2/tools/dedup_partial.py）。含狀態或其他事實的句子（「Alle aufgeführten Zulassungen sind gültig」「davon 9 gültig und 4 gelöscht」等）、查核紀錄文字所在的句子、後一句以 Davon 承接的（paroxetine）不動，約 30 頁仍有重複意思的保留句。
- checker 全量前後都是 0；gate exit 0。

## 第三輪：證據包收錯的有效成分、缺市場段落的公開頁（2026-11-24）

用戶 2026-11-24 第三輪決定（證據包 data-20261117-090726）：
- A. 證據包收錯的品項：collectors/chfda.py 依 drug_mapping.csv 的 DrugBank ID 收許可證，同一個 ID 底下的另一個有效成分（不是本藥的鹽類、酯類或前驅藥，而是另一個分子）會被收進來，例：scopolamini_butylbromidum 收到 29804 Scopolamine Dispersa（scopolamini hydrobromidum，眼藥水；兩者都對到 DB00747）。
  排除規則在 `config/bundle_record_exclusions.json`（每條附 reason、basis）：證據包名在規則的 bundles 裡，紀錄成分欄（「, 」分隔）有一段符合 family、卻沒有一段符合 keep 就排除；`src/chtxgnn/regulatory/record_exclusions.py` 判定，
  `scripts/exclude_mismatched_records.py` 把已有證據包的這些紀錄移到 `tfda.excluded_records`（附 excluded、excluded_reason、excluded_basis；total_matches 扣掉；可重複執行），collectors/chfda.py 收集時也照同一份規則；
  `.github/workflows/license-refresh.yml` 在 license_refresh 前先跑（有移出就照常發新 Release）。
  全站掃（成分欄跟證據包名第一個字同字根、其餘不同的配對 482 組逐組看）收進規則的 13 條、17 個證據包、113 筆紀錄：scopolamine butylbromide／hydrobromide 互收、trastuzumab 與 T-DM1／T-DXd 三向互收、povidone K 25／povidone-iodine 互收、
  phenol 與 formaldehyde 收到 Tannosynt（苯酚—苯酚磺酸—甲醛—尿素縮合物）、icosapent ethyl／telotristat ethyl 互收（DB13259 錯配）、fluticasone furoate／propionate 互收。
  不收的（同一分子的鹽類、酯類或前驅藥，或同一激素的不同製程）：amantadine 鹽、diclofenac 鹽、各種 steroid 酯（methylprednisolone、prednisolone、hydrocortisone、dexamethasone、triamcinolone）、tenofovir／disoproxil／alafenamide 對 tenofovirum、follitropin alfa／beta／delta、zincum 各種鹽（離子類）。
  公開頁受影響 5 頁（scopolamini_butylbromidum、trastuzumabum、povidonum_k_25、phenol、formaldehyde）：程式表、概覽狀態列／張數列照新證據包同步（phenol 變成 0 張「keine Zulassung erfasst」）；正文矛盾以 `ch-lic-20261124c-*` 9 筆（7 correct、2 annotate）更正、
  `ch-lic-20261124b-phenol-1`、`-scopolamini_butylbromidum-1` 同 id 重發（前版存 history）：摘要的「Tannosynt＝Phenol／Formaldehyd」「也有消毒乳膏」、概覽表原適應症裡別的成分的 Swissmedic 適應症（Mydriatikum、Wunddesinfektion、Enhertu／Kadcyla 的適應症、Tannosynt 的皮膚病）；
  phenol、formaldehyde 的模型推論段以原適應症為前提，原文不改、加註。front matter description 的「Ursprüngliche Indikation: Entzündliche…」（phenol、formaldehyde）沒有紀錄機制可改，未動（待決定）。
- B. 公開頁沒有 Marktinformationen 段落、證據包卻有紀錄的 51 頁：`scripts/sync_license_tables.py` 的 add_section 在「Sicherheitshinweise」（同級標題；沒有就 Fazit und nächste Schritte、Haftungsausschluss）之前補「Marktinformationen Schweiz」段落放程式表、段落後一行「---」；
  noindex 頁與 0 筆紀錄的頁不補。gate 第 18 項（block_problems）擋「公開頁有證據包紀錄卻沒有市場段落」；license_adapter 的 PAGE_NOTE 放行新標題行與「---」。51 頁正文沒有跟新表矛盾的句子；last_modified_at 改 2026-11-24。
- checker 全量前後都是 0；gate exit 0。
