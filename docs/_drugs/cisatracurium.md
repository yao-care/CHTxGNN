---
layout: default
title: Cisatracurium
parent: 僅模型預測 (L5)
nav_order: 13
evidence_level: L5
indication_count: 10
---

# Cisatracurium
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

Using the `txgnn-pipeline` skill to guide this report generation. Now producing the evaluation report based on the Evidence Pack.

---

# Cisatracurium: From Perioperative Neuromuscular Blockade to Cauda Equina Syndrome

## One-Sentence Summary

Cisatracurium is a non-depolarizing neuromuscular blocking agent (NMBA) used perioperatively to facilitate tracheal intubation, provide skeletal muscle relaxation during surgery, and support mechanical ventilation in ICU settings.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, however **0 clinical trials** and **0 publications** currently support this direction — placing evidence at the lowest possible level (L5).
The mechanistic rationale for this prediction is critically weak, and the overall assessment is **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registration data available (perioperative neuromuscular blockade based on known pharmacology) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 — Model prediction only, no supporting studies |
| Swiss Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Cisatracurium is a benzylisoquinolinium non-depolarizing NMBA that competitively antagonizes nicotinic acetylcholine receptors (nAChR) at the neuromuscular junction (NMJ), producing reversible skeletal muscle paralysis. It undergoes spontaneous Hofmann elimination — a pH- and temperature-dependent degradation pathway — making it particularly useful in patients with hepatic or renal insufficiency.

Cauda equina syndrome (CES) is a serious neurological emergency caused by compression of the lumbar nerve roots within the spinal canal. It typically presents with lower limb weakness or paralysis, urinary and bowel dysfunction, and saddle-area sensory loss. The standard of care is urgent surgical decompression; pharmacological interventions play no primary therapeutic role.

The mechanistic link between cisatracurium and CES is effectively absent. NMJ blockade acts peripherally on skeletal muscle motor endplates and cannot address nerve root compression, restore neural conduction, or accelerate cauda equina recovery. The high TxGNN score (99.99%) likely reflects a topological pattern in the biomedical knowledge graph rather than a biologically meaningful therapeutic signal. Without any supporting preclinical data, clinical trials, or plausible molecular hypothesis, this prediction does not meet the threshold for further development at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Swiss Market Information

Cisatracurium holds no Swissmedic authorizations and is not currently marketed in Switzerland.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Cisatracurium are rated L5 (model prediction only) with a uniform "Hold" recommendation. For the top-ranked indication — cauda equina syndrome — there are zero supporting clinical trials or publications, and the mechanism of NMJ blockade is pharmacologically incompatible with the pathophysiology of nerve root compression. A high TxGNN score alone is insufficient to advance a candidate with no mechanistic basis.

**To proceed, the following is needed:**

- **Mechanistic hypothesis:** A biologically plausible explanation connecting NMJ blockade (or any off-target cisatracurium effect) to cauda equina syndrome pathophysiology must be established before any further evaluation
- **MOA data (DG002):** Retrieve complete DrugBank MOA data to identify any secondary pharmacological targets that might be relevant to predicted indications
- **Safety data (DG001):** Obtain and parse the package insert to document key warnings and contraindications — currently a blocking data gap
- **Preclinical evidence:** Any in vitro or animal studies suggesting a cauda equina–relevant mechanism would be the minimum requirement to upgrade from L5
- **Reassessment of ranked indications:** Consider whether any of the lower-ranked indications (e.g., preeclampsia rank 2, where cisatracurium is already used instrumentally in emergency C-section GA) offer a more defensible starting point for a focused safety/utility study
---

