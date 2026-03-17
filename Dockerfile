FROM python:3.10-slim

WORKDIR /app

# cài ffmpeg cho whisperx
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

# copy requirements
COPY requirements.txt .

# install python libs
RUN pip install --no-cache-dir -r requirements.txt

# copy toàn bộ project
COPY app ./app

# tạo thư mục upload
RUN mkdir -p audio_upload

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]