import json
from app.models.portfolio import Portfolio
from app.repositories.portfolio_repository import PortfolioRepository
from devtools import debug


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
    def create_portfolio(conn, params):
        try:
            model = PortfolioService._instantiate(params)
            params_new = model.transform()
            created = PortfolioRepository.create(conn, params_new)

            return {
                "status": True,
                "data": created,
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
            updated = PortfolioRepository.update(conn, params_new)

            return {
                "status": True,
                "data": updated,
            }
        except Exception as e:
            return {
                "status": False,
                "error": str(e),
            }

    @staticmethod
    def delete_portfolio(conn, params):
        try:
            deleted = PortfolioRepository.delete(conn, params)

            return {"status": True, "data": deleted}
        except Exception as e:
            return {
                "status": False,
                "error": str(e),
            }

    @staticmethod
    def _instantiate(params):
        return Portfolio(
            id=params.get("id"),
            name=params.get("name"),
            experience=params.get("experience"),
            skills=params.get("skills", []),
            companies=params.get("companies", []),
        )
