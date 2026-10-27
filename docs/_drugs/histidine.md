---
layout: default
title: Histidine
parent: Nur Modellvorhersage (L5)
nav_order: 56
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Histidine: vorhergesagte neue Indikation Gastroparese (Evidenzstufe L5). Ursprüngliche Indikation: Parenterale Ernährung"
monitor_inn: "histidine"
predicted_indications: ["gastroparesis (disease)", "sclerosing cholangitis"]
---

# Histidine
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **2** 
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

## Histidin: Von parenteraler Ernährung zu Gastroparese
{: .text-alpha }

---

### Zusammenfassung

Histidin ist eine Aminosäure, die in der Schweiz als Bestandteil von Infusionslösungen zur parenteralen Ernährung sowie in einer Peritonealdialyselösung zugelassen ist. Das Modell TxGNN sagt eine mögliche Wirksamkeit bei Gastroparese voraus, mit einem sehr hohen Vorhersagewert. Diese Vorhersage beruht jedoch ausschliesslich auf einer Modellrechnung: Es gibt keine klinischen Studien, und die einzige gefundene Publikation untersucht Histidin nicht.

---

### Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Parenterale Ernährung; Peritonealdialyselösung |
| Vorhergesagte neue Indikation | Gastroparese |
| TxGNN-Vorhersagewert | 99,6 % |
| Evidenzniveau | L5 (nur Modellvorhersage) |
| Marktstatus Schweiz | Im Handel |
| Anzahl Zulassungen | 8 |
| Empfohlene Entscheidung | Abwarten |

---

### Warum ist diese Vorhersage plausibel?

Der ursprüngliche Wirkmechanismus von Histidin ist in den vorliegenden Daten nicht angegeben, was die mechanistische Bewertung einschränkt. Histidin ist eine essenzielle Aminosäure und dient als Ausgangsstoff für Histamin. Histamin kann die Magensäuresekretion und möglicherweise die Magenmotilität beeinflussen.

Dieser Zusammenhang ist jedoch spekulativ. Die einzige gefundene Publikation (PMID 42668409) beschreibt Amyloid-Ablagerungen und den Verlust der Nervenversorgung der Magenschleimhaut bei hereditärer ATTR-Amyloidose. Sie testet kein Histidin und stützt keinen histidinspezifischen Mechanismus bei Gastroparese. Der hohe Vorhersagewert sollte daher nicht als klinischer Hinweis auf Wirksamkeit verstanden werden.

---

### Klinische Studien

Derzeit keine verwandten klinischen Studien registriert.

---

### Literaturbelege

| PMID | Jahr | Typ | Zeitschrift | Wichtige Ergebnisse |
|------|-----|------|------|---------|
| [42668409](https://pubmed.ncbi.nlm.nih.gov/42668409/) | 2026 | Kohorte/präklinisch (Patienten und Mausmodell) | Amyloid | Untersucht Amyloid-Ablagerungen im Magen und den Verlust der Nervenversorgung der Schleimhaut bei hereditärer ATTR-Amyloidose mit Polyneuropathie. Histidin wurde nicht getestet. |

---

### Marktinformationen Schweiz

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| 55337 | Aminoven 5 %, Infusionslösung | Synthetika | Parenterale Ernährung |
| 54850 | Aminoven infant 10%, Infusionslösung | Synthetika | Parenterale Ernährung |
| 52459 | Nutrineal PD 4 mit 1.1% Aminosäuren, Peritonealdialyselösung | Synthetika | Peritonealdialyselösung |
| 65450 | Aminoplasmal B. Braun 10%, Infusionslösung | Synthetika | Parenterale Ernährung |
| 65726 | Omegaflex special ohne Elektrolyte, Emulsion zur Infusion 625 ml | Synthetika | Parenterale Ernährung |
| 66859 | SmofKabiven special EF 1012 ml, Infusionsemulsion | Synthetika | Parenterale Ernährung |
| 59377 | OLIMEL 4,4 % ohne Elektrolyte, Infusionslösung | Synthetika | Parenterale Ernährung |
| 62283 | SmofKabiven EF, Infusionsemulsion 986 ml | Synthetika | Parenterale Ernährung für Erwachsene |

---

### Sicherheitshinweise

Die Fachinformation lieferte keine auswertbaren Warnungen oder Kontraindikationen. Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

Ergänzend nennt der Wissensgraph (keine Angaben aus der Fachinformation) mögliche Krankheitsbilder, bei denen Vorsicht geboten sein könnte:
- **Nieren:** Nierenerkrankung, chronische Niereninsuffizienz, terminales Nierenversagen, Nephrolithiasis, Nephrokalzinose, akute Uratnephropathie
- **Herz-Kreislauf:** Herzerkrankung, Herz-Kreislauf-Erkrankung, Kammerflimmern, Digitalisvergiftung
- **Stoffwechsel:** Phenylketonurie und andere Störungen des Phenylalaninstoffwechsels, Störungen des Phosphorstoffwechsels, Hyperkalzämie (einschliesslich humoraler Hyperkalzämie bei Malignomen), Sarkoidose
- **Sonstige:** Pyoureter

Zu Arzneimittelwechselwirkungen liegen keine Daten vor.

---

### Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
- Die Vorhersage für Gastroparese beruht allein auf einem Rechenmodell (L5). Es gibt keine klinischen Studien, und die einzige Publikation untersucht Histidin nicht.
- Der Wirkmechanismus ist nicht dokumentiert, und die Fachinformation lieferte keine Sicherheitsdaten. Die Sicherheitsprüfung kann daher nicht fortgesetzt werden.

**Um fortzufahren, wird Folgendes benötigt:**
- Die Fachinformation von Swissmedic (Warnungen, Kontraindikationen) herunterladen und auswerten.
- Den Wirkmechanismus aus DrugBank ergänzen.
- Präklinische oder klinische Daten zu Histidin bei Gastroparese, einschliesslich der Rolle von Histamin in der Magenmotilität.
- Prüfung der Darreichungsform und des Applikationswegs (bisher nur Infusionen).
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

