from fastapi import APIRouter, UploadFile, File
from app.services.STT_service import speech_to_text
from app.schemas import STTResponse
from fastapi.concurrency import run_in_threadpool   


router = APIRouter(
    prefix="/stt",
    tags=["Speech To Text"]    
)

@router.post("/transcribe", response_model=STTResponse)
async def transcribe(file: UploadFile = File(...)):

    result = await run_in_threadpool(speech_to_text, file)


    return {
        "dialogues": result
    }


