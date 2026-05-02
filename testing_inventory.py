from app.services.inventory import advanced_inventory, eoq, safety_stock

# Example forecast values
forecast_values = [100, 150, 200]

# Dummy demand history (needed for ML inventory + safety stock)
demand_history = [90, 110, 120, 130, 140]

for f in forecast_values:
    stock = advanced_inventory(f, demand_history)
    reorder = safety_stock(demand_history)

    print("Forecast:", f)
    print("Recommended Stock:", stock)
    print("Reorder Point (Safety Stock):", reorder)
    print("EOQ:", eoq(f))
    print("-" * 30)