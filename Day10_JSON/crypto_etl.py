"""
2/10/2025 - crypto_etl.py 

This script is an end to end mini ETL for crypto prices 
1. Generate sample price data and save it to JSON 
2.Load the JSON and compute per symbol min, max, average 
3.Save the summary to json and print report 

"""
import json, random 
from datetime import datetime, timedelta
from statistics import mean 
from typing import List, Dict, Any

#write a json file 
def save_json(path, obj): 
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=4)
    print(f"✅ Saved: {path}")
#reading json file
def load_json(path): 
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

#generate fake crypto data 
def generate_fake_crypto(symbols, n_per_symbol=4):
    now = datetime.now()
    out = []
    #Prices will be randomized +- 10% of the base value declared
    base = {
        "BTC": 65000,
        "ETH":3500,
        "SOL": 150,
    }

    for sym in symbols:
        base_price = base.get(sym, 1000)
        for i in range(n_per_symbol):
            ts = (now - timedelta(minutes=i)).isoformat(timespec="seconds")
            jitter = random.uniform(-0.10, 0.10) * base_price #+- 10%
            price = round(base_price + jitter, 2)
            out.append({"symbol": sym, "price_usd": price, "ts": ts})
    return out

#Transforming the data 
def summarize_crypto(rows):
    #Get the min, max, average 
    all_prices = {} #sym -> list of prices 
    for row in rows: 
        sym = row["symbol"]
        price = float(row["price_usd"])
        if sym not in all_prices:
            all_prices[sym] = []
        all_prices[sym].append(price)

    summary = {}
    for sym, prices in all_prices.items():
        summary[sym] = {
            "min": min(prices),
            "max": max(prices),
            "avg": round(mean(prices), 2),
            "count": len(prices),
        }
    return summary

#load and print 
def print_summary(summary):
    print("\n Crypto Summary")
    print("-----------------")
    for sym in sorted(summary.keys()):
        s = summary[sym]
        print(f"{sym}: min=${s['min']:,.2f} | max=${s['max']:,.2f} | avg=${s['avg']:,.2f} (n={s['count']})")

def main():
    symbols = ["BTC", "ETH"]
    raw_path = "crypto_log.json"
    summary_path = "crypto_summary.json"
    #Generate and save the fake data 
    rows = generate_fake_crypto(symbols, n_per_symbol=6) #generate 6 instances for given symbol
    save_json(raw_path, rows)
    #Load raw and summarized 
    data = load_json(raw_path) #load crypto_log.json
    summary = summarize_crypto(data)
    #Save and print report 
    save_json(summary_path, summary)
    print_summary(summary) #pretty print in terminal 

if __name__ == "__main__":
    main()