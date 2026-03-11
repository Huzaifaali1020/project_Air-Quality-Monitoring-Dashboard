import streamlit as st
from utils.utils_data_loader import load_data
import plotly.express as px

df = load_data()
st.title("Pollution Analysis")

pollutant = st.selectbox(
"Select Pollutant",
["CO_AQI","NO2_AQI","SO2_AQI"]
)

fig = px.histogram(
df,
x=pollutant,
nbins=40,
title=f"{pollutant} Distribution"
)
st.plotly_chart(fig,use_container_width=True)
st.subheader("Pollutant Comparison")
fig2 = px.box(
df,
y=["CO_AQI","NO2_AQI","SO2_AQI"],
title="Pollutant Spread"
)

st.plotly_chart(fig2,use_container_width=True)

st.subheader("Correlation Heatmap")
corr = df[["Temperature","Humidity","CO_AQI","NO2_AQI","SO2_AQI","AQI"]].corr()

fig3 = px.imshow(
corr,
text_auto=True,
color_continuous_scale="RdBu"
)
st.plotly_chart(fig3,use_container_width=True)