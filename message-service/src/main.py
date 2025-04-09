from fastapi import FastAPI
from src.chat import router as chat_router
from src.auth.middleware import AuthMiddleware

app = FastAPI()

# Apply middleware globally
app.add_middleware(AuthMiddleware)

# Include the auth router
app.include_router(chat_router.router, prefix="/api/v1/chat")

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI project"}
