---
layout: default
title: Sorbitol
parent: Nur Modellvorhersage (L5)
nav_order: 86
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Sorbitol: vorhergesagte neue Indikation Belastungsinduzierte maligne Hyperthermie (Evidenzstufe L5). Ursprüngliche Indikation: Obstipation"
---

# Sorbitol
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **1** 
{: .fs-6 .fw-300 }

---

## Inhaltsverzeichnis
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmazeutischer Bewertungsbericht

</div>

# Sorbitol: Von Obstipation zu belastungsinduzierter maligner Hyperthermie

---

## Zusammenfassung

Sorbitol wird in der Schweiz als Abführmittel bei Verstopfung (Obstipation) eingesetzt. Das Vorhersagemodell TxGNN schlägt eine mögliche Wirksamkeit bei belastungsinduzierter maligner Hyperthermie vor, einer akuten, lebensbedrohlichen Störung der Skelettmuskulatur. Diese Vorhersage beruht ausschliesslich auf einem Modellwert; es liegen weder klinische Studien noch Literatur vor, und ein plausibler pharmakologischer Zusammenhang lässt sich aus den vorliegenden Daten nicht herleiten.

---

## Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Obstipation; Laxans |
| Vorhergesagte neue Indikation | Belastungsinduzierte maligne Hyperthermie |
| TxGNN-Vorhersagewert | 99,4 % |
| Evidenzniveau | L5 (nur Modellvorhersage, keine tatsächlichen Studien) |
| Marktstatus Schweiz | Im Handel |
| Anzahl Zulassungen | 2 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage plausibel?

Sorbitol ist ein Zuckeralkohol und wirkt als osmotisches Abführmittel: Es zieht Wasser in den Darm, macht den Stuhl weicher und fördert die Darmentleerung. Der ursprüngliche Wirkmechanismus liegt in den vorliegenden Daten nicht vor, die obige Beschreibung entspricht dem allgemeinen pharmakologischen Wissen.

Die maligne Hyperthermie ist dagegen eine Störung der Kalziumregulation in der Skelettmuskulatur, meist im Zusammenhang mit Varianten im RYR1-Gen. Zwischen der abführenden Wirkung von Sorbitol und diesem Krankheitsmechanismus lässt sich aus den vorhandenen Daten keine nachvollziehbare Verbindung herstellen.

Der hohe Vorhersagewert könnte auf Artefakte in der Struktur des Wissensgraphen zurückgehen, etwa auf gemeinsame Verknüpfungen von Zuckeralkoholen oder Hilfsstoffen (zum Beispiel Mannitol in verwandten Anwendungen), und nicht auf eine echte pharmakologische Beziehung. Hinzu kommt, dass für diese Erkrankung mit Dantrolen bereits eine etablierte Standardtherapie existiert. Eine Umwidmung bräuchte deshalb sehr starke Belege.

---

## Marktinformationen Schweiz

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| 54285 | Pursana Feigensirup mit Sorbitol, Sirup | Synthetika | Obstipation |
| 29869 | Microlax, Klysma | Synthetika | Laxans |

---

## Sicherheitshinweise

- **Kontraindikationen aus dem Wissensgraphen** (keine Angabe aus einer Fachinformation): aktives peptisches Ulkusleiden
- **Arzneimittelwechselwirkungen** (2 Einträge):
  - Tolevamer: **schwerwiegend (Major)**
  - Lamivudin: mässig (Moderate)

Die Warnhinweise und Kontraindikationen der Swissmedic-Fachinformation liegen nicht vor. Bitte beachten Sie die Fachinformation für vollständige Sicherheitsinformationen.

---

## Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
- Die Vorhersage stützt sich allein auf einen Modellwert (99,4 %) ohne klinische Studien oder Literatur. Ein pharmakologischer Zusammenhang ist nicht erkennbar, und für die Erkrankung gibt es eine etablierte Standardtherapie.

**Um fortzufahren, wird Folgendes benötigt:**
- Ergänzung des Wirkmechanismus von Sorbitol (z. B. über DrugBank)
- Prüfung, ob ein biologisch plausibler Zusammenhang mit der Kalziumregulation im Skelettmuskel besteht, und Analyse, ob die Vorhersage ein Artefakt des Wissensgraphen ist
- Auswertung der Fachinformation von Swissmedic (Warnhinweise und Kontraindikationen), da dies für die Sicherheitsprüfung blockierend ist
- Systematische Literatur- und Studienrecherche zu Sorbitol und maligner Hyperthermie
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

