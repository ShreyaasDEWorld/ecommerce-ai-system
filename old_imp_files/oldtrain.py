from app.utils.db_loader import load_and_preprocess
from app.services.forecasting import train_forecast
from app.services.delay_model import train_delay_model
import joblib
from app.services.anomaly_model import train_anomaly_model

df = load_and_preprocess()

# train for product P1 (start simple)
model = train_forecast(df, "P1")

joblib.dump(model, "models/forecast_P1.pkl")

print("✅ Forecast model trained")

# train delay model
train_delay_model(df)

#ANOMALY MODEL
train_anomaly_model(df)