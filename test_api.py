# test_api.py
import requests
import time

url = "http://127.0.0.1:8000/predict"

data1 = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

data2 = {
    "sepal_length": 6.7,
    "sepal_width": 3.1,
    "petal_length": 4.7,
    "petal_width": 1.5
}

for _ in range(20): # Send multiple requests to generate metrics
    response1 = requests.post(url, json=data1)
    print("Prediction for data1:", response1.json())
    response2 = requests.post(url, json=data2)
    print("Prediction for data2:", response2.json())
    time.sleep(1) # Wait for 1 second between requests