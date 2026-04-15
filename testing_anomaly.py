from app.services.anomaly_model import load_anomaly_model, detect_anomaly

model = load_anomaly_model()

# normal case
print(detect_anomaly(model, orders=120, stock=300, capacity=400))

# anomaly case
print(detect_anomaly(model, orders=500, stock=50, capacity=100))