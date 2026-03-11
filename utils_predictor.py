import joblib
import numpy as np

model = joblib.load("model/aqi_model.pkl")

def predict_aqi(temp, humidity, co, no2, so2):

    data = np.array([[temp, humidity, co, no2, so2]])
    prediction = model.predict(data)

    return prediction[0]