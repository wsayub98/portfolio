from app.controllers.user_controller import UserController
from core.router import Router
from app.controllers.portfolio_controller import PortfolioController


def setup():
    rType = "api"
    rVersion = "v1"

    Router.register(f"/{rType}/{rVersion}/portfolio", "POST", PortfolioController.index)
    Router.register(
        f"/{rType}/{rVersion}/admin/login", "POST", UserController.authenticate
    )
    Router.register(
        f"/{rType}/{rVersion}/portfolio/create", "POST", PortfolioController.store
    )
    Router.register(
        f"/{rType}/{rVersion}/portfolio/update", "POST", PortfolioController.update
    )
    Router.register(
        f"/{rType}/{rVersion}/portfolio/delete", "DELETE", PortfolioController.destroy
    )
