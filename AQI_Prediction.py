import streamlit as st
import pandas as pd
from utils.utils_predictor import predict_aqi
import plotly.graph_objects as go

st.title("AQI Prediction")
st.write("Enter environmental conditions to predict AQI")
col1, col2 = st.columns(2)
with col1:
    temp = st.slider("Temperature (°C)",0,50,25)
    humidity = st.slider("Humidity (%)",0,100,60)
with col2:
    co = st.slider("CO AQI",0,300,50)
    no2 = st.slider("NO2 AQI",0,300,50)
    so2 = st.slider("SO2 AQI",0,300,50)
if st.button("Predict AQI"):

    prediction = predict_aqi(temp,humidity,co,no2,so2)
    st.subheader(f"Predicted AQI: {round(prediction,2)}")

    if prediction <= 50:
        st.success("Air Quality: Good 🟢")
    elif prediction <=100:
        st.warning("Air Quality: Moderate 🟡")
    else:
        st.error("Air Quality: Unhealthy 🔴")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prediction,
        title={'text':"AQI Level"},
        gauge={
            'axis':{'range':[0,500]},
            'bar':{'color':"red"}
        }
    ))
    st.plotly_chart(fig,use_container_width=True)