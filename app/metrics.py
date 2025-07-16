import psutil
import platform
import socket
import time

def get_metrics():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory()._asdict(),
        "hostname": socket.gethostname(),
        "platform": platform.platform(),
    }

def get_disk_usage():
    return psutil.disk_usage('/')._asdict()

def get_network_stats():
    return psutil.net_io_counters(pernic=False)._asdict()

def get_uptime_minutes():
    return int(time.time() - psutil.boot_time()) // 60
