from researcher import Researcher
from researcherproject import ResearchProject

class ResearchManagementSystem:
    def __init__(self):
        self.researchers = []
        self.research_projects = []

    def add_researcher(self, researcher):
        self.researchers.append(researcher)

    def create_research_project(self, title, description, researchers=None):
        project = ResearchProject(title, description, researchers)
        self.research_projects.append(project)
        return project

    def print_research_details(self):
        for researcher in self.researchers:
            print(researcher)
            associated_projects = [project for project in self.research_projects if researcher in project.researchers]
            for project in associated_projects:
                print(project)
            print("\n")