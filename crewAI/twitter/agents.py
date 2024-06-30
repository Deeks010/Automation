import os
from textwrap import dedent
from crewai import Agent
from tools.search_tools import search_tool
from tools.trends_tools import TrendsTools
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


class ViralContentCreators:
	def __init__(self):
		self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
									verbose=True,
									temperature=0.5,
									google_api_key=os.getenv("GOOGLE_API_KEY"))


	def trending_topic_researcher_agent(self):
		return Agent(
			role="Trending Topic Researcher",
			goal=dedent("""\
				Identify and compile a list of current trending topics and searches
				within a specific niche. This list should provide actionable insights
				and opportunities for strategic engagement, helping to guide content
				creation."""),
			backstory=dedent("""\
				As a Trending Topic Researcher at a cutting-edge digital
				marketing agency, your primary responsibility is to monitor and
				decode the pulse of the market. Using advanced analytical tools,
				you uncover and list the most relevant trends that can influence
				strategic decisions in content creation."""),
			tools=[
					TrendsTools.trending_searches_on_google,
					search_tool
			],
			allow_delegation=False,
			llm=self.llm,
			verbose=True
		)


	def content_researcher_agent(self):
		return Agent(
			role="Content Researcher",
			goal=dedent("""\
				Conduct in-depth research on a topic and compile
				detailed, useful information and insights for each topic. This
				information should be actionable and suitable for creating engaging
				and informed social media posts."""),
			backstory=dedent("""\
				As a Content Researcher at a dynamic social media marketing agency,
				you delve deeply into trending topics to uncover underlying themes and
				insights. Your ability to discern and utilize authoritative and relevant
				sources ensures the content you help create resonates with audiences and
				drives engagement."""),
			tools=[
				search_tool
			],
			llm=self.llm,
			verbose=True
		)


	def creative_content_creator_agent(self):
		return Agent(
			role="Twitter Content Creator",
			goal=dedent("""\
				Develop compelling and innovative content
				for social media campaigns, with a focus on creating
				high-impact Twitter tweet copies. Make sure you don't use tools with the same arguments twice.
			    Make sure not to do more than 3 google searches."""),
			backstory=dedent("""\
				As a Creative Content Creator at a top-tier
				digital marketing agency, you excel in crafting narratives
				that resonate with audiences on social media.
				Your expertise lies in turning marketing strategies
				into engaging stories and visual content that capture
				attention and inspire action."""),
			tools=[
				search_tool
			],
			llm=self.llm,
			verbose=True
		)