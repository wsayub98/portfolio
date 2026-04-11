from app.controllers.portfolio_controller import PortfolioController

routes = {
    "v1": [
        {"path": "/portfolio", "method": "POST", "action": PortfolioController.index},
        {"path": "/portfolio", "method": "GET", "action": PortfolioController.index},
    ]
}
