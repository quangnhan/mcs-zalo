import requests

# Your FastAPI backend URL
BASE_URL = "http://localhost:8001"

# Replace this with a valid JWT from your auth service
jwt_token = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ0Mjk0MDQxLCJpYXQiOjE3NDQyMDc2NDEsImp0aSI6IjMxOWRlZDkwOWU3ODQ0MGRhNDQzNWI2MjY3ZDA5NzFmIiwidXNlcl9pZCI6MX0.xewjJLrTYZEfkl0OpF3iwZsVju9dcIcZAoQvifXHlIV-_jfZbViXR3nY4ViSe1aWXgeXETbuYzdyPj_YFrbz8w"

# Construct the full URL
collection_name = "message_123"
url = f"{BASE_URL}/api/v1/chat/collections/{collection_name}/"

# Set the Authorization header
headers = {
    "Authorization": f"Bearer {jwt_token}"
}

# Send the GET request
response = requests.get(url, headers=headers)

# Print response
if response.status_code == 200:
    documents = response.json()
    for doc in documents:
        print(doc)
else:
    print("Failed to fetch messages:", response.status_code, response.text)
