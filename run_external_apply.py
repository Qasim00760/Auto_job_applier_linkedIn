"""
Standalone launcher for External Job Application Automation
"""

import sys
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from modules.external_apply.runner import run_external_apply

if __name__ == "__main__":
    # Set auto_submit=False for human-in-the-loop review before final submission (recommended for security)
    # Set auto_submit=True for full automatic submission
    run_external_apply(auto_submit=False, max_jobs=15)
