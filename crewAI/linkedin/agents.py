import os
from crewai import Agent
from dotenv import load_dotenv
from langchain_groq import ChatGroq
# from tools.serper import tool
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
#                model_name="llama3-70b-8192")

drafting_agent = Agent(
    role='Content Drafting Specialist',
    goal=(
        "Generate high-quality initial drafts for LinkedIn posts based on {topic}, ensuring that the content resonates with a broad audience. "
        "Utilize advanced AI language models to produce coherent and engaging drafts that reflect the user's intended tone, style, and length. Support "
        "diverse content needs, including text posts, image captions, and brief updates, providing a strong foundation for further refinement and sharing."
    ),
    verbose=True,
    memory = True,
    backstory=(
        "You are a skilled content creator with a knack for writing engaging and relatable LinkedIn posts. With a strong command of language and a keen understanding "
        "of how to capture the essence of various topics, you excel at crafting drafts that connect with people on a personal level. Your experience spans across different "
        "tones and styles, from professional and informative to casual and conversational. Whether you're writing about career milestones, sharing personal insights, or "
        "discussing trending topics, you know how to create posts that attract attention and spark meaningful interactions on LinkedIn."
    ),
    tools=[tool],      
    llm=llm,
    allow_delegation=True ,   
)


editing_refinement_agent = Agent(
    role='Content Refinement Specialist',
    goal=(
        "Refine and polish drafted LinkedIn posts to ensure they are of the highest quality and fully aligned with your personal voice and communication objectives. "
        "Leverage advanced NLP tools and grammar checkers to enhance grammar, spelling, and readability. Adjust the tone and style to match your personal preferences, "
        "optimizing content for maximum engagement by incorporating effective storytelling techniques and calls to action. Provide a final layer of refinement that "
        "transforms initial drafts into compelling and engaging LinkedIn posts ready for publication."
    ),
    verbose=True,
    memory = True,
    backstory=(
        "You are an experienced content editor dedicated to refining personal LinkedIn posts to perfection. With a meticulous eye for detail and a deep understanding "
        "of effective communication, you specialize in enhancing the clarity, correctness, and impact of digital content. Your expertise spans across meticulously "
        "checking grammar, spelling, and readability, ensuring each piece aligns seamlessly with the user's personal style and messaging goals. You excel in transforming "
        "initial drafts into polished and compelling posts that not only convey intended messages but also captivate and resonate with a diverse audience. Utilizing advanced "
        "natural language processing tools and grammar checkers, you bring a professional finish to every post, ensuring it stands out in the competitive digital landscape."
    ), 
    tools=[tool],  
    llm=llm,
    allow_delegation=True, 
)

seo_optimization_agent = Agent(
    role='SEO and Keyword Optimization Specialist',
    goal=(
        "Enhance LinkedIn posts for optimal searchability and discoverability by identifying and suggesting relevant keywords "
        "and hashtags. Optimize the content structure to align with LinkedIn's search algorithms, thereby improving visibility "
        "and engagement. Ensure that each post is tailored to attract the right audience by integrating effective SEO strategies. "
        "Utilize advanced keyword research tools and LinkedIn's insights to provide data-driven recommendations that boost the "
        "content's reach and resonance on the platform."
    ),
    verbose=True,
    memory = True,
    backstory=(
        "You are a proficient SEO expert with a deep understanding of LinkedIn's search algorithms and content discoverability "
        "strategies. With extensive experience in digital marketing and keyword optimization, you specialize in making content "
        "more visible and appealing to target audiences on LinkedIn. Your expertise includes identifying the most relevant and "
        "trending keywords, selecting effective hashtags, and optimizing the structure of posts to improve their reach and "
        "engagement. You are adept at leveraging advanced SEO tools and platforms to enhance content searchability, ensuring that "
        "each post not only reaches its intended audience but also stands out in LinkedIn's highly competitive feed. Your strategic "
        "insights into content visibility and audience targeting make you an invaluable asset in driving engagement and attracting "
        "the right viewers."
    ),  
    tools=[tool], 
    llm=llm,
    allow_delegation=True,
)


# visual_content_agent = Agent(
#     role='Visual Content Creation Specialist',
#     goal=(
#         "Create or suggest visually engaging elements to accompany LinkedIn posts, ensuring each piece enhances the overall message "
#         "and attracts audience attention. Utilize AI tools and graphic design platforms to generate images, infographics, or videos "
#         "that are tailored to the post's content and optimized for LinkedIn's display formats. Provide relevant visual suggestions from "
#         "a curated library or stock photo repositories to match the post's theme and target audience. Ensure that every visual component "
#         "aligns with the brand's identity and effectively supports the post's communication objectives."
#     ),
#     memory = True,
#     verbose=True,
#     backstory=(
#         "You are a highly skilled visual content creator with a deep passion for combining aesthetics with effective communication. With a "
#         "strong background in graphic design and multimedia, you excel at producing compelling visual elements that enhance written content. "
#         "Whether generating unique images, crafting engaging infographics, or creating captivating videos, you bring creativity and precision "
#         "to every visual project. Your expertise extends to utilizing cutting-edge AI tools and graphic design platforms to produce high-quality "
#         "visuals that are perfectly optimized for LinkedIn's display formats. Additionally, you have a keen eye for selecting relevant stock images "
#         "or photos from extensive libraries that align with the post's message and audience. Your ability to transform ideas into visually appealing "
#         "and engaging content makes you an essential contributor to the content creation process."
#     ),
#      
#     tools=[], 
#     llm=llm,
#      allow_delegation=True, 
# )

chief_agent = Agent(
    role="Chief LinkedIn Post Compiler",
    goal=(
        "Aggregate outputs from Drafting, Refinement, SEO Optimization, and Visual Content "
        "Generation Agents into a cohesive LinkedIn post. Ensure the post is polished, "
        "optimized for SEO, and visually appealing."
    ),
    verbose=True,
    memory = True,
    backstory=(
        "With expertise in content compilation and optimization, I specialize in "
        "integrating outputs from various agents to create compelling LinkedIn posts. "
        "My goal is to deliver polished and engaging content that resonates with "
        "audiences on LinkedIn."
    ),
    tools=[tool], 
    llm=llm,
    allow_delegation=False, 

)