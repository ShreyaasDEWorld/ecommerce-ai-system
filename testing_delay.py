from app.services.delay_model import load_delay_model, predict_delay

model = load_delay_model()

# 🟢 Case 1: Balanced system (Low risk)
print("\n🟢 Case 1: Balanced system (Low delay risk expected)")
print("Input → Orders: 100, Stock: 200, Capacity: 300")
print("Output →", predict_delay(model, orders=100, stock=200, capacity=300))


# 🟢 Case 2: Good stock, manageable demand
print("\n🟢 Case 2: Sufficient stock and capacity")
print("Input → Orders: 150, Stock: 250, Capacity: 300")
print("Output →", predict_delay(model, orders=150, stock=250, capacity=300))


# 🟡 Case 3: Demand close to capacity (Medium risk)
print("\n🟡 Case 3: Demand near capacity (Moderate delay risk)")
print("Input → Orders: 180, Stock: 150, Capacity: 200")
print("Output →", predict_delay(model, orders=180, stock=150, capacity=200))


# 🔴 Case 4: Demand exceeds capacity (High risk)
print("\n🔴 Case 4: Demand exceeds capacity (High delay risk)")
print("Input → Orders: 300, Stock: 100, Capacity: 200")
print("Output →", predict_delay(model, orders=300, stock=100, capacity=200))


# 🔴 Case 5: Low stock, high demand (Critical risk)
print("\n🔴 Case 5: Low stock with high demand (Very high risk)")
print("Input → Orders: 250, Stock: 50, Capacity: 200")
print("Output →", predict_delay(model, orders=250, stock=50, capacity=200))


# 🔴 Case 6: Extreme overload (Severe delay expected)
print("\n🔴 Case 6: Extreme demand vs capacity mismatch")
print("Input → Orders: 500, Stock: 80, Capacity: 150")
print("Output →", predict_delay(model, orders=500, stock=80, capacity=150))