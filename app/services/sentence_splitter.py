import re
## Tách câu từ các đoạn đã được merge theo speaker
def split_sentences(segments):

    final_dialogues = []

    for seg in segments:

        sentences = re.split(r'(?<=[.!?])\s+', seg["text"])

        duration = seg["end"] - seg["start"]
        step = duration / max(len(sentences),1)

        cur_start = seg["start"]

        for s in sentences:

            if not s.strip():
                continue

            final_dialogues.append({
                "speaker": seg.get("speaker","UNK"),
                "start": cur_start,
                "end": cur_start + step,
                "text": s.strip()
            })

            cur_start += step

    return final_dialogues