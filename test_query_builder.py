import sys
import os

# Add root to sys.path
sys.path.append(os.getcwd())

from modules.job_searcher.job_query_builder import JobQueryBuilder

def main():
    try:
        print("Initializing JobQueryBuilder...")
        builder = JobQueryBuilder()
        print("Generating queries...")
        queries = builder.generate_queries()
        print("Generated Queries:")
        for q in queries:
            print(f"- {q}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    queries = JobQueryBuilder().generate_queries()
    print(queries)

    # from modules.job_searcher.search_jobs import JobFinder
    # for query in queries:
    #     jobs = JobFinder().search_jobs(query)
    #     print(jobs)
    #     print("\n")
    #     print('-------------------------')

    # jobs = [{'title': 'Junior Software Engineer (RPA)', 'company': None, 'url': 'https://www.synapseindia.rocks/opening-details/Junior-Software-Engineer-RPA-769/', 'date': '2026-01-23'}, {'title': 'Junior Software Engineer', 'company': None, 'url': 'https://in.linkedin.com/jobs/view/junior-software-engineer-at-aetosky-4363421824', 'date': '2026-01-23'}, {'title': 'Junior Software Engineer', 'company': None, 'url': 'http://in.indeed.com/job/junior-software-engineer-d670c04c0a689219', 'date': '2026-01-23'}, {'title': 'Junior Software Engineer', 'company': None, 'url': 'https://www.naukri.com/job-listings-junior-software-engineer-aikon-nautics-llp-margao-0-to-5-years-230126029179', 'date': '2026-01-23'}, {'title': 'Junior Software Engineer', 'company': None, 'url': 'https://in.linkedin.com/jobs/view/junior-software-engineer-at-mpc-cloud-consulting-pvt-ltd-4361915883', 'date': '2026-01-21'}, {'title': 'Junior Software Engineer SharePoint', 'company': None, 'url': 'https://www.naukri.com/job-listings-junior-software-engineer-sharepoint-synapse-design-noida-1-to-5-years-200126507032', 'date': '2026-01-20'}, {'title': 'Junior Software Engineer NET', 'company': None, 'url': 'https://www.naukri.com/job-listings-junior-software-engineer-net-synapse-design-noida-1-to-4-years-200126507053', 'date': '2026-01-20'}, {'title': 'Junior Software Engineer Backend', 'company': None, 'url': 'https://www.naukri.com/job-listings-junior-software-engineer-backend-axelerant-technologies-pvt-ltd-remote-2-to-7-years-200126507457', 'date': '2026-01-20'}, {'title': 'Junior Software Engineer', 'company': None, 'url': 'http://in.indeed.com/job/junior-software-engineer-2732061f30b65344', 'date': '2026-01-20'}, {'title': 'Junior Software Engineer', 'company': None, 'url': 'https://in.linkedin.com/jobs/view/junior-software-engineer-at-rintel-4353754679', 'date': '2026-01-19'}, {'title': 'Junior Software Test Engineer', 'company': None, 'url': 'http://in.indeed.com/job/junior-software-test-engineer-2c382a3ad61eccf1', 'date': '2026-01-19'}, {'title': 'Junior Software Engineer -Dotnet', 'company': None, 'url': 'http://in.indeed.com/job/junior-software-engineer-dotnet-3513d313d14a4c83', 'date': '2026-01-17'}, {'title': 'Junior software engineer', 'company': None, 'url': 'http://in.indeed.com/job/junior-software-engineer-dc7b18bdae1b4022', 'date': '2026-01-17'}, {'title': 'Junior Software Engineer', 'company': None, 'url': 'https://in.linkedin.com/jobs/view/junior-software-engineer-at-techactivator-4328008209', 'date': '2026-01-16'}, {'title': 'Junior Software Engineer', 'company': None, 'url': 'https://in.linkedin.com/jobs/view/junior-software-engineer-at-logai-enterprise-intelligence-platform-4352524524', 'date': '2026-01-16'}, {'title': 'Junior Software Engineer - Campus', 'company': None, 'url': 'https://job-boards.greenhouse.io/ibkr/jobs/8370235002?Source=Linkedin', 'date': '2026-01-16'}, {'title': 'Junior Software Engineer-Java/Kotlin', 'company': None, 'url': 'https://ikea.avature.net/External/JobDetail?id=287237%3Fsource%3DLinkedIn', 'date': '2026-01-16'}, {'title': 'Junior Software Engineer', 'company': None, 'url': 'http://in.indeed.com/job/junior-software-engineer-39f885c245410376', 'date': '2026-01-16'}, {'title': 'Junior Software Test Engineer', 'company': None, 'url': 'https://candidate.siaa.app/job-listings/677d30347a4fc09e77e09b92', 'date': '2026-01-15'}, {'title': 'Junior Software Engineer', 'company': None, 'url': 'https://in.linkedin.com/jobs/view/junior-software-engineer-at-harjai-talent-4362368346', 'date': '2026-01-15'}, {'title': 'Junior Software Engineer (.NET)', 'company': None, 'url': 'https://www.naukri.com/job-listings-junior-software-engineer-net-imriel-technology-solutions-pvt-ltd-vadodara-0-to-1-years-150126504288', 'date': '2026-01-15'}, {'title': 'Junior Software Engineer – Backend', 'company': None, 'url': 'https://axelerant.pinpointhq.com/postings/eb761c56-124e-46be-9f41-399bb816e599/applications/new?utm_medium=job_board&utm_source=linkedIn', 'date': '2026-01-15'}, {'title': 'Junior Software Engineer', 'company': None, 'url': 'https://www.naukri.com/job-listings-junior-software-engineer-aytech-ernakulam-trivandrum-0-to-1-years-150126927656', 'date': '2026-01-15'}, {'title': 'Junior Software Engineer', 'company': None, 'url': 'https://www.positivty.com/talent/apply?id=37', 'date': '2026-01-15'}, {'title': 'Junior Software Engineer (SharePoint)', 'company': None, 'url': 'https://www.synapseindia.rocks/opening-details/Junior-Software-Engineer-SharePoint-736/', 'date': '2026-01-14'}]