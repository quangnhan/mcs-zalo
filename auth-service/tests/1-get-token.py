import requests

url = "http://localhost:8000/api/token/"
data = {
    "username": "admin",
    "password": "admin"
}

response = requests.post(url, json=data)

if response.status_code == 200:
    tokens = response.json()
    print("Access Token:", tokens["access"])
    print("Refresh Token:", tokens["refresh"])
else:
    print("Failed to get token:", response.status_code, response.text)
