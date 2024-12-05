from crewai import Agent
from tools import yt_tool

from dotenv import load_dotenv
load_dotenv()

import os 

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL_NAME= "gpt-3.5-turbo"

from crewai import LLM

# Basic configuration
llm = LLM(model=OPENAI_MODEL_NAME)


#llm = "gpt-4-0125-preview"

## Create a Senior blog content writer

blog_reasearcher = Agent(name="blog_reasearcher",
    role='blog_reasearcher from Youtube videos',
    goal='Get the relevent video content for the topic {topic} from youtube videos',
    verbose=True,
    memory=True,
    backstory=(
        "You are an Expert in an understanding Data Science, Machine Learning, Deep Learning and Gen AI and providing suggestions"
        ),
    tools=[],
    llm = llm,
    allow_delegation=True
    )

## Create a Senior blog content writer
blog_writer = Agent(
    name="blog_writer",
    role='blog_writer from Youtube videos',
    goal='Narrate complelling tech stories about the video {topic} from youtube channel',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplyfying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner" 
        ),
    tools=[],
    llm=llm,
    allow_delegation=False
)