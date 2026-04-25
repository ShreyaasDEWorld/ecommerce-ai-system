import pandas as pd
from sqlalchemy import create_engine   # ✅ THIS LINE MUST EXIST

DB_URL = "postgresql://mangesh:Admin@localhost:5432/Ecom"
engine = create_engine(DB_URL)

def get_demand_history(product_id="P1", limit=30):
    # reuse same DB connection
    DB_URL = "postgresql://mangesh:Admin@localhost:5432/Ecom"
    engine = create_engine(DB_URL)

    query = f"""
        SELECT orders
        FROM ecommerce_data
        WHERE product_id = '{product_id}'
        ORDER BY date DESC
        LIMIT {limit}
    """

    df = pd.read_sql(query, engine)

    # convert to list
    demand_history = df["orders"].tolist()

    # fallback (IMPORTANT)
    if len(demand_history) == 0:
        return [0]

    return demand_history