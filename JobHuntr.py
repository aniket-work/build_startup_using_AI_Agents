import crewai
from crewai.tools import Tool
import requests
from bs4 import BeautifulSoup
import json

class JobSearchTool(Tool):
    def __init__(self, domain):
        self.domain = domain
        self.description = f"Search for job openings in the {domain} domain"

    def _run(self, query):
        # Search for job openings on popular job sites
        jobs = []
        for site in ["indeed.com", "glassdoor.com", "monster.com"]:
            url = f"https://www.{site}/jobs?q={query}&l=&fromage=any"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            job_listings = soup.find_all("div", {"class": "job-listing"})
            for listing in job_listings:
                title = listing.find("h2").text.strip()
                company = listing.find("span", {"class": "company"}).text.strip()
                location = listing.find("span", {"class": "location"}).text.strip()
                jobs.append({"title": title, "company": company, "location": location})

        return jobs

    def _acrush(self, jobs):
        return json.dumps(jobs, indent=2)

# Define the agents
job_hunter = crewai.Agent(
    role="Job Hunter",
    goal="Find job openings in specific domains",
    backstory="You are an expert at finding job openings across various domains.",
    tools=[JobSearchTool("finance"), JobSearchTool("tech"), JobSearchTool("manufacturing")]
)

# Define the crew
crew = crewai.Crew(
    agents=[job_hunter],
    goal="Search for job openings in finance, tech, and manufacturing domains, and write the results to a JSON file."
)

# Run the crew
crew.run()

# Write the results to a JSON file
with open("job_openings.json", "w") as f:
    f.write(crew.result)