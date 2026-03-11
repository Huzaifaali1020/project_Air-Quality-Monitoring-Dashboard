import streamlit as st
from utils.utils_data_loader import load_data
import plotly.express as px

df = load_data()

st.title("AQI Trend Over Time")

df["Date"] = df["Datetime"].dt.date
daily = df.groupby("Date")["AQI"].mean().reset_index()
fig = px.line(
daily,
x="Date",
y="AQI",
title="Daily AQI Trend",
markers=True
)
st.plotly_chart(fig,use_container_width=True)
st.subheader("Temperature vs AQI")
fig2 = px.scatter(
df,
x="Temperature",
y="AQI",
color="Humidity",
title="Temperature vs AQI"
)
st.plotly_chart(fig2,use_container_width=True)