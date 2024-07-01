from crewai import Crew,Process
from agents import preprocessing_agent, topic_extraction_agent, summarization_agent, evaluation_agent
from tasks import preprocessing_task, topic_extraction_task, summarization_task, evaluation_task

class Summarizer:
    def __init__(self):
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
        result = self.crew.kickoff(inputs={'topic': 
"""In the realm of artificial intelligence, machine learning has emerged as a powerful tool. It enables computers to learn from data and make decisions or predictions based on that learning, without being explicitly programmed. This ability has revolutionized industries ranging from healthcare to finance and entertainment.

Machine learning algorithms can be broadly categorized into supervised learning, unsupervised learning, and reinforcement learning. Supervised learning involves training a model on labeled data, where the algorithm learns to map input data to the correct output. Unsupervised learning deals with finding hidden patterns or intrinsic structures in input data without labeled responses. Reinforcement learning focuses on learning how to make sequences of decisions to maximize a cumulative reward.

Deep learning, a subset of machine learning, has gained prominence due to its ability to automatically learn hierarchical representations of data. Neural networks, inspired by the human brain's structure, are foundational to deep learning. They consist of interconnected layers of nodes, where each node performs a mathematical operation.

Applications of AI and machine learning are vast and diverse. In healthcare, AI aids in diagnosing diseases from medical images and predicting patient outcomes. Financial institutions use machine learning for fraud detection and algorithmic trading. Entertainment platforms utilize recommendation systems powered by AI to personalize content for users.

Despite its transformative potential, AI also raises ethical concerns. Issues such as bias in algorithms, data privacy, and the impact on jobs are hotly debated. Ethical frameworks and regulations are being developed to address these challenges and ensure responsible AI deployment.

Looking ahead, AI's evolution promises continued innovation across industries. Advances in natural language processing, computer vision, and autonomous systems will shape the future landscape. Collaboration between researchers, policymakers, and industry leaders is crucial to harness AI's benefits while mitigating risks."""})
        return result

if __name__ == "__main__":
    summarizer = Summarizer()
    # topic = input("Enter the topic: ")
    result = summarizer.run()
    print(result)
