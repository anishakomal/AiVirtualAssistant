import speech_recognition
import pyttsx3
import requests

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)


def speak(audio):
    print(f" Jarvis Said : {audio}")
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source, 0, 10)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


import requests
def moviesInfo():
    # Replace 'YOUR_API_KEY' with your actual OMDb API key
    api_key = '4a2a54e7'

    # Base URL for OMDb API
    base_url = 'http://www.omdbapi.com/'

    # Movie title to search for
    speak('Enter Movie Name:')
    movie_title = input()

    # Construct the API request URL
    url = f'{base_url}?apikey={api_key}&t={movie_title}'

    # Send GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse JSON response
        movie_data = response.json()

        # Display movie information
        title = movie_data['Title']
        year = movie_data['Year']
        summaries = movie_data['Plot']
        # rating = movie_data['imdbRating']

        # print('Title:', title)
        # speak('Title is {title}' )

        # print('Year:', movie_data['Year'])
        # print('Year:', year)
        # speak(year)

        # print('Plot:', summaries)
        # speak(summaries)

        # Display IMDb rating
        # print('IMDb Rating:', movie_data['imdbRating'])
        # You can access more information from the 'movie_data' dictionary

        # Access more information from the 'movie_data' dictionary
        print('Title:', movie_data['Title'])
        print('Year:', movie_data['Year'])
        print('Rated:', movie_data['Rated'])
        print('Released:', movie_data['Released'])
        print('Runtime:', movie_data['Runtime'])
        print('Genre:', movie_data['Genre'])
        print('Director:', movie_data['Director'])
        print('Writer:', movie_data['Writer'])
        print('Actors:', movie_data['Actors'])

        print('Language:', movie_data['Language'])
        print('Country:', movie_data['Country'])
        print('Awards:', movie_data['Awards'])
        print('Poster URL:', movie_data['Poster'])
        print('IMDb Rating:', movie_data['imdbRating'])
        print('Plot:', movie_data['Plot'])
    else:
        print('Error:', response.status_code)

moviesInfo()
