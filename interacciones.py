import requests
import uuid

def send_interaction():
    # Define the URL for the Discord API endpoint
    url = "https://discord.com/api/v9/interactions"

    # Define the headers with your bot token
    headers = {
        "Authorization": ""  # Replace with your bot token
    }
    nonce = str(uuid.uuid4())[:32]
    # Define the JSON payload
    payload = {
        "type": 3,  # STOCk
        "nonce": nonce,
        "guild_id": "",  # Guild id NO
        "channel_id": "",  # Channel id NO
        "message_flags": 0,  # STOCK NO
        "session_id": "",  # PUEDESER
        "message_id": "",  # Message id SI
        "application_id": "",  # Mudae Id NO
        "data": {  # STOCK
            "component_type": 2,
            "custom_id": ""
        }
    }

    # Send the POST request
    response = requests.post(url, json=payload, headers=headers)

    # Print the response
    if response.status_code == 204:
        print("Request was successful")
        print(response.text)
    else:
        print("Failed to send request")
        print(f"Status code: {response.status_code}")
        print(response.text)

# Call the function
send_interaction()
