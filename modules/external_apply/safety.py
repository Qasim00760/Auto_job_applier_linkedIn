"""
Security, Safety Guardrails, and Human-in-the-Loop Interventions for External Job Applications.
"""

import re
import time
import winsound
from urllib.parse import urlparse
import pyautogui


DANGEROUS_KEYWORDS = [
    "credit card", "debit card", "card number", "cvv", "expiration date",
    "bank account", "routing number", "iban", "wire transfer",
    "pay application fee", "processing fee", "registration fee",
    "bitcoin", "crypto", "usdt", "wallet address"
]

SCAM_SUSPICIOUS_TLDS = [".xyz", ".top", ".buzz", ".work", ".click", ".link"]


def is_safe_url(url: str) -> tuple[bool, str]:
    """Validate that the application URL is safe and legitimate."""
    if not url or not isinstance(url, str):
        return False, "Invalid URL"

    parsed = urlparse(url)
    if parsed.scheme.lower() != "https":
        return False, "Non-HTTPS connection rejected for security"

    domain = parsed.netloc.lower()
    for tld in SCAM_SUSPICIOUS_TLDS:
        if domain.endswith(tld):
            return False, f"Suspicious domain extension ({tld}) rejected for safety"

    return True, "Safe URL"


def check_for_financial_scam(page_text: str) -> tuple[bool, str]:
    """Ensure the external portal is not asking for money or bank/card details."""
    text_lower = page_text.lower()
    for kw in DANGEROUS_KEYWORDS:
        if kw in text_lower:
            return True, f"ALERT: Financial or payment keyword detected ('{kw}'). Aborting to protect user!"
    return False, "Clean"


def detect_captcha(driver) -> bool:
    """Detect presence of common CAPTCHA / bot challenges on the active page."""
    captcha_indicators = [
        "//iframe[contains(@src, 'recaptcha')]",
        "//iframe[contains(@src, 'hcaptcha')]",
        "//iframe[contains(@src, 'cloudflare') or contains(@src, 'turnstile')]",
        "//div[contains(@class, 'g-recaptcha')]",
        "//div[contains(@class, 'h-captcha')]",
        "//div[contains(@id, 'cf-turnstile')]",
        "//div[contains(@class, 'arkose')]",
        "//iframe[contains(@title, 'reCAPTCHA')]",
    ]
    for xpath in captcha_indicators:
        try:
            elements = driver.find_elements("xpath", xpath)
            for el in elements:
                if el.is_displayed():
                    return True
        except Exception:
            continue
    return False


def request_human_help(driver, reason: str = "CAPTCHA or verification detected") -> bool:
    """
    Trigger sound alarm and alert for human intervention (Bhai ka kaam).
    Pauses until human solves challenge and clicks 'Resume'.
    """
    try:
        # Audible beep alarm
        for _ in range(3):
            winsound.Beep(1200, 300)
            time.sleep(0.1)
    except Exception:
        pass

    message = (
        f"🚨 HUMAN INTERVENTION REQUIRED! 🚨\n\n"
        f"Reason: {reason}\n\n"
        f"1. Please look at the open browser window.\n"
        f"2. Solve the CAPTCHA or verification step manually.\n"
        f"3. Click 'Resume' below when you are ready to continue."
    )
    result = pyautogui.confirm(
        text=message,
        title="External Apply - Action Required",
        buttons=["Resume", "Skip This Job", "Stop Application"]
    )
    return result == "Resume"
