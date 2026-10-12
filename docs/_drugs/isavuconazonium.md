---
layout: default
title: Isavuconazonium
parent: Nur Modellvorhersage (L5)
nav_order: 59
evidence_level: L5
indication_count: 2
---

# Isavuconazonium
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **2** 
{: .fs-6 .fw-300 }

---

## Inhaltsverzeichnis
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmazeutischer Bewertungsbericht

</div>

# Isavuconazonium: Von Antimykotikum zu Pneumocystose

## Zusammenfassung

Isavuconazonium ist in der Schweiz als Antimykotikum zugelassen. Das Modell TxGNN sagt als neue Indikation Pneumocystose voraus (Vorhersagewert 99,6 %). Dafür liegen weder klinische Studien noch Literatur vor, und der bekannte Wirkmechanismus spricht gegen die biologische Plausibilität. Die Vorhersage beruht allein auf einem Modell (Evidenzniveau L5).

Hinweis: Die zweite Vorhersage, Myzetom (Rang 2), ist plausibler und wird im Fazit als alternative Forschungsfrage genannt.

---

## Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Antimykotikum |
| Vorhergesagte neue Indikation | Pneumocystose |
| TxGNN-Vorhersagewert | 99,6 % |
| Evidenzniveau | L5 |
| Marktstatus Schweiz | Im Handel (Marketed) |
| Anzahl Zulassungen | 2 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage plausibel?

Isavuconazonium ist die Vorstufe (Prodrug) von Isavuconazol. Der Wirkstoff hemmt das Pilzenzym Lanosterol-14-alpha-Demethylase (CYP51) und blockiert dadurch die Bildung von Ergosterol, einem wichtigen Baustein der Pilzzellmembran. Die Angabe zum ursprünglichen Wirkmechanismus fehlt in den Daten; die Beschreibung stützt sich daher auf das bekannte Azol-Prinzip.

Die Vorhersage ist **biologisch wenig plausibel**. Pneumocystis jirovecii enthält in der Zellmembran kein Ergosterol, sondern Cholesterol. Ein Azol-Wirkstoff, der die Ergosterol-Synthese hemmt, sollte daher kaum wirken. Der hohe Vorhersagewert spiegelt wahrscheinlich eine allgemeine Assoziation mit der Klasse der Antimykotika wider und keine echte mechanistische Passung.

Für die zweite Vorhersage, das **Myzetom**, ist die Lage günstiger. Das Eumyzetom wird durch Pilze wie Madurella mycetomatis verursacht, die grundsätzlich auf Azole ansprechen; Itraconazol gehört bereits zur Standardtherapie. Das bakterielle Aktinomyzetom würde dagegen nicht auf den Wirkstoff ansprechen. Diese Einschätzung ist bislang nur indirekt belegt.

---

## Klinische Studien

Derzeit keine verwandten klinischen Studien registriert.

---

## Literaturbelege

Für Pneumocystose: Derzeit keine verwandte Literatur verfügbar.

Für die alternative Vorhersage Myzetom liegt eine indirekte Quelle vor:

| PMID | Jahr | Typ | Zeitschrift | Wichtige Ergebnisse |
|------|-----|------|------|---------|
| [37907954](https://pubmed.ncbi.nlm.nih.gov/37907954/) | 2023 | Übersichtsarbeit | Parasites & Vectors | Überblick über die Pipeline oraler Antiinfektiva für vernachlässigte Tropenkrankheiten (Off-Label-Anwendung); liefert nur indirekten Kontext, keine direkten Daten zu Isavuconazol beim Myzetom. |

---

## Marktinformationen Schweiz

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| 66172 | Cresemba 100 mg, Hartkapseln | Synthetika | Antimykotikum |
| 66173 | Cresemba 200 mg, Pulver für ein Konzentrat zur Herstellung einer Infusionslösung | Synthetika | Antimykotikum |

Zulassungsinhaberin beider Präparate ist Basilea Pharmaceutica International AG, Allschwil.

---

## Sicherheitshinweise

- **Arzneimittelwechselwirkungen**: Insgesamt wurden 100 Wechselwirkungen erfasst. Davon sind hier die wichtigsten aus der Auswahl aufgeführt:
  - **Schwerwiegend (Major)**: Clarithromycin, Eliglustat, Cisapride
  - **Mässig (Moderate)**: unter anderem Hydrocortisone, Dexamethason, Betamethason, Triamcinolon, Budesonid, Metformin, Pioglitazon, Saxagliptin, Linagliptin, Empagliflozin, Loperamid, Bupropion, Aprepitant, Cimetidin, Clotrimazol
  - **Gering (Minor)**: Fidaxomicin

Warnhinweise und Kontraindikationen aus der Fachinformation liegen nicht vor. Bitte beachten Sie die Fachinformation für diese Sicherheitsinformationen.

---

## Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
- Der hohe Modellwert für Pneumocystose wird weder durch Studien noch durch Literatur gestützt. Der Azol-Mechanismus spricht zudem gegen eine Wirksamkeit, weil P. jirovecii kein Ergosterol besitzt.
- Das Myzetom (Eumyzetom) ist als Forschungsfrage sinnvoller, bleibt aber bisher nur indirekt belegt (Evidenzniveau L4).

**Um fortzufahren, wird Folgendes benötigt:**
- Auswertung der Fachinformation von Swissmedic (Warnungen, Kontraindikationen); diese Lücke blockiert derzeit die Sicherheitsprüfung.
- Ergänzung des Wirkmechanismus aus DrugBank.
- Für das Myzetom: In-vitro-Empfindlichkeitsdaten von Madurella mycetomatis gegenüber Isavuconazol und anschliessend frühe klinische Studien.
- Für Pneumocystose: Nur bei neuen experimentellen Hinweisen auf eine Wirksamkeit erneut prüfen.
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

