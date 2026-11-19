---
layout: default
title: Itraconazolum
parent: Nur Modellvorhersage (L5)
nav_order: 325
evidence_level: L5
indication_count: 1
drugbank_id: DB01167
monitor_inn: "Itraconazole"
predicted_indications: ["pneumocystosis"]
last_modified_at: 2026-11-20
description: "Itraconazolum: vorhergesagte neue Indikation Pneumozystose (pneumocystosis) (Evidenzstufe L5). Ursprüngliche Indikation: Antimykotikum"
---

# Itraconazolum
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

## Itraconazolum: Pneumozystose (pneumocystosis)
{: .text-alpha }

---

### Zusammenfassung

Itraconazol ist ein Antimykotikum, das in der Schweiz in mehreren Kapselpräparaten im Handel ist. Für die Pneumozystose (pneumocystosis) liefert das Modell einen hohen Vorhersagewert, doch die vorliegende Evidenz ist sehr dünn: Es gibt keine registrierten klinischen Studien und keine Publikation, die Itraconazol direkt bei dieser Erkrankung untersucht. Der Mechanismus spricht eher gegen eine Wirksamkeit, daher ist die Vorhersage als rein modellbasiert (L5) einzustufen.

---

### Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Antimykotikum; Vulvovaginalcandiosis |
| Vorhergesagte neue Indikation | Pneumozystose (pneumocystosis) |
| TxGNN-Vorhersagewert | 0.9934 |
| Evidenzniveau | L5 |
| Marktstatus Schweiz | Im Handel (gültige Zulassungen: 7 von 7) |
| Anzahl Zulassungen | 7 (gültig: 7) |
| Empfohlene Entscheidung | Abwarten |

---

### Warum ist diese Vorhersage plausibel?

Itraconazol hemmt das Pilzenzym Lanosterol-14-alpha-Demethylase (CYP51) und blockiert damit die Ergosterol-Synthese. Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Itraconazolum (inoffizielle Übersetzung): „In-vitro-Studien haben gezeigt, dass Itraconazol die Cytochrom-P450-abhängige Synthese von Ergosterol hemmt, einem lebenswichtigen Bestandteil der Zellmembranen von Pilzen.“ Englischer Originalwortlaut: "In vitro studies have demonstrated that itraconazole inhibits the cytochrome P450-dependent synthesis of ergosterol, which is a vital component of fungal cell membranes." ([DailyMed: Sporanox (itraconazole) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a4d555fa-787c-40fb-bb7d-b0d4f7318fd0), Fassung vom 2026-07-13; abgerufen am 2026-11-19).

Bei näherer Betrachtung ist die Plausibilität gering. Pneumocystis jirovecii enthält in der Zellmembran kein Ergosterol, sondern vor allem Cholesterol und verwandte Sterole. Der Azol-Mechanismus ist daher gegen diesen Erreger nicht zu erwarten. Eine Arbeit zur Lanosterol-14-alpha-Demethylase von Pneumocystis carinii (2003) beschreibt zudem eine natürliche Resistenz gegenüber Azolen.

Der hohe Vorhersagewert spiegelt wahrscheinlich Zusammenhänge mit anderen opportunistischen Pilzinfektionen (z. B. Histoplasmose) und mit Prophylaxe-Situationen (Transplantation, HIV, Neutropenie) wider, nicht einen belegten Wirkmechanismus. Standardtherapie und -prophylaxe ist Trimethoprim-Sulfamethoxazol; Alternativen sind Atovaquon, Pentamidin, Dapson und Primaquin-Clindamycin. Itraconazol gehört nicht dazu.

---

### Literaturbelege

Keine der Publikationen untersucht Itraconazol direkt bei Pneumozystose. Die Auswahl zeigt die relevantesten Arbeiten.

| PMID | Jahr | Typ | Zeitschrift | Wichtige Ergebnisse |
|------|-----|------|------|---------|
| [12606318](https://pubmed.ncbi.nlm.nih.gov/12606318/) | 2003 | Mechanismusstudie | American Journal of Respiratory Cell and Molecular Biology | Das Azol-Zielenzym Erg11 von Pneumocystis carinii wurde kloniert; der Erreger ist von Natur aus gegen Azole resistent. |
| [7859871](https://pubmed.ncbi.nlm.nih.gov/7859871/) | 1995 | Kohorte | European Journal of Haematology | 24 Patienten mit akuter myeloischer Leukämie erhielten ambulant Ciprofloxacin, Cotrimoxazol und Itraconazol als Begleittherapie; Itraconazol-Effekt auf Pneumocystis nicht separat untersucht. |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Kohorte | Transplantation Proceedings | Erfahrungen eines Zentrums mit invasiven Pilzinfektionen nach Nierentransplantation. |
| [22273250](https://pubmed.ncbi.nlm.nih.gov/22273250/) | 2012 | Retrospektive Studie | Leukemia & Lymphoma | Nichtbakterielle Infektionen bei 182 Patienten unter Alemtuzumab. |
| [15250025](https://pubmed.ncbi.nlm.nih.gov/15250025/) | 2004 | Übersicht | Clinical Infectious Diseases | Antimikrobielle Prophylaxe bei febriler Neutropenie; Trimethoprim-Sulfamethoxazol schützt wirksam vor Pneumocystis-Pneumonie. |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Übersicht | BMJ Clinical Evidence | Primär- und Sekundärprophylaxe opportunistischer Infektionen bei HIV. |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Übersicht | Drugs | Therapie und Prophylaxe systemischer Protozoeninfektionen, u. a. Pneumocystis carinii. |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Übersicht | Seminars in Respiratory Infections | Infektionen nach Lungentransplantation. |
| [29374650](https://pubmed.ncbi.nlm.nih.gov/29374650/) | 2018 | Fallbericht | BMJ Case Reports | Gleichzeitige Pneumocystis-Pneumonie und Histoplasmose bei einem HIV-Patienten. |
| [14760976](https://pubmed.ncbi.nlm.nih.gov/14760976/) | 2003 | Fallbericht | International Journal of Medical Microbiology | Chronische granulomatöse Lungeninfektion durch Emmonsia sp., zunächst als Pneumocystis-Pneumonie gedeutet. |

---

### Marktinformationen Schweiz

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| 60137 | Itraconazol axapharm, Kapseln | Synthetika | Antimykotikum |
| 49610 | Sporanox, Kapseln | Synthetika | Antimykotikum |
| 57493 | Itraconazol Spirig HC, Kapseln | Synthetika | Antimykotikum |
| 57544 | Itracim, Kapseln | Synthetika | Antimykotikum |
| 53630 | Sporanox G, Kapseln | Synthetika | Vulvovaginalkandidose |
| 59319 | Itraconazol Sandoz eco 100 mg, Kapseln | Synthetika | Antimykotikum |
| 57368 | Itraconazol-Mepha 100, Kapseln | Synthetika | Antimykotikum |

---

### Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
- Der hohe Vorhersagewert (0,9934) wird weder durch Studien noch durch den Wirkmechanismus gestützt; Pneumocystis besitzt kein Ergosterol und gilt als azolresistent.
- Mit Trimethoprim-Sulfamethoxazol und weiteren Alternativen stehen etablierte Behandlungen zur Verfügung.

**Um fortzufahren, wird Folgendes benötigt:**
- Direkte präklinische oder klinische Daten zu Itraconazol bei Pneumozystose
- Eine Fachinformation mit Warnhinweisen und Kontraindikationen für die Sicherheitsbewertung (derzeit nicht verfügbar)
- Angaben zum Wirkmechanismus aus einer verlässlichen Arzneimittelquelle

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Sporanox (itraconazole) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a4d555fa-787c-40fb-bb7d-b0d4f7318fd0) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

