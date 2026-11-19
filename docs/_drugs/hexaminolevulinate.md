---
layout: default
title: Hexaminolevulinate
parent: Nur Modellvorhersage (L5)
nav_order: 55
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
description: "Hexaminolevulinate: vorhergesagte neue Indikation Bronchitis (Evidenzstufe L5). Ursprüngliche Indikation: Diagnostikum zur Fluoreszenz-Zystoskopie"
monitor_inn: "hexaminolevulinate"
predicted_indications: ["bronchitis"]
---

# Hexaminolevulinate
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

## Hexaminolevulinat: Von Fluoreszenz-Zystoskopie (Diagnostikum) zu Bronchitis
{: .text-alpha }

---

### Zusammenfassung

Hexaminolevulinat wird in der Schweiz als Diagnostikum für die Fluoreszenz-Zystoskopie eingesetzt. Ein Modell (TxGNN) sagt nun eine mögliche Eignung bei Bronchitis voraus. Diese Vorhersage beruht ausschliesslich auf einem Modellwert: Es liegen weder klinische Studien noch Literatur vor, und ein plausibler Wirkmechanismus ist nicht erkennbar.

---

### Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Diagnostikum zur Fluoreszenz-Zystoskopie |
| Vorhergesagte neue Indikation | Bronchitis |
| TxGNN-Vorhersagewert | 0,9906 |
| Evidenzniveau | L5 (nur Modellvorhersage, keine tatsächlichen Studien) |
| Marktstatus Schweiz | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Abwarten |

---

### Warum ist diese Vorhersage plausibel?

Die Plausibilität ist aktuell gering. Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Hexaminolevulinate (inoffizielle Übersetzung): „Hexaminolevulinat ist ein Ester der Häm-Vorstufe Aminolävulinsäure. Nach der Instillation in die Harnblase dringt Hexaminolevulinat in die Blasenschleimhaut ein und gelangt vermutlich in den Intrazellularraum der Schleimhautzellen, wo es als Vorstufe für die Bildung des photoaktiven Zwischenprodukts Protoporphyrin IX (PpIX) und anderer photoaktiver Porphyrine (PAPs) verwendet wird.“ Englischer Originalwortlaut: "Hexaminolevulinate is an ester of the heme precursor, aminolevulinic acid. After bladder instillation, hexaminolevulinate enters the bladder mucosa and is proposed to enter the intracellular space of mucosal cells where it is used as a precursor in the formation of the photoactive intermediate protoporphyrin IX (PpIX) and other photoactive porphyrins (PAPs)." ([DailyMed: Cysview (hexaminolevulinate hydrochloride) prescribing information, Photocure Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5aeed40d-6841-4adf-8940-f51d439fdfa3), Fassung vom 2026-06-03; abgerufen am 2026-11-19). Bekannt ist, dass Hexaminolevulinat eine Vorstufe von Protoporphyrin IX (PpIX) ist. Es wird bevorzugt von veränderten Urothelzellen aufgenommen und in PpIX umgewandelt. Unter Blaulicht fluoresziert PpIX, wodurch Tumorareale in der Blase sichtbar werden.

Zwischen der ursprünglichen Anwendung (Darstellung von Blasentumoren) und Bronchitis (entzündliche oder infektiöse Erkrankung der Atemwege) lässt sich aus den vorliegenden Daten keine sinnvolle Verbindung herleiten. Denkbar wäre allenfalls ein photodynamischer antimikrobieller Effekt. Das ist jedoch spekulativ, durch keine Daten gestützt und für ein in die Blase eingebrachtes Diagnostikum kaum praktikabel.

Der hohe Vorhersagewert allein ist kein Beleg. Der Wert stammt vom TxGNN-Modell (Deep Learning) und kann Ähnlichkeiten widerspiegeln, die das Modell zwischen verwandten Erkrankungen gelernt hat, nicht biologische Evidenz.

---

### Klinische Studien

Derzeit keine verwandten klinischen Studien registriert

---

### Literaturbelege

Derzeit keine verwandte Literatur verfügbar

---

### Marktinformationen Schweiz

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| 58015 | Hexvix, Pulver und Lösungsmittel zur Herstellung einer Fertigspritze zur intravesikalen Anwendung | Synthetika | Diagnostikum zur Fluoreszenz-Zystoskopie |

---

### Sicherheitshinweise

- **Arzneimittelwechselwirkungen**: Eine Wechselwirkung der Schweregrad-Stufe «Major» ist verzeichnet, und zwar mit **Valrubicin** (Quelle: DDInter).

Für weitere Sicherheitsinformationen beachten Sie bitte die Fachinformation.

---

### Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
- Die Vorhersage stützt sich allein auf einen Modellwert (L5). Es gibt weder Studien noch Literatur, und ein plausibler Mechanismus für Bronchitis fehlt.
- Zudem ist Hexaminolevulinat ein intravesikal angewendetes Diagnostikum. Die Anwendungsart ist mit einer Behandlung der Atemwege kaum vereinbar.

**Um fortzufahren, wird Folgendes benötigt:**
- Wirkmechanismus aus DrugBank ergänzen
- Warnhinweise und Kontraindikationen aus der Swissmedic-Fachinformation auswerten (derzeit blockierende Datenlücke für die Sicherheitsprüfung)
- Systematische Literatur- und Studienrecherche zu einem möglichen Zusammenhang mit Bronchitis
- Prüfung der Anwendungswege (Routenkompatibilität), die derzeit offen ist
- Präklinische Hinweise auf einen photodynamischen antimikrobiellen Effekt in den Atemwegen, bevor eine weitere Verfolgung erwogen wird

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Cysview (hexaminolevulinate hydrochloride) prescribing information, Photocure Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5aeed40d-6841-4adf-8940-f51d439fdfa3) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

