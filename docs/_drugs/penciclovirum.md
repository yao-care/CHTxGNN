---
layout: default
title: Penciclovirum
parent: Nur Modellvorhersage (L5)
nav_order: 452
evidence_level: L5
indication_count: 1
drugbank_id: DB00299
monitor_inn: "Penciclovir"
predicted_indications: ["fascioliasis"]
last_modified_at: 2026-11-24
description: "Penciclovirum: vorhergesagte neue Indikation Fasziolose (fascioliasis) (Evidenzstufe L5). Ursprüngliche Indikation: Herpes labialis"
---

# Penciclovirum
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

## Penciclovirum: Fasziolose (fascioliasis)
{: .text-alpha }

### Zusammenfassung

Penciclovir ist ein antivirales Arzneimittel, das in der Schweiz als Creme gegen Lippenherpes im Handel ist. Für die vorhergesagte neue Indikation Fasziolose (fascioliasis) liegt ein hoher TxGNN-Vorhersagewert vor, aber keine klinischen Studien und keine Literatur. Die Evidenz beruht allein auf der Modellvorhersage (Evidenzniveau L5).

---

### Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Herpes labialis |
| Vorhergesagte neue Indikation | Fasziolose (fascioliasis) |
| TxGNN-Vorhersagewert | 0.9906 |
| Evidenzniveau | L5 |
| Marktstatus Schweiz | Im Handel (gültige Zulassungen: 2 von 2) |
| Anzahl Zulassungen | 2 (gültig: 2) |
| Empfohlene Entscheidung | Abwarten |

---

### Warum ist diese Vorhersage plausibel?

Die Plausibilität ist gering. Laut den Abschnitten „Mechanism of Action“ und „Microbiology“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Penciclovirum (inoffizielle Übersetzung): „Penciclovir ist ein antiviraler Wirkstoff mit Aktivität gegen Alpha-Herpesviren. […] Penciclovir weist eine hemmende Aktivität gegen Herpes-simplex-Virus Typ 1 (HSV-1) und Typ 2 (HSV-2) auf. In mit HSV-1 oder HSV-2 infizierten Zellen phosphoryliert die virale Thymidinkinase Penciclovir zu einer Monophosphatform, die ihrerseits durch zelluläre Kinasen in die aktive Form Penciclovir-Triphosphat umgewandelt wird.“ Englischer Originalwortlaut: "Penciclovir is an antiviral agent active against alpha herpes viruses. […] Penciclovir has inhibitory activity against herpes simplex virus types 1 (HSV-1) and 2 (HSV-2). In cells infected with HSV-1 or HSV-2, the viral thymidine kinase phosphorylates penciclovir to a monophosphate form that, in turn, is converted by cellular kinases to the active form penciclovir triphosphate." ([DailyMed: Denavir (penciclovir) prescribing information, Mylan Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=61229829-55a0-4d6f-a423-4b48a2b4d8e5), Fassung vom 2018-11-26; abgerufen am 2026-11-19). Aus der Substanzklasse ist bekannt, dass Penciclovir ein Guanosin-Nukleosid-Analogon ist. Nach der Phosphorylierung durch die virale Thymidinkinase hemmt es die virale DNA-Polymerase. Seine Wirkung ist damit auf Herpesviren (HSV-1, HSV-2, VZV) beschränkt.

Fasziolose wird durch die Leberegel Fasciola hepatica und F. gigantica verursacht, also durch parasitäre Trematoden und nicht durch Viren. Die Standardbehandlung ist Triclabendazol. Ein antiparasitärer Wirkmechanismus von Penciclovir ist nicht erkennbar, und es sind keine Zielstrukturen im Parasiten bekannt.

Der hohe Vorhersagewert ist daher wahrscheinlich ein Artefakt des Modells, etwa durch gemeinsame Nachbarn im Datennetzwerk, und kein Hinweis auf tatsächliche biologische Aktivität.

---

### Klinische Studien

Derzeit keine verwandten klinischen Studien registriert.

---

### Literaturbelege

Derzeit keine verwandte Literatur verfügbar.

---

### Marktinformationen Schweiz

<!-- licenses:begin -->

| Zulassungsnummer | Produktname | Kategorie (Heilmittelcode) | Anwendungsgebiet (Swissmedic) | Status |
|------|------|------|------|------|
| 53680 | Fenivir, Crème | Synthetika | Herpes labialis | Gültig |
| 62647 | Fenivir, Crème teintée | Synthetika | Herpes labialis | Gültig |

Quelle: Swissmedic – Zugelassene Packungen und Zugelassene Arzneimittel (Humanarzneimittel); Produktname, Kategorie und Anwendungsgebiet im Wortlaut der Swissmedic-Listen. „Erloschen“: Gültigkeitsdauer der Zulassung abgelaufen oder in den aktuellen Swissmedic-Listen nicht mehr aufgeführt.

<!-- licenses:end -->

---

### Sicherheitshinweise

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

---

### Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
- Die Vorhersage stützt sich nur auf den Modellwert. Es gibt weder Studien noch Literatur, und ein plausibler Wirkmechanismus gegen Leberegel ist nicht erkennbar.

**Um fortzufahren, wird Folgendes benötigt:**
- Präklinische Daten (z. B. In-vitro-Tests gegen Fasciola) als Nachweis einer antiparasitären Wirkung
- Angaben zum Wirkmechanismus von Penciclovir und möglichen Zielstrukturen im Parasiten
- Die Warnhinweise und Kontraindikationen aus der Swissmedic-Fachinformation für die Sicherheitsbewertung

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Denavir (penciclovir) prescribing information, Mylan Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=61229829-55a0-4d6f-a423-4b48a2b4d8e5) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

