/**
 * CHTxGNN Drug-Drug Interaction Checker
 *
 * Client-side DDI checking with 15 built-in curated rules (DDInter consulted as a reference; not a full database lookup).
 * Provides real-time interaction alerts for drug repurposing candidates.
 *
 * @author CHTxGNN Team
 * @version 1.0.0
 */
(function(global) {
  'use strict';

  const CONFIG = {
    // This site does not publish /data/ddi-index.json; only the curated rules
    // below are used. Set a URL here once such a file exists.
    ddiDataUrl: null,
    maxAlerts: 10
  };

  // Severity levels with priority (higher = more severe)
  const SEVERITY = {
    'Major': { priority: 3, class: 'ddi-major', label: 'Schwer' },
    'Moderate': { priority: 2, class: 'ddi-moderate', label: 'Mittel' },
    'Minor': { priority: 1, class: 'ddi-minor', label: 'Gering' }
  };

  // 15 built-in high-priority DDI rules (hand-curated, DDInter consulted as a reference)
  // Format: { drug1: [synonym list], drug2: [synonym list], severity, summary, detail }
  const CURATED_DDI_RULES = [
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['ibuprofen', 'advil', 'motrin', 'brufen']
      ],
      severity: 'Major',
      summary: 'Warfarin + Ibuprofen: erhöhtes Blutungsrisiko',
      detail: 'NSAR hemmen die Thrombozytenfunktion und können die gerinnungshemmende Wirkung von Warfarin verstärken; das Risiko gastrointestinaler Blutungen steigt deutlich.',
      recommendation: 'Stattdessen Paracetamol verwenden oder zum Magenschutz einen PPI ergänzen.'
    },
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['aspirin', 'acetylsalicylic acid']
      ],
      severity: 'Major',
      summary: 'Warfarin + Acetylsalicylsäure: erhöhtes Blutungsrisiko',
      detail: 'Beide beeinflussen die Hämostase; die gemeinsame Anwendung erhöht das Blutungsrisiko stark.',
      recommendation: 'Ist die Kombination notwendig, niedrig dosierte Acetylsalicylsäure verwenden und die INR engmaschig kontrollieren.'
    },
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['naproxen', 'aleve', 'naprosyn']
      ],
      severity: 'Major',
      summary: 'Warfarin + Naproxen: erhöhtes Blutungsrisiko',
      detail: 'Naproxen zusammen mit Warfarin erhöht das Risiko gastrointestinaler und anderer Blutungen.',
      recommendation: 'Zur Schmerzlinderung stattdessen Paracetamol verwenden.'
    },
    {
      drugs: [
        ['metformin', 'glucophage'],
        ['iodixanol', 'visipaque', 'iopamidol', 'isovue', 'contrast']
      ],
      severity: 'Major',
      summary: 'Metformin + jodhaltige Kontrastmittel: Risiko einer Laktatazidose',
      detail: 'Kontrastmittel können eine akute Nierenschädigung verursachen, die zur Anreicherung von Metformin und zur Laktatazidose führt.',
      recommendation: 'Metformin 48 Stunden vor der Untersuchung absetzen und erst nach bestätigter normaler Nierenfunktion wieder beginnen.'
    },
    {
      drugs: [
        ['colchicine', 'colcrys'],
        ['clarithromycin', 'biaxin', 'klacid']
      ],
      severity: 'Major',
      summary: 'Colchicin + Clarithromycin: Toxizitätsrisiko',
      detail: 'Clarithromycin ist ein starker CYP3A4-Hemmer und erhöht die Colchicin-Blutspiegel stark.',
      recommendation: 'Kombination vermeiden oder die Colchicin-Dosis deutlich senken.'
    },
    {
      drugs: [
        ['colchicine', 'colcrys'],
        ['ritonavir', 'norvir', 'cobicistat', 'tybost']
      ],
      severity: 'Major',
      summary: 'Colchicin + HIV-Proteasehemmer: Risiko schwerer Toxizität',
      detail: 'HIV-Proteasehemmer erhöhen die Colchicin-Spiegel deutlich und können eine tödliche Toxizität verursachen.',
      recommendation: 'Bei Patienten mit eingeschränkter Nieren- oder Leberfunktion kontraindiziert.'
    },
    {
      drugs: [
        ['simvastatin', 'zocor'],
        ['amiodarone', 'cordarone']
      ],
      severity: 'Major',
      summary: 'Simvastatin + Amiodaron: Myopathierisiko',
      detail: 'Amiodaron erhöht die Simvastatin-Spiegel und damit das Risiko einer Rhabdomyolyse.',
      recommendation: 'Simvastatin nicht über 20 mg/Tag dosieren oder auf ein anderes Statin wechseln.'
    },
    {
      drugs: [
        ['fluoxetine', 'prozac', 'sertraline', 'zoloft', 'paroxetine', 'paxil'],
        ['tramadol', 'ultram']
      ],
      severity: 'Major',
      summary: 'SSRI + Tramadol: Risiko eines Serotoninsyndroms',
      detail: 'Beide steigern die serotonerge Aktivität; die gemeinsame Anwendung kann ein lebensbedrohliches Serotoninsyndrom auslösen.',
      recommendation: 'Engmaschig auf Symptome achten (Hyperthermie, Myoklonien, veränderter Bewusstseinszustand) und ein anderes Analgetikum erwägen.'
    },
    {
      drugs: [
        ['fluoxetine', 'prozac', 'sertraline', 'zoloft', 'paroxetine', 'paxil'],
        ['linezolid', 'zyvox']
      ],
      severity: 'Major',
      summary: 'SSRI + Linezolid: Risiko eines Serotoninsyndroms',
      detail: 'Linezolid ist ein MAO-Hemmer; die Kombination mit einem SSRI ist sehr gefährlich.',
      recommendation: 'Kombination vermeiden. Ist Linezolid erforderlich, den SSRI absetzen und eine angemessene Auswaschphase einhalten.'
    },
    {
      drugs: [
        ['amiodarone', 'cordarone'],
        ['moxifloxacin', 'avelox']
      ],
      severity: 'Major',
      summary: 'Amiodaron + Moxifloxacin: Risiko einer QT-Verlängerung',
      detail: 'Beide können das QT-Intervall verlängern; die gemeinsame Anwendung erhöht das Risiko von Torsade de pointes.',
      recommendation: 'Kombination vermeiden oder das EKG engmaschig überwachen.'
    },
    {
      drugs: [
        ['digoxin', 'lanoxin'],
        ['amiodarone', 'cordarone']
      ],
      severity: 'Major',
      summary: 'Digoxin + Amiodaron: Risiko einer Digoxin-Toxizität',
      detail: 'Amiodaron erhöht die Digoxin-Blutspiegel um etwa 70%.',
      recommendation: 'Bei Beginn mit Amiodaron die Digoxin-Dosis halbieren und die Blutspiegel kontrollieren.'
    },
    {
      drugs: [
        ['clopidogrel', 'plavix'],
        ['omeprazole', 'prilosec', 'esomeprazole', 'nexium']
      ],
      severity: 'Moderate',
      summary: 'Clopidogrel + PPI: verminderte Thrombozytenhemmung',
      detail: 'Omeprazol hemmt CYP2C19 und vermindert die Umwandlung von Clopidogrel in seinen aktiven Metaboliten.',
      recommendation: 'Stattdessen Pantoprazol oder einen H2-Blocker erwägen.'
    },
    {
      drugs: [
        ['lithium', 'lithobid'],
        ['ibuprofen', 'advil', 'naproxen', 'aleve', 'diclofenac']
      ],
      severity: 'Major',
      summary: 'Lithium + NSAR: Risiko einer Lithiumtoxizität',
      detail: 'NSAR vermindern die renale Ausscheidung von Lithium und erhöhen dessen Blutspiegel.',
      recommendation: 'Kombination vermeiden oder die Lithiumspiegel engmaschig kontrollieren.'
    },
    {
      drugs: [
        ['potassium', 'k-dur', 'klor-con'],
        ['spironolactone', 'aldactone', 'eplerenone', 'inspra']
      ],
      severity: 'Major',
      summary: 'Kaliumpräparate + kaliumsparende Diuretika: Risiko einer Hyperkaliämie',
      detail: 'Beide erhöhen das Serumkalium; die gemeinsame Anwendung kann eine lebensbedrohliche Hyperkaliämie verursachen.',
      recommendation: 'Serumkalium regelmäßig kontrollieren und keine zusätzlichen Kaliumpräparate geben.'
    },
    {
      drugs: [
        ['methotrexate', 'trexall'],
        ['trimethoprim', 'bactrim', 'septra', 'sulfamethoxazole']
      ],
      severity: 'Major',
      summary: 'Methotrexat + Cotrimoxazol: Risiko einer Knochenmarksuppression',
      detail: 'Beide hemmen den Folatstoffwechsel; die gemeinsame Anwendung erhöht das Risiko von Knochenmarksuppression und Mukositis.',
      recommendation: 'Kombination vermeiden oder für ausreichende Folsäuresubstitution sorgen und das Blutbild engmaschig kontrollieren.'
    }
  ];

  let ddiIndex = null;
  let isLoaded = false;

  /**
   * Load DDI index data
   */
  async function loadDDIIndex() {
    if (isLoaded) return;
    if (!CONFIG.ddiDataUrl) {
      isLoaded = true;
      return;
    }

    try {
      const response = await fetch(CONFIG.ddiDataUrl);
      if (response.ok) {
        ddiIndex = await response.json();
        isLoaded = true;
        console.log('DDI index loaded:', ddiIndex?.count || 0, 'interactions');
      }
    } catch (error) {
      console.warn('DDI index not available, using curated rules only');
      isLoaded = true;
    }
  }

  /**
   * Normalize drug name for comparison
   */
  function normalizeDrugName(name) {
    if (!name) return '';
    return name.toLowerCase()
      .replace(/\s+/g, ' ')
      .replace(/[^a-z0-9\s]/g, '')
      .trim();
  }

  /**
   * Check if a drug name matches any of the synonyms
   */
  function matchesDrug(drugName, synonyms) {
    const normalized = normalizeDrugName(drugName);
    return synonyms.some(syn => {
      const normalizedSyn = normalizeDrugName(syn);
      return normalized.includes(normalizedSyn) || normalizedSyn.includes(normalized);
    });
  }

  /**
   * Check for DDI between two drugs using curated rules
   */
  function checkCuratedDDI(drug1, drug2) {
    const alerts = [];

    for (const rule of CURATED_DDI_RULES) {
      const [drugGroup1, drugGroup2] = rule.drugs;

      // Check if drug1 matches group1 and drug2 matches group2, or vice versa
      if (
        (matchesDrug(drug1, drugGroup1) && matchesDrug(drug2, drugGroup2)) ||
        (matchesDrug(drug1, drugGroup2) && matchesDrug(drug2, drugGroup1))
      ) {
        alerts.push({
          drug1: drug1,
          drug2: drug2,
          severity: rule.severity,
          severityInfo: SEVERITY[rule.severity],
          summary: rule.summary,
          detail: rule.detail,
          recommendation: rule.recommendation,
          source: 'Integrierte DDI-Regeln von CHTxGNN (15 ausgewählte Regeln; keine vollständige DDInter-Abfrage)'
        });
      }
    }

    return alerts;
  }

  /**
   * Check DDI for a list of medications
   * @param {string[]} medications - Array of medication names
   * @returns {Object[]} Array of DDI alerts
   */
  function checkInteractions(medications) {
    if (!medications || medications.length < 2) {
      return [];
    }

    const allAlerts = [];
    const seen = new Set();

    // Check all pairs
    for (let i = 0; i < medications.length; i++) {
      for (let j = i + 1; j < medications.length; j++) {
        const drug1 = medications[i];
        const drug2 = medications[j];
        const pairKey = [drug1, drug2].sort().join('|');

        if (seen.has(pairKey)) continue;
        seen.add(pairKey);

        const alerts = checkCuratedDDI(drug1, drug2);
        allAlerts.push(...alerts);
      }
    }

    // Sort by severity (highest first) and limit
    return allAlerts
      .sort((a, b) => b.severityInfo.priority - a.severityInfo.priority)
      .slice(0, CONFIG.maxAlerts);
  }

  /**
   * Check if a new drug has interactions with existing medications
   * @param {string} newDrug - The new drug to check
   * @param {string[]} currentMeds - Array of current medication names
   * @returns {Object[]} Array of DDI alerts
   */
  function checkNewDrug(newDrug, currentMeds) {
    if (!newDrug || !currentMeds || currentMeds.length === 0) {
      return [];
    }

    const allAlerts = [];

    for (const currentDrug of currentMeds) {
      const alerts = checkCuratedDDI(newDrug, currentDrug);
      allAlerts.push(...alerts);
    }

    return allAlerts
      .sort((a, b) => b.severityInfo.priority - a.severityInfo.priority);
  }

  /**
   * Format alerts as HTML for display
   */
  function formatAlertsHTML(alerts) {
    if (!alerts || alerts.length === 0) {
      return '<div class="ddi-no-alerts">Keine Hinweise auf Wechselwirkungen gefunden</div>';
    }

    let html = '<div class="ddi-alerts">';

    alerts.forEach((alert, index) => {
      html += `
        <div class="ddi-alert ${alert.severityInfo.class}">
          <div class="ddi-alert-header">
            <span class="ddi-severity-badge">${alert.severityInfo.label}</span>
            <span class="ddi-summary">${escapeHtml(alert.summary)}</span>
          </div>
          <div class="ddi-alert-body">
            <p class="ddi-detail">${escapeHtml(alert.detail)}</p>
            <p class="ddi-recommendation"><strong>Empfehlung:</strong> ${escapeHtml(alert.recommendation)}</p>
          </div>
          <div class="ddi-alert-footer">
            <span class="ddi-source">Quelle: ${escapeHtml(alert.source)}</span>
          </div>
        </div>
      `;
    });

    html += '</div>';
    return html;
  }

  /**
   * Format alerts for CDS Hooks response
   */
  function formatForCDSHooks(alerts) {
    return alerts.map((alert, index) => ({
      uuid: `ddi-alert-${index}`,
      summary: alert.summary,
      indicator: alert.severity === 'Major' ? 'critical' : alert.severity === 'Moderate' ? 'warning' : 'info',
      detail: `${alert.detail}\n\nEmpfehlung: ${alert.recommendation}`,
      source: {
        label: 'CHTxGNN DDI Checker',
        url: 'https://chtxgnn.yao.care/'
      }
    }));
  }

  function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Export
  global.TwTxGNN = global.TwTxGNN || {};
  global.TwTxGNN.DDIChecker = {
    load: loadDDIIndex,
    checkInteractions: checkInteractions,
    checkNewDrug: checkNewDrug,
    formatAlertsHTML: formatAlertsHTML,
    formatForCDSHooks: formatForCDSHooks,
    SEVERITY: SEVERITY
  };

  // Auto-load when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadDDIIndex);
  } else {
    loadDDIIndex();
  }

})(typeof window !== 'undefined' ? window : this);
