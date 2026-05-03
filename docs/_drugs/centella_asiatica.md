---
layout: default
title: Centella Asiatica
parent: 僅模型預測 (L5)
nav_order: 12
evidence_level: L5
indication_count: 3
---

# Centella Asiatica
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Ich verwende den `txgnn-pipeline`-Skill für die korrekte Verarbeitung. Da dieser keine zusätzlichen Formatierungsregeln für die Berichterstellung vorgibt, folge ich direkt dem definierten Ausgabeformat aus dem Systemprompt.

---

# Centella asiatica: Von traditioneller Heilpflanze zu Insomnie

## Zusammenfassung

Centella asiatica (Gotu Kola) ist eine traditionelle Heilpflanze aus der Ayurveda- und traditionellen chinesischen Medizin, die seit Jahrhunderten bei Wundheilung, Hauterkrankungen sowie neuropsychiatrischen Beschwerden eingesetzt wird. Das TxGNN-Modell prognostiziert Insomnie als führende neue therapeutische Indikation mit einem Vorhersagewert von 99,94 %, gestützt auf neuroprotektive und sedierende Wirkeigenschaften der enthaltenen Triterpene. Die verfügbare Evidenz beschränkt sich jedoch ausschliesslich auf präklinische Tiermodelle; randomisierte klinische Studien beim Menschen für diese Indikation fehlen derzeit vollständig.

---

## Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Traditionelle Anwendung: Wundheilung, Hauterkrankungen, neuropsychiatrische Beschwerden |
| Vorhergesagte neue Indikation | Insomnie |
| TxGNN-Vorhersagewert | 99,94 % |
| Evidenzniveau | L4 – Präklinische Studien / Mechanismusstudien |
| Marktstatus Schweiz | Nicht zugelassen |
| Anzahl Zulassungen | 0 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage plausibel?

Centella asiatica enthält eine Reihe aktiver Triterpene – insbesondere Asiaticoside, Asiatinsäure und Madecassoside – die in mehreren präklinischen Studien neuroprotektive und sedierende Eigenschaften gezeigt haben. Eine Schlüsselstudie im Zebrafischmodell (PMID 38812527) demonstrierte, dass ein Ethanolextrakt von CA Insomnie-ähnliche Verhaltensweisen durch Hemmung des Orexin/Hypocretin-Signalwegs sowie der nachgeschalteten ERK1/2-, Akt- und p38-MAPK-Pfade signifikant reduzieren kann. Diese Signalwege spielen eine zentrale Rolle in der Regulation des Schlaf-Wach-Rhythmus.

Ergänzend weisen biochemische In-vitro-Studien auf eine negative Modulation von GABA-A-Rezeptoren durch die Ursantriterpenoide Asiatinsäure und Madecassinsäure hin (PMID 27062315, 26016167), was dem Wirkmechanismus klassischer Sedativa und Anxiolytika ähnelt. Die enge mechanistische Überlappung zwischen Insomnie und Angststörungen – beide Indikationen involvieren GABAerge Neurotransmission und den Orexin-Signalweg – erklärt, warum TxGNN sowohl Insomnie (Rang 1) als auch Angst (Rang 2) und Schlafinitiations- und -aufrechterhaltungsstörungen (Rang 3) in der Spitzengruppe der Vorhersagen platziert.

Die biologische Plausibilität ist damit grundsätzlich gegeben, beruht jedoch ausschliesslich auf Tier- und Zellmodellen. Ein klinischer Wirksamkeitsnachweis beim Menschen erfordert kontrollierte Humanstudien.

---

## Klinische Studien

| Studiennummer | Phase | Status | Teilnehmer | Wichtige Ergebnisse |
|---------|------|------|------|---------|
| [NCT04872946](https://clinicaltrials.gov/study/NCT04872946) | NA | Abgeschlossen | 74 | Untersuchung eines oralen Inner-Calm-Supplements und eines topischen Super-Calm-Produkts auf Hautgesundheit und allgemeines Wohlbefinden (Rötung, Hautempfindlichkeit). Insomnie ist kein primärer Endpunkt; der Bezug zur Indikation Schlafstörung ist gering (Relevanzgrad C). |
| [NCT07274371](https://clinicaltrials.gov/study/NCT07274371) | NA | Aktiv (keine Rekrutierung) | 30 | Pilot-RCT bei perimenopausalen Frauen (40–55 Jahre): nächtliche 10-minütige Fussmassage mit Brahmi-Gotu-Kola-Öl vs. Bio-Sesamöl als Kontrolle. Schlafqualität und Stimmungsstörungen als primäre Endpunkte; Applikation topisch (kein orales CA), Stichprobe klein (Relevanzgrad B). |

---

## Literaturbelege

| PMID | Jahr | Typ | Zeitschrift | Wichtige Ergebnisse |
|------|-----|------|------|---------|
| [38812527](https://pubmed.ncbi.nlm.nih.gov/38812527/) | 2024 | Tierstudie (Zebrafischmodell) | F1000Research | CA-Ethanolextrakt reduziert Insomnie-Verhalten bei Zebrafischlarven durch Hemmung von Orexin, ERK1/2, Akt und p38-MAPK. Liefert die mechanistische Grundlage für die Insomnie-Vorhersage; keine Humanübertragbarkeit ohne weitere klinische Studien. |

---

## Sicherheitshinweise

> Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

---

## Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
- Die einzige direkt relevante Evidenz für die Insomnie-Indikation stammt aus einem Zebrafisch-Tiermodell (L4); klinische Humanstudien mit schlafspezifischen Endpunkten fehlen vollständig, weshalb eine gezielte Weiterentwicklung dieser Indikation verfrüht wäre. Parallel dazu bietet die Angst-Indikation (Rang 2, L3-Evidenz, Empfehlung „Proceed with Guardrails") eine deutlich solidere klinische Grundlage und sollte prioritär weiterverfolgt werden.

**Um fortzufahren, wird Folgendes benötigt:**
- Klärung des fehlenden Wirkmechanismus (DG002): Abfrage der vollständigen MOA-Daten bei DrugBank (DB14256)
- Klärung der Sicherheitsdaten (DG001): Herunterladen und Auswertung der Fachinformation (Swissmedic / TFDA)
- Identifikation oder Initiierung einer humanen Pilotstudie (Phase 1/2) zur oralen CA-Supplementation bei primärer Insomnie mit validierten Schlafendpunkten (z. B. PSQI, Aktigraphie, Polysomnographie)
- Prüfung optimaler Darreichungsform (oral), standardisiertem Extrakt (z. B. TECA) und Dosierung für die Schlafindikation
- Bevorzugte Weiterentwicklung der Angst-Indikation (L3) als mechanistisch verwandten Brückennachweis für Schlafstörungen
## Haftungsausschluss

Diese Vorhersagen dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

