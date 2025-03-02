# Import necessary modules and classes
from crewAI.facebook.agents import (
    facebook_drafting_agent,
    facebook_refinement_agent,
    facebook_seo_agent,
    facebook_content_compiler,
    facebook_image_creator,
    facebook_content_formatter
)
from crewai import Task

# Drafting Task for Facebook
drafting_task_facebook = Task(
    description=(
        "Generate a draft for a Facebook post on {topic}. "
        "Create content that is informative, engaging, and aligns with current trends or developments in {topic}. "
        "Include a mix of text and ideas for multimedia elements (like images, videos, or links) to enhance the post's engagement."
    ),
    expected_output=(
        "A compelling draft Facebook post on {topic}, capturing the essence of {topic} and resonating with Facebook users. "
        "The draft should include suggestions for multimedia elements that support the content and enhance its appeal."
    ),
    agent=facebook_drafting_agent,
)

# Editing Task for Facebook
editing_task_facebook = Task(
    description=(
        "Refine and polish a draft Facebook post on {topic}. "
        "Focus on enhancing grammar, clarity, and overall readability while ensuring alignment with the intended style and engagement goals. "
        "Ensure the content is structured to maximize readability and interaction, and consider the inclusion of appropriate media."
    ),
    expected_output=(
        "A polished Facebook post on {topic}, improved in grammar, clarity, and readability. "
        "The post effectively communicates the intended message while maintaining a style that resonates with Facebook users. "
        "The content should be engaging and ready for integration with multimedia elements."
    ),
    agent=facebook_refinement_agent,
)

# SEO Task for Facebook
seo_task_facebook = Task(
    description=(
        "Optimize a Facebook post on {topic} for discoverability and engagement. "
        "Identify and integrate relevant keywords and tags to improve visibility on Facebook's platform. "
        "Consider the use of effective SEO strategies to enhance the post's reach and engagement."
    ),
    expected_output=(
        "An optimized Facebook post on {topic}, enhanced with relevant keywords and tags. "
        "The post is structured to maximize discoverability and engagement, appealing to the target audience effectively. "
        "Include the top 5 keywords and tags that best represent the content and attract the intended audience."
    ),
    agent=facebook_seo_agent,
)

# Chief Task for Facebook
chief_task_facebook = Task(
    description=(
        "Aggregate and compile the final results from various tasks into a cohesive Facebook post. "
        "Integrate content generated by drafting, refinement, SEO optimization, and media selection into a unified and engaging presentation."
    ),
    expected_output=(
        "A finalized Facebook post on {topic}, incorporating outputs from drafting, refinement, SEO optimization, and media selection. "
        "The post should be engaging, visually appealing, and tailored to resonate with the target audience on Facebook. "
        "End the post with a call-to-action inviting viewers to engage with the content, such as commenting, sharing, or clicking a link."
    ),
    agent=facebook_content_compiler,
)

# Image Creation Task for Facebook
image_generate_task_facebook = Task(
    description=(
        "Create 3 visually compelling images that capture and enhance the essence of a Facebook post about {topic}. "
        "Each image should be relevant to the content of the post, reflecting the tone and aesthetic of Facebook. "
        "Focus on creating images that add visual appeal and effectively convey the message to engage the Facebook audience. "
        "Describe each image in a paragraph, detailing its relevance and how it captures the audience's attention."
        "Here are some examples for you to follow:"
        "- a vibrant community event, with people interacting, smiling, and engaging, in high resolution, wide shot"
        "- a sleek, modern product display, showcasing the product in use, in a crisp and professional manner, close-up shot"
        "- a beautiful natural landscape with rich colors, capturing the essence of the location, in 4K quality, wide shot"

        "Think creatively and ensure that the images are designed to stand out and engage the Facebook audience."
    ),
    agent=facebook_image_creator,
    expected_output=(
        "Three visually compelling images that represent and complement the Facebook post on {topic}. "
        "Each image should be professional, engaging, and aligned with Facebook's aesthetic and tone. "
        "Include a paragraph describing each image, explaining its relevance and how it captures the audience's attention."
    ),
)

# Formatting Task for Facebook
format_content_task_facebook = Task(
    description=(
        "Format the Facebook content in a professional and engaging manner, including the selected media. "
        "Ensure the post is well-structured, visually appealing, and optimized for readability and interaction. "
        "Format the content in Markdown, if applicable, and include the chosen image description at the end of the post."
    ),
    agent=facebook_content_formatter,
    expected_output=(
        "A well-formatted Facebook post that is around 100 words in the beginning, choosing one description among the images generated and attaching it to the end of the post content. "
        "The content should be formatted in Markdown, ensuring it is engaging and ready for publication."
    ),
    context=[chief_task_facebook, image_generate_task_facebook],
    async_execution=False,
    output_file="outputs/facebook/post.md"
)
