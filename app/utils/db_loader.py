import pandas as pd
from sqlalchemy import create_engine

def load_data():
    # update credentials
    DB_URL = "postgresql://mangesh:Admin@localhost:5432/Ecom"

    engine = create_engine(DB_URL)

    query = "SELECT * FROM ecommerce_data"

    df = pd.read_sql(query, engine)

    return df

def preprocess(df):
    df["date"] = pd.to_datetime(df["date"])

    # optional features
    df["day_of_week"] = df["date"].dt.dayofweek
    df["month"] = df["date"].dt.month

    return df

def load_and_preprocess():
    df = load_data()

    df["date"] = pd.to_datetime(df["date"])
    df["day_of_week"] = df["date"].dt.dayofweek
    df["month"] = df["date"].dt.month

    return df

