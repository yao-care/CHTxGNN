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

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## Schweiz: ein Beispiel von dieser Website

Ein Bericht auf dieser Website wird in drei Schritten gelesen: Evidenzstufe, lokale Marktdaten, Prüfprotokoll.

{% assign gx = site.data.local_facts.example %}
{% if gx %}Öffnen Sie [{{ gx.t }}]({{ gx.u | relative_url }}): Der Kopf zeigt Evidenzstufe **{{ gx.l }}**; die wichtigste vorhergesagte neue Indikation ist **{{ gx.i }}**; die lokalen Daten enthalten **{{ gx.lt }}** Swissmedic-Zulassungen, davon **{{ gx.lv }}** gültige; das Prüfprotokoll der Seite hat **{{ gx.r }}** Einträge.{% endif %}

{% if site.data.local_facts.most_reviewed.size > 0 %}Arzneimittel mit den meisten Prüfprotokoll-Einträgen: {% for r in site.data.local_facts.most_reviewed %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.r }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

{% if site.data.local_facts.recent_reviews.size > 0 %}Letzte Korrekturen im Prüfprotokoll: {% for r in site.data.local_facts.recent_reviews limit: 8 offset: 8 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

Beispiele für Vorhersagen, die keine andere TxGNN-Website für dasselbe Arzneimittel nennt: [Acidum Salicylicum]({{ '/drugs/acidum-salicylicum/' | relative_url }}) → Papilläre Konjunktivitis, [Acidum Tranexamicum]({{ '/drugs/acidum-tranexamicum/' | relative_url }}) → amenorrhea (disease), [Acidum Ursodeoxycholicum]({{ '/drugs/acidum-ursodeoxycholicum/' | relative_url }}) → Homozygote familiäre Hypercholesterinämie, [Acidum Valproicum]({{ '/drugs/acidum-valproicum/' | relative_url }}) → Trigeminusnerven-Neoplasie, [Almotriptanum]({{ '/drugs/almotriptanum/' | relative_url }}) → atrophoderma vermiculata, [Benzylpenicillinum]({{ '/drugs/benzylpenicillinum/' | relative_url }}) → Perikoronitis.

<!-- local-facts:end -->

## Ein Arzneimittel nachschlagen

<ol class="actionable-steps">
<li>Verwenden Sie das Suchfeld am oberen Seitenrand (Wirkstoffnamen treffen besser als Handelsnamen).</li>
<li>Oder durchsuchen Sie die vollständige Liste unter <a href="{{ '/drugs/' | relative_url }}">Alle Arzneimittel</a>.</li>
<li>Sie können auch nach Evidenzstufe blättern: <a href="{{ '/evidence-high/' | relative_url }}">hoch</a>, <a href="{{ '/evidence-medium/' | relative_url }}">mittel</a>, <a href="{{ '/evidence-low/' | relative_url }}">nur Modellvorhersage</a>.</li>
</ol>

---

<!-- local-condensed:start（母目錄 .claude/gen_local_pages_20261119.py；原共用段落縮寫，勿手改）-->
## Einen Bericht lesen

<p class="key-answer" data-question="Was bedeuten die Evidenzstufen L1 bis L5?">
Jede vorhergesagte Indikation hat eine Stufe von <strong>L1</strong> (mehrere Phase-3-Studien) bis <strong>L5</strong> (nur Modellvorhersage). Jeder Beleg nennt eine NCT- oder PMID-Nummer zum Nachlesen; Vorhersagen sind Forschungshinweise, keine klinische Empfehlung. Definitionen und Regeln: <a href="{{ '/methodology/' | relative_url }}">Methodik</a>.
</p>
<!-- local-condensed:end -->

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
