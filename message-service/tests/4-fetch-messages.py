import requests

# Your FastAPI backend URL
BASE_URL = "http://localhost:8001"

# Replace this with a valid JWT token
jwt_token = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ0Mjk0MDQxLCJpYXQiOjE3NDQyMDc2NDEsImp0aSI6IjMxOWRlZDkwOWU3ODQ0MGRhNDQzNWI2MjY3ZDA5NzFmIiwidXNlcl9pZCI6MX0.xewjJLrTYZEfkl0OpF3iwZsVju9dcIcZAoQvifXHlIV-_jfZbViXR3nY4ViSe1aWXgeXETbuYzdyPj_YFrbz8w"

# Test data
conversation_id = "message_123"
url = f"{BASE_URL}/api/v1/chat/{conversation_id}"

headers = {
    "Authorization": f"Bearer {jwt_token}",
    "Content-Type": "application/json"
}


# Send the POST request
response = requests.get(url, headers=headers)

# Print response
if response.status_code == 200:
    messages = response.json()
    for msg in messages:
        print(msg)
else:
    print("Failed to fetch messages:", response.status_code, response.text)

