import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
import pyttsx3


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""


def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def main():
    print("Hello! How can I assist you today?")
    while True:
        command = listen()
        if "translate" in command.lower():
            print("What would you like to translate?")
            text_to_translate = listen()
            print("To which language?")
            target_language = listen()
            translated_text = translate_text(text_to_translate, target_language)
            print("Translated text:", translated_text)
            speak(translated_text)
        elif "exit" in command.lower():
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
