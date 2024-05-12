import json
import os

import requests
from langchain.tools import tool
from langchain_community.tools.google_jobs import GoogleJobsQueryRun
from langchain_community.utilities.google_jobs import GoogleJobsAPIWrapper

class JobSearchTool():
    name = "JobSearchTool"
    description = "Search the internet for job openings in specified domains using the SerpAPI."

    def __init__(self, serpapi_api_key):
        self.serpapi_api_key = serpapi_api_key

    @tool("Search internet")
    def search_internet(self):
        """Useful to search the internet about a given topic and return relevant
        results."""
        return JobSearchTool.search()

    def search(self):
        return  GoogleJobsQueryRun(api_wrapper=GoogleJobsAPIWrapper())
