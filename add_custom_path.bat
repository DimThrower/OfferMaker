@echo off
rem Grab folder path
for %%I in ("%~dp0") do set "ParentFolder=%%~fI"
echo ParentFolder=%ParentFolder%

rem Activate the venv
call "%ParentFolder%venv\Scripts\activate"

rem Navigate to the site-package directory
cd /d "%ParentFolder%venv\Lib\site-packages"

rem Create the .pth file
echo %ParentFolder% > mypath.pth
echo .pth file created in: %cd%

rem Deactivate venv
call "%ParentFolder%venv\Scripts\deactivate"

echo Python path updated successfully

pause
