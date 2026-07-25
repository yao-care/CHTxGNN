---
layout: default
title: Mittlere Evidenz (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "Kandidaten der Arzneimittel-Umwidmung mit L3-L4 in CHTxGNN, gestützt auf beobachtende oder präklinische Evidenz."
---

# Mittlere Evidenz (L3-L4)

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
