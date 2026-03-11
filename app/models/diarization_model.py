from app.config import DEVICE, HF_TOKEN
from whisperx.diarize import DiarizationPipeline

print("Loading diarization model...")

diarization_model = DiarizationPipeline(
    token=HF_TOKEN,
    device=DEVICE
)

def get_diarization_model():
    return diarization_model