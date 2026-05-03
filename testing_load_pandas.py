import pandas as pd
from sqlalchemy import create_engine

# 🔌 Step 1: Database Connection
DB_URL = "postgresql://mangesh:Admin@localhost:5432/Ecom"
engine = create_engine(DB_URL)

print("✅ Connected to database successfully")

# 🔍 Step 2: Query Data
query = """
SELECT date, orders, stock, capacity
FROM ecommerce_data
WHERE product_id = 'P1'
ORDER BY date
"""

df = pd.read_sql(query, engine)

# ⚠️ Step 3: Safety Check
if df.empty:
    print("❌ No data found")
else:
    print("✅ Data loaded successfully")

    print("\n=========== DATA PREVIEW (First 5 Rows) ===========")
    print(df.head())

    print("\n=========== DATA SHAPE (Rows, Columns) ===========")
    print(df.shape)

    print("\n=========== COLUMN NAMES ===========")
    print(df.columns)

    print("\n=========== DATAFRAME INFO ===========")
    df.info()

    print("\n=========== FORMATTED TABLE VIEW ===========")
    print(df.head().to_string())

    print("\n=========== SAMPLE SUMMARY ===========")
    print(df.describe())