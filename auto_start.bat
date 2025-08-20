@echo off
REM This script automates the startup of your remote control system.

REM Set the working directory to your project folder.
cd /d D:\AutoControl

REM Start Ngrok in the background.
REM Use /B to run the command without creating a new window.
start /B ngrok.exe http 8000

REM Wait 25 seconds for Ngrok to establish its tunnel. (Crucial for stability)
ping localhost -n 05 >nul

REM Run the update script. The batch file will WAIT for this script to finish.
python update_ifttt.py

REM Wait 30 seconds for IFTTT to process the webhook and update the Google Sheet.
ping localhost -n 05 >nul

REM Start the Flask app for executing commands in the background.
start /B python remote_control.py

REM Start the polling script that checks the Google Sheet for commands.
start /B python relay_server.py