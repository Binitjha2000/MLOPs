python train_model.py
docker-compose up --build
python test_api.py

Access Grafana Dashboard:

Open your web browser and go to http://localhost:3000.
Log in with username admin and password password.
Add Prometheus Data Source:
Click "Connections" (or "Data Sources").
"Add data source" -> "Prometheus".
Set URL to http://prometheus:9090.
"Save & test".
Create Grafana Dashboard:

"Dashboards" -> "Create new dashboard".
Add Panels: Create panels using "Add visualization" and configure them as described in the previous detailed response, using queries like:
iris_prediction_requests_total (for total requests - Stat panel)
rate(iris_prediction_request_latency_seconds_sum[1m]) / rate(iris_prediction_request_latency_seconds_count[1m]) (for average latency - Graph panel)
iris_model_predictions_total (for prediction class counts - Pie Chart or Bar Chart panel)
Observe Metrics:
Watch your Grafana dashboard as test_api.py continues to run. You should see the metrics update, showing request counts, latency, and prediction distributions.

Stop Docker Compose:
When done, in the terminal where you ran docker-compose up, press Ctrl+C (if running in attached mode) or run docker-compose down in the terminal to stop the containers.