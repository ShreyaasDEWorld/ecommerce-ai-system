from fastapi import APIRouter
from pydantic import BaseModel
import joblib

from app.services.forecasting import predict_forecast
from app.services.delay_model import load_delay_model, predict_delay
from app.services.anomaly_model import load_anomaly_model, detect_anomaly
from app.services.inventory import advanced_inventory, eoq, safety_stock
# from app.utils.db_loader import get_demand_history

router = APIRouter()


# ✅ Request schema (important)
class OptimizeRequest(BaseModel):
    stock: int
    capacity: int = 200
    product_id: str = "P1"


# ✅ Load static models
delay_model = load_delay_model()
anomaly_model = load_anomaly_model()


# ✅ Dynamic forecast model loader
def load_forecast_model(product_id):
    return joblib.load(f"models/forecast_{product_id}.pkl")


@router.post("/optimize")
def optimize(data: OptimizeRequest):

    product_id = data.product_id

    # ✅ Load correct model per product
    forecast_model = load_forecast_model(product_id)

    # 1. Forecast
    forecast_df = predict_forecast(forecast_model)
    forecast_value = int(forecast_df["yhat"].iloc[-1])

    # 2. Delay prediction
    delay = predict_delay(
        delay_model,
        orders=forecast_value,
        stock=data.stock,
        capacity=data.capacity
    )

    # ✅ Fetch demand ONCE
    # demand_history = get_demand_history(product_id)
    demand_history = [100, 120, 130, 110]

    # 3. Inventory
    recommended_stock = advanced_inventory(forecast_value, demand_history)
    order_quantity = eoq(forecast_value)
    safety = safety_stock(demand_history)

    # 4. Anomaly detection
    anomaly = detect_anomaly(
        anomaly_model,
        orders=forecast_value,
        stock=data.stock,
        capacity=data.capacity
    )

    return {
        "product_id": product_id,
        "forecast": forecast_value,
        "delay_risk": delay,
        "inventory": {
            "recommended": recommended_stock,
            "eoq": order_quantity,
            "safety_stock": safety
        },
        "anomaly": anomaly
    }