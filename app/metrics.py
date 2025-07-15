import psutil
import platform
import socket
import shutil
import time
import os

def get_metrics():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory()._asdict(),
        "hostname": socket.gethostname(),
        "platform": platform.platform(),
    }

def get_disk_usage():
    total, used, free = shutil.disk_usage("/")
    return {
        "total_gb": round(total / (1024 ** 3), 2),
        "used_gb": round(used / (1024 ** 3), 2),
        "free_gb": round(free / (1024 ** 3), 2),
    }

def get_network_stats():
    net = psutil.net_io_counters()
    return {
        "bytes_sent_mb": round(net.bytes_sent / (1024 ** 2), 2),
        "bytes_recv_mb": round(net.bytes_recv / (1024 ** 2), 2),
        "packets_sent": net.packets_sent,
        "packets_recv": net.packets_recv,
    }

def get_uptime_minutes():
    boot_time = psutil.boot_time()
    current_time = time.time()
    uptime_seconds = current_time - boot_time
    return round(uptime_seconds / 60, 2)
