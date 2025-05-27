# V1
'''from gtts import gTTS
import os
from config import GEMINI_CONFIG

def speak(text: str) -> None:
    tts = gTTS(text=text)
    tts.save("output.mp3")
    os.system(f'ffplay -nodisp -autoexit -af "atempo={GEMINI_CONFIG["tts_speed"]}" output.mp3')
'''
# V@2
'''import os
import asyncio
import edge_tts
import tempfile

async def speak_async(text: str, voice="en-IN-NeerjaNeural", rate="+10%"):
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as fp:
        output_path = fp.name
    communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate)
    await communicate.save(output_path)
    os.system(f'ffplay -nodisp -autoexit {output_path}')

# Run async
def speak(text, voice="ml-IN-SobhanaNeural", rate="+15%"):
    asyncio.run(speak_async(text, voice, rate))

if __name__ == '__main__':
    speak("Hello! നിങ്ങൾക്ക് സുഖമാണോ? This is a mix of English and Malayalam.")'''

# V3
import asyncio
import edge_tts
import os

async def save2_async(text: str, voice="ml-IN-SobhanaNeural", rate="+10%"):
    communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate)
    await communicate.save("output.mp3")

async def speak2_async(text: str, voice="ml-IN-SobhanaNeural", rate="+10%"):
    await save2_async(text, voice, rate)
    os.system('ffplay -nodisp -autoexit output.mp3')

def speak(text, voice="ml-IN-SobhanaNeural", rate="+10%"):
    asyncio.run(speak2_async(text, voice, rate))

def process2(text, voice="en-GB-SoniaNeural", rate="+10%"):
    #communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate)
    #return communicate
    tts = gTTS(text=text)
    return tts

# Example usage
if __name__ == "__main__":
    speak2("Hello User, ഞാൻ ചെറുതായി സംസാരിക്കുകയാണ്.")
