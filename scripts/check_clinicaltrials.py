#!/usr/bin/env python3
"""
Check ClinicalTrials.gov for new clinical trials related to our drug list.
Creates GitHub Issues when new trials are found.

NOTE: Filters out known/approved indications to focus on repurposing evidence.
"""

import json
import os
import re
import time
from datetime import datetime, timedelta
from pathlib import Path

import requests

from github_utils import create_issue, close_older_clinicaltrials_issues


# 2026-11-03：已核准用途排除改成嚴格比對。原本的關鍵字比對會誤殺（例如 amlodipine 的
# pulmonary hypertension 因為 hypertension 被排除）；現在只認兩種情形：
#   1. 正規化後名稱完全相同
#   2. 一方是另一方前後加上限定詞（type 2、subtype A、form、variant 等）
# approved_indication 是 extract_drug_list.py 輸出的「; 」分隔已知適應症（英文疾病名）。
_QUALIFIER_WORDS = {"type", "subtype", "form", "variant", "group", "class", "grade", "stage"}


def _norm_indication(name: str) -> list:
    name = re.sub(r"\((disease|disorder)\)", " ", (name or "").lower())
    return re.sub(r"[^\w]+", " ", name).split()


def _is_qualifier(words: list) -> bool:
    # 限定詞要以 type／subtype 等字開頭（"type 2"、"subtype a"）；單獨的字母不算（hepatitis b ≠ hepatitis）
    return bool(words) and words[0] in _QUALIFIER_WORDS and all(
        w in _QUALIFIER_WORDS or re.fullmatch(r"\d+[a-z]?|[ivx]+|[a-z]", w) for w in words)


def _same_or_qualified(a: list, b: list) -> bool:
    if a == b:
        return True
    short, long_ = (a, b) if len(a) < len(b) else (b, a)
    if not short or len(short) == len(long_):
        return False
    n = len(short)
    for i in range(len(long_) - n + 1):
        if long_[i:i + n] == short and _is_qualifier(long_[:i] + long_[i + n:]) \
                and (i == 0 or i + n == len(long_)):
            return True
    return False


def is_known_indication(approved_indication: str, predicted_indication: str) -> bool:
    """Is the predicted indication one of the drug's known (approved) indications?

    Strict match against each '; '-separated known indication: identical after
    normalization, or one is the other plus a qualifier (e.g. 'type 2', 'subtype A').
    """
    if not approved_indication or not predicted_indication:
        return False
    pred = _norm_indication(predicted_indication)
    return any(_same_or_qualified(pred, _norm_indication(k))
               for k in re.split(r"[;；]", approved_indication) if k.strip())

# Configuration
API_BASE = "https://clinicaltrials.gov/api/v2/studies"
CACHE_FILE = Path(__file__).parent.parent / "data" / "cache" / "clinicaltrials_cache.json"
DRUG_LIST_FILE = Path(__file__).parent / "drug_list.json"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPO = os.environ.get("GITHUB_REPOSITORY", "yao-care/EuTxGNN")
RATE_LIMIT_DELAY = 0.5  # seconds between API calls
DAYS_BACK = 7  # 查詢窗：LastUpdatePostDate 在這幾天內；其中 StudyFirstPostDate 也在窗內的才算新試驗


def load_cache() -> dict:
    """Load the cache of previously seen trial IDs."""
    if CACHE_FILE.exists():
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"last_check": None, "seen_trials": {}}


def save_cache(cache: dict):
    """Save the cache."""
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    cache["last_check"] = datetime.now().isoformat()
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)


def load_drug_list() -> list:
    """Load the drug list."""
    with open(DRUG_LIST_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["drugs"]



# --- 試驗與藥物的關係必須是結構化的介入角色（JpTxGNN #26713）---
# query.term 全文搜尋會把只在描述中提到藥名的試驗（例：安慰劑用的生理食鹽水、AI 工具研究）
# 也當成該藥的新試驗。改用 query.intr，並要求藥名出現在介入措施名稱／別名、且不是安慰劑組。
_SALTS = {"hydrochloride", "hcl", "sodium", "potassium", "calcium", "sulfate", "sulphate", "maleate", "fumarate",
          "tartrate", "citrate", "acetate", "mesylate", "besylate", "succinate", "phosphate", "bromide", "chloride"}


def _norm_name(text) -> str:
    import unicodedata
    t = unicodedata.normalize("NFKD", str(text or "")).encode("ascii", "ignore").decode().lower()
    return " ".join("".join(c if c.isalnum() else " " for c in t).split())


def _role_bound(study: dict, drug_name: str) -> bool:
    full = _norm_name(drug_name)
    core = " ".join(w for w in full.split() if w not in _SALTS) or full
    ivs = (study.get("protocolSection", {}).get("armsInterventionsModule", {}) or {}).get("interventions", []) or []
    for iv in ivs:
        name = _norm_name(iv.get("name", ""))
        if "placebo" in name:
            continue
        text = " " + " ".join([name] + [_norm_name(n) for n in (iv.get("otherNames") or [])]) + " "
        if (full and f" {full} " in text) or (core and f" {core} " in text):
            return True
    return False

def _clean_condition(name: str) -> str:
    name = re.sub(r"\s*\((disease|disorder)\)\s*", " ", name, flags=re.I)
    return re.sub(r"\s+", " ", name).strip().replace('"', "")


def trial_hits(trial: dict, indications: list) -> list:
    """試驗的 condition 直接對到哪些預測新適應症（原 issue 內文「Matched predicted indication」的比對）。"""
    conds = [c for c in trial.get("protocolSection", {}).get("conditionsModule", {}).get("conditions", []) if c.strip()]
    return [i for i in (indications or [])
            if any(_clean_condition(i).lower() in c.lower() or c.lower() in _clean_condition(i).lower() for c in conds)]


def first_posted(trial: dict) -> str:
    """StudyFirstPostDate（YYYY-MM-DD 或 YYYY-MM）；沒有就回傳空字串。"""
    status = trial.get("protocolSection", {}).get("statusModule", {})
    return (status.get("studyFirstPostDateStruct") or {}).get("date", "")


def search_trials(drug_name: str, days_back: int = 7, conditions: list = None) -> list:
    """Search for trials updated in the last N days.

    2026-10-16：conditions 給預測新適應症時，只抓「藥＋這些疾病」的試驗。
    """
    min_date = (datetime.now() - timedelta(days=days_back)).strftime("%Y-%m-%d")

    params = {
        "query.intr": drug_name,
        "filter.advanced": f"AREA[LastUpdatePostDate]RANGE[{min_date},MAX]",
        "pageSize": 50,
        "fields": "NCTId,BriefTitle,OverallStatus,Phase,EnrollmentCount,Condition,LastUpdatePostDate,StudyFirstPostDate,InterventionName,InterventionType,InterventionOtherName"
    }
    # ClinicalTrials.gov 對過長片語回 400「Too complicated query」：略過超過 6 個字的疾病名
    conds = [f'"{_clean_condition(c)}"' for c in (conditions or [])
             if len(_clean_condition(c)) > 3 and len(_clean_condition(c).split()) <= 6]
    if conditions and not conds:
        return []
    if conds:
        params["query.cond"] = " OR ".join(conds)

    try:
        response = requests.get(API_BASE, params=params, timeout=30)
        if response.status_code == 400 and len(conds) > 3:
            params["query.cond"] = " OR ".join(conds[:3])
            response = requests.get(API_BASE, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        return [s for s in data.get("studies", []) if _role_bound(s, drug_name)]
    except requests.RequestException as e:
        print(f"Error searching trials for {drug_name}: {e}")
        return []


ROLE_PATTERNS = [
    (r"refractory|relapsed|after failure|inadequate response|switch(ing)? (from|to)|prior (therapy|treatment)|resistant to", "drug may be prior/frontline therapy, not the tested intervention"),
    (r"conditioning|myeloablative|transplant", "drug may be used as transplant conditioning"),
    (r"versus|vs\.?|compared with|comparator", "comparative study — check whether the drug is the comparator arm"),
]


def _role_flags(text: str) -> str:
    """N-02：標出需要人工判讀藥物角色的試驗（以標題關鍵字判斷，僅供提示）。"""
    t = (text or "").lower()
    return "; ".join(msg for pat, msg in ROLE_PATTERNS if re.search(pat, t))


def create_github_issue(drug_name: str, new_trials: list, indications: list = None):
    """Create a GitHub Issue for new trials found."""
    indications = indications or []
    ind_label = "; ".join(indications[:2]) + (" …" if len(indications) > 2 else "")
    title = f"🔬 新臨床試驗：{drug_name} ({len(new_trials)} 筆)"
    if ind_label:
        title += f" → {ind_label}"  # 接在數量後面，github_utils 以「：…(」擷取藥名才對得上

    if not GITHUB_TOKEN:
        print(f"[DRY RUN] Would create issue for {drug_name} with {len(new_trials)} new trials")
        for trial in new_trials[:3]:
            nct_id = trial.get("protocolSection", {}).get("identificationModule", {}).get("nctId", "Unknown")
            brief_title = trial.get("protocolSection", {}).get("identificationModule", {}).get("briefTitle", "Unknown")
            print(f"  - {nct_id}: {brief_title[:60]}...")
        return

    # Close older issues for this drug before creating a new one
    closed_count = close_older_clinicaltrials_issues(drug_name)
    if closed_count > 0:
        print(f"  → Closed {closed_count} older issue(s) for {drug_name}")

    # Format trial details
    trial_details = []
    for trial in new_trials:
        protocol = trial.get("protocolSection", {})
        id_module = protocol.get("identificationModule", {})
        status_module = protocol.get("statusModule", {})
        design_module = protocol.get("designModule", {})

        nct_id = id_module.get("nctId", "Unknown")
        brief_title = id_module.get("briefTitle", "Unknown")
        status = status_module.get("overallStatus", "Unknown")
        phase = ", ".join(design_module.get("phases", ["Unknown"]))
        enrollment = design_module.get("enrollmentInfo", {}).get("count", "Unknown")

        conds = protocol.get("conditionsModule", {}).get("conditions", [])
        hit = trial_hits(trial, indications)
        role = _role_flags(brief_title)
        trial_details.append(
            f"### {nct_id}\n"
            f"- **Title**: {brief_title}\n"
            f"- **Conditions**: {'; '.join(conds) if conds else '-'}\n"
            f"- **First posted**: {first_posted(trial) or '-'}\n"
            f"- **Matched predicted indication**: {'; '.join(hit) if hit else '(no direct condition match)'}\n"
            + (f"- **⚠ Role flag**: {role}\n" if role else "")
            + f"- **Status**: {status}\n"
            f"- **Phase**: {phase}\n"
            f"- **Enrollment**: {enrollment}\n"
            f"- **Link**: https://clinicaltrials.gov/study/{nct_id}\n"
        )

    body = f"""## 🔬 New Clinical Trials Detected

This issue was automatically created by GitHub Actions.

### Drug Name
{drug_name}

### Predicted New Indication(s)
{chr(10).join("- " + x for x in indications) if indications else "-"}

### NCT IDs
{", ".join(t.get("protocolSection", {}).get("identificationModule", {}).get("nctId", "") for t in new_trials)}

### Data Source
ClinicalTrials.gov

### Evidence Type
New Clinical Trials (first posted in the last 7 days)

### Details
Found **{len(new_trials)}** new clinical trials:

{"".join(trial_details)}

### Suggested Actions
- [ ] Review trial details
- [ ] Evaluate if drug report evidence level needs updating
- [ ] Add trial information to report

---
*Auto-detected at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC*
"""

    # Create the issue with deduplication check
    labels = ["auto-detected", "needs-review", "clinicaltrials"]
    create_issue(title, body, labels)


def main():
    print("=" * 60)
    print("ClinicalTrials.gov Evidence Checker")
    print("(Filtering out known/approved indications)")
    print(f"Started at: {datetime.now().isoformat()}")
    print("=" * 60)

    # Load data
    cache = load_cache()
    drugs = load_drug_list()

    print(f"Loaded {len(drugs)} drugs from drug list")
    print(f"Last check: {cache.get('last_check', 'Never')}")

    # Check each drug
    new_findings = []
    seen_trials = cache.get("seen_trials", {})
    min_first_posted = (datetime.now() - timedelta(days=DAYS_BACK)).strftime("%Y-%m-%d")
    skipped_known = 0

    for i, drug in enumerate(drugs):
        drug_name = drug["name"]
        predicted_indication = drug.get("predicted_indication", "")
        approved_indication = drug.get("approved_indication", "")

        # 2026-11-03：不再因第一個預測是已知適應症就整個藥跳過；改在下面逐一排除

        print(f"\n[{i+1}/{len(drugs)}] Checking: {drug_name}")

        predicted = drug.get("predicted_indications") or []
        # 2026-11-03：逐一排除和已核准用途重疊的預測（approved_indication 由 extract_drug_list.py 提供）
        if approved_indication:
            predicted = [x for x in predicted if not is_known_indication(approved_indication, x)]
            if not predicted:
                skipped_known += 1
                continue
        if not predicted or not drug.get("inn"):
            continue
        trials = search_trials(drug["inn"], days_back=DAYS_BACK, conditions=predicted)
        time.sleep(RATE_LIMIT_DELAY)

        if not trials:
            continue

        # Filter to truly new trials
        drug_seen = seen_trials.get(drug_name, [])
        is_initial_discovery = not drug_seen  # First time checking this drug
        new_trials = []

        for trial in trials:
            nct_id = trial.get("protocolSection", {}).get("identificationModule", {}).get("nctId")
            if nct_id and nct_id not in drug_seen:
                new_trials.append(trial)
                drug_seen.append(nct_id)

        if new_trials:
            # Skip issue creation for initial discovery (first time seeing this drug)
            if is_initial_discovery:
                print(f"  Initial discovery: {len(new_trials)} trials (baseline established)")
            else:
                # 2026-11-03：只有「首次刊登」在查詢窗內的才算新試驗；舊試驗只是更新（LastUpdatePostDate）
                # 不開 issue，NCT 照樣記進 cache。
                fresh = [t for t in new_trials if first_posted(t) >= min_first_posted]
                hits = [x for x in predicted if any(x in trial_hits(t, predicted) for t in fresh)]
                if len(fresh) < len(new_trials):
                    print(f"  {len(new_trials) - len(fresh)} updated older trial(s) - cache only")
                # Skip if only 1 trial - wait for more evidence
                if len(fresh) < 2:
                    print(f"  Only {len(fresh)} newly posted trial(s) - below threshold")
                # 至少一筆試驗的 condition 直接對到目前的預測新適應症才開 issue
                elif not hits:
                    print(f"  {len(fresh)} new trials, none directly matches a predicted indication - cache only")
                else:
                    print(f"  Found {len(fresh)} new trials!")
                    new_findings.append({
                        "drug": drug_name,
                        "trials": fresh,
                        "indications": hits,
                    })

        # Update seen trials
        seen_trials[drug_name] = drug_seen

    # Update cache
    cache["seen_trials"] = seen_trials
    save_cache(cache)

    # Create issues for new findings
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"Skipped (known indications): {skipped_known}")

    if new_findings:
        print(f"New findings: {len(new_findings)}")
        print("\nCreating Issues...")
        for finding in new_findings:
            create_github_issue(finding["drug"], finding["trials"], finding["indications"])
    else:
        print("No new trials found.")

    print(f"\nCompleted at: {datetime.now().isoformat()}")


if __name__ == "__main__":
    main()
