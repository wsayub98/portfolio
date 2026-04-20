from typing import Callable
from typing_extensions import TYPE_CHECKING
import json
from devtools import debug

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
            # Get response status.
            status = json.loads(response).get("status")
            # Determine http status code.
            # Todo: refactor - need to consider authorization, 201,401,403, etc.
            if status:
                handler.send_response(200)
            else:
                handler.send_response(400)

            handler.send_header("Content-type", "application_json")
            handler.end_headers()
            handler.wfile.write(response.encode())
            return

        handler.send_response(404)
        handler.end_headers()
        handler.wfile.write(b'{"error": "Page Not Found! 404"}')
