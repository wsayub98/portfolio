import json
from app.models.portfolio import Portfolio
from app.repositories.portfolio_repository import PortfolioRepository


class PortfolioService:
    @staticmethod
    def get_portfolio():
        fetched = PortfolioRepository.get_all()
        data = fetched[0]

        portfolio = Portfolio(
            name=data["name"],
            experience=data["experience"],
            skills=data["skills"],
            companies=data["companies"],
        )
        data = portfolio.to_dict()

        return {
            "status": True,
            "data": data,
        }
