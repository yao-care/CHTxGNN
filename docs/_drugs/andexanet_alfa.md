---
layout: default
title: Andexanet Alfa
parent: 僅模型預測 (L5)
nav_order: 11
evidence_level: L5
indication_count: 4
---

# Andexanet Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

以下為根據 Evidence Pack 生成的完整藥師評估報告：

---

# Andexanet Alfa: From Factor Xa Inhibitor Reversal to Glanzmann Thrombasthenia

## One-Sentence Summary

Andexanet alfa is a recombinant modified human Factor Xa decoy protein approved in the US and EU as a reversal agent for life-threatening bleeding in patients receiving Factor Xa inhibitors (apixaban, rivaroxaban), though it has not been registered in Taiwan.
The TxGNN model predicts it may be effective for **Glanzmann Thrombasthenia**, a rare inherited platelet aggregation disorder,
with **0 clinical trials** and **0 publications** currently supporting this direction — making this a model-only prediction at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Reversal of anticoagulation by Factor Xa inhibitors in uncontrolled/life-threatening bleeding (not registered with Taiwan TFDA) |
| Predicted New Indication | Glanzmann Thrombasthenia |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from the formal DrugBank record is not available. Based on published literature and known pharmacology, andexanet alfa (Andexxa®) is a catalytically inactive recombinant human Factor Xa variant. Its primary mechanism is to act as a "decoy" receptor that binds and sequesters direct oral Factor Xa inhibitors — primarily apixaban and rivaroxaban — reversing their anticoagulant effect within minutes of intravenous administration. An additional, non-intended secondary effect is its binding to TFPI (Tissue Factor Pathway Inhibitor), which theoretically can amplify thrombin generation through the extrinsic coagulation pathway. This TFPI-inhibiting mechanism has been validated as a therapeutic target in hemophilia through a dedicated agent, marstacimab (approved 2024).

Glanzmann Thrombasthenia (GT) is caused by deficiency or functional impairment of GPIIb/IIIa (integrin αIIbβ3) on platelet surfaces, resulting in a complete failure of platelet aggregation despite normal platelet counts. The pathological mechanism operates entirely within the platelet receptor–cytoskeletal pathway — structurally and functionally disconnected from the coagulation cascade where andexanet alfa acts. Andexanet alfa has no known ability to upregulate, bypass, or compensate for GPIIb/IIIa dysfunction.

The TxGNN model's high prediction score (99.77%) almost certainly reflects **knowledge graph proximity among hemorrhagic phenotypes** rather than a genuine mechanistic treatment vector. Both GT and the FXa pathway connect through shared bleeding-disorder nodes in the disease graph, producing high cosine similarity without implying biological plausibility. There is an additional theoretical concern: andexanet's procoagulant TFPI-inhibiting side effect was associated with thromboembolic adverse events in the ANNEXA-4 trial, introducing a risk signal that would need careful evaluation even for indirect hemostatic applications.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for Glanzmann Thrombasthenia is supported by zero clinical trials and zero publications, representing a model-only signal (L5 evidence). More critically, the known mechanism of andexanet alfa (FXa decoy / TFPI inhibitor) has no established pathway to address GPIIb/IIIa deficiency, the root cause of GT — making this prediction mechanistically implausible at the current state of knowledge.

**To proceed, the following is needed:**
- Formal MOA characterization from DrugBank to confirm any secondary pathways relevant to platelet biology
- Preclinical data (in vitro or animal model) demonstrating any effect of andexanet alfa or TFPI inhibition on platelet GPIIb/IIIa expression or function
- A scientific rationale bridging TFPI pathway modulation to platelet aggregation defects in GT
- Taiwan TFDA package insert data to assess full contraindication and safety profile before any exploratory use
- Consultation with hematology specialists regarding unmet need versus existing treatments (platelet transfusion, recombinant FVIIa) for GT management
---

