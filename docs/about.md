---
layout: default
title: Über uns
nav_order: 90
permalink: /about/
description: "CHTxGNN ist eine Plattform für Vorhersagen zur Arzneimittel-Umwidmung, entwickelt von 藥提醒科技有限公司 (yao.care) auf Basis des Harvard-Modells TxGNN; sie deckt die in der Schweiz von Swissmedic zugelassenen Arzneimittel ab."
---

# Über uns

<div class="key-takeaway">
Mit KI die Evidenzvalidierung der Arzneimittel-Umwidmung beschleunigen — von der Vorhersage bis zur Evidenz auf einen Blick.
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

## Hintergrund

<p class="key-answer" data-question="Was ist CHTxGNN?">
<strong>CHTxGNN</strong> ist eine forschungsunterstützende Plattform für die Arzneimittel-Umwidmung,
aufgebaut auf dem Modell TxGNN, das vom Zitnik Lab der Harvard University in <em>Nature Medicine</em>
veröffentlicht wurde. Sie sagt Indikationserweiterungen für Arzneimittel voraus, die in der Schweiz
von Swissmedic zugelassen sind. Über die KI-Vorhersagewerte hinaus bindet die Plattform klinische
Evidenz aus ClinicalTrials.gov und PubMed ein, damit Forschende rasch beurteilen können, wie
belastbar jede Vorhersage ist.
</p>

---

## Über den Entwickler

Diese Plattform wird von **藥提醒科技有限公司** (yao.care, Unternehmensregisternummer
83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan) entwickelt und betrieben.

CHTxGNN ist die Schweizer Website der Produktlinie «TxGNN Drug Repurposing» des Unternehmens.
Dasselbe System ist in 30 Ländern und Regionen im Einsatz, jeweils unter dem Namen `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN und so weiter) unter `{cc}txgnn.yao.care`.
Produktübersicht: <https://www.yao.care/medical/txgnn/>.

Das Modell TxGNN selbst wurde vom Zitnik Lab an der Harvard Medical School entwickelt und in
*Nature Medicine* veröffentlicht. Diese Plattform ist das Produktivsystem, das 藥提醒科技有限公司 auf
Basis dieses Modells aufgebaut hat; es umfasst die Integration nationaler Arzneimittelzulassungsdaten,
die Deep-Learning-Vorhersage unter Ausschluss der bereits im Wissensgraphen erfassten Anwendungen, die Evidenzbewertung aus PubMed /
ClinicalTrials sowie die Anbindung an elektronische Patientenakten über SMART on FHIR.

---

## Was ist Arzneimittel-Umwidmung?

<p class="key-answer" data-question="Was ist Arzneimittel-Umwidmung?">
<strong>Arzneimittel-Umwidmung</strong> bedeutet, neue therapeutische Anwendungen für bereits
vorhandene Arzneimittel zu finden. Verglichen mit der Entwicklung eines völlig neuen Arzneimittels —
10 bis 15 Jahre und 1&ndash;2 Mrd. USD — dauert eine Umwidmung 3 bis 5 Jahre und kostet
100&ndash;300 Mio. USD; zudem liegen bereits Sicherheitsdaten am Menschen vor, sodass das
Fehlschlagrisiko geringer ist.
</p>

<table class="comparison-table">
<thead>
<tr><th>Aspekt</th><th>Neuentwicklung eines Arzneimittels</th><th>Arzneimittel-Umwidmung</th></tr>
</thead>
<tbody>
<tr><td>Dauer</td><td>10&ndash;15 Jahre</td><td>3&ndash;5 Jahre</td></tr>
<tr><td>Kosten</td><td>1&ndash;2 Mrd. USD</td><td>100&ndash;300 Mio. USD</td></tr>
<tr><td>Sicherheitsdaten</td><td>Müssen erst erhoben werden</td><td>Daten am Menschen liegen bereits vor</td></tr>
<tr><td>Fehlschlagrisiko</td><td>Sehr hoch (&gt;90 %)</td><td>Geringer</td></tr>
</tbody>
</table>

---

## Was ist TxGNN?

<p class="key-answer" data-question="Was ist TxGNN?">
<a href="https://www.nature.com/articles/s41591-024-03233-x">TxGNN</a> ist ein Deep-Learning-Modell,
das vom Zitnik Lab an der Harvard Medical School entwickelt und in <em>Nature Medicine</em>
veröffentlicht wurde. Es sagt neuartige Zusammenhänge zwischen Arzneimitteln und Krankheiten voraus
und ist das erste Basismodell für die Arzneimittel-Umwidmung, das gezielt für Klinikerinnen und
Kliniker entworfen wurde.
</p>

<blockquote class="expert-quote">
«TxGNN bindet einen Wissensgraphen mit 17'080 Krankheiten ein und nutzt Graph-Neuronale
Netze, um komplexe Beziehungen zwischen Knoten zu lernen und die mögliche Wirksamkeit von
Arzneimitteln gegen seltene Krankheiten vorherzusagen.»
<cite>&mdash; Huang et al., Nature Medicine (2024)</cite>
</blockquote>

---

## Datenquellen

Die Datenquellen der Plattform (TxGNN-Vorhersage, klinische Studien, Literatur, DrugBank und die
lokale Arzneimittelliste) sowie ihre Lizenzen und Aktualisierungsintervalle sind auf der Seite
<a href="{{ '/sources/' | relative_url }}">Datenquellen</a> aufgeführt.

---

## Wissenschaftliche Grundlage

> Huang, K., et al. (2024). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)

---

## Umfang

| Position | Wert |
|------|-------|
| Arzneimittelberichte | {{ site.data.drug_stats.total_drugs }} |
| Zulassungsbehörde | Swissmedic |
| Bereitgestellte Websites | 30 Länder / Regionen |

---

## Kontakt

- **GitHub Issues**: <https://github.com/yao-care/CHTxGNN/issues>
- **Entwickler**: 藥提醒科技有限公司 (<https://www.yao.care>, service@yao.care)
- **Produktübersicht**: <https://www.yao.care/medical/txgnn/>

---

<div class="disclaimer">
<strong>Haftungsausschluss</strong><br>
Dieser Bericht dient ausschliesslich als Referenz für die akademische Forschung und <strong>stellt keine medizinische Beratung dar</strong>. Befolgen Sie stets die Anweisungen Ihrer Ärztin oder Ihres Arztes; ändern Sie Ihre Medikation niemals eigenmächtig. Jede Entscheidung zur Arzneimittel-Umwidmung erfordert eine vollständige klinische Validierung und eine regulatorische Prüfung.
<br><br>
<small>Geprüft von: 藥提醒科技有限公司 (yao.care)</small>
</div>
