@echo off

if exist "./dist" rd /s /q "./dist"
if exist "./build" rd /s /q "./build"
if exist "./src/PyCrossWindowKeyStrokeSender.egg-info" rd /s /q "./src/PyCrossWindowKeyStrokeSender.egg-info"
if exist "./TestResults" rd /s /q "./TestResults"

echo done