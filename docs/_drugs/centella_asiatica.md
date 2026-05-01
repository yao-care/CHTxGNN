---
layout: default
title: Centella Asiatica
parent: 僅模型預測 (L5)
nav_order: 12
evidence_level: L5
indication_count: 3
---

# Centella Asiatica
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Using `txgnn-pipeline` to frame this as a Taiwan TxGNN report context. Now generating the evaluation report from the Evidence Pack.

---

# Centella Asiatica: From Wound Healing to Insomnia

## One-Sentence Summary

Centella asiatica (Gotu Kola) is a traditional Ayurvedic botanical, historically recognized for wound healing, venous insufficiency, and skin conditions across Southeast Asian and Ayurvedic traditions — with no formal approved indications on record in Taiwan.

The TxGNN model predicts it may be effective for **Insomnia**, with **2 clinical trials** and **1 publication** currently supporting this direction.

The overall evidence remains at preclinical stage (L4); mechanistic plausibility exists but human validation is absent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Wound healing, venous insufficiency, skin conditions (traditional use; no formal Taiwan approval) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is unavailable for Centella asiatica. Based on known phytochemical research, its primary active constituents are **triterpene saponins** — asiaticoside, madecassoside, and asiatic acid — which exert pleiotropic biological effects spanning anti-inflammatory, antioxidant, and neuroprotective activities. In Ayurvedic medicine, Centella asiatica has long been classified as a *medhya rasayana* (neurological tonic), suggesting historical recognition of its CNS-relevant properties well before modern mechanistic study.

The bridge from Centella asiatica to insomnia is proposed through two overlapping pathways. First, a 2016 in vitro electrophysiology study demonstrated that asiatic acid and madecassic acid act as **selective negative modulators of GABA-A receptor subtypes** expressed in *Xenopus laevis* oocytes (PMID 27062315) — a mechanism shared by benzodiazepines and classical hypnotics. Second, a 2024 zebrafish insomnia model study (PMID 38812527) found that Centella asiatica ethanol extract reduced insomnia-like behavior by inhibiting the **orexin/hypocretin signaling cascade** and its downstream ERK/Akt/p38 pathways, which regulate the arousal system. Orexin antagonism is, notably, the mechanism of clinically approved drugs such as suvorexant.

That said, the traditional indication (wound healing / collagen synthesis) and insomnia are mechanistically distant: the sleep-relevant GABAergic and orexinergic activities appear to be secondary pharmacological actions, not the primary wound-repair pathway. No human pharmacokinetic data currently confirms that oral doses of asiaticoside or madecassoside reach CNS-active concentrations in people. The prediction is biologically plausible but remains unvalidated in humans.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07274371](https://clinicaltrials.gov/study/NCT07274371) | NA | Active, Not Recruiting | 30 | Nightly 10-min Brahmi-Gotu Kola oil foot massage vs. sesame oil for sleep and mood disturbances in perimenopausal women (ages 40–55); includes validated sleep scale outcomes; no results available yet |
| [NCT04872946](https://clinicaltrials.gov/study/NCT04872946) | NA | Completed | 74 | Oral + topical Centella asiatica formulation assessed for skin redness and sensitivity; sleep was neither a primary nor secondary outcome; relevant only as background safety data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [38812527](https://pubmed.ncbi.nlm.nih.gov/38812527/) | 2024 | Animal Study (zebrafish larvae) | F1000Research | Centella asiatica ethanol extract reduced insomnia-like behavior in zebrafish larvae by suppressing orexin expression and inhibiting ERK, Akt, and p38 downstream signaling; provides direct mechanistic support for the insomnia hypothesis, but requires human pharmacological translation |

---

## Taiwan Market Information

No product authorizations for Centella asiatica are registered with TFDA, and the compound is not marketed in Taiwan. Accordingly, no authorization records are available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base for Centella asiatica in insomnia consists of a single zebrafish preclinical study and two clinical trials that did not directly test the insomnia indication — placing this at L4 evidence level. While the orexin and GABA-A mechanistic hypotheses are biologically grounded, neither has been validated in human subjects, and CNS bioavailability of the active triterpenes after oral dosing remains uncharacterized.

**To proceed, the following is needed:**

- **Human pilot study**: A Phase 1/2 trial using a standardized Centella asiatica extract (e.g., titrated extract TECA or water extract CAW) with pre-specified sleep outcomes (Pittsburgh Sleep Quality Index, actigraphy, or polysomnography)
- **Pharmacokinetic profiling**: Confirm CNS bioavailability of asiaticoside and madecassoside after oral dosing in humans
- **Dose-ranging data**: Determine whether doses needed for neurological/sleep effects differ meaningfully from traditional wound-care or dermatological doses
- **Safety characterization**: Obtain drug interaction and contraindication data for the neurological use case, particularly given GABA-A modulation (potential for sedation or interaction with other CNS agents)
- **Consider pivoting to anxiety first**: Centella asiatica's predicted **anxiety** indication (rank 2, L3 evidence, recommendation: "Proceed with Guardrails") has substantially stronger clinical support — including one completed Phase 2 trial (NCT03482063, N=141) and 20 publications — and may offer a more viable near-term repurposing pathway, with insomnia as a downstream co-indication
---

