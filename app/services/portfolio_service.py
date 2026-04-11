from app.models.portfolio import Portfolio


class PortfolioService:
    @staticmethod
    def get_portfolio():
        portfolio = Portfolio(
            name="Ronaldo",
            experience=4,
            skills=["PHP", "Laravel", "CodeIgniter", "Drupal"],
            companies=[
                {"name": "Company A", "role": "Developer"},
                {"name": "Company B", "role": "PHP Developer"},
                {"name": "Company C", "role": "Laravel Developer"},
            ],
        )

        data = portfolio.to_dict()

        return {
            "status": True,
            "data": data,
        }
