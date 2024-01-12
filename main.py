from researcher import Researcher
from researcherproject import ResearchProject
from researchmanagementsystem import ResearchManagementSystem


taha_mphil = Researcher("Taha", "MPhil", ["Advance Machine Learning"])
hamza_phd = Researcher("Hamza", "PhD", ["Robotics"])


rms = ResearchManagementSystem()


rms.add_researcher(taha_mphil)
rms.add_researcher(hamza_phd)


project1 = rms.create_research_project("Advance Machine Learning", "Exploring the latest advancements in ML", [taha_mphil])

project2 = rms.create_research_project("Robotics", "Applications of robotics in various domains", [hamza_phd])

rms.print_research_details()