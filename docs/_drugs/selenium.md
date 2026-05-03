---
layout: default
title: Selenium
parent: 僅模型預測 (L5)
nav_order: 16
evidence_level: L5
indication_count: 1
---

# Selenium
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

Ich verwende die `txgnn-pipeline`-Skill-Informationen und erstelle nun den Bewertungsbericht auf Basis des bereitgestellten Evidence Packs.

---

# Selenium: Von Selenmangel zu Sklerosierender Cholangitis

## Zusammenfassung

Selenium ist ein essenzielles Spurenelement, das primär zur Behandlung von Selenmangel und als antioxidativer Kofaktor in der Ernährungsmedizin eingesetzt wird. TxGNN-Modellvorhersagen mit einem Score von 99,04 % deuten auf ein potenzielles therapeutisches Potenzial bei primärer sklerosierender Cholangitis (PSC) hin – einer chronisch-fibrosierenden Lebererkrankung mit ausgeprägtem oxidativen Stressmuster. Die gesamte vorliegende Evidenz stammt jedoch ausschliesslich aus Beobachtungsstudien und Tiermodellen (Evidenzniveau L4); interventionelle Humanstudien existieren derzeit nicht.

---

## Kurzübersicht

| Punkt | Inhalt |
|---|---|
| Ursprüngliche Indikation | Selenmangel / Spurenelementsubstitution |
| Vorhergesagte neue Indikation | Sklerosierende Cholangitis (*Sclerosing Cholangitis*) |
| TxGNN-Vorhersagewert | 99,04 % |
| Evidenzniveau | L4 – Beobachtungsstudien / Mechanismusstudien |
| Marktstatus Schweiz | Nicht zugelassen |
| Anzahl Zulassungen | 0 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage plausibel?

Selenium ist ein unverzichtbarer Kofaktor für zwei zentrale antioxidative Enzymsysteme: Glutathionperoxidase (GPx) und Thioredoxinreduktase (TrxR). Über die Elimination reaktiver Sauerstoffspezies (ROS) entfaltet Selenium sowohl antioxidative als auch antifibrotische Wirkungen auf Gewebeebene. Obwohl der spezifische Wirkmechanismus aus den vorliegenden Daten nicht vollständig dokumentiert werden konnte, ist dieser Zusammenhang in der publizierten Fachliteratur gut belegt.

Die primäre sklerosierende Cholangitis ist pathophysiologisch durch eine cholestatisch-induzierte, persistierende oxidative Stressantwort geprägt, die als zentraler Treiber der Gallengangfibrose und Krankheitsprogression gilt. PMID 9053974 dokumentiert direkt veränderte Selenretentionsmuster in der Leber von 32 PSC-Patienten und liefert damit einen biologisch plausiblen Hinweis auf eine pathophysiologische Verbindung zwischen gestörtem Selenmetabolismus und PSC-Krankheitsgeschehen.

Der hohe TxGNN-Score (0,9904) reflektiert wahrscheinlich, dass das Modell eine gemeinsame GPx/Oxidativer-Stress-Signatur zwischen Selenium und PSC erkannt hat. Die bisherige Evidenz bleibt jedoch rein beobachtend oder indirekt – es existieren keine interventionellen Studien mit Selenium bei PSC-Patienten. Ob die Korrektur des Selenstatus einen therapeutischen Nutzen bietet, lässt sich auf dieser Datenbasis nicht beurteilen.

---

## Klinische Studien

Derzeit keine verwandten klinischen Studien registriert.

---

## Literaturbelege

| PMID | Jahr | Typ | Zeitschrift | Wichtige Ergebnisse |
|---|---|---|---|---|
| [9053974](https://pubmed.ncbi.nlm.nih.gov/9053974/) | 1995 | Beobachtungsstudie / Fallserie | *Scandinavian Journal of Gastroenterology* | Nachweis abnormer Kupfer- und Selenretention in der Leber bei 32 PSC-Patienten; direkte Evidenz für veränderten Selenmetabolismus als biologisch relevantes Merkmal der PSC |
| [29148959](https://pubmed.ncbi.nlm.nih.gov/29148959/) | 2017 | Klinische Beobachtung | *JPEN – Journal of Parenteral and Enteral Nutrition* | Oxidativer Stress und geschwächte antioxidative Abwehrmechanismen als Pathogenesefaktoren bei cholestatischen Erkrankungen; deutet auf eine potenzielle Rolle von Antioxidantien wie Selenium hin |
| [39601354](https://pubmed.ncbi.nlm.nih.gov/39601354/) | 2025 | Querschnittsstudie | *Liver International* | PSC-Patienten zeigen mangelhaften Konsum fettlöslicher Vitamine und insgesamt schlechte Ernährungsqualität im Vergleich zu den Nordischen Ernährungsempfehlungen 2023 (NNR2023) |
| [17109383](https://pubmed.ncbi.nlm.nih.gov/17109383/) | 2006 | Tierstudie (Proteomik) | *Proteomics* | Vergleichende Proteomanalyse in murinen Modellen für toxisch induzierte Fibrose und sklerosierende Cholangitis; liefert mechanistischen Kontext für antifibrotische Therapieansätze |
| [18941372](https://pubmed.ncbi.nlm.nih.gov/18941372/) | 2008 | Narrativer Review | *European Journal of Cancer Prevention* | Übersicht zu chemopreventiven Wirkstoffen bei kolorektalem Karzinom; Selenium als Kandidat im Kontext antioxidativer Chemoprotektion erwähnt |

---

## Sicherheitshinweise

> Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

---

## Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
- Die TxGNN-Vorhersage ist mechanistisch plausibel (Selenium als GPx/TrxR-Kofaktor, oxidativer Stress als zentraler PSC-Pathomechanismus), jedoch stützt sich die gesamte verfügbare Evidenz auf Beobachtungsstudien und Tiermodelle (L4) – ohne jegliche interventionelle Humanstudie. Zur Weiterentwicklung dieser Hypothese sind zunächst präklinische Interventionsstudien erforderlich.

**Um fortzufahren, wird Folgendes benötigt:**
- Systematische Literaturrecherche zu Selenium-Supplementation bei Lebererkrankungen und cholestatischen Zuständen (DG002 schliessen: MOA über DrugBank-Abfrage verifizieren)
- Präklinische Proof-of-Concept-Studien in PSC-Tiermodellen mit Selenium als aktive Intervention
- Ermittlung des optimalen Dosierungsbereichs und der hepatischen Bioverfügbarkeit für PSC-relevante Serumspiegel
- Beantragung einer Swissmedic-Beratungsanfrage zur Zulassungsfähigkeit als Arzneimittelkandidaten (aktuell: keine Zulassung in der Schweiz)
## Haftungsausschluss

Diese Vorhersagen dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

