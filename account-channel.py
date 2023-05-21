import requests
import json

url = "https://www.rubika.ir/ajax/channels/moreChannels"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

payload = {
    "offset": 0,
    "limit": 100
}

response = requests.post(url, headers=headers, data=payload)

if response.status_code == 200:
    data = json.loads(response.content.decode('utf-8'))
    for channel in data["channels"]:
        print("Channel Name: ", channel["name"])
        print("Channel ID: ", channel["id"])
        print("Channel Owner ID: ", channel["owner_id"])
        print("Channel Description: ", channel["description"])
        print("Channel Followers: ", channel["follows"])
        print("-------------")
else:
    print("Error: ", response.status_code)
