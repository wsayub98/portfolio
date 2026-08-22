import json


class Portfolio:
    def __init__(self, id: int | None, name, experience, skills, companies, projects):
        self.id = id
        self.name = name
        self.experience = experience
        self.skills = skills
        self.companies = companies
        self.projects = projects

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "experience": self.experience,
            "skills": self.skills,
            "companies": self.companies,
            "projects": self.projects,
        }

    def transform(self):
        return {
            "id": self.id,
            "name": self.name,
            "experience": self.experience,
            "skills": self.skills,
            "companies": json.dumps(self.companies),
            "projects": json.dumps(self.projects),
        }
