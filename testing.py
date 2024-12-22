import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

url = "https://gate.whapi.cloud/messages/text"

payload = {
    "typing_time": 0,
    "body": "New day - new",
    "to": "120363364397326934@g.us"

}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": f"Bearer {os.getenv('TOKEN')}"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)