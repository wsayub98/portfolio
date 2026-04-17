from typing import Callable


class Router:
    _routes = {}

    @staticmethod
    def register(path: str, method: str, action: Callable):
        Router._routes[(path, method)] = action

    @staticmethod
    def handle(handler):
        action = Router._routes.get((handler.path, handler.command))
        if action:
            response = action()

            handler.send_response(200)
            handler.send_header("Content-type", "application_json")
            handler.end_headers()

            handler.wfile.write(response.encode())
            return

        handler.send_response(404)
        handler.end_headers()
        handler.wfile.write(b'{"error": "Page Not Found! 404"}')
