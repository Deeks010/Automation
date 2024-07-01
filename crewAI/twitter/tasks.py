from crewai import Task
from .agents import trending_topic_researcher_agent,content_researcher_agent,creative_content_creator_agent

topic_analysis =  Task(
		description=("""
			Find trending searches/topics related to the niche:{topic}, in the past 1 month.
			
			Compile this information into a structured list of topics and searches. 
			Each item in the list should include a brief description and relevance score 
			to guide content creation efforts around these trends. 
			Ensure the final list of trending topics is clear, actionable, and ready to inform strategic 
			content development."""),
		expected_output="List of trending topics and searches in the format: [topic1, topic2, ...]",
		agent=trending_topic_researcher_agent
	)

content_research = Task(
		description=("""
			Do indepth research of all the trending topics and searches.
			For each trending topics related to - {topic}, search for 
				the most authoritative and relevant websites within the {topic} niche.
				Create a list of websites to visit for each trending topic.
				
				Compile comprehensive details for each topic, including:
					- A summary of the topic's significance.
					- Statistical data or recent studies related to the topic.
					- Current discussion points or controversies.
					- Predictions or trends that indicate how this topic might evolve.
					- Possible angles or hooks for content creation.
					
				Maximum number of google searches you can do is 10."""),
		expected_output=("""\
						A map of trending topic to structured research details for that topic.
					This report will serve as a foundation 
					for creating targeted, informed, and engaging twitter posts"""),
		agent=content_researcher_agent
	)

create_twitter_posts = Task(
		description=("""\
			First filter out the topics that are related to {topic} and remove the ones not related.
			Next, Create 5 Twitter posts related to {topic} using the content research done for each of 
				the trending topic/search and craft engaging, valuable and actionable Twitter posts that are ready to 
				be published. Try to use the following structure:
				1. Start with a Strong Hook: Begin with an intriguing question, startling fact, or 
						engaging statement to grab attention.
				2. Add Value or Insight: Incorporate useful and relevant information such as statistics, 
						quick tips, or enlightening observations or interesting facts.
				3. Call to Action (CTA): Encourage readers to engage further by trying out a tip, 
						sharing the post, or leaving comments. And give them some useful relevant link to
						blog, website or video.
				4. Use Appropriate Hashtags: Include 2-3 relevant hashtags to enhance visibility 
						but avoid overuse.

				Example Post:
				"Did you know that 10 minutes of meditation daily can boost your focus significantly? 
					🧘‍♂️✨ Consistent, brief meditation improves concentration and stress levels, even during work hours. 
					It's not just good for your mind—it's a productivity booster!
					Give it a try tomorrow morning, and see the difference for your! 
					🌞🚀 Share this tip with someone who needs a focus boost. 
					#ProductivityHacks #Mindfulness #MentalHealth"

			Note: Ensure each post is standalone and provides all necessary context, as users might 
					not see other related posts. Compile these posts into a document or list, with each entry clearly 
					labeled with the topic it addresses. This document will be used by another agent to handle 
					the actual posting on Twitter.
					
			After executing this task, you should print the output.
			Task should return an array containing all the 5 twitter posts"""),
		expected_output="The entire post content must be formatted in markdown containing the twitter posts, not as list of posts andnit should not contain any brackets for the refinement "
		"The twitter post that you generated must be the final tweet."
		"Should not need any alterations",
		output_file="outputs/tweet.md"  ,
		agent=creative_content_creator_agent
	)

# def publish_twitter_posts(, agent, tweets):
# 	return Task(
# 		description=("""\
# 			Print all the tweets created by previous task in the logs.
# 			Publish all the tweets to Twitter.
# 			"""),
# 		expected_output="Posting status of all the tweets.",
# 		agent=agent
# 	)