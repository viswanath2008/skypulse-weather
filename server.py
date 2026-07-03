import http.server
import socketserver

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {args[0]} {args[1]} {args[2]}")

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"SkyPulse running at http://localhost:{PORT}")
    print(f"Press Ctrl+C to stop")
    httpd.serve_forever()
