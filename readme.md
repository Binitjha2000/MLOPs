# Iris Classification ML Pipeline with FastAPI, Prometheus, and Grafana

## Project Description

This project demonstrates a complete Machine Learning Operations (MLOps) pipeline for Iris classification. It encompasses model training, API deployment using FastAPI, real-time monitoring with Prometheus and Grafana, and containerization with Docker.

**Key Features:**

*   **Model Training:** Trains a Random Forest classifier on the Iris dataset using `train_model.py` and tracks experiments with MLflow.
*   **REST API Deployment:** Deploys the trained model as a REST API using FastAPI in `main.py`. The API exposes a `/predict` endpoint for making predictions.
*   **API Monitoring:** Implements Prometheus metrics within the API to track:
    *   Total prediction requests (`iris_prediction_requests_total`)
    *   Prediction request latency (`iris_prediction_request_latency_seconds`)
    *   Number of predictions per Iris class (`iris_model_predictions_total`)
*   **Visualization with Grafana:** Provides a Grafana dashboard to visualize the Prometheus metrics, offering real-time insights into API performance and model behavior.
*   **Containerization with Docker:**  Uses Docker to containerize the FastAPI application and sets up Prometheus and Grafana using Docker Compose for easy deployment and reproducibility.
*   **API Testing:** Includes `test_api.py` to send test requests to the deployed API and generate metrics for monitoring.

## Code Structure

*   **`main.py`:**  FastAPI application that loads the trained Iris classification model and serves it via a REST API. Includes Prometheus metrics instrumentation.
*   **`train_model.py`:** Python script to train a Random Forest model on the Iris dataset using scikit-learn and log the model with MLflow. Saves the trained model locally.
*   **`test_api.py`:** Python script to send sample prediction requests to the deployed API endpoint to test functionality and generate monitoring data.
*   **`Dockerfile`:** Defines the Docker image for the FastAPI application, including dependencies and startup command.
*   **`docker-compose.yml`:**  Defines the Docker Compose setup, orchestrating the FastAPI application, Prometheus, and Grafana containers.
*   **`requirements.txt`:** Lists the Python dependencies required for the FastAPI application and model training.

## Setup and Run Instructions

**Prerequisites:**

*   Docker and Docker Compose installed on your system.
*   Python 3.8 or higher.

**Steps:**

1.  **Clone the repository (or create the files as provided in the prompt):**

    If you have the files directly, ensure they are in the same directory.

2.  **Build and Start the Docker Compose environment:**

    Open a terminal in the project directory and run:

    ```bash
    docker-compose up --build
    ```

    This command will:
    *   Build the Docker image for the FastAPI application.
    *   Start three containers: FastAPI API, Prometheus, and Grafana.

3.  **Train the Machine Learning Model:**

    Open a new terminal in the project directory and run the training script:

    ```bash
    python train_model.py
    ```

    This script will:
    *   Train a Random Forest model.
    *   Save the trained model locally in the `random_forest_model` directory.
    *   Log the model and accuracy to MLflow (MLflow server is assumed to be running, as per `train_model.py`'s `mlflow.set_tracking_uri`).

4.  **Test the API and Generate Metrics:**

    Open another new terminal in the project directory and run the test script:

    ```bash
    python test_api.py
    ```

    This script will send prediction requests to the API endpoint, which will:
    *   Return predictions.
    *   Increment Prometheus metrics counters and histograms.

5.  **Access the Grafana Dashboard:**

    *   Open your web browser and go to: `http://localhost:3000`
    *   Log in with the default credentials:
        *   **Username:** `admin`
        *   **Password:** `password`

6.  **Add Prometheus Data Source to Grafana:**

    *   In the Grafana sidebar, click on **"Connections"** (or **"Data Sources"**, depending on your Grafana version).
    *   Click **"Add data source"**.
    *   Search for and select **"Prometheus"**.
    *   In the "URL" field, enter: `http://prometheus:9090`
    *   Click **"Save & test"** to verify the connection.

7.  **Create a Grafana Dashboard:**

    *   In the Grafana sidebar, click on **"Dashboards"** -> **"Create new dashboard"**.
    *   **Add Panels:** For each metric you want to visualize, click **"Add visualization"** and configure the panel:

        *   **Total Requests (Stat Panel):**
            *   Panel type: **Stat**
            *   Query: `iris_prediction_requests_total`

        *   **Average Latency (Graph Panel):**
            *   Panel type: **Graph**
            *   Query: `rate(iris_prediction_request_latency_seconds_sum[1m]) / rate(iris_prediction_request_latency_seconds_count[1m])`

        *   **Prediction Class Counts (Pie Chart or Bar Chart Panel):**
            *   Panel type: **Pie Chart** or **Bar Chart**
            *   Query: `iris_model_predictions_total`

    *   Adjust panel titles and settings as desired.

8.  **Observe Metrics:**

    *   Keep `test_api.py` running (or run it again).
    *   Watch your Grafana dashboard. You should see the panels updating in real-time as `test_api.py` sends requests and generates metrics, showing request counts, latency, and prediction class distributions.

## Stopping the Project

To stop the Docker Compose environment, go to the terminal where you ran `docker-compose up` and:

*   Press `Ctrl+C` if running in attached mode.
*   OR, in another terminal in the project directory, run:

    ```bash
    docker-compose down
    ```

    This will stop and remove the containers.

## Further Exploration

*   **Improve Model Accuracy:** Experiment with different models, hyperparameters, or feature engineering to improve the Iris classification accuracy.
*   **Advanced Monitoring:** Add more sophisticated metrics and alerts in Prometheus and Grafana, such as error rates, resource utilization, etc.
*   **Scalability:** Explore methods to scale the API deployment using load balancers and container orchestration tools like Kubernetes.
*   **Model Versioning and Deployment Pipeline:** Implement a CI/CD pipeline to automate model training, testing, and deployment with version control and rollback capabilities.
*   **Security:**  Implement security measures for the API, such as authentication and authorization.

This README provides a detailed guide to understand, set up, and run the Iris classification ML pipeline project. Enjoy exploring and experimenting!