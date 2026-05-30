import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Set page to wide mode to completely break the old layout style
st.set_page_config(layout="wide")

# Custom Dark Sports-Console Styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stat-box {
        background-color: #1f2937;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #ff4b4b;
        margin-bottom: 10px;
    }
    .vs-text {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        color: #ff4b4b;
        padding-top: 30px;
    }
    </style>
""", unsafe_allowed_html=True)

# 1. THE DATABASE: Multi-Generational Player Profiles
CRICKET_DATABASE = {
    "Classic Era (Pre-1980)": {
        "Sir Don Bradman": {
            "Role": "Batsman",
            "Batting": {"Matches": 52, "Runs": 6996, "Average": 99.94, "Strike Rate": 71.4},
            "Bowling": {"Wickets": 2, "Economy": 3.20, "Average": 36.0},
            "Fielding": {"Catches": 32, "Run Outs": 4},
            "All-Round": {"Rating": 45}
        },
        "Sir Garfield Sobers": {
            "Role": "All-Rounder",
            "Batting": {"Matches": 93, "Runs": 8032, "Average": 57.78, "Strike Rate": 65.2},
            "Bowling": {"Wickets": 235, "Economy": 2.22, "Average": 34.03},
            "Fielding": {"Catches": 109, "Run Outs": 12},
            "All-Round": {"Rating": 98}
        }
    },
    "Golden Era (1980-2010)": {
        "Sachin Tendulkar": {
            "Role": "Batsman",
            "Batting": {"Matches": 200, "Runs": 15921, "Average": 53.78, "Strike Rate": 54.0},
            "Bowling": {"Wickets": 46, "Economy": 3.52, "Average": 54.17},
            "Fielding": {"Catches": 115, "Run Outs": 23},
            "All-Round": {"Rating": 65}
        },
        "Shane Warne": {
            "Role": "Bowler",
            "Batting": {"Matches": 145, "Runs": 3154, "Average": 17.32, "Strike Rate": 48.1},
            "Bowling": {"Wickets": 708, "Economy": 2.65, "Average": 25.41},
            "Fielding": {"Catches": 138, "Run Outs": 15},
            "All-Round": {"Rating": 55}
        }
    },
    "Modern Era (2010-Present)": {
        "Virat Kohli": {
            "Role": "Batsman",
            "Batting": {"Matches": 113, "Runs": 8848, "Average": 49.15, "Strike Rate": 55.6},
            "Bowling": {"Wickets": 0, "Economy": 4.20, "Average": 0.0},
            "Fielding": {"Catches": 111, "Run Outs": 29},
            "All-Round": {"Rating": 30}
        },
        "Ravindra Jadeja": {
            "Role": "All-Rounder",
            "Batting": {"Matches": 72, "Runs": 3130, "Average": 36.39, "Strike Rate": 58.9},
            "Bowling": {"Wickets": 294, "Economy": 2.48, "Average": 24.13},
            "Fielding": {"Catches": 44, "Run Outs": 35},
            "All-Round": {"Rating": 92}
        }
    }
}

# App Title Layout
st.title("⚔️ CRICKET GEN-CROSS ARENA")
st.subheader("Compare historical performance profiles across distinct cricket epochs")
st.write("---")

# 2. CONTROL PANEL LAYOUT (Side-by-Side Selection Columns)
col_left, col_space, col_right = st.columns([4, 1, 4])

with col_left:
    st.markdown("### 🔴 Player 1 Selection")
    era_1 = st.selectbox("Choose Era", list(CRICKET_DATABASE.keys()), key="era1")
    player_1 = st.selectbox("Choose Player", list(CRICKET_DATABASE[era_1].keys()), key="p1")
    p1_data = CRICKET_DATABASE[era_1][player_1]

with col_space:
    st.markdown("<div class='vs-text'>VS</div>", unsafe_allowed_html=True)

with col_right:
    st.markdown("### 🔵 Player 2 Selection")
    era_2 = st.selectbox("Choose Era", list(CRICKET_DATABASE.keys()), key="era2")
    player_2 = st.selectbox("Choose Player", list(CRICKET_DATABASE[era_2].keys()), key="p2")
    p2_data = CRICKET_DATABASE[era_2][player_2]

st.write("---")

# 3. GRAPHICS ENGINE: Parallel Radar Comparison Chart
st.markdown("### 📊 Holistic Attribute Balance")

categories = ['Batting Avg', 'Strike Rate', 'Bowling Econ (Inverted)', 'Fielding RunOuts', 'All-Round Rating']

# Normalizing or plotting raw balanced representations
# For bowling econ, lower is better, so we invert it for visual representation scale (5 - econ)
p1_radar = [p1_data["Batting"]["Average"], p1_data["Batting"]["Strike Rate"], max(0, 6 - p1_data["Bowling"]["Economy"]), p1_data["Fielding"]["Run Outs"], p1_data["All-Round"]["Rating"]]
p2_radar = [p2_data["Batting"]["Average"], p2_data["Batting"]["Strike Rate"], max(0, 6 - p2_data["Bowling"]["Economy"]), p2_data["Fielding"]["Run Outs"], p2_data["All-Round"]["Rating"]]

fig = go.Figure()
fig.add_trace(go.Scatterpolar(r=p1_radar, theta=categories, fill='toself', name=player_1, line_color='#ff4b4b'))
fig.add_trace(go.Scatterpolar(r=p2_radar, theta=categories, fill='toself', name=player_2, line_color='#1f77b4'))

fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 120])),
    template="plotly_dark",
    showlegend=True,
    margin=dict(l=20, r=20, t=20, b=20)
)
st.plotly_chart(fig, use_container_width=True)

# 4. TABULAR DATA COMPARTMENTS (Separating Batting, Bowling, Fielding, All-Round)
st.markdown("### 🗂️ Granular Stats Breakdown")
tab1, tab2, tab3, tab4 = st.tabs(["🏏 Batting Metrics", "🥎 Bowling Metrics", "🧤 Fielding Metrics", "🌟 All-Round Value"])

with tab1:
    st.markdown("#### Career Batting Comparison")
    df_bat = pd.DataFrame({
        "Metric": ["Matches Played", "Total Runs", "Batting Average", "Strike Rate"],
        player_1: [p1_data["Batting"]["Matches"], p1_data["Batting"]["Runs"], p1_data["Batting"]["Average"], p1_data["Batting"]["Strike Rate"]],
        player_2: [p2_data["Batting"]["Matches"], p2_data["Batting"]["Runs"], p2_data["Batting"]["Average"], p2_data["Batting"]["Strike Rate"]]
    })
    st.table(df_bat.set_index("Metric"))

with tab2:
    st.markdown("#### Career Bowling Comparison")
    df_bowl = pd.DataFrame({
        "Metric": ["Wickets Taken", "Economy Rate", "Bowling Average"],
        player_1: [p1_data["Bowling"]["Wickets"], p1_data["Bowling"]["Economy"], p1_data["Bowling"]["Average"]],
        player_2: [p2_data["Bowling"]["Wickets"], p2_data["Bowling"]["Economy"], p2_data["Bowling"]["Average"]]
    })
    st.table(df_bowl.set_index("Metric"))

with tab3:
    st.markdown("#### Defensive & Outfield Performance")
    df_field = pd.DataFrame({
        "Metric": ["Catches Taken", "Direct-Hit Run Outs"],
        player_1: [p1_data["Fielding"]["Catches"], p1_data["Fielding"]["Run Outs"]],
        player_2: [p2_data["Fielding"]["Catches"], p2_data["Fielding"]["Run Outs"]]
    })
    st.table(df_field.set_index("Metric"))

with tab4:
    st.markdown("#### Integrated Utility Matrix")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"<div class='stat-box'><h4>{player_1}</h4>Era Profile: {era_1}<br>Composite All-Round Impact Index: <b>{p1_data['All-Round']['Rating']}/100</b></div>", unsafe_allowed_html=True)
    with c2:
        st.markdown(f"<div class='stat-box'><h4>{player_2}</h4>Era Profile: {era_2}<br>Composite All-Round Impact Index: <b>{p2_data['All-Round']['Rating']}/100</b></div>", unsafe_allowed_html=True)
