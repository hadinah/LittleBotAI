from speech_handler import listen, sr
from gemini_handler import get_response, give_get_response
from tts_handler import speak
from functions import *

while True:
    try:
        text = input("Enter Prompt: ") #"It is too dark in this room"
        #text = listen()
        print("📝 You said:", text)
        
        command, reply = get_response(text)
        #print("🤖 Little Bot says:", reply)
        #print("Command", command)

        print("..excecuting command")
        if "get_response" in command:
            speak(reply)
            run_command("from gemini_handler import my_initial_question; "+command, globals())
            run_command(command)
        else:
            run_command("from gemini_handler import my_initial_question; "+command, globals())
        speak(reply)
        publish("0")
    except sr.UnknownValueError:
        print("❌ Sorry, I couldn't understand that.")
    except sr.RequestError as e:
        print(f"🔌 Request error: {e}")
    except Exception as e:
        print(f"⚠️ Error: {e}")
