---
layout: default
title: Über uns
nav_order: 90
permalink: /about/
description: "CHTxGNN ist eine Plattform für Vorhersagen zur Arzneimittel-Umwidmung, entwickelt von 藥提醒科技有限公司 (yao.care) auf Basis des Harvard-Modells TxGNN; sie deckt die in der Schweiz von Swissmedic zugelassenen Arzneimittel ab."
---

# Über uns

<div class="key-takeaway">
Mit KI die Evidenzvalidierung der Arzneimittel-Umwidmung beschleunigen — von der Vorhersage bis zur Evidenz auf einen Blick.
</div>

---

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## Schweiz: die Daten dieser Website in Zahlen

Lokale Daten: [Swissmedic: Zugelassene Packungen (Humanarzneimittel)](https://www.swissmedic.ch/swissmedic/en/home/services/listen_neu.html). Die lokalen Daten sind die Swissmedic-Listen der zugelassenen Humanarzneimittel und Packungen. Eine Zulassungsnummer, die in keiner aktuellen Swissmedic-Liste mehr steht, wird hier nicht als gültig gezählt.

| Angabe | Wert |
|---|---|
| Arzneimittel mit veröffentlichtem Bericht | {{ site.data.local_facts.drugs_total }} |
| Arzneimittel in den lokalen Daten | {{ site.data.local_facts.licence.drugs_with_data }} |
| …mit mindestens einem gültigen Eintrag | {{ site.data.local_facts.licence.drugs_with_current }} |
| …mit Einträgen, aber keinem gültigen | {{ site.data.local_facts.licence.drugs_none_current }} |
| Arzneimittel nicht in den lokalen Daten | {{ site.data.local_facts.licence.drugs_without_data }} |
| Lokale Einträge (Swissmedic-Zulassungen) | {{ site.data.local_facts.licence.items_total }} |
| …davon gültige | {{ site.data.local_facts.licence.items_current }} |
| Einträge im Prüfprotokoll | {{ site.data.local_facts.reviews.records }} |
| Arzneimittelseiten mit Prüfprotokoll-Einträgen | {{ site.data.local_facts.reviews.public_pages_with_records }} |
| Vorhergesagte Arzneimittel-Krankheits-Paare, die keine andere TxGNN-Website nennt | {{ site.data.local_facts.cross.unique_pairs }} |

{% if site.data.local_facts.top_licensed.size > 0 %}Arzneimittel mit den meisten gültigen Swissmedic-Zulassungen: {% for r in site.data.local_facts.top_licensed %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.lv }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

{% if site.data.local_facts.recent_reviews.size > 0 %}Letzte Korrekturen im Prüfprotokoll: {% for r in site.data.local_facts.recent_reviews limit: 8 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

Beispiele für Vorhersagen, die keine andere TxGNN-Website für dasselbe Arzneimittel nennt: [Panobinostatum]({{ '/drugs/panobinostatum/' | relative_url }}) → Myeloische Leukämie, [Magnesii Hydroxidum]({{ '/drugs/magnesii-hydroxidum/' | relative_url }}) → Magenerkrankung, [Minoxidilum]({{ '/drugs/minoxidilum/' | relative_url }}) → pulmonary arterial hypertension associated with connective tissue disease, [Acidum Ascorbicum]({{ '/drugs/acidum-ascorbicum/' | relative_url }}) → Nicht-syndromische Ösophagusfehlbildung, [Acidum Chenodeoxycholicum]({{ '/drugs/acidum-chenodeoxycholicum/' | relative_url }}) → Homozygote familiäre Hypercholesterinämie, [Acidum Citricum D200]({{ '/drugs/acidum-citricum-d200/' | relative_url }}) → Magenerkrankung, [Acidum Folicum]({{ '/drugs/acidum-folicum/' | relative_url }}) → Biotin-Stoffwechselerkrankung, [Acidum Fusidicum Anhydricum]({{ '/drugs/acidum-fusidicum-anhydricum/' | relative_url }}) → Expositionskeratitis.

<!-- local-facts:end -->

## Hintergrund

<p class="key-answer" data-question="Was ist CHTxGNN?">
<strong>CHTxGNN</strong> ist eine forschungsunterstützende Plattform für die Arzneimittel-Umwidmung,
aufgebaut auf dem Modell TxGNN, das vom Zitnik Lab der Harvard University in <em>Nature Medicine</em>
veröffentlicht wurde. Sie sagt Indikationserweiterungen für Arzneimittel voraus, die in der Schweiz
von Swissmedic zugelassen sind. Über die KI-Vorhersagewerte hinaus bindet die Plattform klinische
Evidenz aus ClinicalTrials.gov und PubMed ein, damit Forschende rasch beurteilen können, wie
belastbar jede Vorhersage ist.
</p>

---

<!-- local-condensed:start（母目錄 .claude/gen_local_pages_20261119.py；原共用段落縮寫，勿手改）-->
## Über den Entwickler

Diese Plattform wird von **藥提醒科技有限公司** (yao.care, Unternehmensregisternummer 83620786, Taichung, Taiwan) als eine von 30 Länder- und Regionalwebsites der TxGNN-Produktlinie entwickelt und betrieben ([Produktübersicht](https://www.yao.care/medical/txgnn/)).

---

## Die Methode in Kürze

Die Vorhersagen stammen aus TxGNN, einem Graph-Neural-Network-Modell des Zitnik Lab der Harvard Medical School (Huang et al., *Nature Medicine* 2024, [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)); jede vorhergesagte Indikation wird anhand von ClinicalTrials.gov und PubMed in die Stufen L1–L5 eingeordnet. Modell, Stufen und Regeln: [Methodik]({{ '/methodology/' | relative_url }}). Datensätze, Downloads und Lizenzen: [Datenquellen]({{ '/sources/' | relative_url }}).
<!-- local-condensed:end -->

---

## Kontakt

- **GitHub Issues**: <https://github.com/yao-care/CHTxGNN/issues>
- **Entwickler**: 藥提醒科技有限公司 (<https://www.yao.care>, service@yao.care)
- **Produktübersicht**: <https://www.yao.care/medical/txgnn/>

---

<div class="disclaimer">
<strong>Haftungsausschluss</strong><br>
Dieser Bericht dient ausschliesslich als Referenz für die akademische Forschung und <strong>stellt keine medizinische Beratung dar</strong>. Befolgen Sie stets die Anweisungen Ihrer Ärztin oder Ihres Arztes; ändern Sie Ihre Medikation niemals eigenmächtig. Jede Entscheidung zur Arzneimittel-Umwidmung erfordert eine vollständige klinische Validierung und eine regulatorische Prüfung.
<br><br>
<small>Geprüft von: 藥提醒科技有限公司 (yao.care)</small>
</div>
