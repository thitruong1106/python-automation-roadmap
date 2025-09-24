"""
22/09/2025 
BTC logger - The purpose of this script is to fetch live prices from coinmarketcap api every 10 seconds and log the results into a csv file that includes (timestamp, code name, and usd price)
"""

from datetime import datetime
import os, time, csv, requests
from dotenv import load_dotenv
#load environments from env
load_dotenv() 
API_KEY = os.getenv("coinmarketcap") 

URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest" #url 
#request json from cmc
HEADERS = {
    "Accepts": "application/json", 
    "X-CMC_PRO_API_KEY": API_KEY} 

def ensure_header(path):
    #If file doesnt exits, or file exist with 0 bytes
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        #open the file, or create if file doesnt exists
        with open(path, "a", newline="", encoding="utf-8") as f:
            #write the header row once
            csv.writer(f).writerow(["timestamp", "symbol", "price_usd"])

def fetch_price(symbol="BTC"): #fetch prices for BTC only 
    #send HTTP get request to url, headers,symbol name,and convert to usd price, timeout after 10 seconds without response
    r = requests.get(URL, headers=HEADERS, params={"symbol": symbol, "convert": "USD"}, timeout=10)
    r.raise_for_status()
    return r.json()["data"][symbol]["quote"]["USD"]["price"]

#logger function 
def log_row(path, ts, symbol, price):
    with open(path, "a", newline="", encoding="utf-8") as f:
        #write timestamp, crpto name, and price into csv 
        csv.writer(f).writerow([ts, symbol, f"{price:.2f}"])
#function called man, taking parameters (BTC, how often it should fetch prices, duration of script, and csv path)
def main(symbol="BTC", cooldown=10, duration=60, csv_path="btc_log.csv"):
    #log header to file
    ensure_header(csv_path)
    #run for 1 minute 
    end = time.monotonic() + duration
    #last printed, 0 as never printed 
    last = 0.0
    while time.monotonic() < end: #while current time is less than end 
        now = time.monotonic()
        if now - last >= cooldown:
            price = fetch_price(symbol)
            ts = datetime.now().isoformat(timespec="seconds")
            log_row(csv_path, ts, symbol, price)
            #print in terminal 
            print(f"{ts} | {symbol}: ${price:.2f}")
            last = now
        time.sleep(0.5)

if __name__ == "__main__":
    main()
