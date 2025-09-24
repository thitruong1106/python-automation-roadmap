"""
Weather Alert Bot 

The purpose of this script: 
- is to fetch weather from OpenWeatherMap API 
- print city, temp, humidity, and description in terminal 
- log results to csv every N seconds for M duration. 
- Alert user with umbrella is needed, if rain is expected 

Notes:
- requires .env file with OPENWEATHER API Key. 
- units: metric (C)

https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
"""

from dotenv import load_dotenv
import os,time,csv,requests,json
from datetime import datetime

#load api keys 
load_dotenv()
API_KEY = os.getenv("openweatherapi")
WEBHOOK = os.getenv("discord_visual_hook")

#write header to file once 
def ensure_header(path, header): 
    if not os.path.exists(path) or os.path.getsize(path) == 0: 
        with open(path, "a", newline='', encoding='utf-8') as f:
            csv.writer(f).writerow(header)

def fetch_weather(city="Sydney"):
    url = "http://api.openweathermap.org/data/2.5/weather?"
    resp = requests.get(
        url,
        params= {"q": city, "appid": API_KEY, "units": "metric"},
        timeout = 10
    )
    resp.raise_for_status()
    data = resp.json()
    #return temp, humidity, desc
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    desc = data["weather"][0]["description"]
    return temp, humidity, desc



def log_row(path, ts, city, temp, humidity, desc):
    with open(path, "a", newline ='', encoding='utf-8') as f:
        csv.writer(f).writerow([ts,city,temp,humidity,desc])

    #run for 30 minutes, 1800, with 10 minutes cool down or 600 seconds 

def discord_send(content:str, webhook:str, timeout: int = 10):
    if not webhook:
        raise ValueError("Missing discord webhook url")
    r = requests.post(
        webhook,
        json={"content": content},
        timeout = timeout
    )
    #Discord return 204 no content on success 
    if r.status_code not in (200,204):
        raise RuntimeError(f"Discord error {r.status_code}: {r.text}" )
    
def main(city="Sydney", cooldown=600, duration=1800, csv_path="python_roadmap/Day7to8//weather_log.csv"):
    #log header to csv path 
    ensure_header(csv_path, ["timestamp", "city", "temp_c", "humidity", "description"])
    # run loop with cooldown, fetch weather, log, and print
    end = time.monotonic() + duration
    last = 0.0 #never been printed 
    while time.monotonic() < end: #Run this while, time is less than end duration 
        now = time.monotonic() 
        if now - last >= cooldown:
            temp, humidity,desc = fetch_weather(city)
            ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            #print to terminal 
            print(f"{ts} | {city} | {temp:.1f}°C | {humidity}% | {desc}")
            if "rain" in desc.lower():
                print("☔ Bring umbrella")
                discord_send(f"**Umbrella alert**: Rain expected in {city}", WEBHOOK)
            elif "scattered clouds" in desc.lower():
                discord_send(f"🧣 clouds are scatter", WEBHOOK)
            #log to csv 
            log_row(csv_path, ts, city, temp, humidity, desc)
            last = now
        time.sleep(1)

if __name__ == "__main__":
    main()