# Functions
import datetime
import requests
import pywhatkit
from Speak import Say
from googletrans import Translator
from Listen import Listen
import credential


# 2-Types
# i) Non Input eg: Date, Time,Speed Test
# ii)Input eg: Google search, wikipedia

# ******************************************************* NoN Input Wala Task
def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)


def Date():
    date = datetime.date.today()
    Say(date)


def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    advice = res['slip']['advice']
    print(advice)


def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text


def internet_speed():
    from Speedtest import get_speedtest
    get_speedtest()


def Movies():
    from MoviesDetails import moviesInfo
    moviesInfo()


def News():
    from NewHeadline import get_latest_news
    get_latest_news()



def WhatsApp():
    Say("Enter the phone Number")
    number = input("Enter Mob. Number:")
    Say("Write your Message here:")
    user_message = input("Message:")
    pywhatkit.sendwhatmsg_instantly(f"+91{number}", user_message)
    print("Message Sent Successfully!")
    Say("Message Sent Successfully!")

def Temperature():
    from Temperature import get_weather
    get_weather()



def NonInputExecution(query):
    query = str(query)
    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    elif "day" in query:
        Day()

    elif "random advice" in query:
        get_random_advice()

    elif "internet Speed" in query:
        internet_speed()


def InputExecution(tag, query):
    if "wikipedia" in tag:
        query = str(query).replace("who is", "").replace("about", "").replace("wikipedia", "").replace("what is", "")
        import wikipedia
        result = wikipedia.summary(query)
        Say(result)

    elif "google" in tag:
        query = str(query).replace("google", "").replace("search", "")
        import pywhatkit
        pywhatkit.search(query)  # Browser Open hoga or usmei search hoga

    elif "translate" in tag:
        print("What would you like to translate?")
        text_to_translate = Listen()
        print("To which language?")
        target_language = Listen()
        translated_text = translate_text(text_to_translate, target_language)
        print("Translated text:", translated_text)
        Say(translated_text)

    elif "movie" in tag:
        Movies()

    elif "news" in tag:
        News()

    elif "whatsapp" in tag:
        WhatsApp()

    elif "temperature" in tag:
        Temperature()
