"""
The function of this script is too 
* Fetch weather and crypto prices through openweathermap api and coinmarketcapapi 
* log results into a file using python logging module 
* send alerts when conditions are met ( discord + console )
"""

import logging, time,os,requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
OWM_API = os.getenv("openweatherapi")
WEBHOOK = os.getenv("discord_visual_hook")
URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest" #url 
CMC_KEY = os.getenv("coinmarketcap") 

logging.basicConfig(
    level=logging.INFO,
    filename="alert.log",
    filemode="a",
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def fetch_weather(city="Sydney"):
    if not OWM_API:
        raise RuntimeError("Missing weather api")
    url = "https://api.openweathermap.org/data/2.5/weather"
    r = requests.get(
        url, 
        params= {"q": city, "appid": OWM_API, "units": "metric"},
        timeout=10
     )
    r.raise_for_status()
    data = r.json()
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    desc = data["weather"][0]["description"]
    return temp, humidity, desc

def fetch_price(symbol):
    if not CMC_KEY:
        raise RuntimeError("Missing API key")
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest" #url 
    headers = {
    "Accepts": "application/json", 
    "X-CMC_PRO_API_KEY": CMC_KEY} 
    #send request.get
    r = requests.get(url, headers=headers, params={"symbol": symbol, "convert": "USD"}, timeout=10)
    r.raise_for_status()
    return r.json()["data"][symbol]["quote"]["USD"]["price"]

def send_discord(content:str,webhook:str,timeout: int = 10):
    if not webhook:
        return #skip if webhook is not configure.
    r = requests.post(
        webhook,
        json={"content": content},
        timeout=timeout
    )
    if r.status_code not in (200,204):
        logging.error(f"Discord error {r.status_code}: {r.text}")
    
def send_alert(msg, use_console=True, use_discord=False): #by defualt send message on console, unless overwritter
    if use_console: 
        print(f"[ALERT] {msg}")
    if use_discord:
        send_discord(msg, WEBHOOK)

def main(duration=60,cooldown=10):
    end = time.monotonic() + duration #run for duration time 
    last_btc_alert = 0.0
    btc_alert_cooldown = 300
    while time.monotonic() < end:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #weather check 
        try:
            temp, humidity, desc = fetch_weather()
            logging.info(f"Weather: {temp:.1f}°C, {humidity}% humidity, {desc}")
            if "rain" in desc.lower():
                send_alert("☔ Bring umbrella!", True,True)
        except Exception as e:
            logging.error(f"Failed to fetch weather: {e}")
        #crypto check 
        try:
            btc_price = fetch_price("BTC")
            logging.info(f"BTC price: ${btc_price:,.2f}")
            now = time.monotonic()
            if btc_price <60000 and (now - last_btc_alert) >= btc_alert_cooldown:
                send_alert(f"🚨 BTC dropped: ${btc_price:,.2f}", True, True)
                last_btc_alert = now
        except Exception as e:
            logging.error(f"Failed to fetch BTC {e}")
        time.sleep(cooldown)

if __name__ == "__main__":
    main()