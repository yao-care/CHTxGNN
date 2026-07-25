---
layout: default
title: Methodik
nav_order: 91
permalink: /methodology/
description: "Wie CHTxGNN Vorhersagen erzeugt und validiert: Wissensgraph-Vorhersage mit TxGNN, Evidenzsammlung, Einstufung L1-L5 und Entscheidungsempfehlungen."
---

# Methodik

<div class="key-takeaway">
Von der KI-Vorhersage bis zur Evidenzeinstufung — für jeden Kandidaten ist die Grundlage seiner Bewertung nachvollziehbar.
</div>

---

## Gesamter Ablauf

<p class="key-answer" data-question="Wie erzeugt CHTxGNN seine Vorhersagen?">
Die Plattform arbeitet mit einem vierstufigen Ablauf: Das Wissensgraph-Modell TxGNN sagt mögliche
Zusammenhänge zwischen Arzneimitteln und Krankheiten voraus, anschliessend wird für jedes vorhergesagte
Paar automatisch Evidenz gesammelt, die Evidenz wird von L1 bis L5 eingestuft und schliesslich wird eine
Entscheidungsempfehlung ausgesprochen.
</p>

<ol class="actionable-steps">
<li><strong>TxGNN-Vorhersage</strong>: Beziehungen zwischen Arzneimitteln und Krankheiten werden mit einem Wissensgraphen in Kombination mit Graph-Neuronalen Netzen vorhergesagt.</li>
<li><strong>Evidenzsammlung</strong>: Für jedes vorhergesagte Paar wird Evidenz aus ClinicalTrials.gov, PubMed, DrugBank und Swissmedic zusammengetragen.</li>
<li><strong>Evidenzeinstufung</strong>: Einstufung von L1 bis L5, wobei L1 die stärkste Stufe ist (mehrere Phase-3-RCTs) und L5 nur eine Modellvorhersage bedeutet.</li>
<li><strong>Entscheidungsempfehlung</strong>: Go, Proceed, Consider, Explore oder Hold, je nach Evidenzstufe.</li>
</ol>

---

## Kriterien der Evidenzeinstufung

<table class="comparison-table">
<thead>
<tr><th>Stufe</th><th>Definition</th><th>Klinische Bedeutung</th></tr>
</thead>
<tbody>
<tr><td><strong>L1</strong></td><td>Mehrere Phase-3-RCTs / systematische Übersichtsarbeiten</td><td>Starke Absicherung; klinische Anwendung kann erwogen werden</td></tr>
<tr><td><strong>L2</strong></td><td>Einzelne RCT oder mehrere Phase-2-Studien</td><td>Mittlere Absicherung; Validierungsstudien können geplant werden</td></tr>
<tr><td><strong>L3</strong></td><td>Beobachtungsstudien / grosse Fallserien</td><td>Vorläufige Absicherung; weitere Validierung erforderlich</td></tr>
<tr><td><strong>L4</strong></td><td>Präklinische / mechanistische Studien</td><td>Theoretische Absicherung; weit von der klinischen Anwendung entfernt</td></tr>
<tr><td><strong>L5</strong></td><td>Nur Modellvorhersage</td><td>Hypothesenstadium; bislang keine Evidenz am Menschen</td></tr>
</tbody>
</table>

---

## Vorhersage mit zwei Verfahren

Zwei Verfahren laufen parallel, und eine Konfidenzangabe hält fest, ob sie übereinstimmen:

| Verfahren | Geschwindigkeit | Genauigkeit | Beschreibung |
|--------|-------|-----------|-------------|
| Wissensgraph (KG) | Schnell | Geringer | Inferenz über DrugBank-Beziehungen und Graphstruktur |
| Deep Learning (DL) | Langsam | Höher | Graph-Neuronales-Netz-Modell TxGNN |

| Konfidenz | Quelle | Bedeutung |
|------------|--------|---------|
| very_high | KG + DL | Beide Verfahren stimmen überein |
| high | Nur DL | Deep-Learning-Absicherung mit hohem Wert |
| medium | Nur KG | Absicherung durch den Wissensgraphen |

---

## Einbindung der Zulassungsdaten

Die Arzneimittelzulassungsdaten für die Schweiz stammen von Swissmedic. Die Wirkstoffnamen werden auf
das Vokabular von DrugBank abgebildet; Wirkstoffe, die sich nicht abbilden lassen — Pflanzenextrakte,
Impfstoffe, Hilfsstoffe und weitere, die in DrugBank nicht erfasst sind — werden von der Vorhersage
ausgeschlossen.

---

## Grenzen

<ol class="actionable-steps">
<li>Vorhersagen sind statistische Zusammenhänge und <strong>bedeuten weder Kausalität noch klinische Wirksamkeit</strong>.</li>
<li>Eine Einstufung als L5 bedeutet, dass nur eine Modellvorhersage vorliegt und keine belegende Evidenz am Menschen.</li>
<li>Die Evidenzsammlung stützt sich auf öffentliche Datenbanken; unveröffentlichte oder nicht indexierte Studien werden nicht erfasst.</li>
<li>Bei der Wirkstoffabbildung können Einträge aufgrund abweichender Bezeichnungen fehlen.</li>
</ol>

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

<div class="disclaimer">
<strong>Haftungsausschluss</strong><br>
Dieser Bericht dient ausschliesslich als Referenz für die akademische Forschung und <strong>stellt keine medizinische Beratung dar</strong>. Befolgen Sie stets die Anweisungen Ihrer Ärztin oder Ihres Arztes; ändern Sie Ihre Medikation niemals eigenmächtig. Jede Entscheidung zur Arzneimittel-Umwidmung erfordert eine vollständige klinische Validierung und eine regulatorische Prüfung.
<br><br>
<small>Geprüft von: 藥提醒科技有限公司 (yao.care)</small>
</div>
