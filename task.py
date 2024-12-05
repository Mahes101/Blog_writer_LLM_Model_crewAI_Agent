from crewai import Task
from tools import yt_tool
from agents import blog_reasearcher, blog_writer

## Research Task
research_task = Task(
    description=(
        "Identify the video {topic}"
        "Get detailed information about the video from the youtube channel."
        ),
    expected_output="A comprehensive 3 paragraphs long report based on the {topic} from the video content.",
    tools=[yt_tool],
    agent=blog_reasearcher
)

## Write Task with a language configuration model
write_task = Task(
    description="Get the info from the channel on the {topic}. ",
    expected_output="Summarize the info from the youtube channel video on the {topic} and create the content for the blog.",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file="new-blog-post.md"
)