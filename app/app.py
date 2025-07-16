from flask import Flask, jsonify, Response
from metrics import (
    get_metrics,
    get_disk_usage,
    get_network_stats,
    get_uptime_minutes
)
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter

app = Flask(__name__)

# Define custom Prometheus metric
REQUEST_COUNT = Counter("app_requests_total", "Total HTTP Requests", ["endpoint"])

@app.route("/metrics")
def metrics():
    REQUEST_COUNT.labels(endpoint="/metrics").inc()
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route("/disk")
def disk():
    REQUEST_COUNT.labels(endpoint="/disk").inc()
    return jsonify(get_disk_usage())

@app.route("/network")
def network():
    REQUEST_COUNT.labels(endpoint="/network").inc()
    return jsonify(get_network_stats())

@app.route("/uptime")
def uptime():
    REQUEST_COUNT.labels(endpoint="/uptime").inc()
    return jsonify({"uptime_minutes": get_uptime_minutes()})

@app.route("/health")
def health():
    REQUEST_COUNT.labels(endpoint="/health").inc()
    return jsonify({"status": "ok"})

@app.route("/")
def index():
    REQUEST_COUNT.labels(endpoint="/").inc()
    return jsonify({
        "message": "Welcome to the system metrics API",
        "available_endpoints": [
            "/health",
            "/metrics",
            "/disk",
            "/network",
            "/uptime"
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
