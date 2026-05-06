from app.services.forecasting import predict_forecast
import joblib

model = joblib.load("models/forecast_P1.pkl")

result = predict_forecast(model)
print(result)