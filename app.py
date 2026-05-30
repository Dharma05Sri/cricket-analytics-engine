import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import random

# ==========================================
# 1. CORE ARCHITECTURE & CSS OVERRIDES
# ==========================================
st.set_page_config(page_title="AstraForge Ultimate", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    .stApp { background-color: #030712; color: #F8FAFC; font-family: 'Inter', sans-serif; }
    header { visibility: hidden; }
    
    /* Neon Gradient Headers */
    .title-text {
        font-size: 48px; font-weight: 900;
        background: -webkit-linear-gradient(#00C9FF, #92FE9D);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 0px; padding-bottom: 0px; text-align: center;
    }
    
    /* Premium Glassmorphism Cards */
    div[data-testid="metric-container"] {
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid rgba(0, 201, 255, 0.3);
        padding: 20px; border-radius: 12px;
        box-shadow: 0 8px 32px 0 rgba(0, 201, 255, 0.15);
        backdrop-filter: blur(12px);
    }
    
    /* Simulated Live Red Dot */
    .live-indicator {
        color: #EF4444; font-weight: bold; font-size: 18px;
        animation: blinker 1.5s linear infinite;
    }
    @keyframes blinker { 50% { opacity: 0; } }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title-text">⚡ ASTRAFORGE OS : APEX EDITION</p>', unsafe_allow_html=True)
st.markdown("<center><i>The Complete AI-Powered Cricket Ecosystem</i></center>", unsafe_allow_html=True)
st.divider()

# ==========================================
# 2. THE MASTER DATABASE
# ==========================================
batsmen_db = {
    "Virat Kohli": {"Runs": 4008, "Average": 52.7, "Strike Rate": 137.9, "Sixes": 117, "Fantasy Price": 10.5},
    "Rohit Sharma": {"Runs": 3853, "Average": 31.3, "Strike Rate": 139.2, "Sixes": 182, "Fantasy Price": 10.0},
    "Suryakumar Yadav": {"Runs": 2141, "Average": 45.5, "Strike Rate": 171.5, "Sixes": 123, "Fantasy Price": 9.5},
    "MS Dhoni": {"Runs": 1617, "Average": 37.6, "Strike Rate": 126.1, "Sixes": 52, "Fantasy Price": 8.5},
    "Hardik Pandya": {"Runs": 1348, "Average": 25.4, "Strike Rate": 139.8, "Sixes": 68, "Fantasy Price": 9.0}
}

bowlers_db = {
    "Jasprit Bumrah": {"Wickets": 74, "Economy": 6.55, "Strike Rate": 18.3, "Fantasy Price": 9.5},
    "Rashid Khan": {"Wickets": 130, "Economy": 6.16, "Strike Rate": 14.2, "Fantasy Price": 10.0},
    "Mitchell Starc": {"Wickets": 73, "Economy": 7.66, "Strike Rate": 17.1, "Fantasy Price": 9.0}
}

# ==========================================
# 3. PLATFORM NAVIGATION (5 MEGA-MODULES)
# ==========================================
t1, t2, t3, t4, t5 = st.tabs([
    "🔴 LIVE STUDIO", "📊 GLOBAL TELEMETRY", "⚔️ VERSUS MATRIX", "🧠 AI & FANTASY LAB", "📰 NEWS & COMMUNITY"
])

# ------------------------------------------
# TAB 1: LIVE BROADCAST STUDIO
# ------------------------------------------
with t1:
    st.markdown('<p class="live-indicator">● LIVE MATCH: T20 WORLD CUP FINALS</p>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    
    with c1:
        st.metric(label="IND (Batting)", value="214/4", delta="19.2 Overs")
        st.caption("Current Batsman: S. Yadav (68*)")
    with c2:
        # Simulated Worm Chart (Runs per Over)
        overs = list(range(1, 21))
        ind_runs = [random.randint(5, 15) for _ in range(20)]
        aus_runs = [random.randint(4, 18) for _ in range(15)] + [None]*5
        
        fig_worm = go.Figure()
        fig_worm.add_trace(go.Scatter(x=overs, y=ind_runs, mode='lines+markers', name='IND', line=dict(color='#00C9FF', width=3)))
        fig_worm.add_trace(go.Scatter(x=overs, y=aus_runs, mode='lines+markers', name='AUS (Target: 215)', line=dict(color='#FCD34D', width=3)))
        fig_worm.update_layout(title="Worm Chart: Run Rate Trajectory", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="#E2E8F0", height=300)
        st.plotly_chart(fig_worm, use_container_width=True)
    with c3:
        st.metric(label="AUS (Bowling)", value="Req: --", delta="-4 Wickets", delta_color="inverse")
        st.caption("Current Bowler: M. Starc (2/34)")

# ------------------------------------------
# TAB 2: GLOBAL TELEMETRY (From Previous)
# ------------------------------------------
with t2:
    st.markdown("### 🌐 Active Roster Performance Matrix")
    df_bat = pd.DataFrame.from_dict(batsmen_db, orient='index').reset_index()
    df_bat.rename(columns={'index': 'Player'}, inplace=True)
    
    fig_scatter = px.scatter(
        df_bat, x="Average", y="Strike Rate", size="Runs", color="Player",
        title="Impact Matrix: Average vs Strike Rate",
        template="plotly_dark", size_max=45
    )
    fig_scatter.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig_scatter, use_container_width=True)

# ------------------------------------------
# TAB 3: HEAD-TO-HEAD (From Previous)
# ------------------------------------------
with t3:
    st.markdown("### 🎯 Interactive Radar Matrix")
    colA, colB = st.columns(2)
    with colA: p1 = st.selectbox("🟦 PLAYER 1:", list(batsmen_db.keys()), index=0)
    with colB: p2 = st.selectbox("🟩 PLAYER 2:", list(batsmen_db.keys()), index=1)
    
    stats1 = batsmen_db[p1]
    stats2 = batsmen_db[p2]
    categories = ["Runs", "Average", "Strike Rate", "Sixes"] # Dropped fantasy price for the chart
    
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=[stats1[c] for c in categories], theta=categories, fill='toself', name=p1, line_color='#00C9FF', fillcolor='rgba(0, 201, 255, 0.3)'
    ))
    fig_radar.add_trace(go.Scatterpolar(
        r=[stats2[c] for c in categories], theta=categories, fill='toself', name=p2, line_color='#92FE9D', fillcolor='rgba(146, 254, 157, 0.3)'
    ))
    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=False), angularaxis=dict(color="#E2E8F0")),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="#E2E8F0"
    )
    st.plotly_chart(fig_radar, use_container_width=True)

# ------------------------------------------
# TAB 4: AI PREDICTOR & FANTASY LAB
# ------------------------------------------
with t4:
    col_ai, col_fan = st.columns(2)
    
    with col_ai:
        st.markdown("### 🤖 Matchup AI Predictor")
        target_bat = st.selectbox("Select Batsman:", list(batsmen_db.keys()), key="ai_bat")
        target_bowl = st.selectbox("Select Bowler:", list(bowlers_db.keys()), key="ai_bowl")
        
        bat_sr = batsmen_db[target_bat]["Strike Rate"]
        bowl_econ = bowlers_db[target_bowl]["Economy"]
        
        win_probability = ((bat_sr / 100) * (bowl_econ / 6) * 6 / 12) * 100
        
        st.markdown("#### ⚡ Win Probability Meter")
        st.progress(min(int(win_probability), 100))
        st.info(f"**AI ANALYST INSIGHT:** Based on historical trajectories, {target_bat} has a {round(win_probability, 1)}% chance of dominating a 6-ball over against {target_bowl}. The algorithm suggests bowling wide-yorkers to restrict scoring.")
        
    with col_fan:
        st.markdown("### 🏆 Fantasy Team Builder")
        budget = 30.0
        st.caption(f"Total Budget: {budget} Credits")
        
        all_players = list(batsmen_db.keys()) + list(bowlers_db.keys())
        selected_team = st.multiselect("Draft Your Players:", all_players, max_selections=3)
        
        total_cost = 0.0
        for p in selected_team:
            if p in batsmen_db: total_cost += batsmen_db[p]["Fantasy Price"]
            elif p in bowlers_db: total_cost += bowlers_db[p]["Fantasy Price"]
            
        st.metric(label="Credits Used", value=f"{total_cost} / 30.0", delta=f"{budget - total_cost} Remaining")
        if total_cost > budget:
            st.error("🚨 BUDGET EXCEEDED! Remove a player.")
        elif len(selected_team) == 3:
            st.success("✅ Team Locked. Generating Projected Points...")

# ------------------------------------------
# TAB 5: NEWS, MAGAZINE & COMMUNITY
# ------------------------------------------
with t5:
    st.markdown("### 📰 Digital Sports Magazine")
    n1, n2 = st.columns(2)
    
    with n1:
        st.image("https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="Cinematic Match Highlights")
        st.markdown("#### The Anatomy of a Perfect Cover Drive")
        st.write("AI breakdown of biomechanics in modern cricket. Read how body positioning increases boundary probability by 34%.")
        
    with n2:
        st.markdown("### 📊 Live Community Polls")
        st.write("**Who will be the Player of the Tournament?**")
        st.caption("Virat Kohli (62%)")
        st.progress(62)
        st.caption("Jasprit Bumrah (28%)")
        st.progress(28)
        st.caption("Other (10%)")
        st.progress(10)
        
        st.divider()
        st.markdown("#### 💬 Live Fan Reactions")
        st.write("👤 **@CricketNerd99:** `That worm chart trajectory for IND is insane right now. Momentum shifted entirely in the 14th over.`")
        st.write("👤 **@StatMatrix:** `AI prediction was spot on regarding Starc's economy rate in the death overs.`")
