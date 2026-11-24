---
layout: default
title: Ketoprofenum
parent: Nur Modellvorhersage (L5)
nav_order: 330
evidence_level: L5
indication_count: 9
drugbank_id: DB01009
monitor_inn: "Ketoprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "WHIM syndrome", "juvenile arthritis due to defect in LACC1"]
last_modified_at: 2026-11-24
description: "Ketoprofenum: vorhergesagte neue Indikation Akromesomele Dysplasie Typ Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) (Evidenzstufe L5)."
---

# Ketoprofenum
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **9** 
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

## Ketoprofenum: Akromesomele Dysplasie Typ Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type)
{: .text-alpha }

---

### Zusammenfassung

Ketoprofen ist ein entzündungshemmendes und schmerzlinderndes Arzneimittel aus der Gruppe der nichtsteroidalen Antirheumatika. Das Vorhersagemodell TxGNN schlägt als neue Indikation die akromesomele Dysplasie Typ Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) vor, eine seltene genetische Skeletterkrankung. Dafür liegen weder klinische Studien noch Literatur vor; die Vorhersage beruht allein auf dem Modell (Evidenzniveau L5).

---

### Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Antiphlogistikum, Antirheumatikum |
| Vorhergesagte neue Indikation | Akromesomele Dysplasie Typ Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) |
| TxGNN-Vorhersagewert | 0.9998 |
| Evidenzniveau | L5 |
| Marktstatus Schweiz | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Abwarten |

---

### Warum ist diese Vorhersage plausibel?

Laut dem Abschnitt „Clinical Pharmacology“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Ketoprofenum (inoffizielle Übersetzung): „In entzündungshemmenden Modellen wurde gezeigt, dass Ketoprofen hemmende Wirkungen auf die Prostaglandin- und Leukotriensynthese, eine Antibradykinin-Aktivität sowie eine lysosomale membranstabilisierende Wirkung besitzt. Sein Wirkmechanismus ist jedoch, wie der anderer nichtsteroidaler Antirheumatika, nicht vollständig geklärt.“ Englischer Originalwortlaut: "In anti-inflammatory models ketoprofen has been shown to have inhibitory effects on prostaglandin and leukotriene synthesis, to have antibradykinin activity, as well as to have lysosomal membrane-stabilizing action. However, its mode of action, like that of other non-steroidal anti-inflammatory drugs, is not fully understood." ([DailyMed: Orudis (ketoprofen) prescribing information, Allegis Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=47d0b808-7142-c7a9-e063-6394a90a6e0d), Fassung vom 2026-01-07; abgerufen am 2026-11-19). Bekannt ist, dass Ketoprofen die Cyclooxygenasen COX-1 und COX-2 hemmt und dadurch Schmerzen und Entzündungen lindert.

Die akromesomele Dysplasie Typ Hunter-Thompson ist eine genetische Skeletterkrankung. Sie hängt mit Funktionsverlust-Mutationen im Gen CDMP1/GDF5 zusammen, das die Knorpelbildung steuert. Die COX-Hemmung greift in diesen Signalweg nicht ein.

Ein belegter mechanistischer Zusammenhang besteht daher nicht. Der sehr hohe Vorhersagewert ist ein reines Modellergebnis und wird durch keine Studie gestützt. Die Vorhersage sollte deshalb als Hypothese verstanden werden, nicht als Hinweis auf eine Wirksamkeit.

---

### Marktinformationen Schweiz

<!-- licenses:begin -->

| Zulassungsnummer | Produktname | Kategorie (Heilmittelcode) | Anwendungsgebiet (Swissmedic) | Status |
|------|------|------|------|------|
| 50227 | Fastum, Gel | Synthetika | Antiphlogistikum, Antirheumatikum | Gültig |

Quelle: Swissmedic – Zugelassene Packungen und Zugelassene Arzneimittel (Humanarzneimittel); Produktname, Kategorie und Anwendungsgebiet im Wortlaut der Swissmedic-Listen. „Erloschen“: Gültigkeitsdauer der Zulassung abgelaufen oder in den aktuellen Swissmedic-Listen nicht mehr aufgeführt.

<!-- licenses:end -->

---

### Sicherheitshinweise

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

---

### Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
- Die Vorhersage stützt sich ausschliesslich auf das Modell, es gibt keine klinischen Studien, keine Literatur und keinen plausiblen Wirkmechanismus für diese Erkrankung.

**Um fortzufahren, wird Folgendes benötigt:**
- Ein belegter biologischer Zusammenhang zwischen COX-Hemmung und dem GDF5-Signalweg, etwa durch präklinische Studien
- Die Warnhinweise und Kontraindikationen aus der Swissmedic-Fachinformation
- Der Wirkmechanismus aus DrugBank
- Die Prüfung, ob die topische Darreichungsform (Gel) für die Zielerkrankung überhaupt geeignet ist

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Orudis (ketoprofen) prescribing information, Allegis Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=47d0b808-7142-c7a9-e063-6394a90a6e0d) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

