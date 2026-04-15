from app.utils.db_loader import load_data

df = load_data()

print(df.head())
print(df.shape)