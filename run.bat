@echo off
call C:\Users\Lavanya.Gorrela\PycharmProjects\SeleniumPythonProject\.venv\scripts\activate
pytest -v -s .\test_cases\test_admin_login.py --html=report_admin_login.html
pytest -v -s .\test_cases\test_categories.py --html=report_categories.html
pause
