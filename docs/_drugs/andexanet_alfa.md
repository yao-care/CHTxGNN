---
layout: default
title: Andexanet Alfa
parent: 僅模型預測 (L5)
nav_order: 11
evidence_level: L5
indication_count: 4
---

# Andexanet Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Analysiere das Evidence Pack und erstelle den Bewertungsbericht auf Basis der Vorlage v5.

---

# Andexanet alfa: Von Faktor-Xa-Inhibitor-Antagonisierung zu Glanzmann-Thrombasthenie

---

## Zusammenfassung

Andexanet alfa (DB14562) ist ein rekombinantes, katalytisch inaktives Faktor-Xa-Decoy-Protein, das als spezifisches Antidot bei lebensbedrohlichen Blutungen unter Faktor-Xa-Hemmern (Apixaban, Rivaroxaban) eingesetzt wird – in der Schweiz ist es derzeit jedoch nicht zugelassen. Das TxGNN-Modell sagt mit einem Vorhersagewert von 99,77 % eine mögliche Anwendung bei Glanzmann-Thrombasthenie voraus, einer seltenen angeborenen Störung der Thrombozytenaggregation durch GPIIb/IIIa-Defekt. Die Evidenzgrundlage beschränkt sich ausschliesslich auf die Modellvorhersage (Evidenzniveau L5) ohne klinische Studien oder Literaturbelege; ein biologisch plausibler Wirkungsmechanismus für diese Indikation konnte nicht identifiziert werden.

---

## Kurzübersicht

| Punkt | Inhalt |
|---|---|
| Ursprüngliche Indikation | Reversal-Therapie bei Faktor-Xa-Hemmer-bedingten Blutungen (in der Schweiz nicht zugelassen) |
| Vorhergesagte neue Indikation | Glanzmann-Thrombasthenie |
| TxGNN-Vorhersagewert | 99,77 % |
| Evidenzniveau | L5 – Ausschliesslich Modellvorhersage, keine klinischen Studien vorhanden |
| Marktstatus Schweiz | Nicht zugelassen (Swissmedic) |
| Anzahl Zulassungen | 0 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage plausibel?

Andexanet alfa wirkt als Decoy-Protein der sekundären Hämostase: Es bindet kompetitiv an Faktor-Xa-Hemmer (Apixaban, Rivaroxaban) und neutralisiert deren antikoagulante Wirkung. Als sekundären Effekt bindet es auch an TFPI (Tissue Factor Pathway Inhibitor), den wichtigsten endogenen Inhibitor des extrinsischen Gerinnungswegs. Über diesen TFPI-Bindungseffekt könnte theoretisch die Thrombinbildung verstärkt werden – ein Konzept, das bei der Entwicklung spezifischer Anti-TFPI-Antikörper (Marstacimab, Concizumab) für die Hämophiliebehandlung gezielt verfolgt wurde. Der TFPI-Effekt von Andexanet alfa ist jedoch eine nicht beabsichtigte Nebenwirkung; Dosis-Wirkungs-Beziehung, Dauer und klinische Relevanz bei anderen Erkrankungen als der Faktor-Xa-Hemmung sind nicht untersucht.

Glanzmann-Thrombasthenie ist dagegen eine Erkrankung der **primären Hämostase**: Ein angeborener Defekt im GPIIb/IIIa-Rezeptor (Integrin αIIbβ3) verhindert die Fibrinogenbindung und damit die Aggregation von Thrombozyten. Dieser Signalweg – Thrombozytenaggregation über Fibrinogen – hat keine bekannte Überschneidung mit der FXa/TFPI-Achse, auf die Andexanet alfa ausschliesslich wirkt. Die etablierten Behandlungen der Glanzmann-Thrombasthenie (Thrombozytentransfusionen, rekombinanter FVIIa) betreffen andere Ebenen der Blutstillung, die von Andexanet alfa nicht beeinflusst werden.

Der hohe TxGNN-Vorhersagewert von 99,77 % geht wahrscheinlich auf eine **Übergeneralisierung im Wissens-Graphen** zurück: Andexanet alfa und Glanzmann-Thrombasthenie teilen den übergeordneten Knoten «hämorrhagische Erkrankungen», was zu einer scheinbar hohen Modellaffinität führt, ohne dass ein echter mechanistischer Zusammenhang besteht. Nach aktuellem Kenntnisstand ist eine klinische Wirksamkeit von Andexanet alfa bei Glanzmann-Thrombasthenie biologisch nicht begründbar.

---

## Klinische Studien

Derzeit keine verwandten klinischen Studien registriert.

---

## Literaturbelege

Derzeit keine verwandte Literatur verfügbar.

---

## Marktinformationen Schweiz

Andexanet alfa ist in der Schweiz nicht zugelassen. Die Swissmedic-Datenbank verzeichnet keine Zulassungen für diesen Wirkstoff (Stand: Mai 2026). Eine Marktübersicht kann erst nach Einreichung eines Zulassungsgesuchs erstellt werden.

---

## Sicherheitshinweise

> Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

---

## Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
- Die TxGNN-Vorhersage beruht ausschliesslich auf einer Modellbefund-Ebene (L5) ohne jegliche klinische oder präklinische Belege. Der Wirkungsmechanismus von Andexanet alfa (FXa-Antagonisierung / TFPI-Bindung → sekundäre Hämostase) und die Pathophysiologie der Glanzmann-Thrombasthenie (GPIIb/IIIa-Defekt → primäre Hämostase) liegen auf biologisch getrennten Ebenen; ein plausibler Wirkungsweg ist nicht erkennbar.

**Um fortzufahren, wird Folgendes benötigt:**
- Erhebung der vollständigen Sicherheitsdaten und des Wirkungsmechanismus (DrugBank-API-Abfrage, Swissmedic-Fachinformation)
- Überprüfung der TxGNN-Modellarchitektur auf systematische Übergeneralisierung im Bereich hämorrhagischer Erkrankungen («Blutungs-Cluster»-Problem)
- Präklinische Mechanismus-Studien, falls nachträglich doch ein Wirkungsweg auf die Thrombozytenfunktion identifiziert werden sollte
- Für klinisch relevantere Umwidmungskandidaten: Fokus auf Indikationen entlang der Gerinnungskaskade (z.B. perioperative Antikoagulanzienumkehr, Blutungsmanagement bei Leberzirrhose) sowie Überprüfung der Indikation **Hämophilie** (Rank 4, Evidenzniveau L4), die eine schwache, aber theoretisch nachvollziehbare TFPI-basierte Rationale aufweist
## Haftungsausschluss

Diese Vorhersagen dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

