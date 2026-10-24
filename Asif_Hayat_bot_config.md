# LinkedIn Auto Job Applier — Config for Asif Hayat

Source: Asif's CV (Asif_Hayat_Electrical_Project_Manager_CV.pdf) + his filled setup form.
Lines marked `# TODO` must be confirmed with Asif before the first real run.

---

## 1. config/personals.py

```python
first_name = "Asif"
middle_name = ""
last_name = "Hayat"
phone_number = "+966562355616"
current_city = "Riyadh"
street = ""                      # left empty (not provided)
state = "Riyadh Province"
zipcode = ""
country = "Saudi Arabia"
# Equal-opportunity questions: leave as "Decline" unless Asif wants to answer
ethnicity = "Decline"
gender = "Decline"
disability_status = "Decline"
veteran_status = "Decline"
```

---

## 2. config/questions.py

```python
default_resume_path = "all resumes/default/resume.pdf"   # put Asif's CV here

years_of_experience = "15"
require_visa = "No"                                      # from form
website = ""                                             # no portfolio
linkedIn = "https://www.linkedin.com/in/asif-hayat-pmp%C2%AE-31b02489/"
us_citizenship = "Other"                                 # US-only question; not applicable

desired_salary = 330000          # TODO confirm. Yearly SAR (27,500/month x 12). Form says 25,000-30,000 SAR/month.
                                 #      Tool divides by 12 when a form asks for monthly salary.
current_ctc = 0                  # TODO current yearly salary in SAR (left blank on form)
notice_period = 30               # TODO confirm notice period in days (left blank on form)

linkedin_headline = "Electrical Project Manager | Senior Electrical Engineer | PMP® | 15+ Years HV/MV/LV Power Distribution, Saudi Arabia"

linkedin_summary = """
PMP-certified Electrical Project Manager with 15+ years leading infrastructure, power distribution and construction projects in Saudi Arabia.
Delivered 114+ HV, MV and LV projects worth more than SAR 800 million for SEC and infrastructure clients.
Skilled in planning, execution, QA/QC, testing and commissioning of HV/MV/LV/ELV systems to SEC and IEC standards, with strong project controls (Primavera P6, EVM, Power BI).
"""

cover_letter = """
Dear Hiring Manager,

I am writing to apply for this role. I am a PMP-certified Electrical Project Manager with more than 15 years of experience in Saudi Arabia, delivering 114+ HV, MV and LV projects with a combined value of over SAR 800 million.

In my current role as Area Manager at Project Development Company (PDC) for Saudi Energy, I review and clear distribution works for acceptance and energization. Before this, I managed MV substation works up to 33 kV at Construction & Energy Pillars Company, and planned and supervised MV/LV networks at Saudi Energy Company. I am an SEC-approved Project Manager for MV/LV projects and an SEC-approved QC Engineer for 115/132 kV projects.

I bring strong project controls (Primavera P6, Earned Value Management, Power BI reporting), FIDIC contract administration and a firm commitment to safety and quality. I would welcome the opportunity to discuss how I can contribute to your projects.

Kind regards,
Asif Hayat
+966 56 235 5616 | Asifh6221@gmail.com
"""

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

recent_employer = "Project Development Company (PDC)"
confidence_level = "9"

# Safety
pause_before_submit = True         # keep True for the first week
pause_at_failed_question = True    # ALWAYS True (False = random answers)
overwrite_previous_answers = False
```

---

## 3. config/search.py

```python
search_terms = ["Electrical Project Manager", "Electrical Manager", "Senior Electrical Engineer", "Lead Electrical Engineer", "Electrical Department Manager"]
search_location = "Saudi Arabia"
switch_number = 3                  # 5 titles x 3 = max 15 applications per run
randomize_search_order = True

sort_by = "Most recent"
date_posted = "Past week"
easy_apply_only = True
experience_level = ["Mid-Senior level", "Director"]
job_type = ["Full-time"]
on_site = ["On-site", "Hybrid"]

about_company_bad_words = []
about_company_good_words = []
bad_words = ["US Citizen", "USA Citizen", "Security Clearance"]   # removed the author's software-developer words

skip_non_sponsoring_jobs = False
skip_jobs_without_sponsorship = False
security_clearance = False
did_masters = False                # TODO form says "Yes", CV shows only BSc. Confirm.
current_experience = 15

pause_after_filters = True
```

---

## 4. config/settings.py

```python
click_gap = 5
run_non_stop = False
run_in_background = False
smooth_scroll = True
follow_companies = False
safe_mode = True
keep_screen_awake = True
auto_manage_driver = True
close_tabs = True
```

## 5. config/secrets.py

Leave username and password EMPTY. Asif logs in himself in the browser on first run.
