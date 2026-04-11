import json
from app.services.portfolio_service import PortfolioService


class PortfolioController:
    @staticmethod
    def index():
        portfolio_service = PortfolioService.get_portfolio()
        return json.dumps(portfolio_service)
