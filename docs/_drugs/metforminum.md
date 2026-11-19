---
layout: default
title: Metforminum
parent: Nur Modellvorhersage (L5)
nav_order: 376
evidence_level: L5
indication_count: 5
drugbank_id: DB00331
monitor_inn: "Metformin"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy"]
last_modified_at: 2026-11-16
description: "Metforminum: vorhergesagte neue Indikation Fokales Stiff-Limb-Syndrom (focal stiff limb syndrome) (Evidenzstufe L5). Ursprüngliche Indikation: Orales Antidiabetikum"
---

# Metforminum
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **5** 
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

## Metforminum: Fokales Stiff-Limb-Syndrom (focal stiff limb syndrome)
{: .text-alpha }

### Zusammenfassung

Metformin ist in der Schweiz als orales Antidiabetikum zugelassen. Für das fokale Stiff-Limb-Syndrom (focal stiff limb syndrome) liegt eine reine Modellvorhersage vor. Es gibt dafür keine klinischen Studien und keine Literatur, daher ist die Evidenz sehr schwach (Niveau L5).

---

### Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Orales Antidiabetikum; orales Antidiabetikum |
| Vorhergesagte neue Indikation | Fokales Stiff-Limb-Syndrom (focal stiff limb syndrome) |
| TxGNN-Vorhersagewert | 0.9945 |
| Evidenzniveau | L5 |
| Marktstatus Schweiz | Im Handel (gültige Zulassungen: mindestens 3) |
| Anzahl Zulassungen | mindestens 3 |
| Empfohlene Entscheidung | Abwarten |

---

### Warum ist diese Vorhersage plausibel?

Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Metforminum (inoffizielle Übersetzung): „Metformin ist ein antihyperglykämischer Wirkstoff, der die Glukosetoleranz bei Patienten mit Diabetes mellitus Typ 2 verbessert und sowohl die basale als auch die postprandiale Plasmaglukose senkt. Metformin verringert die hepatische Glukoseproduktion, verringert die intestinale Resorption von Glukose und verbessert die Insulinsensitivität durch Steigerung der peripheren Glukoseaufnahme und -verwertung.“ Englischer Originalwortlaut: "Metformin is an antihyperglycemic agent which improves glucose tolerance in patients with type 2 diabetes mellitus, lowering both basal and postprandial plasma glucose. Metformin decreases hepatic glucose production, decreases intestinal absorption of glucose, and improves insulin sensitivity by increasing peripheral glucose uptake and utilization." ([DailyMed: Metformin Hydrochloride Er (metformin hydrochloride) prescribing information, Leading Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3dca884d-ec44-496f-9eeb-31fd8fa3f574), Fassung vom 2026-09-21; abgerufen am 2026-11-19). Bekannt ist allgemein, dass Metformin die AMPK aktiviert, die Glukosebildung in der Leber senkt und den Komplex I der Mitochondrien beeinflusst. Diese Wirkungen haben keine belegte Verbindung zur Erkrankung.

Das fokale Stiff-Limb-Syndrom ist eine seltene Variante des Stiff-Person-Spektrums. Man vermutet eine Autoimmunstörung der hemmenden GABA- und Glycin-Signalwege. Ein klarer Zusammenhang mit dem Wirkprinzip von Metformin ist aus den vorliegenden Daten nicht erkennbar.

Der hohe Vorhersagewert ist ein reines Rechenergebnis. Er ist identisch mit dem Wert für das klassische Stiff-Person-Syndrom. Das spricht dafür, dass er eine Nähe der beiden Krankheiten im Modell widerspiegelt und keine unabhängige Evidenz darstellt. Die Vorhersage ist deshalb nur eine Hypothese.

---

### Marktinformationen Schweiz

Die Liste kann unvollständig sein (mindestens 3 Zulassungen erfasst).

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| 59099 | Metfo-X 500 mg, Filmtabletten | Synthetika | Orales Antidiabetikum |
| 69689 | Metformin axapharm 500 mg, Filmtabletten | Synthetika | Orales Antidiabetikum |
| 57950 | Metformin-Mepha 500 mg, Filmtabletten | Synthetika | Orales Antidiabetikum |

---

### Sicherheitshinweise

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

---

### Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
- Es gibt weder klinische Studien noch Publikationen zum fokalen Stiff-Limb-Syndrom, und ein plausibler Wirkmechanismus fehlt. Der hohe Vorhersagewert allein reicht nicht als Grundlage für eine Weiterverfolgung.

**Um fortzufahren, wird Folgendes benötigt:**
- Der Wirkmechanismus von Metformin aus einer verlässlichen Quelle (z. B. DrugBank)
- Die Warnhinweise und Kontraindikationen aus der Swissmedic-Fachinformation
- Präklinische oder klinische Daten, die einen Nutzen bei dieser Erkrankung belegen
- Eine Prüfung, ob der identische Wert für das klassische Stiff-Person-Syndrom nur auf der Nähe der Krankheiten im Modell beruht

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Metformin Hydrochloride Er (metformin hydrochloride) prescribing information, Leading Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3dca884d-ec44-496f-9eeb-31fd8fa3f574) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

