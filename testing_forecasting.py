import joblib
from app.services.forecasting import predict_forecast


model = joblib.load("models/forecast_P1.pkl")

forecast = predict_forecast(model)

print(forecast)
