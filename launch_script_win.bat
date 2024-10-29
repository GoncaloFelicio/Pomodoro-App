::@echo off
:: Comments start with :: or REM (optional)
echo Starting the Pomodoro launch script...
:: Change directory
cd C:\Users\Goncalo\Documents\Github\Pomodoro-App\
:: Activate the Virtual Env
call venv\Scripts\activate.bat
:: Launch the python file
python pomodoro.py