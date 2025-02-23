# train_model.py
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Set our tracking server URI for logging
mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")
# Set the experiment name; this creates it if it doesn't exist
mlflow.set_experiment("MLOps_Lab11")

# 2. Load and Preprocess the Dataset:
# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
# Split the dataset into training (80%) and test (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train the Model and Log with MLflow:
# Start a new MLflow run; this will track the entire experiment's steps
with mlflow.start_run() as run:
    # Instantiate the RandomForestClassifier with specified hyperparameters
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    # Train the model on the training dataset
    model.fit(X_train, y_train)
    # Log the trained model to MLflow
    mlflow.sklearn.log_model(model, "random_forest_model")
    # Save the model locally
    model_path = "random_forest_model"
    mlflow.sklearn.save_model(model, model_path)
    # Calculate the model accuracy using the test dataset
    accuracy = accuracy_score(y_test, model.predict(X_test))
    # Log the accuracy as a metric in MLflow
    mlflow.log_metric("accuracy", accuracy)
    # Retrieve and print the run ID for future reference (e.g., loading or deployment)
    run_id = run.info.run_id
    print("Run ID:", run_id)
    # Print the run ID for use in later tasks
    print("Model saved at:", model_path) # Print the local model path