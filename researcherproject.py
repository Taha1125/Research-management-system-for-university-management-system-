from researcher import Researcher

class ResearchProject:
    def __init__(self, title, description, researchers=None):
        self.title = title
        self.description = description
        self.researchers = researchers if researchers else []

    def add_researcher(self, researcher):
        self.researchers.append(researcher)

    def __str__(self):
        researchers_str = ", ".join([researcher.name for researcher in self.researchers])
        return f"Project: {self.title}\nDescription: {self.description}\nResearchers: {researchers_str}"