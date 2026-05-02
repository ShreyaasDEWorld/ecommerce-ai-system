from prophet import Prophet
import pandas as pd

def train_forecast(df, product_id):

    df = df.rename(columns={
        "date": "ds",
        "orders": "y"
    })

    df["ds"] = pd.to_datetime(df["ds"])
    df["y"] = df["y"].astype(float)

    model = Prophet(
        daily_seasonality=True,
        weekly_seasonality=True,
        yearly_seasonality=False
    )

    model.fit(df)

    return model

def predict_forecast(model, days=7):
    future = model.make_future_dataframe(periods=days)
    forecast = model.predict(future)

    return forecast[["ds", "yhat"]].tail(days)