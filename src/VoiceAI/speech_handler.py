# V1
'''import speech_recognition as sr
recognizer = sr.Recognizer()

def listen() -> None:
    with sr.Microphone() as source:
            print("\n🎙️ Say something...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
    return recognizer.recognize_google(audio)'''

# V2
import time
import speech_recognition as sr

recognizer = sr.Recognizer()

def listen(**kwargs) -> str:
    with sr.Microphone() as source:
        print("\n🎙️ Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    # Save the audio to a WAV file for debugging
    with open("debug_audio.wav", "wb") as f:
        f.write(audio.get_wav_data())

    return recognizer.recognize_google(audio_data=audio, **kwargs)

def listen_bylingual(**kwargs) -> str:
    with sr.Microphone() as source:
        print("\n🎙️ Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    # Save the audio to a WAV file for debugging
    with open("debug_audio.wav", "wb") as f:
        f.write(audio.get_wav_data())

    try:
        text = recognizer.recognize_google(audio_data=audio, language="en-US",**kwargs)
    finally:
        for wakeup_call in ["hey", "hello"]:
            if wakeup_call in text.lower():
                return text
    try:
        text = recognizer.recognize_google(audio_data=audio, language="ml-IN",**kwargs)
    finally:
        for wakeup_call in ["എന്നോട് പറയ"]:
            if wakeup_call in text:
                return text
    raise sr.UnknownValueError()

# Test
if __name__ == "__main__":
    while True:
        try:
            text = listen_bylingual()
            print("📝 You said:", text)
            '''for wakeup_call in ["hey", "hello"]:
                if wakeup_call in text.lower():
                    time.sleep(5)'''
        except sr.UnknownValueError or Exception("cannot access local variable 'text' where it is not associated with a value"):
            print("❌ Sorry, I couldn't understand that.")
        except sr.RequestError as e:
            print(f"🔌 Request error: {e}")
        except Exception as e:
            print(f"⚠️ Error: {e}")
