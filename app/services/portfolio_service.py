import json
from app.models.portfolio import Portfolio
from app.repositories.portfolio_repository import PortfolioRepository


class PortfolioService:
    @staticmethod
    def get_portfolio(conn):
        try:
            fetched = PortfolioRepository.get_all(conn)

            data = fetched
            portfolio = PortfolioService._instantiate(data)
            data = portfolio.to_dict()

            return {
                "status": True,
                "data": data,
            }
        except Exception as e:
            return {
                "status": False,
                "error": str(e),
            }

    @staticmethod
    def update_portfolio(conn, params):
        try:
            portfolio = PortfolioService._instantiate(params)
            params_new = portfolio.transform()

            updated = PortfolioRepository.update_portfolio(conn, params_new)
            return {"status": True, "data": updated}
        except Exception as e:
            return {"status": False, "error": str(e)}

    @staticmethod
    def _instantiate(params):
        return Portfolio(
            id=params["id"],
            name=params["name"],
            experience=params["experience"],
            skills=params["skills"],
            companies=params["companies"],
        )
