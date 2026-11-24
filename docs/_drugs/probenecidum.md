---
layout: default
title: Probenecidum
parent: Nur Modellvorhersage (L5)
nav_order: 491
evidence_level: L5
indication_count: 3
drugbank_id: DB01032
monitor_inn: "Probenecid"
predicted_indications: ["hypouricemia, renal", "Lesch-Nyhan syndrome", "hypoxanthine guanine phosphoribosyltransferase partial deficiency"]
last_modified_at: 2026-11-24
description: "Probenecidum: vorhergesagte neue Indikation Renale Hypourikämie (hypouricemia, renal) (Evidenzstufe L5). Ursprüngliche Indikation: Urikosurikum"
---

# Probenecidum
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **3** 
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

## Probenecidum: Renale Hypourikämie (hypouricemia, renal)
{: .text-alpha }

### Zusammenfassung

Probenecid ist in der Schweiz als Urikosurikum zugelassen. Für die vorhergesagte neue Anwendung, die renale Hypourikämie (hypouricemia, renal), liegen keine klinischen Studien vor, und die vorhandene Literatur beschreibt die Erkrankung, nicht aber Probenecid als Behandlung. Die Vorhersage ist daher rein modellbasiert und wirkt mechanistisch widersprüchlich: Das Arzneimittel verstärkt die Harnsäureausscheidung, die bei dieser Erkrankung ohnehin zu hoch ist.

---

### Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Urikosurikum |
| Vorhergesagte neue Indikation | Renale Hypourikämie (hypouricemia, renal) |
| TxGNN-Vorhersagewert | 0.9973 |
| Evidenzniveau | L5 |
| Marktstatus Schweiz | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Abwarten |

---

### Warum ist diese Vorhersage plausibel?

Probenecid hemmt den Harnsäuretransporter URAT1 (SLC22A12) sowie die Transporter OAT1 und OAT3 in der Niere. Dadurch wird weniger Harnsäure aus dem Primärharn zurückgenommen, und die Ausscheidung steigt. Laut dem Abschnitt „Clinical Pharmacology“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Probenecidum (inoffizielle Übersetzung): „Probenecid ist ein urikosurischer und die Nierentubuli blockierender Wirkstoff.“ Englischer Originalwortlaut: "Probenecid is a uricosuric and renal tubular blocking agent." ([DailyMed: probenecid prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=65b4888c-d49a-433f-9bfd-17880ae40069), Fassung vom 2026-11-06; abgerufen am 2026-11-19).

Die renale Hypourikämie beruht meist auf Funktionsverlust-Mutationen in SLC22A12 (URAT1) oder GLUT9. Die Niere scheidet dann zu viel Harnsäure aus, und der Harnsäurespiegel im Blut ist niedrig. Der hohe Vorhersagewert spiegelt vermutlich die enge Verknüpfung beider Themen im Harnsäuretransport wider, nicht einen therapeutischen Nutzen.

Mechanistisch würde Probenecid den Defekt eher nachahmen oder verstärken, als ihn zu behandeln. Plausibler ist eine diagnostische Verwendung: In Fallberichten dient Probenecid zusammen mit Pyrazinamid zur Charakterisierung des Transportdefekts.

---

### Literaturbelege

Keine der Publikationen untersucht Probenecid als Therapie der renalen Hypourikämie. Es handelt sich überwiegend um Übersichtsarbeiten, Fallberichte und genetische Studien. Die Auswahl zeigt die relevantesten Arbeiten.

| PMID | Jahr | Typ | Zeitschrift | Wichtige Ergebnisse |
|------|-----|------|------|---------|
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Übersichtsarbeit | Molecular genetics and metabolism | Die hereditäre renale Hypourikämie beruht meist auf Funktionsverlust-Mutationen im URAT1-Gen (SLC22A12), die zu erhöhter Harnsäureausscheidung führen. |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Übersichtsarbeit | Clinical rheumatology | Aktueller Überblick über Ursachen und Abklärung der Hypourikämie (Serumharnsäure < 2 mg/dl) für die rheumatologische Praxis. |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Kohorte (genetisch) | Journal of the American Society of Nephrology | Untersuchung des SLC22A12-Gens bei 32 Patienten mit idiopathischer renaler Hypourikämie; Zusammenhang zwischen Genveränderungen und Harnsäureausscheidung. |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | Fallbericht/Übersicht | American journal of kidney diseases | Belastungsinduziertes akutes Nierenversagen bei renaler Hypourikämie; Überblick über Vorbeugung und Literatur. |
| [14747372](https://pubmed.ncbi.nlm.nih.gov/14747372/) | 2004 | Präklinisch (Maus) | Journal of the American Society of Nephrology | Funktion und Lokalisation des Harnsäuretransporters in der Mausniere, Modell für das menschliche URAT1. |
| [3442957](https://pubmed.ncbi.nlm.nih.gov/3442957/) | 1987 | Fallbericht | Clinical nephrology | Zwei Patienten ohne Anstieg der Harnsäureclearance nach Probenecid, Hinweis auf einen teilweisen Defekt des Harnsäuretransports. |
| [854144](https://pubmed.ncbi.nlm.nih.gov/854144/) | 1977 | Fallbericht | Nephron | Familiäre Hypourikämie mit abgeschwächter Reaktion der Harnsäureclearance auf Probenecid und Pyrazinamid. |
| [10955943](https://pubmed.ncbi.nlm.nih.gov/10955943/) | 2000 | Fallbericht | Pediatric nephrology | Belastungsinduziertes Nierenversagen; keine Änderung der Harnsäureclearance nach Pyrazinamid oder Probenecid. |
| [667288](https://pubmed.ncbi.nlm.nih.gov/667288/) | 1978 | Fallbericht | Biomedicine | Familie mit genetischer Hypourikämie; Harnsäureausscheidung stieg nach Probenecid um 25 %. |
| [1944743](https://pubmed.ncbi.nlm.nih.gov/1944743/) | 1991 | Fallserie | Nephron | 14 Patienten mit Typ-1-Diabetes und renaler Hypourikämie; Untersuchung der Mechanismen der Harnsäureausscheidung. |

---

### Marktinformationen Schweiz

<!-- licenses:begin -->

| Zulassungsnummer | Produktname | Kategorie (Heilmittelcode) | Anwendungsgebiet (Swissmedic) | Status |
|------|------|------|------|------|
| 57365 | Santuril, Tabletten | Synthetika | Urikosurikum | Gültig |

Quelle: Swissmedic – Zugelassene Packungen und Zugelassene Arzneimittel (Humanarzneimittel); Produktname, Kategorie und Anwendungsgebiet im Wortlaut der Swissmedic-Listen. „Erloschen“: Gültigkeitsdauer der Zulassung abgelaufen oder in den aktuellen Swissmedic-Listen nicht mehr aufgeführt.

<!-- licenses:end -->

---

### Sicherheitshinweise

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

---

### Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
- Es gibt keine klinischen Studien und keine Literatur, die Probenecid als Behandlung der renalen Hypourikämie belegt. Der Wirkmechanismus (Hemmung der Harnsäure-Rückresorption) würde den zugrunde liegenden Defekt eher verstärken als beheben.

**Um fortzufahren, wird Folgendes benötigt:**
- Ein plausibler therapeutischer Mechanismus, der erklärt, warum ein Urikosurikum bei erhöhter Harnsäureausscheidung nützen könnte.
- Direkte klinische oder präklinische Studien zu Probenecid bei renaler Hypourikämie.
- Die Fachinformation von Swissmedic mit Warnhinweisen und Gegenanzeigen, die derzeit fehlt, für die Sicherheitsbewertung.
- Angaben zum Wirkmechanismus aus einer Arzneimitteldatenbank (z. B. DrugBank).

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: probenecid prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=65b4888c-d49a-433f-9bfd-17880ae40069) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

