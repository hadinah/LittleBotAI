import speech_recognition as sr
recognizer = sr.Recognizer()

def listen() -> None:
    with sr.Microphone() as source:
            print("\n🎙️ Say something...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
    return recognizer.recognize_google(audio)