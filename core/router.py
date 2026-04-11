from routes.api import routes


class Router:
    @staticmethod
    def handle(handler):
        path = handler.path
        method = handler.command

        for version, endpoints in routes.items():
            for endpoint in endpoints:
                route_path = "/" + version + endpoint["path"]
                if route_path == path and endpoint["method"] == method:
                    # Controller class method.
                    response = endpoint["action"]()

                    handler.send_response(200)
                    handler.send_header("Content-type", "application_json")
                    handler.end_headers()

                    handler.wfile.write(response.encode())
                    return

        handler.send_response(404)
        handler.end_headers()
        handler.wfile.write(b'{"error": "Page Not Found"}')
