def prepare_features(df):

    X = df[[
        "Temperature",
        "Humidity",
        "CO_AQI",
        "NO2_AQI",
        "SO2_AQI"
    ]]

    y = df["AQI"]

    return X, y