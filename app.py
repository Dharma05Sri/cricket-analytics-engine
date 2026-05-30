import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ==========================================
# 1. ARCHITECTURE & CSS OVERRIDES
# ==========================================
st.set_page_config(page_title="Cricket Chronicles", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    /* Deep Dark Background */
    .stApp { background-color: #050914; color: #E2E8F0; }
    
    /* Neon Gradient Title */
    .main-title {
        font-size: 50px; 
        font-weight: 900;
        text-align: center;
        background: -webkit-linear-gradient(#ff4b4b, #ffaa00);
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px; 
        padding-bottom: 0px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    /* Premium Data Cards */
    .stat-box {
        background: rgba(31, 41, 55, 0.6);
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #00C9FF;
        margin-bottom: 15px;
        box-shadow: 0 4px 15px rgba(0, 201, 255, 0.1);
    }
    
    /* Versus Text */
    .vs-text {
        font-size: 55px;
        font-weight: 900;
        text-align: center;
        color: #ff4b4b;
        padding-top: 25px;
        text-shadow: 0px 0px 15px rgba(255, 75, 75, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🏏 CRICKET CHRONICLES: APEX LEGENDS ARENA</p>', unsafe_allow_html=True)
st.markdown("<center><i>Cross-Generational Data & AI Matchup Simulation</i></center>", unsafe_allow_html=True)
st.write("---")

# ==========================================
# 2. THE EXPANDED DATABASE
# ==========================================
CRICKET_DATABASE = {
    "Classic Era (Pre-1980)": {
        "Sir Don Bradman": {
            "Role": "Batsman",
            "Batting": {"Matches": 52, "Runs": 6996, "Average": 99.94, "Strike Rate": 71.4, "100s": 29, "50s": 13},
            "Bowling": {"Wickets": 2, "Economy": 3.20, "Average": 36.0, "5W": 0},
            "Fielding": {"Catches": 32, "Run Outs": 4},
            "All-Round": {"Rating": 45}
        },
        "Sir Garfield Sobers": {
            "Role": "All-Rounder",
            "Batting": {"Matches": 93, "Runs": 8032, "Average": 57.78, "Strike Rate": 65.2, "100s": 26, "50s": 30},
            "Bowling": {"Wickets": 235, "Economy": 2.22, "Average": 34.03, "5W": 6},
            "Fielding": {"Catches": 109, "Run Outs": 12},
            "All-Round": {"Rating": 98}
        }
    },
    "Golden Era (1980-2010)": {
        "Sachin Tendulkar": {
            "Role": "Batsman",
            "Batting": {"Matches": 200, "Runs": 15921, "Average": 53.78, "Strike Rate": 54.0, "100s": 51, "50s": 68},
            "Bowling": {"Wickets": 46, "Economy": 3.52, "Average": 54.17, "5W": 0},
            "Fielding": {"Catches": 115, "Run Outs": 23},
            "All-Round": {"Rating": 65}
        },
        "Shane Warne": {
            "Role": "Bowler",
            "Batting": {"Matches": 145, "Runs": 3154, "Average": 17.32, "Strike Rate": 48.1, "100s": 0, "50s": 12},
            "Bowling": {"Wickets": 708, "Economy": 2.65, "Average": 25.41, "5W": 37},
            "Fielding": {"Catches": 138, "Run Outs": 15},
            "All-Round": {"Rating": 55}
        }
    },
    "Modern Era (2010-Present)": {
        "Virat Kohli": {
            "Role": "Batsman",
            "Batting": {"Matches": 113, "Runs": 8848, "Average": 49.15, "Strike Rate": 55.6, "100s": 29, "50s": 30},
            "Bowling": {"Wickets": 0, "Economy": 4.20, "Average": 0.0, "5W": 0},
            "Fielding": {"Catches": 111, "Run Outs": 29},
            "All-Round": {"Rating": 30}
        },
        "Ravindra Jadeja": {
            "Role": "All-Rounder",
            "Batting": {"Matches": 72, "Runs": 3130, "Average": 36.39, "Strike Rate": 58.9, "100s": 4, "50s": 20},
            "Bowling": {"Wickets": 294, "Economy": 2.48, "Average": 24.13, "5W": 13},
            "Fielding": {"Catches": 44, "Run Outs": 35},
            "All-Round": {"Rating": 92}
        },
        "Jasprit Bumrah": {
            "Role": "Bowler",
            "Batting": {"Matches": 36, "Runs": 212, "Average": 7.31, "Strike Rate": 51.2, "100s": 0, "50s": 0},
            "Bowling": {"Wickets": 159, "Economy": 2.74, "Average": 20.69, "5W": 10},
            "Fielding": {"Catches": 12, "Run Outs": 5},
            "All-Round": {"Rating": 40}
        }
    }
}

# ==========================================
# 3. CONTROL PANEL (SELECTION)
# ==========================================
col_left, col_space, col_right = st.columns([4, 1, 4])

with col_left:
    st.markdown("### 🟦 PLAYER 1")
    era_1 = st.selectbox("Select Era:", list(CRICKET_DATABASE.keys()), key="era1")
    player_1 = st.selectbox("Select Athlete:", list(CRICKET_DATABASE[era_1].keys()), key="p1")
    p1_data = CRICKET_DATABASE[era_1][player_1]

with col_space:
    st.markdown("<div class='vs-text'>VS</div>", unsafe_allow_html=True)

with col_right:
    st.markdown("### 🟩 PLAYER 2")
    era_2 = st.selectbox("Select Era:", list(CRICKET_DATABASE.keys()), key="era2", index=2)
    player_2 = st.selectbox("Select Athlete:", list(CRICKET_DATABASE[era_2].keys()), key="p2")
    p2_data = CRICKET_DATABASE[era_2][player_2]

st.write("---")

# ==========================================
# 4. TALE OF THE TAPE (POWER METERS)
# ==========================================
st.markdown("### ⚡ TALE OF THE TAPE: All-Round Power Index")
c_pow1, c_pow2 = st.columns(2)
with c_pow1:
    st.markdown(f"**{player_1} ({p1_data['Role']})** - Power: {p1_data['All-Round']['Rating']}/100")
    st.progress(p1_data['All-Round']['Rating'])
with c_pow2:
    st.markdown(f"**{player_2} ({p2_data['Role']})** - Power: {p2_data['All-Round']['Rating']}/100")
    st.progress(p2_data['All-Round']['Rating'])

# ==========================================
# 5. GRAPHICS ENGINE (RADAR)
# ==========================================
categories = ['Batting Avg', 'Strike Rate', '100s Scored', 'Fielding (Catches)', 'Bowling Rating']

# Calculating a dynamic bowling rating based on wickets and economy to make the chart look balanced
p1_bowl_rating = min(100, (p1_data["Bowling"]["Wickets"] / 5) + max(0, (5 - p1_data["Bowling"]["Economy"]) * 10))
p2_bowl_rating = min(100, (p2_data["Bowling"]["Wickets"] / 5) + max(0, (5 - p2_data["Bowling"]["Economy"]) * 10))

p1_radar = [p1_data["Batting"]["Average"], p1_data["Batting"]["Strike Rate"], p1_data["Batting"]["100s"], p1_data["Fielding"]["Catches"] / 2, p1_bowl_rating]
p2_radar = [p2_data["Batting"]["Average"], p2_data["Batting"]["Strike Rate"], p2_data["Batting"]["100s"], p2_data["Fielding"]["Catches"] / 2, p2_bowl_rating]

fig = go.Figure()
fig.add_trace(go.Scatterpolar(r=p1_radar, theta=categories, fill='toself', name=player_1, line_color='#00C9FF', fillcolor='rgba(0, 201, 255, 0.4)'))
fig.add_trace(go.Scatterpolar(r=p2_radar, theta=categories, fill='toself', name=player_2, line_color='#92FE9D', fillcolor='rgba(146, 254, 157, 0.4)'))

fig.update_layout(
    polar=dict(radialaxis=dict(visible=False)),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="#E2E8F0",
    margin=dict(l=20, r=20, t=20, b=20)
)
st.plotly_chart(fig, use_container_width=True)

# ==========================================
# 6. GRANULAR DATA & AI SIMULATOR TABS
# ==========================================
tab1, tab2, tab3, tab4 = st.tabs(["🏏 BATTING", "🥎 BOWLING", "🧤 FIELDING", "🤖 AI MATCHUP SIMULATOR"])

with tab1:
    st.markdown("#### Career Batting Matrix")
    df_bat = pd.DataFrame({
        "Metric": ["Matches", "Total Runs", "Batting Average", "Strike Rate", "Centuries (100s)", "Fifties (50s)"],
        player_1: [p1_data["Batting"]["Matches"], p1_data["Batting"]["Runs"], p1_data["Batting"]["Average"], p1_data["Batting"]["Strike Rate"], p1_data["Batting"]["100s"], p1_data["Batting"]["50s"]],
        player_2: [p2_data["Batting"]["Matches"], p2_data["Batting"]["Runs"], p2_data["Batting"]["Average"], p2_data["Batting"]["Strike Rate"], p2_data["Batting"]["100s"], p2_data["Batting"]["50s"]]
    })
    st.table(df_bat.set_index("Metric"))

with tab2:
    st.markdown("#### Career Bowling Matrix")
    df_bowl = pd.DataFrame({
        "Metric": ["Wickets Taken", "Economy Rate", "Bowling Average", "5-Wicket Hauls"],
        player_1: [p1_data["Bowling"]["Wickets"], p1_data["Bowling"]["Economy"], p1_data["Bowling"]["Average"], p1_data["Bowling"]["5W"]],
        player_2: [p2_data["Bowling"]["Wickets"], p2_data["Bowling"]["Economy"], p2_data["Bowling"]["Average"], p2_data["Bowling"]["5W"]]
    })
    st.table(df_bowl.set_index("Metric"))

with tab3:
    st.markdown("#### Outfield Telemetry")
    df_field = pd.DataFrame({
        "Metric": ["Total Catches", "Direct-Hit Run Outs"],
        player_1: [p1_data["Fielding"]["Catches"], p1_data["Fielding"]["Run Outs"]],
        player_2: [p2_data["Fielding"]["Catches"], p2_data["Fielding"]["Run Outs"]]
    })
    st.table(df_field.set_index("Metric"))

with tab4:
    st.markdown("#### ⚔️ AI Battle Simulator: Batsman vs Bowler")
    st.write("If Player 1 (Batting) faced Player 2 (Bowling) for a 6-ball over, who would win mathematically based on their career stats?")
    
    # AI Math Logic
    p1_bat_power = (p1_data["Batting"]["Average"] * p1_data["Batting"]["Strike Rate"]) / 100
    p2_bowl_power = (p2_data["Bowling"]["Wickets"]) / (p2_data["Bowling"]["Economy"] + 0.1) 
    
    if p2_data["Bowling"]["Wickets"] == 0:
        st.error(f"{player_2} does not have enough bowling stats to run the simulation!")
    elif p1_data["Batting"]["Runs"] == 0:
        st.error(f"{player_1} does not have enough batting stats to run the simulation!")
    else:
        st.divider()
        if p1_bat_power > p2_bowl_power:
            st.success(f"🏏 **ADVANTAGE: {player_1}** - The AI calculates that their aggressive strike rate would overpower {player_2}'s economy.")
        else:
            st.info(f"🥎 **ADVANTAGE: {player_2}** - The AI calculates that their tight economy and wicket-taking ability would dismiss or restrict {player_1}.")
