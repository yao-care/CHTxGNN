---
layout: default
title: Nur Modellvorhersage (L5)
nav_order: 23
permalink: /evidence-low/
description: "566 Arzneimittel mit Evidenzstufe L5 auf dieser Website (Schweiz), z. B. Denosumabum, Afliberceptum, Dextromethorphanum, jeweils mit wichtigster vorhergesagter Indikation, Swissmedic-Zulassungen und Prüfprotokoll."
---

# Nur Modellvorhersage (L5)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Diese Seite listet **{{ site.data.evidence_tier_facts.low.count }}** der **{{ site.data.drug_stats.total_drugs }}** Arzneimittel mit veröffentlichtem Bericht auf dieser Website ({{ site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %): L5 **{{ site.data.evidence_tier_facts.low.by_level.L5 }}**.
Medianer Anteil der Stufen L5 über die 30 TxGNN-Websites: {{ site.data.evidence_tier_facts.low.cross.median_share }} %. {% if ev_share > site.data.evidence_tier_facts.low.cross.median_share %}Diese Website liegt über dem Median.{% elsif ev_share < site.data.evidence_tier_facts.low.cross.median_share %}Diese Website liegt unter dem Median.{% else %}Diese Website liegt beim Median.{% endif %}

{% if site.data.evidence_tier_facts.low.count > 0 %}
In den lokalen Daten (Swissmedic-Zulassungen) haben **{{ site.data.evidence_tier_facts.low.with_current }}** dieser Arzneimittel mindestens einen gültigen Eintrag, **{{ site.data.evidence_tier_facts.low.none_current }}** haben Einträge, aber keinen gültigen, und **{{ site.data.evidence_tier_facts.low.without_data }}** sind nicht in den lokalen Daten. **{{ site.data.evidence_tier_facts.low.with_reviews }}** haben Einträge im Prüfprotokoll (Korrekturen von Zulassungsangaben auf der Arzneimittelseite). **{{ site.data.evidence_tier_facts.low.cross.unique_drugs }}** haben eine vorhergesagte Indikation, die keine andere TxGNN-Website für dasselbe Arzneimittel nennt.
{% if site.data.evidence_tier_facts.low.none_current_list.size > 0 %}

Mit Einträgen, aber keinem gültigen: {% for r in site.data.evidence_tier_facts.low.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}

Arzneimittel mit einem gültigen lokalen Eintrag stehen zuerst.
{% endif %}

Definition aller Stufen: [Methodik]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

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

### L5 ({{ site.data.evidence_tier_facts.low.by_level.L5 }} Arzneimittel)

<!-- tier-table:start L5（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Arzneimittel | Stufe | Wichtigste vorhergesagte neue Indikation | Swissmedic-Zulassungen: gültige / gesamt | Prüfprotokoll | Nur auf dieser Website |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.low.rows %}{% if r.l == "L5" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ja ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Haftungsausschluss</strong><br>
Dieser Bericht dient ausschliesslich als Referenz für die akademische Forschung und <strong>stellt keine medizinische Beratung dar</strong>. Befolgen Sie stets die Anweisungen Ihrer Ärztin oder Ihres Arztes; ändern Sie Ihre Medikation niemals eigenmächtig. Jede Entscheidung zur Arzneimittel-Umwidmung erfordert eine vollständige klinische Validierung und eine regulatorische Prüfung.
<br><br>
<small>Geprüft von: 藥提醒科技有限公司 (yao.care)</small>
</div>
