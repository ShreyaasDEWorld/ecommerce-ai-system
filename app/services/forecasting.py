from prophet import Prophet

def train_forecast(df, product_id):
    df = df[df["product_id"] == product_id]

    df = df.rename(columns={
        "date": "ds",
        "orders": "y"
    })

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