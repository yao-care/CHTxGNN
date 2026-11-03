#!/usr/bin/env python3
"""
Extract drug list from docs/_drugs/*.md files.
Creates a JSON file with drug names, evidence levels, and indication counts.
"""

import json
import re
from pathlib import Path


def parse_front_matter(content: str) -> dict:
    """Parse YAML front matter from markdown content."""
    if not content.startswith("---"):
        return {}

    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}

    front_matter = {}
    for line in parts[1].strip().split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            front_matter[key] = value

    return front_matter


def extract_predicted_indication(content: str) -> str:
    """Extract predicted indication from the drug report."""
    # Look for the pattern in the quick overview table
    match = re.search(r'\|\s*預測新適應症\s*\|\s*([^|]+)\s*\|', content)
    if match:
        return match.group(1).strip()
    return ""


def load_known_indications() -> dict:
    """2026-11-03：已知（已核准）適應症，給 check_*.py 的 is_known_indication() 排除用。

    來源是 docs/data/search-index.json 每個藥的 "original"：TxGNN 知識圖譜上該藥已有的適應症
    （英文疾病名，以「；」分隔），和 predicted_indications 同一套名稱。沒有這個檔或欄位就回傳空表，
    各藥的 approved_indication 就是空字串（不排除，和以前一樣）。
    """
    index_file = Path(__file__).parent.parent / "docs" / "data" / "search-index.json"
    try:
        entries = json.loads(index_file.read_text(encoding="utf-8")).get("drugs", [])
    except (OSError, ValueError):
        return {}
    known = {}
    for entry in entries:
        original = "; ".join(x.strip() for x in str(entry.get("original") or "").split("；") if x.strip())
        if original:
            known[("slug", entry.get("slug", ""))] = original
            known[("name", str(entry.get("name", "")).lower())] = original
    return known


def main():
    drugs_dir = Path(__file__).parent.parent / "docs" / "_drugs"
    output_file = Path(__file__).parent / "drug_list.json"
    known = load_known_indications()

    drugs = []

    for md_file in sorted(drugs_dir.glob("*.md")):
        content = md_file.read_text(encoding="utf-8")
        front_matter = parse_front_matter(content)

        drug_name = front_matter.get("title", md_file.stem)
        evidence_level = front_matter.get("evidence_level", "")
        indication_count = front_matter.get("indication_count", "0")

        # Extract predicted indication for search queries
        predicted_indication = extract_predicted_indication(content)

        # 2026-10-16：監測改用 front matter 的英文 INN 與預測新適應症（不分語言）；
        # 沒有這兩個欄位的頁（轉址頁、無新預測頁）不監測
        try:
            predicted_indications = json.loads(front_matter.get("predicted_indications", "[]"))
        except ValueError:
            predicted_indications = []
        monitor_inn = front_matter.get("monitor_inn", "")
        if not predicted_indications or not monitor_inn:
            continue
        slug = re.sub(r"[\W_]+", "-", md_file.stem, flags=re.U).strip("-").lower()
        approved_indication = known.get(("slug", slug)) or known.get(("name", drug_name.lower()), "")

        drugs.append({
            "name": drug_name,
            "file": md_file.name,
            "evidence_level": evidence_level,
            "indication_count": int(indication_count) if indication_count.isdigit() else 0,
            "predicted_indication": predicted_indication,
            "inn": monitor_inn,
            "predicted_indications": predicted_indications,
            "approved_indication": approved_indication,
        })

    # Save to JSON
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({
            "total": len(drugs),
            "generated_at": __import__("datetime").datetime.now().isoformat(),
            "drugs": drugs
        }, f, indent=2, ensure_ascii=False)

    print(f"Extracted {len(drugs)} drugs to {output_file}")
    print(f"  with approved_indication (search-index original): {sum(1 for d in drugs if d['approved_indication'])}")

    # Print summary
    level_counts = {}
    for drug in drugs:
        level = drug["evidence_level"] or "Unknown"
        level_counts[level] = level_counts.get(level, 0) + 1

    print("\nEvidence level distribution:")
    for level in sorted(level_counts.keys()):
        print(f"  {level}: {level_counts[level]}")


if __name__ == "__main__":
    main()
