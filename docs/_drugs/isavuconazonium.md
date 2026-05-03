---
layout: default
title: Isavuconazonium
parent: 僅模型預測 (L5)
nav_order: 15
evidence_level: L5
indication_count: 2
---

# Isavuconazonium
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

Der `txgnn-pipeline`-Skill ist geladen. Nun analysiere ich das Evidence Pack und erstelle den Bewertungsbericht.

---

# Isavuconazonium: Von Invasiver Aspergillose zu Pneumozystose

---

## Zusammenfassung

Isavuconazonium ist das Prodrug des Breitspektrum-Triazol-Antimykotikums Isavuconazol, das international für die Behandlung invasiver Aspergillose und Mukormykose eingesetzt wird – in der Schweiz ist das Präparat nicht registriert. Das TxGNN-Modell erzielt mit einem Vorhersagewert von 99,6 % einen auffallend hohen Score für eine mögliche Wirksamkeit bei Pneumozystose (Pneumocystis-Pneumonie, PCP). Die mechanistische Analyse offenbart jedoch grundlegende biologische Inkompatibilitäten zwischen dem Wirkstoff und dem Erreger; es liegen weder klinische Studien noch publizierte Literaturbelege zu dieser Indikation vor, weshalb die Evidenzstufe als L5 einzustufen und eine Weiterentwicklung derzeit nicht empfohlen wird.

---

## Kurzübersicht

| Punkt | Inhalt |
|-------|--------|
| Ursprüngliche Indikation | Invasive Aspergillose / Mukormykose (international zugelassen; in der Schweiz nicht registriert) |
| Vorhergesagte neue Indikation | Pneumozystose (pneumocystosis) |
| TxGNN-Vorhersagewert | 99,6 % |
| Evidenzniveau | L5 – Nur Modellvorhersage, keine tatsächlichen Studien |
| Marktstatus Schweiz | Nicht registriert |
| Anzahl Zulassungen | 0 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage plausibel?

Isavuconazol (aktiver Metabolit von Isavuconazonium) hemmt selektiv das pilzliche Enzym CYP51 (Lanosterol-14α-Demethylase), das einen zentralen Schritt in der Ergosterol-Biosynthese katalysiert. Ergosterol ist ein unverzichtbarer Bestandteil der pilzlichen Zellmembran; seine Depletion führt zu Membraninstabilität und Zelltod. Dieses Wirkprinzip verleiht Isavuconazol ein breites Spektrum gegen Aspergillus-Arten, Mucorales und zahlreiche Schimmelpilze.

Pneumocystis jirovecii, der Erreger der Pneumozystose, weist jedoch eine fundamentale biologische Besonderheit auf: Seine Zellmembran enthält kein Ergosterol, sondern ist cholesterolbasiert aufgebaut. Darüber hinaus unterscheidet sich das CYP51-Enzym von P. jirovecii strukturell erheblich von demjenigen anderer Pilze, weshalb klassische Triazole in vitro kaum Aktivität gegen diesen Erreger zeigen. Die etablierte Standardtherapie der Pneumozystose bleibt Trimethoprim-Sulfamethoxazol (TMP-SMX); es existieren weder Studien noch publizierte Fallberichte, die eine klinische Wirksamkeit von Isavuconazol bei dieser Erkrankung belegen.

Der sehr hohe TxGNN-Score (99,6 %) lässt sich am ehesten durch phänotypische Ähnlichkeit erklären: Sowohl Pneumozystose als auch die von Isavuconazol behandelten invasiven Mykosen treten überwiegend bei stark immungeschwächten Patienten auf (HIV/AIDS, Organ- oder Stammzelltransplantation, hämatologische Malignome). Das Modell erfasst diesen gemeinsamen klinischen Kontext opportunistischer Pilzinfektionen beim immunkompromittierten Wirt, unterscheidet jedoch nicht zwischen den grundlegend verschiedenen Erregerzellbiologien.

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
Die mechanistische Grundlage für eine Wirksamkeit von Isavuconazonium bei Pneumozystose ist biologisch nicht plausibel – P. jirovecii besitzt kein Ergosterol und ist gegenüber CYP51-Hemmern intrinsisch unempfindlich. Es liegen keine klinischen Studien und keine Literaturbelege vor; der hohe TxGNN-Score spiegelt wahrscheinlich phänotypische Ähnlichkeit im Sinne eines gemeinsamen immungeschwächten Wirtsumfelds wider, nicht aber eine echte mechanistische Verwandtschaft.

**Hinweis zu Rang 2 – Mykzetom (mycetoma):**
Die zweithöchst bewertete Indikation Mykzetom (TxGNN: 99,3 %, Evidenzniveau: L4) besitzt eine erheblich plausiblere mechanistische Basis, da Isavuconazol gegen die kausalen Schimmelpilze wie *Madurella mycetomatis* oder *Scedosporium boydii* (eumycetoma) breite in-vitro-Aktivität zeigen kann. Verwandte Triazole (Itraconazol, Voriconazol) liegen zudem bereits in kleinen klinischen Berichten für Eumykzetom vor. Eine gesonderte Evaluation dieser Indikation wird empfohlen.

**Um fortzufahren, wird Folgendes benötigt:**
- Internationale Fachinformation (SmPC, z. B. EMA-Zulassung von Cresemba®) für vollständige Sicherheitsdaten: Warnhinweise, Kontraindikationen und Arzneimittelwechselwirkungen
- Abklärung des Wirkmechanismus (MOA) über die DrugBank-API (DB06636)
- Systematische Literaturrecherche zur in-vitro-Aktivität von Triazolen gegen P. jirovecii zur endgültigen mechanistischen Ausschlussbestätigung
- Separate Bewertung der Indikation Mykzetom (Rang 2) auf Basis der vorhandenen Literaturbelege und der stärkeren mechanistischen Rationale
## Haftungsausschluss

Diese Vorhersagen dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

