def optimize_stock(forecast):
    return int(forecast * 1.2)


def reorder_point(forecast, lead_time=2):
    return forecast * lead_time