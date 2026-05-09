from app.services.anomaly_model import load_anomaly_model, detect_anomaly

model = load_anomaly_model()

print("\n🟢 Case 1: Balanced system (Normal expected)")
print("Input → Orders: 120, Stock: 300, Capacity: 400")
print("Output →", detect_anomaly(model, orders=120, stock=300, capacity=400))


print("\n🟢 Case 2: Slightly high demand but safe")
print("Input → Orders: 180, Stock: 350, Capacity: 400")
print("Output →", detect_anomaly(model, orders=180, stock=350, capacity=400))


print("\n🟡 Case 3: Near capacity (Borderline situation)")
print("Input → Orders: 380, Stock: 200, Capacity: 400")
print("Output →", detect_anomaly(model, orders=380, stock=200, capacity=400))


print("\n🔴 Case 4: Very high demand, low stock (Anomaly expected)")
print("Input → Orders: 500, Stock: 50, Capacity: 100")
print("Output →", detect_anomaly(model, orders=500, stock=50, capacity=100))


print("\n🔴 Case 5: Low stock with moderate demand (Risky situation)")
print("Input → Orders: 200, Stock: 20, Capacity: 150")
print("Output →", detect_anomaly(model, orders=200, stock=20, capacity=150))


print("\n🔴 Case 6: Extreme mismatch (Clear anomaly)")
print("Input → Orders: 600, Stock: 30, Capacity: 200")
print("Output →", detect_anomaly(model, orders=600, stock=30, capacity=200))