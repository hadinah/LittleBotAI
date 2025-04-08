from speech_handler import listen, sr
from gemini_handler import get_response
from tts_handler import speak
from functions import run_command

while True:
    try:
        #text = "It is too dark in this room"
        text = listen()
        print("📝 You said:", text)

        command, reply = get_response(text)
        print("🤖 Little Bot says:", reply)
        print("Command", command)

        run_command(command)
        speak(reply)
    except sr.UnknownValueError:
        print("❌ Sorry, I couldn't understand that.")
    except sr.RequestError as e:
        print(f"🔌 Request error: {e}")
    except Exception as e:
        print(f"⚠️ Error: {e}")
