---
layout: default
title: Vorhersagen zur Arzneimittel-Umwidmung
nav_order: 1
description: "KI-gestützte Vorhersagen zur Arzneimittel-Umwidmung für die Schweiz. Evidenzbasierte Analyse zugelassener Arzneimittel auf mögliche neue Anwendungsgebiete."
permalink: /
---

# Vorhersagen zur Arzneimittel-Umwidmung — Schweiz

Dieses Projekt verwendet das TxGNN-Modell (Deep Learning), um potenzielle neue therapeutische Anwendungen für in der Schweiz zugelassene Arzneimittel vorherzusagen.

**Haftungsausschluss**: Dieser Inhalt dient ausschließlich Forschungszwecken und stellt keine medizinische Beratung dar. Alle Vorhersagen zur Arzneimittel-Umwidmung erfordern eine klinische Validierung vor der Anwendung.

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## Schweiz: Umfang dieser Website

Diese Website veröffentlicht Berichte zu **{{ site.data.drug_stats.total_drugs }}** Arzneimitteln aus den Zulassungsdaten von [Swissmedic](https://www.swissmedic.ch/) (Schweiz).

### Lokale Daten dieser Website

| Punkt | Angabe |
|------|--------|
| Datensatz | Zugelassene Packungen, Humanarzneimittel (Excel-Datei) |
| Herausgeber | Swissmedic |
| Download | <https://www.swissmedic.ch/dam/swissmedic/de/dokumente/internetlisten/zugelassene_packungen_human.xlsx.download.xlsx/zugelassene_packungen_ham.xlsx> (Übersicht: <https://www.swissmedic.ch/swissmedic/en/home/services/listen_neu.html>) |
| Kennung | Zulassungsnummer |
| Aktualisierung | Automatischer wöchentlicher Download (jeden Montag); eine abgelaufene Gültigkeitsdauer gilt als erloschene Zulassung, eine Zulassungsnummer, die nicht mehr in der Liste steht, behält ihren bisherigen Status |

Details: [Datenquellen]({{ '/sources/' | relative_url }}).

Berichte nach Evidenzstufe:

| Evidenzstufe | Berichte | Anteil |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

3 vorhergesagte Arzneimittel-Krankheits-Paare dieser Website kommen auf keiner anderen der 30 TxGNN-Websites vor.

### Arzneimittel mit der höchsten Evidenzstufe auf dieser Website

| Arzneimittel | Evidenzstufe |
|---|---|
| [Calcipotriol](/drugs/calcipotriol/) | L3 |
| [Velpatasvir](/drugs/velpatasvir/) | L3 |
| [Tryptophan](/drugs/tryptophan/) | L3 |

### Arzneimittel, die unter den 30 TxGNN-Websites nur diese Website abdeckt

| Arzneimittel | Evidenzstufe |
|---|---|
| [Echinacea](/drugs/echinacea/) | L5 |

<!-- local-home:end -->

## Über den Entwickler

Diese Plattform wird von **藥提醒科技有限公司** (yao.care) entwickelt und betrieben. Den vollständigen
Hintergrund zum Unternehmen und zur Methodik finden Sie auf der Seite <a href="{{ '/about/' | relative_url }}">Über uns</a>.
