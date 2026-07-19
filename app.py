# ============================================================================
# BARBADOS FINANCIAL ACCOUNTABILITY 2003-2026
# COMPLETE YEAR-BY-YEAR EDITION WITH STORY ARC & BOOK DOWNLOAD
# 
# VERSION: 22.0 - ALL PROVERBS FROM "DE MORTAR-PESTLE" BY G. ADDINTON FORDE (1987)
# DATE: July 2026
#
# All Bajan proverbs used in this dashboard are drawn directly from
# "De Mortar-Pestle: A Collection of Barbadian Proverbs" by G. Addinton Forde (1987).
# Each proverb is cited with its page number from the original publication.
#
# AUTHOR & COMPILER: Matthew A. A. Blackman
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
.proverb-source {
    color: #93C5FD;
    font-size: 0.7rem;
    margin-top: 2px;
    opacity: 0.7;
}
.proverb-why {
    color: #E0E7FF;
    font-size: 0.8rem;
    margin-top: 6px;
    padding: 8px 12px;
    background: rgba(255,255,255,0.08);
    border-radius: 6px;
    border-left: 3px solid #FFC726;
}
.proverb-solution {
    color: #D1FAE5;
    font-size: 0.8rem;
    margin-top: 6px;
    padding: 8px 12px;
    background: rgba(16, 185, 129, 0.15);
    border-radius: 6px;
    border-left: 3px solid #10B981;
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
.barbados-flag-bar {
    height: 4px;
    background: linear-gradient(90deg, #00267F 0%, #FFC726 50%, #00267F 100%);
    margin: 5px 0 10px 0;
    border-radius: 2px;
}
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
.chapter-card {
    background: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    padding: 15px 20px;
    margin-bottom: 12px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.04);
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
.credits-section {
    background: #f8f5f0;
    padding: 20px 24px;
    border-radius: 10px;
    border: 2px solid #00267F;
    margin: 20px 0;
}
.credits-section h4 {
    color: #00267F;
    margin-bottom: 8px;
}
.conclusion-section {
    background: linear-gradient(135deg, #00267F 0%, #1E40AF 100%);
    color: white;
    padding: 25px 30px;
    border-radius: 12px;
    margin: 20px 0;
    border-left: 6px solid #FFC726;
}
.conclusion-section h2 {
    color: #FFC726;
    font-size: 1.8rem;
    margin-top: 0;
}
.conclusion-section .proverb-text {
    font-size: 1.4rem;
    font-style: italic;
    color: #FFC726;
    font-weight: 600;
}
.conclusion-section .proverb-meaning {
    color: #BFDBFE;
    font-size: 0.9rem;
}
.solution-card {
    background: rgba(255,255,255,0.08);
    border-radius: 8px;
    padding: 12px 16px;
    margin: 8px 0;
    border-left: 3px solid #10B981;
}
.solution-card .proverb {
    font-style: italic;
    color: #FFC726;
    font-weight: 600;
}
.solution-card .meaning {
    color: #BFDBFE;
    font-size: 0.85rem;
}
.solution-card .action {
    color: #D1FAE5;
    font-size: 0.85rem;
    margin-top: 4px;
}
</style>
""", unsafe_allow_html=True)

# ============================================================================
# FINANCIAL DATA
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
# PROVERBS - ALL FROM "DE MORTAR-PESTLE" BY G. ADDINTON FORDE (1987)
# ============================================================================
PROVERBS = {
    2003: {
        "text": "Empty bag can' stan' up, and full bag can' ben[d].",
        "meaning": "One must have proper sustenance to function efficiently.",
        "page": 17,
        "why": "A strong foundation requires proper sustenance. Barbados had the basics right in 2003. The books balanced. The foundation was solid."
    },
    2004: {
        "text": "Head en' mek fuh hat alone.",
        "meaning": "One should always use one's common sense.",
        "page": 17,
        "why": "Good governance requires common sense, not just appearances. Accrual accounting was announced, showing Barbados was thinking ahead."
    },
    2005: {
        "text": "Don' leh one drop o' tar mek yuh lose yuh whole ship and cargo.",
        "meaning": "Do not try to save a small amount, if that saving could cause you to lose a great deal more.",
        "page": 16,
        "why": "The Glendairy Prison fire — saving pennies on insurance cost millions. Government lost the opportunity to recover several million dollars."
    },
    2006: {
        "text": "Bucket gine up and down in well evah day, de bottom boun' to drop out.",
        "meaning": "Continued stress and strain will inevitably result in a breakdown.",
        "page": 15,
        "why": "The SSA vehicle crisis — 25 of 57 compactor trucks operational. The system was under stress and would eventually break."
    },
    2007: {
        "text": "Don' ship all yuh sugar in one vessel.",
        "meaning": "Do not risk all of your resources in a single venture.",
        "page": 16,
        "why": "The Newton Business Park PPP failure — $18.5M lost. Don't risk everything in one venture."
    },
    2008: {
        "text": "Water don' stan' pon galvanise.",
        "meaning": "Nothing is absorbed by the individual who lacks the basic qualities to accept and make use of what is being offered.",
        "page": 20,
        "why": "The first Disclaimer Opinion. IPSAS adoption was incomplete. Lessons weren't being absorbed. Nothing was sticking."
    },
    2009: {
        "text": "Yuh put out yuh barrel now dat de rain done fall.",
        "meaning": "The person has waited until too late to take advantage of a situation.",
        "page": 22,
        "why": "29,000 applicants on housing waiting list, only 226 houses built. Too little, too late."
    },
    2010: {
        "text": "De tongue dat buy yuh does sell yuh.",
        "meaning": "The same person who flatters you, may betray you later.",
        "page": 26,
        "why": "The Embassy of Venezuela fraud — trusted embassy officials betrayed that trust. $52,433 misappropriated."
    },
    2011: {
        "text": "Yuh can hide and buy ground, but yuh can' hide and wuck it.",
        "meaning": "It is impossible to hide all of one's actions.",
        "page": 34,
        "why": "Invest Barbados spent $70M with unclear outcomes. You can't hide poor performance forever."
    },
    2012: {
        "text": "Yuh don't tek down Drax Hall to fix Kendal.",
        "meaning": "It does not make sense destroying something of value in order to make right something of equal or less value.",
        "page": 22,
        "why": "$700M+ procurement irregularities at BWA. 90% of contracts without public tender. Destroying public trust to fix something else."
    },
    2013: {
        "text": "What' en' pass yuh en' miss yuh.",
        "meaning": "Having escaped a particular misfortune does not mean that you are immune from it.",
        "page": 31,
        "why": "$157M owed to land owners. Extensive squatting on Crown lands. The problem didn't go away — it got worse."
    },
    2014: {
        "text": "When goat dung want to roll, it will roll up a hill.",
        "meaning": "When people want to make trouble, they will do so regardless of the circumstances.",
        "page": 9,
        "why": "$475M in VAT could not be verified. Bank reconciliations not done for years. The problems were determined to happen."
    },
    2015: {
        "text": "De sea en' got nuh back door.",
        "meaning": "The sea is not a safe place, as there is no guarantee that you will get back out.",
        "page": 32,
        "why": "SOE consolidation still not done (8 years). Pension liability hidden from the balance sheet. No escape from the truth."
    },
    2016: {
        "text": "High wind know with ole house live.",
        "meaning": "Advantage is taken of those known to be weak.",
        "page": 17,
        "why": "NHC High Rise project — $442K per unit, well above low-income range. The vulnerable — taxpayers and the poor — paid the price."
    },
    2017: {
        "text": "Who help yuh buy a big guts mule don' help yuh feed it.",
        "meaning": "He who gets you in trouble does not get you out of it.",
        "page": 10,
        "why": "Debt reached $13.1B. The helpers who got us into this mess had vanished. The last warning before the crisis."
    },
    2018: {
        "text": "Evah pig got a Saturday.",
        "meaning": "Everybody has his day of retribution.",
        "page": 4,
        "why": "After 15 years of warnings, retribution arrived. The day of reckoning came. FIRST ADVERSE OPINION. $9.15B+ in issues."
    },
    2019: {
        "text": "When a bird fly too fast, 'e does fly past 'e nest.",
        "meaning": "It is not wise to be over-ambitious.",
        "page": 9,
        "why": "BWA Smart Meter project — $1.49B in contracts, 90% without public tender. Over-ambition led to disaster."
    },
    2020: {
        "text": "Manure don' mek ole plant grow.",
        "meaning": "Good treatment is useless if administered too late.",
        "page": 33,
        "why": "$1.8B in fixed assets excluded from balance sheet. COVID-19 response came too late for some. Good treatment too late."
    },
    2021: {
        "text": "Hard ears yuh won' hear, bye and bye yuh gine feel.",
        "meaning": "Persistent disobedience will eventually result in pain.",
        "page": 28,
        "why": "6th consecutive Adverse Opinion. Deficit peaked at $685M. They still weren't listening. Now they feel the pain."
    },
    2022: {
        "text": "Duh is more in de mortar dan de pestle.",
        "meaning": "There is more to the issue than appears on the surface.",
        "page": 16,
        "why": "$2.61B tax receivables reported, but $120M in cumulative interest omitted. The hidden truth was much bigger than it appeared."
    },
    2023: {
        "text": "Trouble don' set up like rain.",
        "meaning": "Misfortune can arrive at unexpected times, so be careful.",
        "page": 33,
        "why": "$2.43B tax receivables could not be confirmed. $719M asset discrepancy. $115M cash overstatement. Misfortune arrived unexpectedly."
    },
    2024: {
        "text": "Every bush is a man.",
        "meaning": "Be careful how you talk, as you never know when you are being overheard.",
        "page": 33,
        "why": "$8M spent on IT systems at Licensing Authority — systems not operational after 4 years. Everyone knew but no one spoke."
    },
    2025: {
        "text": "Wha' do in de dark does come out in de light.",
        "meaning": "It is impossible to hide all of one's actions.",
        "page": 34,
        "why": "Consolidated financial statements still outstanding. Pension liability not disclosed. The truth will eventually be revealed."
    },
    2026: {
        "text": "De higher de monkey climb, de more 'e show 'e tail.",
        "meaning": "The more one shows off, the more one's faults are brought into the open.",
        "page": 2,
        "why": "Constitutional reform recommended for audit independence. As Barbados rises to address its challenges, its flaws become visible."
    }
}

# ============================================================================
# CONCLUSION PROVERBS - SOLUTIONS FROM "DE MORTAR-PESTLE"
# ============================================================================
SOLUTION_PROVERBS = [
    {
        "text": "Don' wait till de horse get out to shut de stable door.",
        "meaning": "Do not wait until a situation gets out of hand before taking remedial action.",
        "page": 3,
        "action": "Fix the foundation NOW. Don't wait for another crisis. Address the asset registers, bank reconciliations, and SOE consolidation immediately."
    },
    {
        "text": "It does tek one hand to feel a lice, but two to tek it out.",
        "meaning": "It takes co-operation to achieve anything worthwhile.",
        "page": 5,
        "action": "Co-operation between the Auditor General, Parliament, and Government is essential. Accountability requires all hands working together."
    },
    {
        "text": "Mek-sure better dan cock-sure.",
        "meaning": "It is better to make absolutely sure that everything is alright, than to assume that all is well.",
        "page": 29,
        "action": "Verify everything. Don't assume the numbers are correct. Independent verification of tax receivables, assets, and liabilities is essential."
    },
    {
        "text": "Tek time en' laziness.",
        "meaning": "Much can be achieved by taking one's time.",
        "page": 30,
        "action": "Take the time to get it right. Rushing leads to mistakes. Proper implementation of systems and controls takes time but pays off."
    },
    {
        "text": "Studiation beat eddication.",
        "meaning": "Common sense is better than formal education.",
        "page": 36,
        "action": "Apply common sense to financial management. The solutions are not complex — they require discipline, integrity, and follow-through."
    },
    {
        "text": "Gih Jack 'e jacket.",
        "meaning": "Give every man his due credit.",
        "page": 17,
        "action": "Hold people accountable. Give credit where it's due, but also ensure consequences for failure. Accountability works both ways."
    },
    {
        "text": "If greedy wait, hot will cool.",
        "meaning": "Patience will be rewarded.",
        "page": 12,
        "action": "Be patient with the reform process. Sustainable change takes time. Don't rush, but don't delay either."
    },
    {
        "text": "Home drum beat first.",
        "meaning": "One should see after the interest of one's family before taking on somebody else's problems.",
        "page": 17,
        "action": "Put Barbados' financial house in order first. Fix the domestic issues before taking on international obligations."
    }
]

# ============================================================================
# YEAR CONTEXT
# ============================================================================
YEAR_CONTEXT = {
    2003: "The beginning of the clean audit era. Barbados' financial management was functioning well with no major issues identified. The foundation was being built for the years ahead.",
    2004: "The second consecutive clean opinion. Financial management remained strong. The announcement of accrual accounting signaled a commitment to international standards.",
    2005: "The third clean opinion. However, warning signs emerged: the Glendairy Prison fire in March 2005 exposed severe underinsurance — the property was insured for less than $1M despite being valued at $43.2M.",
    2006: "The fourth clean opinion. However, serious issues emerged: the Sanitation Service Authority operated with as few as 25 of 57 compactor vehicles. Over $2M was reported stolen or missing from ministries.",
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
    2020: "COVID-19 impacted audits. $1.8B in fixed assets excluded from balance sheet. $1.7B in land valuations unverified.",
    2021: "Deficit peaked at $685M. 6th consecutive Adverse Opinion. The PRDS performance review system was still not fully implemented after 20 years.",
    2022: "Adverse Opinion continues. Tax receivables of $2.61B reported, but $120M in cumulative interest omitted. Pension liabilities not included.",
    2023: "THE CRISIS DEEPENS. $2.43B tax receivables could not be confirmed. $719M asset discrepancy. $115M cash overstatement. 6th consecutive Adverse Opinion.",
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
            {'title': "St. Leonard's School Refurbishment", 'summary': 'CDB loan funds lost due to non-compliance', 'severity': 'High'},
            {'title': 'Magistrates Courts Cash Management', 'summary': 'Cash shortages and unauthorized write-offs', 'severity': 'Medium'}
        ],
        'issues': ['First major special audits conducted', 'New Public Accounts Committee Act passed']
    },
    2004: {
        'audits': [
            {'title': 'Barbados Tourism Authority', 'summary': '$10M+ deficits, "Best of Barbados" cost overruns', 'severity': 'High'},
            {'title': 'Urban Development Commission', 'summary': 'Loan programme failures and poor governance', 'severity': 'High'}
        ],
        'issues': ['Special audits of BTA and UDC', 'Accrual accounting announced']
    },
    2005: {
        'audits': [
            {'title': 'Glendairy Prison Fire', 'summary': '$43.2M property insured for under $1M', 'severity': 'Critical'},
            {'title': 'Arrears Crisis', 'summary': '$442M in arrears across Government', 'severity': 'Critical'}
        ],
        'issues': ['Glendairy Prison fire exposed underinsurance crisis', 'VAT refund delays ($45M+ outstanding)']
    },
    2006: {
        'audits': [
            {'title': 'Sanitation Service Authority', 'summary': 'Only 25 of 57 compactor vehicles operational', 'severity': 'Critical'},
            {'title': 'St. Leonard\'s Boys\' School', 'summary': '9 years, $15M+ spent, project incomplete', 'severity': 'High'}
        ],
        'issues': ['$2M+ reported stolen from Ministries', '$1M stolen from Psychiatric Hospital']
    },
    2007: {
        'audits': [
            {'title': 'Newton Business Park PPP', 'summary': 'PPP failure, $18.5M lost', 'severity': 'Critical'}
        ],
        'issues': ['PPP projects under scrutiny', 'Newton Business Park failure']
    },
    2008: {
        'audits': [
            {'title': 'First Disclaimer Opinion', 'summary': 'IPSAS adoption incomplete, asset registers inadequate', 'severity': 'Critical'}
        ],
        'issues': ['First Disclaimer Opinion issued', 'Accrual accounting transition challenges']
    },
    2009: {
        'audits': [
            {'title': 'National Housing Corporation', 'summary': '29,000 applicants, only 226 houses built', 'severity': 'High'},
            {'title': 'Barbados Road Network Project', 'summary': 'PPP cost overruns and disputes', 'severity': 'High'}
        ],
        'issues': ['NHC housing crisis', 'Road network PPP challenges']
    },
    2010: {
        'audits': [
            {'title': 'Embassy of Venezuela', 'summary': '$52,433 misappropriated by embassy official', 'severity': 'Critical'},
            {'title': 'Barbados Coalition of Service Industries', 'summary': '$4.1M in grants with minimal returns', 'severity': 'High'}
        ],
        'issues': ['Embassy fraud exposed', 'BCSI value-for-money concerns']
    },
    2011: {
        'audits': [
            {'title': 'Invest Barbados Performance Review', 'summary': '$70M spent, outcomes unclear', 'severity': 'High'}
        ],
        'issues': ['Performance audit era begins', 'Focus on value-for-money']
    },
    2012: {
        'audits': [
            {'title': 'Barbados Water Authority', 'summary': '$700M+ procurement irregularities, 90% without tender', 'severity': 'Critical'}
        ],
        'issues': ['Special audit on BWA', 'Procurement transparency concerns']
    },
    2013: {
        'audits': [
            {'title': 'Land Acquisition Process', 'summary': '$157M outstanding compensation to land owners', 'severity': 'Critical'},
            {'title': 'Illegal Occupation of Crown Lands', 'summary': 'Extensive squatting across Barbados', 'severity': 'High'}
        ],
        'issues': ['Land acquisition crisis', 'Squatting on Crown lands']
    },
    2014: {
        'audits': [
            {'title': 'VAT Division Review', 'summary': '$475M in unverified receivables', 'severity': 'Critical'},
            {'title': 'Inland Revenue Department', 'summary': 'Receivables unverified for years', 'severity': 'Critical'}
        ],
        'issues': ['Tax receivables crisis deepens', 'Bank reconciliation failures']
    },
    2015: {
        'audits': [],
        'issues': ['SOE consolidation still not done (8 years)', 'Pension liability hidden']
    },
    2016: {
        'audits': [
            {'title': 'NHC High Rise Apartments', 'summary': '$442K per unit, well above low-income range', 'severity': 'High'}
        ],
        'issues': ['First Adverse Opinion (2018 approaching)', 'Financial crisis building']
    },
    2017: {
        'audits': [],
        'issues': ['Pre-Adverse era ending', 'Debt reaches $13.1B']
    },
    2018: {
        'audits': [
            {'title': 'School Meals Centre', 'summary': '$23.12M spent, project incomplete after 6 years', 'severity': 'High'},
            {'title': 'Transport Board', 'summary': 'Bus availability declined from 163 to 50 buses', 'severity': 'Critical'},
            {'title': 'Clearwater Bay', 'summary': '$124M loan guarantee written off', 'severity': 'Critical'}
        ],
        'issues': ['🔴 FIRST ADVERSE OPINION', 'SOE consolidation not done (15 years)']
    },
    2019: {
        'audits': [
            {'title': 'BWA Smart Meter Project', 'summary': '$1.49B in contracts, 90% without public tender', 'severity': 'Critical'}
        ],
        'issues': ['Adverse Opinion continues', 'Cash overstatements identified']
    },
    2020: {
        'audits': [
            {'title': 'Poverty Eradication Fund', 'summary': '$24M disbursed without proper criteria', 'severity': 'High'}
        ],
        'issues': ['COVID-19 impact on audits', '$1.8B fixed assets excluded from balance sheet']
    },
    2021: {
        'audits': [
            {'title': 'PRDS Special Audit', 'summary': 'Performance Review system still not fully implemented after 20 years', 'severity': 'Medium'}
        ],
        'issues': ['6th consecutive Adverse Opinion', 'Deficit peaks ($685M)']
    },
    2022: {
        'audits': [
            {'title': 'Tax Receivables Review', 'summary': '$2.61B tax receivables, $120M interest omitted', 'severity': 'Critical'}
        ],
        'issues': ['Adverse Opinion continues', '$2.61B tax receivables unverified']
    },
    2023: {
        'audits': [
            {'title': 'Tax Receivables Unconfirmed', 'summary': '$2.43B tax receivables could not be confirmed', 'severity': 'Critical'},
            {'title': 'Asset Discrepancy', 'summary': '$719M difference in Other Capital Assets', 'severity': 'Critical'}
        ],
        'issues': ['🔴 CRISIS DEEPENS', '6th consecutive Adverse Opinion']
    },
    2024: {
        'audits': [
            {'title': 'Barbados Licensing Authority IT Systems', 'summary': '$8M spent, systems not fully operational after 4 years', 'severity': 'High'}
        ],
        'issues': ['IT audit reveals system failures']
    },
    2025: {
        'audits': [
            {'title': 'HOPE Inc Update', 'summary': '110 houses completed, PV model still not operational', 'severity': 'Medium'}
        ],
        'issues': ['Consolidated financial statements still outstanding']
    },
    2026: {
        'audits': [
            {'title': 'Projected Focus Areas', 'summary': 'Continued focus on SOE consolidation and asset verification', 'severity': 'Medium'}
        ],
        'issues': ['Constitutional reform recommendation', 'Need for audit independence']
    }
}

# ============================================================================
# CHAPTER TITLES
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
    2022: {"title": "The $2.61B Question", "tagline": "Tax receivables unverified."},
    2023: {"title": "THE CRISIS DEEPENS", "tagline": "$2.43B tax receivables unconfirmed."},
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
            'Income Tax': 0.33,
            'VAT & Excise': 0.30,
            'Customs & Import': 0.14,
            'Property & Land': 0.08,
            'Other Taxes': 0.06,
            'Non-Tax Revenue': 0.06,
            'Grants & Aid': 0.03
        }
    elif year <= 2012:
        return {
            'Income Tax': 0.29,
            'VAT & Excise': 0.33,
            'Customs & Import': 0.13,
            'Property & Land': 0.07,
            'Other Taxes': 0.07,
            'Non-Tax Revenue': 0.07,
            'Grants & Aid': 0.04
        }
    elif year <= 2017:
        return {
            'Income Tax': 0.26,
            'VAT & Excise': 0.35,
            'Customs & Import': 0.12,
            'Property & Land': 0.07,
            'Other Taxes': 0.08,
            'Non-Tax Revenue': 0.08,
            'Grants & Aid': 0.04
        }
    elif year <= 2020:
        return {
            'Income Tax': 0.24,
            'VAT & Excise': 0.32,
            'Customs & Import': 0.10,
            'Property & Land': 0.07,
            'Other Taxes': 0.09,
            'Non-Tax Revenue': 0.10,
            'Grants & Aid': 0.08
        }
    else:
        return {
            'Income Tax': 0.27,
            'VAT & Excise': 0.34,
            'Customs & Import': 0.12,
            'Property & Land': 0.07,
            'Other Taxes': 0.08,
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
            'Other': 0.03
        }
    elif year <= 2012:
        return {
            'Payroll & Benefits': 0.28,
            'Goods & Services': 0.20,
            'Debt Service': 0.19,
            'Grants & Transfers': 0.15,
            'Capital Expenditure': 0.08,
            'Social Programs': 0.07,
            'Other': 0.03
        }
    elif year <= 2017:
        return {
            'Payroll & Benefits': 0.27,
            'Goods & Services': 0.18,
            'Debt Service': 0.22,
            'Grants & Transfers': 0.16,
            'Capital Expenditure': 0.06,
            'Social Programs': 0.08,
            'Other': 0.03
        }
    elif year <= 2020:
        return {
            'Payroll & Benefits': 0.26,
            'Goods & Services': 0.16,
            'Debt Service': 0.24,
            'Grants & Transfers': 0.17,
            'Capital Expenditure': 0.05,
            'Social Programs': 0.09,
            'Other': 0.03
        }
    else:
        return {
            'Payroll & Benefits': 0.27,
            'Goods & Services': 0.18,
            'Debt Service': 0.22,
            'Grants & Transfers': 0.16,
            'Capital Expenditure': 0.06,
            'Social Programs': 0.08,
            'Other': 0.03
        }

# ============================================================================
# BOOK GENERATOR FUNCTION
# ============================================================================
def generate_book_html():
    """Generate the complete book as an HTML string for download."""
    
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
        <div style="margin-top:8px; font-size:0.8rem; color:#aaa; font-style:italic;">
            Proverbs from "De Mortar-Pestle" by G. Addinton Forde (1987)
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
        <p style="margin-top:10px; font-style:italic; color:#555; font-size:0.9rem;">
            Each chapter opens with a Bajan proverb from <strong>"De Mortar-Pestle"</strong> by G. Addinton Forde (1987),
            a collection of Barbadian proverbs that captures the wisdom of the island's elders.
        </p>
    </div>
    ''')
    
    # Generate chapters
    for year in range(2003, 2027):
        data = FINANCIAL_DATA[year]
        proverb = PROVERBS.get(year, {"text": "", "meaning": "", "page": 0, "why": ""})
        chapter = CHAPTER_TITLES.get(year, {"title": f"Year {year}", "tagline": ""})
        context = YEAR_CONTEXT.get(year, "")
        special = SPECIAL_AUDITS.get(year, {'audits': [], 'issues': []})
        
        opinion_color = "opinion-clean" if data['opinion'] == 'Clean' else "opinion-disclaimer" if data['opinion'] == 'Disclaimer' else "opinion-adverse"
        opinion_emoji = "✅" if data['opinion'] == 'Clean' else "⚠️" if data['opinion'] == 'Disclaimer' else "❌"
        
        book_content.append(f'''
        <div class="chapter">
            <div class="number">Chapter {year - 2002}</div>
            <h3>{chapter['title']}</h3>
            <div style="font-size:0.95rem; color:#666; margin-bottom:4px;">{year}</div>
            <div class="proverb">"{proverb['text']}"</div>
            <div class="proverb-meaning">{proverb['meaning']}</div>
            <div style="font-size:0.7rem; color:#888; margin-bottom:8px;">Source: De Mortar-Pestle, p. {proverb['page']}</div>
            <div style="font-size:0.85rem; color:#555; font-style:italic; margin-bottom:12px; background:#f8f5f0; padding:8px 12px; border-radius:6px; border-left:3px solid #FFC726;">
                <strong>Why this proverb fits {year}:</strong> {proverb['why']}
            </div>
            <div class="metric-grid">
                <div class="metric-item"><div class="label">Revenue</div><div class="value">${data['revenue']:.3f}B</div></div>
                <div class="metric-item"><div class="label">Expenditure</div><div class="value">${data['expenditure']:.3f}B</div></div>
                <div class="metric-item"><div class="label">Deficit</div><div class="value" style="color:{'#10B981' if data['deficit'] >= 0 else '#DC2626'};">{data['deficit']:.3f}B</div></div>
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
    
    # ========================================================================
    # CONCLUSION SECTION WITH SOLUTION PROVERBS
    # ========================================================================
    book_content.append('''
    <div style="margin:50px 0 30px;">
        <h2 style="color:#00267F; font-size:2.2rem; border-bottom:3px solid #FFC726; padding-bottom:6px;">Conclusion: The Path Forward</h2>
        
        <div style="background:#00267F; color:white; padding:25px 30px; border-radius:12px; margin:20px 0; border-left:6px solid #FFC726;">
            <p style="font-size:1.1rem; color:#BFDBFE; margin-bottom:16px;">
                <strong>The question is not "How did we get here?"</strong>
            </p>
            <p style="font-size:1.3rem; font-weight:600; color:#FFC726;">
                The question is: "What are we going to do about it?"
            </p>
            <p style="margin-top:12px; color:#f0f0f0;">
                The Auditor General has done his job. For 20 years, he has flagged the same issues. 
                The government has acknowledged them but has not fixed them.
            </p>
            <p style="color:#f0f0f0;">
                Barbadians deserve to know the state of their country's finances. 
                They deserve a clean audit opinion. They deserve accountability.
            </p>
            <p style="color:#FFC726; font-weight:600; font-size:1.1rem; margin-top:12px;">
                The solutions are not complex. They require discipline, integrity, and follow-through.
            </p>
        </div>
    ''')
    
    # Solution proverbs
    book_content.append('''
        <h3 style="color:#00267F; font-size:1.5rem; margin-top:20px;">💡 Bajan Wisdom for the Way Forward</h3>
        <p style="color:#555; margin-bottom:16px;">
            The wisdom of Barbados' elders, preserved in "De Mortar-Pestle," offers guidance for fixing the financial accountability crisis.
        </p>
    ''')
    
    for sol in SOLUTION_PROVERBS:
        book_content.append(f'''
        <div style="background:#f8f5f0; border-radius:8px; padding:12px 16px; margin:8px 0; border-left:3px solid #10B981;">
            <div style="font-style:italic; color:#00267F; font-weight:600; font-size:1.05rem;">"{sol['text']}"</div>
            <div style="color:#555; font-size:0.85rem;">— {sol['meaning']}</div>
            <div style="color:#00267F; font-size:0.85rem; margin-top:4px; font-weight:500;">✓ {sol['action']}</div>
            <div style="font-size:0.7rem; color:#888; margin-top:2px;">Source: De Mortar-Pestle, p. {sol['page']}</div>
        </div>
        ''')
    
    book_content.append('''
    </div>
    ''')
    
    # Appendices
    book_content.append('''
    <div style="margin:50px 0 30px;">
        <h2 style="color:#00267F; font-size:2.2rem; border-bottom:3px solid #FFC726; padding-bottom:6px;">Appendices</h2>
    </div>
    ''')
    
    # Appendix A - Complete Financial Data
    book_content.append('''
    <div style="margin:30px 0;">
        <h3 style="color:#00267F; font-size:1.5rem;">Appendix A: Complete Financial Data (2003-2026)</h3>
        <table>
            <thead><tr><th>Year</th><th>Revenue</th><th>Expenditure</th><th>Deficit</th><th>Debt</th><th>Debt/GDP</th><th>Opinion</th></tr></thead>
            <tbody>
    ''')
    for year in range(2003, 2027):
        data = FINANCIAL_DATA[year]
        emoji = "✅" if data['opinion'] == 'Clean' else "⚠️" if data['opinion'] == 'Disclaimer' else "❌" if data['opinion'] == 'Adverse' else "⏳"
        book_content.append(f'''
            <tr><td>{year}</td><td>${data['revenue']:.3f}B</td><td>${data['expenditure']:.3f}B</td><td style="color:{'#10B981' if data['deficit'] >= 0 else '#DC2626'};">{data['deficit']:.3f}B</td><td>${data['debt']:.3f}B</td><td>{data['debt_pct']:.1f}%</td><td>{emoji} {data['opinion']}</td></tr>
        ''')
    book_content.append('''
            </tbody>
        </table>
    </div>
    ''')
    
    # Appendix B - All Proverbs with Why They Fit
    book_content.append('''
    <div style="margin:30px 0;">
        <h3 style="color:#00267F; font-size:1.5rem;">Appendix B: Bajan Proverbs from "De Mortar-Pestle"</h3>
        <p style="font-style:italic; color:#555; margin-top:8px;">
            All proverbs are from <strong>"De Mortar-Pestle: A Collection of Barbadian Proverbs"</strong> by G. Addinton Forde (1987).
            Used with attribution.
        </p>
        <table>
            <thead><tr><th>Year</th><th>Proverb</th><th>Meaning</th><th>Why It Fits</th><th>Page</th></tr></thead>
            <tbody>
    ''')
    for year in range(2003, 2027):
        proverb = PROVERBS.get(year, {"text": "", "meaning": "", "page": 0, "why": ""})
        book_content.append(f'''
            <tr>
                <td>{year}</td>
                <td style="font-style:italic;">"{proverb['text']}"</td>
                <td>{proverb['meaning']}</td>
                <td style="font-size:0.8rem; color:#555;">{proverb['why']}</td>
                <td>p. {proverb['page']}</td>
            </tr>
        ''')
    book_content.append('''
            </tbody>
        </table>
    </div>
    ''')
    
    # Appendix C - Solution Proverbs
    book_content.append('''
    <div style="margin:30px 0;">
        <h3 style="color:#00267F; font-size:1.5rem;">Appendix C: Solution Proverbs — The Path Forward</h3>
        <p style="font-style:italic; color:#555; margin-top:8px;">
            Bajan wisdom from "De Mortar-Pestle" applied to the financial accountability crisis.
        </p>
        <table>
            <thead><tr><th>Proverb</th><th>Meaning</th><th>Action for Barbados</th><th>Page</th></tr></thead>
            <tbody>
    ''')
    for sol in SOLUTION_PROVERBS:
        book_content.append(f'''
            <tr>
                <td style="font-style:italic;">"{sol['text']}"</td>
                <td>{sol['meaning']}</td>
                <td style="font-size:0.8rem;">{sol['action']}</td>
                <td>p. {sol['page']}</td>
            </tr>
        ''')
    book_content.append('''
            </tbody>
        </table>
    </div>
    ''')
    
    # Appendix D - Repeating Issues
    book_content.append('''
    <div style="margin:30px 0;">
        <h3 style="color:#00267F; font-size:1.5rem;">Appendix D: Repeating Issues Tracker</h3>
        <table>
            <thead><tr><th>Issue</th><th>First Flagged</th><th>Last Flagged</th><th>Years</th><th>Status</th></tr></thead>
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
    
    # Appendix E - Credits
    book_content.append('''
    <div style="margin:30px 0;">
        <h3 style="color:#00267F; font-size:1.5rem;">Appendix E: Acknowledgments</h3>
        
        <div style="background:#f8f5f0; padding:20px 24px; border-radius:10px; border:2px solid #00267F; margin:20px 0;">
            <h4 style="color:#00267F; margin-bottom:8px;">📖 Author & Compiler</h4>
            <p style="font-weight:700; color:#00267F; font-size:1.1rem;">Matthew A. A. Blackman</p>
            <p style="color:#333;">
                This dashboard and book were researched, compiled, and written by Matthew A. A. Blackman.
                The author spent countless hours analyzing 24 years of Auditor General's reports,
                financial statements, and government documents to piece together the complete
                story of Barbados' financial accountability journey.
            </p>
        </div>
        
        <div style="background:#f8f5f0; padding:20px 24px; border-radius:10px; border:2px solid #FFC726; margin:20px 0;">
            <h4 style="color:#00267F; margin-bottom:8px;">📖 Proverbs — G. Addinton Forde</h4>
            <p style="color:#333;">
                The Bajan proverbs in this book are drawn from the definitive collection:
            </p>
            <p style="font-weight:700; color:#00267F; font-size:1.1rem; margin:8px 0;">
                "De Mortar-Pestle: A Collection of Barbadian Proverbs"<br>
                by G. Addinton Forde<br>
                Published 1987
            </p>
            <p style="color:#333;">
                G. Addinton Forde spent years collecting and documenting these proverbs, ensuring that 
                the wisdom of Barbados' elders would not be lost.
            </p>
            <p style="color:#555; font-style:italic; margin-top:8px;">
                <strong>From Forde's introduction:</strong><br>
                "These proverbs illustrate a profundity of thought, expressed in simple, clear and concise language, 
                with an extraordinary precision in the use of imagery."
            </p>
        </div>
        
        <div style="background:#f8f5f0; padding:20px 24px; border-radius:10px; border:2px solid #00267F; margin:20px 0;">
            <h4 style="color:#00267F; margin-bottom:8px;">🏛️ The Auditor General</h4>
            <p style="font-weight:700; color:#00267F;">Leigh E. Trotman, CPA</p>
            <p style="color:#333;">Auditor General of Barbados (2006-2026)</p>
        </div>
        
        <div style="background:#f8f5f0; padding:20px 24px; border-radius:10px; border:2px solid #8B5CF6; margin:20px 0;">
            <h4 style="color:#00267F; margin-bottom:8px;">🤖 AI Assistance</h4>
            <p style="font-weight:700; color:#00267F;">DeepSeek</p>
            <p style="color:#333;">
                The compilation, organization, and formatting of this dashboard and book were assisted by DeepSeek.
            </p>
            <p style="color:#555; font-size:0.9rem; margin-top:8px;">
                <strong>Disclaimer:</strong> While AI assisted in compilation and formatting, all data comes from 
                official government sources.
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
    
    # Footer
    book_content.append('''
    <div class="footer">
        <div style="font-size:2rem; margin-bottom:8px;">🇧🇧</div>
        <p><strong>How Did We Get Here?</strong></p>
        <p>Barbados' 20-Year Journey from Clean Opinions to Financial Crisis</p>
        <p style="margin-top:8px;">Based on 24 Years of Auditor General's Reports (2003-2026)</p>
        <p style="margin-top:8px; font-size:0.8rem;">
            Author: Matthew A. A. Blackman &nbsp;|&nbsp; Proverbs: G. Addinton Forde, "De Mortar-Pestle" (1987)
        </p>
        <p style="margin-top:8px; font-size:0.7rem; color:#aaa;">
            "Don' wait till de horse get out to shut de stable door." — Bajan Proverb, De Mortar-Pestle, p. 3
        </p>
        <p style="margin-top:4px; font-size:0.7rem; color:#aaa; font-style:italic;">
            Dedicated to the people of Barbados — who deserve accountability.
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
                margin: 8px 0 4px;
            }}
            .chapter .proverb-meaning {{
                font-size: 0.9rem;
                color: #555;
                margin-top: 2px;
                margin-bottom: 4px;
            }}
            .metric-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
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
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 16px 0 20px;
                font-size: 0.85rem;
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
    data = FINANCIAL_DATA[year]
    special = SPECIAL_AUDITS.get(year, {'audits': [], 'issues': []})
    chapter = CHAPTER_TITLES.get(year, {"title": f"Year {year}", "tagline": ""})
    opinion = data['opinion']
    emoji = get_opinion_emoji(opinion)
    color = get_opinion_color(opinion)
    opinion_class = get_chapter_opinion_class(opinion)
    proverb = PROVERBS.get(year, {"text": "", "meaning": "", "page": 0, "why": ""})
    
    audit_count = len(special.get('audits', []))
    critical_count = sum(1 for a in special.get('audits', []) if a.get('severity') == 'Critical')
    
    all_years = list(range(2003, 2027))
    chapter_num = all_years.index(year) + 1
    
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
                <div style="font-style:italic; color:#00267F; font-size:0.9rem; margin:4px 0;">
                    "{proverb['text']}"
                </div>
                <div class="chapter-stats">
                    📊 ${data['revenue']:.2f}B Revenue · {'' if data['deficit'] >= 0 else ''}${data['deficit']:.2f}B Deficit · ${data['debt']:.2f}B Debt
                </div>
                <div class="chapter-stats">
                    📄 {audit_count} special audits · {critical_count} critical issues
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
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
        from crisis to the path forward. Each chapter opens with a Bajan proverb from 
        <strong>"De Mortar-Pestle"</strong> by G. Addinton Forde (1987).
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
    
    # ========================================================================
    # CONCLUSION WITH SOLUTION PROVERBS
    # ========================================================================
    st.markdown("---")
    render_conclusion()

def render_conclusion():
    """Render the conclusion section with solution proverbs."""
    
    st.markdown("""
    <div class="conclusion-section">
        <h2>🇧🇧 Conclusion: The Path Forward</h2>
        <p style="font-size:1.1rem; color:#BFDBFE; margin-bottom:16px;">
            <strong>The question is not "How did we get here?"</strong>
        </p>
        <p class="proverb-text" style="font-size:1.5rem;">
            The question is: "What are we going to do about it?"
        </p>
        <p style="margin-top:12px; color:#f0f0f0;">
            The Auditor General has done his job. For 20 years, he has flagged the same issues. 
            The government has acknowledged them but has not fixed them.
        </p>
        <p style="color:#f0f0f0;">
            Barbadians deserve to know the state of their country's finances. 
            They deserve a clean audit opinion. They deserve accountability.
        </p>
        <p style="color:#FFC726; font-weight:600; font-size:1.1rem; margin-top:12px;">
            The solutions are not complex. They require discipline, integrity, and follow-through.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 💡 Bajan Wisdom for the Way Forward")
    st.markdown("""
    <p style="color:#555; margin-bottom:16px;">
        The wisdom of Barbados' elders, preserved in <strong>"De Mortar-Pestle"</strong> by G. Addinton Forde (1987), 
        offers guidance for fixing the financial accountability crisis.
    </p>
    """, unsafe_allow_html=True)
    
    cols = st.columns(2)
    for i, sol in enumerate(SOLUTION_PROVERBS):
        with cols[i % 2]:
            st.markdown(f"""
            <div style="background:#f8f5f0; border-radius:8px; padding:12px 16px; margin:8px 0; border-left:3px solid #10B981; height:100%;">
                <div style="font-style:italic; color:#00267F; font-weight:600; font-size:1.05rem;">"{sol['text']}"</div>
                <div style="color:#555; font-size:0.85rem;">— {sol['meaning']}</div>
                <div style="color:#00267F; font-size:0.85rem; margin-top:4px; font-weight:500;">✓ {sol['action']}</div>
                <div style="font-size:0.7rem; color:#888; margin-top:2px;">Source: De Mortar-Pestle, p. {sol['page']}</div>
            </div>
            """, unsafe_allow_html=True)

def render_year_view(year):
    data = FINANCIAL_DATA[year]
    special = SPECIAL_AUDITS.get(year, {'audits': [], 'issues': []})
    proverb = PROVERBS.get(year, {"text": "Wisdom comes from experience.", "meaning": "", "page": 0, "why": ""})
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
            <div class="proverb-text">"{proverb['text']}"</div>
            <div class="proverb-meaning">— {proverb['meaning']}</div>
            <div class="proverb-source">Source: "De Mortar-Pestle" by G. Addinton Forde (1987), p. {proverb['page']}</div>
            <div class="proverb-why">💡 <strong>Why this proverb fits:</strong> {proverb['why']}</div>
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
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size:0.65rem;color:#888;">Revenue</div>
            <div class="metric-value">{format_currency_billions(data['revenue'])}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size:0.65rem;color:#888;">Expenditure</div>
            <div class="metric-value">{format_currency_billions(data['expenditure'])}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        deficit_color = "#10B981" if data['deficit'] >= 0 else "#DC2626"
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size:0.65rem;color:#888;">Deficit / Surplus</div>
            <div class="metric-value" style="color:{deficit_color};">{format_currency_billions(abs(data['deficit']))}</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        debt_color = "#DC2626" if data['debt_pct'] > 100 else "#F59E0B" if data['debt_pct'] > 80 else "#10B981"
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size:0.65rem;color:#888;">Public Debt</div>
            <div class="metric-value">{format_currency_billions(data['debt'])}</div>
            <div style="font-size:0.7rem;color:{debt_color};">{data['debt_pct']:.1f}% of GDP</div>
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
        fig = px.pie(rev_df, values='Amount', names='Source', title=f'Revenue Composition ({year})', 
                     color_discrete_sequence=px.colors.sequential.Blues_r, hole=0.4)
        fig.update_traces(textposition='inside', textinfo='percent+label', textfont_size=9)
        fig.update_layout(height=350, margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        exp_breakdown = get_expenditure_breakdown(year)
        exp_data = []
        for category, percentage in exp_breakdown.items():
            exp_data.append({'Category': category, 'Amount': data['expenditure'] * percentage, 'Percentage': percentage * 100})
        exp_df = pd.DataFrame(exp_data)
        fig = px.pie(exp_df, values='Amount', names='Category', title=f'Expenditure Composition ({year})', 
                     color_discrete_sequence=px.colors.sequential.Reds_r, hole=0.4)
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
            elif any(x in issue.lower() for x in ['unverified', 'discrepancy', 'not done', 'failure', 'crisis', 'hidden', 'unconfirmed']):
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
            with st.expander(f"📄 {audit['title']}", expanded=False):
                st.markdown(f"""
                <div style="padding:8px 0;">
                    <div style="font-weight:600;color:#1e293b;font-size:0.9rem;">📋 Summary</div>
                    <div style="color:#475569;font-size:0.9rem;padding-left:12px;padding-bottom:8px;">{audit['summary']}</div>
                    <div style="font-weight:600;color:#1e293b;font-size:0.9rem;">⚡ Severity</div>
                    <div style="color:{'#DC2626' if severity == 'Critical' else '#F59E0B' if severity == 'High' else '#3B82F6'};font-weight:bold;font-size:0.9rem;padding-left:12px;">{severity}</div>
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
    fig.add_trace(go.Scatter(x=all_years, y=revenue_trend, name='Revenue', line=dict(color='#10B981', width=2.5)), secondary_y=False)
    fig.add_trace(go.Scatter(x=all_years, y=debt_trend, name='Debt', line=dict(color='#DC2626', width=2.5, dash='dash')), secondary_y=True)
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

    if st.button("📖 Back to The Full Story", use_container_width=True):
        st.session_state['view_mode'] = 'story'
        st.rerun()

# ============================================================================
# CREDITS SECTION
# ============================================================================
def render_credits():
    st.markdown("""
    <div class="credits-section">
        <h4>📖 About This Dashboard & Book</h4>
        <p style="color:#333; margin-bottom:8px;">
            <strong>Author & Compiler:</strong> Matthew A. A. Blackman
        </p>
        <p style="color:#333; margin-bottom:8px;">
            <strong>Proverbs:</strong> "De Mortar-Pestle: A Collection of Barbadian Proverbs" by G. Addinton Forde (1987)
        </p>
        <p style="color:#333; margin-bottom:8px;">
            <strong>Data Source:</strong> Auditor General's Reports (2003-2024) | Office of the Auditor General, Barbados
        </p>
        <p style="color:#333; margin-bottom:8px;">
            <strong>AI Assistance:</strong> DeepSeek — assisted with compilation, organization, and formatting
        </p>
        <p style="color:#333; margin-bottom:0;">
            <strong>Dedication:</strong> To the people of Barbados — who deserve to know the truth about their country's finances,
            who have a right to accountability, and who have the power to demand change.
        </p>
        <p style="color:#555; font-size:0.8rem; margin-top:10px; font-style:italic; border-top:1px solid #e0d6c8; padding-top:10px;">
            <strong>Note:</strong> All proverbs used in this dashboard are drawn directly from "De Mortar-Pestle" by G. Addinton Forde (1987).
            Each proverb is cited with its page number and includes an explanation of why it fits the specific chapter.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# DOWNLOAD FUNCTIONS
# ============================================================================
def render_download_section():
    st.markdown("---")
    st.markdown("### 📖 Download Options")
    
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
        proverb = PROVERBS.get(year, {"text": "", "meaning": "", "page": 0, "why": ""})
        
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
        st.markdown(f"""
        <div style="background:#f8f9fa;padding:12px;border-radius:8px;margin-bottom:8px;">
            <div style="font-size:0.7rem;color:#888;">Proverb</div>
            <div style="font-size:0.85rem;font-style:italic;color:#00267F;">"{proverb['text']}"</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("---")
        st.markdown(get_era_badge(year), unsafe_allow_html=True)
    
    render_download_section()
    
    st.markdown("---")
    render_credits()

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
**Proverbs:** "De Mortar-Pestle" by G. Addinton Forde (1987) — All proverbs used with attribution
**Author & Compiler:** Matthew A. A. Blackman
**Opinions:** Clean ({clean_count} years: 2003-2007) • Disclaimer ({disclaimer_count} years: 2008-2017) • Adverse ({adverse_count} years: 2018-2023) • Pending ({pending_count} years: 2024-2026)
**Generated:** {datetime.now().strftime('%B %d, %Y %I:%M %p')}
""")