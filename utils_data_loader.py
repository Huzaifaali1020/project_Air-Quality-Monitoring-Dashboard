import pandas as pd

def load_data():

    df = pd.read_csv("data/AQM-dataset-updated.csv")

    df["Datetime"] = pd.to_datetime(df["Date"] + " " + df["Time"], dayfirst=True)

    df["AQI"] = df[["CO_AQI","NO2_AQI","SO2_AQI"]].max(axis=1)

    return df