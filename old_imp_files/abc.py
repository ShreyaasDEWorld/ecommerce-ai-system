import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

def load_forecast_model(product_id):
    path = os.path.join(BASE_DIR, "models", f"forecast_{product_id}.pkl")
    return joblib.load(path)