@echo off

set PROJECT_PATH=%~dp0

if exist "%PROJECT_PATH%dist" rd /s /q "%PROJECT_PATH%dist"
if exist "%PROJECT_PATH%build" rd /s /q "%PROJECT_PATH%build"
if exist "%PROJECT_PATH%out" rd /s /q "%PROJECT_PATH%out"
if exist "%PROJECT_PATH%src\PyCrossWindowKeyStrokeSender.egg-info" rd /s /q "%PROJECT_PATH%src\PyCrossWindowKeyStrokeSender.egg-info"
if exist "%PROJECT_PATH%TestResults" rd /s /q "%PROJECT_PATH%TestResults"

echo done