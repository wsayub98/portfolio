class Portfolio:
    def __init__(self, name, experience, skills, companies):
        self.name = (name,)
        self.experience = (experience,)
        self.skills = (skills,)
        self.companies = companies

    def to_dict(self):
        return {
            "name": self.name,
            "experience": self.experience,
            "skills": self.skills,
            "companies": self.companies,
        }
