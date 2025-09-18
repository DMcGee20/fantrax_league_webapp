import streamlit as st
import plotly.express as px
from mock_data import get_mock_rosters, get_mock_free_agents
from insights import team_strengths, free_agent_targets

st.set_page_config(page_title="Fantasy Baseball Dashboard", layout="wide")
st.title("⚾ Fantasy Baseball Insights Dashboard (Mock Data)")

# Load mock data
roster_df = get_mock_rosters()
fa_df = get_mock_free_agents()

# Team Strengths
st.subheader("📈 Team Strengths Overview")
strengths = team_strengths(roster_df)

fig = px.bar(strengths, x="team", y=["HR", "RBI", "SB", "K"],
             title="Team Offensive/Strikeout Strengths", barmode="group")
st.plotly_chart(fig, use_container_width=True)

# Free Agent Insights
st.subheader("📝 Free Agent Targets")
stat_choice = st.selectbox("Select a stat to optimize:", ["HR", "RBI", "AVG", "SB", "ERA", "K"])
top_fa = free_agent_targets(fa_df, stat=stat_choice)

st.write(f"Top Free Agents by **{stat_choice}**:")
st.dataframe(top_fa)

# Team Roster Browser
st.subheader("🔍 Browse Team Rosters")
team_choice = st.selectbox("Select a team:", roster_df["team"].unique())
st.dataframe(roster_df[roster_df["team"] == team_choice])