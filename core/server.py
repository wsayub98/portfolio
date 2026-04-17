from http.server import BaseHTTPRequestHandler, HTTPServer
from core.router import Router


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        Router.handle(self)

    def do_POST(self):
        Router.handle(self)


def run(server_class=HTTPServer, handler=RequestHandler):
    server_address = ("", 8000)
    httpd = server_class(server_address, handler)
    print("Server running at http://localhost:8000")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server")
        httpd.server_close()
