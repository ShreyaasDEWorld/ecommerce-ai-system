import joblib
import os

from app.utils.db_loader import load_and_preprocess
from app.services.forecasting import train_forecast
from app.services.delay_model import train_delay_model
from app.services.anomaly_model import train_anomaly_model

os.makedirs("models", exist_ok=True)

# ✅ load proper DataFrame
df = load_and_preprocess("P1")
# ✅ Add delay column (IMPORTANT FIX)
#if "delay" not in df.columns:
#    df["delay"] = (df["orders"] > df["capacity"]).astype(int)

import numpy as np

df["delay"] = (
                (df["orders"] > df["capacity"]) |
                (np.random.rand(len(df)) > 0.7)
              ).astype(int)   

# train forecast
model = train_forecast(df, "P1")
joblib.dump(model, "models/forecast_P1.pkl")

print("✅ Forecast model trained")

# train other models
train_delay_model(df)
#print("✅ Delay model trained")
train_anomaly_model(df)
#print("✅ Anomaly model trained")