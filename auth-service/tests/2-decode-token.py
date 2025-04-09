from jose import jwt
from jose.exceptions import JWTError, ExpiredSignatureError

# Example values
jwt_token = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ0Mjk0MDQxLCJpYXQiOjE3NDQyMDc2NDEsImp0aSI6IjMxOWRlZDkwOWU3ODQ0MGRhNDQzNWI2MjY3ZDA5NzFmIiwidXNlcl9pZCI6MX0.xewjJLrTYZEfkl0OpF3iwZsVju9dcIcZAoQvifXHlIV-_jfZbViXR3nY4ViSe1aWXgeXETbuYzdyPj_YFrbz8w"
SECRET_KEY = "123abc456def789ghi0123456789jklmnopqrs"
ALGORITHM = "HS512"

try:
    payload = jwt.decode(jwt_token, SECRET_KEY, algorithms=[ALGORITHM])
    print("✅ Token is valid. Payload:")
    print(payload)
except ExpiredSignatureError:
    print("❌ Token has expired")
except JWTError as e:
    print(f"❌ Invalid token: {str(e)}")
