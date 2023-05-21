import requests
import json
username = input("Enter Rubika username: ")
response = requests.get('https://rubika.ir/api/v1/users/search?q=' + username)
data = json.loads(response.text)
user_id = data[0]['id']
user_auth_id = data[0]['auth_id']
user_name = data[0]['username']
user_bio = data[0]['biography']

# چاپ اطلاعات حساب کاربری
print("User ID:", user_id)
print("User Auth ID:", user_auth_id)
print("Username:", user_name)
print("Biography:", user_bio)
