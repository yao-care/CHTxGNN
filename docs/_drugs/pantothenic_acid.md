---
layout: default
title: Pantothenic Acid
parent: Nur Modellvorhersage (L5)
nav_order: 70
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Pantothenic Acid: vorhergesagte neue Indikation Angeborener Prothrombinmangel (congenital prothrombin deficiency) (Evidenzstufe L5). Ursprüngliche Indikation: Vitaminzusatz zur parenteralen Ernährung"
---

# Pantothenic Acid
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **9** 
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

# Pantothensäure: Von Vitaminzusatz zur parenteralen Ernährung zu angeborenem Prothrombinmangel

## Zusammenfassung

Pantothensäure (Vitamin B5) wird in der Schweiz als Vitaminzusatz zur parenteralen Ernährung eingesetzt. Das Modell TxGNN sagt für den angeborenen Prothrombinmangel einen sehr hohen Wert voraus, doch dafür gibt es weder klinische Studien noch Literatur und auch keinen erkennbaren biologischen Mechanismus. Die Vorhersage beruht allein auf dem Modell (Evidenzniveau L5); eine Weiterverfolgung ist derzeit nicht begründet.

---

## Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Vitaminzusatz zur parenteralen Ernährung |
| Vorhergesagte neue Indikation | Angeborener Prothrombinmangel (congenital prothrombin deficiency) |
| TxGNN-Vorhersagewert | 99,96 % |
| Evidenzniveau | L5 (nur Modellvorhersage) |
| Marktstatus Schweiz | Im Handel |
| Anzahl Zulassungen | 2 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage plausibel?

Pantothensäure ist ein Vorläufer von Coenzym A und spielt eine zentrale Rolle im Energie- und Fettstoffwechsel. Zum Wirkmechanismus liegen in den zusammengestellten Daten keine weiteren Angaben vor.

Der angeborene Prothrombinmangel ist eine genetisch bedingte Gerinnungsstörung (Gen F2). Für Pantothensäure ist keine Rolle bei der Bildung oder Funktion von Prothrombin bekannt. Ein mechanistischer Zusammenhang zwischen der ursprünglichen und der vorhergesagten Indikation ist daher nicht erkennbar.

Der hohe Vorhersagewert ist deshalb als reines Modellergebnis zu verstehen, vermutlich aus Netzwerkähnlichkeiten im Wissensgraphen. Er ersetzt keine biologische oder klinische Evidenz.

### Weitere vorhergesagte Indikationen (zur Einordnung)

Für andere Vorhersagen liegt etwas mehr Material vor, aber keine davon ist klinisch belegt:

| Vorhergesagte Indikation | TxGNN-Wert | Evidenzniveau | Einschätzung |
|------|------|------|------|
| Folsäuremangelanämie | 99,60 % | L4 | Plausible Wechselwirkung von B-Vitamin-Mängeln. Die Hinweise sind alt, indirekt und stammen aus Tierstudien und Übersichtsarbeiten. Folsäure bleibt die Standardtherapie. |
| Entzündliche Erkrankung der Gebärmutter | 99,14 % | L4 | Eine Mausstudie von 2026 zeigt einen Schutz vor Endometriumschäden nach Vagotomie. Es gibt keine Humandaten. |
| Glycerinstoffwechselstörung | 99,77 % | L5 | Die gefundenen Arbeiten sind Metabolomstudien, in denen Pantothenat nur als gemessener Stoff vorkommt. |
| Ochronose, xanthogranulomatöse Pyelonephritis, Harnwegsinfekt, gonokokkenbedingte Urethritis, Ureaplasma-Urethritis | 99,10 % – 99,78 % | L5 | Kein plausibler Mechanismus, keine belastbare Evidenz. |

---

## Klinische Studien

Derzeit keine verwandten klinischen Studien registriert.

---

## Literaturbelege

Derzeit keine verwandte Literatur verfügbar (für angeborenen Prothrombinmangel).

---

## Marktinformationen Schweiz

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| 43678 | Soluvit N, Trockenampullen (Fresenius Kabi (Schweiz) AG) | Synthetika | Vitaminzusatz zur parenteralen Ernährung |
| 69577 | Viant, Pulver zur Herstellung einer Infusionslösung (B. Braun Medical AG) | Synthetika | Vitaminzusatz zur parenteralen Ernährung |

---

## Sicherheitshinweise

- **Hinweise aus dem Wissensgraphen (keine Angaben aus der Fachinformation):** In der Wissensbasis sind Kontraindikations-Verbindungen zu folgenden Erkrankungen verzeichnet: Nierenerkrankung, Pyoureter, Sichelzellanämie, hereditäre Persistenz von fetalem Hämoglobin, primäre Hyperoxalurie, hereditäre Hämochromatose, Hämosiderose, Eisenstoffwechselstörung und Morbus Wilson. Diese Verbindungen sind nicht durch Fachinformationstexte belegt und müssen vor einer Bewertung geprüft werden.
- **Arzneimittelwechselwirkungen:** Es wurden keine Wechselwirkungen gefunden.

Bitte beachten Sie die Fachinformation für Warnhinweise und Kontraindikationen.

---

## Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
- Für die am höchsten bewertete Vorhersage (angeborener Prothrombinmangel) gibt es weder Studien noch Literatur noch einen erkennbaren Mechanismus. Der hohe Modellwert allein genügt nicht.
- Die Evidenz für die übrigen Vorhersagen ist ebenfalls schwach (höchstens L4, präklinisch oder indirekt).

**Um fortzufahren, wird Folgendes benötigt:**
- Die Fachinformation von Swissmedic mit Warnhinweisen und Kontraindikationen, da ohne sie die Sicherheitsprüfung nicht möglich ist.
- Angaben zum Wirkmechanismus aus DrugBank, um mögliche Zusammenhänge zu den vorhergesagten Indikationen zu prüfen.
- Eine gezielte Literaturrecherche zu Pantothensäure und Gerinnungsstörungen. Alternativ können Indikationen mit besserer Evidenzlage (z. B. Folsäuremangelanämie, entzündliche Gebärmuttererkrankung) vorrangig weiterverfolgt werden, zunächst mit Humandaten.
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

