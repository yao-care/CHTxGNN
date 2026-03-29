"""疾病映射模組 - 葡萄牙語適應症/治療類別映射至 TxGNN 疾病本體"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd


# 葡萄牙語-英語疾病/症狀對照表
DISEASE_DICT = {
    # === Herz-Kreislauf-System (Cardiovascular) ===
    "bluthochdruck": "hypertension",
    "hypertonie": "hypertension",
    "arterielle hypertonie": "hypertension",
    "niedriger blutdruck": "hypotension",
    "herzinfarkt": "myocardial infarction",
    "myokardinfarkt": "myocardial infarction",
    "angina pectoris": "angina",
    "herzrhythmusstörung": "arrhythmia",
    "vorhofflimmern": "atrial fibrillation",
    "herzinsuffizienz": "heart failure",
    "herzschwäche": "heart failure",
    "koronare herzkrankheit": "coronary artery disease",
    "khk": "coronary artery disease",
    "tiefe venenthrombose": "deep vein thrombosis",
    "lungenembolie": "pulmonary embolism",
    "hypercholesterinämie": "hypercholesterolemia",
    "fettstoffwechselstörung": "dyslipidemia",
    "arteriosklerose": "atherosclerosis",
    "endokarditis": "endocarditis",
    "myokarditis": "myocarditis",
    "perikarditis": "pericarditis",

    # === Atemwegssystem (Respiratory) ===
    "chronisch obstruktive lungenerkrankung": "chronic obstructive pulmonary disease",
    "copd": "chronic obstructive pulmonary disease",
    "asthma": "asthma",
    "asthma bronchiale": "asthma",
    "lungenentzündung": "pneumonia",
    "pneumonie": "pneumonia",
    "bronchitis": "bronchitis",
    "grippe": "influenza",
    "influenza": "influenza",
    "tuberkulose": "tuberculosis",
    "mukoviszidose": "cystic fibrosis",
    "schlafapnoe": "obstructive sleep apnea",
    "atemnot": "dyspnea",
    "lungenemphysem": "emphysema",
    "sinusitis": "sinusitis",
    "allergischer schnupfen": "allergic rhinitis",

    # === Verdauungssystem (Gastrointestinal) ===
    "gastroösophageale refluxkrankheit": "gastroesophageal reflux disease",
    "sodbrennen": "gastroesophageal reflux disease",
    "magengeschwür": "gastric ulcer",
    "zwölffingerdarmgeschwür": "duodenal ulcer",
    "gastritis": "gastritis",
    "magenschleimhautentzündung": "gastritis",
    "reizdarmsyndrom": "irritable bowel syndrome",
    "chronisch-entzündliche darmerkrankung": "inflammatory bowel disease",
    "morbus crohn": "crohn disease",
    "colitis ulcerosa": "ulcerative colitis",
    "verstopfung": "constipation",
    "durchfall": "diarrhea",
    "übelkeit": "nausea",
    "erbrechen": "vomiting",
    "fettleber": "hepatic steatosis",
    "leberzirrhose": "liver cirrhosis",
    "hepatitis": "hepatitis",
    "hepatitis b": "hepatitis b",
    "hepatitis c": "hepatitis c",
    "bauchspeicheldrüsenentzündung": "pancreatitis",
    "gallensteine": "cholelithiasis",

    # === Nervensystem (Neurological) ===
    "alzheimer-krankheit": "alzheimer disease",
    "alzheimer": "alzheimer disease",
    "parkinson-krankheit": "parkinson disease",
    "parkinson": "parkinson disease",
    "epilepsie": "epilepsy",
    "multiple sklerose": "multiple sclerosis",
    "migräne": "migraine",
    "kopfschmerzen": "headache",
    "schlaganfall": "stroke",
    "hirninfarkt": "stroke",
    "neuropathie": "neuropathy",
    "periphere neuropathie": "peripheral neuropathy",
    "trigeminusneuralgie": "trigeminal neuralgia",
    "hirnhautentzündung": "meningitis",
    "enzephalitis": "encephalitis",

    # === Psychische Erkrankungen (Psychiatric) ===
    "depression": "depression",
    "schwere depression": "major depressive disorder",
    "angststörung": "anxiety disorder",
    "generalisierte angststörung": "generalized anxiety disorder",
    "bipolare störung": "bipolar disorder",
    "schizophrenie": "schizophrenia",
    "zwangsstörung": "obsessive-compulsive disorder",
    "posttraumatische belastungsstörung": "post-traumatic stress disorder",
    "ptbs": "post-traumatic stress disorder",
    "schlaflosigkeit": "insomnia",
    "aufmerksamkeitsdefizit-hyperaktivitätsstörung": "attention deficit hyperactivity disorder",
    "adhs": "attention deficit hyperactivity disorder",

    # === Hormonsystem (Endocrine) ===
    "diabetes mellitus": "diabetes mellitus",
    "diabetes typ 1": "type 1 diabetes mellitus",
    "diabetes typ 2": "type 2 diabetes mellitus",
    "zuckerkrankheit": "diabetes mellitus",
    "schilddrüsenunterfunktion": "hypothyroidism",
    "schilddrüsenüberfunktion": "hyperthyroidism",
    "kropf": "goiter",
    "cushing-syndrom": "cushing syndrome",
    "morbus addison": "addison disease",
    "fettleibigkeit": "obesity",
    "adipositas": "obesity",
    "metabolisches syndrom": "metabolic syndrome",
    "gicht": "gout",
    "hyperurikämie": "hyperuricemia",

    # === Muskel-Skelett-System (Musculoskeletal) ===
    "arthritis": "arthritis",
    "rheumatoide arthritis": "rheumatoid arthritis",
    "arthrose": "osteoarthritis",
    "osteoporose": "osteoporosis",
    "systemischer lupus erythematodes": "systemic lupus erythematosus",
    "lupus": "systemic lupus erythematosus",
    "fibromyalgie": "fibromyalgia",
    "morbus bechterew": "ankylosing spondylitis",
    "sehnenentzündung": "tendinitis",
    "rückenschmerzen": "low back pain",
    "lumbago": "low back pain",

    # === Hautkrankheiten (Dermatological) ===
    "schuppenflechte": "psoriasis",
    "psoriasis": "psoriasis",
    "ekzem": "eczema",
    "neurodermitis": "atopic dermatitis",
    "nesselsucht": "urticaria",
    "akne": "acne",
    "rosazea": "rosacea",
    "weißfleckenkrankheit": "vitiligo",
    "haarausfall": "alopecia",
    "gürtelrose": "herpes zoster",
    "lippenherpes": "herpes simplex",
    "pilzinfektion": "fungal infection",

    # === Harnwegssystem (Urological) ===
    "harnwegsinfektion": "urinary tract infection",
    "blasenentzündung": "cystitis",
    "nierenentzündung": "nephritis",
    "nierenversagen": "renal failure",
    "chronische nierenerkrankung": "chronic kidney disease",
    "nierensteine": "nephrolithiasis",
    "gutartige prostatavergrößerung": "benign prostatic hyperplasia",
    "harninkontinenz": "urinary incontinence",

    # === Augenheilkunde (Ophthalmological) ===
    "grüner star": "glaucoma",
    "glaukom": "glaucoma",
    "grauer star": "cataract",
    "katarakt": "cataract",
    "makuladegeneration": "macular degeneration",
    "bindehautentzündung": "conjunctivitis",
    "diabetische retinopathie": "diabetic retinopathy",
    "trockene augen": "dry eye syndrome",

    # === HNO (ENT) ===
    "mittelohrentzündung": "otitis media",
    "rachenentzündung": "pharyngitis",
    "mandelentzündung": "tonsillitis",
    "kehlkopfentzündung": "laryngitis",
    "schwindel": "vertigo",

    # === Infektionskrankheiten (Infectious) ===
    "hiv-infektion": "hiv infection",
    "aids": "acquired immunodeficiency syndrome",
    "malaria": "malaria",
    "covid-19": "covid-19",
    "coronavirus": "covid-19",
    "blutvergiftung": "sepsis",
    "sepsis": "sepsis",
    "pilzerkrankung": "fungal infection",
    "toxoplasmose": "toxoplasmosis",

    # === Allergien (Allergic) ===
    "allergie": "allergy",
    "anaphylaxie": "anaphylaxis",
    "allergisches asthma": "allergic asthma",
    "heuschnupfen": "allergic rhinitis",
    "kontaktdermatitis": "contact dermatitis",
    "nahrungsmittelallergie": "food allergy",

    # === Frauenheilkunde (Gynecological) ===
    "endometriose": "endometriosis",
    "polyzystisches ovarialsyndrom": "polycystic ovary syndrome",
    "wechseljahre": "menopause",
    "menstruationsschmerzen": "dysmenorrhea",
    "ausbleiben der regel": "amenorrhea",
    "scheidenentzündung": "vaginitis",
    "gebärmuttermyom": "uterine fibroid",
    "präeklampsie": "preeclampsia",

    # === Krebs (Oncological) ===
    "krebs": "cancer",
    "brustkrebs": "breast cancer",
    "lungenkrebs": "lung cancer",
    "darmkrebs": "colorectal cancer",
    "prostatakrebs": "prostate cancer",
    "leberkrebs": "liver cancer",
    "magenkrebs": "stomach cancer",
    "bauchspeicheldrüsenkrebs": "pancreatic cancer",
    "leukämie": "leukemia",
    "lymphom": "lymphoma",
    "melanom": "melanoma",
    "nierenkrebs": "kidney cancer",
    "blasenkrebs": "bladder cancer",
    "schilddrüsenkrebs": "thyroid cancer",

    # === Allgemeine Symptome (General) ===
    "fieber": "fever",
    "schmerzen": "pain",
    "chronische schmerzen": "chronic pain",
    "entzündung": "inflammation",
    "ödem": "edema",
    "müdigkeit": "fatigue",
    "blutarmut": "anemia",
    "anämie": "anemia",
}


def load_disease_vocab(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 TxGNN 疾病詞彙表"""
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "disease_vocab.csv"
    return pd.read_csv(filepath)


def build_disease_index(disease_df: pd.DataFrame) -> Dict[str, Tuple[str, str]]:
    """建立疾病名稱索引（關鍵詞 -> (disease_id, disease_name)）"""
    index = {}

    for _, row in disease_df.iterrows():
        disease_id = row["disease_id"]
        disease_name = row["disease_name"]
        name_upper = row["disease_name_upper"]

        # 完整名稱
        index[name_upper] = (disease_id, disease_name)

        # 提取關鍵詞（按空格和逗號分割）
        keywords = re.split(r"[,\s\-]+", name_upper)
        for kw in keywords:
            kw = kw.strip()
            if len(kw) > 3 and kw not in index:  # 只保留較長的關鍵詞
                index[kw] = (disease_id, disease_name)

    return index


def extract_indications(indication_str: str) -> List[str]:
    """從適應症/治療類別文字提取個別適應症

    使用葡萄牙語常見分隔符分割
    """
    if not indication_str:
        return []

    # 正規化
    text = indication_str.strip().lower()

    # 使用分隔符分割
    parts = re.split(r"[.;]", text)

    indications = []
    for part in parts:
        # 再用逗號細分
        sub_parts = re.split(r"[,/]", part)
        for sub in sub_parts:
            sub = sub.strip()
            # 移除常見前綴
            sub = re.sub(r"^(para |tratamento de |indicado para |usado para )", "", sub)
            # 移除常見後綴
            sub = re.sub(r"( e outros| etc\.?)$", "", sub)
            sub = sub.strip()
            if sub and len(sub) >= 2:
                indications.append(sub)

    return indications


def translate_indication(indication: str) -> List[str]:
    """將葡萄牙語適應症翻譯為英文關鍵詞"""
    keywords = []
    indication_lower = indication.lower()

    for pt, en in DISEASE_DICT.items():
        if pt in indication_lower:
            keywords.append(en.upper())

    return keywords


def map_indication_to_disease(
    indication: str,
    disease_index: Dict[str, Tuple[str, str]],
) -> List[Tuple[str, str, float]]:
    """將單一適應症映射到 TxGNN 疾病

    Returns:
        [(disease_id, disease_name, confidence), ...]
    """
    results = []

    # 翻譯為英文關鍵詞
    keywords = translate_indication(indication)

    for kw in keywords:
        # 完全匹配
        if kw in disease_index:
            disease_id, disease_name = disease_index[kw]
            results.append((disease_id, disease_name, 1.0))
            continue

        # 部分匹配
        for index_kw, (disease_id, disease_name) in disease_index.items():
            if kw in index_kw or index_kw in kw:
                results.append((disease_id, disease_name, 0.8))

    # 去重並按信心度排序
    seen = set()
    unique_results = []
    for disease_id, disease_name, conf in sorted(results, key=lambda x: -x[2]):
        if disease_id not in seen:
            seen.add(disease_id)
            unique_results.append((disease_id, disease_name, conf))

    return unique_results[:5]  # 最多返回 5 個匹配


def map_fda_indications_to_diseases(
    fda_df: pd.DataFrame,
    disease_df: Optional[pd.DataFrame] = None,
) -> pd.DataFrame:
    """將巴西 ANVISA 藥品治療類別映射到 TxGNN 疾病"""
    if disease_df is None:
        disease_df = load_disease_vocab()

    disease_index = build_disease_index(disease_df)

    results = []

    for _, row in fda_df.iterrows():
        # ANVISA 使用 CLASSE_TERAPEUTICA 而非適應症
        indication_str = row.get("CLASSE_TERAPEUTICA", "")
        if not indication_str:
            continue

        # 提取個別適應症
        indications = extract_indications(indication_str)

        for ind in indications:
            # 翻譯並映射
            matches = map_indication_to_disease(ind, disease_index)

            if matches:
                for disease_id, disease_name, confidence in matches:
                    results.append({
                        "NUMERO_REGISTRO_PRODUTO": row.get("NUMERO_REGISTRO_PRODUTO", ""),
                        "NOME_PRODUTO": row.get("NOME_PRODUTO", ""),
                        "CLASSE_TERAPEUTICA": indication_str[:100],
                        "extracted_indication": ind,
                        "disease_id": disease_id,
                        "disease_name": disease_name,
                        "confidence": confidence,
                    })
            else:
                results.append({
                    "NUMERO_REGISTRO_PRODUTO": row.get("NUMERO_REGISTRO_PRODUTO", ""),
                    "NOME_PRODUTO": row.get("NOME_PRODUTO", ""),
                    "CLASSE_TERAPEUTICA": indication_str[:100],
                    "extracted_indication": ind,
                    "disease_id": None,
                    "disease_name": None,
                    "confidence": 0,
                })

    return pd.DataFrame(results)


def get_indication_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """計算適應症映射統計"""
    total = len(mapping_df)
    mapped = mapping_df["disease_id"].notna().sum()
    unique_indications = mapping_df["extracted_indication"].nunique()
    unique_diseases = mapping_df[mapping_df["disease_id"].notna()]["disease_id"].nunique()

    return {
        "total_indications": total,
        "mapped_indications": int(mapped),
        "mapping_rate": mapped / total if total > 0 else 0,
        "unique_indications": unique_indications,
        "unique_diseases": unique_diseases,
    }
