:: Build64.bat [<python_version>]
:: <python_version>
::     3                (default)
::     3.9
@echo off
setlocal EnableDelayedExpansion

set PYTHON_VERSION=%1

if "!PYTHON_VERSION!" neq "" (
    set PY_PYTHON_VERSION=-!PYTHON_VERSION!-64
) else (
    set PY_PYTHON_VERSION=-3-64
)

py !PY_PYTHON_VERSION! setup.py bdist_wheel --plat-name=win-amd64
