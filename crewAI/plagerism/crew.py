from crewai import Crew, Process
from agents import input_processing_agent,ai_generated_content_detection_agent,web_based_plagiarism_detection_agent,document_similarity_agent,source_attribution_agent,report_generation_agent
from tasks import input_processing_task,ai_generated_content_detection_task,web_based_plagiarism_detection_task,document_similarity_task,source_attribution_task,report_generation_task

class Plagerism:
    def __init__(self):
        self.agents = [input_processing_agent,ai_generated_content_detection_agent,web_based_plagiarism_detection_agent,document_similarity_agent,source_attribution_agent,report_generation_agent]

        self.tasks = [input_processing_task,ai_generated_content_detection_task,web_based_plagiarism_detection_task,document_similarity_task,source_attribution_task,report_generation_task]
        
        self.crew = Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            memory=True,
            cache=True,
            max_rpm=200,  # Increase max RPM (requests per minute) limit
            max_iterations=1000,  # Increase max iterations allowed per agent
            max_execution_time=600  
        )

    def run(self):
        text = "This Data Science Tutorial with Python tutorial will help you learn the basics of Data Science along with the basics of Python according to the need in 2024 such as data preprocessing, data visualization, statistics, making machine learning models, and much more with the help of detailed and well-explained examples. This tutorial will help beginners and trained professionals master data science with Python."
        result = self.crew.kickoff(inputs={'topic': text})
        print(result)
            


if __name__ == "__main__":
    crew_runner = Plagerism()
    crew_runner.run()
