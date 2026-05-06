import joblib
from sklearn.ensemble import IsolationForest

def train_anomaly_model(df):
    # features (same as delay model)
    X = df[["orders", "stock", "capacity"]]


    model = IsolationForest(
        contamination=0.05,  # 5% anomalies
        random_state=42
    )

    model.fit(X)

    joblib.dump(model, "models/anomaly.pkl")

    print("✅ Anomaly model trained")


def load_anomaly_model():
    return joblib.load("models/anomaly.pkl")


def detect_anomaly(model, orders, stock, capacity):
    import pandas as pd

    data = pd.DataFrame([{
        "orders": orders,
        "stock": stock,
        "capacity": capacity
    }])

    prediction = model.predict(data)[0]   # -1 = anomaly, 1 = normal
    score = model.decision_function(data)[0]

    return {
        #"anomaly": prediction == -1,
        "anomaly": bool(prediction == -1),
        "score": float(score)
    }