from crewai import Crew, Process
from agents import drafting_agent, seo_optimization_agent, editing_refinement_agent, chief_agent
from tasks import drafting_task, seo_task, chief_task, editing_task

class LinkedInPostGenerator:
    def __init__(self):
        self.crew = Crew(
            agents=[drafting_agent, editing_refinement_agent, seo_optimization_agent, chief_agent],
            tasks=[drafting_task, editing_task, seo_task, chief_task],
            process=Process.sequential,
            memory=True,
            cache=True,
            max_rpm=100,
            share_crew=True
        )

    def generate_post(self, topic):
        result = self.crew.kickoff(inputs={'topic': topic})
        return result

if __name__ == "__main__":
    generator = LinkedInPostGenerator()

    text = input("Enter here: ")

    result = generator.generate_post(topic=text)
    print(result)
