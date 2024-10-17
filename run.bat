@echo off
call C:\Users\Lavanya.Gorrela\PycharmProjects\SeleniumPythonProject\.venv\scripts\activate
C:\Users\Lavanya.Gorrela\PycharmProjects\SeleniumPythonProject\.venv\Scripts\python -m pytest -v -s .\test_cases\test_admin_login.py
C:\Users\Lavanya.Gorrela\PycharmProjects\SeleniumPythonProject\.venv\Scripts\python -m pytest -v -s .\test_cases\test_categories.py
pause
