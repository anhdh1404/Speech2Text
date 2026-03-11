import os
from unittest import result
import shutil

from app.config import UPLOAD_DIR
from app.services.transcribe_service import transcribe_audio
from app.services.merged_segments import merge_speaker_segments
from app.services.sentence_splitter import split_sentences


def speech_to_text(file):

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # save file (stream)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:

        result = transcribe_audio(file_path)
        segments = result["segments"]

        merged = merge_speaker_segments(segments)

        dialogues = split_sentences(merged)

        return dialogues

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)




