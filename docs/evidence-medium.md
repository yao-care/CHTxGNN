---
layout: default
title: Mittlere Evidenz (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "Kandidaten der Arzneimittel-Umwidmung mit L3-L4 in CHTxGNN, gestützt auf beobachtende oder präklinische Evidenz."
---

# Mittlere Evidenz (L3-L4)

<!-- page-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
{% assign pd_m = site.data.drug_stats.level_counts.L3 | plus: site.data.drug_stats.level_counts.L4 %}
Diese Seite listet **{{ pd_m }}** der **{{ site.data.drug_stats.total_drugs }}** Arzneimittel mit veröffentlichtem Bericht auf dieser Website ({{ pd_m | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %). Definition der Stufen: [Methodik]({{ '/methodology/' | relative_url }}).
<!-- page-data:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Kandidaten mit vorläufiger Evidenz, die einer weiteren Validierung bedürfen
</p>

---

## Kriterien

| Stufe | Definition | Klinische Bedeutung |
|-------|------------|------------------|
| **L3** | Beobachtungsstudien / grosse Fallserien | Vorläufige Absicherung; weitere Validierung erforderlich |
| **L4** | Präklinische / mechanistische Studien | Theoretische Absicherung; weit von der klinischen Anwendung entfernt |

---

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | sort: "title" %}

### L3 ({{ l3_drugs.size }} Arzneimittel)

| Arzneimittel | Indikationen | Link |
|---------|---------|------|
{% for drug in l3_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Bericht ansehen]({{ drug.url | relative_url }}) |
{% endfor %}

### L4 ({{ l4_drugs.size }} Arzneimittel)

| Arzneimittel | Indikationen | Link |
|---------|---------|------|
{% for drug in l4_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Bericht ansehen]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Haftungsausschluss</strong><br>
Dieser Bericht dient ausschliesslich als Referenz für die akademische Forschung und <strong>stellt keine medizinische Beratung dar</strong>. Befolgen Sie stets die Anweisungen Ihrer Ärztin oder Ihres Arztes; ändern Sie Ihre Medikation niemals eigenmächtig. Jede Entscheidung zur Arzneimittel-Umwidmung erfordert eine vollständige klinische Validierung und eine regulatorische Prüfung.
<br><br>
<small>Geprüft von: 藥提醒科技有限公司 (yao.care)</small>
</div>
