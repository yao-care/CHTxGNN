---
layout: default
title: Enfortumab Vedotin
parent: Nur Modellvorhersage (L5)
nav_order: 47
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Enfortumab Vedotin: vorhergesagte neue Indikation Lepra (Evidenzstufe L5). Ursprüngliche Indikation: Urothelkarzinom"
monitor_inn: "enfortumab vedotin"
predicted_indications: ["leprosy", "multiple endocrine neoplasia", "cytomegalovirus infection", "candidiasis", "cerebral infarction", "HIV infectious disease", "homozygous familial hypercholesterolemia", "malignant catarrh", "infectious bovine rhinotracheitis"]
---

# Enfortumab Vedotin
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

# Enfortumab Vedotin: Von Urothelkarzinom zu Lepra

---

### Zusammenfassung

Enfortumab Vedotin (Padcev) ist ein Antikörper-Wirkstoff-Konjugat, das in der Schweiz zur Behandlung des Urothelkarzinoms zugelassen ist. Das Vorhersagemodell TxGNN schlägt Lepra als neue Indikation vor, mit einem sehr hohen Vorhersagewert. Diese Vorhersage beruht jedoch ausschliesslich auf einer Modellberechnung: Es liegen weder klinische Studien noch Literatur vor, und ein plausibler Wirkmechanismus ist nicht erkennbar.

---

### Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Urothelkarzinom |
| Vorhergesagte neue Indikation | Lepra |
| TxGNN-Vorhersagewert | 99,5 % |
| Evidenzniveau | L5 (nur Modellvorhersage, keine tatsächlichen Studien) |
| Marktstatus Schweiz | Im Handel |
| Anzahl Zulassungen | 1 |
| Empfohlene Entscheidung | Abwarten |

---

### Warum ist diese Vorhersage plausibel?

Enfortumab Vedotin ist ein gegen Nectin-4 gerichtetes Antikörper-Wirkstoff-Konjugat. Der Antikörper bringt den zytotoxischen Wirkstoff MMAE gezielt in Tumorzellen, die Nectin-4 tragen. Die ursprüngliche Wirkmechanismus-Angabe fehlt in den für diesen Bericht zusammengestellten Daten; die Beschreibung stützt sich daher auf die Einordnung der Wirkstoffklasse.

Für Lepra, eine bakterielle Infektion, ist kein mechanistischer Zusammenhang bekannt. Es gibt keine Hinweise, dass ein zytotoxisches Antikörper-Wirkstoff-Konjugat gegen Mykobakterien wirkt. Der hohe TxGNN-Wert (99,5 %) ist eine rein rechnerische Vorhersage aus Netzwerkbeziehungen und kein Beleg für eine Wirksamkeit. Das zytotoxische und das potenziell immunsupprimierende Profil des Arzneimittels sprechen bei einer Infektionskrankheit eher dagegen.

Die weiteren vorhergesagten Indikationen (u. a. multiple endokrine Neoplasie, Zytomegalie-Infektion, Candidiasis, Hirninfarkt, HIV, homozygote familiäre Hypercholesterinämie) weisen ebenfalls keinen plausiblen Zusammenhang auf. Zwei Einträge (maligner Katarrh, infektiöse bovine Rhinotracheitis) sind Tierkrankheiten und vermutlich Artefakte der Datenbasis. Die beiden vorhandenen Publikationen zu Zytomegalie-Infektion bzw. Candidiasis beschreiben Nebenwirkungen und Sicherheitssignale, keinen Nutzen.

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
| 68291 | Padcev 20 mg, Pulver für ein Konzentrat zur Herstellung einer Infusionslösung | Biotechnologika | Urothelkarzinom |

---

### Zytotoxizität

| Punkt | Inhalt |
|------|------|
| Zytotoxizitätsklassifikation | Zielgerichtete Therapie (Antikörper-Wirkstoff-Konjugat mit MMAE) |
| Überwachungspunkte | Blutbild, Leber- und Nierenfunktion |
| Handhabungsschutz | Als zytotoxisches Arzneimittel sind Schutzmassnahmen bei Zubereitung und Handhabung zu beachten; Details siehe Fachinformation |

Zum Myelosuppressionsrisiko und zur Emetogenität liegen in den zusammengestellten Daten keine Angaben vor.

---

### Sicherheitshinweise

- **Arzneimittelwechselwirkungen**: Insgesamt wurden 147 Wechselwirkungen erfasst. Die Mehrzahl ist als moderat eingestuft, darunter Antidiabetika (z. B. Metformin, Pioglitazon, Glimepiride, Glipizid, Glibenclamid, Acarbose, Dapagliflozin, Empagliflozin, Linagliptin, Exenatid, Dulaglutid) sowie Aprepitant. Als **schwerwiegend** eingestuft ist die Wechselwirkung mit **Clarithromycin**.

Für Warnhinweise und Kontraindikationen liegen keine verwertbaren Daten vor. Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

---

### Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
- Die Vorhersage für Lepra beruht allein auf einem Modellwert. Es gibt weder Studien noch Literatur noch einen erkennbaren Wirkmechanismus, und das zytotoxische Profil spricht gegen den Einsatz bei einer bakteriellen Infektion.

**Um fortzufahren, wird Folgendes benötigt:**
- Fachinformation von Swissmedic (Warnhinweise, Kontraindikationen) beschaffen und auswerten
- Wirkmechanismus aus DrugBank ergänzen
- Präklinische oder mechanistische Hinweise, die einen Zusammenhang zwischen Nectin-4-gerichteter MMAE-Abgabe und Lepra belegen
- Prüfung, ob andere vorhergesagte Indikationen biologisch sinnvoller sind (aktuell keine mit Evidenz über Niveau L4 hinaus)
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

