import psutil
import platform
import socket

def get_metrics():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory()._asdict(),
        "hostname": socket.gethostname(),
        "platform": platform.platform(),
    }