# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JCKQ1ZmLQXT6rnjcoZf9ZXCzRiXgWORX
"""

# Install Whisper and dependencies
!pip install -q git+https://github.com/openai/whisper.git
!pip install -q ffmpeg

from google.colab import files

# Upload an audio file (MP3, WAV, M4A, etc.)
uploaded = files.upload()

# List the uploaded file
import os
filename = next(iter(uploaded))
print(f"Uploaded file: {filename}")

import whisper

# Load Whisper model
model = whisper.load_model("medium")  # or "large" for better accuracy

# Transcribe uploaded file
result = model.transcribe(filename)

# Display result
print("\n🔍 Transcription:\n")
print(result["text"])