# 🧠 E-commerce AI Optimization System

This project is an AI-powered backend system for:

- Demand forecasting
- Delay prediction
- Inventory optimization
- Anomaly detection

## 🚀 Features

- 📊 Forecast demand using Prophet
- ⚠️ Predict delays using RandomForest
- 📦 Optimize inventory
- 🚨 Detect anomalies using IsolationForest
- 🌐 FastAPI backend

## 🏗️ Tech Stack

- Python
- FastAPI
- scikit-learn
- Prophet
- PostgreSQL

## ▶️ How to Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload


API

Visit:
http://127.0.0.1:8000/docs

Example Input:
{
  "stock": 100,
  "capacity": 200
}
Example Output:

{
  "forecast": 114,
  "delay_risk": 0.46,
  "recommended_stock": 136,
  "anomaly": true
}


Use Case

AI system for e-commerce, logistics, and telemetry-based decision-making.
