import os
import json
from agents import RecruitmentAgents
from tasks import RecruitmentTasks
from crewai import Crew

# Create dummy resumes
def create_dummy_resumes(num_resumes):
    resumes = []
    for i in range(num_resumes):
        resume = {
            "name": f"Candidate {i+1}",
            "qualifications": ["Qualification 1", "Qualification 2"],
            "experience": ["Experience 1", "Experience 2"],
            "skills": ["Skill 1", "Skill 2"]
        }
        resumes.append(resume)
    return resumes

# Create dummy job openings
def create_dummy_job_openings(num_jobs):
    job_openings = {
        "finance": [],
        "tech": [],
        "manufacturing": []
    }
    for i in range(num_jobs):
        job = {
            "title": f"Job {i+1}",
            "company": f"Company {i+1}",
            "location": f"Location {i+1}"
        }
        domain = ["finance", "tech", "manufacturing"][i % 3]
        job_openings[domain].append(job)
    return job_openings

# Save resumes and job openings to files
def save_data(resumes, job_openings):
    with open("resumes.json", "w") as f:
        json.dump(resumes, f, indent=2)
    with open("job_openings.json", "w") as f:
        json.dump(job_openings, f, indent=2)

# Load data from files
def load_data():
    with open("resumes.json", "r") as f:
        resumes = json.load(f)
    with open("job_openings.json", "r") as f:
        job_openings = json.load(f)
    return resumes, job_openings

# Create dummy data
num_resumes = 10
num_jobs = 15
resumes = create_dummy_resumes(num_resumes)
job_openings = create_dummy_job_openings(num_jobs)
save_data(resumes, job_openings)

# Load data from files
resumes, job_openings = load_data()

# Create agents
recruitment_agents = RecruitmentAgents()
job_hunter = recruitment_agents.job_hunter_agent()
resume_analyst = recruitment_agents.resume_analyst_agent()
candidate_engagement = recruitment_agents.candidate_engagement_agent()
company_investigator = recruitment_agents.company_investigator_agent()
workflow_orchestrator = recruitment_agents.workflow_orchestrator_agent()

# Create tasks
recruitment_tasks = RecruitmentTasks()
job_search_task = recruitment_tasks.job_search(job_hunter)
resume_analysis_task = recruitment_tasks.resume_analysis(resume_analyst)
candidate_outreach_task = recruitment_tasks.candidate_outreach(candidate_engagement)
company_research_task = recruitment_tasks.company_research(company_investigator)
final_matching_task = recruitment_tasks.final_matching(workflow_orchestrator)

# Create crew
recruitment_crew = Crew(
    agents=[job_hunter, resume_analyst, candidate_engagement, company_investigator, workflow_orchestrator],
    tasks=[job_search_task, resume_analysis_task, candidate_outreach_task, company_research_task, final_matching_task],
    verbose=True
)

# Run the recruitment process
recruitment_crew.kickoff()

# Print the results
print("\n\n########################")
print("## Recruitment Results")
print("########################\n")
print(recruitment_crew.result)