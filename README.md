# Research-management-system-for-university-management-system-

class Researcher:
    def __init__(self, name, id, program):
        self.name = name
        self.id = id
        self.program = program
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

class ResearchProject:
    def __init__(self, title, status, supervisor):
        self.title = title
        self.status = status
        self.supervisor = supervisor
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

class ResearchManagementSystem:
    def __init__(self):
        self.researchers = []
        self.projects = []

    def add_researcher(self, researcher):
        self.researchers.append(researcher)

    def add_project(self, project):
        self.projects.append(project)

# Example usage:

# Create researchers
researcher1 = Researcher("John Doe", "R001", "PhD")
researcher2 = Researcher("Jane Smith", "R002", "MPhil")

# Create projects
project1 = ResearchProject("Machine Learning in Healthcare", "Ongoing", "Dr. Smith")
project2 = ResearchProject("Environmental Sustainability", "Completed", "Prof. Johnson")

# Assign projects to researchers
researcher1.add_project(project1)
researcher2.add_project(project2)

# Create tasks for a project
task1 = Task("Literature Review", "2023-12-01")
task2 = Task("Data Collection", "2024-02-15")

# Add tasks to a project
project1.add_task(task1)
project1.add_task(task2)

# Mark a task as completed
task1.mark_as_completed()

# Create a research management system
rms = ResearchManagementSystem()

# Add researchers and projects to the system
rms.add_researcher(researcher1)
rms.add_researcher(researcher2)
rms.add_project(project1)
rms.add_project(project2)
