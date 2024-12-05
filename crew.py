from crewai import Crew, Process
from tools import yt_tool
from agents import blog_reasearcher, blog_writer
from task import research_task, write_task



##Forming Tech focused with some enhanced configurations

crew = Crew(
    agents=[blog_reasearcher, blog_writer],
    tasks=[research_task, write_task],
    processes=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=3,
    share_crew=True
)

## Start the Execution Process with enhanced feedback

result = crew.kickoff(inputs={'topic':'AI VS ML VS DL VS Data Science'})

print(result)