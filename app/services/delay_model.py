import joblib
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

def train_delay_model(df):
    # features (VERY IMPORTANT)
    X = df[["orders", "stock", "capacity"]]

    # target
    y = df["delay"]

    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42
    )

    model.fit(X, y)

    # save model
    joblib.dump(model, "models/delay.pkl")

    print("✅ Delay model trained")


def load_delay_model():
    return joblib.load("models/delay.pkl")


#def predict_delay(model, orders, stock, capacity):
#    prob = model.predict_proba([[orders, stock, capacity]])[0][1]
#    return float(prob)

def predict_delay(model, orders, stock, capacity):
    data = pd.DataFrame([{
        "orders": orders,
        "stock": stock,
        "capacity": capacity
    }])

    prob = model.predict_proba(data)[0][1]
    return float(prob)

