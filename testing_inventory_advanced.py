from app.services.inventory import ml_inventory, eoq, safety_stock, advanced_inventory

demand_history = [100, 120, 110, 130, 115, 140]

forecast = 120

print("ML Inventory:", ml_inventory(forecast, demand_history))
print("EOQ:", eoq(forecast))
print("Safety Stock:", safety_stock(demand_history))
print("Final Inventory:", advanced_inventory(forecast, demand_history))