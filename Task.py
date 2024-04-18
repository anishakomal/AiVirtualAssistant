# Functions
import datetime
from Speak import Say


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


def NonInputExecution(query):
    query = str(query)
    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    elif "day" in query:
        Day()

def InputExecution(tag,query):

    if "wikipedia" in tag:
        query = str(query).replace("who is", "").replace("about",  "").replace("wikipedia", "").replace("what is", "")
        import wikipedia
        result = wikipedia.summary(query)
        Say(result)

    elif "google" in tag:
        query = str(query).replace("google","").replace("search","")
        import pywhatkit
        pywhatkit.search(query) # Browser Open hoga or usmei search hoga


