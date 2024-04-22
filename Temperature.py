from Listen import Listen
from Speak import Say
import requests


# Function to get weather updates
def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != "404":
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        Say(f"The current temperature in {city} is {temperature}°C with {weather_description}.")
    else:
        Say(f"Sorry, I couldn't find weather information for {city}.")


city_name = "Bengaluru"
api_key ="c6e525bdcb87fc3240e17575902acc9c"
get_weather(city_name,api_key)