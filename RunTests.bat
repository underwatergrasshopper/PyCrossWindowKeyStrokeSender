@echo off

set PROJECT_PATH=%~dp0

set PYTHONPATH=%PYTHONPATH%;%PROJECT_PATH%src

py tests\scenario_send_to_window.py