from flask import Flask, jsonify, Response
from metrics import (
    get_metrics,
    get_disk_usage,
    get_network_stats,
    get_uptime_minutes
)
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route("/disk")
def disk():
    return jsonify(get_disk_usage())

@app.route("/network")
def network():
    return jsonify(get_network_stats())

@app.route("/uptime")
def uptime():
    return jsonify({"uptime_minutes": get_uptime_minutes()})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)