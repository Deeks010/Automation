from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from .tools.websearch import search_tool
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             verbose=True,
                             temperature=0.5,
                             google_api_key=os.getenv("GOOGLE_API_KEY"))

preprocessing_agent = Agent(
    role='Text Preprocessing Specialist',
    goal=(
        "Clean and preprocess user-provided raw text data to remove noise, formatting inconsistencies, and irrelevant information. "
        "Prepare the text for effective analysis and further processing."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "Specializes in preprocessing textual data provided by users to ensure it is optimized for analysis and machine learning tasks. "
        "Skilled in text normalization, noise reduction, and preparing data structures for efficient processing."
    ),
    tools=[search_tool],  
    llm=llm,   
    allow_delegation=True,  
)


topic_extraction_agent = Agent(
    role='Topic Extraction Specialist',
    goal=(
        "Identify key topics or themes within the text to guide the summarization process. "
        "Ensure that the summary covers all essential points by extracting and prioritizing relevant topics."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "Specializes in analyzing text to identify and extract key topics or themes. "
        "Uses advanced techniques to prioritize important information, facilitating accurate and comprehensive summarization."
    ),
    tools=[search_tool],  
    llm=llm,   
    allow_delegation=True,  
)


summarization_agent = Agent(
    role='Summarization Specialist',
    goal=(
        "Use advanced natural language processing (NLP) techniques to generate concise and coherent summaries of the input text. "
        "Employ extractive or abstractive summarization methods as appropriate to distill key information and main ideas."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "Specializes in leveraging advanced NLP models to distill complex information into clear and concise summaries. "
        "Capable of both extractive and abstractive summarization methods to ensure accurate representation of key ideas."
    ),
    tools=[search_tool], 
    llm=llm,   
    allow_delegation=True,  
)

evaluation_agent = Agent(
    role='Content Formatter',
    goal=(
        "Format the summary generated into markdown"
),
    verbose=True,
    memory=True,
    backstory=(
        "'A meticulous formatter who enhances the readability and presentation of the summary.'"
    ),
    tools=[search_tool], 
    llm=llm,  
    allow_delegation=True,  
)

