---
layout: default
title: Cisatracurium
parent: 僅模型預測 (L5)
nav_order: 13
evidence_level: L5
indication_count: 10
---

# Cisatracurium
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

Der `txgnn-pipeline`-Skill ist relevant – es handelt sich um einen Bewertungsbericht im TxGNN-Ökosystem. Ich fahre nun mit der Berichtserstellung gemäss dem definierten Ausgabeformat fort.

---

# Cisatracurium: Von Neuromuskulärer Blockade zu Cauda-equina-Syndrom

## Zusammenfassung

Cisatracurium ist ein nicht-depolarisierendes neuromuskuläres Blockierungsmittel, das in der Anästhesie zur Muskelrelaxation bei der endotrachealen Intubation sowie zur Erleichterung der mechanischen Beatmung auf der Intensivstation eingesetzt wird. Das TxGNN-Modell sagt mit einem Konfidenzwert von 99,99 % eine potenzielle Wirksamkeit beim Cauda-equina-Syndrom voraus. Die vorhandene Evidenz beschränkt sich jedoch ausschliesslich auf die Modellvorhersage (Evidenzniveau L5) – es existieren weder klinische Studien noch Literaturbelege, die diese Indikation stützen.

---

## Kurzübersicht

| Punkt | Inhalt |
|---|---|
| Ursprüngliche Indikation | Neuromuskuläre Blockade (Anästhesie-Induktion, endotracheale Intubation, Erleichterung der mechanischen Beatmung) |
| Vorhergesagte neue Indikation | Cauda-equina-Syndrom |
| TxGNN-Vorhersagewert | 99,99 % |
| Evidenzniveau | L5 |
| Marktstatus Schweiz | Nicht zugelassen |
| Anzahl Zulassungen | 0 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage plausibel?

Cisatracurium blockiert kompetitiv und reversibel die nikotinischen Acetylcholinrezeptoren (nAChR) an der neuromuskulären Endplatte des Skelettmuskels. Diese Blockade unterbricht die Signalübertragung zwischen motorischen Nervenendigungen und Muskelfasern und führt zu einer zeitlich begrenzten schlaffen Lähmung. Der Wirkstoff wird ausschliesslich intravenös verabreicht, wirkt rein peripher und überquert die Blut-Hirn-Schranke nicht.

Das Cauda-equina-Syndrom entsteht durch mechanische Kompression der im Lumbalkanal verlaufenden Nervenwurzeln (L2–S5), typischerweise infolge eines grossen Bandscheibenvorfalls, einer spinalen Stenose oder eines Tumors. Es äussert sich durch Blasen-Darm-Dysfunktion, Satteltaub­heit sowie motorische und sensible Ausfälle der unteren Extremitäten. Die einzig wirksame Behandlung ist die notfallmässige chirurgische Dekompression.

Ein biologisch plausibler Wirkungsmechanismus von Cisatracurium beim Cauda-equina-Syndrom ist nicht erkennbar. Die Blockade von nAChR an der peripheren Endplatte beeinflusst weder die Nervenwurzelkompression noch die damit verbundenen Entzündungs- oder ischämischen Prozesse. Die hohe TxGNN-Konfidenz ist mit hoher Wahrscheinlichkeit auf eine Graphennähe im Wissensgrafen zurückzuführen (falsch-positives Signal durch Knotennähe), und nicht auf eine echte pharmakologische Wirksamkeit.

---

## Klinische Studien

Derzeit keine verwandten klinischen Studien registriert.

---

## Literaturbelege

Derzeit keine verwandte Literatur verfügbar.

---

## Sicherheitshinweise

> Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

---

## Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
- Sämtliche TxGNN-Vorhersagen für Cisatracurium erreichen lediglich Evidenzniveau L5 (reine Modellvorhersage ohne klinische oder präklinische Bestätigung). Der periphere nAChR-Wirkmechanismus weist keine biologisch plausible Verbindung zur Pathophysiologie des Cauda-equina-Syndroms auf, das ausschliesslich durch chirurgische Dekompression behandelt wird.

**Um fortzufahren, wird Folgendes benötigt:**
- Schliessung der MOA-Datenlücke: vollständiges Wirkstoffprofil aus DrugBank und Fachinformation erfassen
- Sicherheitsprofil (Warnhinweise, Kontraindikationen) aus der offiziellen Fachinformation (z. B. EMA EPAR oder Swissmedic-Dossier) dokumentieren
- Präklinische mechanistische Studien zum Zusammenhang zwischen nAChR-Modulation und spinaler Nervenwurzel­kompression als Voraussetzung für jede weitere Bewertung
## Haftungsausschluss

Diese Vorhersagen dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

