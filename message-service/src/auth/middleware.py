from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from jose import JWTError, jwt
from src.config import settings

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        token = request.headers.get("Authorization")
        if not token or not token.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Missing or invalid token")

        try:
            payload = jwt.decode(token[7:], settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            request.state.user = payload
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid token")

        return await call_next(request)
