import json


class Portfo:
    def __init__(self, name, experience, skills, companies):
        self.name = name
        self.experience = experience
        self.skills = skills
        self.companies = companies

    def to_dict(self):
        return {
            "name": self.name,
            "experience_years": self.experience,
            "skills": self.skills,
            "companies": self.companies,
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)


portfolio = Portfo(
    name="Lionel Messi",
    experience=4,
    skills=["php", "mysql", "python"],
    companies=[
        {"name": "Company A", "role": "Senior Backend Developer"},
        {"name": "Company B", "role": "Junior Backend Developer"},
    ],
)

print(portfolio.to_json())
