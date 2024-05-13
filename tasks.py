from crewai import Task
from textwrap import dedent

class RecruitmentTasks:
    def job_search(self, agent):
        return Task(
            name="Job Search Task",
            description=dedent("""
                Search for job openings in finance domains across various job websites and platforms.
                Compile a comprehensive list of relevant job opportunities, including job titles, website link of job posting, company names, job description and locations.
                Make use of the Google Jobs Search tool to search for job openings on the web.
                Your output should be a JSON file containing the scraped job opening data, organized by domain with more detailed information such as required skills, qualifications, and salary range (if available).
            """),
            agent=agent,
            input={
                "query": "finance jobs",
                "location": "New York"
            },
            expected_output="A JSON file containing detailed job opening data scraped from various job sites, organized by domain.",
            output_file="job_openings.json"
        )

    def resume_analysis(self, agent):
        return Task(
            description=dedent("""
                Analyze the resumes of candidates and filter out the most qualified individuals based on predefined criteria.
                Your analysis should take into account the candidates' qualifications, experiences, and skills in relation to the identified job openings.
                Your output should be a shortlist of top candidates suitable for the job openings.
            """),
            agent=agent,
            expected_output="A shortlist of top candidates suitable for the identified job openings."
        )

    def candidate_outreach(self, agent):
        return Task(
            description=dedent("""
                Craft compelling outreach messages to engage with the shortlisted candidates.
                Your outreach should be personalized, conveying the essence of the job opportunity and the corporate culture in an engaging manner.
                Your output should be the initial contact with potential hires, setting the stage for further recruitment steps.
            """),
            agent=agent,
            expected_output="Initial contact with potential hires, setting the stage for further recruitment steps."
        )

    def company_research(self, agent):
        return Task(
            description=dedent("""
                Investigate the organizational culture and values of companies with job openings.
                Gain a comprehensive understanding of their work environment, employee reviews, and industry reputation.
                Your output should be in-depth company profiles that assist in matching candidates with the right organizational fit.
            """),
            agent=agent,
            expected_output="In-depth company profiles that assist in matching candidates with the right organizational fit."
        )

    def final_matching(self, agent):
        return Task(
            description=dedent("""
                Synthesize the information from the resume analysis and company research tasks.
                Match the shortlisted candidates with suitable job openings and companies based on qualifications and cultural fit.
                Your output should be successful placements that align with both professional aspirations and organizational values.
            """),
            agent=agent,
            expected_output="Successful placement of candidates in roles that align with their professional aspirations and the company's culture."
        )