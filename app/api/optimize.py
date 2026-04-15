from fastapi import APIRouter
import joblib

from app.services.forecasting import predict_forecast
from app.services.delay_model import load_delay_model, predict_delay
from app.services.anomaly_model import load_anomaly_model, detect_anomaly
from app.services.inventory import optimize_stock

router = APIRouter()

# load models once (IMPORTANT)
forecast_model = joblib.load("models/forecast_P1.pkl")
delay_model = load_delay_model()
anomaly_model = load_anomaly_model()


@router.post("/optimize")
def optimize(data: dict):

    # 1. Forecast
    forecast_df = predict_forecast(forecast_model)
    forecast_value = int(forecast_df["yhat"].iloc[-1])

    # 2. Delay prediction
    delay = predict_delay(
        delay_model,
        orders=forecast_value,
        stock=data["stock"],
        capacity=data.get("capacity", 200)
    )

    # 3. Inventory
    stock = optimize_stock(forecast_value)

    # 4. Anomaly detection
    anomaly = detect_anomaly(
        anomaly_model,
        orders=forecast_value,
        stock=data["stock"],
        capacity=data.get("capacity", 200)
    )

    return {
        "forecast": forecast_value,
        "delay_risk": delay,
        "recommended_stock": stock,
        "anomaly": anomaly
    }