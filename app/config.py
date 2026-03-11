import os
import torch
from dotenv import load_dotenv

load_dotenv()

MAX_FILE_SIZE_MB = 100
MAX_FILE_SIZE = MAX_FILE_SIZE_MB * 1024 * 1024  # Convert to bytes  


DEVICE = "cuda" if torch.cuda.is_available() else "cpu" 

HF_TOKEN = os.getenv("HF_TOKEN")

# Model
MODEL_NAME = "large-v3"

ALIGN_MODEL = "WAV2VEC2_ASR_LARGE_LV60K_960H"

COMPUTE_TYPE = "float16" if DEVICE == "cuda" else "int8"

# File paths
UPLOAD_DIR = "audio_upload"

OUTPUT_DIR = "outputs"

ALLOWED_AUDIO_TYPES = {
    "audio/wav",
    "audio/mpeg",
    "audio/mp3",
    "audio/x-wav",
    "audio/flac",
    "audio/ogg",
    "audio/mp4",
    "audio/webm"
}