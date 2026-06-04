import os
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="FitLens AI",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# CSS
# ==================================================
st.markdown(
    """
    <style>
    .stApp {
        background: #F6F9FF;
        color: #0F172A;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #071A33 0%, #0B2A4D 100%);
    }

    section[data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }

    section[data-testid="stSidebar"] input,
    section[data-testid="stSidebar"] textarea {
        color: #FFFFFF !important;
        background-color: #0B1220 !important;
        border-radius: 12px !important;
    }

    section[data-testid="stSidebar"] div[data-baseweb="select"] {
        background-color: #0B1220 !important;
        border-radius: 12px !important;
    }

    section[data-testid="stSidebar"] div[data-baseweb="select"] * {
        color: #FFFFFF !important;
    }

    section[data-testid="stSidebar"] button {
        color: #FFFFFF !important;
        background-color: #2563EB !important;
        border-color: #2563EB !important;
        border-radius: 999px !important;
        font-weight: 800 !important;
    }

    .hero {
        padding: 26px 30px;
        border-radius: 26px;
        background: linear-gradient(135deg, #FFFFFF 0%, #EAF3FF 100%);
        border: 1px solid #D8E7FF;
        box-shadow: 0 14px 32px rgba(15, 23, 42, 0.08);
        margin-bottom: 20px;
    }

    .hero-eyebrow {
        color: #2563EB;
        font-size: 12px;
        font-weight: 900;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    .hero-title {
        font-size: 40px;
        font-weight: 950;
        line-height: 1.05;
        color: #0B1F3A;
        margin-bottom: 10px;
    }

    .hero-subtitle {
        font-size: 16px;
        color: #334155;
        max-width: 900px;
        line-height: 1.55;
    }

    .hero-message {
        margin-top: 14px;
        padding: 10px 14px;
        border-radius: 999px;
        background: #DBEAFE;
        color: #1D4ED8;
        font-size: 14px;
        font-weight: 900;
        display: inline-block;
    }

    .built-by {
        margin-left: 8px;
        padding: 10px 14px;
        border-radius: 999px;
        background: #FFFFFF;
        color: #1D4ED8;
        font-size: 13px;
        font-weight: 800;
        border: 1px solid #CFE3FF;
        display: inline-block;
    }

    .section-title {
        color: #0B1F3A;
        font-size: 22px;
        font-weight: 950;
        margin-top: 12px;
        margin-bottom: 6px;
    }

    .section-caption {
        color: #64748B;
        font-size: 14px;
        margin-bottom: 14px;
    }

    .metric-card {
        padding: 18px;
        border-radius: 20px;
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        box-shadow: 0 8px 22px rgba(15, 23, 42, 0.05);
        min-height: 112px;
        margin-bottom: 12px;
    }

    .metric-label {
        font-size: 12px;
        color: #64748B;
        font-weight: 900;
        margin-bottom: 6px;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }

    .metric-value {
        font-size: 25px;
        color: #0B1F3A;
        font-weight: 950;
        margin-bottom: 3px;
    }

    .metric-note {
        font-size: 12px;
        color: #64748B;
        line-height: 1.4;
    }

    .creator-card {
        padding: 20px;
        border-radius: 24px;
        background: #FFFFFF;
        border: 1px solid #DCEBFF;
        box-shadow: 0 10px 28px rgba(37, 99, 235, 0.08);
        min-height: 270px;
        margin-bottom: 12px;
    }

    .creator-card-best {
        border: 2px solid #2563EB;
        box-shadow: 0 16px 34px rgba(37, 99, 235, 0.16);
    }

    .creator-handle {
        color: #0B1F3A;
        font-size: 22px;
        font-weight: 950;
        margin-bottom: 4px;
    }

    .creator-platform {
        color: #64748B;
        font-size: 13px;
        margin-bottom: 12px;
    }

    .pill {
        display: inline-block;
        padding: 7px 11px;
        border-radius: 999px;
        font-weight: 900;
        font-size: 12px;
        margin-right: 5px;
        margin-bottom: 7px;
    }

    .pill-blue {
        background: #DBEAFE;
        color: #1D4ED8;
    }

    .pill-purple {
        background: #F3E8FF;
        color: #7E22CE;
    }

    .pill-teal {
        background: #CCFBF1;
        color: #0F766E;
    }

    .risk-low {
        background: #DCFCE7;
        color: #047857;
    }

    .risk-medium {
        background: #FEF3C7;
        color: #B45309;
    }

    .risk-high {
        background: #FEE2E2;
        color: #B91C1C;
    }

    .small-label {
        color: #64748B;
        font-size: 11px;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-top: 12px;
        margin-bottom: 3px;
    }

    .small-text {
        color: #334155;
        font-size: 13px;
        line-height: 1.45;
    }

    .decision-box {
        padding: 18px 20px;
        border-radius: 22px;
        background: linear-gradient(135deg, #0B1F3A 0%, #1D4ED8 100%);
        color: white;
        box-shadow: 0 14px 30px rgba(29, 78, 216, 0.20);
        margin: 14px 0 20px 0;
    }

    .decision-box h3 {
        color: white;
        margin-bottom: 8px;
    }

    .decision-box p {
        color: #EAF3FF;
        font-size: 14px;
        line-height: 1.55;
    }

    .warning-box {
        padding: 16px 18px;
        border-radius: 20px;
        background: #FFF7ED;
        border: 1px solid #FED7AA;
        color: #9A3412;
        margin-bottom: 14px;
    }

    .success-box {
        padding: 14px 18px;
        border-radius: 18px;
        background: #ECFDF5;
        border: 1px solid #BBF7D0;
        color: #047857;
        font-weight: 800;
        margin-bottom: 16px;
    }

    .api-box {
        padding: 20px;
        border-radius: 22px;
        background: #FFFFFF;
        border: 1px solid #DCEBFF;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.05);
        margin-bottom: 14px;
    }

    div[data-testid="stDataFrame"] {
        border-radius: 18px;
        overflow: hidden;
        border: 1px solid #E2E8F0;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.05);
    }

    .stButton > button {
        border-radius: 999px;
        border: 1px solid #2563EB;
        background: #2563EB;
        color: white;
        font-weight: 850;
        padding: 0.58rem 1.2rem;
    }

    .stButton > button:hover {
        background: #1D4ED8;
        border-color: #1D4ED8;
        color: white;
    }

    .footer {
        padding: 18px;
        border-radius: 20px;
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        color: #64748B;
        font-size: 13px;
        margin-top: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==================================================
# Load data
# ==================================================
@st.cache_data
def load_creators():
    return pd.read_csv("creators.csv")

creators = load_creators()

# ==================================================
# Sidebar setup
# ==================================================
with st.sidebar:
    logo_path = "assets/logo.png"

    if os.path.exists(logo_path):
        st.image(logo_path, use_container_width=True)
    else:
        st.markdown(
            """
            <div style="padding: 18px 0 24px 0;">
                <div style="font-size: 30px; font-weight: 950; color: #FFFFFF;">FitLens AI</div>
                <div style="font-size: 13px; color: #BFDBFE; margin-top: 6px;">Built by Jen Kim</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")
    st.header("Campaign Setup")

    brand_name = st.text_input("Brand name", "COSRX")

    product_focus = st.selectbox(
        "Product focus",
        ["Acne care", "Sensitive skin", "Hydration", "Exfoliation", "K-beauty routine"]
    )

    campaign_goal = st.selectbox(
        "Campaign goal",
        ["Sales", "Product Education", "Awareness", "UGC"]
    )

    target_country = st.selectbox(
        "Target country",
        ["France", "United States", "United Kingdom", "South Korea"]
    )

    target_audience = st.selectbox(
        "Target audience",
        ["Women 18–34", "Women 25–40", "General skincare audience"]
    )

    brand_tone = st.text_input(
        "Brand tone",
        "clinical, honest, minimal"
    )

    budget = st.number_input(
        "Campaign budget (€)",
        min_value=500,
        max_value=50000,
        value=5000,
        step=500
    )

    generate_clicked = st.button("Generate Creator Shortlist", use_container_width=True)

campaign = {
    "brand_name": brand_name,
    "brand_type": "Korean skincare brand",
    "product_focus": product_focus,
    "product_category": "Skincare / Beauty",
    "campaign_goal": campaign_goal,
    "target_country": target_country,
    "target_audience": target_audience,
    "brand_tone": brand_tone,
    "budget": budget
}

# ==================================================
# Scoring logic
# ==================================================
def calculate_audience_match(row, target_country, target_audience):
    country_score = row["audience_france_pct"] if target_country == "France" else 50

    if "Women 18" in target_audience:
        audience_score = row["audience_women_18_34_pct"]
    elif "Women 25" in target_audience:
        audience_score = max(row["audience_women_18_34_pct"] - 5, 50)
    else:
        audience_score = 65

    return round((country_score + audience_score) / 2)


def calculate_skincare_relevance(row, product_focus):
    base_score = row["skincare_relevance"]
    tags = str(row["product_focus_tags"]).lower()
    focus = product_focus.lower()

    bonus = 0

    if "acne" in focus and "acne" in tags:
        bonus += 8
    if "sensitive" in focus and "sensitive" in tags:
        bonus += 8
    if "hydration" in focus and "hydration" in tags:
        bonus += 8
    if "exfoliation" in focus and "exfoliation" in tags:
        bonus += 8
    if "k-beauty" in focus and "k-beauty" in tags:
        bonus += 8

    return round(min(base_score + bonus, 100))


def calculate_content_match(row, brand_tone):
    creator_style = str(row["content_style"]).lower()
    tone_words = brand_tone.lower().replace(",", " ").split()

    match_count = 0

    for word in tone_words:
        if word in creator_style:
            match_count += 1

    if match_count >= 2:
        return 92
    if match_count == 1:
        return 78
    return 58


def calculate_performance_score(row, campaign_goal):
    engagement_score = min(row["engagement_rate"] * 12, 100)
    roi_score = min(row["previous_roi"] * 22, 100)
    follower_score = min(row["followers"] / 2500, 100)

    if campaign_goal == "Sales":
        score = roi_score * 0.50 + engagement_score * 0.35 + follower_score * 0.15
    elif campaign_goal == "Product Education":
        score = engagement_score * 0.40 + roi_score * 0.30 + row["skincare_relevance"] * 0.30
    elif campaign_goal == "Awareness":
        score = follower_score * 0.55 + engagement_score * 0.25 + roi_score * 0.20
    else:
        response_score = max(100 - row["avg_response_time_hours"] * 2, 20)
        score = engagement_score * 0.35 + response_score * 0.35 + row["skincare_relevance"] * 0.30

    return round(min(score, 100))


def calculate_risk(row, budget, audience_score, skincare_score):
    risk_points = 0
    reasons = []

    brand_flag = str(row["brand_safety_flag"]).lower() == "true"

    if brand_flag:
        risk_points += 40
        reasons.append("brand safety flag")

    if row["engagement_rate"] < 2:
        risk_points += 20
        reasons.append("low engagement rate")

    if row["estimated_cost"] > budget * 0.35:
        risk_points += 20
        reasons.append("high cost compared to campaign budget")

    if row["avg_response_time_hours"] > 24:
        risk_points += 10
        reasons.append("slow response time")

    if audience_score < 55:
        risk_points += 15
        reasons.append("weak audience match")

    if skincare_score < 60:
        risk_points += 15
        reasons.append("weak skincare relevance")

    if risk_points >= 40:
        return "High", reasons
    if risk_points >= 20:
        return "Medium", reasons
    return "Low", reasons


def calculate_fit_score(audience, skincare, content, performance, risk_level, campaign_goal):
    if campaign_goal == "Sales":
        weights = {"audience": 0.30, "skincare": 0.25, "content": 0.15, "performance": 0.25, "base": 0.05}
    elif campaign_goal == "Product Education":
        weights = {"audience": 0.25, "skincare": 0.35, "content": 0.25, "performance": 0.10, "base": 0.05}
    elif campaign_goal == "Awareness":
        weights = {"audience": 0.30, "skincare": 0.15, "content": 0.15, "performance": 0.35, "base": 0.05}
    else:
        weights = {"audience": 0.20, "skincare": 0.25, "content": 0.30, "performance": 0.20, "base": 0.05}

    risk_adjustment = {"Low": 0, "Medium": -8, "High": -22}

    score = (
        audience * weights["audience"]
        + skincare * weights["skincare"]
        + content * weights["content"]
        + performance * weights["performance"]
        + 82 * weights["base"]
    )

    score += risk_adjustment[risk_level]
    return round(max(min(score, 100), 0))


def recommend_collaboration(row, campaign_goal, risk_level):
    if risk_level == "High":
        return "Manual review first"

    if campaign_goal == "Sales":
        if row["previous_roi"] >= 3 and row["engagement_rate"] >= 4:
            return "Gifting + affiliate"
        return "Affiliate-only test"

    if campaign_goal == "Product Education":
        return "Seeding + education brief"

    if campaign_goal == "Awareness":
        if row["followers"] >= 100000:
            return "Paid post + usage rights"
        return "Gifting + awareness content"

    return "Product gifting + UGC"


def suggested_next_action(fit_score, risk_level):
    if risk_level == "High":
        return "Review manually"
    if fit_score >= 85:
        return "Invite"
    if fit_score >= 72:
        return "Backup"
    return "Do not prioritize"


def assign_creator_role(row, campaign_goal):
    if campaign_goal == "Product Education":
        if row["skincare_relevance"] >= 90:
            return "Education Creator"
        return "Support Creator"

    if campaign_goal == "Sales":
        if row["previous_roi"] >= 3.5:
            return "Conversion Driver"
        return "Affiliate Test"

    if campaign_goal == "Awareness":
        if row["followers"] >= 100000:
            return "Awareness Booster"
        return "Niche Awareness"

    if row["avg_response_time_hours"] <= 10:
        return "UGC Candidate"

    return "Content Backup"


def evaluate_creators(creators_df, campaign):
    results = []

    for _, row in creators_df.iterrows():
        audience_score = calculate_audience_match(row, campaign["target_country"], campaign["target_audience"])
        skincare_score = calculate_skincare_relevance(row, campaign["product_focus"])
        content_score = calculate_content_match(row, campaign["brand_tone"])
        performance_score = calculate_performance_score(row, campaign["campaign_goal"])
        risk_level, risk_reasons = calculate_risk(row, campaign["budget"], audience_score, skincare_score)

        fit_score = calculate_fit_score(
            audience_score,
            skincare_score,
            content_score,
            performance_score,
            risk_level,
            campaign["campaign_goal"]
        )

        results.append({
            "creator_id": row["creator_id"],
            "handle": row["handle"],
            "platform": row["platform"],
            "followers": row["followers"],
            "engagement_rate": row["engagement_rate"],
            "category": row["category"],
            "audience_france_pct": row["audience_france_pct"],
            "audience_women_18_34_pct": row["audience_women_18_34_pct"],
            "skincare_relevance": row["skincare_relevance"],
            "product_focus_tags": row["product_focus_tags"],
            "content_style": row["content_style"],
            "previous_roi": row["previous_roi"],
            "avg_response_time_hours": row["avg_response_time_hours"],
            "estimated_cost": row["estimated_cost"],
            "brand_safety_flag": row["brand_safety_flag"],
            "audience_match": audience_score,
            "skincare_relevance_score": skincare_score,
            "content_match": content_score,
            "performance_score": performance_score,
            "risk_level": risk_level,
            "risk_reasons": risk_reasons,
            "fit_score": fit_score,
            "recommended_collaboration": recommend_collaboration(row, campaign["campaign_goal"], risk_level),
            "suggested_action": suggested_next_action(fit_score, risk_level),
            "creator_role": assign_creator_role(row, campaign["campaign_goal"])
        })

    return pd.DataFrame(results).sort_values(by="fit_score", ascending=False).reset_index(drop=True)


def risk_class(risk_level):
    if risk_level == "Low":
        return "risk-low"
    if risk_level == "Medium":
        return "risk-medium"
    return "risk-high"


def generate_rule_based_explanation(row, campaign, selected_result):
    risk_reasons = selected_result["risk_reasons"]
    risk_text = ", ".join(risk_reasons) if risk_reasons else "no major risk signal detected"

    return f"""
### Creator Fit Explanation

**{row['handle']}** was evaluated for the **{campaign['brand_name']} {campaign['product_focus']} campaign**.

**Why this creator may fit**
- Audience fit: **{row['audience_france_pct']}% France-based audience** and **{row['audience_women_18_34_pct']}% women aged 18–34**.
- Skincare relevance: **{selected_result['skincare_relevance_score']}/100**, based on category and product focus tags.
- Content style: **{row['content_style']}**, compared with COSRX's brand tone: **{campaign['brand_tone']}**.
- Performance signal: **{row['engagement_rate']}% engagement rate** and **{row['previous_roi']}x previous ROI**.

**Risk check**  
Risk level is **{selected_result['risk_level']}**. Main signal: **{risk_text}**.

**Recommended collaboration**  
{selected_result['recommended_collaboration']}

**Suggested next action**  
{selected_result['suggested_action']}
"""


def generate_ai_explanation(row, campaign, selected_result):
    try:
        from openai import OpenAI

        api_key = st.secrets.get("OPENAI_API_KEY", None)

        if not api_key:
            raise ValueError("OPENAI_API_KEY is missing.")

        client = OpenAI(api_key=api_key)

        prompt = f"""
You are an AI product assistant for an influencer marketing platform.

Evaluate this creator applicant for a COSRX skincare campaign.

Campaign:
- Brand: {campaign['brand_name']}
- Brand type: {campaign['brand_type']}
- Product focus: {campaign['product_focus']}
- Goal: {campaign['campaign_goal']}
- Target country: {campaign['target_country']}
- Target audience: {campaign['target_audience']}
- Brand tone: {campaign['brand_tone']}
- Budget: €{campaign['budget']}

Creator:
- Handle: {row['handle']}
- Platform: {row['platform']}
- Followers: {row['followers']}
- Engagement rate: {row['engagement_rate']}%
- Category: {row['category']}
- Audience France: {row['audience_france_pct']}%
- Audience women 18-34: {row['audience_women_18_34_pct']}%
- Skincare relevance: {row['skincare_relevance']}/100
- Product focus tags: {row['product_focus_tags']}
- Content style: {row['content_style']}
- Previous ROI: {row['previous_roi']}x
- Estimated cost: €{row['estimated_cost']}
- Brand safety flag: {row['brand_safety_flag']}

Evaluation:
- Fit Score: {selected_result['fit_score']}/100
- Audience Match: {selected_result['audience_match']}/100
- Skincare Relevance Score: {selected_result['skincare_relevance_score']}/100
- Content Match: {selected_result['content_match']}/100
- Performance Potential: {selected_result['performance_score']}/100
- Risk Level: {selected_result['risk_level']}
- Risk Reasons: {selected_result['risk_reasons']}
- Recommended Collaboration: {selected_result['recommended_collaboration']}
- Suggested Action: {selected_result['suggested_action']}

Write a concise evaluation with:
1. Fit explanation
2. Main strengths
3. Main risks
4. Recommended collaboration model
5. Suggested next action

Do not invent metrics.
Explain why this reduces creator selection risk.
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a concise Data/AI product assistant for creator-brand fit evaluation."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.35,
            max_tokens=550
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"""
### AI Explanation Unavailable

Reason: {e}

Below is the rule-based fallback explanation:

{generate_rule_based_explanation(row, campaign, selected_result)}
"""

# ==================================================
# Session state
# ==================================================
if "generated" not in st.session_state:
    st.session_state.generated = False

if "results_df" not in st.session_state:
    st.session_state.results_df = evaluate_creators(creators, campaign)

if generate_clicked:
    st.session_state.generated = True
    st.session_state.results_df = evaluate_creators(creators, campaign)

results_df = st.session_state.results_df

# ==================================================
# Header
# ==================================================
st.markdown(
    """
    <div class="hero">
        <div class="hero-eyebrow">Data/AI Product Manager Portfolio MVP</div>
        <div class="hero-title">FitLens AI</div>
        <div class="hero-subtitle">
            A campaign dashboard that helps brands choose the right creators with explainable AI.
            This demo evaluates creator applicants for a COSRX skincare campaign using audience fit,
            skincare relevance, content style, performance signals, and risk indicators.
        </div>
        <div class="hero-message">Not just who to choose — why they are the right choice.</div>
        <div class="built-by">Built by Jen Kim · Lyon, France</div>
    </div>
    """,
    unsafe_allow_html=True
)

# ==================================================
# Tabs
# ==================================================
tab_dashboard, tab_detail, tab_api = st.tabs(["Dashboard", "Creator Detail", "Data & API Design"])

# ==================================================
# Dashboard tab
# ==================================================
with tab_dashboard:
    if st.session_state.generated:
        st.markdown(
            f"""
            <div class="success-box">
                Shortlist generated for {brand_name} · {product_focus} · {campaign_goal}.
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <div class="warning-box">
                Set campaign criteria on the left, then click <strong>Generate Creator Shortlist</strong>.
                The Top 3 recommendation will update immediately here.
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="section-title">Campaign Overview</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">Brand</div>
                <div class="metric-value">{brand_name}</div>
                <div class="metric-note">Korean skincare brand</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">Product Focus</div>
                <div class="metric-value">{product_focus}</div>
                <div class="metric-note">Recommendation logic adapts to this focus</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">Campaign Goal</div>
                <div class="metric-value">{campaign_goal}</div>
                <div class="metric-note">Weights change by objective</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">Market</div>
                <div class="metric-value">{target_country}</div>
                <div class="metric-note">{target_audience}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="section-title">Recommended Shortlist</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">Top creators ranked by fit score, risk level, skincare relevance, and campaign objective.</div>',
        unsafe_allow_html=True
    )

    top3 = results_df.head(3)
    cols = st.columns(3)

    for i, (_, creator) in enumerate(top3.iterrows()):
        best_class = "creator-card creator-card-best" if i == 0 else "creator-card"

        with cols[i]:
            st.markdown(
                f"""
                <div class="{best_class}">
                    <span class="pill pill-blue">{creator['creator_role']}</span>
                    <div class="creator-handle">{creator['handle']}</div>
                    <div class="creator-platform">{creator['platform']} · {creator['category']}</div>
                    <span class="pill pill-blue">{creator['fit_score']}/100 Fit</span>
                    <span class="pill pill-purple">{creator['skincare_relevance_score']}/100 Skincare</span>
                    <span class="pill pill-teal">{creator['performance_score']}/100 Performance</span>
                    <span class="pill {risk_class(creator['risk_level'])}">{creator['risk_level']} Risk</span>
                    <div class="small-label">Recommended model</div>
                    <div class="small-text">{creator['recommended_collaboration']}</div>
                    <div class="small-label">Next action</div>
                    <div class="small-text"><strong>{creator['suggested_action']}</strong></div>
                </div>
                """,
                unsafe_allow_html=True
            )

    shortlist_names = ", ".join(top3["handle"].tolist())
    best_creator = top3.iloc[0]

    st.markdown(
        f"""
        <div class="decision-box">
            <h3>Decision Summary</h3>
            <p>
                Recommended shortlist: <strong>{shortlist_names}</strong>. 
                The strongest fit is <strong>{best_creator['handle']}</strong> with a score of 
                <strong>{best_creator['fit_score']}/100</strong>. 
                This recommendation is based on COSRX campaign goals, skincare relevance, audience alignment,
                performance potential, and risk signals.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="section-title">Applicant Snapshot</div>', unsafe_allow_html=True)

    applicants_count = len(results_df)
    average_fit = round(results_df["fit_score"].mean())
    low_risk_count = len(results_df[results_df["risk_level"] == "Low"])
    high_risk_count = len(results_df[results_df["risk_level"] == "High"])

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">Applicants</div>
                <div class="metric-value">{applicants_count}</div>
                <div class="metric-note">Total creator applicants</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with m2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">Average Fit</div>
                <div class="metric-value">{average_fit}/100</div>
                <div class="metric-note">Average creator fit score</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with m3:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">Low Risk</div>
                <div class="metric-value" style="color:#047857;">{low_risk_count}</div>
                <div class="metric-note">Creators ready for shortlist</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with m4:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">High Risk</div>
                <div class="metric-value" style="color:#B91C1C;">{high_risk_count}</div>
                <div class="metric-note">Creators needing review</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    table_df = results_df.copy()

    table_df["Followers"] = table_df["followers"].apply(lambda x: f"{x:,}")
    table_df["Engagement"] = table_df["engagement_rate"].apply(lambda x: f"{x:.1f}%")
    table_df["Fit"] = table_df["fit_score"].apply(lambda x: f"{x}/100")
    table_df["Skincare"] = table_df["skincare_relevance_score"].apply(lambda x: f"{x}/100")
    table_df["Audience"] = table_df["audience_match"].apply(lambda x: f"{x}/100")
    table_df["Cost"] = table_df["estimated_cost"].apply(lambda x: f"€{x:,}")

    display_df = table_df[
        [
            "handle",
            "creator_role",
            "platform",
            "category",
            "Followers",
            "Engagement",
            "Fit",
            "Skincare",
            "Audience",
            "risk_level",
            "Cost",
            "suggested_action"
        ]
    ].rename(
        columns={
            "handle": "Creator",
            "creator_role": "Role",
            "platform": "Platform",
            "category": "Category",
            "risk_level": "Risk",
            "suggested_action": "Action"
        }
    )

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

# ==================================================
# Creator detail tab
# ==================================================
with tab_detail:
    st.markdown('<div class="section-title">Creator Detail</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">Select a creator to understand why they are a strong or risky choice for this campaign.</div>',
        unsafe_allow_html=True
    )

    selected_creator = st.selectbox(
        "Select creator",
        results_df["handle"].tolist()
    )

    selected_row = creators[creators["handle"] == selected_creator].iloc[0]
    selected_result = results_df[results_df["handle"] == selected_creator].iloc[0]

    d1, d2 = st.columns([1, 2])

    with d1:
        st.markdown(
            f"""
            <div class="creator-card creator-card-best">
                <div class="creator-handle">{selected_result['handle']}</div>
                <div class="creator-platform">{selected_result['platform']} · {selected_result['category']}</div>
                <span class="pill pill-blue">{selected_result['fit_score']}/100 Fit</span>
                <span class="pill pill-purple">{selected_result['skincare_relevance_score']}/100 Skincare</span>
                <span class="pill pill-teal">{selected_result['performance_score']}/100 Performance</span>
                <span class="pill {risk_class(selected_result['risk_level'])}">{selected_result['risk_level']} Risk</span>
                <div class="small-label">Audience Match</div>
                <div class="small-text">{selected_result['audience_match']}/100</div>
                <div class="small-label">Content Match</div>
                <div class="small-text">{selected_result['content_match']}/100</div>
                <div class="small-label">Estimated Cost</div>
                <div class="small-text">€{selected_result['estimated_cost']:,}</div>
                <div class="small-label">Suggested Action</div>
                <div class="small-text"><strong>{selected_result['suggested_action']}</strong></div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with d2:
        use_ai = st.checkbox("Use OpenAI API explanation", value=False)

        if st.button("Explain this creator"):
            with st.spinner("Generating explanation..."):
                if use_ai:
                    explanation = generate_ai_explanation(selected_row, campaign, selected_result)
                else:
                    explanation = generate_rule_based_explanation(selected_row, campaign, selected_result)
                st.markdown(explanation)
        else:
            st.markdown(generate_rule_based_explanation(selected_row, campaign, selected_result))

    st.markdown('<div class="section-title">Campaign Actions</div>', unsafe_allow_html=True)

    a1, a2, a3, a4 = st.columns(4)

    with a1:
        if st.button("Invite", key="invite_detail"):
            st.success(f"{selected_creator} has been added to the invite list.")

    with a2:
        if st.button("Backup", key="backup_detail"):
            st.info(f"{selected_creator} has been saved as backup.")

    with a3:
        if st.button("Request Media Kit", key="media_detail"):
            st.info(f"Media kit request prepared for {selected_creator}.")

    with a4:
        if st.button("Reject", key="reject_detail"):
            st.warning(f"{selected_creator} has been marked as not prioritized.")

# ==================================================
# API tab
# ==================================================
with tab_api:
    st.markdown('<div class="section-title">Data & API Design</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">This section is included to show API/data thinking for a Data/AI Product Manager role.</div>',
        unsafe_allow_html=True
    )

    api1, api2 = st.columns(2)

    with api1:
        st.markdown(
            """
            <div class="api-box">
                <h4>Simulated API Inputs</h4>
                <p><strong>Creator Metrics API</strong><br/>
                followers, engagement rate, audience demographics, category, content style, skincare relevance</p>
                <p><strong>Campaign Brief API</strong><br/>
                brand, product focus, campaign goal, target audience, budget, tone</p>
                <p><strong>Risk Signals</strong><br/>
                brand safety flag, weak audience match, low engagement, high cost, weak skincare relevance</p>
                <p><strong>OpenAI API</strong><br/>
                converts structured scoring output into explainable creator fit and risk recommendations</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with api2:
        st.markdown(
            """
            <div class="api-box">
                <h4>Production API Concept</h4>
                <p><code>GET /api/creators</code></p>
                <p><code>GET /api/campaigns/{campaign_id}/applicants</code></p>
                <p><code>POST /api/evaluations</code></p>
                <p><code>POST /api/ai/explanations</code></p>
                <p>
                In production, this MVP could consume REST APIs with OAuth2 authentication and JSON responses
                from creator metrics, campaign management, and AI explanation services.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.info(
        """
        Product principle: AI should not blindly replace creator selection. 
        FitLens uses structured data and scoring logic first, then uses AI to make the recommendation explainable, consistent, and risk-aware.
        """
    )

    st.markdown(
        """
        <div class="footer">
            © 2026 Jen Kim. Portfolio MVP built for a Data/AI Product Manager application.
            This project demonstrates product thinking, API-ready data design, scoring logic, risk detection,
            and AI-powered explanation for influencer marketing marketplaces.
        </div>
        """,
        unsafe_allow_html=True
    )