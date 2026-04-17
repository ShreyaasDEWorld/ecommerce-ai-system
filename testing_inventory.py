from app.services.inventory import optimize_stock, reorder_point

# Example forecast values
forecast_values = [100, 150, 200]

for f in forecast_values:
    stock = optimize_stock(f)
    reorder = reorder_point(f)

    print("Forecast:", f)
    print("Recommended Stock:", stock)
    print("Reorder Point:", reorder)
    print("-" * 30)