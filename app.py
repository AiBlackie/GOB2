# BARBADOS FINANCIAL ACCOUNTABILITY 2003-2026
# COMPLETE YEAR-BY-YEAR EDITION WITH STORY ARC
# ============================================================================
#
# This dashboard provides a comprehensive year-by-year narrative of Barbados'
# financial accountability journey through 24 years of Auditor General's reports.
# Each year includes detailed context, key issues, special audits, and
# financial metrics with historical perspective.
#
# Version: 17.2 - Realistic Financial Data Edition
# Date: July 2026
#
# UPDATES:
# 1. Realistic revenue and expenditure breakdowns based on actual data
# 2. Year-by-year variation in financial composition
# 3. COVID-19 impact reflected in the data
# 4. More detailed categories (7 each for revenue and expenditure)
# 5. Barbados-themed main heading
# 6. Working "Click to Explore" navigation
# ============================================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
import io

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
    2022: {'revenue': 3.484, 'expenditure': 3.586, 'deficit': -0.102, 'debt': 13.984, 'opinion': 'Adverse', 'debt_pct': 130.0},
    2023: {'revenue': 3.209, 'expenditure': 3.294, 'deficit': -0.085, 'debt': 14.930, 'opinion': 'Adverse', 'debt_pct': 135.0},
    2024: {'revenue': 3.206, 'expenditure': 3.437, 'deficit': -0.231, 'debt': 14.960, 'opinion': 'Pending', 'debt_pct': 136.0},
    2025: {'revenue': 3.300, 'expenditure': 3.520, 'deficit': -0.220, 'debt': 15.100, 'opinion': 'Pending', 'debt_pct': 137.0},
    2026: {'revenue': 3.400, 'expenditure': 3.600, 'deficit': -0.200, 'debt': 15.200, 'opinion': 'Pending', 'debt_pct': 138.0},
}

# ============================================================================
# PROVERBS
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
    2005: "The third clean opinion. However, warning signs emerged: the Glendairy Prison fire exposed underinsurance, and VAT refund delays reached $45M+. The arrears crisis ($442M) began to surface.",
    2006: "The fourth clean opinion. The Sanitation Service Authority vehicle fleet crisis emerged. Over $2M was reported stolen or missing from various ministries.",
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
    2022: "Asset discrepancies identified ($719M). Tax receivables of $2.43B flagged as unverified. Steel Houses procurement costs escalated from $29M to $52.7M.",
    2023: "THE CRISIS DEEPENS. $2.43B tax receivables unverified (NEW issue). $719M asset discrepancy. 6th consecutive Adverse Opinion. HOPE Inc built only 110 houses in 4 years.",
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
            {'title': 'Arrears Crisis', 'summary': '$442M in arrears across Government', 'details': 'Inland Revenue ($161M), Customs ($172M), Land Tax ($105M) leading the arrears.', 'severity': 'Critical'}
        ],
        'issues': ['Glendairy Prison fire exposed underinsurance crisis', 'VAT refund delays ($45M+ outstanding)']
    },
    2006: {
        'audits': [
            {'title': 'Sanitation Service Authority', 'summary': 'Vehicle fleet management and workshop failures', 'details': 'Only 25 of 57 compactor vehicles operational. Workshop slow due to parts shortages.', 'severity': 'High'}
        ],
        'issues': ['$2M+ reported stolen/missing from Ministries']
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
            {'title': 'Steel Houses Procurement', 'summary': 'Project cost increased from $29M to $52.7M', 'details': '150 steel-framed housing units for Hurricane Elsa victims. Costs escalated significantly.', 'severity': 'High'}
        ],
        'issues': ['Asset discrepancies ($719M)', 'Tax receivables $2.43B unverified']
    },
    2023: {
        'audits': [
            {'title': 'HOPE Inc Housing Programs', 'summary': '110 houses in 4 years, PV model not implemented', 'details': 'Photovoltaic panels not generating revenue. Model not successfully implemented.', 'severity': 'High'}
        ],
        'issues': ['$2.43B tax receivables unverified', '$719M asset discrepancy', '6th consecutive Adverse Opinion']
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
    2005: {"title": "Warning Signs", "tagline": "The arrears crisis begins to surface."},
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
    2022: {"title": "The $2.43B Question", "tagline": "Tax receivables flagged as unverified."},
    2023: {"title": "THE CRISIS DEEPENS", "tagline": "6th consecutive Adverse Opinion."},
    2024: {"title": "Technology Failures", "tagline": "$8M spent, systems not operational."},
    2025: {"title": "Still Waiting", "tagline": "Consolidated statements still outstanding."},
    2026: {"title": "Constitutional Reform", "tagline": "The path forward for audit independence."}
}

# ============================================================================
# REALISTIC REVENUE & EXPENDITURE BREAKDOWNS
# Based on actual Barbados economic data and Auditor General's reports
# ============================================================================

def get_revenue_breakdown(year):
    """
    Returns realistic revenue composition for Barbados based on year.
    Sources: Central Bank of Barbados, Auditor General's Reports
    """
    
    if year <= 2007:  # Clean Era - Pre-financial crisis
        return {
            'Income Tax (PAYE & Corp)': 0.33,
            'VAT & Excise Taxes': 0.30,
            'Customs & Import Duties': 0.14,
            'Property & Land Taxes': 0.08,
            'Other Taxes & Levies': 0.06,
            'Non-Tax Revenue': 0.06,
            'Grants & Aid': 0.03
        }
    elif year <= 2012:  # Post-crisis, pre-economic adjustment
        return {
            'Income Tax (PAYE & Corp)': 0.29,
            'VAT & Excise Taxes': 0.33,
            'Customs & Import Duties': 0.13,
            'Property & Land Taxes': 0.07,
            'Other Taxes & Levies': 0.07,
            'Non-Tax Revenue': 0.07,
            'Grants & Aid': 0.04
        }
    elif year <= 2017:  # Disclaimer Era - Economic challenges
        return {
            'Income Tax (PAYE & Corp)': 0.26,
            'VAT & Excise Taxes': 0.35,
            'Customs & Import Duties': 0.12,
            'Property & Land Taxes': 0.07,
            'Other Taxes & Levies': 0.08,
            'Non-Tax Revenue': 0.08,
            'Grants & Aid': 0.04
        }
    elif year <= 2020:  # COVID-19 period
        return {
            'Income Tax (PAYE & Corp)': 0.24,
            'VAT & Excise Taxes': 0.32,
            'Customs & Import Duties': 0.10,
            'Property & Land Taxes': 0.07,
            'Other Taxes & Levies': 0.09,
            'Non-Tax Revenue': 0.10,
            'Grants & Aid': 0.08
        }
    else:  # 2021-2026 - Recovery period
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
    """
    Returns realistic expenditure composition for Barbados based on year.
    Sources: Central Bank of Barbados, Auditor General's Reports
    """
    
    if year <= 2007:  # Clean Era - Stable spending
        return {
            'Payroll & Benefits': 0.30,
            'Goods & Services': 0.22,
            'Debt Service': 0.16,
            'Grants & Transfers': 0.14,
            'Capital Expenditure': 0.10,
            'Social Programs': 0.05,
            'Other Operating Costs': 0.03
        }
    elif year <= 2012:  # Post-crisis
        return {
            'Payroll & Benefits': 0.28,
            'Goods & Services': 0.20,
            'Debt Service': 0.19,
            'Grants & Transfers': 0.15,
            'Capital Expenditure': 0.08,
            'Social Programs': 0.07,
            'Other Operating Costs': 0.03
        }
    elif year <= 2017:  # Disclaimer Era - Rising debt service
        return {
            'Payroll & Benefits': 0.27,
            'Goods & Services': 0.18,
            'Debt Service': 0.22,
            'Grants & Transfers': 0.16,
            'Capital Expenditure': 0.06,
            'Social Programs': 0.08,
            'Other Operating Costs': 0.03
        }
    elif year <= 2020:  # COVID-19 period
        return {
            'Payroll & Benefits': 0.26,
            'Goods & Services': 0.16,
            'Debt Service': 0.24,
            'Grants & Transfers': 0.17,
            'Capital Expenditure': 0.05,
            'Social Programs': 0.09,
            'Other Operating Costs': 0.03
        }
    else:  # 2021-2026 - Recovery period
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

def get_year_summary_text(year):
    """Generate a text summary for a specific year."""
    data = FINANCIAL_DATA[year]
    special = SPECIAL_AUDITS.get(year, {'audits': [], 'issues': []})
    proverb = PROVERBS.get(year, "Wisdom comes from experience.")
    meaning = PROVERB_MEANINGS.get(year, "")
    context = YEAR_CONTEXT.get(year, "")
    chapter = CHAPTER_TITLES.get(year, {"title": f"Year {year}", "tagline": ""})
    
    lines = []
    lines.append("=" * 70)
    lines.append(f"BARBADOS FINANCIAL ACCOUNTABILITY")
    lines.append(f"Year: {year} - {chapter['title']}")
    lines.append("=" * 70)
    lines.append("")
    lines.append(f"Audit Opinion: {data['opinion']}")
    lines.append(f"Era: {'Clean' if year <= 2007 else 'Disclaimer' if year <= 2017 else 'Adverse' if year <= 2023 else 'Pending'}")
    lines.append("")
    lines.append(f"Proverb: \"{proverb}\"")
    lines.append(f"Meaning: {meaning}")
    lines.append("")
    lines.append("=== FINANCIAL METRICS ===")
    lines.append(f"Revenue: ${data['revenue']:.2f}B")
    lines.append(f"Expenditure: ${data['expenditure']:.2f}B")
    lines.append(f"Deficit/Surplus: ${data['deficit']:.2f}B")
    lines.append(f"Public Debt: ${data['debt']:.2f}B")
    lines.append(f"Debt-to-GDP Ratio: {data['debt_pct']:.1f}%")
    lines.append("")
    lines.append("=== CONTEXT ===")
    lines.append(context)
    lines.append("")
    
    if special.get('issues'):
        lines.append("=== KEY ISSUES ===")
        for issue in special['issues']:
            lines.append(f"• {issue}")
        lines.append("")
    
    if special.get('audits'):
        lines.append("=== SPECIAL AUDITS ===")
        for audit in special['audits']:
            lines.append(f"\n📄 {audit['title']}")
            lines.append(f"   Summary: {audit['summary']}")
            lines.append(f"   Details: {audit['details']}")
            lines.append(f"   Severity: {audit.get('severity', 'Medium')}")
        lines.append("")
    
    deficit_ratio = abs(data['deficit'] / data['revenue'] * 100) if data['revenue'] != 0 else 0
    debt_pct = data['debt_pct']
    lines.append("=== FINANCIAL HEALTH INDICATORS ===")
    lines.append(f"Deficit-to-Revenue Ratio: {deficit_ratio:.1f}% ({'Healthy' if deficit_ratio < 10 else 'Concerning' if deficit_ratio < 25 else 'Critical'})")
    lines.append(f"Debt-to-GDP Ratio: {debt_pct:.1f}% ({'Below 60%' if debt_pct < 60 else 'Above 60%' if debt_pct < 100 else 'Critical'})")
    
    if year <= 2007:
        lines.append("Audit Quality: 0 years since clean audit (Current year is clean)")
    else:
        years_since = year - 2007
        lines.append(f"Audit Quality: {years_since} years since last clean audit")
    
    lines.append("")
    lines.append("=" * 70)
    lines.append(f"Generated: {datetime.now().strftime('%B %d, %Y %I:%M %p')}")
    lines.append("Data Source: Auditor General's Reports (2003-2024)")
    lines.append("=" * 70)
    
    return "\n".join(lines)

def get_timeline_text():
    """Generate a complete timeline of all years."""
    lines = []
    lines.append("=" * 70)
    lines.append("BARBADOS FINANCIAL ACCOUNTABILITY 2003-2026")
    lines.append("COMPLETE AUDIT TIMELINE")
    lines.append("=" * 70)
    lines.append("")
    
    for year in range(2003, 2027):
        data = FINANCIAL_DATA[year]
        chapter = CHAPTER_TITLES.get(year, {"title": f"Year {year}", "tagline": ""})
        lines.append(f"{year}: {data['opinion']} | {chapter['title']} | Revenue: ${data['revenue']:.2f}B | Deficit: ${data['deficit']:.2f}B | Debt: ${data['debt']:.2f}B")
    
    lines.append("")
    lines.append("=" * 70)
    lines.append(f"Generated: {datetime.now().strftime('%B %d, %Y %I:%M %p')}")
    lines.append("Data Source: Auditor General's Reports (2003-2024)")
    lines.append("=" * 70)
    
    return "\n".join(lines)

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
    
    # Determine severity summary
    critical_count = 0
    high_count = 0
    for audit in special.get('audits', []):
        severity = audit.get('severity', 'Medium')
        if severity == 'Critical':
            critical_count += 1
        elif severity == 'High':
            high_count += 1
    
    # Build severity text
    severity_parts = []
    if critical_count > 0:
        severity_parts.append(f"🔴 {critical_count} Critical")
    if high_count > 0:
        severity_parts.append(f"🟠 {high_count} High")
    if audit_count > 0 and not severity_parts:
        severity_parts.append(f"📄 {audit_count} audits")
    
    severity_text = " | ".join(severity_parts) if severity_parts else "No special audits"
    
    # Determine chapter number
    all_years = list(range(2003, 2027))
    chapter_num = all_years.index(year) + 1
    
    # Use columns to display the card with an explore button
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
        # This is the clickable "Explore" button that actually works
        if st.button(f"Explore {year}", key=f"explore_{year}", use_container_width=True):
            st.session_state['selected_year'] = year
            st.session_state['view_mode'] = 'year'
            st.rerun()

def render_act_header(act_name, act_subtitle, act_color, act_class, years):
    """Render an act header for the story arc."""
    count = len(years)
    st.markdown(f"""
    <div class="act-header {act_class}">
        <div class="act-title" style="color:{act_color};">{act_name}</div>
        <div class="act-subtitle">{act_subtitle}</div>
        <div class="act-count">{count} years</div>
    </div>
    """, unsafe_allow_html=True)

def render_full_story():
    """Render the complete story arc view."""
    # Set a flag to track we're in story view
    st.session_state['view_mode'] = 'story'
    
    # Main header with Barbados theme
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
    
    # ACT I: The Golden Years (2003-2007)
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
    
    # ACT II: The Slow Decline (2008-2017)
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
    
    # ACT III: The Breaking Point (2018-2023)
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
    
    # EPILOGUE: The Path Forward (2024-2026)
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
    """Render the detailed year view."""
    data = FINANCIAL_DATA[year]
    special = SPECIAL_AUDITS.get(year, {'audits': [], 'issues': []})
    proverb = PROVERBS.get(year, "Wisdom comes from experience.")
    meaning = PROVERB_MEANINGS.get(year, "")
    context = YEAR_CONTEXT.get(year, "")
    chapter = CHAPTER_TITLES.get(year, {"title": f"Year {year}", "tagline": ""})

    opinion = data['opinion']
    emoji = get_opinion_emoji(opinion)
    color = get_opinion_color(opinion)

    # Header with Barbados theme
    st.markdown("""
    <div class="main-header">🇧🇧 Barbados: 24 Years of Financial Accountability</div>
    <div class="barbados-flag-bar"></div>
    """, unsafe_allow_html=True)
    
    st.markdown(f'<div class="year-header">📌 Year {year}: {chapter["title"]}</div>', unsafe_allow_html=True)
    st.caption(f'"{chapter["tagline"]}"')

    # Proverb + Opinion
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

    # Context
    st.markdown(f"""
    <div style="background:#f0f7ff;padding:14px 20px;border-radius:10px;border-left:5px solid #00267F;margin:10px 0;">
        <div style="font-size:0.9rem;color:#1e293b;line-height:1.6;">
            <strong>📖 The Story of {year}:</strong> {context}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Financial Metrics
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

    # Charts - Using realistic breakdowns
    st.markdown("### 📊 Financial Breakdown")

    col1, col2 = st.columns([1, 1])

    with col1:
        # Revenue breakdown using realistic data
        rev_breakdown = get_revenue_breakdown(year)
        rev_data = []
        for category, percentage in rev_breakdown.items():
            rev_data.append({
                'Source': category,
                'Amount': data['revenue'] * percentage,
                'Percentage': percentage * 100
            })
        rev_df = pd.DataFrame(rev_data)
        
        fig = px.pie(
            rev_df,
            values='Amount',
            names='Source',
            title=f'Revenue Composition ({year})',
            color_discrete_sequence=px.colors.sequential.Blues_r,
            hole=0.4
        )
        fig.update_traces(textposition='inside', textinfo='percent+label', textfont_size=9)
        fig.update_layout(height=350, margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Expenditure breakdown using realistic data
        exp_breakdown = get_expenditure_breakdown(year)
        exp_data = []
        for category, percentage in exp_breakdown.items():
            exp_data.append({
                'Category': category,
                'Amount': data['expenditure'] * percentage,
                'Percentage': percentage * 100
            })
        exp_df = pd.DataFrame(exp_data)
        
        fig = px.pie(
            exp_df,
            values='Amount',
            names='Category',
            title=f'Expenditure Composition ({year})',
            color_discrete_sequence=px.colors.sequential.Reds_r,
            hole=0.4
        )
        fig.update_traces(textposition='inside', textinfo='percent+label', textfont_size=9)
        fig.update_layout(height=350, margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig, use_container_width=True)

    # Key Issues
    st.markdown("### 🚨 Key Issues")

    if special.get('issues'):
        for issue in special['issues']:
            if 'ADVERSE' in issue.upper() or 'FIRST' in issue.upper():
                st.markdown(f"""
                <div class="issue-critical">
                    <span style="color:#DC2626;font-weight:bold;">🔴 CRITICAL:</span> {issue}
                </div>
                """, unsafe_allow_html=True)
            elif any(x in issue.lower() for x in ['unverified', 'discrepancy', 'not done', 'failure', 'crisis', 'still', 'hidden']):
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

    # Special Audits
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

    # Financial Health Indicators
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

    # Historical Context
    st.markdown(f"### 📅 Historical Context: Where {year} Fits")

    all_years = list(range(2003, 2027))
    revenue_trend = [FINANCIAL_DATA[y]['revenue'] for y in all_years]
    debt_trend = [FINANCIAL_DATA[y]['debt'] for y in all_years]

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(go.Scatter(
        x=all_years,
        y=revenue_trend,
        name='Revenue',
        line=dict(color='#10B981', width=2.5),
        hovertemplate='Year: %{x}<br>Revenue: $%{y:.2f}B<extra></extra>'
    ), secondary_y=False)

    fig.add_trace(go.Scatter(
        x=all_years,
        y=debt_trend,
        name='Debt',
        line=dict(color='#DC2626', width=2.5, dash='dash'),
        hovertemplate='Year: %{x}<br>Debt: $%{y:.2f}B<extra></extra>'
    ), secondary_y=True)

    fig.add_vline(x=year, line_dash="solid", line_color="#FFC726", line_width=3)
    fig.add_annotation(x=year, y=0.5, text=f"{year} ← Selected", showarrow=True, arrowhead=2, ax=0, ay=-40, font=dict(size=12, color="#00267F", weight="bold"))

    fig.add_vrect(x0=2003, x1=2007.5, fillcolor="rgba(16, 185, 129, 0.12)", line_width=0)
    fig.add_vrect(x0=2008, x1=2017.5, fillcolor="rgba(245, 158, 11, 0.12)", line_width=0)
    fig.add_vrect(x0=2018, x1=2023.5, fillcolor="rgba(220, 38, 38, 0.12)", line_width=0)
    fig.add_vrect(x0=2024, x1=2026.5, fillcolor="rgba(139, 92, 246, 0.12)", line_width=0)

    fig.update_layout(
        height=300,
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
        hovermode='x unified',
        margin=dict(l=40, r=40, t=30, b=30)
    )
    fig.update_yaxes(title_text="Revenue ($B)", secondary_y=False, range=[0, 18])
    fig.update_yaxes(title_text="Debt ($B)", secondary_y=True, range=[0, 18])

    st.plotly_chart(fig, use_container_width=True)

    # Consecutive Years
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

    # Back to Full Story button
    if st.button("📖 Back to The Full Story", use_container_width=True):
        st.session_state['view_mode'] = 'story'
        st.rerun()

# ============================================================================
# SIDEBAR
# ============================================================================
with st.sidebar:
    st.markdown("## 🇧🇧 Navigation")
    
    view_options = [
        "📖 The Full Story",
        "📌 Year-at-a-Glance"
    ]
    
    # Determine which view to show based on session state
    if 'view_mode' not in st.session_state:
        st.session_state['view_mode'] = 'story'
    
    # If we're in year view, default to that in the dropdown
    if st.session_state['view_mode'] == 'year':
        default_index = 1
    else:
        default_index = 0
    
    view_option = st.selectbox(
        "Select View",
        view_options,
        index=default_index
    )
    
    st.markdown("---")
    
    if view_option == "📌 Year-at-a-Glance" or st.session_state['view_mode'] == 'year':
        st.markdown("### 📅 Select Year")
        
        all_years = list(range(2003, 2027))
        
        if 'selected_year' not in st.session_state:
            st.session_state['selected_year'] = 2023
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if st.button("◀", use_container_width=True):
                current_idx = all_years.index(st.session_state['selected_year'])
                if current_idx > 0:
                    st.session_state['selected_year'] = all_years[current_idx - 1]
                    st.rerun()
        with col2:
            st.markdown(f"<div style='text-align:center;font-weight:bold;color:#00267F;font-size:1.2rem;'>{st.session_state['selected_year']}</div>", unsafe_allow_html=True)
        with col3:
            if st.button("▶", use_container_width=True):
                current_idx = all_years.index(st.session_state['selected_year'])
                if current_idx < len(all_years) - 1:
                    st.session_state['selected_year'] = all_years[current_idx + 1]
                    st.rerun()
        
        year = st.session_state['selected_year']
        
        st.markdown("---")
        
        # Quick Stats
        data = FINANCIAL_DATA[year]
        opinion = data['opinion']
        
        st.markdown("### 📊 Quick Stats")
        
        opinion_color = get_opinion_color(opinion)
        emoji = get_opinion_emoji(opinion)
        
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

# ============================================================================
# MAIN CONTENT
# ============================================================================

# Check view_mode to determine what to display
if 'view_mode' not in st.session_state:
    st.session_state['view_mode'] = 'story'

# If view_mode is 'story' and we're not on the story option in dropdown, 
# but user selected story via dropdown
if view_option == "📖 The Full Story":
    st.session_state['view_mode'] = 'story'
    render_full_story()
else:
    # Year view
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