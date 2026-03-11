import whisperx
from app.models.whisperx_largev3 import get_model
from app.models.diarization_model import get_diarization_model

model = get_model()
diarization_model = get_diarization_model()

def transcribe_audio(audio_path):
    audio = whisperx.load_audio(audio_path)
    result = model.transcribe(audio)

    diarize_segments = diarization_model(audio)

    # assign speaker to words
    result = whisperx.assign_word_speakers(
        diarize_segments,
        result
    )

    return result

