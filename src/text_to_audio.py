import PyPDF2
from gtts import gTTS
import os


def text_to_audio(text, output_path):
    tts = gTTS(text, lang="pt")
    tts.save(output_path)
