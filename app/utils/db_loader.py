import pandas as pd
from sqlalchemy import create_engine

DB_URL = "postgresql://mangesh:Admin@localhost:5432/Ecom"
engine = create_engine(DB_URL)


def load_and_preprocess(product_id="P1"):
    query = f"""
        SELECT date, orders,stock, capacity
        FROM ecommerce_data
        WHERE product_id = '{product_id}'
        ORDER BY date
    """

    df = pd.read_sql(query, engine)

    # safety
    if df.empty:
        raise ValueError(f"No data found for {product_id}")

    return df