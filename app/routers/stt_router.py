from fastapi import APIRouter,HTTPException, UploadFile, File
from app.services.STT_service import speech_to_text
from app.schemas import STTResponse
from fastapi.concurrency import run_in_threadpool   
from app.config import MAX_FILE_SIZE, MAX_FILE_SIZE_MB, ALLOWED_AUDIO_TYPES


router = APIRouter(
    prefix="/stt",
    tags=["Speech To Text"]    
)

@router.post("/transcribe", response_model=STTResponse)
async def transcribe(file: UploadFile = File(...)):

    contents = await file.read()

    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail=f"File size exceeds the maximum limit of {MAX_FILE_SIZE_MB} MB."
        )

    if file.content_type not in ALLOWED_AUDIO_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type. Please upload a valid audio file."
        )

    # reset pointer
    file.file.seek(0)

    result = await run_in_threadpool(speech_to_text, file)

    return {"dialogues": result}


