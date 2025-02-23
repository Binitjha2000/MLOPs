# main.py
from fastapi import FastAPI, HTTPException
import mlflow.sklearn
import pandas as pd
from pydantic import BaseModel
import time

# Prometheus client library imports
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import PlainTextResponse

# Initialize FastAPI app
app = FastAPI()

# Load the model from the local path
model_path = "random_forest_model"
try:
    model = mlflow.sklearn.load_model(model_path)
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to load model: {e}")

# Define Pydantic model for input data
class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Prometheus Metrics Initialization
REQUEST_COUNT = Counter(
    "iris_prediction_requests_total", "Total number of prediction requests."
)
REQUEST_LATENCY = Histogram(
    "iris_prediction_request_latency_seconds", "Prediction request latency in seconds."
)
MODEL_PREDICTION_COUNT = Counter(
    "iris_model_predictions_total",
    "Total number of predictions by class.",
    ["prediction_class"],
)

# Prediction Endpoint
@app.post("/predict")
async def predict(data: IrisData):
    start_time = time.time()
    REQUEST_COUNT.inc()  # Increment request counter
    try:
        # Convert input data to DataFrame
        df = pd.DataFrame([data.dict().values()], columns=data.dict().keys())
        prediction = model.predict(df)
        predicted_class = int(prediction[0]) # Get integer prediction
        MODEL_PREDICTION_COUNT.labels(prediction_class=str(predicted_class)).inc() # Increment prediction class counter
        return {"prediction": predicted_class}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")
    finally:
        latency = time.time() - start_time
        REQUEST_LATENCY.observe(latency) # Observe latency

# Metrics Endpoint for Prometheus to scrape
@app.get("/metrics")
async def metrics():
    return PlainTextResponse(generate_latest(), headers={"Content-Type": CONTENT_TYPE_LATEST})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)