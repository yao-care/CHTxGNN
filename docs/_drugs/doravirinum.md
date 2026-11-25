---
layout: default
title: Doravirinum
parent: Nur Modellvorhersage (L5)
nav_order: 201
evidence_level: L5
indication_count: 3
drugbank_id: DB12301
monitor_inn: "Doravirine"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-11-25
description: "Doravirinum: vorhergesagte neue Indikation Simiane Immundefizienzvirus-Infektion (simian immunodeficiency virus infection) (Evidenzstufe L5). Ursprüngliche Indikation: HIV-Infektion"
---

# Doravirinum
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

## Doravirinum: Simiane Immundefizienzvirus-Infektion (simian immunodeficiency virus infection)
{: .text-alpha }

### Zusammenfassung

Doravirin ist ein Arzneimittel gegen HIV, das in der Schweiz zugelassen ist. Für die simiane Immundefizienzvirus-Infektion (simian immunodeficiency virus infection) liegt eine reine Modellvorhersage vor. Es gibt dazu keine Studie am Menschen oder am Tier und keine Studie mit Doravirin. Die Evidenz ist daher sehr gering.

---

### Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | HIV-Infektion |
| Vorhergesagte neue Indikation | Simiane Immundefizienzvirus-Infektion (simian immunodeficiency virus infection) |
| TxGNN-Vorhersagewert | 0.9993 |
| Evidenzniveau | L5 |
| Marktstatus Schweiz | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Abwarten |

---

### Warum ist diese Vorhersage plausibel?

Doravirin gehört zu den nicht-nukleosidischen Reverse-Transkriptase-Inhibitoren (NNRTI). Laut den Abschnitten „Mechanism of Action“ und „Microbiology“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Doravirinum (inoffizielle Übersetzung): „Doravirin ist ein antiretroviraler Wirkstoff. […] Doravirin ist ein Pyridinon-Nicht-Nukleosid-Reverse-Transkriptase-Hemmer von HIV-1 und hemmt die HIV-1-Replikation durch nicht-kompetitive Hemmung der HIV-1-Reverse-Transkriptase (RT). Die inhibitorische Konzentration bei 50 % (IC 50 ) von Doravirin für die RNA-abhängige DNA-Polymerisation durch rekombinante Wildtyp-HIV-1-RT betrug in einem biochemischen Assay 12,2±2,0 nM (n=3).“ Englischer Originalwortlaut: "Doravirine is an antiretroviral drug. […] Doravirine is a pyridinone non-nucleoside reverse transcriptase inhibitor of HIV-1 and inhibits HIV-1 replication by non-competitive inhibition of HIV-1 reverse transcriptase (RT). The inhibitory concentration at 50% (IC 50 ) of doravirine for RNA-dependent DNA polymerization of recombinant wild-type HIV-1 RT in a biochemical assay was 12.2±2.0 nM (n=3)." ([DailyMed: Pifeltro (doravirine) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ff06e5cc-f47a-4779-816b-0e5b13e88a25), Fassung vom 2026-07-09; abgerufen am 2026-11-19).

Das simiane Immundefizienzvirus (SIV) ist ein enger Verwandter von HIV und gehört wie dieses zu den Lentiviren. Daraus lässt sich die Vorhersage inhaltlich nachvollziehen. Der hohe Vorhersagewert spiegelt wahrscheinlich vor allem die Nähe zu HIV-bezogenen Einträgen im Modell wider und nicht SIV-spezifische Daten.

Es gibt auch Gründe für Skepsis. NNRTI wirken in der Regel schlecht gegen HIV-2 und SIV, weil sich die Bindungstasche der Reverse Transkriptase strukturell unterscheidet. Ob Doravirin gegen SIV wirkt, müsste daher zuerst im Labor geprüft werden.

---

### Klinische Studien

Derzeit keine verwandten klinischen Studien registriert.

---

### Literaturbelege

| PMID | Jahr | Typ | Zeitschrift | Wichtige Ergebnisse |
|------|-----|------|------|---------|
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Übersichtsarbeit | Current opinion in HIV and AIDS | Bespricht die mögliche Rolle von Islatravir, einem anderen Wirkstoff (Reverse-Transkriptase-Translokationsinhibitor), bei Behandlung und Vorbeugung der HIV-1-Infektion. Keine Daten zu Doravirin und keine Daten zu SIV; nur indirekte Evidenz. |

---

### Marktinformationen Schweiz

<!-- licenses:begin -->

| Zulassungsnummer | Produktname | Kategorie (Heilmittelcode) | Anwendungsgebiet (Swissmedic) | Status |
|------|------|------|------|------|
| 67065 | Pifeltro, Filmtabletten | Synthetikum | HIV-Infektion | Gültig |

Quelle: Swissmedic – Zugelassene Packungen und Zugelassene Arzneimittel (Humanarzneimittel); Produktname, Kategorie und Anwendungsgebiet im Wortlaut der Swissmedic-Listen. „Erloschen“: Gültigkeitsdauer der Zulassung abgelaufen oder in den aktuellen Swissmedic-Listen nicht mehr aufgeführt.

<!-- licenses:end -->

---

### Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
- Die Vorhersage beruht allein auf einem Modell. Es gibt keine Studie, die Doravirin bei SIV untersucht, und die einzige verknüpfte Arbeit betrifft einen anderen Wirkstoff und HIV-1.
- Zusätzlich sprechen die bekannten Unterschiede in der Reverse Transkriptase gegen eine gute Wirksamkeit von NNRTI bei SIV.

**Um fortzufahren, wird Folgendes benötigt:**
- Laborversuche (in vitro), die die Wirkung von Doravirin gegen SIV prüfen
- Angaben zum Wirkmechanismus von Doravirin
- Die Sicherheitsangaben aus der Fachinformation (Warnhinweise und Kontraindikationen), die in den vorliegenden Daten fehlen

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Pifeltro (doravirine) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ff06e5cc-f47a-4779-816b-0e5b13e88a25) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

