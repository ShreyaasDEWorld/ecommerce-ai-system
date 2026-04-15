import psycopg2
import random
from datetime import datetime, timedelta

# DB connection
conn = psycopg2.connect(
    dbname="Ecom",
    user="mangesh",
    password="Admin",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

products = ["P1", "P2", "P3", "P4"]
warehouses = ["W1", "W2"]

start_date = datetime(2023, 1, 1)

# generate 365 days
for i in range(365):
    date = start_date + timedelta(days=i)

    for product in products:
        orders = random.randint(50, 200)
        stock = random.randint(100, 600)
        delivery_time = random.randint(1, 5)

        # delay logic (IMPORTANT: realistic pattern)
        delay = 1 if orders > stock * 0.8 else 0

        warehouse = random.choice(warehouses)
        capacity = random.randint(200, 500)

        cursor.execute("""
            INSERT INTO ecommerce_data
            (date, product_id, warehouse, orders, delivery_time, delay, stock, capacity)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """, (date, product, warehouse, orders, delivery_time, delay, stock, capacity))

conn.commit()
cursor.close()
conn.close()

print("✅ Data generated successfully")