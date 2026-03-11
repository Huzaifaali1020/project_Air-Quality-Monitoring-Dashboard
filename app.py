import streamlit as st
st.sidebar.markdown("##Developer")
st.sidebar.write("Huzaifa Ali")

st.set_page_config(
    page_title="Air Quality Dashboard",
    layout="wide"
)
st.title("Air Quality Monitoring Dashboard")

st.write("""
This dashboard analyzes air pollution data and predicts
Air Quality Index (AQI) using machine learning.
""")

st.image("data/air-pollution.jpg", width=900)

st.info("Use the sidebar to navigate through different sections.")