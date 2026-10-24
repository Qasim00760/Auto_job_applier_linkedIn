'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (c) 2024-2026 Sai Vignesh Golla

License:    MIT License
            https://opensource.org/license/mit
            
GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

Support me: https://github.com/sponsors/GodsScion

version:    26.01.20.5.08
'''


###################################################### APPLICATION INPUTS ######################################################


# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Give an relative path of your default resume to be uploaded. If file in not found, will continue using your previously uploaded resume in LinkedIn.
default_resume_path = "all resumes/default/resume.pdf"      # (In Development)

# What do you want to answer for questions that ask about years of experience you have, this is different from current_experience? 
years_of_experience = "15"         # A number in quotes Eg: "0","1","2","3","4", etc.

# Do you need visa sponsorship now or in future?
require_visa = "No"               # "Yes" or "No"

# What is the link to your portfolio website, leave it empty as "", if you want to leave this question unanswered
website = ""                                                    # "www.example.bio" or "" and so on....

# Please provide the link to your LinkedIn profile.
linkedIn = "https://www.linkedin.com/in/asif-hayat-pmp%C2%AE-31b02489/"       # "https://www.linkedin.com/in/example" or "" and so on...

# Do you ALREADY have permission to work in the country you are applying to? (Eg: citizen, permanent resident, or a valid work visa such as H-1B or OPT)
# This is NOT `require_visa`, which asks whether you need sponsorship. Someone on a valid work visa answers "Yes" to both.
legally_authorized = "Yes"         # "Yes" or "No"

# What is the status of your citizenship? # If left empty as "", tool will not answer the question. However, note that some companies make it compulsory to be answered
# Valid options are: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", "Canadian Citizen/Permanent Resident" or "Other"
us_citizenship = "Other"



## SOME ANNOYING QUESTIONS BY COMPANIES 🫠 ##

# What to enter in your desired salary question (American and European), What is your expected CTC (South Asian and others)?, only enter in numbers as some companies only allow numbers,
desired_salary = 330000           # 80000, 90000, 100000 or 120000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your expected CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
And if asked in months, then it will divide by 12 and answer. Examples:
* 2400000 will be answered as "200000"
* 850000 will be answered as "70833"
'''

# What is your current CTC? Some companies make it compulsory to be answered in numbers...
current_ctc = 0                 # 800000, 900000, 1000000 or 1200000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your current CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
# And if asked in months, then it will divide by 12 and answer. Examples:
# * 2400000 will be answered as "200000"
# * 850000 will be answered as "70833"
'''

# (In Development) # Currency of salaries you mentioned. Companies that allow string inputs will add this tag to the end of numbers. Eg: 
# currency = "INR"                 # "USD", "INR", "EUR", etc.

# What is your notice period in days?
notice_period = 30                   # Any number >= 0 without quotes. Eg: 0, 7, 15, 30, 45, etc.
'''
Note: If question has 'month' or 'week' in it (Example: What is your notice period in months), 
then it will divide by 30 or 7 and answer respectively. Examples:
* For notice_period = 66:
  - "66" OR "2" if asked in months OR "9" if asked in weeks
* For notice_period = 15:"
  - "15" OR "0" if asked in months OR "2" if asked in weeks
* For notice_period = 0:
  - "0" OR "0" if asked in months OR "0" if asked in weeks
'''

# Your LinkedIn headline in quotes Eg: "Software Engineer @ Google, Masters in Computer Science", "Recent Grad Student @ MIT, Computer Science"
linkedin_headline = "Electrical Project Manager | Senior Electrical Engineer | PMP® | 15+ Years HV/MV/LV Power Distribution, Saudi Arabia" # "Headline" or "" to leave this question unanswered

# Your summary in quotes, use \n to add line breaks if using single quotes "Summary".You can skip \n if using triple quotes """Summary"""
linkedin_summary = """
PMP-certified Electrical Project Manager with 15+ years leading infrastructure, power distribution and construction projects in Saudi Arabia.
Delivered 114+ HV, MV and LV projects worth more than SAR 800 million for SEC and infrastructure clients.
Skilled in planning, execution, QA/QC, testing and commissioning of HV/MV/LV/ELV systems to SEC and IEC standards, with strong project controls (Primavera P6, EVM, Power BI).
"""

'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Your cover letter in quotes, use \n to add line breaks if using single quotes "Cover Letter".You can skip \n if using triple quotes """Cover Letter""" (This question makes sense though)
cover_letter = """
Dear Hiring Manager,

I am writing to apply for this role. I am a PMP-certified Electrical Project Manager with more than 15 years of experience in Saudi Arabia, delivering 114+ HV, MV and LV projects with a combined value of over SAR 800 million.

In my current role as Area Manager at Project Development Company (PDC) for Saudi Energy, I review and clear distribution works for acceptance and energization. Before this, I managed MV substation works up to 33 kV at Construction & Energy Pillars Company, and planned and supervised MV/LV networks at Saudi Energy Company. I am an SEC-approved Project Manager for MV/LV projects and an SEC-approved QC Engineer for 115/132 kV projects.

I bring strong project controls (Primavera P6, Earned Value Management, Power BI reporting), FIDIC contract administration and a firm commitment to safety and quality. I would welcome the opportunity to discuss how I can contribute to your projects.

Kind regards,
Asif Hayat
+966 56 235 5616 | Asifh6221@gmail.com
"""
# Information about you that the AI can use when answering application questions.
# Put anything an answer might need here, for example: name, years of experience,
# key skills, location, work authorization, and so on. Use \n for line breaks.
user_information_all = """
Name: Asif Hayat
Location: Riyadh, Saudi Arabia
Phone: +966562355616
Email: Asifh6221@gmail.com
Total experience: 15+ years, all in Saudi Arabia except 2011 in Pakistan
Current role: Area Manager, Project Development Company (PDC) - Saudi Energy, Riyadh (May 2026 - present)
Previous: Project Manager - Electrical, Construction & Energy Pillars Company (Jan 2024 - Apr 2026);
Senior Electrical Planning & Construction Engineer, Saudi Energy Company (Oct 2021 - Dec 2023);
Lead Electrical Engineer, Dar Al Riyadh Consultants (Jun 2016 - Sep 2021);
Electrical QC Engineer, Mohammed Al-Ojaimi Est. (Jan 2014 - May 2016);
Electrical Engineer, El-Seif Engineering Contracting (Feb 2012 - Nov 2013)
Education: BSc Electrical Engineering, UET Peshawar, Pakistan
Certifications: PMP (PMI); SEC Approved Project Manager MV/LV; SEC Approved QC Engineer 115/132 kV; SEC Permit Issuer/Receiver; NEBOSH IGC; Primavera P6; EVM; EOT Claims; FIDIC training; Power BI; ISO 9001; ISO 14001
Memberships: Saudi Council of Engineers; Pakistan Engineering Council; PMI
Key skills: HV/MV/LV/ELV systems, underground and OHL networks, MV substations up to 33 kV, 115 kV cables, RMUs, switchgear incl. GIS, transformers, testing and commissioning, QA/QC and ITPs, SEC and IEC compliance, HSE, Primavera P6, EVM, KPI reporting, Power BI, delay and claims analysis, risk management, FIDIC, BIM (Revit, Navisworks), AutoCAD
Languages: English (professional), Arabic (intermediate), Urdu (fluent), Pashto (native)
Visa sponsorship needed: No
Work mode: On-site or Hybrid, Full-time
Expected salary: 25,000 - 30,000 SAR per month
"""
'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Name of your most recent employer
recent_employer = "Project Development Company (PDC)" # "", "Lala Company", "Google", "Snowflake", "Databricks"

# Example question: "On a scale of 1-10 how much experience do you have building web or mobile applications? 1 being very little or only in school, 10 being that you have built and launched applications to real users"
confidence_level = "9"             # Any number between "1" to "10" including 1 and 10, put it in quotes ""
##



# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = True         # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''

# Should the tool pause if it needs help in answering questions during easy apply?
# Note: If set as False will answer randomly...
pause_at_failed_question = True    # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''
##

# Do you want to overwrite previous answers?
overwrite_previous_answers = False # True or False, Note: True or False are case-sensitive







############################################################################################################
'''
THANK YOU for using my tool 😊! Wishing you the best in your job hunt 🙌🏻!

Sharing is caring! If you found this tool helpful, please share it with your peers 🥺. Your support keeps this project alive.

Support my work on <PATREON_LINK>. Together, we can help more job seekers.

As an independent developer, I pour my heart and soul into creating tools like this, driven by the genuine desire to make a positive impact.

Your support, whether through donations big or small or simply spreading the word, means the world to me and helps keep this project alive and thriving.

Gratefully yours 🙏🏻,
Sai Vignesh Golla
'''

# --- Load user settings saved by the local control panel (user_config.json).
# --- No-op if that file is absent: values fall back to the defaults above.
from config import _overrides as _o
_o.apply(__name__, globals())
############################################################################################################