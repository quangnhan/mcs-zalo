import requests

# Your FastAPI backend URL
BASE_URL = "http://localhost:8001"

# The conversation ID you want to fetch messages from
collection_name = "messages"

# Replace this with a valid JWT from your auth service
jwt_token = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ0MTI5OTk3LCJpYXQiOjE3NDQxMjkwOTcsImp0aSI6IjI2YmE5MzA3ZTRmZjQyYWRhZjRkNmZjN2U2NzYyYjI3IiwidXNlcl9pZCI6MX0.UwA6Rjz0xY4_bUlY0dE9LNL2hD4aDG8SkGZ3zdxmhpVEJ2PwOOZwxuTKj84BBemi9PB4EACZhQuuF10R88LU_g"

# Construct the full URL
url = f"{BASE_URL}/collections/{collection_name}"

# Set the Authorization header
headers = {
    "Authorization": f"Bearer {jwt_token}"
}

# Send the GET request
response = requests.get(url, headers=headers)

# Print response
if response.status_code == 200:
    data = response.json()
    print("Documents:")
    for msg in data["documents"]:
        print(msg)
else:
    print("Failed to fetch messages:", response.status_code, response.text)
