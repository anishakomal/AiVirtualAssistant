# Speak Function
# How to use voices
# How to change voices
# how to add voices
# how to add external voices
# how to add Google Assistant voices etc.

import pyttsx3
import speech_recognition

print("hello")
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 180)


def speak(audio):
    print(" ")
    print(f": {audio}")
    print(" ")
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 10)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query.lower()

def takeCommand_Hindi():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 10)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='hi')
        print(f"Your Command: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query.lower()






