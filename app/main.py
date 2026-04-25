from fastapi import FastAPI
from app.api import optimize   # 👈 import

app = FastAPI()

app.include_router(optimize.router)  # 👈 connect
@app.get("/")
def home():
    return {"status": "AI system running 🚀"}
