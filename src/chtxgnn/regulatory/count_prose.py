"""正文許可證張數的程式改寫（2026-11-24 建，用戶決定「正文張數自動改寫」；做法移植 KrTxGNN／MyTxGNN 同名檔，
本站從 DETxGNN 同名檔改寫：德文句型相同，資料範圍換成 Swissmedic 許可）。

正文裡「N von M Zulassungen sind gültig」「N gültige Zulassung(en) (von M)」「Von M erfassten Zulassungen sind N gültig」
「Alle N Zulassungen sind gültig」這類 Swissmedic 許可張數敘述，由程式依許可證快照（snapshots/ch_licenses.json.gz 的 facts）改寫，
每週資料更新後跟著改，不逐筆寫查核紀錄（同 Kr／My／Tw：程式改寫的張數敘述是程式產生的正文）。

只改「句型明確、數字確定是本藥 Swissmedic 許可張數」的地方，其餘一律不動：
  - 句子要有許可字樣（Zulassung），且沒有試驗、文獻、病人、劑量、年份等字樣（NOT_LICENSE）。
  - 跳過：查核框（<!-- review -->）、程式許可證區塊（<!-- licenses -->）、表格列、標題、front matter；
    查核紀錄 replacement／anchor 所在的句子（改了紀錄會對不上）。
  - 整句不動（skipped）：有保留（mindestens、unvollständig、Auswahl…）、講證據包或查詢（Evidence Pack、Abfrage、ergab…）、
    相對數（weitere、andere、zusätzlich、übrige）、劑型或單方／複方子集（本站事實層的單方張數用「;;」切成分、Swissmedic 的成分欄
    用「, 」，算不準，所以單方／複方句一律不動）、獸用、其他國家或 EU 許可（FDA、EMA、EU-、Deutschland…；本站範圍就是瑞士，
    「Schweiz」「Swissmedic」不算保留）、
    講表格顯示筆數（Tabelle、Liste、aufgeführt、angezeigt…，reason＝display）；事實層 partial（證據包只收了部分包裝）或總數 0 的頁整頁不動。
角色：「X von Y」的 X 看後面的狀態字（gültig→有效；erloschen／gelöscht／abgelaufen／zurückgezogen／widerrufen→註銷），Y＝總數；
「Von M … sind N gültig」M＝總數、N＝有效；「N gültige …」有效；「N erloschene …」註銷；「N (erfasste) Zulassungen」總數
（後面接「sind erloschen」算註銷）；其餘數字不動。數字可寫成阿拉伯數字或 zwei～zwölf、beide；「eine／ein」只在緊接
（gültige）Zulassung 時算 1。改寫時保留原寫法（文字數字改成文字，超過 12 用阿拉伯數字）。
同一行只要有一句含許可證數字而被略過，整行都不動（免得前後句數字對不上）。
數字已等於該角色的任一合理讀法（沒有限定詞的總數＝總數或有效數）就不動；不等於時兩種讀法相同才改，不同列為 ambiguous。
不改、列出（要改請寫查核紀錄）：原數字 0（zero-premise）、新數字 0（zero-result）、1 跟非 1 之間的改動（德文單複數與動詞要跟著改，
grammar）、句子說「alle／beide … gültig」或「keine … erloschen」而有效≠總數（premise）。
"""
from __future__ import annotations

import re

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-ZÄÖÜ*\[(>-])")
WORDS = {"zwei": 2, "drei": 3, "vier": 4, "fünf": 5, "sechs": 6, "sieben": 7, "acht": 8, "neun": 9, "zehn": 10,
         "elf": 11, "zwölf": 12, "beide": 2, "beiden": 2}
W_OUT = {v: k for k, v in WORDS.items() if k not in ("beide", "beiden")}
ONE = r"(?:eine|ein|einer|einen)"
NUM = re.compile(r"(?<![\w.,/-])(\d{1,4}|" + "|".join(sorted(WORDS, key=len, reverse=True)) + r"|" + ONE +
                 r"(?=\s+(?:(?:einzige[nr]?\s+)(?:gültige[nr]?\s+|erloschene[nr]?\s+)?|(?:gültige[nr]?\s+|erloschene[nr]?\s+))(?:zentrale[nr]?\s+)?(?:EU-|EMA-)?Zulassung))(?![\w%-])", re.I)
LICENSE = re.compile(r"Zulassung", re.I)
NOT_LICENSE = re.compile(r"Studie|Probanden|Patient|PMID|NCT|Publikation|Artikel|Fall|\bmg\b|\bml\b|%|Jahr|Monat|Woche|Dosis|Score|"
                         r"Indikationen|Phase-|\b(?:19|20)\d\d\b", re.I)
HEDGED = re.compile(r"mindestens|zumindest|wenigstens|unvollständig|teilweise|Auswahl|möglicherweise|vermutlich|"
                    r"Evidenz-?Paket|Evidence Pack|Abfrage|abgefragt|ergab|lieferte|zurückgegeben|Datensatz|Datensätze|"
                    r"weitere[nrs]?\b|andere[nrs]?\b|zusätzlich|übrige[nrs]?\b|restliche|darunter|"
                    r"Tierarzneim|veterinär|EMEA/V|Einzelwirkstoff|Einzelpräparat|Monopräparat|Kombination|"
                    r"Tablette|Kapsel|Injektion|Infusion|Lösung|Pulver|Spritze|\bPen\b|Tropfen|Creme|Salbe|Inhal|Pflaster|Implantat|"
                    r"FDA|USA|\bUS-|\bEMA\b|\bEU\b|EU-|europäisch|zentral|Deutschland|BfArM|Hersteller|Zulassungsinhaber", re.I)
DISPLAY = re.compile(r"Tabelle|Liste|\bzeigt|\bersten\b|aufgeführt|aufgelistet|gelistet|angezeigt|dargestellt|\boben\b|\bunten\b|folgende", re.I)
CANC = r"(?:erlosch\w*|gelöscht\w*|abgelaufen\w*|zurückgezogen\w*|zurückgenommen\w*|widerruf\w*|aufgehoben\w*|ungültig\w*)"
VALID = r"(?:gültig\w*|aktiv\w*)"
ADJ = r"(?:(?:erfasste[nr]?|vorhandene[nr]?|hinterlegte[nr]?|registrierte[nr]?|schweizerische[nr]?|einzige[nr]?)\s+)*(?:EU-|EMA-)?"
NOUN = r"Zulassung(?:en)?"
BLOCK = re.compile(r"<!-- (review|licenses):begin.*?<!-- \1:end[^>]*-->", re.S)


def _val(tok):
    t = tok.lower()
    if t.isdigit():
        return int(t)
    if t in WORDS:
        return WORDS[t]
    return 1


def _fmt(tok, v):
    if tok.lower() == "beide":  # 「Beide Zulassungen sind gültig」→「Alle drei Zulassungen …」
        w = "alle " + W_OUT.get(v, str(v))
        return w.capitalize() if tok[:1].isupper() else w
    if tok.isdigit() or v not in W_OUT or re.fullmatch(ONE, tok, re.I):
        return str(v)
    w = W_OUT[v]
    return w.capitalize() if tok[:1].isupper() else w


def _role(s, a, b):
    left, right = s[max(0, a - 45):a], s[b:b + 70]
    # 「X von Y」的 Y（前面是數字或「gültige(n) Zulassung(en)」）＝總數；其他「von N」（Auswahl von 5…）不動
    if re.search(r"\bvon\s+(?:den\s+|insgesamt\s+)?$", left, re.I):
        pre = re.sub(r"\bvon\s+(?:den\s+|insgesamt\s+)?$", "", left, flags=re.I)
        if re.search(r"(\d+|" + "|".join(WORDS) + r"|" + ONE + r")\s*$", pre, re.I) or \
                re.search(r"(gültige[nr]?|erloschene[nr]?)\s+(?:(?:EU-|EMA-)?" + NOUN + r"\s*)?\(?$", pre, re.I):
            return "total"
        if re.search(r"(?:^|[(;,]\s*|\.\s+)$", pre) and re.match(r"\s+" + ADJ + NOUN + r"\b", right):
            return "total"  # 「Von 5 Zulassungen sind 4 gültig」
        return None
    # CH 補（2026-11-24）：「X der Y Zulassungen」（16 der 17 Zulassungen sind gültig）的 Y＝總數；「der」前面不是數字的不算
    if re.search(r"\bder\s+$", left, re.I) and re.search(r"(\d+|" + "|".join(WORDS) + r"|" + ONE + r")\s+der\s+$", left, re.I) \
            and re.match(r"\s+" + ADJ + NOUN + r"\b", right):
        return "total"
    # 「X von Y …」「X der Y …」的 X：看後面的狀態字
    m = re.match(r"\s+(?:von|der)\s+(?:den\s+)?\S+\s+" + ADJ + r"(?:" + NOUN + r")?\s*(?:\([^)]*\)\s*)?(?:(?:ist|sind|bleib\w*|davon|derzeit|aktuell|noch|weiterhin)\s+){0,3}(" + VALID + "|" + CANC + ")", right, re.I)
    if m:
        return "cancelled" if re.match(CANC, m.group(1), re.I) else "valid"
    if re.match(r"\s+(?:von|der)\s+\S+\s+" + ADJ + NOUN, right, re.I):
        return None  # 「X der Y Zulassungen …」後面沒有狀態字：不判
    if re.match(r"\s+von\s+", right):
        if re.search(r"gültige[nr]?\s+" + NOUN + r"\s*\(?$|gültig\w*\s*\(?$", left, re.I):
            return "valid"  # 「eine gültige Zulassung (1 von 1)」
        return None
    if re.match(r"\s+(?:\w+\s+)?" + VALID, right, re.I) and not re.match(r"\s+(?:\w+\s+)?gültig\w*\s+(?!Zulassung|von)", right, re.I) \
            or re.match(r"\s+(?:\w+\s+)?gültige[nr]?\s+(?:EU-|EMA-)?(?:" + NOUN + r"|von)", right, re.I):
        return "valid"
    if re.match(r"\s+(?:\w+\s+)?" + CANC + r"\s+(?:EU-|EMA-)?" + NOUN, right, re.I):
        return "cancelled"
    m = re.match(r"\s+" + ADJ + NOUN + r"\b([^.;,:]{0,30})", right, re.I)
    if m:
        tail = m.group(1)
        if re.search(r"\b(sind|ist|wurden|wurde)\s+(?:\w+\s+)?" + CANC, tail, re.I):
            return "cancelled"
        if re.search(r"\bsind\s+(?:\w+\s+)?gültig", tail, re.I) and not re.search(r"\b(alle|sämtliche|beide)\s*$", left, re.I):
            return "valid"
        return "total"
    # CH 補（2026-11-24）：「… sind 4 gültig und 2 gelöscht」的 2（狀態字後面沒有名詞）
    if re.match(r"\s+(?:\w+\s+)?" + CANC + r"(?![\w-])", right, re.I) and re.search(r"\b(?:und|sowie)\s+$|,\s*$", left, re.I):
        return "cancelled"
    # 「Von 5 Zulassungen sind 4 gültig」的 4
    if re.search(r"\b(?:sind|ist)\s+(?:derzeit\s+|aktuell\s+|noch\s+)?$", left, re.I) and re.match(r"\s+" + VALID, right, re.I):
        return "valid"
    return None


def _readings(role, f, explicit):
    t, v, c = f.get("total"), f.get("valid"), f.get("cancelled")
    if role == "cancelled":
        return {c}, c
    if role == "valid":
        return {v}, v
    if explicit:
        return {t}, t
    return {t, v}, (t if t == v else None)


def _premise_ok(sent, f):
    lo = sent.lower()
    if re.search(r"\b(alle|sämtliche|beide[n]?|die einzige)\b[^.;]{0,50}" + VALID, lo) and (f.get("valid") != f.get("total")):
        return False
    if re.search(r"\bkeine?\b[^.;]{0,30}" + CANC, lo) and f.get("cancelled"):
        return False
    return True


def rewrite_sentence(sent, f):
    """回傳 (新句子, 跳過理由或 None)。"""
    if not LICENSE.search(sent) or not NUM.search(sent):
        return sent, None
    found = [(m, _role(sent, m.start(), m.end())) for m in NUM.finditer(sent)]
    found = [(m, r) for m, r in found if r]
    if not found:
        return sent, None
    if NOT_LICENSE.search(sent):
        return sent, None
    if HEDGED.search(sent):
        return sent, "hedged/subset"
    explicit = any(r in ("valid", "cancelled") for _, r in found)
    if DISPLAY.search(sent):  # 講表格顯示筆數：不改；數字跟事實對不上時列出（reason＝display）
        bad = any(_val(m.group(1)) not in _readings(r, f, explicit)[0] for m, r in found)
        return sent, ("display" if bad else "display-ok")
    subs = []
    for m, role in found:
        old = _val(m.group(1))
        ok, v = _readings(role, f, explicit)
        if old in ok:
            continue
        if v is None:
            return sent, "ambiguous"
        if old == 0:
            return sent, "zero-premise"
        if v == 0:
            return sent, "zero-result"
        if m.group(1).lower() == "beiden":
            return sent, "grammar"
        subs.append((m, role, old, v))
    if not _premise_ok(sent, f):  # CH 補（2026-11-24）：「alle vier … gültig」數字本身對得上有效數、但有效≠總數時也算錯前提
        return sent, "premise"
    if not subs:
        return sent, None
    if any((o == 1) != (v == 1) for _, _, o, v in subs) and re.search(r"\b(einzige|diese|dieser|jene|die eine|der einen)\s+(\w+\s+)?Zulassung\b", sent, re.I):
        return sent, "premise"  # 「die einzige Zulassung」「Diese Zulassung ist gültig」：說只有一張
    out, pos = [], 0
    for m, _, _, v in subs:
        out.append(sent[pos:m.start(1)])
        out.append(_fmt(m.group(1), v))
        pos = m.end(1)
    out.append(sent[pos:])
    new = "".join(out)
    if re.search(r"(?<![\w.,/-])(\S+)\s+der\s+\1\s+" + ADJ + NOUN, new, re.I):
        return sent, "grammar"  # CH 補：改完變成「fünf der fünf Zulassungen」（全部有效）時要換句型，不自動改
    if any((o == 1) != (v == 1) for _, _, o, v in subs):
        new = _agree(new, f, explicit)
        if new is None:
            return sent, "grammar"
    return new, None


VERBS = {"ist": "sind", "besteht": "bestehen", "liegt": "liegen", "existiert": "existieren", "bleibt": "bleiben",
         "wurde": "wurden", "gilt": "gelten"}
VERB_RE = r"(?:" + "|".join(list(VERBS) + list(VERBS.values())) + r")"
ADV = r"(?:(?:es|derzeit|aktuell|noch|nur|insgesamt|laut den Daten|in den Daten|in diesem Land|in der Schweiz|hierzulande|zudem)\s+)*"
NP_TAIL = r"(?:\s+(?:(?:gültige[nr]?|erloschene[nr]?)\s+)?" + ADJ + r"Zulassung(?:en)?)?(?:\s+\(?von\s+(?:insgesamt\s+)?\S+?(?:\s+" + ADJ + r"Zulassung(?:en)?)?\)?)?"


def _flip(v, n):
    sg = next((k for k, x in VERBS.items() if v.lower() in (k, x)), None)
    w = sg if n == 1 else VERBS[sg]
    return w.capitalize() if v[:1].isupper() else w


def _agree(sent, f, explicit):
    """數字跨過 1 的改寫後，名詞單複數與動詞跟著改（只處理句型明確的；判斷不了回 None）。
    名詞：每個計數數字後面（可隔 ADJ／gültige(n)）的 Zulassung／Zulassungen 照數字改；
    動詞：只在數字是主詞時改——數字前面緊接 ist／besteht／liegt…（中間只隔 derzeit、in der Schweiz 等副詞），
    或數字名詞片語（含「von N」）後面緊接動詞；數字前面是介系詞或冠詞（mit、von、die…）時不改動詞。"""
    found = [(m, _role(sent, m.start(), m.end())) for m in NUM.finditer(sent)]
    found = [(m, r) for m, r in found if r]
    # 冠詞＋數字（die 1 vorhandene Zulassung）：形容詞變格要跟著改，不處理
    if any(re.search(r"\b(die|der|den|des|dem)\s+$", sent[:m.start()], re.I) for m, _ in found):
        return None
    # 數字片語以外還有單數「Zulassung」（Die Zulassung ist gültig; …）：說只有一張，不處理
    rest = sent
    for m, _ in reversed(found):
        mm = re.match(NP_TAIL, rest[m.end():])
        rest = rest[:m.start()] + " # " + rest[m.end() + (mm.end() if mm else 0):]
    if re.search(r"\bZulassung\b(?!en|s)", rest):
        return None
    out = sent
    for m, r in reversed(found):
        n = _val(m.group(1))
        mm = re.match(r"(\s+(?:(?:gültige[nr]?|erloschene[nr]?)\s+)?" + ADJ + r")(Zulassung(?:en)?)\b", out[m.end():])
        if mm:
            a = m.end() + mm.start(2)
            out = out[:a] + ("Zulassung" if n == 1 else "Zulassungen") + out[a + len(mm.group(2)):]
    # 主詞數字：有效／註銷數字優先，否則第一個
    found = [(m, _role(out, m.start(), m.end())) for m in NUM.finditer(out)]
    found = [(m, r) for m, r in found if r]
    subj = next((m for m, r in found if r in ("valid", "cancelled")), found[0][0] if found else None)
    if subj is None:
        return out
    if re.search(r"\b(mit|von|bei|für|nach|aus|zu|unter|über|besitzt|hat|umfasst|hält|zählt|weist)\s+(?:\w+\s+)?$", out[:subj.start()], re.I) \
            and not re.search(r"\bvon\s+(?:den\s+)?\S+\s+" + ADJ + r"Zulassung", out[:subj.start()], re.I):
        return out  # 數字不是主詞（Das Arzneimittel ist … mit 1 gültigen Zulassung im Handel）
    n = _val(subj.group(1))
    left = out[:subj.start()]
    mv = re.search(r"\b(" + VERB_RE + r")\s+" + ADV + r"$", left, re.I)
    if mv:
        return out[:mv.start(1)] + _flip(mv.group(1), n) + out[mv.end(1):]
    tail = out[subj.end():]
    mm = re.match(NP_TAIL + r"\s+(" + VERB_RE + r")\b", tail, re.I)
    if mm:
        a = subj.end() + mm.start(1)
        return out[:a] + _flip(mm.group(1), n) + out[a + len(mm.group(1)):]
    if re.search(r"\b" + VERB_RE + r"\b", re.split(r"[;,(]", tail)[0], re.I):
        return None  # 子句裡有動詞但對不上句型
    return out


def _line(ln, f, protect, skipped):
    if ln.startswith(("|", "#", "{:")) or not ln.strip():
        return ln
    parts = SENT_SPLIT.split(ln)
    seps = SENT_SPLIT.findall(ln)
    new, held = [], False
    for s in parts:
        if any(p and (p in s or s in p) for p in protect):
            new.append(s)
            continue
        ns, why = rewrite_sentence(s, f)
        if why:
            skipped.append((why, s.strip()))
            held = True
        new.append(ns)
    if held:  # 同一行有句子判斷不了：整行不動
        return ln
    out = new[0]
    for sep, s in zip(seps, new[1:]):
        out += sep + s
    return out


def rewrite(text, facts, protect=()):
    """text：整頁 markdown。facts：快照的 facts。回傳 (新內容, skipped)。front matter、查核框、程式區塊、表格不動。"""
    skipped = []
    if not facts or facts.get("partial") or not facts.get("total"):
        return text, skipped
    protect = [p.strip() for p in protect if p and len(p.strip()) >= 6]
    fm_end = 0
    if text.startswith("---"):
        j = text.find("\n---", 3)
        fm_end = j + 4 if j > 0 else 0
    body = text[fm_end:]
    keep = []

    def hold(m):
        keep.append(m.group(0))
        return f"\x00{len(keep) - 1}\x00"
    body = BLOCK.sub(hold, body)
    lines = [ln if "\x00" in ln else _line(ln, facts, protect, skipped) for ln in body.split("\n")]
    body = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], "\n".join(lines))
    return text[:fm_end] + body, skipped
