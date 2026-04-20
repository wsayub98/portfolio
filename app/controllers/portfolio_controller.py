import json
from app.services.portfolio_service import PortfolioService
from app.validators.portfolio_validator import PortfolioValidator, ValidationError
from core.database import Database
from devtools import debug


class PortfolioController:
    @staticmethod
    def index(params=None):
        conn = None
        try:
            conn = Database.connect()

            portfolio_service = PortfolioService.get_portfolio(conn)

            return json.dumps(portfolio_service)
        except Exception as e:
            return json.dumps({"status": False, "error": str(e)})
        finally:
            if conn:
                conn.close()

    @staticmethod
    def store(params: dict):
        conn = None
        try:
            conn = Database.connect()

            params = PortfolioValidator.validate_store(params)
            service = PortfolioService.create_portfolio(conn, params)
            conn.commit()

            return json.dumps(service)
        except Exception as e:
            if conn:
                conn.rollback()
            return json.dumps({"status": False, "error": str(e)})
        finally:
            if conn:
                conn.close()

    @staticmethod
    def update(params: dict):
        conn = None
        try:
            conn = Database.connect()

            params = PortfolioValidator.validate(params)
            service_update = PortfolioService.update_portfolio(conn, params)
            conn.commit()

            return json.dumps(service_update)
        except ValidationError as e:
            return json.dumps({"status": False, "error": str(e)})
        except Exception as e:
            if conn:
                conn.rollback()
            return json.dumps({"status": False, "error": str(e)})
        finally:
            if conn:
                conn.close()

    @staticmethod
    def destroy(params: dict):
        conn = None
        try:
            conn = Database.connect()
            params = PortfolioValidator.validate(params)
            service = PortfolioService.delete_portfolio(conn, params)
            conn.commit()

            return json.dumps(service)
        except ValidationError as e:
            return json.dumps({"status": False, "error": str(e)})
        except Exception as e:
            if conn:
                conn.rollback()
            return json.dumps({"status": False, "error": str(e)})
        finally:
            if conn:
                conn.close()
