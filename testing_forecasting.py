import joblib
from app.services.forecasting import predict_forecast
from app.services.delay_model import train_delay_model

model = joblib.load("models/forecast_P1.pkl")

forecast = predict_forecast(model)

print(forecast)
# train delay model
train_delay_model(df)