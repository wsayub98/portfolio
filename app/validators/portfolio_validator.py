class PortfolioValidator:
    @staticmethod
    def validate(data: dict) -> dict:
        errors = {}

        id = data.get("id")
        if not id or not isinstance(id, int):
            errors["id"] = "id is required and must be integer."

        if errors:
            raise ValidationError(errors)

        return data


class ValidationError(Exception):
    pass
