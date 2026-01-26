import os
from dotenv import load_dotenv
import requests

load_dotenv()

class JobFinder:

    def __init__(self):
        self.token = os.getenv("TOKEN")
        self.url = os.getenv("BASE_URL")
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }

    def search_jobs(self, keyword):
        """
        Returns the top 5 jobs for the given keyword
        """
        body = {
            "page": 0,
            "job_title_or": [keyword],
            "job_country_code_or": ["IN"],
            "posted_at_max_age_days": 14,
            "order_by": [{"field": "date_posted", "desc": True}]  # Get the newest ones first
        }

        try:
            # We use json = body instead of data=body to let requests handle the encoding
            response = requests.post(self.url, json=body, headers=self.headers)
            response.raise_for_status()  # Check for errors

            data = response.json()

            # TheirStack usually returns a list of jobs under a 'data' or similar key
            # Based on their docs, it returns a list directly or inside a 'jobs' object
            jobs = data.get('data', [])

            results = []
            for job in jobs:
                results.append({
                    "title": job.get("job_title"),
                    "company": job.get("company_name"),
                    "url": job.get("url"),
                    "date": job.get("date_posted")
                })

            return results

        except requests.exceptions.RequestException as e:
            print(f"Error fetching jobs for {keyword}: {e}")
            return []
