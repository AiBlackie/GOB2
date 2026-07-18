# ============================================================================
# BARBADOS FINANCIAL ACCOUNTABILITY 2003-2026
# COMPLETE YEAR-BY-YEAR EDITION WITH STORY ARC & BOOK DOWNLOAD
# ============================================================================
#
# This dashboard provides a comprehensive year-by-year narrative of Barbados'
# financial accountability journey through 24 years of Auditor General's reports.
# Each year includes detailed context, key issues, special audits, and
# financial metrics with historical perspective.
#
# VERSION: 19.1 - CREDITS IN BOOK DOWNLOAD ONLY
# DATE: July 2026
#
# FEATURES:
# 1. Full story arc with 24 chapters
# 2. Year-at-a-Glance view with drill-down
# 3. Complete financial data (2003-2026)
# 4. Bajan proverbs with meanings
# 5. Special audits browser
# 6. Repeating issues tracker
# 7. 📥 Download complete book as HTML
# 8. 📊 Download financial data as CSV
# 9. Full appendices with credits (BOOK ONLY)
# 10. Barbados-themed design
# 11. Working navigation
# ============================================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
import io
import base64

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="Barbados Financial Accountability 2003-2026",
    page_icon="🇧🇧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS
# ============================================================================
st.markdown("""
<style>
.main-header {
    font-size: 2.4rem;
    font-weight: 700;
    margin-bottom: 0.2rem;
    color: #00267F;
    background: linear-gradient(90deg, #00267F 0%, #FFC726 50%, #00267F 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.05);
    letter-spacing: 0.5px;
    text-align: center;
    padding: 10px 0;
}
.main-subheader {
    text-align: center;
    font-size: 1.1rem;
    color: #666;
    margin-top: -5px;
    margin-bottom: 15px;
    font-style: italic;
    background: linear-gradient(90deg, #00267F 0%, #FFC726 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 500;
}
.year-header {
    font-size: 1.8rem;
    font-weight: 700;
    color: #00267F;
    margin-top: 0.2rem;
    margin-bottom: 0.3rem;
}
.sub-header {
    font-size: 1.3rem;
    color: #00267F;
    font-weight: 600;
    margin-top: 1rem;
    margin-bottom: 0.5rem;
    border-bottom: 3px solid #FFC726;
    padding-bottom: 0.3rem;
}
.section-header {
    font-size: 1.05rem;
    color: #00267F;
    font-weight: 600;
    margin-top: 0.8rem;
    margin-bottom: 0.3rem;
}
.financial-card {
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    padding: 1rem;
    margin-bottom: 0.8rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.04);
    border-left: 4px solid #00267F;
}
.metric-card {
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    padding: 0.8rem;
    text-align: center;
    box-shadow: 0 2px 4px rgba(0,0,0,0.04);
    height: 100%;
}
.metric-value {
    font-size: 1.8rem;
    font-weight: 700;
    color: #00267F;
}
.metric-label {
    font-size: 0.75rem;
    color: #888;
    margin-top: 0.1rem;
}
.proverb-card {
    background: linear-gradient(135deg, #00267F 0%, #1E40AF 100%);
    color: white;
    padding: 18px 22px;
    border-radius: 12px;
    margin: 10px 0;
    border-left: 6px solid #FFC726;
}
.proverb-text {
    font-size: 1.3rem;
    font-style: italic;
    color: #FFC726;
    font-weight: 600;
}
.proverb-meaning {
    color: #BFDBFE;
    font-size: 0.85rem;
    margin-top: 4px;
}
.issue-critical {
    background: #FEF2F2;
    padding: 10px 16px;
    border-radius: 8px;
    border-left: 4px solid #DC2626;
    margin: 6px 0;
    font-size: 0.92rem;
    border: 1px solid #FCA5A5;
}
.issue-warning {
    background: #FFFBEB;
    padding: 10px 16px;
    border-radius: 8px;
    border-left: 4px solid #F59E0B;
    margin: 6px 0;
    font-size: 0.92rem;
    border: 1px solid #FCD34D;
}
.issue-info {
    background: #F0F7FF;
    padding: 10px 16px;
    border-radius: 8px;
    border-left: 4px solid #3B82F6;
    margin: 6px 0;
    font-size: 0.92rem;
    border: 1px solid #93C5FD;
}
.opinion-badge {
    display: inline-block;
    padding: 4px 16px;
    border-radius: 20px;
    font-weight: 600;
    font-size: 1rem;
}
.opinion-clean { background: #D1FAE5; color: #065F46; }
.opinion-disclaimer { background: #FEF3C7; color: #92400E; }
.opinion-adverse { background: #FEE2E2; color: #991B1B; }
.opinion-pending { background: #EDE9FE; color: #5B21B6; }
.era-badge {
    display: inline-block;
    padding: 2px 12px;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 600;
}
.era-clean-badge { background: #D1FAE5; color: #065F46; }
.era-disclaimer-badge { background: #FEF3C7; color: #92400E; }
.era-adverse-badge { background: #FEE2E2; color: #991B1B; }
.era-pending-badge { background: #EDE9FE; color: #5B21B6; }
.download-section {
    background: #f0f7ff;
    padding: 15px 20px;
    border-radius: 10px;
    border: 1px solid #3B82F6;
    margin: 10px 0;
}
.chapter-card {
    background: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    padding: 15px 20px;
    margin-bottom: 12px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.04);
    transition: all 0.3s ease;
    cursor: pointer;
}
.chapter-card:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    transform: translateY(-2px);
}
.chapter-number {
    font-size: 0.8rem;
    color: #888;
    font-weight: 600;
}
.chapter-title {
    font-size: 1.2rem;
    font-weight: 700;
}
.chapter-tagline {
    font-size: 0.95rem;
    color: #666;
    font-style: italic;
}
.chapter-stats {
    font-size: 0.85rem;
    color: #666;
    margin-top: 4px;
}
.chapter-opinion-badge {
    display: inline-block;
    padding: 2px 10px;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 600;
}
.chapter-opinion-clean { background: #D1FAE5; color: #065F46; }
.chapter-opinion-disclaimer { background: #FEF3C7; color: #92400E; }
.chapter-opinion-adverse { background: #FEE2E2; color: #991B1B; }
.chapter-opinion-pending { background: #EDE9FE; color: #5B21B6; }
.act-header {
    padding: 15px 20px;
    border-radius: 10px;
    margin: 15px 0 10px 0;
    text-align: center;
}
.act-clean { background: #ECFDF5; border: 2px solid #10B981; }
.act-disclaimer { background: #FFFBEB; border: 2px solid #F59E0B; }
.act-adverse { background: #FEF2F2; border: 2px solid #DC2626; }
.act-pending { background: #EDE9FE; border: 2px solid #8B5CF6; }
.act-title { font-size: 1.4rem; font-weight: 700; }
.act-subtitle { font-size: 1rem; }
.act-count { font-size: 0.9rem; font-weight: 600; }
.barbados-flag-bar {
    height: 4px;
    background: linear-gradient(90deg, #00267F 0%, #FFC726 50%, #00267F 100%);
    margin: 5px 0 10px 0;
    border-radius: 2px;
}
.download-btn-custom {
    background: #00267F;
    color: white;
    padding: 12px 24px;
    border-radius: 8px;
    border: none;
    font-weight: 600;
    font-size: 1rem;
    cursor: pointer;
    width: 100%;
    transition: all 0.3s ease;
}
.download-btn-custom:hover {
    background: #1E40AF;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,38,127,0.3);
}
</style>
""", unsafe_allow_html=True)

# ============================================================================
# COMPLETE DATASET 2003-2026
# ============================================================================
FINANCIAL_DATA = {
    2003: {'revenue': 1.736, 'expenditure': 2.262, 'deficit': -0.096, 'debt': 3.976, 'opinion': 'Clean', 'debt_pct': 72.5},
    2004: {'revenue': 1.866, 'expenditure': 2.341, 'deficit': -0.190, 'debt': 4.212, 'opinion': 'Clean', 'debt_pct': 74.8},
    2005: {'revenue': 1.897, 'expenditure': 2.404, 'deficit': -0.070, 'debt': 4.472, 'opinion': 'Clean', 'debt_pct': 76.2},
    2006: {'revenue': 2.143, 'expenditure': 2.272, 'deficit': 0.185, 'debt': 4.750, 'opinion': 'Clean', 'debt_pct': 75.0},
    2007: {'revenue': 2.223, 'expenditure': 2.543, 'deficit': -0.047, 'debt': 5.000, 'opinion': 'Clean', 'debt_pct': 72.8},
    2008: {'revenue': 2.500, 'expenditure': 2.700, 'deficit': -0.197, 'debt': 5.762, 'opinion': 'Disclaimer', 'debt_pct': 82.0},
    2009: {'revenue': 2.650, 'expenditure': 3.052, 'deficit': -0.402, 'debt': 6.500, 'opinion': 'Disclaimer', 'debt_pct': 90.0},
    2010: {'revenue': 2.555, 'expenditure': 3.035, 'deficit': -0.480, 'debt': 7.000, 'opinion': 'Disclaimer', 'debt_pct': 95.0},
    2011: {'revenue': 2.433, 'expenditure': 3.116, 'deficit': -0.683, 'debt': 7.500, 'opinion': 'Disclaimer', 'debt_pct': 98.0},
    2012: {'revenue': 2.623, 'expenditure': 3.006, 'deficit': -0.383, 'debt': 8.630, 'opinion': 'Disclaimer', 'debt_pct': 105.0},
    2013: {'revenue': 2.449, 'expenditure': 3.275, 'deficit': -0.826, 'debt': 9.570, 'opinion': 'Disclaimer', 'debt_pct': 110.0},
    2014: {'revenue': 2.340, 'expenditure': 3.322, 'deficit': -0.983, 'debt': 10.769, 'opinion': 'Disclaimer', 'debt_pct': 115.0},
    2015: {'revenue': 2.446, 'expenditure': 3.144, 'deficit': -0.698, 'debt': 11.095, 'opinion': 'Disclaimer', 'debt_pct': 118.0},
    2016: {'revenue': 2.582, 'expenditure': 3.345, 'deficit': -0.763, 'debt': 12.368, 'opinion': 'Disclaimer', 'debt_pct': 120.0},
    2017: {'revenue': 2.850, 'expenditure': 3.241, 'deficit': -0.352, 'debt': 13.102, 'opinion': 'Disclaimer', 'debt_pct': 125.0},
    2018: {'revenue': 2.738, 'expenditure': 3.452, 'deficit': -0.714, 'debt': 13.209, 'opinion': 'Adverse', 'debt_pct': 127.0},
    2019: {'revenue': 3.233, 'expenditure': 3.586, 'deficit': -0.354, 'debt': 12.740, 'opinion': 'Adverse', 'debt_pct': 122.0},
    2020: {'revenue': 3.582, 'expenditure': 3.863, 'deficit': -0.281, 'debt': 13.985, 'opinion': 'Adverse', 'debt_pct': 130.0},
    2021: {'revenue': 2.770, 'expenditure': 3.375, 'deficit': -0.605, 'debt': 12.947, 'opinion': 'Adverse', 'debt_pct': 125.0},
    2022: {'revenue': 2.701, 'expenditure': 3.374, 'deficit': -0.673, 'debt': 13.288, 'opinion': 'Adverse', 'debt_pct': 127.0},
    2023: {'revenue': 3.209, 'expenditure': 3.294, 'deficit': -0.085, 'debt': 13.985, 'opinion': 'Adverse', 'debt_pct': 135.0},
    2024: {'revenue': 3.206, 'expenditure': 3.437, 'deficit': -0.231, 'debt': 14.960, 'opinion': 'Pending', 'debt_pct': 136.0},
    2025: {'revenue': 3.300, 'expenditure': 3.520, 'deficit': -0.220, 'debt': 15.100, 'opinion': 'Pending', 'debt_pct': 137.0},
    2026: {'revenue': 3.400, 'expenditure': 3.600, 'deficit': -0.200, 'debt': 15.200, 'opinion': 'Pending', 'debt_pct': 138.0},
}

# ============================================================================
# PROVERBS - From G. Addinton Forde's "De Mortar-Pestle" (1987)
# ============================================================================
PROVERBS = {
    2003: "De cat can look at de queen.",
    2004: "High wind know where ole house live.",
    2005: "When fowl 'bout, cockroach should mek demsolves scarce.",
    2006: "Every shut eye ain't sleep.",
    2007: "Ah lil more still to go.",
    2008: "All ah we is one people.",
    2009: "Bad mind is worse dan bad foot.",
    2010: "Before yuh buy, try.",
    2011: "Calm water no mean dere ain't crocodile.",
    2012: "Trouble don'-set up like rain.",
    2013: "De higher de monkey climb, de more he show he tail.",
    2014: "De longest journey starts with one step.",
    2015: "De more de hurry, de less de speed.",
    2016: "Every day de bucket go to well.",
    2017: "Foolish questions need no answer.",
    2018: "Gih Jack 'e jacket.",
    2019: "He who feels it knows it.",
    2020: "If yuh cyaan hear, yuh mus feel.",
    2021: "Look before yuh leap.",
    2022: "Mek hay while de sun shine.",
    2023: "When de bottom drop out, e hard to patch it.",
    2024: "Every mikkle mek a muckle.",
    2025: "One one cocoa full basket.",
    2026: "Tomorrow come, but not today."
}

PROVERB_MEANINGS = {
    2003: "Everyone has the right to see what's happening.",
    2004: "Those who are vulnerable are most affected by change.",
    2005: "When people in power are distracted, others should stay out of the way.",
    2006: "Things are not always as they appear.",
    2007: "There's still more work to be done.",
    2008: "In times of crisis, we must stand together.",
    2009: "Negative intentions are worse than physical limitations.",
    2010: "Always test before committing.",
    2011: "Appearances can be deceiving.",
    2012: "Trouble arrives gradually, not suddenly.",
    2013: "The higher one rises, the more visible their flaws become.",
    2014: "Every great achievement begins with a small step.",
    2015: "Rushing leads to mistakes.",
    2016: "Consistent effort is required for success.",
    2017: "Some questions are better left unasked.",
    2018: "Give credit where it's due, but hold people accountable.",
    2019: "Those who experience something truly understand it.",
    2020: "If you won't listen, you'll learn through experience.",
    2021: "Consider consequences before acting.",
    2022: "Take advantage of good opportunities.",
    2023: "When the foundation is broken, fixing it is extremely difficult.",
    2024: "Small things accumulate to make a large whole.",
    2025: "Steady progress leads to success.",
    2026: "The future holds promise, but focus on today."
}

# ============================================================================
# YEAR CONTEXT
# ============================================================================
YEAR_CONTEXT = {
    2003: "The beginning of the clean audit era. Barbados' financial management was functioning well with no major issues identified. The foundation was being built for the years ahead.",
    2004: "The second consecutive clean opinion. Financial management remained strong. The announcement of accrual accounting signaled a commitment to international standards.",
    2005: "The third clean opinion. However, warning signs emerged: the Glendairy Prison fire in March 2005 exposed severe underinsurance — the property was insured for less than $1M despite being valued at $43.2M. VAT refund delays reached $45M+ with $10M in interest owed. The arrears crisis ($442M) began to surface across Inland Revenue ($161M), Customs ($172M), and Land Tax ($105M).",
    2006: "The fourth clean opinion. However, serious issues emerged: the Sanitation Service Authority operated with as few as 25 of 57 compactor vehicles, causing widespread collection delays. Over $2M was reported stolen or missing from ministries, including $1M from the Psychiatric Hospital. The St. Leonard's Boys' School project — 9 years underway, over $15M spent — remained incomplete and CDB loan funds were lost.",
    2007: "The fifth and final clean opinion. This was the last year of unqualified audit opinions. The Newton Business Park PPP failure ($18.5M loss) foreshadowed challenges ahead.",
    2008: "The turning point. IPSAS adoption was incomplete, and the first Disclaimer Opinion was issued. SOE consolidation concerns emerged. Asset registers were found inadequate.",
    2009: "The disclaimer era continued. The NHC housing crisis deepened with 29,000 applicants but only 226 houses built. The Road Network PPP project faced cost overruns.",
    2010: "Serious issues emerged: the Embassy of Venezuela fraud ($52,433 misappropriated) and the BCSI governance failure ($4.1M in grants with minimal returns).",
    2011: "The performance audit era began. Invest Barbados spent $70M with unclear outcomes. The Vocational Training Board showed apprenticeship programme failures.",
    2012: "Major procurement irregularities at the Barbados Water Authority ($700M+). No public tendering for 90% of contracts. $2.75M paid for services not provided.",
    2013: "Two critical issues: $157M owed to land owners, and extensive squatting on Crown lands threatening Zone 1 water supply.",
    2014: "The tax receivables crisis deepened. $475M in VAT could not be verified. Bank reconciliations had not been done for years. IRD receivables of $244M unverified.",
    2015: "A quiet year but issues persisted: SOE consolidation still not done (8 years). Pension liability remained hidden from the balance sheet.",
    2016: "The NHC High Rise project showed cost overruns ($442K per unit). The first Adverse Opinion was approaching. The financial crisis was building.",
    2017: "The last pre-Adverse year. Debt reached $13.1B. The stage was set for the crisis that would follow.",
    2018: "THE BREAKING POINT. First Adverse Opinion issued. $9.15B+ in issues. SOE consolidation not done (15 years). Pension liabilities hidden (15 years).",
    2019: "Adverse Opinion continued. Cash overstatements identified ($115M). The BWA Smart Meter project showed $1.49B in contracts with 90% without public tender.",
    2020: "COVID-19 impacted audits. $1.8B in fixed assets excluded from balance sheet. $1.7B in land valuations unverified. Poverty Eradication Fund showed $24M disbursed without criteria.",
    2021: "Deficit peaked at $685M. 6th consecutive Adverse Opinion. The PRDS performance review system was still not fully implemented after 20 years.",
    2022: "Adverse Opinion continues. Tax receivables of $2.61B reported, but $120M in cumulative interest omitted. Income and Corporation taxes prior to 2013 excluded. Pension liabilities not included. SOE consolidation still not done.",
    2023: "THE CRISIS DEEPENS. $2.43B tax receivables could not be confirmed due to insufficient supporting documentation. $719M asset discrepancy between financial statements and subsidiary records. $115M cash overstatement. 6th consecutive Adverse Opinion.",
    2024: "IT audit reveals system failures at Licensing Authority ($8M spent, systems not operational after 4 years). Budget overruns on technology projects.",
    2025: "Consolidated financial statements still outstanding. Pension liability not disclosed. HOPE Inc's PV model still not operational after 4 years.",
    2026: "Constitutional reform recommendation for audit independence. SOE consolidation and asset verification remain priority focus areas."
}

# ============================================================================
# SPECIAL AUDITS
# ============================================================================
SPECIAL_AUDITS = {
    2003: {
        'audits': [
            {'title': "St. Leonard's School Refurbishment", 'summary': 'CDB loan funds lost due to non-compliance', 'details': 'Government disqualified from CDB loan disbursements due to failure to meet criteria. Commitment fees paid for loans that could not be accessed.', 'severity': 'High'},
            {'title': 'Magistrates Courts Cash Management', 'summary': 'Cash shortages and unauthorized write-offs', 'details': 'Multiple courts had cash shortages. Officers were aware of shortages for years but took no action.', 'severity': 'Medium'},
            {'title': 'Barbados Licensing Authority Review', 'summary': 'Weak controls in driving licence issuance', 'details': 'Inadequate record keeping, unreliable electronic data, and weak internal controls.', 'severity': 'Medium'}
        ],
        'issues': ['First major special audits conducted', 'New Public Accounts Committee Act passed', 'First Audit Office reorganization']
    },
    2004: {
        'audits': [
            {'title': 'Barbados Tourism Authority', 'summary': '$10M+ deficits, "Best of Barbados" cost overruns', 'details': 'Persistent deficits, unbudgeted expenditures, weak budgetary control.', 'severity': 'High'},
            {'title': 'Urban Development Commission', 'summary': 'Loan programme failures and poor governance', 'details': '82% of housing loans in arrears, unauthorized loans, weak internal controls.', 'severity': 'High'}
        ],
        'issues': ['Special audits of BTA and UDC', 'Accrual accounting announced']
    },
    2005: {
        'audits': [
            {'title': 'Glendairy Prison Fire', 'summary': 'Inadequate insurance — $43.2M property insured for under $1M', 'details': 'The Glendairy Prison fire in March 2005 caused extensive damage. The property was insured for less than $1M despite being valued at $43.2M by the Commissioner of Land Tax. Government lost the opportunity to recover several million dollars.', 'severity': 'Critical'},
            {'title': 'Arrears Crisis', 'summary': '$442M in arrears across Government', 'details': 'Inland Revenue ($161M), Customs ($172M), Land Tax ($105M) leading the arrears. VAT refund delays reached $45M+ with $10M in interest owed.', 'severity': 'Critical'}
        ],
        'issues': ['Glendairy Prison fire exposed underinsurance crisis', 'VAT refund delays ($45M+ outstanding)', 'Government lost millions in insurance recovery']
    },
    2006: {
        'audits': [
            {'title': 'Sanitation Service Authority', 'summary': 'Vehicle fleet crisis — only 25 of 57 compactor vehicles operational', 'details': 'The SSA operated with as few as 25 of 57 compactor vehicles. Workshop delays due to parts shortages. No preventative maintenance program in place. Widespread refuse collection delays.', 'severity': 'Critical'},
            {'title': 'St. Leonard\'s Boys\' School', 'summary': '9 years, $15M+ spent, project incomplete', 'details': 'Project started in 1996. Over $15M spent by March 2005. CDB loan funds lost due to non-compliance. Commitment fees paid. School still not completed after 9 years.', 'severity': 'High'}
        ],
        'issues': ['$2M+ reported stolen/missing from Ministries', '$1M stolen from Psychiatric Hospital', 'SSA vehicle fleet crisis']
    },
    2007: {
        'audits': [
            {'title': 'Newton Business Park PPP', 'summary': 'PPP failure, contractor terminated, $18.5M lost', 'details': 'Design-build contract terminated in March 2007. Full contract sum disbursed but project uncompleted.', 'severity': 'Critical'}
        ],
        'issues': ['PPP projects under scrutiny', 'Newton Business Park failure']
    },
    2008: {
        'audits': [
            {'title': 'First Disclaimer Opinion', 'summary': 'IPSAS adoption but incomplete implementation', 'details': 'First time Audit Office could not express an opinion on financial statements. Asset registers inadequate.', 'severity': 'Critical'}
        ],
        'issues': ['First Disclaimer Opinion issued', 'Accrual accounting transition challenges']
    },
    2009: {
        'audits': [
            {'title': 'National Housing Corporation', 'summary': 'Housing demand vs delivery gap', 'details': '29,000 applicants on waiting list. Only 226 houses built against target of 1,600.', 'severity': 'High'},
            {'title': 'Barbados Road Network Project', 'summary': 'PPP cost overruns and disputes', 'details': 'Project cost exceeded $117M, contractor disputes, incomplete designs.', 'severity': 'High'}
        ],
        'issues': ['NHC housing crisis', 'Road network PPP challenges']
    },
    2010: {
        'audits': [
            {'title': 'Embassy of Venezuela', 'summary': 'Misappropriation of funds by embassy official', 'details': 'US$52,433 transferred to personal accounts under guise of official travel. Officer removed from post.', 'severity': 'Critical'},
            {'title': 'Barbados Coalition of Service Industries', 'summary': 'Governance and performance measurement failures', 'details': '$4.1M in grants over 5 years with minimal returns. Trade missions yielded little business.', 'severity': 'High'}
        ],
        'issues': ['Embassy fraud exposed', 'BCSI value-for-money concerns']
    },
    2011: {
        'audits': [
            {'title': 'Invest Barbados Performance Review', 'summary': '$70M spent, outcomes unclear', 'details': 'Performance measures not linked to outcomes. Sales representatives paid without results.', 'severity': 'High'},
            {'title': 'Barbados Vocational Training Board', 'summary': 'Apprenticeship programme failures', 'details': 'Poor monitoring of apprentices, certification issues, project management failures.', 'severity': 'Medium'}
        ],
        'issues': ['Performance audit era begins', 'Focus on value-for-money']
    },
    2012: {
        'audits': [
            {'title': 'Barbados Water Authority (Special)', 'summary': '$700M+ procurement irregularities', 'details': 'No public tendering for 90% of contracts. Smart meter project issues. $2.75M payment for services not provided.', 'severity': 'Critical'}
        ],
        'issues': ['Special audit on BWA', 'Procurement transparency concerns']
    },
    2013: {
        'audits': [
            {'title': 'Land Acquisition Process', 'summary': '$157M outstanding compensation to land owners', 'details': 'Government owes estimated $157M to land owners. Land used without proper acquisition.', 'severity': 'Critical'},
            {'title': 'Illegal Occupation of Crown Lands', 'summary': 'Extensive squatting across Barbados', 'details': 'Hundreds of illegal structures on Crown lands. Zone 1 water supply at risk.', 'severity': 'High'}
        ],
        'issues': ['Land acquisition crisis', 'Squatting on Crown lands']
    },
    2014: {
        'audits': [
            {'title': 'VAT Division Review', 'summary': '$475M in unverified receivables', 'details': 'VAT receivables of $475M could not be verified. Refunds delayed, interest accruing.', 'severity': 'Critical'},
            {'title': 'Inland Revenue Department', 'summary': 'Receivables unverified for years', 'details': 'IRD receivables of $244M could not be verified. Bank reconciliations not done for years.', 'severity': 'Critical'}
        ],
        'issues': ['Tax receivables crisis deepens', 'Bank reconciliation failures']
    },
    2015: {
        'audits': [],
        'issues': ['SOE consolidation still not done (8 years)', 'Pension liability hidden']
    },
    2016: {
        'audits': [
            {'title': 'NHC High Rise Apartments', 'summary': 'Cost overruns, procurement failures', 'details': 'Construction cost $442K per unit, well above low-income range. Poor contractor performance.', 'severity': 'High'}
        ],
        'issues': ['First Adverse Opinion (2018 approaching)', 'Financial crisis building']
    },
    2017: {
        'audits': [],
        'issues': ['Pre-Adverse era ending', 'Debt reaches $13.1B']
    },
    2018: {
        'audits': [
            {'title': 'School Meals Centre', 'summary': '$23.12M spent, project incomplete after 6 years', 'details': 'Original $19.9M contract, $23.12M spent by 2018, project still incomplete. Contractor disputes.', 'severity': 'High'},
            {'title': 'Transport Board', 'summary': 'Bus availability declined from 163 to 50 buses', 'details': 'Average monthly bus availability from 163 (2015) to 50 (2019). Fleet in crisis.', 'severity': 'Critical'},
            {'title': 'Clearwater Bay', 'summary': '$124M loan guarantee written off', 'details': '$124M advanced to Clearwater Bay for Four Seasons project. Written off in 2018.', 'severity': 'Critical'}
        ],
        'issues': ['🔴 FIRST ADVERSE OPINION - 2003 to 2018', 'SOE consolidation not done (15 years)', 'Pension liabilities hidden (15 years)']
    },
    2019: {
        'audits': [
            {'title': 'BWA Smart Meter Project', 'summary': '$1.49B in contracts, 90% without public tender', 'details': 'Smart meter project issues, $5.5M payment for unexplained services.', 'severity': 'Critical'}
        ],
        'issues': ['Adverse Opinion continues', 'Cash overstatements identified']
    },
    2020: {
        'audits': [
            {'title': 'Poverty Eradication Fund', 'summary': '$24M disbursed without proper criteria', 'details': 'Fund established 20+ years ago with no clear objectives. Assistance provided without criteria.', 'severity': 'High'},
            {'title': 'Employment Recruitment Programs', 'summary': '$5.17M spent, limited results', 'details': 'No workers placed in USA for 6 years. Declining numbers in Canada.', 'severity': 'Medium'}
        ],
        'issues': ['COVID-19 impact on audits', '$1.8B fixed assets excluded from balance sheet']
    },
    2021: {
        'audits': [
            {'title': 'PRDS Special Audit', 'summary': 'Performance Review system partially implemented', 'details': 'PRDS introduced 2001, still not fully implemented. 45% of Ministries not fully using system.', 'severity': 'Medium'}
        ],
        'issues': ['6th consecutive Adverse Opinion', 'Deficit peaks ($685M)']
    },
    2022: {
        'audits': [
            {'title': 'Tax Receivables Review', 'summary': '$2.61B tax receivables, $120M interest omitted', 'details': 'Tax receivables of $2.61B did not include $120M in cumulative interest. Income and Corporation taxes prior to 2013 excluded. Bank reconciliations not done for 15+ years.', 'severity': 'Critical'},
            {'title': 'Other Capital Assets', 'summary': '$2.19B in assets, road infrastructure excluded', 'details': 'Other Capital Assets of $2.19B did not include Road Infrastructure and Heritage assets. Asset valuations incomplete.', 'severity': 'High'}
        ],
        'issues': ['Adverse Opinion continues', 'Tax receivables $2.61B unverified', 'Pension liabilities not included', 'SOE consolidation not done']
    },
    2023: {
        'audits': [
            {'title': 'Tax Receivables Unconfirmed', 'summary': '$2.43B tax receivables could not be confirmed', 'details': 'Tax Receivables of $2.43B could not be confirmed due to absence of sufficient supporting documentation. Bad Debt Expense of $68.28M also unconfirmed.', 'severity': 'Critical'},
            {'title': 'Asset Discrepancy', 'summary': '$719M difference in Other Capital Assets', 'details': 'Other Capital Assets showed $719M difference between financial statements and subsidiary records. Cash and Financial Investments overstated by $115M and $147M respectively.', 'severity': 'Critical'}
        ],
        'issues': ['🔴 CRISIS DEEPENS', '$2.43B tax receivables unconfirmed', '$719M asset discrepancy', '6th consecutive Adverse Opinion']
    },
    2024: {
        'audits': [
            {'title': 'Barbados Licensing Authority IT Systems', 'summary': '$8M spent, systems not fully operational after 4 years', 'details': 'EVR and VRS systems at various stages of development. None fully deployed by March 2024.', 'severity': 'High'}
        ],
        'issues': ['IT audit reveals system failures', 'Budget overruns on technology projects']
    },
    2025: {
        'audits': [
            {'title': 'HOPE Inc Update', 'summary': '110 houses completed, PV model still not operational', 'details': 'Four years after inception, photovoltaic revenue model not yet generating income.', 'severity': 'Medium'}
        ],
        'issues': ['Consolidated financial statements still outstanding', 'Pension liability not disclosed']
    },
    2026: {
        'audits': [
            {'title': 'Projected Focus Areas', 'summary': 'Continued focus on SOE consolidation and asset verification', 'details': 'Audit Office seeks constitutional reform for independence.', 'severity': 'Medium'}
        ],
        'issues': ['Constitutional reform recommendation', 'Need for audit independence']
    }
}

# ============================================================================
# CHAPTER TITLES - THE STORY ARC
# ============================================================================
CHAPTER_TITLES = {
    2003: {"title": "The Foundation", "tagline": "The beginning of the clean audit era."},
    2004: {"title": "Building Momentum", "tagline": "Second consecutive clean opinion."},
    2005: {"title": "Warning Signs", "tagline": "The Glendairy Prison fire exposes underinsurance."},
    2006: {"title": "First Cracks", "tagline": "Vehicle fleet crisis and missing funds."},
    2007: {"title": "The Last Clean Year", "tagline": "The final year of unqualified opinions."},
    2008: {"title": "The Turning Point", "tagline": "First Disclaimer Opinion issued."},
    2009: {"title": "The Housing Crisis", "tagline": "29,000 applicants, only 226 houses built."},
    2010: {"title": "The Embassy Scandal", "tagline": "Fraud and governance failures exposed."},
    2011: {"title": "Performance Audits Begin", "tagline": "Focus shifts to value-for-money."},
    2012: {"title": "The BWA Scandal", "tagline": "$700M+ procurement irregularities."},
    2013: {"title": "Land & Squatting Crisis", "tagline": "$157M owed to land owners."},
    2014: {"title": "Tax Crisis Deepens", "tagline": "$475M in VAT could not be verified."},
    2015: {"title": "The Quiet Year", "tagline": "Issues persist, but no new scandals."},
    2016: {"title": "The High Rise Disaster", "tagline": "$442K per unit, well above low-income range."},
    2017: {"title": "The Last Warning", "tagline": "Debt reaches $13.1B."},
    2018: {"title": "FIRST ADVERSE OPINION", "tagline": "The system broke. $9.15B+ in issues."},
    2019: {"title": "The Smart Meter Scandal", "tagline": "$1.49B in contracts, 90% without tender."},
    2020: {"title": "COVID & Missing Assets", "tagline": "$1.8B fixed assets excluded."},
    2021: {"title": "The Peak of Deficit", "tagline": "Deficit peaks at $685M."},
    2022: {"title": "The $2.61B Question", "tagline": "Tax receivables unverified. $120M interest omitted."},
    2023: {"title": "THE CRISIS DEEPENS", "tagline": "$2.43B tax receivables unconfirmed. 6th Adverse Opinion."},
    2024: {"title": "Technology Failures", "tagline": "$8M spent, systems not operational."},
    2025: {"title": "Still Waiting", "tagline": "Consolidated statements still outstanding."},
    2026: {"title": "Constitutional Reform", "tagline": "The path forward for audit independence."}
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================
def format_currency_billions(value):
    if value is None or pd.isna(value):
        return "N/A"
    if isinstance(value, str):
        return value
    return f"${value:.2f}B"

def get_opinion_color(opinion):
    if opinion == 'Clean':
        return '#10B981'
    elif opinion == 'Disclaimer':
        return '#F59E0B'
    elif opinion == 'Adverse':
        return '#DC2626'
    elif opinion == 'Pending':
        return '#8B5CF6'
    else:
        return '#6B7280'

def get_opinion_emoji(opinion):
    if opinion == 'Clean':
        return '✅'
    elif opinion == 'Disclaimer':
        return '⚠️'
    elif opinion == 'Adverse':
        return '❌'
    elif opinion == 'Pending':
        return '⏳'
    else:
        return 'ℹ️'

def get_opinion_class(opinion):
    if opinion == 'Clean':
        return 'opinion-clean'
    elif opinion == 'Disclaimer':
        return 'opinion-disclaimer'
    elif opinion == 'Adverse':
        return 'opinion-adverse'
    elif opinion == 'Pending':
        return 'opinion-pending'
    else:
        return ''

def get_era_badge(year):
    if year <= 2007:
        return '<span class="era-badge era-clean-badge">🟢 Clean Era</span>'
    elif year <= 2017:
        return '<span class="era-badge era-disclaimer-badge">🟡 Disclaimer Era</span>'
    elif year <= 2023:
        return '<span class="era-badge era-adverse-badge">🔴 Adverse Era</span>'
    else:
        return '<span class="era-badge era-pending-badge">🟣 Pending Era</span>'

def get_chapter_opinion_class(opinion):
    if opinion == 'Clean':
        return 'chapter-opinion-clean'
    elif opinion == 'Disclaimer':
        return 'chapter-opinion-disclaimer'
    elif opinion == 'Adverse':
        return 'chapter-opinion-adverse'
    elif opinion == 'Pending':
        return 'chapter-opinion-pending'
    else:
        return ''

def get_dataframe():
    """Convert FINANCIAL_DATA to pandas DataFrame for export."""
    rows = []
    for year, data in FINANCIAL_DATA.items():
        rows.append({
            'Year': year,
            'Revenue_Billions': data['revenue'],
            'Expenditure_Billions': data['expenditure'],
            'Deficit_Billions': data['deficit'],
            'Debt_Billions': data['debt'],
            'Debt_to_GDP_Pct': data['debt_pct'],
            'Audit_Opinion': data['opinion']
        })
    return pd.DataFrame(rows)

def get_revenue_breakdown(year):
    if year <= 2007:
        return {
            'Income Tax (PAYE & Corp)': 0.33,
            'VAT & Excise Taxes': 0.30,
            'Customs & Import Duties': 0.14,
            'Property & Land Taxes': 0.08,
            'Other Taxes & Levies': 0.06,
            'Non-Tax Revenue': 0.06,
            'Grants & Aid': 0.03
        }
    elif year <= 2012:
        return {
            'Income Tax (PAYE & Corp)': 0.29,
            'VAT & Excise Taxes': 0.33,
            'Customs & Import Duties': 0.13,
            'Property & Land Taxes': 0.07,
            'Other Taxes & Levies': 0.07,
            'Non-Tax Revenue': 0.07,
            'Grants & Aid': 0.04
        }
    elif year <= 2017:
        return {
            'Income Tax (PAYE & Corp)': 0.26,
            'VAT & Excise Taxes': 0.35,
            'Customs & Import Duties': 0.12,
            'Property & Land Taxes': 0.07,
            'Other Taxes & Levies': 0.08,
            'Non-Tax Revenue': 0.08,
            'Grants & Aid': 0.04
        }
    elif year <= 2020:
        return {
            'Income Tax (PAYE & Corp)': 0.24,
            'VAT & Excise Taxes': 0.32,
            'Customs & Import Duties': 0.10,
            'Property & Land Taxes': 0.07,
            'Other Taxes & Levies': 0.09,
            'Non-Tax Revenue': 0.10,
            'Grants & Aid': 0.08
        }
    else:
        return {
            'Income Tax (PAYE & Corp)': 0.27,
            'VAT & Excise Taxes': 0.34,
            'Customs & Import Duties': 0.12,
            'Property & Land Taxes': 0.07,
            'Other Taxes & Levies': 0.08,
            'Non-Tax Revenue': 0.08,
            'Grants & Aid': 0.04
        }

def get_expenditure_breakdown(year):
    if year <= 2007:
        return {
            'Payroll & Benefits': 0.30,
            'Goods & Services': 0.22,
            'Debt Service': 0.16,
            'Grants & Transfers': 0.14,
            'Capital Expenditure': 0.10,
            'Social Programs': 0.05,
            'Other Operating Costs': 0.03
        }
    elif year <= 2012:
        return {
            'Payroll & Benefits': 0.28,
            'Goods & Services': 0.20,
            'Debt Service': 0.19,
            'Grants & Transfers': 0.15,
            'Capital Expenditure': 0.08,
            'Social Programs': 0.07,
            'Other Operating Costs': 0.03
        }
    elif year <= 2017:
        return {
            'Payroll & Benefits': 0.27,
            'Goods & Services': 0.18,
            'Debt Service': 0.22,
            'Grants & Transfers': 0.16,
            'Capital Expenditure': 0.06,
            'Social Programs': 0.08,
            'Other Operating Costs': 0.03
        }
    elif year <= 2020:
        return {
            'Payroll & Benefits': 0.26,
            'Goods & Services': 0.16,
            'Debt Service': 0.24,
            'Grants & Transfers': 0.17,
            'Capital Expenditure': 0.05,
            'Social Programs': 0.09,
            'Other Operating Costs': 0.03
        }
    else:
        return {
            'Payroll & Benefits': 0.27,
            'Goods & Services': 0.18,
            'Debt Service': 0.22,
            'Grants & Transfers': 0.16,
            'Capital Expenditure': 0.06,
            'Social Programs': 0.08,
            'Other Operating Costs': 0.03
        }

# ============================================================================
# BOOK GENERATOR FUNCTION - WITH CREDITS ONLY IN BOOK
# ============================================================================
def generate_book_html():
    """Generate the complete book as an HTML string for download."""
    
    # Build the book content
    book_content = []
    
    # Cover
    book_content.append(f'''
    <div class="cover">
        <div style="font-size:2.5rem; letter-spacing:8px;">🇧🇧</div>
        <h1>HOW DID WE <span class="highlight">GET HERE</span>?</h1>
        <div class="flag-bar"></div>
        <div class="subtitle">Barbados' 20-Year Journey from Clean Opinions to Financial Crisis</div>
        <div class="byline">A Story of Accountability, Failure, and the Path Forward</div>
        <div class="years">2003 — 2026</div>
        <div style="margin-top:20px; font-size:0.9rem; color:#888;">
            Based on 24 Years of Auditor General's Reports
        </div>
    </div>
    ''')
    
    # Preface
    book_content.append('''
    <div style="margin:30px 0 40px;">
        <h2 style="color:#00267F; font-size:2rem; border-bottom:2px solid #FFC726; padding-bottom:6px;">Preface</h2>
        <p style="margin-top:12px; font-size:1.05rem;">
            Every Barbadian has a right to know the state of their country's finances.
        </p>
        <p style="margin-top:10px;">
            For 20 years, the Auditor General has been telling Parliament and the public the same story:
        </p>
        <ul style="margin:10px 0 10px 30px;">
            <li>Asset registers are deficient</li>
            <li>Bank reconciliations are not done</li>
            <li>State-Owned Enterprises are not consolidated</li>
            <li>Pension liabilities are hidden</li>
            <li>Tax receivables cannot be verified</li>
        </ul>
        <p style="margin-top:10px;">
            Year after year, report after report, the same findings. The same warnings. The same lack of action.
        </p>
        <p style="margin-top:10px; font-weight:600; color:#00267F;">
            <strong>How did we get here?</strong>
        </p>
        <p style="margin-top:6px;">
            This book is an attempt to answer that question.
        </p>
    </div>
    ''')
    
    # Introduction
    book_content.append('''
    <div style="margin:30px 0 40px;">
        <h2 style="color:#00267F; font-size:2rem; border-bottom:2px solid #FFC726; padding-bottom:6px;">Introduction</h2>
        <h3 style="color:#1a1a2e; font-size:1.4rem; margin-top:12px;">The Story of Barbados' Financial Accountability</h3>
        <p style="margin-top:10px;">
            In 2003, Barbados received a clean audit opinion.
        </p>
        <p>
            The country's finances were in order. The books balanced. The Auditor General had no major issues to report.
        </p>
        <p>
            By 2023, that had changed dramatically.
        </p>
        <table style="width:100%; border-collapse:collapse; margin:16px 0;">
            <thead><tr style="background:#00267F; color:white;"><th>Period</th><th>Opinion</th><th>Meaning</th></tr></thead>
            <tbody>
                <tr><td>2003-2007</td><td><span class="opinion-badge opinion-clean">✅ Clean</span></td><td>Everything was in order</td></tr>
                <tr><td>2008-2017</td><td><span class="opinion-badge opinion-disclaimer">⚠️ Disclaimer</span></td><td>The numbers couldn't be verified</td></tr>
                <tr><td>2018-2023</td><td><span class="opinion-badge opinion-adverse">❌ Adverse</span></td><td>The numbers were materially wrong</td></tr>
            </tbody>
        </table>
        <div style="margin-top:16px;">
            <p><strong>How did we go from clean opinions to adverse opinions?</strong></p>
            <p><strong>How did debt grow from $3.98B to $13.99B?</strong></p>
            <p><strong>How did the same issues persist for 20 years without being fixed?</strong></p>
        </div>
        <p style="margin-top:10px; font-style:italic; color:#555;">This book traces the journey.</p>
    </div>
    ''')
    
    # Generate chapters
    eras = [
        (2003, 2008, "PART I", "The Road to Clean Opinions", "2003 — 2007"),
        (2008, 2018, "PART II", "The Slow Decline", "2008 — 2017"),
        (2018, 2024, "PART III", "The Breaking Point", "2018 — 2023")
    ]
    
    for start, end, part, title, years in eras:
        book_content.append(f'<div class="part"><h2>{part}</h2><div class="sub">{title}</div><div style="font-size:1.2rem; margin-top:4px;">{years}</div></div>')
        
        for year in range(start, end):
            data = FINANCIAL_DATA[year]
            proverb = PROVERBS.get(year, "")
            meaning = PROVERB_MEANINGS.get(year, "")
            chapter = CHAPTER_TITLES.get(year, {"title": f"Year {year}", "tagline": ""})
            context = YEAR_CONTEXT.get(year, "")
            special = SPECIAL_AUDITS.get(year, {'audits': [], 'issues': []})
            
            opinion_color = "opinion-clean" if data['opinion'] == 'Clean' else "opinion-disclaimer" if data['opinion'] == 'Disclaimer' else "opinion-adverse"
            opinion_emoji = "✅" if data['opinion'] == 'Clean' else "⚠️" if data['opinion'] == 'Disclaimer' else "❌"
            deficit_class = "positive" if data['deficit'] >= 0 else "negative"
            deficit_sign = "+" if data['deficit'] >= 0 else ""
            
            book_content.append(f'''
            <div class="chapter">
                <div class="number">Chapter {year - 2002}</div>
                <h3>{chapter['title']}</h3>
                <div style="font-size:0.95rem; color:#666; margin-bottom:4px;">{year}</div>
                <div class="proverb">"{proverb}"</div>
                <div class="proverb-meaning">{meaning}</div>
                <div class="metric-grid">
                    <div class="metric-item"><div class="label">Revenue</div><div class="value">${data['revenue']:.3f}B</div></div>
                    <div class="metric-item"><div class="label">Expenditure</div><div class="value">${data['expenditure']:.3f}B</div></div>
                    <div class="metric-item"><div class="label">{"Surplus" if data['deficit'] >= 0 else "Deficit"}</div><div class="value {deficit_class}">{deficit_sign}{data['deficit']:.3f}B</div></div>
                    <div class="metric-item"><div class="label">Debt</div><div class="value">${data['debt']:.3f}B</div></div>
                    <div class="metric-item"><div class="label">Opinion</div><div><span class="opinion-badge {opinion_color}">{opinion_emoji} {data['opinion']}</span></div></div>
                </div>
                <p>{context}</p>
            </div>
            ''')
            
            if special.get('audits'):
                book_content.append('<div style="margin:8px 0;">')
                for audit in special['audits']:
                    severity_class = "issue-critical" if audit.get('severity') == 'Critical' else "issue-warning" if audit.get('severity') == 'High' else "issue-info"
                    icon = '🔴' if audit.get('severity') == 'Critical' else '🟠' if audit.get('severity') == 'High' else 'ℹ️'
                    book_content.append(f'''
                    <div class="{severity_class}">
                        <strong>{icon} {audit['title']}</strong><br>
                        {audit['summary']}
                    </div>
                    ''')
                book_content.append('</div>')
    
    # Era summaries
    book_content.append('''
    <div class="summary-box">
        <h4>The Pattern — From Clean to Adverse</h4>
        <table style="width:100%; color:white; border-collapse:collapse;">
            <thead><tr style="border-bottom:1px solid rgba(255,255,255,0.2);"><th>Metric</th><th>Clean Era (2003-07)</th><th>Disclaimer Era (2008-17)</th><th>Adverse Era (2018-23)</th></tr></thead>
            <tbody>
                <tr><td>Average Revenue</td><td>$1.97B</td><td>$2.55B</td><td>$3.04B</td></tr>
                <tr><td>Average Deficit</td><td>-$0.04B</td><td>-$0.57B</td><td>-$0.45B</td></tr>
                <tr><td>Average Debt</td><td>$4.48B</td><td>$9.37B</td><td>$13.36B</td></tr>
                <tr><td>Average Debt/GDP</td><td>74.3%</td><td>99.8%</td><td>127.7%</td></tr>
            </tbody>
        </table>
        <p style="margin-top:12px; color:#BFDBFE; font-style:italic;">Revenue grew. But debt grew faster. Deficits grew. But accountability did not.</p>
    </div>
    ''')
    
    # Repeating issues
    book_content.append('''
    <div style="margin:40px 0;">
        <h2 style="color:#00267F; font-size:1.8rem; border-bottom:2px solid #FFC726; padding-bottom:6px;">The Groundhog Day Pattern</h2>
        <table style="width:100%; border-collapse:collapse; margin:16px 0;">
            <thead><tr style="background:#00267F; color:white;"><th>Issue</th><th>First Flagged</th><th>Last Flagged</th><th>Years</th><th>Status</th></tr></thead>
            <tbody>
                <tr><td>SOE Consolidation not done</td><td>2008</td><td>2023</td><td>15 years</td><td style="color:#DC2626;">❌ Unresolved</td></tr>
                <tr><td>Asset Registers deficient</td><td>2003</td><td>2023</td><td>20 years</td><td style="color:#DC2626;">❌ Unresolved</td></tr>
                <tr><td>Bank Reconciliations not done</td><td>2004</td><td>2023</td><td>19 years</td><td style="color:#DC2626;">❌ Unresolved</td></tr>
                <tr><td>Pension Liability hidden</td><td>2008</td><td>2023</td><td>15 years</td><td style="color:#DC2626;">❌ Unresolved</td></tr>
                <tr><td>Tax Receivables unverified</td><td>2008</td><td>2023</td><td>15 years</td><td style="color:#DC2626;">❌ Unresolved</td></tr>
                <tr><td>Staff shortages at Audit Office</td><td>2006</td><td>2023</td><td>17 years</td><td style="color:#DC2626;">❌ Unresolved</td></tr>
            </tbody>
        </table>
        <p style="font-style:italic; color:#555; text-align:center;">The same issues, year after year. The same warnings, decade after decade.</p>
    </div>
    ''')
    
    # Cost of Inaction
    book_content.append('''
    <div style="margin:40px 0;">
        <h2 style="color:#00267F; font-size:1.8rem; border-bottom:2px solid #FFC726; padding-bottom:6px;">The Cost of Inaction</h2>
        <table style="width:100%; border-collapse:collapse; margin:16px 0;">
            <thead><tr style="background:#DC2626; color:white;"><th>Category</th><th>Amount</th></tr></thead>
            <tbody>
                <tr><td>Deficits accumulated (2003-2023)</td><td style="color:#DC2626;">-$9.86B</td></tr>
                <tr><td>Debt increase (2003-2023)</td><td style="color:#DC2626;">+$10.01B</td></tr>
                <tr><td>Unverified Tax Receivables</td><td style="color:#DC2626;">$2.43B</td></tr>
                <tr><td>Asset Discrepancy</td><td style="color:#F59E0B;">$719M</td></tr>
                <tr><td>Hidden Pension Liability</td><td style="color:#DC2626;">$4.3B+</td></tr>
                <tr><td>SOE Long-term Debt</td><td style="color:#DC2626;">$732.5M</td></tr>
                <tr><td style="font-weight:700;">TOTAL</td><td style="font-weight:700; color:#DC2626;">~$28.7B+</td></tr>
            </tbody>
        </table>
        <p style="font-weight:600; color:#DC2626; text-align:center;">~$28.7B+ in unverified, hidden, or questionable amounts.</p>
    </div>
    ''')
    
    # SOE Crisis Summary
    book_content.append('''
    <div style="margin:40px 0;">
        <h2 style="color:#00267F; font-size:1.8rem; border-bottom:2px solid #FFC726; padding-bottom:6px;">The State-Owned Enterprise Crisis</h2>
        <table style="width:100%; border-collapse:collapse; margin:16px 0;">
            <thead><tr style="background:#00267F; color:white;"><th>SOE</th><th>Status</th><th>Debt</th><th>Pension Liability</th><th>Arrears</th></tr></thead>
            <tbody>
                <tr><td><strong>GAIA</strong></td><td style="color:#DC2626;">Going concern warning</td><td>$140M</td><td>Unknown</td><td>Unknown</td></tr>
                <tr><td><strong>Transport Board</strong></td><td style="color:#DC2626;">Technically insolvent</td><td>Unknown</td><td>Unknown</td><td>Unknown</td></tr>
                <tr><td><strong>Barbados Water Authority</strong></td><td style="color:#F59E0B;">Cash flow issues</td><td>$70M</td><td>$130M</td><td>$14M+</td></tr>
                <tr><td><strong>HOPE Inc.</strong></td><td style="color:#DC2626;">Technically insolvent</td><td>$54M</td><td>Unknown</td><td>Unknown</td></tr>
            </tbody>
        </table>
        <p style="margin-top:12px;"><strong>Total SOE Long-term Debt: $732.5M</strong></p>
        <p><strong>Total SOE Unfunded Pension Liabilities: $282.7M</strong></p>
    </div>
    ''')
    
    # Conclusion
    book_content.append('''
    <div style="margin:50px 0 30px;">
        <h2 style="color:#00267F; font-size:2rem; border-bottom:3px solid #FFC726; padding-bottom:6px;">Conclusion</h2>
        <h3 style="color:#1a1a2e; font-size:1.4rem; margin-top:12px;">The Answer</h3>
        <p style="margin-top:10px;">
            <strong>How did we get here?</strong>
        </p>
        <p>
            We got here because the same issues were flagged year after year and nothing was done.
        </p>
        <p>
            We got here because there were no consequences for failure.
        </p>
        <p>
            We got here because accountability was replaced by acceptance.
        </p>
        <p>
            We got here because the Auditor General's warnings were ignored.
        </p>
        <p style="font-weight:600; color:#00267F; font-size:1.2rem; margin-top:16px;">
            The question is not "How did we get here?"
        </p>
        <p style="font-weight:600; color:#DC2626; font-size:1.2rem;">
            The question is: "What are we going to do about it?"
        </p>
    </div>
    ''')
    
    # Final Word
    book_content.append('''
    <div style="background:#00267F; color:white; padding:30px 30px; border-radius:8px; margin:30px 0;">
        <div style="text-align:center; font-size:2rem; margin-bottom:8px;">🇧🇧</div>
        <h3 style="color:#FFC726; text-align:center; font-size:1.6rem;">The Final Word</h3>
        <p style="margin-top:12px; color:#f0f0f0;">
            This book is not about blame. It is about accountability.
        </p>
        <p style="color:#f0f0f0;">
            The Auditor General has done his job. For 20 years, he has flagged the same issues. The government has acknowledged them but has not fixed them.
        </p>
        <p style="color:#f0f0f0;">
            Barbadians deserve to know the state of their country's finances. They deserve a clean audit opinion. They deserve accountability.
        </p>
        <p style="color:#FFC726; font-weight:600; font-size:1.2rem; text-align:center; margin-top:12px;">
            The question is: Will we get it?
        </p>
        <div style="text-align:center; margin-top:16px; font-style:italic; color:#BFDBFE;">
            "When de bottom drop out, e hard to patch it."
            <br>
            — Bajan Proverb, 2023
        </div>
    </div>
    ''')
    
    # ========================================================================
    # APPENDICES (BOOK ONLY - WITH CREDITS HERE)
    # ========================================================================
    book_content.append('''
    <div style="margin:50px 0 30px;">
        <h2 style="color:#00267F; font-size:2.2rem; border-bottom:3px solid #FFC726; padding-bottom:6px;">Appendices</h2>
    </div>
    ''')
    
    # Appendix A - Complete Financial Data
    book_content.append('''
    <div style="margin:30px 0;">
        <h3 style="color:#00267F; font-size:1.5rem;">Appendix A: Complete Financial Data (2003-2026)</h3>
        <table style="width:100%; border-collapse:collapse; margin:16px 0; font-size:0.8rem;">
            <thead><tr style="background:#00267F; color:white;"><th>Year</th><th>Revenue ($B)</th><th>Expenditure ($B)</th><th>Deficit ($B)</th><th>Debt ($B)</th><th>Debt/GDP</th><th>Opinion</th></tr></thead>
            <tbody>
    ''')
    
    for year in range(2003, 2027):
        data = FINANCIAL_DATA[year]
        opinion_emoji = "✅" if data['opinion'] == 'Clean' else "⚠️" if data['opinion'] == 'Disclaimer' else "❌" if data['opinion'] == 'Adverse' else "⏳"
        deficit_str = f"{data['deficit']:.3f}"
        if data['deficit'] >= 0:
            deficit_str = f"+{deficit_str}"
        book_content.append(f'''
                <tr><td>{year}</td><td>${data['revenue']:.3f}</td><td>${data['expenditure']:.3f}</td><td style="color:{'#10B981' if data['deficit'] >= 0 else '#DC2626'};">{deficit_str}</td><td>${data['debt']:.3f}</td><td>{data['debt_pct']:.1f}%</td><td>{opinion_emoji} {data['opinion']}</td></tr>
        ''')
    
    book_content.append('''
            </tbody>
        </table>
    </div>
    ''')
    
    # Appendix B - Repeating Issues
    book_content.append('''
    <div style="margin:30px 0;">
        <h3 style="color:#00267F; font-size:1.5rem;">Appendix B: Repeating Issues Tracker</h3>
        <table style="width:100%; border-collapse:collapse; margin:16px 0;">
            <thead><tr style="background:#00267F; color:white;"><th>Issue</th><th>First Flagged</th><th>Last Flagged</th><th>Years</th><th>Status</th></tr></thead>
            <tbody>
                <tr><td>SOE Consolidation not done</td><td>2008</td><td>2023</td><td>15 years</td><td style="color:#DC2626;">❌ Unresolved</td></tr>
                <tr><td>Asset Registers deficient</td><td>2003</td><td>2023</td><td>20 years</td><td style="color:#DC2626;">❌ Unresolved</td></tr>
                <tr><td>Bank Reconciliations not done</td><td>2004</td><td>2023</td><td>19 years</td><td style="color:#DC2626;">❌ Unresolved</td></tr>
                <tr><td>Pension Liability hidden</td><td>2008</td><td>2023</td><td>15 years</td><td style="color:#DC2626;">❌ Unresolved</td></tr>
                <tr><td>Tax Receivables unverified</td><td>2008</td><td>2023</td><td>15 years</td><td style="color:#DC2626;">❌ Unresolved</td></tr>
                <tr><td>Staff shortages at Audit Office</td><td>2006</td><td>2023</td><td>17 years</td><td style="color:#DC2626;">❌ Unresolved</td></tr>
            </tbody>
        </table>
    </div>
    ''')
    
    # Appendix C - SOE Crisis
    book_content.append('''
    <div style="margin:30px 0;">
        <h3 style="color:#00267F; font-size:1.5rem;">Appendix C: State-Owned Enterprise Crisis Summary</h3>
        <table style="width:100%; border-collapse:collapse; margin:16px 0;">
            <thead><tr style="background:#00267F; color:white;"><th>SOE</th><th>Status</th><th>Debt</th><th>Pension Liability</th><th>Arrears</th></tr></thead>
            <tbody>
                <tr><td><strong>GAIA</strong></td><td style="color:#DC2626;">Going concern warning</td><td>$140M</td><td>Unknown</td><td>Unknown</td></tr>
                <tr><td><strong>Transport Board</strong></td><td style="color:#DC2626;">Technically insolvent</td><td>Unknown</td><td>Unknown</td><td>Unknown</td></tr>
                <tr><td><strong>Barbados Water Authority</strong></td><td style="color:#F59E0B;">Cash flow issues</td><td>$70M</td><td>$130M</td><td>$14M+</td></tr>
                <tr><td><strong>HOPE Inc.</strong></td><td style="color:#DC2626;">Technically insolvent</td><td>$54M</td><td>Unknown</td><td>Unknown</td></tr>
            </tbody>
        </table>
        <p style="margin-top:12px;"><strong>Total SOE Long-term Debt: $732.5M</strong></p>
        <p><strong>Total SOE Unfunded Pension Liabilities: $282.7M</strong></p>
    </div>
    ''')
    
    # Appendix D - The Bajan Proverbs
    book_content.append('''
    <div style="margin:30px 0;">
        <h3 style="color:#00267F; font-size:1.5rem;">Appendix D: The Bajan Proverbs — Full Collection</h3>
        <p style="font-style:italic; color:#555; margin-top:8px;">
            This book's proverbs are drawn from <strong>"De Mortar-Pestle: A Collection of Barbadian Proverbs"</strong> by G. Addinton Forde (1987).
        </p>
        <table style="width:100%; border-collapse:collapse; margin:16px 0; font-size:0.85rem;">
            <thead><tr style="background:#00267F; color:white;"><th>Year</th><th>Proverb</th><th>Meaning</th></tr></thead>
            <tbody>
    ''')
    
    for year in range(2003, 2027):
        proverb = PROVERBS.get(year, "")
        meaning = PROVERB_MEANINGS.get(year, "")
        book_content.append(f'''
                <tr><td>{year}</td><td style="font-style:italic;">"{proverb}"</td><td>{meaning}</td></tr>
        ''')
    
    book_content.append('''
            </tbody>
        </table>
    </div>
    ''')
    
    # Appendix E - Sources & Credits (BOOK ONLY)
    book_content.append('''
    <div style="margin:30px 0;">
        <h3 style="color:#00267F; font-size:1.5rem;">Appendix E: Sources & Acknowledgments</h3>
        
        <div style="background:#f8f5f0; padding:20px 24px; border-radius:10px; border:2px solid #00267F; margin:20px 0;">
            <h4 style="color:#00267F; margin-bottom:8px;">Author & Compiler</h4>
            <p style="font-size:1.05rem; font-weight:700; color:#00267F;">Matthew A. A. Blackman</p>
            <p style="color:#333;">
                This book was researched, compiled, and written by Matthew A. A. Blackman. 
                The author spent countless hours analyzing 24 years of Auditor General's reports, 
                financial statements, and government documents to piece together the complete story 
                of Barbados' financial accountability journey.
            </p>
            <p style="color:#333; margin-top:8px;">
                The goal was to make this critical information accessible to every Barbadian — 
                not buried in government archives, but presented in a clear, compelling narrative 
                that tells the truth about where Barbados has been and where it needs to go.
            </p>
        </div>
        
        <div style="background:#f8f5f0; padding:20px 24px; border-radius:10px; border:2px solid #FFC726; margin:20px 0;">
            <h4 style="color:#00267F; margin-bottom:8px;">📖 The Proverbs — Credit to G. Addinton Forde</h4>
            <p style="color:#333;">
                The Bajan proverbs that open each chapter of this book are drawn from the definitive collection:
            </p>
            <p style="font-weight:700; color:#00267F; font-size:1.1rem; margin:8px 0;">
                "De Mortar-Pestle: A Collection of Barbadian Proverbs"<br>
                by G. Addinton Forde<br>
                Published 1987
            </p>
            <p style="color:#333;">
                G. Addinton Forde spent years collecting and documenting these proverbs, ensuring that 
                the wisdom of Barbados' elders would not be lost. His work preserves the wit, insight, 
                and cultural heritage of the Barbadian people. This book would be incomplete without 
                his contribution.
            </p>
            <p style="color:#555; font-style:italic; margin-top:8px;">
                <strong>From Forde's introduction:</strong><br>
                "These proverbs illustrate a profundity of thought, expressed in simple, clear and concise language, 
                with an extraordinary precision in the use of imagery. This is noteworthy, since the people who 
                coined them had little formal education."
            </p>
        </div>
        
        <div style="background:#f8f5f0; padding:20px 24px; border-radius:10px; border:2px solid #00267F; margin:20px 0;">
            <h4 style="color:#00267F; margin-bottom:8px;">🏛️ The Auditor General</h4>
            <p style="font-size:1.05rem; font-weight:700; color:#00267F;">Leigh E. Trotman, CPA</p>
            <p style="color:#333;">
                Auditor General of Barbados (2006-2026)
            </p>
            <p style="color:#333; margin-top:8px;">
                The Auditor General and his staff have produced the reports that form the foundation of this book. 
                For over two decades, they have done their duty — flagging the same issues, year after year, 
                warning Parliament and the public of the problems that have persisted.
            </p>
            <p style="color:#333; margin-top:8px;">
                This book is a testament to their work. The Auditor General has done his job. 
                Now it is time for the rest of the country to do theirs.
            </p>
        </div>
        
        <div style="background:#f8f5f0; padding:20px 24px; border-radius:10px; border:2px solid #8B5CF6; margin:20px 0;">
            <h4 style="color:#00267F; margin-bottom:8px;">🤖 AI-Assisted Compilation</h4>
            <p style="font-weight:700; color:#00267F;">DeepSeek (AI Assistant)</p>
            <p style="color:#333;">
                The compilation, organization, and formatting of this book were assisted by DeepSeek, 
                an artificial intelligence language model.
            </p>
            <p style="color:#555; font-size:0.9rem; margin-top:8px;">
                <strong>Disclaimer:</strong> While AI assisted in compilation and formatting, all data comes from 
                official government sources. The analysis, conclusions, and narrative are based on the actual 
                Auditor General's reports and financial statements.
            </p>
        </div>
        
        <div style="background:#f8f5f0; padding:20px 24px; border-radius:10px; border:2px solid #10B981; margin:20px 0;">
            <h4 style="color:#00267F; margin-bottom:8px;">🇧🇧 The People of Barbados</h4>
            <p style="color:#333;">
                This book is dedicated to the people of Barbados — who deserve to know the truth about their 
                country's finances, who have a right to accountability, and who have the power to demand change.
            </p>
        </div>
    </div>
    ''')
    
    # Primary Sources
    book_content.append('''
    <div style="margin:30px 0;">
        <h3 style="color:#00267F; font-size:1.5rem;">Primary Sources</h3>
        <ol style="margin-left:20px; line-height:1.8;">
            <li><strong>Auditor General's Reports (2003-2024)</strong> — Office of the Auditor General, Barbados. Laid before Parliament annually.</li>
            <li><strong>Financial Statements of the Government of Barbados</strong> — Prepared by the Accountant General. Audited by the Barbados Audit Office.</li>
            <li><strong>Fiscal Framework Documents (2026-2029)</strong> — Ministry of Finance, Economic Affairs and Investment. Laid before Parliament.</li>
            <li><strong>BERT Programme Documents</strong> — BERT 2018, BERT 2022, BERT 2026. Barbados Economic Recovery and Transformation Plan.</li>
            <li><strong>Estimates of Revenue and Expenditure (2026-2027)</strong> — Government of Barbados. Laid before Parliament.</li>
            <li><strong>GAIA Financial Statements (2024)</strong> — Grantley Adams International Airport Inc. Audited by Ernst &amp; Young Ltd.</li>
            <li><strong>Special Audits</strong> — Barbados Water Authority (2012), Transport Board (2019), HOPE Inc. (2025), and others.</li>
        </ol>
    </div>
    ''')
    
    # Footer with credits
    book_content.append('''
    <div class="footer">
        <div style="font-size:2rem; margin-bottom:8px;">🇧🇧</div>
        <p><strong>How Did We Get Here?</strong></p>
        <p>Barbados' 20-Year Journey from Clean Opinions to Financial Crisis</p>
        <p style="margin-top:8px;">Based on 24 Years of Auditor General's Reports (2003-2026)</p>
        <p style="margin-top:8px; font-size:0.8rem;">
            Author: Matthew A. A. Blackman &nbsp;|&nbsp; Proverbs: G. Addinton Forde &nbsp;|&nbsp; AI Assistance: DeepSeek
        </p>
        <p style="margin-top:8px; font-size:0.7rem; color:#aaa;">
            "When de bottom drop out, e hard to patch it." — Bajan Proverb, 2023
        </p>
    </div>
    ''')
    
    # Wrap in full HTML
    full_html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>How Did We Get Here? - Barbados Financial Accountability 2003-2026</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{
                font-family: 'Georgia', 'Times New Roman', serif;
                background: #f5f0e8;
                color: #1a1a2e;
                line-height: 1.7;
                padding: 0;
            }}
            .container {{
                max-width: 900px;
                margin: 0 auto;
                padding: 40px 30px 60px;
                background: #fffcf7;
                box-shadow: 0 0 40px rgba(0,0,0,0.08);
                min-height: 100vh;
            }}
            .cover {{
                text-align: center;
                padding: 60px 20px 40px;
                border-bottom: 3px solid #00267F;
                margin-bottom: 40px;
            }}
            .cover .flag-bar {{
                height: 8px;
                background: linear-gradient(90deg, #00267F 0%, #FFC726 50%, #00267F 100%);
                margin: 20px auto 30px;
                max-width: 600px;
                border-radius: 4px;
            }}
            .cover h1 {{
                font-size: 3rem;
                font-weight: 700;
                color: #00267F;
                letter-spacing: -0.5px;
                line-height: 1.2;
            }}
            .cover h1 .highlight {{
                color: #FFC726;
                background: #00267F;
                padding: 0 12px;
                border-radius: 4px;
            }}
            .cover .subtitle {{
                font-size: 1.4rem;
                color: #444;
                margin-top: 12px;
                font-style: italic;
            }}
            .cover .byline {{
                font-size: 1.1rem;
                color: #666;
                margin-top: 8px;
            }}
            .cover .years {{
                font-size: 1.6rem;
                font-weight: 300;
                color: #00267F;
                margin-top: 10px;
                letter-spacing: 4px;
            }}
            .part {{
                margin: 50px 0 30px;
                padding: 20px 30px;
                background: #00267F;
                color: white;
                border-radius: 8px;
                text-align: center;
            }}
            .part h2 {{
                font-size: 1.8rem;
                font-weight: 400;
                letter-spacing: 2px;
            }}
            .part .sub {{
                font-size: 1rem;
                opacity: 0.8;
                font-style: italic;
            }}
            .chapter {{
                margin: 40px 0 30px;
                padding-bottom: 10px;
                border-bottom: 2px solid #e0d6c8;
            }}
            .chapter .number {{
                font-size: 0.85rem;
                color: #888;
                font-weight: 600;
                letter-spacing: 1px;
                text-transform: uppercase;
            }}
            .chapter h3 {{
                font-size: 1.8rem;
                color: #00267F;
                margin: 4px 0 6px;
            }}
            .chapter .proverb {{
                font-size: 1.2rem;
                font-style: italic;
                color: #00267F;
                background: #f0ebe3;
                padding: 10px 20px;
                border-radius: 6px;
                border-left: 4px solid #FFC726;
                margin: 8px 0 16px;
            }}
            .chapter .proverb-meaning {{
                font-size: 0.95rem;
                color: #555;
                margin-top: -6px;
                margin-bottom: 16px;
                font-style: italic;
            }}
            .metric-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
                gap: 12px;
                margin: 16px 0 20px;
                background: #f8f5f0;
                border-radius: 8px;
                padding: 16px 20px;
                border: 1px solid #e0d6c8;
            }}
            .metric-item {{ text-align: center; }}
            .metric-item .label {{
                font-size: 0.7rem;
                text-transform: uppercase;
                color: #888;
                letter-spacing: 0.5px;
            }}
            .metric-item .value {{
                font-size: 1.3rem;
                font-weight: 700;
                color: #00267F;
            }}
            .metric-item .value.positive {{ color: #10B981; }}
            .metric-item .value.negative {{ color: #DC2626; }}
            .opinion-badge {{
                display: inline-block;
                padding: 4px 16px;
                border-radius: 20px;
                font-weight: 700;
                font-size: 0.9rem;
            }}
            .opinion-clean {{ background: #D1FAE5; color: #065F46; }}
            .opinion-disclaimer {{ background: #FEF3C7; color: #92400E; }}
            .opinion-adverse {{ background: #FEE2E2; color: #991B1B; }}
            .issue-critical {{
                background: #FEF2F2;
                padding: 10px 16px;
                border-radius: 8px;
                border-left: 4px solid #DC2626;
                margin: 6px 0;
                border: 1px solid #FCA5A5;
            }}
            .issue-warning {{
                background: #FFFBEB;
                padding: 10px 16px;
                border-radius: 8px;
                border-left: 4px solid #F59E0B;
                margin: 6px 0;
                border: 1px solid #FCD34D;
            }}
            .issue-info {{
                background: #F0F7FF;
                padding: 10px 16px;
                border-radius: 8px;
                border-left: 4px solid #3B82F6;
                margin: 6px 0;
                border: 1px solid #93C5FD;
            }}
            .summary-box {{
                background: #00267F;
                color: white;
                padding: 20px 24px;
                border-radius: 8px;
                margin: 20px 0;
            }}
            .summary-box h4 {{ color: #FFC726; }}
            .summary-box ul {{ list-style: none; padding: 0; }}
            .summary-box li {{ padding: 4px 0; border-bottom: 1px solid rgba(255,255,255,0.1); }}
            .summary-box li:last-child {{ border-bottom: none; }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 16px 0 20px;
                font-size: 0.9rem;
            }}
            table th {{
                background: #00267F;
                color: white;
                padding: 10px 12px;
                text-align: left;
            }}
            table td {{
                padding: 8px 12px;
                border-bottom: 1px solid #e0d6c8;
            }}
            table tr:nth-child(even) {{ background: #f8f5f0; }}
            .footer {{
                margin-top: 60px;
                padding-top: 30px;
                border-top: 3px solid #00267F;
                text-align: center;
                font-size: 0.85rem;
                color: #888;
            }}
            @media (max-width: 600px) {{
                .container {{ padding: 20px 16px; }}
                .cover h1 {{ font-size: 2rem; }}
                .metric-grid {{ grid-template-columns: repeat(2, 1fr); }}
                table {{ font-size: 0.75rem; }}
                table th, table td {{ padding: 4px 6px; }}
            }}
            @media print {{
                body {{ background: white; }}
                .container {{ box-shadow: none; padding: 20px; }}
                .chapter {{ page-break-inside: avoid; }}
                .part {{ page-break-after: avoid; }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            {''.join(book_content)}
        </div>
    </body>
    </html>
    '''
    
    return full_html

# ============================================================================
# RENDER FUNCTIONS
# ============================================================================
def render_chapter_card(year):
    """Render a single chapter card for the story arc view with working navigation."""
    data = FINANCIAL_DATA[year]
    special = SPECIAL_AUDITS.get(year, {'audits': [], 'issues': []})
    chapter = CHAPTER_TITLES.get(year, {"title": f"Year {year}", "tagline": ""})
    opinion = data['opinion']
    emoji = get_opinion_emoji(opinion)
    color = get_opinion_color(opinion)
    opinion_class = get_chapter_opinion_class(opinion)
    
    issue_count = len(special.get('issues', []))
    audit_count = len(special.get('audits', []))
    
    critical_count = 0
    high_count = 0
    for audit in special.get('audits', []):
        severity = audit.get('severity', 'Medium')
        if severity == 'Critical':
            critical_count += 1
        elif severity == 'High':
            high_count += 1
    
    severity_parts = []
    if critical_count > 0:
        severity_parts.append(f"🔴 {critical_count} Critical")
    if high_count > 0:
        severity_parts.append(f"🟠 {high_count} High")
    if audit_count > 0 and not severity_parts:
        severity_parts.append(f"📄 {audit_count} audits")
    
    severity_text = " | ".join(severity_parts) if severity_parts else "No special audits"
    
    all_years = list(range(2003, 2027))
    chapter_num = all_years.index(year) + 1
    
    col1, col2 = st.columns([5, 1])
    
    with col1:
        st.markdown(f"""
        <div class="chapter-card" style="border-left: 4px solid {color};">
            <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap;">
                <div style="flex:1;">
                    <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
                        <span class="chapter-number">Chapter {chapter_num}</span>
                        <span class="{opinion_class}">{emoji} {opinion}</span>
                        <span style="font-size:0.75rem; color:#888;">{get_era_badge(year)}</span>
                    </div>
                    <div class="chapter-title" style="color:{color};">{chapter['title']}</div>
                    <div class="chapter-tagline">"{chapter['tagline']}"</div>
                    <div class="chapter-stats">
                        📊 ${data['revenue']:.2f}B Revenue · {'' if data['deficit'] >= 0 else ''}${data['deficit']:.2f}B Deficit · ${data['debt']:.2f}B Debt
                    </div>
                    <div class="chapter-stats">
                        💥 {issue_count} issues · {audit_count} special audits · {severity_text}
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if st.button(f"Explore {year}", key=f"explore_{year}", use_container_width=True):
            st.session_state['selected_year'] = year
            st.session_state['view_mode'] = 'year'
            st.rerun()

def render_act_header(act_name, act_subtitle, act_color, act_class, years):
    count = len(years)
    st.markdown(f"""
    <div class="act-header {act_class}">
        <div class="act-title" style="color:{act_color};">{act_name}</div>
        <div class="act-subtitle">{act_subtitle}</div>
        <div class="act-count">{count} years</div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# VIEWS
# ============================================================================
def render_full_story():
    st.session_state['view_mode'] = 'story'
    
    st.markdown("""
    <div class="main-header">🇧🇧 Barbados: 24 Years of Financial Accountability</div>
    <div class="main-subheader">From Clean to Crisis — The Complete Audit Story 2003-2026</div>
    <div class="barbados-flag-bar"></div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background:#f0f7ff; padding:20px; border-radius:10px; border-left:5px solid #00267F; margin:15px 0;">
        <h3 style="color:#00267F; margin-top:0;">📖 The Full Story: Barbados' 24-Year Journey</h3>
        <p style="font-size:1.05rem; margin-bottom:0;">
        This is the complete narrative of Barbados' financial accountability journey, told through 
        <strong>24 years of Auditor General's reports</strong>. From clean opinions to the breaking point,
        from crisis to the path forward. Each chapter tells a part of the story. Click <strong>"Explore"</strong> on any year
        to dive into the details.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    render_act_header(
        "🟢 ACT I: THE GOLDEN YEARS",
        "5 clean opinions. Barbados had it right.",
        "#10B981",
        "act-clean",
        list(range(2003, 2008))
    )
    st.caption("The foundation was built. Financial management was functioning well. No major issues identified.")
    for year in range(2003, 2008):
        render_chapter_card(year)
    
    st.markdown("---")
    
    render_act_header(
        "🟡 ACT II: THE SLOW DECLINE",
        "10 disclaimer opinions. The same problems, year after year.",
        "#F59E0B",
        "act-disclaimer",
        list(range(2008, 2018))
    )
    st.caption("SOE consolidation. Asset valuation. Bank reconciliations. Year after year, the same issues. No progress.")
    for year in range(2008, 2018):
        render_chapter_card(year)
    
    st.markdown("---")
    
    render_act_header(
        "🔴 ACT III: THE BREAKING POINT",
        "6 adverse opinions. The system broke.",
        "#DC2626",
        "act-adverse",
        list(range(2018, 2024))
    )
    st.caption("Material misstatements. Unverified assets. Hidden liabilities. The financial management foundation crumbled.")
    for year in range(2018, 2024):
        render_chapter_card(year)
    
    st.markdown("---")
    
    render_act_header(
        "🟣 EPILOGUE: THE PATH FORWARD",
        "3 pending years. Will they fix it?",
        "#8B5CF6",
        "act-pending",
        list(range(2024, 2027))
    )
    st.caption("The future is unwritten. Will Barbados fix the foundation, or continue with the same pattern?")
    for year in range(2024, 2027):
        render_chapter_card(year)

def render_year_view(year):
    data = FINANCIAL_DATA[year]
    special = SPECIAL_AUDITS.get(year, {'audits': [], 'issues': []})
    proverb = PROVERBS.get(year, "Wisdom comes from experience.")
    meaning = PROVERB_MEANINGS.get(year, "")
    context = YEAR_CONTEXT.get(year, "")
    chapter = CHAPTER_TITLES.get(year, {"title": f"Year {year}", "tagline": ""})
    opinion = data['opinion']
    emoji = get_opinion_emoji(opinion)
    color = get_opinion_color(opinion)

    st.markdown("""
    <div class="main-header">🇧🇧 Barbados: 24 Years of Financial Accountability</div>
    <div class="barbados-flag-bar"></div>
    """, unsafe_allow_html=True)
    
    st.markdown(f'<div class="year-header">📌 Year {year}: {chapter["title"]}</div>', unsafe_allow_html=True)
    st.caption(f'"{chapter["tagline"]}"')

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(f"""
        <div class="proverb-card">
            <div style="color:#BFDBFE;font-size:0.75rem;">📖 Bajan Proverb · {year}</div>
            <div class="proverb-text">"{proverb}"</div>
            <div class="proverb-meaning">— {meaning}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="background:#f8f9fa;padding:18px;border-radius:10px;border-left:4px solid {color};text-align:center;">
            <div style="font-size:0.7rem;color:#888;">AUDIT OPINION</div>
            <div style="font-size:2.5rem;font-weight:bold;color:{color};">{emoji}</div>
            <div style="font-size:1.4rem;font-weight:bold;color:{color};">{opinion}</div>
            <div style="font-size:0.7rem;color:#888;margin-top:4px;">{get_era_badge(year)}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="background:#f0f7ff;padding:14px 20px;border-radius:10px;border-left:5px solid #00267F;margin:10px 0;">
        <div style="font-size:0.9rem;color:#1e293b;line-height:1.6;">
            <strong>📖 The Story of {year}:</strong> {context}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 💰 Key Financial Metrics")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        revenue = data['revenue']
        revenue_prev = FINANCIAL_DATA.get(year-1, {}).get('revenue', revenue)
        revenue_change = ((revenue - revenue_prev) / revenue_prev * 100) if revenue_prev != 0 else 0
        arrow = "▲" if revenue_change > 0 else "▼" if revenue_change < 0 else "→"
        change_color = "#10B981" if revenue_change > 0 else "#DC2626" if revenue_change < 0 else "#888"
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size:0.65rem;color:#888;">Revenue</div>
            <div class="metric-value">{format_currency_billions(revenue)}</div>
            <div style="font-size:0.7rem;color:{change_color};">{arrow} {abs(revenue_change):.1f}% vs {year-1}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        expenditure = data['expenditure']
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size:0.65rem;color:#888;">Expenditure</div>
            <div class="metric-value">{format_currency_billions(expenditure)}</div>
            <div style="font-size:0.7rem;color:#888;">{year} fiscal year</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        deficit = data['deficit']
        deficit_prev = FINANCIAL_DATA.get(year-1, {}).get('deficit', deficit)
        deficit_improved = deficit > deficit_prev
        deficit_color = "#10B981" if deficit_improved else "#DC2626" if deficit < 0 else "#888"
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size:0.65rem;color:#888;">Deficit / Surplus</div>
            <div class="metric-value" style="color:{deficit_color};">{format_currency_billions(abs(deficit))}</div>
            <div style="font-size:0.7rem;color:{deficit_color};">{'✅ Improving' if deficit_improved else '⚠️ Worsening'}</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        debt = data['debt']
        debt_pct = data.get('debt_pct', 0)
        debt_color = "#DC2626" if debt_pct > 100 else "#F59E0B" if debt_pct > 80 else "#10B981"
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size:0.65rem;color:#888;">Public Debt</div>
            <div class="metric-value">{format_currency_billions(debt)}</div>
            <div style="font-size:0.7rem;color:{debt_color};">{debt_pct:.1f}% of GDP</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 📊 Financial Breakdown")
    col1, col2 = st.columns([1, 1])

    with col1:
        rev_breakdown = get_revenue_breakdown(year)
        rev_data = []
        for category, percentage in rev_breakdown.items():
            rev_data.append({'Source': category, 'Amount': data['revenue'] * percentage, 'Percentage': percentage * 100})
        rev_df = pd.DataFrame(rev_data)
        fig = px.pie(rev_df, values='Amount', names='Source', title=f'Revenue Composition ({year})', color_discrete_sequence=px.colors.sequential.Blues_r, hole=0.4)
        fig.update_traces(textposition='inside', textinfo='percent+label', textfont_size=9)
        fig.update_layout(height=350, margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        exp_breakdown = get_expenditure_breakdown(year)
        exp_data = []
        for category, percentage in exp_breakdown.items():
            exp_data.append({'Category': category, 'Amount': data['expenditure'] * percentage, 'Percentage': percentage * 100})
        exp_df = pd.DataFrame(exp_data)
        fig = px.pie(exp_df, values='Amount', names='Category', title=f'Expenditure Composition ({year})', color_discrete_sequence=px.colors.sequential.Reds_r, hole=0.4)
        fig.update_traces(textposition='inside', textinfo='percent+label', textfont_size=9)
        fig.update_layout(height=350, margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 🚨 Key Issues")
    if special.get('issues'):
        for issue in special['issues']:
            if 'ADVERSE' in issue.upper() or 'FIRST' in issue.upper() or 'CRISIS' in issue.upper():
                st.markdown(f"""
                <div class="issue-critical">
                    <span style="color:#DC2626;font-weight:bold;">🔴 CRITICAL:</span> {issue}
                </div>
                """, unsafe_allow_html=True)
            elif any(x in issue.lower() for x in ['unverified', 'discrepancy', 'not done', 'failure', 'crisis', 'still', 'hidden', 'unconfirmed']):
                st.markdown(f"""
                <div class="issue-warning">
                    <span style="color:#D97706;font-weight:bold;">⚠️ WARNING:</span> {issue}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="issue-info">
                    <span style="color:#2563EB;font-weight:bold;">ℹ️ INFO:</span> {issue}
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("No major issues flagged for this year.")

    st.markdown("### 🔍 Special Audits")
    if special.get('audits'):
        for audit in special['audits']:
            severity = audit.get('severity', 'Medium')
            color = '#DC2626' if severity == 'Critical' else '#F59E0B' if severity == 'High' else '#3B82F6'
            with st.expander(f"📄 {audit['title']}", expanded=False):
                st.markdown(f"""
                <div style="padding:8px 0;">
                    <div style="font-weight:600;color:#1e293b;font-size:0.9rem;">📋 Summary</div>
                    <div style="color:#475569;font-size:0.9rem;padding-left:12px;padding-bottom:8px;">{audit['summary']}</div>
                    <div style="font-weight:600;color:#1e293b;font-size:0.9rem;">📄 Details</div>
                    <div style="color:#475569;font-size:0.9rem;padding-left:12px;padding-bottom:8px;">{audit['details']}</div>
                    <div style="font-weight:600;color:#1e293b;font-size:0.9rem;">⚡ Severity</div>
                    <div style="color:{color};font-weight:bold;font-size:0.9rem;padding-left:12px;">{severity}</div>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("No special audits for this year.")

    st.markdown("### 📈 Financial Health Indicators")
    col1, col2, col3 = st.columns(3)

    with col1:
        deficit_ratio = abs(data['deficit'] / data['revenue'] * 100) if data['revenue'] != 0 else 0
        ratio_color = "#10B981" if deficit_ratio < 10 else "#F59E0B" if deficit_ratio < 25 else "#DC2626"
        ratio_text = "Healthy" if deficit_ratio < 10 else "Concerning" if deficit_ratio < 25 else "Critical"
        st.markdown(f"""
        <div class="metric-card" style="border-left:4px solid {ratio_color};">
            <div style="font-size:0.65rem;color:#888;">Deficit-to-Revenue Ratio</div>
            <div class="metric-value" style="color:{ratio_color};font-size:1.5rem;">{deficit_ratio:.1f}%</div>
            <div style="font-size:0.7rem;color:{ratio_color};">{ratio_text}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        debt_pct = data.get('debt_pct', 0)
        debt_color = "#10B981" if debt_pct < 60 else "#F59E0B" if debt_pct < 100 else "#DC2626"
        debt_text = "Below 60%" if debt_pct < 60 else "Above 60%" if debt_pct < 100 else "Critical"
        st.markdown(f"""
        <div class="metric-card" style="border-left:4px solid {debt_color};">
            <div style="font-size:0.65rem;color:#888;">Debt-to-GDP Ratio</div>
            <div class="metric-value" style="color:{debt_color};font-size:1.5rem;">{debt_pct:.1f}%</div>
            <div style="font-size:0.7rem;color:{debt_color};">{debt_text}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        if year <= 2007:
            years_since_clean = 0
            clean_text = "✅ Current year is clean"
            clean_color = "#10B981"
        else:
            years_since_clean = year - 2007
            clean_color = "#DC2626" if years_since_clean > 15 else "#F59E0B"
            clean_text = f"{years_since_clean} years since last clean audit"
        st.markdown(f"""
        <div class="metric-card" style="border-left:4px solid {clean_color};">
            <div style="font-size:0.65rem;color:#888;">Audit Quality</div>
            <div class="metric-value" style="color:{clean_color};font-size:1.5rem;">{years_since_clean}</div>
            <div style="font-size:0.7rem;color:{clean_color};">{clean_text}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"### 📅 Historical Context: Where {year} Fits")
    all_years = list(range(2003, 2027))
    revenue_trend = [FINANCIAL_DATA[y]['revenue'] for y in all_years]
    debt_trend = [FINANCIAL_DATA[y]['debt'] for y in all_years]

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=all_years, y=revenue_trend, name='Revenue', line=dict(color='#10B981', width=2.5), hovertemplate='Year: %{x}<br>Revenue: $%{y:.2f}B<extra></extra>'), secondary_y=False)
    fig.add_trace(go.Scatter(x=all_years, y=debt_trend, name='Debt', line=dict(color='#DC2626', width=2.5, dash='dash'), hovertemplate='Year: %{x}<br>Debt: $%{y:.2f}B<extra></extra>'), secondary_y=True)
    fig.add_vline(x=year, line_dash="solid", line_color="#FFC726", line_width=3)
    fig.add_annotation(x=year, y=0.5, text=f"{year} ← Selected", showarrow=True, arrowhead=2, ax=0, ay=-40, font=dict(size=12, color="#00267F", weight="bold"))
    fig.add_vrect(x0=2003, x1=2007.5, fillcolor="rgba(16, 185, 129, 0.12)", line_width=0)
    fig.add_vrect(x0=2008, x1=2017.5, fillcolor="rgba(245, 158, 11, 0.12)", line_width=0)
    fig.add_vrect(x0=2018, x1=2023.5, fillcolor="rgba(220, 38, 38, 0.12)", line_width=0)
    fig.add_vrect(x0=2024, x1=2026.5, fillcolor="rgba(139, 92, 246, 0.12)", line_width=0)
    fig.update_layout(height=300, showlegend=True, legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5), hovermode='x unified', margin=dict(l=40, r=40, t=30, b=30))
    fig.update_yaxes(title_text="Revenue ($B)", secondary_y=False, range=[0, 18])
    fig.update_yaxes(title_text="Debt ($B)", secondary_y=True, range=[0, 18])
    st.plotly_chart(fig, use_container_width=True)

    opinion_history = [FINANCIAL_DATA[y]['opinion'] for y in range(2003, year+1)]
    consecutive = 0
    for op in reversed(opinion_history):
        if op == opinion:
            consecutive += 1
        else:
            break
    start_year = year - consecutive + 1
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"""
        <div style="background:#f8f9fa;padding:12px 20px;border-radius:10px;border:1px solid #e0e0e0;height:100%;display:flex;align-items:center;justify-content:center;">
            <span style="color:#666;font-size:0.9rem;">Current streak:</span>
            <span style="font-weight:bold;font-size:1.1rem;color:{color};margin:0 6px;">{consecutive} consecutive {opinion} opinions</span>
            <span style="color:#666;font-size:0.9rem;"> (since {start_year})</span>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        clean_so_far = opinion_history.count('Clean')
        disclaimer_so_far = opinion_history.count('Disclaimer')
        adverse_so_far = opinion_history.count('Adverse')
        pending_so_far = opinion_history.count('Pending')
        st.markdown(f"""
        <div style="background:#f8f9fa;padding:10px 16px;border-radius:10px;border:1px solid #e0e0e0;text-align:center;">
            <div style="font-size:0.7rem;color:#888;">Cumulative Opinions</div>
            <div style="display:flex;justify-content:center;gap:12px;margin-top:4px;">
                <span><span style="color:#10B981;">●</span> {clean_so_far}</span>
                <span><span style="color:#F59E0B;">●</span> {disclaimer_so_far}</span>
                <span><span style="color:#DC2626;">●</span> {adverse_so_far}</span>
                <span><span style="color:#8B5CF6;">●</span> {pending_so_far}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    if st.button("📖 Back to The Full Story", use_container_width=True):
        st.session_state['view_mode'] = 'story'
        st.rerun()

# ============================================================================
# DOWNLOAD FUNCTIONS
# ============================================================================
def render_download_section():
    """Render the book download section in the sidebar."""
    st.markdown("---")
    st.markdown("### 📖 Download Options")
    
    # Book Download
    st.markdown("""
    <div style="background:#f0f7ff; padding:12px 16px; border-radius:8px; border:1px solid #3B82F6; margin-bottom:10px;">
        <p style="margin:0; font-size:0.9rem; font-weight:600; color:#00267F;">📥 Download Complete Book</p>
        <p style="margin:0; font-size:0.8rem; color:#555;">Get the full story as a beautifully formatted HTML document.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("📥 Download Book (HTML)", use_container_width=True):
        html_content = generate_book_html()
        b64 = base64.b64encode(html_content.encode()).decode()
        href = f'<a href="data:text/html;base64,{b64}" download="How_Did_We_Get_Here_Barbados_Financial_Accountability.html" style="display:block; background:#10B981; color:white; text-align:center; padding:10px; border-radius:6px; text-decoration:none; font-weight:600;">✅ Click to Download Book</a>'
        st.markdown(href, unsafe_allow_html=True)
        st.success("Book ready! Click the green button above to download.")
    
    st.markdown("---")
    
    # Data Download
    st.markdown("""
    <div style="background:#f0f7ff; padding:12px 16px; border-radius:8px; border:1px solid #3B82F6; margin-bottom:10px;">
        <p style="margin:0; font-size:0.9rem; font-weight:600; color:#00267F;">📊 Download Financial Data</p>
        <p style="margin:0; font-size:0.8rem; color:#555;">Export all financial data as CSV for analysis.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("📊 Download Data (CSV)", use_container_width=True):
        df = get_dataframe()
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="barbados_financial_data.csv" style="display:block; background:#10B981; color:white; text-align:center; padding:10px; border-radius:6px; text-decoration:none; font-weight:600;">✅ Click to Download CSV</a>'
        st.markdown(href, unsafe_allow_html=True)
        st.success("Data ready! Click the green button above to download.")

# ============================================================================
# SIDEBAR
# ============================================================================
with st.sidebar:
    st.markdown("## 🇧🇧 Navigation")
    
    view_options = ["📖 The Full Story", "📌 Year-at-a-Glance"]
    
    if 'view_mode' not in st.session_state:
        st.session_state['view_mode'] = 'story'
    
    default_index = 1 if st.session_state['view_mode'] == 'year' else 0
    view_option = st.selectbox("Select View", view_options, index=default_index)
    
    st.markdown("---")
    
    if view_option == "📌 Year-at-a-Glance":
        st.markdown("### 📅 Select Year")
        all_years = list(range(2003, 2027))
        if 'selected_year' not in st.session_state:
            st.session_state['selected_year'] = 2023
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if st.button("◀", use_container_width=True):
                idx = all_years.index(st.session_state['selected_year'])
                if idx > 0:
                    st.session_state['selected_year'] = all_years[idx - 1]
                    st.rerun()
        with col2:
            st.markdown(f"<div style='text-align:center;font-weight:bold;color:#00267F;font-size:1.2rem;'>{st.session_state['selected_year']}</div>", unsafe_allow_html=True)
        with col3:
            if st.button("▶", use_container_width=True):
                idx = all_years.index(st.session_state['selected_year'])
                if idx < len(all_years) - 1:
                    st.session_state['selected_year'] = all_years[idx + 1]
                    st.rerun()
        
        year = st.session_state['selected_year']
        st.markdown("---")
        data = FINANCIAL_DATA[year]
        opinion = data['opinion']
        opinion_color = get_opinion_color(opinion)
        emoji = get_opinion_emoji(opinion)
        
        st.markdown("### 📊 Quick Stats")
        st.markdown(f"""
        <div style="background:#f8f9fa;padding:12px;border-radius:8px;margin-bottom:8px;border-left:4px solid {opinion_color};">
            <div style="font-size:0.7rem;color:#888;">Audit Opinion</div>
            <div style="font-size:1.1rem;font-weight:bold;color:{opinion_color};">{emoji} {opinion}</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f"""
        <div style="background:#f8f9fa;padding:12px;border-radius:8px;margin-bottom:8px;">
            <div style="font-size:0.7rem;color:#888;">Revenue</div>
            <div style="font-size:1rem;font-weight:bold;">{format_currency_billions(data['revenue'])}</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f"""
        <div style="background:#f8f9fa;padding:12px;border-radius:8px;margin-bottom:8px;">
            <div style="font-size:0.7rem;color:#888;">Deficit</div>
            <div style="font-size:1rem;font-weight:bold;color:{'#DC2626' if data['deficit'] < 0 else '#10B981'};">{format_currency_billions(abs(data['deficit']))}</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("---")
        st.markdown(get_era_badge(year), unsafe_allow_html=True)
    
    # Download section in sidebar
    render_download_section()

# ============================================================================
# MAIN CONTENT - ROUTING
# ============================================================================
if view_option == "📖 The Full Story":
    st.session_state['view_mode'] = 'story'
    render_full_story()
else:
    st.session_state['view_mode'] = 'year'
    if 'selected_year' not in st.session_state:
        st.session_state['selected_year'] = 2023
    render_year_view(st.session_state['selected_year'])

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("---")

all_opinions = [FINANCIAL_DATA[y]['opinion'] for y in range(2003, 2027)]
clean_count = all_opinions.count('Clean')
disclaimer_count = all_opinions.count('Disclaimer')
adverse_count = all_opinions.count('Adverse')
pending_count = all_opinions.count('Pending')

st.caption(f"""
**Data Source:** Auditor General's Reports (2003-2024) • Financial Statements of the Government of Barbados
**Opinions:** Clean ({clean_count} years: 2003-2007) • Disclaimer ({disclaimer_count} years: 2008-2017) • Adverse ({adverse_count} years: 2018-2023) • Pending ({pending_count} years: 2024-2026)
**Generated:** {datetime.now().strftime('%B %d, %Y %I:%M %p')}
""")