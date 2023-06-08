from dotenv import load_dotenv
import os
from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics
from mongoConfig import get_database
import psutil
import time

app = Flask(__name__)
load_dotenv()

"""
The prometheus_flask_exporter.PrometheusMetrics class is used to create an instance of the Prometheus metrics exporter.
The metrics object is passed to the Flask application app to enable the Prometheus metrics endpoint.
By default, the metrics endpoint will be available at /metrics.

You will now have a Prometheus metrics endpoint available at http://localhost:5000/metrics (assuming your Flask app is running on port 5000).
"""
metrics = PrometheusMetrics(app)

def databaseConnection():
    mongoDB = get_database()
    return mongoDB

databaseConnection()

@app.route("/")
def home():
    return """Here's a summary of the Flask application's `/increase_cpu` endpoint:

The Flask application provides an endpoint `/increase_cpu` that accepts a POST request. This endpoint is designed to increase the CPU load to a specific percentage for a specific duration.

Here's an overview of the `/increase_cpu` endpoint functionality:

- The endpoint expects a JSON payload in the request body, which should include the following parameters:
  - `percentage`: The desired CPU load percentage (integer value).
  - `duration`: The duration in seconds for which the CPU load should be increased (integer value).
- Upon receiving a valid POST request, the application uses the `psutil` library to calculate the number of processes required to achieve the desired CPU load percentage.
- It starts the necessary number of processes, each of which continuously consumes CPU resources.
- After waiting for the specified duration, the application stops the CPU load processes.
- Finally, a response is returned indicating the CPU load percentage and duration that were applied.

To use this endpoint, you can make a POST request to `http://localhost:5000/increase_cpu` (assuming the Flask application is running locally on port 5000) and provide a JSON payload containing the `percentage` and `duration` parameters.

Please note that increasing CPU load can impact system performance and stability. Use this endpoint with caution and ensure proper monitoring and resource management.
"""

@app.route('/increase-cpu', methods=['POST'])
def increase_cpu():
    if 'percentage' in request.json and 'duration' in request.json:
        percentage = request.json['percentage']
        duration = request.json['duration']

        # Get the current CPU count
        cpu_count = psutil.cpu_count()
        # Calculate the number of process needed to achieve the desired percentage
        target_processes = int(cpu_count * (percentage / 100))

        # Start the CPU load processes
        processes = []
        for _ in range(target_processes):
            process = psutil.Process()
            process.cpu_percent(interval=None) # Set the interval to None for continous usage
            processes.append(process)

        # Wait for the specified duration
        time.sleep(duration)

        # Stop the CPU load processes
        for process in processes:
            process.cpu_percent(interval=None) # Stop CPU usage
            return f"CPU load increased to {percentage}% for {duration} seconds."
        else:
            return "Invalid request. Please provide 'percentage' and 'duration' parameters in the request body.", 400


if __name__ == '__main__':
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))
