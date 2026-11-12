"""本站查核機制的在地設定（2026-11-12 建；核心流程比照 TwTxGNN、UsTxGNN，程式在同目錄與 scripts/）。

頁面上的查核框、查核紀錄表、說明文字用本站語言（德文）；依據是 Swissmedic 核准包裝清單（zugelassene Packungen）。
改這裡的字樣後跑 python3 scripts/apply_drug_reviews.py 重套，gate（scripts/check_seo_docs.py）會檢查。
COMMITS／REGEN_COMMITS：2026-10-31～11-06 正文的許可證刪改提交與期間內 AI 重產報告的提交（scripts/reviews_from_edits.py --git 用）。
"""
import json as _json

C = _json.loads(r"""{
 "SITE": "CHTxGNN",
 "ID_PREFIX": "ch",
 "SNAPSHOT": "ch_licenses.json.gz",
 "HEADER_LABEL": "Evidenzniveau",
 "OVERVIEW_LABELS": [
  "Evidenzniveau",
  "Evidenzstufe"
 ],
 "WITHDRAWN_RE": "Zurückgezogen|Widerrufen",
 "DESC_LEVEL_RE": "Evidenzstufe (L[1-5]|N/A)",
 "DESC_LEVEL_FMT": "Evidenzstufe {lv}",
 "NA_DESC": "nur bekannte Anwendungen",
 "HEADER_RULE_NOTE": "2026-11-12 實測：有 Quick Overview 等級的 98 頁，頁首全部等於第一個等級（本站整格取最高也是 0 頁不同）；沒有總覽表的 719 頁簡頁頁首不動",
 "MARKET_RE": "Markt|Grundlegende Informationen",
 "ID_RE": "\\b\\d{5}\\b",
 "PROSE_ID_RE": null,
 "ORIGINAL_LABELS": [
  "Ursprüngliche Indikation",
  "Originalindikation"
 ],
 "ORIGINAL_NONE_RE": "^\\s*(in den lokalen daten nicht|nicht (erfasst|verfügbar|angegeben)|keine|n/a|–|-)",
 "ORIGINAL_SPLIT_RE": "[;,/()]+|\\bund\\b|\\boder\\b",
 "ORIGINAL_NOTE": "2026-11-12：證據包的許可證紀錄來自 Swissmedic 核准包裝清單；可比對頁數以程式輸出為準",
 "COMMITS": [],
 "REGEN_COMMITS": [
  "53c06b36",
  "cfeb1489",
  "d461ce7a",
  "92173fa9"
 ],
 "SOURCES": [
  {
   "title": "Swissmedic – Zugelassene Packungen (Humanarzneimittel)",
   "url": "https://www.swissmedic.ch/dam/swissmedic/de/dokumente/internetlisten/zugelassene_packungen_human.xlsx.download.xlsx/zugelassene_packungen_ham.xlsx"
  }
 ],
 "PROGRAM_LINE_RE": null,
 "CLASSIFY": [
  [
   "tw",
   "Taiwan|TFDA|台灣|臺灣"
  ],
  [
   "combo",
   "Einzelwirkstoff|Kombinationspräparat|Kombinationsprodukt|Monopräparat|Einzelpräparat"
  ],
  [
   "cancel",
   "erlosch|widerruf|ungültig|zurückgezogen|nicht (?:mehr )?(?:zugelassen|im Handel|gültig|vermarktet)|keine (?:gültige|aktive|gültigen)|außer Handel|ausgelaufen|abgelaufen|gestrichen"
  ],
  [
   "count",
   "\\b\\d+\\b[^.;]{0,40}(?:Zulassung|Packung|Präparat|Produkt|Eintr|Datens)|(?:Zulassung|Packung|Präparat|Produkt|Eintr)[^.;]{0,30}\\b\\d+\\b|\\b(?:alle|beide|sämtliche)\\b[^.;]{0,30}(?:Zulassung|gültig)|\\bgültig"
  ],
  [
   "product",
   "\\b(?:als|in Form|Darreichungsform|Tablette|Kapsel|Injektion|Salbe|im Handel|vermarktet)\\b"
  ]
 ],
 "T": {
  "label": {
   "correct": "Prüfkorrektur",
   "annotate": "Prüfhinweis",
   "rereview": "Erneute Prüfung ausstehend",
   "rereview_result": "Ergebnis der erneuten Prüfung"
  },
  "action": {
   "correct": "Korrigiert",
   "annotate": "Hinweis ergänzt",
   "rereview": "Zur erneuten Prüfung markiert",
   "section": "Belegten Abschnitt ergänzt",
   "rereview_result": "Erneute Prüfung abgeschlossen",
   "header_level": "Evidenzniveau im Seitenkopf aus der Schnellübersicht neu berechnet",
   "description_level": "Evidenzstufe in der Seitenbeschreibung an den Seitenkopf angeglichen"
  },
  "verdict": {
   "maintain": "Beibehalten",
   "downgrade": "Herabgestuft",
   "upgrade": "Heraufgestuft",
   "withdraw": "Zurückgezogen"
  },
  "log_head": "## Prüfprotokoll",
  "disclaimer_re": "Haftungsausschluss",
  "log_cols": [
   "Prüfdatum",
   "Punkt",
   "Maßnahme",
   "Quelle"
  ],
  "level_same": "Evidenzstufe {o} unverändert",
  "level_change": "Evidenzstufe {o} → {n}",
  "orig": "Ursprünglich stand hier: „{x}“",
  "table_updated": "Die Angaben „{labels}“ auf dieser Seite wurden an das Prüfergebnis angepasst; die ursprünglichen Werte stehen im Prüfprotokoll unten.",
  "decision": "Entscheidungsempfehlung: {x}",
  "source": "Quelle",
  "rereviewed": "Zur erneuten Prüfung markiert → erneut geprüft (siehe Ergebnis der erneuten Prüfung)",
  "hdr": "Evidenzniveau im Seitenkopf aus der Schnellübersicht neu berechnet ({o} → {n})",
  "hdr_withdraw": "Hauptvorhersage bei erneuter Prüfung zurückgezogen; Evidenzniveau im Seitenkopf neu berechnet ({o} → {n})",
  "now_listed": ", jetzt unter „{x}“",
  "rr": "Erneute Prüfung: {v}, {c}",
  "tu": "; {l}: „{a}“ → „{b}“",
  "desc": "Seitenbeschreibung: „{a}“ geändert in „{b}“ (folgt dem Seitenkopf; übriger Text unverändert, Original im Protokoll)",
  "revised": " (überarbeitet am {d}; frühere Fassung im Protokoll erhalten)",
  "superseded": "Durch die programmatisch erzeugte Zulassungstabelle ersetzt (vorher: {a})",
  "regen": "Nach Neuerstellung des Berichts nicht mehr vorhanden ({d}: {n}; vorher: {a})",
  "program": "Nach einer Programmkorrektur nicht mehr vorhanden ({d}: {n}; vorher: {a})",
  "withdrawn": "Prüfung zurückgezogen ({d}: {n}; vorher: {a})",
  "intro": "Nachfolgend das Prüfprotokoll dieser Seite: Aussagen, die mit den amtlichen Zulassungsdaten (Swissmedic-Liste der zugelassenen Packungen) abgeglichen wurden. Korrekturen beschränken sich auf grundlegende Sachangaben; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.",
  "intro_header": "Nachfolgend das Prüfprotokoll dieser Seite; das Evidenzniveau im Seitenkopf folgt der Schnellübersicht. Modellvorhersagen, Übersichtstabelle und Schlussfolgerungen wurden nicht umgeschrieben.",
  "intro_rr": "Nachfolgend das Prüfprotokoll dieser Seite: Aussagen, die mit den amtlichen Zulassungsdaten (Swissmedic-Liste der zugelassenen Packungen) abgeglichen wurden. Korrekturen beschränken sich auf grundlegende Sachangaben, der Text der Modellvorhersage wurde nicht umgeschrieben; Evidenzstufen und Entscheidungen wurden nur durch ein Ergebnis der erneuten Prüfung (Herab-, Heraufstufung oder Rückzug) geändert, die ursprünglichen Werte stehen unten.",
  "figures": "In den Daten (Swissmedic-Liste der zugelassenen Packungen) sind für dieses Arzneimittel {total} Zulassungen erfasst, davon {valid} gültig; die aktuellen Zahlen stehen in der Schnellübersicht und bei den Marktinformationen.",
  "data_as_of": "Swissmedic-Liste der zugelassenen Packungen, Stand {date}",
  "notes": {
   "rewrite": "Korrigiert: Die Aussage stimmte nicht mit den Zulassungsdaten überein ({d}) und wurde durch den jetzigen Wortlaut ersetzt.",
   "tw": "Entfernt: Textbaustein aus der taiwanischen Vorlage (TFDA), der für diese Seite nicht gilt.",
   "combo": "Entfernt: Die Angabe zu Einzel- oder Kombinationspräparaten stimmte nicht mit den Zulassungsdaten überein ({d}).",
   "cancel": "Entfernt: Die Aussage, die Zulassungen seien erloschen, widerrufen oder ungültig, stimmte nicht mit den Zulassungsdaten überein ({d}).",
   "count": "Entfernt: Die angegebene Zahl oder der Status der Zulassungen stimmte nicht mit den Zulassungsdaten überein ({d}).",
   "product": "Entfernt: Die Beschreibung der Präparate stimmte nicht mit den Zulassungsdaten überein ({d}).",
   "generic": "Entfernt: Die Aussage widersprach den Zulassungsdaten ({d})."
  },
  "notes_with_figures": [
   "cancel",
   "count",
   "product",
   "generic"
  ],
  "summary": "Entfernt: „{x}“",
  "regen_note": "der Bericht wurde im November 2026 neu erstellt und enthält diese Aussage nicht mehr"
 }
}""")
