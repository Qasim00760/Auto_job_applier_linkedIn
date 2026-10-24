@echo off
REM Launcher for External Job Applier
setlocal
cd /d "%~dp0"

echo ========================================================
echo   External Job Applier (AI / ATS Automation)
echo ========================================================
echo.

set "VENV_PY=.venv\Scripts\python.exe"
if exist "%VENV_PY%" (
    "%VENV_PY%" run_external_apply.py
) else (
    python run_external_apply.py
)

pause
