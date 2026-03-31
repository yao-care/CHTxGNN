# CHTxGNN - Schweiz: Arzneimittel-Repositionierung

[![Website](https://img.shields.io/badge/Website-chtxgnn.yao.care-blue)](https://chtxgnn.yao.care)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Vorhersagen zur Arzneimittel-Repositionierung (Drug Repurposing) fuer die Schweiz mit dem TxGNN-Modell.

## Haftungsausschluss

- Die Ergebnisse dieses Projekts dienen ausschliesslich zu Forschungszwecken und stellen keine medizinische Beratung dar.
- Kandidaten fuer die Arzneimittel-Repositionierung erfordern eine klinische Validierung vor der Anwendung.

## Projektuebersicht

| Element | Anzahl |
|---------|--------|
| **Arzneimittelberichte** | 725 |
| **Gesamtvorhersagen** | 20,463,352 |

## Vorhersagemethoden

### Wissensgraph-Methode (Knowledge Graph)
Direkte Abfrage von Arzneimittel-Krankheits-Beziehungen im TxGNN-Wissensgraphen, Identifizierung potenzieller Repositionierungskandidaten basierend auf bestehenden Verbindungen im biomedizinischen Netzwerk.

### Deep-Learning-Methode
Verwendet das vortrainierte neuronale Netzwerkmodell TxGNN zur Berechnung von Vorhersagewerten und bewertet die Wahrscheinlichkeit neuer therapeutischer Indikationen fuer zugelassene Arzneimittel.

## Links

- Webseite: https://chtxgnn.yao.care
- TxGNN-Publikation: https://doi.org/10.1038/s41591-023-02233-x
