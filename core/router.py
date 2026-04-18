from typing import Callable
from typing_extensions import TYPE_CHECKING
import json

if TYPE_CHECKING:
    from core.server import RequestHandler


class Router:
    _routes = {}

    @staticmethod
    def register(path: str, method: str, action: Callable):
        Router._routes[(path, method)] = action

    @staticmethod
    def handle(handler: "RequestHandler"):
        action = Router._routes.get((handler.path, handler.command))
        if action:
            content_length = int(handler.headers["Content-Length"])
            body = handler.rfile.read(content_length)
            params = json.loads(body.decode("utf-8")) if body else None

            response = action(params)

            handler.send_response(200)
            handler.send_header("Content-type", "application_json")
            handler.end_headers()

            handler.wfile.write(response.encode())
            return

        handler.send_response(404)
        handler.end_headers()
        handler.wfile.write(b'{"error": "Page Not Found! 404"}')
