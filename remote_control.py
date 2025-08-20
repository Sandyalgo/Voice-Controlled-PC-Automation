from flask import Flask
import os

app = Flask(__name__)

@app.route('/shutdown')
def shutdown():
    os.system("shutdown /s /t 1")
    return "Shutdown command sent."

@app.route('/lock') 
def lock():
    os.system("rundll32.exe user32.dll,LockWorkStation")
    return "Lock command sent."

@app.route('/open_browser')
def open_browser():
    os.system("start chrome")
    return "Chrome browser opened."

# --- ADD THIS NEW RESTART ROUTE ---
@app.route('/restart')
def restart_pc():
    os.system("shutdown /r /t 1") # /r for restart, /t 1 for 1 second delay
    return "Restart command sent."
# --- END NEW RESTART ROUTE ---

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)