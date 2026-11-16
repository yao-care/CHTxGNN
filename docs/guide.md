---
layout: default
title: Benutzerhandbuch
nav_order: 92
permalink: /guide/
description: "Benutzerhandbuch zu CHTxGNN: wie man Arzneimittel nachschlägt, Evidenzstufen liest und Empfehlungen einordnet."
---

# Benutzerhandbuch

<div class="key-takeaway">
Prüfen Sie zuerst die Evidenzstufe, dann die Empfehlung und lesen Sie anschliessend die Originalliteratur.
</div>

---

<!-- site-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
## Schweiz: Daten dieser Website

Diese Website veröffentlicht Berichte zu **{{ site.data.drug_stats.total_drugs }}** Arzneimitteln aus den Zulassungsdaten von [Swissmedic](https://www.swissmedic.ch/) (Schweiz).

Datensatz: [Swissmedic: Zugelassene Packungen (Humanarzneimittel)](https://www.swissmedic.ch/swissmedic/en/home/services/listen_neu.html); er wird jede Woche (montags) automatisch heruntergeladen und abgeglichen. Details: [Datenquellen]({{ '/sources/' | relative_url }}).

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

<!-- site-data:end -->

## Ein Arzneimittel nachschlagen

<ol class="actionable-steps">
<li>Verwenden Sie das Suchfeld am oberen Seitenrand (Wirkstoffnamen treffen besser als Handelsnamen).</li>
<li>Oder durchsuchen Sie die vollständige Liste unter <a href="{{ '/drugs/' | relative_url }}">Alle Arzneimittel</a>.</li>
<li>Sie können auch nach Evidenzstufe blättern: <a href="{{ '/evidence-high/' | relative_url }}">hoch</a>, <a href="{{ '/evidence-medium/' | relative_url }}">mittel</a>, <a href="{{ '/evidence-low/' | relative_url }}">nur Modellvorhersage</a>.</li>
</ol>

---

## Einen Bericht lesen

<p class="key-answer" data-question="Was bedeuten die Evidenzstufen L1 bis L5?">
Jeder Arzneimittelbericht führt vorhergesagte neue Indikationen auf, und jede Indikation trägt eine
Evidenzstufe L1&ndash;L5. <strong>L1 bedeutet, dass bereits mehrere randomisierte kontrollierte
Phase-3-Studien sie stützen; L5 bedeutet, dass nur eine Modellvorhersage vorliegt, ohne Evidenz am
Menschen.</strong> Die vollständigen Kriterien finden Sie auf der Seite
<a href="{{ '/methodology/' | relative_url }}">Methodik</a>.
</p>

| Wenn Sie sehen | Bedeutet das | Empfohlenes Vorgehen |
|-----------|----------|------------------|
| L1 / L2 | Evidenz aus klinischen Studien liegt vor | Die zugrunde liegenden NCT- und PMID-Einträge prüfen |
| L3 / L4 | Beobachtende oder präklinische Evidenz | Als Forschungsansatz behandeln |
| L5 | Nur Modellvorhersage | Nur zur Hypothesenbildung; nicht als klinische Referenz |

---

## Zitierung und Nachvollziehbarkeit

Jeder Evidenzbeleg in einem Bericht trägt eine nachvollziehbare Kennung:

- **NCT-Nummer**: verweist auf die Registrierung bei ClinicalTrials.gov
- **PMID**: verweist auf den Eintrag in PubMed
- **DrugBank-ID**: verweist auf Daten zu Arzneimitteln und Zielstrukturen

Bitte lesen Sie die Originalliteratur, um den Kontext zu prüfen, bevor Sie eine Schlussfolgerung
dieser Plattform zitieren.

---

## Häufig gestellte Fragen

<p class="key-answer" data-question="Können die Vorhersagen klinisch genutzt werden?">
<strong>Nein.</strong> Die Vorhersagen dieser Plattform sind Forschungsansätze, keine klinische
Beratung. Jede klinische Anwendung einer Arzneimittel-Umwidmung muss eine vollständige Validierung
in klinischen Studien und eine regulatorische Prüfung durchlaufen.
</p>

<p class="key-answer" data-question="Warum finde ich ein bestimmtes Arzneimittel nicht?">
Ein Wirkstoff muss sich auf das Vokabular von DrugBank abbilden lassen, um in die Vorhersage
aufgenommen zu werden. Pflanzenextrakte, Impfstoffe, Hilfsstoffe und andere in DrugBank nicht
erfasste Einträge erscheinen auf dieser Plattform nicht.
</p>

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
