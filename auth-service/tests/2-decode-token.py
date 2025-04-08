from jose import jwt
from jose.exceptions import JWTError, ExpiredSignatureError

# Example values
token = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ0MTI5OTk3LCJpYXQiOjE3NDQxMjkwOTcsImp0aSI6IjI2YmE5MzA3ZTRmZjQyYWRhZjRkNmZjN2U2NzYyYjI3IiwidXNlcl9pZCI6MX0.UwA6Rjz0xY4_bUlY0dE9LNL2hD4aDG8SkGZ3zdxmhpVEJ2PwOOZwxuTKj84BBemi9PB4EACZhQuuF10R88LU_g"
SECRET_KEY = "123abc456def789ghi0123456789jklmnopqrs"
ALGORITHM = "HS512"

try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    print("✅ Token is valid. Payload:")
    print(payload)
except ExpiredSignatureError:
    print("❌ Token has expired")
except JWTError as e:
    print(f"❌ Invalid token: {str(e)}")
