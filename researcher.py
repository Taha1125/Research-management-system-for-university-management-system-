class Researcher:
    def __init__(self, name, program, research_interests):
        self.name = name
        self.program = program  # MPhil or PhD
        self.research_interests = research_interests

    def __str__(self):
        return f"{self.name} ({self.program}): {', '.join(self.research_interests)}"