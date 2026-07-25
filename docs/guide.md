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
