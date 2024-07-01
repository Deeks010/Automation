from crewai import Crew,Process
from .agents import preprocessing_agent, topic_extraction_agent, summarization_agent, evaluation_agent
from .tasks import preprocessing_task, topic_extraction_task, summarization_task, evaluation_task

class Summarizer:
    def __init__(self,voice_assistant):
        self.voice_assistant = voice_assistant
        self.crew = Crew(
            agents=[
                preprocessing_agent,
                topic_extraction_agent,
                summarization_agent,
                evaluation_agent
            ],
            tasks=[
                preprocessing_task,
                topic_extraction_task,
                summarization_task,
                evaluation_task
            ],
            process=Process.sequential,
            memory=True,
            cache=True,
            max_rpm=100,
            share_crew=True
        )

    def run(self):
        self.voice_assistant.speak("Enter the content to be summarized: ")
        text = input(": ")
        if len(text) > 1:
            result = self.crew.kickoff(inputs={'topic': text})
            print(result)


