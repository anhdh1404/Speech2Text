from pydantic import BaseModel
from typing import List


class TranscriptSegment(BaseModel):

    speaker: str
    start: float
    end: float
    text: str


class STTResponse(BaseModel):

    dialogues: List[TranscriptSegment]