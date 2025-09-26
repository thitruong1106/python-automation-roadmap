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
WEBHOOK = os.getenv("discord_visual_hook") #get api url for discord webhook 
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

def fetch_price(symbol): #fetch prices for symbol 
    #send HTTP get request to url, headers,symbol name,and convert to usd price, timeout after 10 seconds without response
    r = requests.get(URL, headers=HEADERS, params={"symbol": symbol, "convert": "USD"}, timeout=10)
    r.raise_for_status()
    return r.json()["data"][symbol]["quote"]["USD"]["price"]

#logger function 
def log_row(path, ts, symbol, price):
    with open(path, "a", newline="", encoding="utf-8") as f:
        #write timestamp, crpto name, and price into csv 
        csv.writer(f).writerow([ts, symbol, f"{price:.2f}"])

def discord_send(content: str, webhook: str, timeout: int = 10):
    if not webhook:
        raise ValueError("missing discord webhook url")
    resp = requests.post(
        webhook, 
        json={"content": content}, 
        timeout = timeout)
    if resp.status_code not in (200,204):
        raise RuntimeError(f"Discord error {resp.status_code}: {resp.text}")
    
#function called man, taking parameters (BTC, how often it should fetch prices, duration of script, and csv path)
#alert discord if the price is below 60000
#symbol - fetchign BTC prices
#cooldown, how often to fetch price 
#duration, how long to run 
#alert_threshold, alert when btc reaches this price 
#alert cooldown mins(seconds) between discord alerts
def main(symbol=("BTC","ETH"), cooldown=10, duration=60, csv_path="btc_log.csv",alert_threshold={"BTC": 60000, "ETH":3000}, alert_cooldown=600):
    #log header to file
    ensure_header(csv_path)
    #run for 1 minute 
    end = time.monotonic() + duration
    #last printed, 0 as never printed 
    last = 0.0
    last_alert = {s: -1e9 for s in symbol}
    while time.monotonic() < end: #while current time is less than end 
        now = time.monotonic()
        if now - last >= cooldown:
            #fetch timestamp
            ts = datetime.now().isoformat(timespec="seconds")
            #for each symbol in symbol
            for sym in symbol:
                price = fetch_price(sym) #fetch price for each symbol 
                #log and print 
                log_row(csv_path, ts,sym,price)
                print(f"{ts} | {sym}: ${price:,.2f}")

                #alert checking 
                if sym in alert_threshold and price <= alert_threshold[sym]:
                    if now-last_alert[sym] >= alert_cooldown:
                        discord_send(
                            f"🚨 {sym} ≤ ${alert_threshold[sym]:,.0f} — now ${price:,.2f}",WEBHOOK)
                        last_alert[sym] = now #last alert for BTC OR ETC updated 
            last = now
        time.sleep(0.5)

if __name__ == "__main__":
    main()
