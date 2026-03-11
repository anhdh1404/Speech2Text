from fastapi import FastAPI
from app.routers.stt_router import router

app = FastAPI(
    title="Speech To Text API"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to Speech To Text API"
    }

app.include_router(router)