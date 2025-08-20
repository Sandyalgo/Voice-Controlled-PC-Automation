

# <img src="https://github.com/user-attachments/assets/4aeb748d-0b92-4932-a8e2-08a008b3813c" alt="Microphone Icon" width="40" height="40" /> Voice-Controlled PC Automation

> Control your Windows PC remotely using **Google Assistant voice commands**.  
This project lets you **lock, restart, or shut down** your computer from anywhere in the world without worrying about static IPs or firewall restrictions.  

---

## 🏆 Badges  

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)  
![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)  
![Ngrok](https://img.shields.io/badge/Ngrok-Secure_Tunnel-orange?logo=ngrok)  
![Stars](https://img.shields.io/github/stars/Sandyalgo/Voice-Controlled-PC-Automation?style=social)  
![Forks](https://img.shields.io/github/forks/Sandyalgo/Voice-Controlled-PC-Automation?style=social)  
![License](https://img.shields.io/badge/License-MIT-green)  

---

## 🚀 Problem Statement  

Controlling a PC remotely is often challenging due to:  
- Dynamic IP addresses (especially in hostels or shared networks).  
- Restrictions like firewalls and no port-forwarding.  
- Lack of easy voice-based automation.  

✅ This project solves the issue by combining **Google Assistant + IFTTT + Google Sheets + Flask + Ngrok**, enabling seamless **voice-controlled remote automation**.  

---

## ⚙️ How It Works  

The system works in a **four-step communication pipeline**:  

1️⃣ You say a command like **“Hey Google, lock my PC”**.  
2️⃣ **IFTTT** captures the command and writes it into a **Google Sheet**.  
3️⃣ A **Python script** on your PC continuously checks the sheet for new commands.  
4️⃣ When a command appears, it is sent via **Flask API (exposed through Ngrok)** → executed on your Windows PC.  

📌 Example:  
- Voice command → “activate pc lock”  
- IFTTT → Writes `lock` into Google Sheet  
- Python script → Reads `lock` → Calls Flask API  
- Flask → Executes system command → PC locks 🚀  
---
<img width="1475" height="755" alt="Screenshot 2025-08-20 234023" src="https://github.com/user-attachments/assets/50e2e0ac-e481-4014-bf92-923c86fc3908" />

---
![trigger](https://github.com/user-attachments/assets/cd83dfe1-78b2-4d7c-ac93-b626e6f25956)

---
<img width="1247" height="619" alt="Screenshot 2025-08-20 234241" src="https://github.com/user-attachments/assets/eba520f0-d2ae-4562-97fe-c4ada53119c1" />

---
<img width="1474" height="755" alt="Screenshot 2025-08-20 234145" src="https://github.com/user-attachments/assets/41b28e0f-f0ef-48cc-a612-34e82ec58886" />

---
<img width="1336" height="666" alt="Screenshot 2025-08-20 234518" src="https://github.com/user-attachments/assets/2dedcd0a-0f36-472b-8c4a-6486df792c4d" />

---

## ✨ Features  

- 🎙 **Voice Control** – Trigger commands using Google Assistant.  
- 🌍 **Remote Access** – Works from **anywhere** (even outside local network).  
- 🔄 **Dynamic IP Handling** – Ngrok auto-manages changing IPs.  
- 🖥 **System Commands** – Lock, restart, shut down, or extend with custom commands.  
- ⚡ **Automation on Startup** – Runs in background using Windows Task Scheduler.  
- 🔒 **Secure** – Commands only executed when authorized via Google Assistant.  

---

## 🛠️ Tech Stack  

- **Python** – Backend logic.  
- **Flask** – REST API for executing PC commands.  
- **Ngrok** – Public secure tunnel for local Flask server.  
- **Google Sheets API** – Cloud-based communication hub.  
- **IFTTT** – Connects Google Assistant → Google Sheets.  
- **Windows Batch Scripts** – Automates startup process.  

---

## 📂 Project Structure  

📦 Voice-Controlled-PC-Automation
┣ 📜 auto_start.bat # Starts Ngrok + Flask + Listener
┣ 📜 relay_server.py # Flask API server
┣ 📜 remote_control.py # Reads Google Sheets + executes commands
┣ 📜 update_ifttt.py # Updates Ngrok URL in IFTTT
┣ 📜 ngrok.exe # Ngrok tunnel
┣ 📜 .gitignore # Ignored files (includes credentials.json ✅)
┗ 📜 README.md


📌 Note: `credentials.json` is excluded from GitHub for security (kept in `.gitignore`).  

---

## 🖥️ Setup Instructions  

### 1. Clone the Repository  
```bash

git clone https://github.com/Sandyalgo/Voice-Controlled-PC-Automation.git
cd Voice-Controlled-PC-Automation

2. Install Dependencies
pip install Flask requests gspread oauth2client

3. Configure Ngrok
Download ngrok.exe → Download here
Authenticate:
ngrok config add-authtoken YOUR_AUTH_TOKEN

4. Set up Google Sheets API
Create a Google Cloud Project.
Enable Google Sheets API.
Create Service Account → Download credentials.json.
Share your Google Sheet with the service account email.

5. Configure IFTTT
Create Google Assistant → Google Sheets applets.
Example trigger: “Lock my PC” → Write lock in Sheet.

6. Run the Project
python remote_control.py
or use
auto_start.bat
to run everything automatically.
```
---

🔮 Future Improvements  

&emsp;📡 Add real-time WebSocket communication (instead of polling).  
&emsp;🤖 Add custom commands like opening apps, playing music, etc.  
&emsp;📱 Build a mobile companion app for direct control.  
&emsp;🔐 Enhance security with authentication tokens.  

---
🤝 Contributing  

- Contributions are welcome!  
- Fork the repo  
- Create a feature branch  
- Submit a pull request 🚀  

---
🧑‍💻 Author  
👤 Sandeep Gadi  
[![GitHub](https://img.shields.io/badge/GitHub-Sandyalgo-black?style=for-the-badge&logo=github)](https://github.com/Sandyalgo)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sandeep%20Gadi-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/sandeepgadi/)  

---
⭐ Support  
- If you like this project, give it a star ⭐ on GitHub. It helps others find it too!  
