from crewai import Crew ,Process
from agents import content_compiler,content_formatter,drafting_agent,image_creator,refinement_agent,seo_agent
from tasks import drafting_task_instagram,editing_task_instagram,seo_task_instagram,chief_task_instagram,image_generate_task_instagram,format_content_task_instagram

class InstagramPostGenerator:
    def __init__(self):
        self.crew = Crew(
            agents=[drafting_agent,refinement_agent,seo_agent,content_compiler,image_creator,content_formatter],
            tasks=[drafting_task_instagram,editing_task_instagram,seo_task_instagram,chief_task_instagram,image_generate_task_instagram,format_content_task_instagram],
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
    generator = InstagramPostGenerator()

    text = input("Enter here: ")

    result = generator.generate_post(topic=text)
    print(result)
