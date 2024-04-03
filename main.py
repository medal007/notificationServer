from datetime import datetime

import requests

# Replace these values with your own app_id and rest_api_key
app_id = ""
rest_api_key = ""

# Define the notification data
notification_data = {
    "app_id": app_id,
    "included_segments": ["Active Users"],
    "include_external_user_ids": ["+23278344558"],
    "contents": {"en": "Chrislin Sent Le 250.00 To Your Gentri Wallet"},
    "priority": 10,
    "send_after": datetime.now().isoformat(),  # Send the notification immediately
}

# Make a POST request to send the notification
response = requests.post(
    "https://onesignal.com/api/v1/notifications",
    headers={"Authorization": f"Basic {rest_api_key}"},
    json=notification_data
)

# Check the response
if response.status_code == 200:
    print("Notification sent successfully!")
    print(response.text)
else:
    print(f"Failed to send notification. Status code: {response.status_code}")
    print(response.text)
