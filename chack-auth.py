import requests

def find_rubika_account_id_by_name(name):
    url = "https://api.rubika.ir/v1/users/search"
    params = {
        "q": name
    }
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN"
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data["data"]:
            return data["data"][0]["auth"]
        else:
            return None
    else:
        return None
