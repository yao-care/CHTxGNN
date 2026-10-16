---
layout: default
title: Ceftolozane
parent: Nur Modellvorhersage (L5)
nav_order: 28
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ceftolozane: vorhergesagte neue Indikation Ureaplasma-Urethritis (Evidenzstufe L5). Ursprüngliche Indikation: Infektionskrankheiten"
monitor_inn: "ceftolozane"
predicted_indications: ["Ureaplasma urethritis", "gonococcal urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "urogenital tuberculosis", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease"]
---

# Ceftolozane
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **10** 
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

# Ceftolozan: Von Infektionskrankheiten zu Ureaplasma-Urethritis

---

## Zusammenfassung

Ceftolozan ist in der Schweiz als Zerbaxa für die Behandlung von Infektionskrankheiten zugelassen. Das Modell TxGNN sagt für die Ureaplasma-Urethritis einen sehr hohen Wert voraus. Diese Vorhersage beruht jedoch ausschliesslich auf Rechenmodellen: Es gibt weder klinische Studien noch Literatur dazu, und der Wirkmechanismus spricht gegen eine Wirksamkeit.

---

## Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Infektionskrankheiten |
| Vorhergesagte neue Indikation | Ureaplasma-Urethritis |
| TxGNN-Vorhersagewert | 99,89 % |
| Evidenzniveau | L5 |
| Marktstatus Schweiz | Im Handel |
| Anzahl Zulassungen | 1 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage plausibel?

Ceftolozan ist ein Cephalosporin aus der Gruppe der Beta-Laktam-Antibiotika. Es hemmt die Zellwandsynthese von Bakterien. Es ist vor allem auf Pseudomonas aeruginosa und Enterobacterales ausgerichtet und wird mit Tazobactam kombiniert. Für die Angaben zum ursprünglichen Wirkmechanismus liegen in den zusammengestellten Daten keine Informationen vor.

Die Beziehung zwischen der ursprünglichen und der neuen Indikation besteht nur auf Klassenebene: Beides sind bakterielle Infektionen. Der hohe Vorhersagewert ist deshalb sehr wahrscheinlich ein Artefakt des Wissensgraphen, der Antiinfektiva allgemein miteinander verknüpft.

Der Mechanismus spricht sogar gegen die Vorhersage. Ureaplasmen besitzen keine Zellwand, daher sind Beta-Laktame von Natur aus unwirksam. Die Plausibilität ist somit gering.

---

## Klinische Studien

Derzeit keine verwandten klinischen Studien registriert

---

## Literaturbelege

Derzeit keine verwandte Literatur verfügbar

---

## Marktinformationen Schweiz

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| 65472 | Zerbaxa 1.5 g, Pulver für ein Konzentrat zur Herstellung einer Infusionslösung | Synthetika | Infektionskrankheiten |

---

## Weitere vorhergesagte Indikationen

Die weiteren Vorhersagen der Rangliste sind ebenfalls rein rechnerisch (Evidenzniveau L5, Ausnahme: L4 bei der xanthogranulomatösen Pyelonephritis).

| Rang | Indikation | TxGNN-Wert | Einschätzung |
|------|------|------|------|
| 2 | Gonokokken-Urethritis | 99,89 % | Cephalosporine sind bei Gonorrhö etabliert, aber für Ceftolozan fehlen Daten, und Standardtherapien sind bereits verfügbar. |
| 3 | Entzündliche Gebärmuttererkrankung | 99,88 % | Infektionen sind oft polymikrobiell, die Abdeckung durch Ceftolozan/Tazobactam wäre unvollständig. |
| 4 | Xanthogranulomatöse Pyelonephritis | 99,88 % | Indirekte Plausibilität durch die Zulassung bei komplizierten Harnwegsinfektionen. Die Erkrankung wird meist chirurgisch behandelt. Die einzige Publikation ist eine allgemeine Übersichtsarbeit (PMID [26658652](https://pubmed.ncbi.nlm.nih.gov/26658652/), 2016) ohne krankheits- oder wirkstoffspezifische Daten. |
| 5 | Polyklonales Hyperviskositätssyndrom | 99,52 % | Kein plausibler Mechanismus, vermutlich Modellartefakt. |
| 6 | Hyperamylasämie | 99,52 % | Laborbefund statt Infektion, vermutlich Modellartefakt. |
| 7 | Urogenitale Tuberkulose | 99,50 % | Mycobacterium tuberculosis ist durch BlaC-Beta-Laktamase und seine Zellwand weitgehend resistent gegen Beta-Laktame. |
| 8 | Kongenitale Analbuminämie | 99,44 % | Genetische Erkrankung, keine Relevanz für ein Antibiotikum. |
| 9 | Blutgruppeninkompatibilität | 99,22 % | Immunologisch, ohne infektiöses Ziel. |
| 10 | Prämaligne hämatologische Erkrankung | 99,11 % | Keine mechanistische Grundlage. |

---

## Sicherheitshinweise

- **Arzneimittelwechselwirkungen** (11 Einträge, alle mit mässigem Schweregrad):
  - Aminoglykoside: Kanamycin, Neomycin, Streptomycin, Amikacin (einschliesslich liposomal), Gentamicin
  - Gerinnungshemmer: Warfarin, Dicoumarol
  - Weitere: Chloramphenicol, Ethinylestradiol, Mykophenolsäure

Warnhinweise und Kontraindikationen aus der Fachinformation lagen nicht vor. Bitte beachten Sie die Fachinformation für diese Sicherheitsinformationen.

---

## Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
- Die Vorhersage stützt sich nur auf ein Rechenmodell (L5). Für Ureaplasma-Urethritis spricht der Mechanismus sogar dagegen, weil Ureaplasmen keine Zellwand haben.
- Für die übrigen Kandidaten gibt es keine Studien. Bei den plausibleren Infektionen (Gonokokken-Urethritis, Pyelonephritis) bestehen bereits Standardtherapien oder chirurgische Verfahren.

**Um fortzufahren, wird Folgendes benötigt:**
- Fachinformation von Swissmedic mit Warnhinweisen und Kontraindikationen (blockierende Datenlücke, ohne sie ist keine Sicherheitsprüfung möglich)
- Angaben zum Wirkmechanismus aus DrugBank
- In-vitro-Empfindlichkeitsdaten (MHK) von Ceftolozan/Tazobactam gegen Neisseria gonorrhoeae und gegebenenfalls Erreger der Beckeninfektionen
- Klinische Studien oder krankheitsspezifische Literatur für die plausibleren Kandidaten
- Prüfung der Darreichungsform: Ceftolozan liegt nur als Infusionskonzentrat vor, die Eignung für die jeweilige Indikation ist offen
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

