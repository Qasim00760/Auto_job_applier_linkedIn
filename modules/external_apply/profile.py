"""
Candidate profile manager for external job application filling.
Pulls verified data from Asif Hayat's configuration and CV.
"""

import os
from config import personals, questions


def get_candidate_profile() -> dict:
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    resume_path = os.path.join(root_dir, questions.default_resume_path.replace("/", os.sep))

    return {
        "first_name": personals.first_name,
        "last_name": personals.last_name,
        "full_name": f"{personals.first_name} {personals.last_name}".strip(),
        "email": "Asifh6221@gmail.com",
        "phone": personals.phone_number,
        "city": personals.current_city,
        "state": personals.state,
        "country": personals.country,
        "linkedin": questions.linkedIn,
        "headline": questions.linkedin_headline,
        "summary": questions.linkedin_summary.strip(),
        "cover_letter": getattr(questions, "cover_letter", "").strip(),
        "years_of_experience": questions.years_of_experience,
        "degree": "BSc Electrical Engineering",
        "university": "University of Engineering & Technology (UET), Peshawar",
        "has_masters": True,
        "notice_period_days": str(questions.notice_period),
        "expected_salary_yearly_sar": str(questions.desired_salary),
        "expected_salary_monthly_sar": "27500",
        "require_sponsorship": questions.require_visa,  # "No"
        "legally_authorized": questions.legally_authorized,  # "Yes"
        "current_employer": getattr(questions, "recent_employer", "Project Development Company (PDC)"),
        "resume_path": resume_path if os.path.exists(resume_path) else None,
    }
