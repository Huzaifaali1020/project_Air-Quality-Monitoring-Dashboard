import streamlit as st
from utils.utils_data_loader import load_data

df = load_data()
st.title("Dataset Overview")
col1,col2,col3,col4 = st.columns(4)

col1.metric("Records",len(df))
col2.metric("Avg Temperature",round(df["Temperature"].mean(),2))
col3.metric("Avg Humidity",round(df["Humidity"].mean(),2))
col4.metric("Avg AQI",round(df["AQI"].mean(),2))

st.divider()
st.subheader("Dataset Preview")
st.dataframe(df.head(20),use_container_width=True)

st.subheader("Dataset Statistics")
st.dataframe(df.describe(),use_container_width=True)