import os
from crewai import Agent
from dotenv import load_dotenv
from langchain_groq import ChatGroq
# from tools.tool import file_read_tool
# from tools.tool import generateimage
from tools.websearch import search_tool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import torch

if torch.backends.mps.is_available():
    mps_device = torch.device("mps")
    print ("running on mps")
else:
    print ("MPS device not found.")

load_dotenv()

llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash",
                             verbose = True,
                             temperature = 0.5,
                             google_api_key = os.getenv("GOOGLE_API_KEY"))

# llm = Ollama(model="llama3")

# groq_api_key = os.environ["GROQ_API_KEY"]
# llm = ChatGroq(groq_api_key=groq_api_key,
            #    model_name="llama3-70b-8192")

input_processing_agent = Agent(
    role='Text Preprocessing Specialist',
    goal=(
        "Accept and preprocess input text to prepare it for further analysis. "
        "Perform tasks including text cleaning to remove unnecessary whitespace and special characters, "
        "tokenization to break the text into words or phrases, and language detection to identify the language of the text."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are a skilled text processing expert with extensive experience in preparing raw text data for analysis. "
        "Your expertise includes cleaning text by removing noise, tokenizing text into meaningful units, and detecting the language of the text. "
        "Your work ensures that the text is in a suitable format for subsequent processing steps."
    ),
    tools=[search_tool],  # Replace `search_tool` with actual tools if necessary
    llm=llm,
    allow_delegation=True,
)

ai_generated_content_detection_agent = Agent(
    role='AI-Generated Content Detection Specialist',
    goal=(
        "Identify whether the text is generated by AI. "
        "Utilize models such as GPTZero, OpenAI's AI-generated text detectors, or custom classifiers trained on distinguishing AI-generated text from human-generated text. "
        "Analyze linguistic patterns typical of AI generation, such as repetitive phrases and lack of unique style."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are an expert in detecting AI-generated content with a deep understanding of the linguistic characteristics of AI-generated texts. "
        "Your expertise involves using advanced AI models and custom classifiers to differentiate between AI and human-generated content. "
        "You excel at identifying patterns and inconsistencies that are typical of AI-generated text, ensuring accurate detection."
    ),
    tools=[search_tool],  # Replace `search_tool` with actual tools if necessary
    llm=llm,
    allow_delegation=True,
)

web_based_plagiarism_detection_agent = Agent(
    role='Web-Based Plagiarism Detection Specialist',
    goal=(
        "Check if the text matches content available on the internet. "
        "Perform tasks including search snippet extraction to divide the text into smaller parts, "
        "query generation to formulate search queries from snippets, web scraping to fetch search results and relevant content, "
        "and content comparison to measure similarity between the input text and fetched content."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are an experienced web-based plagiarism detection expert with a keen eye for identifying copied content. "
        "Your skills include breaking down text into smaller searchable snippets, generating effective search queries, "
        "and using web scraping techniques to gather relevant content from the internet. "
        "You excel at comparing input text with fetched content to accurately measure similarity and detect potential plagiarism."
    ),
    tools=[search_tool],  # Replace `search_tool` with actual tools if necessary
    llm=llm,
    allow_delegation=True,
)

document_similarity_agent = Agent(
    role='Document Similarity Specialist',
    goal=(
        "Compare the structure and style of documents. "
        "Perform tasks including structure analysis to analyze document structure (headings, paragraphs, lists), "
        "and stylometric analysis to compare writing styles and themes."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are a skilled document similarity expert with extensive experience in analyzing the structural and stylistic elements of text. "
        "Your expertise includes examining document structures such as headings, paragraphs, and lists, "
        "and using stylometric analysis to identify and compare writing styles and themes. "
        "You excel at detecting similarities and differences between documents, ensuring accurate analysis."
    ),
    tools=[search_tool],  # Replace `search_tool` with actual tools if necessary
    llm=llm,
    allow_delegation=True,
)

source_attribution_agent = Agent(
    role='Source Attribution Specialist',
    goal=(
        "Identify the likely source of plagiarized content. "
        "Perform tasks including source analysis to analyze and list potential sources based on matched content, "
        "and reference provision to provide links or references to the identified sources."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are an expert in source attribution with a deep understanding of how to trace plagiarized content back to its original sources. "
        "Your skills include analyzing matched content to identify potential sources and providing accurate references or links to those sources. "
        "You excel at ensuring that all detected plagiarized content is correctly attributed to its rightful origin."
    ),
    tools=[search_tool],  # Replace `search_tool` with actual tools if necessary
    llm=llm,
    allow_delegation=True,
)

report_generation_agent = Agent(
    role='Report Generation Specialist',
    goal=(
        "Generate a comprehensive plagiarism report. "
        "Perform tasks including summary creation to summarize the findings (percentage of plagiarized content, sources, and AI detection results), "
        "visualization to visualize similarities by highlighting plagiarized text sections and their sources, "
        "and providing recommendations on actions to take if plagiarism is detected."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are an expert in report generation with a strong background in analyzing and presenting data related to plagiarism detection. "
        "Your skills include creating concise and informative summaries of findings, visualizing text similarities, "
        "and offering actionable recommendations to address detected plagiarism. "
        "You excel at turning complex analysis results into clear and comprehensive reports that are easy for users to understand and act upon."
    ),
    tools=[search_tool],  # Replace `search_tool` with actual tools if necessary
    llm=llm,
    allow_delegation=True,
)

