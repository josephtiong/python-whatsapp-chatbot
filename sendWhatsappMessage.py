import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

def send_whapi_request(message):
    
    TOKEN = os.getenv('TOKEN')
    url = os.getenv('API_SENDTEXT')
    GROUD_ID = os.getenv('GROUP_ID')

    payload = {
        "typing_time": 0,
        "body": message,
        "to": f"{GROUD_ID}"
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {TOKEN}"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)

send_whapi_request("Hello, World!")