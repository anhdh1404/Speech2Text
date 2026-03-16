import whisperx
import os

import app
from app.config import MODEL_NAME, DEVICE, COMPUTE_TYPE, HF_TOKEN

os.environ["HF_TOKEN"] = HF_TOKEN

model = whisperx.load_model(
    MODEL_NAME,
    DEVICE,
    language="en",
    compute_type=COMPUTE_TYPE
)

@app.on_event("startup")
def get_model():
    return model