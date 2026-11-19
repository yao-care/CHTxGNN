---
layout: default
title: Trametinibum
parent: Nur Modellvorhersage (L5)
nav_order: 600
evidence_level: L5
indication_count: 1
drugbank_id: DB08911
monitor_inn: "Trametinib"
predicted_indications: ["choroideremia"]
last_modified_at: 2026-11-16
description: "Trametinibum: vorhergesagte neue Indikation Choroideremie (choroideremia) (Evidenzstufe L5). Ursprüngliche Indikation: Melanom, nicht-kleinzelliges Lungenkarzinom"
---

# Trametinibum
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **1** 
{: .fs-6 .fw-300 }

---

## Inhaltsverzeichnis
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmazeutischer Bewertungsbericht

</div>

## Trametinibum: Choroideremie (choroideremia)
{: .text-alpha }

---

### Zusammenfassung

Trametinib ist ein Arzneimittel, das in der Schweiz unter dem Handelsnamen Mekinist zugelassen ist. Für die Aderhautdystrophie Choroideremie (choroideremia) liegt ein hoher Vorhersagewert vor, doch es gibt weder klinische Studien noch Publikationen, die diese Erkrankung untersuchen. Die Vorhersage beruht daher allein auf einem Modell (Evidenzniveau L5).

---

### Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Melanom, nicht-kleinzelliges Lungenkarzinom |
| Vorhergesagte neue Indikation | Choroideremie (choroideremia) |
| TxGNN-Vorhersagewert | 0.9931 |
| Evidenzniveau | L5 |
| Marktstatus Schweiz | Im Handel (gültige Zulassungen: 2 von 2) |
| Anzahl Zulassungen | 2 (gültig: 2) |
| Empfohlene Entscheidung | Abwarten |

---

### Warum ist diese Vorhersage plausibel?

Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Trametinibum (inoffizielle Übersetzung): „Trametinib ist ein reversibler Inhibitor der Aktivierung der mitogenaktivierten, durch extrazelluläre Signale regulierten Kinase 1 (MEK1) und MEK2 sowie der Kinaseaktivität von MEK1 und MEK2. MEK-Proteine sind vorgeschaltete Regulatoren des Signalwegs der extrazellulären signalregulierten Kinase (ERK), der die Zellproliferation fördert.“ Englischer Originalwortlaut: "Trametinib is a reversible inhibitor of mitogen-activated extracellular signal-regulated kinase 1 (MEK1) and MEK2 activation and of MEK1 and MEK2 kinase activity. MEK proteins are upstream regulators of the extracellular signal-related kinase (ERK) pathway, which promotes cellular proliferation." ([DailyMed: Mekinist (trametinib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0002ad27-779d-42ab-83b5-bc65453412a1), Fassung vom 2026-05-07; abgerufen am 2026-11-19). Allgemein bekannt ist, dass Trametinib die Kinasen MEK1 und MEK2 im MAPK-Signalweg hemmt.

Ein klarer mechanistischer Zusammenhang mit Choroideremie ist nicht erkennbar. Choroideremie ist eine X-chromosomal vererbte Netzhautdegeneration, die durch den Verlust des Gens CHM bzw. des Proteins REP1 verursacht wird. Sie wird nicht durch den MAPK-Signalweg angetrieben. Der hohe Vorhersagewert (0,9931) ist deshalb wahrscheinlich ein Artefakt der Modellberechnung und kein Hinweis auf eine biologisch begründete Wirkung.

Hinzu kommt ein Sicherheitsaspekt: MEK-Hemmer können eine Netzhauterkrankung (MEK-Inhibitor-assoziierte Retinopathie) auslösen. Bei einer bereits degenerativen Netzhauterkrankung wäre dies besonders bedenklich.

---

### Marktinformationen Schweiz

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| 65883 | Mekinist 0.5 mg, Filmtabletten | Synthetika | Melanom, nicht-kleinzelliges Lungenkarzinom |
| 69134 | Mekinist 4.7 mg, Pulver zur Herstellung einer Lösung zum Einnehmen | Synthetika | Melanom, nicht-kleinzelliges Lungenkarzinom |

---

### Zytotoxizität

| Punkt | Inhalt |
|------|------|
| Zytotoxizitätsklassifikation | Zielgerichtete Therapie (MEK-Inhibitor) |

---

### Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
- Für Choroideremie gibt es weder klinische Studien noch Literatur, und ein biologischer Zusammenhang mit dem MAPK-Signalweg ist nicht erkennbar. Das Risiko einer MEK-Inhibitor-assoziierten Retinopathie spricht zusätzlich gegen eine Weiterverfolgung.

**Um fortzufahren, wird Folgendes benötigt:**
- Eine belastbare mechanistische Begründung, warum eine MEK-Hemmung bei Verlust von CHM/REP1 nützlich sein könnte
- Präklinische Daten in geeigneten Modellen der Choroideremie, inklusive Bewertung der Netzhautsicherheit
- Die Sicherheitsangaben (Warnungen, Kontraindikationen) aus der Swissmedic-Fachinformation, die in den vorliegenden Daten fehlen
- Die Angabe des Wirkmechanismus aus DrugBank

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Mekinist (trametinib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0002ad27-779d-42ab-83b5-bc65453412a1) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

