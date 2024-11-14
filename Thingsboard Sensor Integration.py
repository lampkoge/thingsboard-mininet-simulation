import requests
import time
import json

THINGSBOARD_HOST = "http://localhost"  # replace with Thingsboard server URL
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"  # replace with actual access token

def send_fire_alerts():
    url = f"{THINGSBOARD_HOST}/api/v1/{ACCESS_TOKEN}/telemetry"
    headers = {"Content-Type": "application/json"}
    
    while True:
        # Simulated fire alert data
        data = {
            "temperature": 75.0,
            "smoke_level": 2.5,
            "fire_alert": True  # this could trigger evacuation
        }
        requests.post(url, headers=headers, data=json.dumps(data))
        print("Sent fire alert to Thingsboard:", data)
        time.sleep(10)

if __name__ == "__main__":
    send_fire_alerts()
