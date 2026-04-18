import json


class Portfolio:
    def __init__(self, id: int | None, name, experience, skills, companies):
        self.id = id
        self.name = name
        self.experience = experience
        self.skills = skills
        self.companies = companies

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "experience": self.experience,
            "skills": self.skills,
            "companies": self.companies,
        }

    def transform(self):
        return {
            "id": self.id,
            "name": self.name,
            "experience": self.experience,
            "skills": self.skills,
            "companies": json.dumps(self.companies),
        }
