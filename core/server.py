from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from core.router import Router


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        Router.handle(self)

    def do_POST(self):
        Router.handle(self)

    def do_DELETE(self):
        Router.handle(self)

    def do_OPTIONS(self):
        self.send_response(200, "OK")
        self.end_headers()

    def end_headers(self) -> None:
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET,POST,DELETE")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        return super().end_headers()


def run(server_class=HTTPServer, handler=RequestHandler):
    port = int(os.getenv("PORT", 8000))
    server_address = ("0.0.0.0", port)
    httpd = server_class(server_address, handler)
    print(f"Server running on port {port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server")
        httpd.server_close()
