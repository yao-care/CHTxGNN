---
layout: default
title: Datenquellen
nav_order: 93
permalink: /sources/
description: "Die Datenquellen hinter CHTxGNN: Zulassungsdaten von Swissmedic, TxGNN, ClinicalTrials.gov, PubMed und DrugBank."
---

# Datenquellen

<div class="key-takeaway">
Jede Schlussfolgerung lässt sich auf eine öffentliche Datenquelle zurückführen — nichts ist eine Blackbox.
</div>

---

## Übersicht der Quellen

<table class="comparison-table">
<thead>
<tr><th>Art</th><th>Quelle</th><th>Verwendet für</th></tr>
</thead>
<tbody>
<tr><td>Zulassungsdaten</td><td><a href="https://www.swissmedic.ch/">Swissmedic</a></td><td>Liste der zugelassenen Packungen (Humanarzneimittel) mit Wirkstoffen und Gültigkeitsdauer der Zulassung</td></tr>
<tr><td>Vorhersagemodell</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Vorhersage von Zusammenhängen zwischen Arzneimitteln und Krankheiten</td></tr>
<tr><td>Klinische Studien</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Evidenzeinstufung (NCT)</td></tr>
<tr><td>Literatur</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Evidenzeinstufung (PMID)</td></tr>
<tr><td>Arzneimittelinformationen</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Wirkstoffabbildung und Daten zu Zielstrukturen</td></tr>
<tr><td>Wechselwirkungen</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Daten zu Arzneimittelwechselwirkungen</td></tr>
</tbody>
</table>

---

## Lokale Daten dieser Website

Die Schweizer Arzneimittel und ihr Zulassungsstatus stammen aus der Swissmedic-Liste
«Zugelassene Packungen» (Humanarzneimittel). Die Liste enthält nur aktuell zugelassene Packungen und
kein eigenes Statusfeld; massgebend ist die Gültigkeitsdauer der Zulassung.

| Punkt | Angabe |
|------|--------|
| Datensatz | Zugelassene Packungen, Humanarzneimittel (Excel-Datei) |
| Herausgeber | Swissmedic |
| Download | <https://www.swissmedic.ch/dam/swissmedic/de/dokumente/internetlisten/zugelassene_packungen_human.xlsx.download.xlsx/zugelassene_packungen_ham.xlsx> (Übersicht: <https://www.swissmedic.ch/swissmedic/en/home/services/listen_neu.html>) |
| Kennung | Zulassungsnummer |
| Aktualisierung | Automatischer wöchentlicher Download (jeden Montag); eine abgelaufene Gültigkeitsdauer gilt als erloschene Zulassung, eine Zulassungsnummer, die nicht mehr in der Liste steht, behält ihren bisherigen Status |

---

## Lizenzen

Jede Quelle hat ihre eigene Lizenz — bitte prüfen Sie diese vor dem Zitieren:

- **TxGNN**: akademische Nutzung; Huang et al. (2024) zitieren
- **ClinicalTrials.gov / PubMed**: öffentliche Daten der US-amerikanischen NIH
- **DrugBank**: nicht-kommerzielle Nutzung nach Massgabe der Lizenzbedingungen
- **Swissmedic**: nach Massgabe der Open-Data-Bedingungen der Zulassungsbehörde der Schweiz

---

## Aktualisierungsintervall

| Daten | Intervall |
|------|-----------|
| Swissmedic «Zugelassene Packungen» | Wöchentlich (jeden Montag) |
| Evidenz aus Studien / Literatur | Regelmässig erneut erhoben |
| Wechselwirkungsdaten | Vierteljährlich überprüft |

---

## Wissenschaftliche Zitierung

> Huang, K., et al. (2024). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)

---

## Über den Entwickler

Diese Plattform wird von **藥提醒科技有限公司** (yao.care) entwickelt und betrieben. Den vollständigen
Hintergrund zum Unternehmen und zur Methodik finden Sie auf der Seite <a href="{{ '/about/' | relative_url }}">Über uns</a>.

---

<div class="disclaimer">
<strong>Haftungsausschluss</strong><br>
Dieser Bericht dient ausschliesslich als Referenz für die akademische Forschung und <strong>stellt keine medizinische Beratung dar</strong>. Befolgen Sie stets die Anweisungen Ihrer Ärztin oder Ihres Arztes; ändern Sie Ihre Medikation niemals eigenmächtig. Jede Entscheidung zur Arzneimittel-Umwidmung erfordert eine vollständige klinische Validierung und eine regulatorische Prüfung.
<br><br>
<small>Geprüft von: 藥提醒科技有限公司 (yao.care)</small>
</div>
