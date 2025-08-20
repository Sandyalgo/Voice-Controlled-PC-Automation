import requests
import json

def get_ngrok_url():
    try:
        response = requests.get("http://127.0.0.1:4040/api/tunnels")
        tunnels = response.json()["tunnels"]
        for tunnel in tunnels:  
            if tunnel["public_url"].startswith("https://"):
                return tunnel["public_url"]
    except Exception as e:
        print("Error getting ngrok URL:", e)
    return None

def send_to_ifttt(url):
    event_name = "update_url"
    ifttt_key = "e9yVhjD4cC5AW1N00HTV8lJEVXgxxWZ69FxXAFiFhhT"
    webhook_url = f"https://maker.ifttt.com/trigger/{event_name}/with/key/{ifttt_key}"
    
    payload = {'value1': url}
    headers = {'Content-Type': "application/json"}

    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    
    print("Sent to IFTTT:", payload)
    print("Response code:", response.status_code)
    print("Response text:", response.text)

    if response.status_code == 200:
        print("✅ IFTTT updated successfully!")
    else:
        print("❌ Failed to update IFTTT")

if __name__ == "__main__":
    ngrok_url = get_ngrok_url()
    if ngrok_url:
        print("Current Ngrok URL:", ngrok_url)
        send_to_ifttt(ngrok_url)
    else:
        print("⚠ Could not find Ngrok HTTPS tunnel.")