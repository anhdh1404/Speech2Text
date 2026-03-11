import os
import torch
from dotenv import load_dotenv

load_dotenv()

DEVICE = "cuda" if torch.cuda.is_available() else "cpu" 

HF_TOKEN = os.getenv("HF_TOKEN")

# Model
MODEL_NAME = "large-v3"

ALIGN_MODEL = "WAV2VEC2_ASR_LARGE_LV60K_960H"

COMPUTE_TYPE = "float16" if DEVICE == "cuda" else "int8"

# File paths
UPLOAD_DIR = "audio_upload"

OUTPUT_DIR = "outputs"
