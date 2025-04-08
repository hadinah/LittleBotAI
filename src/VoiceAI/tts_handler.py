from gtts import gTTS
import os
from config import GEMINI_CONFIG

def speak(text: str) -> None:
    tts = gTTS(text=text)
    tts.save("output.mp3")
    os.system(f'ffplay -nodisp -autoexit -af "atempo={GEMINI_CONFIG["tts_speed"]}" output.mp3')