from crewai import Task
from .agents import preprocessing_agent,topic_extraction_agent,summarization_agent,evaluation_agent

preprocessing_task = Task(
    description=("Clean and preprocess the raw text data related to {topic}. Remove noise, handle formatting inconsistencies, and prepare the text for efficient summarization."),
    expected_output=("Cleaned and preprocessed text data ready for summarization on {topic}."),
    agent=preprocessing_agent,  
)

topic_extraction_task = Task(
    description=("Identify key topics or themes within the text related to {topic} to guide the summarization process. Extract essential information to ensure comprehensive coverage in the summary."),
    expected_output=("Key topics or themes identified for summarization on {topic}."),
    agent=topic_extraction_agent,  
)

summarization_task = Task(
    description=("Generate a concise and coherent summary of the text related to {topic} using advanced natural language processing techniques. Ensure the summary captures the main points effectively."),
    expected_output=("Concise and coherent summary of {topic} generated."),
    agent=summarization_agent,  
)

evaluation_task = Task(
    description=("Format the generated summary in impresive markdown"),
    expected_output=('The entire summary must be formatted and written  beautifully in markdown language'),
    agent=evaluation_agent,
    async_execution=False,
    output_file="outputs/summarizer/summarized.md"
)