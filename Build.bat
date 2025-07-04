:: Build64.bat [<python_version>]
:: <python_version>
::     Version of python used to build the package.
::
::     <major>[.<minor>[-<architecture>]]

@echo off
setlocal EnableDelayedExpansion

set PROJECT_PATH=%~dp0

set PYTHON_VERSION=%1

if "!PYTHON_VERSION!" neq "" (
    set PYTHON_VERSION=-!PYTHON_VERSION!
)

set PYTHON_TAG=py311

py !PYTHON_VERSION! -m build --wheel -C--build-option=--python-tag=!PYTHON_TAG! -C--build-option=--plat-name=win-amd64 %PROJECT_PATH%
if %errorlevel% neq 0 (
    exit /b 1
)
py !PYTHON_VERSION! -m build --wheel -C--build-option=--python-tag=!PYTHON_TAG! -C--build-option=--plat-name=win32 %PROJECT_PATH%
