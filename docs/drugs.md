---
layout: default
title: Alle Arzneimittel
nav_order: 20
permalink: /drugs/
description: "Alle Arzneimittel-Validierungsberichte und Statistiken zu den Evidenzstufen in CHTxGNN."
---
{%- comment -%}2026-10-16：列表不含舊 ID 轉址頁與 noindex 頁{%- endcomment -%}
{% assign listed_drugs = site.drugs | where_exp: "d", "d.layout != 'redirect'" | where_exp: "d", "d.noindex != true" %}
{% assign l1_count = listed_drugs | where: "evidence_level", "L1" | size %}
{% assign l2_count = listed_drugs | where: "evidence_level", "L2" | size %}
{% assign l3_count = listed_drugs | where: "evidence_level", "L3" | size %}
{% assign l4_count = listed_drugs | where: "evidence_level", "L4" | size %}
{% assign l5_count = listed_drugs | where: "evidence_level", "L5" | size %}

# Alle Arzneimittel

{{ listed_drugs.size }} Arzneimittel-Validierungsberichte

---

## Aufschlüsselung nach Evidenzstufe

| Evidenzstufe | Arzneimittel | Beschreibung |
|---------|--------|------|
| **L1** | {{ l1_count }} | Mehrere RCTs / systematische Übersichtsarbeiten |
| **L2** | {{ l2_count }} | Einzelne RCT / Phase-2-Studien |
| **L3** | {{ l3_count }} | Beobachtungsstudien / grosse Fallserien |
| **L4** | {{ l4_count }} | Präklinische / mechanistische Studien |
| **L5** | {{ l5_count }} | Nur Modellvorhersage |

---

## Vollständige Arzneimittelliste

{% assign all_drugs = listed_drugs | sort: 'title' %}

| Arzneimittel | Evidenzstufe | Indikationen |
|---------|---------|---------|
{% for drug in all_drugs %}| [{{ drug.title }}]({{ drug.url | relative_url }}) | {{ drug.evidence_level }} | {{ drug.indication_count }} |
{% endfor %}

---

<div class="disclaimer">
<strong>Haftungsausschluss</strong><br>
Dieser Bericht dient ausschliesslich als Referenz für die akademische Forschung und <strong>stellt keine medizinische Beratung dar</strong>. Befolgen Sie stets die Anweisungen Ihrer Ärztin oder Ihres Arztes; ändern Sie Ihre Medikation niemals eigenmächtig. Jede Entscheidung zur Arzneimittel-Umwidmung erfordert eine vollständige klinische Validierung und eine regulatorische Prüfung.
<br><br>
<small>Geprüft von: 藥提醒科技有限公司 (yao.care)</small>
</div>
