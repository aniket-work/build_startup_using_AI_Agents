from serpapi import GoogleSearch
import  json

class JobScrapeQueryRun:
    def __init__(self, api_key):
        self.api_key = api_key

    def scrape_google_jobs_listing(self, job_ids):  # Add self as the first argument
        data = []

        for job_id in job_ids:
            params = {
                'api_key': self.api_key,  # Use self.api_key
                'engine': 'google_jobs_listing',
                'q': job_id,
            }

            search = GoogleSearch(params)
            results = search.get_dict()

            data.append({
                'job_id': job_id,
                'apply_options': results.get('apply_options'),
                'salaries': results.get('salaries'),
                'ratings': results.get('ratings')
            })

        return data

    def extract_multiple_jobs(self):  # Add self as the first argument
        params = {
            'api_key': self.api_key,
            'engine': 'google_jobs',
            'gl': 'us',
            'hl': 'en',
            'q': 'barista new york',
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        job_ids = [job.get('job_id') for job in results['jobs_results']]

        # Call self.scrape_google_jobs_listing with job_ids obtained from extract_multiple_jobs
        return json.dumps(self.scrape_google_jobs_listing(job_ids), indent=2, ensure_ascii=False)

