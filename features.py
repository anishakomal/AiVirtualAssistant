import pywhatkit
import pyttsx3
import main
import wikipedia
from pywikihow import WikiHow, search_wikihow
import os


def GoggleSearch(term):
    query = term.replace("jarvis", "")
    query = query.replace("what is", "")
    query = query.replace("how to", "")
    query = query.replace("what is", "")
    query = query.replace(" ", "")
    query = query.replace("what do you mean by", "")

    Query = str(term)
    pywhatkit.search(Query)

    if 'how to' in Query:
        max_result = 1
        how_to_func = search_wikihow(query=Query, max_results=max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print()
        main.speak(how_to_func[0].summary)
    else:
        pywhatkit.search(Query)
        search = wikipedia.summary(Query, 2)
        main.speak(f": According To Your Search: {search}")


def Alarm(query):
    TimeHere = open('C:\\Users\\Administrator\\PycharmProjects\\AiVirtualAssistant\\Data.txt', 'a')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("C:\\Users\\Administrator\\PycharmProjects\\AiVirtualAssistant\\alarm.py")


Alarm('set alarm for 17 and 19')

