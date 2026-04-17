import routes.api
from core.server import run

if __name__ == "__main__":
    # Routes register.
    routes.api.setup()
    # Run server.
    run()
