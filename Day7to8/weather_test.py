"""
5. Mini-Project 2: Weather Alert Bot

Use OpenWeatherMap API (free, needs signup key).

Fetch current weather for a city.

Print "Sydney: 22°C, Clear sky".

Stretch: If rain is expected, print "Bring umbrella ☔".

https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
"""

from dotenv import load_dotenv
import os,time,csv,requests,json
load_dotenv()
API_KEY = os.getenv("openweatherapi")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
CITY = "GEELONG"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()
print(json.dumps(response, indent=4))

city = response["name"]
desc = response["weather"][0]["description"]
temp = response["main"]["temp"]

print(city, desc, temp)

if "rain" in desc.lower():
    print("Bring umbrella ☔")
elif "clear sky" in desc.lower():
    print("Clear Skies⛅")
elif "overcast clouds" in desc.lower():
    print("overcast skies 🌨️")


