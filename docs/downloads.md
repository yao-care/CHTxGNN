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
