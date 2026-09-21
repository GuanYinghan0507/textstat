@echo off
cd /d "%~dp0"
py -3 run_tests.py
if errorlevel 1 (
  echo.
  echo Tests reported failures. Review the summary and results\junit.xml.
  pause
  exit /b 1
)
echo.
echo All tests passed.
pause
