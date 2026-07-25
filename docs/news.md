---
layout: default
title: 健康新聞
nav_order: 30
permalink: /news/
has_children: true
description: "Health news coverage tracked by CHTxGNN for its drugs and indications."
---

# 健康新聞

<div class="key-takeaway">
Automatically tracked news coverage for the drugs and predicted indications on this site.
</div>

---

## All coverage

{% assign items = site.news | sort: 'title' %}
{% if items.size == 0 %}
No matching coverage yet.
{% else %}
{% for item in items %}- [{{ item.title }}]({{ item.url | relative_url }})
{% endfor %}
{% endif %}

---

## About the Developer

This platform is developed and operated by **藥提醒科技有限公司** (yao.care, company registration
number 83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

CHTxGNN is the Switzerland site of the company's "TxGNN Drug Repurposing" product line.
The same system is deployed across 30 countries and regions, each named `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN, and so on) at `{cc}txgnn.yao.care`.
Product overview: <https://www.yao.care/medical/txgnn/>.

The TxGNN model itself was developed by the Zitnik Lab at Harvard Medical School and published
in *Nature Medicine*. This platform is the production system 藥提醒科技有限公司 built on top of that
model, covering national drug-registration data integration, dual knowledge-graph and
deep-learning prediction, PubMed / ClinicalTrials evidence grading, and SMART on FHIR
electronic health record integration.

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
This report is for academic research reference only and <strong>does not constitute medical advice</strong>. Always follow your physician's instructions; never adjust medication on your own. Any drug repurposing decision requires full clinical validation and regulatory review.
<br><br>
<small>Reviewed by: 藥提醒科技有限公司 (yao.care)</small>
</div>
