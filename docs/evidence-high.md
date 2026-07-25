---
layout: default
title: Hohe Evidenz (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "Kandidaten der Arzneimittel-Umwidmung mit L1-L2 in CHTxGNN, gestützt auf klinische Studien oder systematische Übersichtsarbeiten."
---

# Hohe Evidenz (L1-L2)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Kandidaten, die vorrangig für eine klinische Bewertung infrage kommen
</p>

---

## Kriterien

| Stufe | Definition | Klinische Bedeutung |
|-------|------------|------------------|
| **L1** | Mehrere Phase-3-RCTs / systematische Übersichtsarbeiten | Starke Absicherung; klinische Anwendung kann erwogen werden |
| **L2** | Einzelne RCT oder mehrere Phase-2-Studien | Mittlere Absicherung; Validierungsstudien können geplant werden |

---

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | sort: "title" %}

### L1 ({{ l1_drugs.size }} Arzneimittel)

| Arzneimittel | Indikationen | Link |
|---------|---------|------|
{% for drug in l1_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Bericht ansehen]({{ drug.url | relative_url }}) |
{% endfor %}

### L2 ({{ l2_drugs.size }} Arzneimittel)

| Arzneimittel | Indikationen | Link |
|---------|---------|------|
{% for drug in l2_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Bericht ansehen]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Haftungsausschluss</strong><br>
Dieser Bericht dient ausschliesslich als Referenz für die akademische Forschung und <strong>stellt keine medizinische Beratung dar</strong>. Befolgen Sie stets die Anweisungen Ihrer Ärztin oder Ihres Arztes; ändern Sie Ihre Medikation niemals eigenmächtig. Jede Entscheidung zur Arzneimittel-Umwidmung erfordert eine vollständige klinische Validierung und eine regulatorische Prüfung.
<br><br>
<small>Geprüft von: 藥提醒科技有限公司 (yao.care)</small>
</div>
