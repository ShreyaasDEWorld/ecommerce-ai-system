import numpy as np
import math

def ml_inventory(forecast, demand_history):
    avg_demand = np.mean(demand_history)
    std_demand = np.std(demand_history)

    if avg_demand == 0:
        safety_factor = 1
    else:
        safety_factor = 1 + (std_demand / avg_demand)

    return round(forecast * safety_factor)


def eoq(demand, ordering_cost=50, holding_cost=2):
    if demand <= 0:
        return 0

    return round(math.sqrt((2 * demand * ordering_cost) / holding_cost))


def safety_stock(demand_history, lead_time=2, service_level=1.65):
    std_dev = np.std(demand_history)
    return round(service_level * std_dev * (lead_time ** 0.5))


def advanced_inventory(forecast, demand_history):
    ss = safety_stock(demand_history)
    return round(forecast + ss)