---
layout: default
title: Selenium
parent: 僅模型預測 (L5)
nav_order: 16
evidence_level: L5
indication_count: 1
---

# Selenium
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

The txgnn-pipeline skill confirms this is a TxGNN report generation task. Now let me generate the full evaluation report based on the Evidence Pack.

---

# Selenium: From Trace Element Supplementation to Sclerosing Cholangitis

## One-Sentence Summary

Selenium is an essential trace element traditionally supplemented to address selenium deficiency and support antioxidant function.
The TxGNN model predicts it may be effective for **Sclerosing Cholangitis**,
with **0 clinical trials** and **5 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Trace element supplementation / selenium deficiency |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L4 |
| Swiss Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known information, selenium is an essential trace element serving as a cofactor for a family of selenoproteins — most notably glutathione peroxidase (GPx) and thioredoxin reductase — which are central to cellular antioxidant defense and redox homeostasis.

Primary sclerosing cholangitis (PSC) is a chronic cholestatic liver disease in which oxidative stress, immune dysregulation, and progressive biliary fibrosis are central pathological features. Several studies have reported reduced antioxidant capacity and altered trace element profiles in PSC patients. Notably, one observational study (PMID 9053974) directly examined hepatic selenium retention in PSC patients, suggesting that selenium metabolism is perturbed in this disease, which may provide a mechanistic rationale for the TxGNN model's prediction.

However, the connection remains at the level of association rather than established therapeutic efficacy. The prediction score of 99.04% reflects the model's graph-based inference from biological network relationships, not clinical trial outcomes. Validation through interventional studies would be required before any repurposing conclusion can be drawn.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [9053974](https://pubmed.ncbi.nlm.nih.gov/9053974/) | 1995 | Observational | Scand J Gastroenterol | Studied trace element metabolism in 32 PSC patients; found abnormal hepatic selenium retention, suggesting disturbed selenium metabolism in PSC |
| [39601354](https://pubmed.ncbi.nlm.nih.gov/39601354/) | 2025 | Observational | Liver International | Evaluated dietary intake in PSC patients vs. Nordic nutrition recommendations 2023; identified poor fat-soluble vitamin and micronutrient (including selenium) intake |
| [29148959](https://pubmed.ncbi.nlm.nih.gov/29148959/) | 2017 | Case Report | JPEN | Case study of overlapping PSC and UC with severe malabsorption; discusses antioxidant deficiency and oxidative stress as contributors to cholestatic liver disease pathogenesis |
| [17109383](https://pubmed.ncbi.nlm.nih.gov/17109383/) | 2006 | Preclinical | Proteomics | Hepatic proteome analysis in murine models of toxic fibrogenesis and sclerosing cholangitis; mechanistic discussion of protein expression changes relevant to redox pathways |
| [18941372](https://pubmed.ncbi.nlm.nih.gov/18941372/) | 2008 | Review | Eur J Cancer Prev | Review of chemoprevention agents for colorectal cancer; includes selenium among candidate micronutrients, relevant given high CRC risk in PSC patients |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no registered clinical trials testing selenium for sclerosing cholangitis, and the available literature is limited to observational trace element studies and indirect mechanistic evidence — insufficient to support a repurposing recommendation at this stage.

**To proceed, the following is needed:**

- **Mechanism of action data** (MOA): Retrieve from DrugBank API (DB11135) to establish a formal mechanistic rationale linking selenium's antioxidant activity to PSC pathophysiology
- **Clinical trial feasibility assessment**: Evaluate whether any Phase 1/2 trials for selenium in liver or biliary diseases exist that could be extended to PSC
- **Safety and dosage data**: Obtain package insert warnings and contraindications to assess the risk-benefit profile for a chronic liver disease population (selenium toxicity window is narrow)
- **Regulatory standing**: Confirm selenium's approval status in relevant markets as a medicinal product vs. dietary supplement, as this affects repurposing pathway
- **Biomarker studies**: Determine whether PSC patients with low serum selenium levels represent a targetable subpopulation for a hypothesis-driven pilot trial
---

