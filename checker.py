#!/usr/bin/env python3


import json
import re
import socket
import subprocess
import threading
import time
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOSTS = [
    {"name": "Proxmox",   "host": "10.147.17.110", "port": 8006},
    {"name": "Navidrome", "host": "10.147.17.101", "port": 4533},
    {"name": "Monitor",   "host": "10.147.17.25"},
    {"name": "Grafana",   "host": "10.147.17.25", "port": 3000},
    {"name": "Uptime",    "host": "10.147.17.25", "port": 3001},
    {"name": "InfluxDB",  "host": "10.147.17.25", "port": 8086},
    {"name": "Feed",      "host": "feed.aut0iq.qzz.io", "port": 443},
]

INTERVAL = 30
TIMEOUT = 4
HISTORY = 20
LISTEN = ("127.0.0.1", 8099)


_state = {h["name"]: {"up": None, "ms": None, "history": deque(maxlen=HISTORY)}
          for h in HOSTS}
_updated = None
_lock = threading.Lock()

_PING_TIME = re.compile(r"time[=<]([\d.]+)")


def check_tcp(host, port):
    started = time.perf_counter()
    try:
        with socket.create_connection((host, port), timeout=TIMEOUT):
            return True, round((time.perf_counter() - started) * 1000)
    except OSError:
        return False, None


def check_icmp(host):
    try:
        res = subprocess.run(
            ["ping", "-n", "-c", "1", "-W", str(TIMEOUT), host],
            capture_output=True, text=True, timeout=TIMEOUT + 2,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False, None
    if res.returncode != 0:
        return False, None
    m = _PING_TIME.search(res.stdout)
    return True, round(float(m.group(1))) if m else 0


def probe(entry):
    if entry.get("port"):
        up, ms = check_tcp(entry["host"], entry["port"])
    else:
        up, ms = check_icmp(entry["host"])
    return entry["name"], up, ms


def sweep():
    with ThreadPoolExecutor(max_workers=min(16, len(HOSTS) or 1)) as pool:
        results = list(pool.map(probe, HOSTS))

    global _updated
    with _lock:
        for name, up, ms in results:
            slot = _state[name]
            slot["up"] = up
            slot["ms"] = ms
            slot["history"].append({"up": up, "ms": ms})
        _updated = datetime.now(timezone.utc).isoformat(timespec="seconds")


def loop():
    while True:
        try:
            sweep()
        except Exception as err:
            print("sweep failed:", err, flush=True)
        time.sleep(INTERVAL)


def snapshot():
    with _lock:
        return {
            "updated": _updated,
            "interval": INTERVAL,
            "hosts": [
                {
                    "name": h["name"],
                    "up": _state[h["name"]]["up"],
                    "ms": _state[h["name"]]["ms"],
                    "history": list(_state[h["name"]]["history"]),
                }
                for h in HOSTS
            ],
        }


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def do_GET(self):
        if self.path.rstrip("/") not in ("", "/status"):
            self.send_error(404)
            return
        body = json.dumps(snapshot(), ensure_ascii=False).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    threading.Thread(target=loop, daemon=True).start()
    ThreadingHTTPServer(LISTEN, Handler).serve_forever()
