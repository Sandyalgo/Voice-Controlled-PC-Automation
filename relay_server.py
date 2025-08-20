import time
#import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import traceback
import requests # Needed to make requests to remote_control.py via its Ngrok URL

# --- Google Sheets Setup (Remains the same) ---
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# --- Google Sheet Configuration ---
SHEET_NAME = "ngrok_url_log"
COMMAND_CELL = "B1" # Cell where IFTTT writes the command
# We'll keep getting Ngrok URL from Column A as before.

# --- Function to get the latest Ngrok URL (from previous working code) ---
def get_latest_ngrok_url():
    try:
        sheet = client.open(SHEET_NAME).sheet1  # Open the first sheet
        # Get all entries in Column A
        list_of_raw_entries = sheet.col_values(1)
        valid_urls = []
        for entry in list_of_raw_entries:
            if entry:
                https_index = entry.find("https://")
                if https_index != -1:
                    potential_url = entry[https_index:].strip()
                    if potential_url.startswith("https://"):
                        valid_urls.append(potential_url)
        
        if not valid_urls:
            print("No valid Ngrok URLs found in Column A after filtering.")
            return None
        
        url = valid_urls[-1]
        return url
    except Exception as e:
        print(f"Error getting Ngrok URL from Google Sheet: {e}")
        traceback.print_exc()
        return None

# --- Function to execute commands ---
def execute_command(command, ngrok_base_url):
    print(f"Executing command: '{command}' via Ngrok URL: {ngrok_base_url}")
    try:
        if ngrok_base_url:
            # Construct the full URL for remote_control.py
            full_command_url = f"{ngrok_base_url}/{command}"
            print(f"Attempting to call: {full_command_url}")
            response = requests.get(full_command_url)
            if response.status_code == 200:
                print(f"Command '{command}' sent successfully. Response: {response.text}")
            else:
                print(f"Failed to send command '{command}'. Status: {response.status_code}, Response: {response.text}")
        else:
            print("Cannot execute command: Ngrok URL is not available.")
    except Exception as e:
        print(f"Error executing command '{command}': {e}")
        traceback.print_exc()

# --- Main Polling Loop ---
def start_polling():
    print("Starting Google Sheet polling for commands...")
    sheet = client.open(SHEET_NAME).sheet1 # Open sheet once outside loop

    while True:
        try:
            # Read the command cell
            # FIXED: Use acell() for string addresses like "B1"
            command = sheet.acell(COMMAND_CELL).value
            
            if command and command.strip() != "":
                command = command.strip().lower() # Normalize command string

                print(f"\nDetected command: '{command}' in cell {COMMAND_CELL}")

                ngrok_url = get_latest_ngrok_url() # Get the latest Ngrok URL
                
                if ngrok_url:
                    execute_command(command, ngrok_url)
                    # Clear the command cell after execution to prevent re-triggering
                    # FIXED: Use update_acell() for string addresses
                    sheet.update_acell(COMMAND_CELL, "")
                    print(f"Command '{command}' executed and cell {COMMAND_CELL} cleared.")
                else:
                    print("Ngrok URL not available, cannot execute command.")
            
            time.sleep(5) # Poll every 5 seconds
        except gspread.exceptions.SpreadsheetNotFound:
            print(f"Error: Spreadsheet '{SHEET_NAME}' not found. Please check name and permissions.")
            time.sleep(30) # Wait longer before retrying
        except Exception as e:
            print(f"An unexpected error occurred during polling: {e}")
            traceback.print_exc()
            time.sleep(10) # Wait a bit before retrying after an error

if __name__ == '__main__':
    start_polling()