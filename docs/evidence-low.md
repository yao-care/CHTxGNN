---
layout: default
title: Nur Modellvorhersage (L5)
nav_order: 23
permalink: /evidence-low/
description: "L5-Kandidaten in CHTxGNN: nur Modellvorhersage, bislang ohne klinische Evidenz oder Literaturbelege."
---

# Nur Modellvorhersage (L5)

<!-- page-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
{% assign pd_m = site.data.drug_stats.level_counts.L5 %}
Diese Seite listet **{{ pd_m }}** der **{{ site.data.drug_stats.total_drugs }}** Arzneimittel mit veröffentlichtem Bericht auf dieser Website ({{ pd_m | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %). Definition der Stufen: [Methodik]({{ '/methodology/' | relative_url }}).
<!-- page-data:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Kandidaten mit reiner Modellvorhersage und bislang ohne Evidenz am Menschen
</p>

---

## Kriterien

| Stufe | Definition | Klinische Bedeutung |
|-------|------------|------------------|
| **L5** | Nur Modellvorhersage | Hypothesenstadium; bislang keine Evidenz am Menschen |

---

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | sort: "title" %}

### L5 ({{ l5_drugs.size }} Arzneimittel)

| Arzneimittel | Indikationen | Link |
|---------|---------|------|
{% for drug in l5_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Bericht ansehen]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Haftungsausschluss</strong><br>
Dieser Bericht dient ausschliesslich als Referenz für die akademische Forschung und <strong>stellt keine medizinische Beratung dar</strong>. Befolgen Sie stets die Anweisungen Ihrer Ärztin oder Ihres Arztes; ändern Sie Ihre Medikation niemals eigenmächtig. Jede Entscheidung zur Arzneimittel-Umwidmung erfordert eine vollständige klinische Validierung und eine regulatorische Prüfung.
<br><br>
<small>Geprüft von: 藥提醒科技有限公司 (yao.care)</small>
</div>
