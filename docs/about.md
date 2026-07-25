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
die duale Vorhersage aus Wissensgraph und Deep Learning, die Evidenzbewertung aus PubMed /
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
<a href="https://www.nature.com/articles/s41591-023-02233-x">TxGNN</a> ist ein Deep-Learning-Modell,
das vom Zitnik Lab an der Harvard Medical School entwickelt und in <em>Nature Medicine</em>
veröffentlicht wurde. Es sagt neuartige Zusammenhänge zwischen Arzneimitteln und Krankheiten voraus
und ist das erste Basismodell für die Arzneimittel-Umwidmung, das gezielt für Klinikerinnen und
Kliniker entworfen wurde.
</p>

<blockquote class="expert-quote">
«TxGNN bindet einen Wissensgraphen mit 17'080 biomedizinischen Entitäten ein und nutzt Graph-Neuronale
Netze, um komplexe Beziehungen zwischen Knoten zu lernen und die mögliche Wirksamkeit von
Arzneimitteln gegen seltene Krankheiten vorherzusagen.»
<cite>&mdash; Huang et al., Nature Medicine (2023)</cite>
</blockquote>

---

## Datenquellen

<table class="comparison-table">
<thead>
<tr><th>Art</th><th>Quelle</th><th>Beschreibung</th></tr>
</thead>
<tbody>
<tr><td>KI-Vorhersage</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Wissensgraph-Vorhersagemodell aus Harvard</td></tr>
<tr><td>Klinische Studien</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Weltweites Register klinischer Studien</td></tr>
<tr><td>Literatur</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Biomedizinische Literaturdatenbank</td></tr>
<tr><td>Arzneimittelinformationen</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Datenbank zu Arzneimitteln und Zielstrukturen</td></tr>
<tr><td>Zulassungsdaten</td><td><a href="https://www.swissmedic.ch/">Swissmedic</a></td><td>Arzneimittelzulassungsdaten für die Schweiz</td></tr>
</tbody>
</table>

---

## Wissenschaftliche Grundlage

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

---

## Umfang

| Position | Wert |
|------|-------|
| Arzneimittelberichte | 730 |
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
