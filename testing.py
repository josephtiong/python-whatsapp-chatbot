import requests

url = "https://gate.whapi.cloud/messages/text"

payload = {
    "typing_time": 0,
    "body": "testing text",
    "to": "120363364397326934@g.us"

}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer "
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)