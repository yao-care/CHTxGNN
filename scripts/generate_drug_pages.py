#!/usr/bin/env python3
"""
Generate individual drug pages for Jekyll from repurposing predictions.

Creates markdown pages for each drug with predicted indications.

Output: docs/_drugs/{drug-slug}.md
"""

import pandas as pd
from datetime import datetime
from pathlib import Path

# Project configuration
PROJECT_ROOT = Path(__file__).parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
DRUGS_DIR = DOCS_DIR / "_drugs"
DATA_DIR = PROJECT_ROOT / "data" / "processed"

# Country-specific settings
COUNTRY_CODE = "BR"
COUNTRY_NAME = "Brazil"
LANGUAGE = "pt-BR"
REGULATORY_AGENCY = "ANVISA"
SITE_URL = "https://artxgnn.yao.care"


def slugify(text: str) -> str:
    """Convert text to URL-safe slug."""
    import re
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text)
    return text.strip("_")


def get_page_strings(base_dir: Path) -> dict:
    """Get localized strings for drug pages based on project name."""
    proj = base_dir.name if base_dir else ""
    strings = {
        "CHTxGNN": {
            "basic_info": "Grundlegende Informationen",
            "predicted": "Vorhergesagte Indikationen (TxGNN)",
            "intro": "Die folgenden sind potenzielle neue Indikationen, die vom TxGNN-Modell vorhergesagt wurden. Höhere Punktzahlen deuten auf eine höhere vorhergesagte Relevanz hin.",
            "disclaimer_h": "Haftungsausschluss",
            "disclaimer": "Diese Vorhersagen dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.\nVor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.",
            "back": "Zurück zur Arzneimittelsuche",
            "item": "Element", "value": "Wert", "evidence": "Evidenzniveau",
            "ev_desc": "L5 (Computergestützte Vorhersage)", "num_ind": "Anzahl vorhergesagter Indikationen",
            "ind": "Indikation", "source": "Quelle", "showing": "Zeige die ersten 50 von",
        },
        "SETxGNN": {
            "basic_info": "Grundläggande information",
            "predicted": "Förutsagda indikationer (TxGNN)",
            "intro": "Följande är potentiella nya indikationer som förutsagts av TxGNN-modellen. Högre poäng indikerar högre förutsagd relevans.",
            "disclaimer_h": "Ansvarsfriskrivning",
            "disclaimer": "Dessa förutsägelser är endast avsedda för forskningsändamål och utgör inte medicinsk rådgivning.\nKlinisk validering krävs före klinisk tillämpning.",
            "back": "Tillbaka till läkemedelssökning",
            "item": "Objekt", "value": "Värde", "evidence": "Evidensnivå",
            "ev_desc": "L5 (Datorbaserad förutsägelse)", "num_ind": "Antal förutsagda indikationer",
            "ind": "Indikation", "source": "Källa", "showing": "Visar de 50 första av",
        },
    }
    return strings.get(proj, {
        "basic_info": "Basic Information",
        "predicted": "Predicted Indications (TxGNN)",
        "intro": "The following are potential new indications predicted by the TxGNN model. Higher scores indicate higher predicted relevance.",
        "disclaimer_h": "Disclaimer",
        "disclaimer": "These predictions are for research purposes only and do not constitute medical advice.\nClinical validation is required before any clinical application.",
        "back": "Back to Drug Search",
        "item": "Item", "value": "Value", "evidence": "Evidence Level",
        "ev_desc": "L5 (Computational Prediction)", "num_ind": "Number of Predicted Indications",
        "ind": "Indication", "source": "Source", "showing": "Showing top 50 of",
    })


def generate_drug_page(drugbank_id: str, drug_name: str, indications: list, s: dict) -> str:
    """Generate markdown content for a drug page."""
    slug = slugify(drug_name)

    content = f"""---
layout: drug
title: {drug_name}
drugbank_id: {drugbank_id}
evidence_level: L5
permalink: /drugs/{slug}/
---

# {drug_name}

## {s['basic_info']}

| {s['item']} | {s['value']} |
|------|-------|
| DrugBank ID | [{drugbank_id}](https://go.drugbank.com/drugs/{drugbank_id}) |
| {s['evidence']} | {s['ev_desc']} |
| {s['num_ind']} | {len(indications)} |

## {s['predicted']}

{s['intro']}

| # | {s['ind']} | {s['source']} |
|---|------------|--------|
"""

    for i, ind in enumerate(indications[:50], 1):
        ind_name = ind.get("indication", "")
        source = ind.get("source", "KG")
        content += f"| {i} | {ind_name} | {source} |\n"

    if len(indications) > 50:
        content += f"\n*({s['showing']} {len(indications)})*\n"

    content += f"""
## {s['disclaimer_h']}

{s['disclaimer']}

---

[← {s['back']}](/drugs/)
"""

    return content


def main():
    base_dir = Path(__file__).parent.parent
    s = get_page_strings(base_dir)

    print("=" * 60)
    print(f"{base_dir.name} - Generate Drug Pages")
    print("=" * 60)
    print()

    # Load prediction data
    candidates_path = DATA_DIR / "repurposing_candidates.csv.gz"

    if not candidates_path.exists():
        print(f"Error: {candidates_path} not found")
        print("Please run run_kg_prediction.py first")
        return

    print(f"1. Loading predictions from {candidates_path}...")
    candidates = pd.read_csv(candidates_path)
    print(f"   Loaded {len(candidates)} predictions")

    # Group by drug
    drug_col = "drugbank_id" if "drugbank_id" in candidates.columns else candidates.columns[0]
    indication_col = "potential_indication" if "potential_indication" in candidates.columns else "disease_name"
    source_col = "source" if "source" in candidates.columns else None

    print()
    print("2. Grouping by drug...")
    drugs = {}
    for _, row in candidates.iterrows():
        drug_id = row.get(drug_col, "")
        if pd.isna(drug_id):
            continue
        drug_id = str(drug_id)

        if drug_id not in drugs:
            # Try to get drug name from ingredient column
            drug_name = drug_id
            if "drug_ingredient" in row:
                drug_name = row["drug_ingredient"] or drug_id
            drugs[drug_id] = {
                "name": drug_name,
                "indications": []
            }

        indication = row.get(indication_col, "")
        if pd.isna(indication):
            continue

        source = row.get(source_col, "KG") if source_col else "KG"
        drugs[drug_id]["indications"].append({
            "indication": str(indication),
            "source": str(source) if not pd.isna(source) else "KG"
        })

    print(f"   Found {len(drugs)} unique drugs")

    # Create output directory
    DRUGS_DIR.mkdir(parents=True, exist_ok=True)

    print()
    print("3. Generating drug pages...")
    pages_created = 0
    skipped = 0
    for drug_id, drug_data in drugs.items():
        slug = slugify(drug_data["name"])
        page_path = DRUGS_DIR / f"{slug}.md"

        # Skip if a pharmacist report page already exists
        if page_path.exists():
            skipped += 1
            continue

        content = generate_drug_page(drug_id, drug_data["name"], drug_data["indications"], s)
        with open(page_path, "w", encoding="utf-8") as f:
            f.write(content)
        pages_created += 1

    print(f"   Created {pages_created} drug pages (skipped {skipped} existing)")
    print()
    print("=" * 60)
    print("Done!")
    print(f"Output: {DRUGS_DIR}")


if __name__ == "__main__":
    main()
