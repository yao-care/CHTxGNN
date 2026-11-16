---
layout: default
title: Downloads
nav_order: 94
permalink: /downloads/
description: "Offene Daten von CHTxGNN zum Herunterladen: FHIR-Ressourcen, Vorhersageergebnisse und Suchindex."
---

# Downloads

<div class="key-takeaway">
Die Vorhersagen werden im Format FHIR R4 veröffentlicht und lassen sich unmittelbar in Systeme für elektronische Patientenakten einbinden.
</div>

---

<!-- site-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
## Schweiz: Daten dieser Website

Diese Website veröffentlicht Berichte zu **{{ site.data.drug_stats.total_drugs }}** Arzneimitteln aus den Zulassungsdaten von [Swissmedic](https://www.swissmedic.ch/) (Schweiz).

Datensatz: [Swissmedic: Zugelassene Packungen (Humanarzneimittel)](https://www.swissmedic.ch/swissmedic/en/home/services/listen_neu.html); er wird jede Woche (montags) automatisch heruntergeladen und abgeglichen. Details: [Datenquellen]({{ '/sources/' | relative_url }}).

Berichte nach Evidenzstufe:

| Evidenzstufe | Berichte | Anteil |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

3 vorhergesagte Arzneimittel-Krankheits-Paare dieser Website kommen auf keiner anderen der 30 TxGNN-Websites vor.

<!-- site-data:end -->

## FHIR-Ressourcen

Diese Website veröffentlicht die Vorhersagen als FHIR-R4-Ressourcen, die von SMART on FHIR-Anwendungen
direkt genutzt werden können:

| Ressource | Pfad | Beschreibung |
|----------|------|-------------|
| CapabilityStatement | `/fhir/metadata` | Capability Statement des FHIR-Servers |
| MedicationKnowledge | `/fhir/MedicationKnowledge/` | Arzneimittel-Ressourcen |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/` | Vorhergesagte Indikationen |
| Bundle | `/fhir/Bundle/all-predictions.json` | Alle Vorhersagen gebündelt |

---

## Suchindex

`/data/search-index.json` stellt einen Suchindex zu Arzneimitteln und Indikationen bereit, mit dem Sie
eine eigene Abfrageoberfläche aufbauen können.

---

## Nutzungsbedingungen

<ol class="actionable-steps">
<li>Die Daten dieser Website dienen <strong>ausschliesslich als Referenz für die Forschung</strong> und dürfen nicht als Grundlage für medizinische Entscheidungen verwendet werden.</li>
<li>Nennen Sie beim Zitieren CHTxGNN (藥提醒科技有限公司) und zitieren Sie die Originalarbeit zu TxGNN.</li>
<li>Weiterverwendete Daten unterliegen weiterhin den Lizenzbedingungen der jeweiligen Originalquelle (siehe <a href="{{ '/sources/' | relative_url }}">Datenquellen</a>).</li>
</ol>

---

## Über den Entwickler

Diese Plattform wird von **藥提醒科技有限公司** (yao.care) entwickelt und betrieben. Den vollständigen
Hintergrund zum Unternehmen und zur Methodik finden Sie auf der Seite <a href="{{ '/about/' | relative_url }}">Über uns</a>.

---

<div class="disclaimer">
<strong>Haftungsausschluss</strong><br>
Dieser Bericht dient ausschliesslich als Referenz für die akademische Forschung und <strong>stellt keine medizinische Beratung dar</strong>. Befolgen Sie stets die Anweisungen Ihrer Ärztin oder Ihres Arztes; ändern Sie Ihre Medikation niemals eigenmächtig. Jede Entscheidung zur Arzneimittel-Umwidmung erfordert eine vollständige klinische Validierung und eine regulatorische Prüfung.
<br><br>
<small>Geprüft von: 藥提醒科技有限公司 (yao.care)</small>
</div>
