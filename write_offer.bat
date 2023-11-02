rem "/d" gets the current letter of the drive the batch file is located in
rem "%~d0" holds the actual drive letter
cd /d %~d0

set "write_offer=main\Scripts\gui.py"

start cmd /k "C:\Users\charl\Desktop\Offer_Maker\venv\Scripts\activate.bat && python %write_offer%"
