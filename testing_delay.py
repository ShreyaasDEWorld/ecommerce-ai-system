from app.services.delay_model import load_delay_model, predict_delay

model = load_delay_model()

risk = predict_delay(model, orders=150, stock=100, capacity=200)

print("Delay risk:", risk)