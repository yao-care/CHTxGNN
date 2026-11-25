---
layout: default
title: Dimenhydrinatum
parent: Nur Modellvorhersage (L5)
nav_order: 195
evidence_level: L5
indication_count: 2
drugbank_id: DB00985
monitor_inn: "Dimenhydrinate"
predicted_indications: ["allergic urticaria", "cold urticaria"]
last_modified_at: 2026-11-25
description: "Dimenhydrinatum: vorhergesagte neue Indikation Allergische Urtikaria (allergic urticaria) (Evidenzstufe L5). Ursprüngliche Indikation: maux de voyage"
---

# Dimenhydrinatum
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **2** 
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

## Dimenhydrinatum: Allergische Urtikaria (allergic urticaria)
{: .text-alpha }

### Zusammenfassung

Dimenhydrinat ist ein Salz aus Diphenhydramin und 8-Chlortheophyllin und in der Schweiz zugelassen. Es könnte voraussichtlich bei allergischer Urtikaria (allergic urticaria) wirksam sein, da Diphenhydramin die Histaminwirkung am H1-Rezeptor blockiert. Die Evidenz ist sehr schwach: Es liegt nur eine pharmakokinetische Studie am Hund vor, die keine Wirksamkeitsdaten bei Urtikaria enthält.

---

### Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | maux de voyage |
| Vorhergesagte neue Indikation | Allergische Urtikaria (allergic urticaria) |
| TxGNN-Vorhersagewert | 0.9974 |
| Evidenzniveau | L5 |
| Marktstatus Schweiz | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Abwarten |

---

### Warum ist diese Vorhersage plausibel?

Dimenhydrinat setzt im Körper Diphenhydramin frei, einen H1-Rezeptor-Antagonisten (inverser Agonist) der ersten Generation. Laut dem Abschnitt „Clinical Pharmacology“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Dimenhydrinatum (inoffizielle Übersetzung): „Obwohl der genaue Wirkmechanismus von Dimenhydrinat nicht bekannt ist, übt es eine dämpfende Wirkung auf eine übermäßig stimulierte Labyrinthfunktion aus.“ Englischer Originalwortlaut: "While the precise mode of action of dimenhydrinate is not known, it has a depressant action on hyperstimulated labyrinthine function." ([DailyMed: dimenhydrinate prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bc71539e-1a33-4709-8a24-c2894e8dbc1c), Fassung vom 2025-01-15; abgerufen am 2026-11-19).

Bei allergischer Urtikaria setzen Mastzellen Histamin frei, das Quaddeln und Juckreiz auslöst. Die Blockade des H1-Rezeptors greift an genau dieser Stelle an, weshalb der Mechanismus biologisch nachvollziehbar ist. Der hohe TxGNN-Wert ist jedoch eine rein rechnerische Vorhersage.

Einschränkend gilt: Aktuelle Urtikaria-Leitlinien bevorzugen nicht sedierende H1-Antihistaminika der zweiten Generation. Die Sedierung und die anticholinerge Belastung eines Wirkstoffs der ersten Generation begrenzen seine praktische Rolle.

---

### Literaturbelege

| PMID | Jahr | Typ | Zeitschrift | Wichtige Ergebnisse |
|------|-----|------|------|---------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | Pharmakokinetische Pilotstudie (Hund) | Veterinary Dermatology | Vergleicht Diphenhydramin nach oraler und intravenöser Gabe sowie nach oraler Gabe von Dimenhydrinat bei gesunden Hunden. Hinweis auf eine gute Aufnahme von Diphenhydramin aus Dimenhydrinat; keine Wirksamkeitsdaten bei Urtikaria beim Menschen. |

---

### Marktinformationen Schweiz

<!-- licenses:begin -->

| Zulassungsnummer | Produktname | Kategorie (Heilmittelcode) | Anwendungsgebiet (Swissmedic) | Status |
|------|------|------|------|------|
| 43194 | Trawell 20 mg, gomme à mâcher médicamenteuse | Synthetikum | maux de voyage | Gültig |

Quelle: Swissmedic – Zugelassene Packungen und Zugelassene Arzneimittel (Humanarzneimittel); Produktname, Kategorie und Anwendungsgebiet im Wortlaut der Swissmedic-Listen. „Erloschen“: Gültigkeitsdauer der Zulassung abgelaufen oder in den aktuellen Swissmedic-Listen nicht mehr aufgeführt.

<!-- licenses:end -->

---

### Sicherheitshinweise

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

---

### Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
- Die Vorhersage ist mechanistisch plausibel, aber keine Studie untersucht Dimenhydrinat bei allergischer Urtikaria; das Evidenzniveau bleibt daher L5. Zweitgenerations-Antihistaminika sind etablierte und besser verträgliche Alternativen.

**Um fortzufahren, wird Folgendes benötigt:**
- Klinische Wirksamkeitsdaten zu Dimenhydrinat oder Diphenhydramin bei allergischer Urtikaria, idealerweise im Vergleich mit Zweitgenerations-Antihistaminika
- Sicherheitsinformationen (Warnhinweise und Kontraindikationen) aus der Schweizer Fachinformation
- Angaben zum Wirkmechanismus aus einer Arzneimitteldatenbank

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: dimenhydrinate prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bc71539e-1a33-4709-8a24-c2894e8dbc1c) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

