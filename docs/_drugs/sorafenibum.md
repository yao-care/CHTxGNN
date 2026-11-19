---
layout: default
title: Sorafenibum
parent: Nur Modellvorhersage (L5)
nav_order: 550
evidence_level: L5
indication_count: 6
drugbank_id: DB00398
monitor_inn: "Sorafenib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "female breast carcinoma", "renal pelvis carcinoma", "vulva sarcoma", "dermatofibrosarcoma protuberans"]
last_modified_at: 2026-11-20
description: "Sorafenibum: vorhergesagte neue Indikation Liposarkom (liposarcoma) (Evidenzstufe L5). Ursprüngliche Indikation: Leberzellkarzinom, Nierenzellkarzinom, Schilddrüsenkarzinom"
---

# Sorafenibum
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **6** 
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

## Sorafenibum: Liposarkom (liposarcoma)
{: .text-alpha }

### Zusammenfassung

Sorafenib ist ein Multikinase-Inhibitor, der in der Schweiz im Handel ist. Für das Liposarkom (liposarcoma) sagt das Modell eine mögliche Wirksamkeit voraus. Die Evidenz ist dünn: Es gibt keine Studie, die ausschliesslich Liposarkome untersucht, sondern nur Studien zu fortgeschrittenen Weichteilsarkomen insgesamt.

---

### Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Leberzellkarzinom, Nierenzellkarzinom, Schilddrüsenkarzinom |
| Vorhergesagte neue Indikation | Liposarkom (liposarcoma) |
| TxGNN-Vorhersagewert | 0.9982 |
| Evidenzniveau | L5 |
| Marktstatus Schweiz | Im Handel (gültige Zulassungen: 2 von 2) |
| Anzahl Zulassungen | 2 (gültig: 2) |
| Empfohlene Entscheidung | Abwarten |

---

### Warum ist diese Vorhersage plausibel?

Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Sorafenibum (inoffizielle Übersetzung): „Sorafenib ist ein Kinase-Inhibitor, der die Proliferation von Tumorzellen in vitro verringert. Es wurde gezeigt, dass Sorafenib mehrere intrazelluläre Kinasen (c-CRAF, BRAF und mutiertes BRAF) und Zelloberflächenkinasen (KIT, FLT- 3, RET, RET/PTC, VEGFR-1, VEGFR- 2, VEGFR- 3 und PDGFR-ß) hemmt.“ Englischer Originalwortlaut: "Sorafenib is a kinase inhibitor that decreases tumor cell proliferation in vitro. Sorafenib was shown to inhibit multiple intracellular (c-CRAF, BRAF and mutant BRAF) and cell surface kinases (KIT, FLT- 3, RET, RET/PTC, VEGFR-1, VEGFR- 2, VEGFR- 3, and PDGFR-ß)." ([DailyMed: Nexavar (sorafenib) prescribing information, Bayer HealthCare Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b50667e4-5ebc-4968-a646-d605058dbef0), Fassung vom 2023-08-28; abgerufen am 2026-11-19). Aus der Literatur ist bekannt, dass Sorafenib den RAF/MEK/ERK-Signalweg sowie die Rezeptoren VEGFR-2/3 und PDGFR-β hemmt. Das ergibt eine nachvollziehbare Begründung für eine gefässhemmende und wachstumshemmende Wirkung bei Weichteilsarkomen.

Der Zusammenhang zum Liposarkom ist jedoch nur indirekt. Liposarkome werden vor allem durch eine MDM2/CDK4-Amplifikation (gut und entdifferenzierte Formen) oder durch FUS-DDIT3 (myxoider Typ) getrieben, nicht durch die Zielstrukturen von Sorafenib. Der sehr hohe Vorhersagewert dürfte vor allem von der Nähe zur breiteren Sarkomgruppe stammen. Eine Studie an entdifferenzierten Liposarkom-Xenograft-Modellen (PTEN-Herunterregulierung) stützt Sorafenib nicht direkt.

---

### Klinische Studien

| Studiennummer | Phase | Status | Teilnehmer | Wichtige Ergebnisse |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | Abgeschlossen | 51 | Einarmige Studie zu Sorafenib bei fortgeschrittenen Weichteilsarkomen. Gemischte Histologien, nicht liposarkomspezifisch; keine Ergebnisse in den Daten angegeben. |

---

### Literaturbelege

| PMID | Jahr | Typ | Zeitschrift | Wichtige Ergebnisse |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | Phase-2-Studie (SWOG S0505) | Cancer | Sorafenib bei fortgeschrittenen Weichteilsarkomen; Sorafenib hemmt u. a. RAF, VEGFR1–3, PDGFR-B, FLT3 und c-Kit. Ergebnisse im verfügbaren Abstract nicht enthalten. |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase-1-Studie | Annals of Surgical Oncology | Neoadjuvante Strahlentherapie plus Sorafenib bei lokal fortgeschrittenem Extremitäten-Weichteilsarkom. |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Übersichtsarbeit | Annals of Oncology | Weichteilsarkome werden zunehmend nach Histologie behandelt; Trabectedin zeigt Wirkung bei Liposarkomen. Sorafenib ist nicht der Schwerpunkt. |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Übersichtsarbeit | Magyar Onkologia | Histologiebasierte medikamentöse Behandlung von Weichteilsarkomen. |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | Präklinisch | Molecular Cancer Therapeutics | Sorafenib hemmt Wachstum und MAPK-Signalweg in Zelllinien maligner peripherer Nervenscheidentumoren; untersucht wurden auch entdifferenzierte Liposarkom-Zelllinien. |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | Präklinisch | American Journal of Pathology | Neue Xenograft-Modelle des entdifferenzierten Liposarkoms; Ansprechen auf Hemmung des PI3K-Signalwegs, nicht auf Sorafenib. |

---

### Marktinformationen Schweiz

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| 68210 | Sorafenib Zentiva 200 mg, Filmtabletten | Synthetika | Leberzellkarzinom, Nierenzellkarzinom, Schilddrüsenkarzinom |
| 57583 | Nexavar, Filmtabletten | Synthetika | Leberzellkarzinom, Nierenzellkarzinom, Schilddrüsenkarzinom |

---

### Zytotoxizität

| Punkt | Inhalt |
|------|------|
| Zytotoxizitätsklassifikation | Zielgerichtete Therapie (Multikinase-Inhibitor) |

Weitere Angaben (Myelosuppressionsrisiko, Emetogenität, Überwachung, Handhabungsschutz) sind in den zusammengestellten Daten nicht enthalten; bitte die Fachinformation beachten.

---

### Sicherheitshinweise

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

---

### Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
- Keine zusammengestellte Studie untersucht das Liposarkom selbst; die vorhandene Evidenz betrifft gemischte Weichteilsarkome. Der Zusammenhang zu den Zielstrukturen von Sorafenib ist indirekt, und die Sicherheitsdaten fehlen.

**Um fortzufahren, wird Folgendes benötigt:**
- Auswertung der Ergebnisse der Phase-2-Studien (NCT00217620, SWOG S0505), insbesondere der Liposarkom-Untergruppe
- Fachinformation von Swissmedic mit Warnhinweisen und Kontraindikationen
- Angaben zum Wirkmechanismus aus einer Arzneimitteldatenbank
- Klärung, ob Sorafenib einen Vorteil gegenüber den etablierten, histologiebasierten Therapien des Liposarkoms bietet

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Nexavar (sorafenib) prescribing information, Bayer HealthCare Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b50667e4-5ebc-4968-a646-d605058dbef0) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

