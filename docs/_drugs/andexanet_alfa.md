---
layout: default
title: Andexanet Alfa
parent: Nur Modellvorhersage (L5)
nav_order: 16
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
description: "Andexanet Alfa: vorhergesagte neue Indikation Glanzmann-Thrombasthenie (Evidenzstufe L5). Ursprüngliche Indikation: Antidot gegen Faktor-Xa-Inhibitoren"
monitor_inn: "ANDEXANET ALFA"
predicted_indications: ["Glanzmann thrombasthenia", "primary release disorder of platelets", "pseudo-von Willebrand disease", "hemophilia"]
---

# Andexanet Alfa
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **4** 
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

## Andexanet alfa: Von Antidot gegen Faktor-Xa-Inhibitoren zu Glanzmann-Thrombasthenie
{: .text-alpha }

## Zusammenfassung

Andexanet alfa ist in der Schweiz als Antidot gegen Faktor-Xa-Inhibitoren zugelassen. Das Modell sagt eine mögliche Wirksamkeit bei der Glanzmann-Thrombasthenie voraus, einer angeborenen Störung der Blutplättchenfunktion. Diese Vorhersage beruht ausschliesslich auf einem Modellwert; es gibt weder klinische Studien noch Literatur dazu, und ein plausibler Wirkmechanismus ist nicht erkennbar.

---

## Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Antidot gegen Faktor-Xa-Inhibitoren |
| Vorhergesagte neue Indikation | Glanzmann-Thrombasthenie |
| TxGNN-Vorhersagewert | 0,9977 |
| Evidenzniveau | L5 (nur Modellvorhersage) |
| Marktstatus Schweiz | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage plausibel?

Die Vorhersage ist nach aktueller Datenlage **nicht plausibel begründbar**. Andexanet alfa ist ein rekombinantes, katalytisch inaktives Faktor-Xa-Täuschmolekül. Es bindet Faktor-Xa-Inhibitoren und neutralisiert so deren gerinnungshemmende Wirkung. Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Andexanet Alfa (inoffizielle Übersetzung): „Koagulationsfaktor Xa (rekombinant), inaktiviert-zhzo, entfaltet seine prokoagulatorische Wirkung durch Bindung und Sequestrierung der FXa-Inhibitoren Rivaroxaban und Apixaban. Eine weitere beobachtete prokoagulatorische Wirkung des ANDEXXA-Proteins ist seine Fähigkeit, an den Tissue Factor Pathway Inhibitor (TFPI) zu binden und dessen Aktivität zu hemmen.“ Englischer Originalwortlaut: "Coagulation factor Xa (recombinant), inactivated-zhzo exerts its procoagulant effect by binding and sequestering the FXa inhibitors, rivaroxaban and apixaban. Another observed procoagulant effect of the ANDEXXA protein is its ability to bind to, and inhibit the activity of, Tissue Factor Pathway Inhibitor (TFPI)." ([DailyMed: Andexxa (andexanet alfa) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2d9d90a6-63e6-46ef-96ff-dd6519ae7b6c), Fassung vom 2025-05-23; abgerufen am 2026-11-19).

Die Glanzmann-Thrombasthenie ist dagegen ein angeborener Defekt des Plättchen-Integrins αIIbβ3 (GPIIb/IIIa), der die Plättchenaggregation beeinträchtigt. Ein Zusammenhang zwischen der Aufhebung einer Faktor-Xa-Hemmung und der Korrektur dieses Plättchendefekts ist nicht erkennbar. Der hohe Vorhersagewert ist wahrscheinlich ein Artefakt des TxGNN-Modells (Deep Learning), der auf gemeinsamen Nachbarn im Bereich «Blutstillung/Blutung» beruht.

Weitere vorhergesagte Indikationen mit ähnlich hohen Werten sind die primäre Thrombozyten-Freisetzungsstörung (0,9976), das Pseudo-von-Willebrand-Syndrom (0,9965) und die Hämophilie (0,9910). Auch dafür fehlt ein mechanistischer Zusammenhang. Bei der Hämophilie gibt es zwar neun Publikationen, diese behandeln aber die zugelassene Anwendung von Andexanet alfa oder Laborstörungen durch direkte orale Antikoagulanzien, nicht eine Behandlung der Hämophilie.

---

## Klinische Studien

Derzeit keine verwandten klinischen Studien registriert.

---

## Literaturbelege

Derzeit keine verwandte Literatur verfügbar.

---

## Marktinformationen Schweiz

<!-- licenses:begin -->

| Zulassungsnummer | Produktname | Kategorie (Heilmittelcode) | Anwendungsgebiet (Swissmedic) | Status |
|------|------|------|------|------|
| 67759 | Ondexxya 200 mg, Pulver zur Herstellung einer Infusionslösung | Biotechnologika | Antidot gegen Faktor Xa-Inhibitoren | Gültig |

Quelle: Swissmedic – Zugelassene Packungen und Zugelassene Arzneimittel (Humanarzneimittel); Produktname, Kategorie und Anwendungsgebiet im Wortlaut der Swissmedic-Listen. „Erloschen“: Gültigkeitsdauer der Zulassung abgelaufen oder in den aktuellen Swissmedic-Listen nicht mehr aufgeführt.

<!-- licenses:end -->

---

## Sicherheitshinweise

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

Zusätzlich ist zu beachten: Bei Patientinnen und Patienten mit Gerinnungsstörungen könnte ein thrombotisches Risiko bestehen. Dies wäre eine Sicherheitsfrage und kein Nutzen. Daten zu Arzneimittelwechselwirkungen wurden nicht gefunden.

---

## Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
- Die Vorhersage stützt sich nur auf einen Modellwert (L5). Es gibt keine Studien, keine Literatur und keinen plausiblen Mechanismus.
- Die Sicherheitsdaten aus der Schweizer Fachinformation fehlen. Eine Sicherheitsprüfung ist daher derzeit nicht möglich.

**Um fortzufahren, wird Folgendes benötigt:**
- Auswertung der Schweizer Fachinformation (Warnungen und Kontraindikationen) von der Swissmedic-Website
- Ergänzung des Wirkmechanismus aus DrugBank
- Eine nachvollziehbare mechanistische Begründung für den Einsatz bei Plättchenfunktionsstörungen
- Präklinische oder klinische Daten, die einen Nutzen bei der Glanzmann-Thrombasthenie belegen

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Andexxa (andexanet alfa) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2d9d90a6-63e6-46ef-96ff-dd6519ae7b6c) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

