from fastapi import APIRouter
from modules.job_searcher.job_query_builder import JobQueryBuilder
from modules.job_searcher.search_jobs import JobFinder

router = APIRouter()

@router.post("/query")
def query():
    """
    Use the predefined functions to generate job queries, search them and return the found jobs.
    """
    query_builder = JobQueryBuilder()
    queries = query_builder.generate_queries()
    
    job_finder = JobFinder()
    jobs = [] # List of dicts of jobs
    for query in queries:
        jobs.extend(job_finder.search_jobs(query))
    return jobs
