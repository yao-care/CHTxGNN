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
<tr><td>Zulassungsdaten</td><td><a href="https://www.swissmedic.ch/">Swissmedic</a></td><td>Liste der zugelassenen Arzneimittel und Wirkstoffe für die Schweiz</td></tr>
<tr><td>Vorhersagemodell</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Vorhersage von Zusammenhängen zwischen Arzneimitteln und Krankheiten</td></tr>
<tr><td>Klinische Studien</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Evidenzeinstufung (NCT)</td></tr>
<tr><td>Literatur</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Evidenzeinstufung (PMID)</td></tr>
<tr><td>Arzneimittelinformationen</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Wirkstoffabbildung und Daten zu Zielstrukturen</td></tr>
<tr><td>Wechselwirkungen</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Daten zu Arzneimittelwechselwirkungen</td></tr>
</tbody>
</table>

---

## Lizenzen

Jede Quelle hat ihre eigene Lizenz — bitte prüfen Sie diese vor dem Zitieren:

- **TxGNN**: akademische Nutzung; Huang et al. (2023) zitieren
- **ClinicalTrials.gov / PubMed**: öffentliche Daten der US-amerikanischen NIH
- **DrugBank**: nicht-kommerzielle Nutzung nach Massgabe der Lizenzbedingungen
- **Swissmedic**: nach Massgabe der Open-Data-Bedingungen der Zulassungsbehörde der Schweiz

---

## Aktualisierungsintervall

| Daten | Intervall |
|------|-----------|
| Zulassungsdaten | Nach Veröffentlichung durch die Zulassungsbehörde |
| Evidenz aus Studien / Literatur | Regelmässig erneut erhoben |
| Wechselwirkungsdaten | Vierteljährlich überprüft |

---

## Wissenschaftliche Zitierung

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

---

## Über den Entwickler

Diese Plattform wird von **藥提醒科技有限公司** (yao.care, Unternehmensregisternummer
83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan) entwickelt und betrieben.

CHTxGNN ist die Schweizer Website der Produktlinie «TxGNN Drug Repurposing» des Unternehmens.
Dasselbe System ist in 30 Ländern und Regionen im Einsatz, jeweils unter dem Namen `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN und so weiter) unter `{cc}txgnn.yao.care`.
Produktübersicht: <https://www.yao.care/medical/txgnn/>.

Das Modell TxGNN selbst wurde vom Zitnik Lab an der Harvard Medical School entwickelt und in
*Nature Medicine* veröffentlicht. Diese Plattform ist das Produktivsystem, das 藥提醒科技有限公司 auf
Basis dieses Modells aufgebaut hat; es umfasst die Integration nationaler Arzneimittelzulassungsdaten,
die duale Vorhersage aus Wissensgraph und Deep Learning, die Evidenzbewertung aus PubMed /
ClinicalTrials sowie die Anbindung an elektronische Patientenakten über SMART on FHIR.

---

<div class="disclaimer">
<strong>Haftungsausschluss</strong><br>
Dieser Bericht dient ausschliesslich als Referenz für die akademische Forschung und <strong>stellt keine medizinische Beratung dar</strong>. Befolgen Sie stets die Anweisungen Ihrer Ärztin oder Ihres Arztes; ändern Sie Ihre Medikation niemals eigenmächtig. Jede Entscheidung zur Arzneimittel-Umwidmung erfordert eine vollständige klinische Validierung und eine regulatorische Prüfung.
<br><br>
<small>Geprüft von: 藥提醒科技有限公司 (yao.care)</small>
</div>
