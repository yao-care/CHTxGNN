---
layout: default
title: "Nur bekannte Anwendungen (keine neuen Vorhersagen)"
nav_order: 24
permalink: /known-uses/
description: "Bei diesen Arzneimitteln sind alle Kandidaten des TxGNN-Modells bereits bekannte Anwendungen (im Wissensgraphen oder in einer Zulassung erfasst); es gibt d…"
---

# Nur bekannte Anwendungen (keine neuen Vorhersagen)

Bei diesen Arzneimitteln sind alle Kandidaten des TxGNN-Modells bereits bekannte Anwendungen (im Wissensgraphen oder in einer Zulassung erfasst); es gibt daher keine neue vorhergesagte Indikation. Jede Seite listet die bekannten Anwendungen und den lokalen Marktstatus.

{% assign known_drugs = site.drugs | where: "evidence_level", "N/A" | sort: "title" %}

**{{ known_drugs.size }} Arzneimittel**

| Arzneimittel | Bericht |
|------|------|
{% for drug in known_drugs %}| **{{ drug.title }}** | [Seite ansehen]({{ drug.url | relative_url }}) |
{% endfor %}
