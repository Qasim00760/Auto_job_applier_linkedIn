"""
Runner for External Apply Module.
Processes queued external job links sequentially with safety checks and human-in-the-loop support.
"""

import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from modules.external_apply.queue_manager import get_pending_jobs, update_job_status, get_queue_stats
from modules.external_apply.profile import get_candidate_profile
from modules.external_apply.safety import is_safe_url
from modules.external_apply.form_filler import apply_to_external_form
import pyautogui


def run_external_apply(auto_submit: bool = False, max_jobs: int = 10) -> None:
    print("\n========================================================")
    print("      EXTERNAL JOB APPLIER (AI / ATS Agent)             ")
    print("========================================================\n")

    stats = get_queue_stats()
    print(f"Queue Status: Total={stats['total']}, Pending={stats['pending']}, Applied={stats['applied']}, Failed={stats['failed']}")

    pending_jobs = get_pending_jobs()
    if not pending_jobs:
        print("\nNo pending external jobs in the queue.")
        manual_url = pyautogui.prompt(
            "The external jobs queue is empty!\n\nEnter an external job URL manually to test/apply, or click Cancel:",
            "External Job Apply"
        )
        if not manual_url:
            print("Exiting.")
            return
        pending_jobs = [{
            "job_id": "manual_" + str(int(time.time())),
            "title": "Manual Job",
            "company": "Direct External",
            "job_link": manual_url,
            "external_link": manual_url,
        }]

    profile = get_candidate_profile()
    print(f"\nCandidate: {profile['full_name']} ({profile['email']})")
    print(f"Resume: {profile['resume_path'] or 'MISSING (Please add all resumes/default/resume.pdf)'}")

    # Launch Chrome browser
    print("\nLaunching browser...")
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)

    processed = 0
    applied_count = 0
    failed_count = 0

    try:
        for job in pending_jobs:
            if processed >= max_jobs:
                print(f"Reached maximum jobs limit for this run ({max_jobs}).")
                break

            job_id = job.get("job_id")
            title = job.get("title", "Unknown")
            company = job.get("company", "Unknown")
            ext_url = job.get("external_link", "")

            print(f"\n[{processed + 1}/{len(pending_jobs)}] Processing: {title} at {company}")
            print(f"URL: {ext_url}")

            # 1. URL Safety Check
            safe, reason = is_safe_url(ext_url)
            if not safe:
                print(f"  ❌ Security check failed: {reason}")
                update_job_status(job_id, "failed", f"Security: {reason}")
                failed_count += 1
                continue

            # 2. Navigate
            try:
                driver.get(ext_url)
                time.sleep(3)
            except Exception as e:
                print(f"  ❌ Failed to open URL: {e}")
                update_job_status(job_id, "failed", str(e))
                failed_count += 1
                continue

            # 3. Fill and submit
            success, msg = apply_to_external_form(driver, profile, auto_submit=auto_submit)
            if success:
                print(f"  ✅ {msg}")
                update_job_status(job_id, "applied")
                applied_count += 1
            else:
                print(f"  ⚠️ {msg}")
                update_job_status(job_id, "failed", msg)
                failed_count += 1

            processed += 1
            time.sleep(2)

    finally:
        print("\n========================================================")
        print(f"External Apply Summary: Processed={processed}, Applied={applied_count}, Failed/Skipped={failed_count}")
        print("========================================================\n")
        try:
            driver.quit()
        except Exception:
            pass


if __name__ == "__main__":
    run_external_apply(auto_submit=False)
