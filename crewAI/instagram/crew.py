from crewai import Crew ,Process
from agents import instagram_content_compiler,instagram_content_formatter,instagram_drafting_agent,instagram_image_creator,instagram_refinement_agent,instagram_seo_agent
from tasks import drafting_task_instagram,editing_task_instagram,seo_task_instagram,chief_task_instagram,image_generate_task_instagram,format_content_task_instagram

class InstagramPostGenerator:
    def __init__(self):
        self.crew = Crew(
            agents=[instagram_drafting_agent,instagram_refinement_agent,instagram_seo_agent,instagram_content_compiler,instagram_image_creator,instagram_content_formatter],
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
