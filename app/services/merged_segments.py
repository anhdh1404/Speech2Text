## merge các đoạn có cùng speaker thành một đoạn duy nhất
def merge_speaker_segments(segments):

    segments = sorted(segments, key=lambda x: x["start"])
    merged = []
    current = None

    for seg in segments:

        if current is None:
            current = seg.copy()
            continue

        if seg.get("speaker") == current.get("speaker"):
            # Nếu cùng speaker, cập nhật thời gian kết thúc và nối text
            current["end"] = seg["end"]
            current["text"] += " " + seg["text"]

        else:
            # Nếu khác speaker, lưu đoạn hiện tại và bắt đầu đoạn mới
            merged.append(current)
            current = seg.copy()

    if current:
        merged.append(current)

    return merged