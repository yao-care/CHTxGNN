---
layout: default
title: Isavuconazonium
parent: 僅模型預測 (L5)
nav_order: 15
evidence_level: L5
indication_count: 2
---

# Isavuconazonium
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

以下是根據 Evidence Pack 生成的評估報告：

---

# Isavuconazonium: From Invasive Aspergillosis to Pneumocystosis

## One-Sentence Summary

Isavuconazonium (prodrug of isavuconazole) is a broad-spectrum triazole antifungal approved internationally for invasive aspergillosis and invasive mucormycosis, acting by inhibiting fungal CYP51 to block ergosterol biosynthesis.
The TxGNN model predicts it may be effective for **Pneumocystosis** (PCP, *Pneumocystis jirovecii* pneumonia), with a high prediction score of **99.56%**.
However, **no clinical trials and no supporting publications** have been identified for this combination, and mechanistic analysis raises significant concerns about the biological plausibility of this prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Invasive aspergillosis; invasive mucormycosis (based on drug class; no formal indication text available in this Evidence Pack) |
| Predicted New Indication | Pneumocystosis (*Pneumocystis jirovecii* pneumonia, PCP) |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L5 |
| Swiss Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Isavuconazonium is a water-soluble prodrug that is rapidly converted in vivo to its active form, isavuconazole. As a second-generation triazole antifungal, isavuconazole inhibits lanosterol 14α-demethylase (CYP51), a key enzyme in the ergosterol biosynthesis pathway. Disruption of ergosterol synthesis compromises fungal cell membrane integrity, ultimately leading to cell death. Isavuconazole's broad spectrum covers *Aspergillus* spp., *Mucorales*, *Fusarium*, *Candida*, and several other molds — all of which depend on ergosterol as their primary membrane sterol.

At first glance, the prediction seems mechanistically plausible: *Pneumocystis jirovecii* does possess a CYP51 homolog (Erg11), which theoretically could be inhibited by triazoles. It is likely this structural and pathway-level similarity in the knowledge graph (KG) that drove TxGNN's high prediction score, as "fungal infection" nodes are densely connected within the KG.

**However, there is a critical biological barrier.** Unlike most pathogenic fungi, *P. jirovecii* cannot synthesize its own ergosterol and instead incorporates **cholesterol** from the human host as its primary membrane sterol. This fundamentally undermines CYP51 inhibition as a therapeutic strategy. Consistent with this, all triazoles evaluated to date — including voriconazole and itraconazole — have demonstrated **no clinically meaningful efficacy** against PCP. The standard of care remains trimethoprim-sulfamethoxazole (TMP-SMX), which targets folate synthesis via a completely different mechanism. This is a well-documented case where a surface-level mechanistic link does not translate to clinical activity, and the TxGNN prediction is most likely a **false positive driven by KG topology** rather than disease-specific biology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Swiss Market Information

Isavuconazonium has no authorizations recorded in this Evidence Pack's regulatory database. The drug is not currently marketed in this jurisdiction.

> **Note for context:** Isavuconazonium sulfate (brand name Cresemba®) has been approved by the US FDA (2015), EMA (2015), and other regulatory authorities for invasive aspergillosis and invasive mucormycosis. Local regulatory registration should be verified separately.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a TxGNN score of 99.56%, the prediction is mechanistically unsupported — *P. jirovecii* relies on host-derived cholesterol rather than self-synthesized ergosterol, rendering CYP51 inhibition ineffective, a finding already confirmed by multiple failed triazole clinical experiences in PCP. This is an L5 prediction with zero supporting clinical trials or literature.

**To proceed, the following would be needed:**

- **Mechanistic validation**: In vitro susceptibility testing of isavuconazole against *P. jirovecii* isolates (noting that in vitro culture of this organism is extremely difficult)
- **Preclinical animal model data**: Rodent PCP models with isavuconazole to establish proof-of-concept before any clinical investment
- **KG bias analysis**: Review whether TxGNN's high score reflects genuine disease-specific signal or broad KG node connectivity artefacts in the "fungal infection" cluster
- **Safety data**: Obtain formal package insert warnings, contraindications, and drug interaction profile from DrugBank or product labelling
- **Comparison with rank-2 indication (Mycetoma)**: Eumycetoma caused by *Madurella* spp. presents a substantially more plausible repurposing target, as these organisms have intact ergosterol biosynthesis pathways. This direction (L4, "Research Question") warrants priority over pneumocystosis for further investigation
---

