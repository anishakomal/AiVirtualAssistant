import pywhatkit
import wikipedia
import webbrowser
from Speak import Say

# def searchGoogle(query):
#     if "google" in query:
#         import wikipedia as googleScrap
#         query = query.replace("jarvis", "")
#         query = query.replace("google search", "")
#         query = query.replace("google", "")
#         Say("This is what I found on google")
#         try:
#             pywhatkit.search(query)
#             result = googleScrap.summary(query, 1)
#             Say(result)
#         except:
#             Say("No speakable output available")


# def searchWikipedia(query):
#     if "wikipedia" in query:
#         Say("Searching from wikipedia...")
#         query = query.replace("search wikipedia", "")
#         query = query.replace("wikipedia", "")
#         result = wikipedia.summary(query, sentences=1)
#         Say("According to wikipedia")
#         print(result)
#         Say(result)

def searchYoutube(query):
    if "youtube" in query:
        Say("This is what I found for your search!")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        query = query.replace("jarvis", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        Say("Done, sir")


