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

    @staticmethod
    def validate_store(data: dict) -> dict:
        errors = {}

        name = data.get("name")
        if not name or not isinstance(name, str):
            errors["name"] = "name is required and must be string."

        experience = data.get("experience")
        if not experience or not isinstance(experience, int):
            errors["experience"] = "experience is required and must be integer."

        skills = data.get("skills")
        if not skills or not isinstance(skills, list):
            errors["skills"] = "skills is required and must be list."

        companies = data.get("companies")
        if not companies or not isinstance(companies, list):
            errors["companies"] = "companies is required and must be dict."

        if errors:
            raise ValidationError(errors)

        return data


"""
noted: improvise in the future. validation: required|data_type|etc
"""


class ValidationError(Exception):
    pass
