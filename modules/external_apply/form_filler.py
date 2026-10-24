"""
Intelligent ATS Form Filler for External Job Portals.
Supports Workday, Greenhouse, Lever, SmartRecruiters, Taleo, and generic career portals.
"""

import os
import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modules.external_apply.safety import check_for_financial_scam, detect_captcha, request_human_help
import pyautogui


def fill_field(element, text: str) -> bool:
    try:
        element.click()
        time.sleep(0.2)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        for char in str(text):
            element.send_keys(char)
            time.sleep(0.02)
        return True
    except Exception:
        return False


def apply_to_external_form(driver, profile: dict, auto_submit: bool = False) -> tuple[bool, str]:
    """
    Fills out an external job application form using the candidate's profile.
    Returns (success: bool, message: str).
    """
    # 1. Safety check: Page content
    try:
        page_source = driver.page_source
        is_scam, scam_reason = check_for_financial_scam(page_source)
        if is_scam:
            return False, scam_reason
    except Exception:
        pass

    # 2. Check for CAPTCHA upfront
    if detect_captcha(driver):
        resumed = request_human_help(driver, "CAPTCHA detected on page load")
        if not resumed:
            return False, "Skipped by user at CAPTCHA stage"

    # 3. Handle File Upload (Resume / CV)
    if profile.get("resume_path") and os.path.exists(profile["resume_path"]):
        try:
            file_inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='file']")
            for f_in in file_inputs:
                try:
                    f_in.send_keys(profile["resume_path"])
                    time.sleep(1.5)
                    break
                except Exception:
                    continue
        except Exception:
            pass

    # 4. Fill text inputs
    try:
        inputs = driver.find_elements(By.CSS_SELECTOR, "input:not([type='hidden']):not([type='file'])")
        for inp in inputs:
            if not inp.is_displayed() or not inp.is_enabled():
                continue

            # Identify input by id, name, aria-label, placeholder, or parent text
            ident = " ".join([
                inp.get_attribute("name") or "",
                inp.get_attribute("id") or "",
                inp.get_attribute("aria-label") or "",
                inp.get_attribute("placeholder") or "",
                inp.get_attribute("autocomplete") or "",
            ]).lower()

            # First name
            if any(k in ident for k in ["first_name", "firstname", "first name", "given name"]):
                fill_field(inp, profile["first_name"])
            # Last name
            elif any(k in ident for k in ["last_name", "lastname", "last name", "family name", "surname"]):
                fill_field(inp, profile["last_name"])
            # Full name
            elif any(k in ident for k in ["full_name", "fullname", "full name", "applicant_name", "your name"]):
                fill_field(inp, profile["full_name"])
            # Email
            elif any(k in ident for k in ["email", "e-mail"]):
                fill_field(inp, profile["email"])
            # Phone
            elif any(k in ident for k in ["phone", "mobile", "cell", "contact number"]):
                fill_field(inp, profile["phone"])
            # City / Location
            elif any(k in ident for k in ["city", "location", "address"]):
                fill_field(inp, profile["city"])
            # LinkedIn
            elif "linkedin" in ident:
                fill_field(inp, profile["linkedin"])
            # Years of experience
            elif any(k in ident for k in ["years of experience", "total experience"]):
                fill_field(inp, profile["years_of_experience"])
            # Notice period
            elif "notice" in ident and "period" in ident:
                fill_field(inp, profile["notice_period_days"])
            # Expected salary
            elif any(k in ident for k in ["expected salary", "desired salary", "compensation", "salary"]):
                fill_field(inp, profile["expected_salary_monthly_sar"])
            # Current employer
            elif any(k in ident for k in ["current employer", "current company", "employer"]):
                fill_field(inp, profile["current_employer"])
    except Exception:
        pass

    # 5. Fill Textarea (Cover letter / Summary)
    try:
        textareas = driver.find_elements(By.TAG_NAME, "textarea")
        for ta in textareas:
            if not ta.is_displayed():
                continue
            ta_ident = " ".join([
                ta.get_attribute("name") or "",
                ta.get_attribute("id") or "",
                ta.get_attribute("aria-label") or "",
                ta.get_attribute("placeholder") or "",
            ]).lower()

            if any(k in ta_ident for k in ["cover letter", "letter"]):
                fill_field(ta, profile["cover_letter"])
            elif any(k in ta_ident for k in ["summary", "about you", "objective"]):
                fill_field(ta, profile["summary"])
    except Exception:
        pass

    # 6. Check for agreement / terms checkboxes
    try:
        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        for cb in checkboxes:
            cb_id = (cb.get_attribute("name") or cb.get_attribute("id") or "").lower()
            if any(k in cb_id for k in ["agree", "consent", "terms", "policy", "privacy"]):
                if not cb.is_selected():
                    try:
                        driver.execute_script("arguments[0].click();", cb)
                    except Exception:
                        pass
    except Exception:
        pass

    # 7. Final Step: Review / Human-in-the-loop confirmation
    if detect_captcha(driver):
        resumed = request_human_help(driver, "CAPTCHA detected on the form")
        if not resumed:
            return False, "Skipped at CAPTCHA stage"

    if not auto_submit:
        # Prompt human (Bhai ka kaam) to review the pre-filled form and confirm submission
        msg = (
            "✅ Form is pre-filled!\n\n"
            "Please review the application in the open browser window:\n"
            "- Check all fields and uploaded CV.\n"
            "- If everything looks good, click 'Submit' yourself on the website, then click 'Confirm Applied' below.\n"
            "- Or click 'Skip' if you don't want to apply to this job."
        )
        choice = pyautogui.confirm(text=msg, title="External Apply - Review Step", buttons=["Confirm Applied", "Skip", "Abort"])
        if choice == "Confirm Applied":
            return True, "Applied successfully (verified by user)"
        elif choice == "Skip":
            return False, "Job skipped by user"
        else:
            return False, "Aborted by user"
    else:
        # Attempt to click submit button
        submit_candidates = driver.find_elements(By.XPATH, "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'submit') or contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'apply')]")
        for btn in submit_candidates:
            if btn.is_displayed() and btn.is_enabled():
                try:
                    btn.click()
                    time.sleep(3)
                    return True, "Auto-submitted successfully"
                except Exception:
                    continue
        return False, "Could not locate visible Submit button"
