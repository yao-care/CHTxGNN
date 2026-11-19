---
layout: default
title: Hohe Evidenz (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "23 Arzneimittel mit Evidenzstufe L1–L2 auf dieser Website (Schweiz), z. B. Bendamustinum, Doxorubicini Hydrochloridum, Hydrocortisonum, jeweils mit wichtigster vorhergesagter Indikation, Swissmedic-Zulassungen und Prüfprotokoll."
---

# Hohe Evidenz (L1-L2)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Diese Seite listet **{{ site.data.evidence_tier_facts.high.count }}** der **{{ site.data.drug_stats.total_drugs }}** Arzneimittel mit veröffentlichtem Bericht auf dieser Website ({{ site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %): L1 **{{ site.data.evidence_tier_facts.high.by_level.L1 }}**, L2 **{{ site.data.evidence_tier_facts.high.by_level.L2 }}**.
Medianer Anteil der Stufen L1–L2 über die 30 TxGNN-Websites: {{ site.data.evidence_tier_facts.high.cross.median_share }} %. {% if ev_share > site.data.evidence_tier_facts.high.cross.median_share %}Diese Website liegt über dem Median.{% elsif ev_share < site.data.evidence_tier_facts.high.cross.median_share %}Diese Website liegt unter dem Median.{% else %}Diese Website liegt beim Median.{% endif %}

{% if site.data.evidence_tier_facts.high.count > 0 %}
In den lokalen Daten (Swissmedic-Zulassungen) haben **{{ site.data.evidence_tier_facts.high.with_current }}** dieser Arzneimittel mindestens einen gültigen Eintrag, **{{ site.data.evidence_tier_facts.high.none_current }}** haben Einträge, aber keinen gültigen, und **{{ site.data.evidence_tier_facts.high.without_data }}** sind nicht in den lokalen Daten. **{{ site.data.evidence_tier_facts.high.with_reviews }}** haben Einträge im Prüfprotokoll (Korrekturen von Zulassungsangaben auf der Arzneimittelseite). **{{ site.data.evidence_tier_facts.high.cross.unique_drugs }}** haben eine vorhergesagte Indikation, die keine andere TxGNN-Website für dasselbe Arzneimittel nennt.
{% if site.data.evidence_tier_facts.high.none_current_list.size > 0 %}

Mit Einträgen, aber keinem gültigen: {% for r in site.data.evidence_tier_facts.high.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

Definition aller Stufen: [Methodik]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

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

### L1 ({{ site.data.evidence_tier_facts.high.by_level.L1 }} Arzneimittel)

<!-- tier-table:start L1（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Arzneimittel | Stufe | Wichtigste vorhergesagte neue Indikation | Swissmedic-Zulassungen: gültige / gesamt | Prüfprotokoll | Nur auf dieser Website |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L1" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ja ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### L2 ({{ site.data.evidence_tier_facts.high.by_level.L2 }} Arzneimittel)

<!-- tier-table:start L2（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Arzneimittel | Stufe | Wichtigste vorhergesagte neue Indikation | Swissmedic-Zulassungen: gültige / gesamt | Prüfprotokoll | Nur auf dieser Website |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L2" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ja ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Haftungsausschluss</strong><br>
Dieser Bericht dient ausschliesslich als Referenz für die akademische Forschung und <strong>stellt keine medizinische Beratung dar</strong>. Befolgen Sie stets die Anweisungen Ihrer Ärztin oder Ihres Arztes; ändern Sie Ihre Medikation niemals eigenmächtig. Jede Entscheidung zur Arzneimittel-Umwidmung erfordert eine vollständige klinische Validierung und eine regulatorische Prüfung.
<br><br>
<small>Geprüft von: 藥提醒科技有限公司 (yao.care)</small>
</div>
