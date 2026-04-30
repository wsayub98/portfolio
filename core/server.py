from http.server import BaseHTTPRequestHandler, HTTPServer
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
    server_address = ("", 8000)
    httpd = server_class(server_address, handler)
    print("Server running at http://localhost:8000")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server")
        httpd.server_close()
