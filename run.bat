@echo off
call C:\Users\Lavanya.Gorrela\PycharmProjects\SeleniumPythonProject\.venv\scripts\activate
rem pytest -v -s .\test_cases\test_admin_login.py
 pytest -v -s .\test_cases\test_categories.py
pause