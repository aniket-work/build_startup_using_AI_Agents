from serpapi import GoogleSearch
import json

from serpapi import GoogleSearch
import json

class JobScraper:
    def __init__(self, api_key):
        self.api_key = api_key

    def run(self, search_query, num_results=20):
        params = {
            "api_key": self.api_key,
            "engine": "google_jobs",
            "query": search_query,
            "num_jobs": num_results,
            "start": 0
        }

        client = GoogleSearch(params)
        results = client.get_dict()

        job_listings = []
        for job in results.get("jobs_results", []):
            job_listing = {
                "title": job.get("title", ""),
                "company_name": job.get("company_name", ""),
                "location": job.get("location", ""),
                "job_description": job.get("description", ""),
                "job_link": job.get("job_link", ""),
                "salary_range": job.get("salary_estimate", ""),
                "qualifications": job.get("qualifications", "")
            }
            job_listings.append(job_listing)

        return job_listings

from serpapi import GoogleSearch

class JobScrapeQueryRun:
    def __init__(self, api_key):
        self.api_key = api_key

    def run(self, query_dict):
        search_query = query_dict.get("query")
        location = query_dict.get("location", "United States")
        num_results = query_dict.get("num_results", 20)

        params = {
            "api_key": self.api_key,
            "engine": "google_jobs",
            "query": search_query,
            "location": location,
            "num_jobs": num_results,
            "start": 0
        }

        client = GoogleSearch(params)
        results = client.get_dict()

        job_listings = []
        for job in results.get("jobs_results", []):
            job_listing = {
                "title": job.get("title", ""),
                "company_name": job.get("company_name", ""),
                "location": job.get("location", ""),
                "job_description": job.get("description", ""),
                "job_link": job.get("job_link", ""),
                "salary_range": job.get("salary_estimate", ""),
                "qualifications": job.get("qualifications", "")
            }
            job_listings.append(job_listing)

        return job_listings

    def validate_input(self, action_input):
        if not isinstance(action_input, dict):
            return False

        if "query" not in action_input:
            return False

        return True

    def format_error(self, action_input):
        return f"Invalid input format. Expected a dictionary with key 'query'. Received: {action_input}"