#anaylse data.

#load the json file 
import json 

with open('crypto_log.json', 'r') as f:
    data = json.load(f)

summary = {}

for entry in data: #for each entry in the dataset 
    sym = entry['symbol']
    price = entry['price_usd']

    if sym not in summary:
        summary[sym] = {"prices": []}
    
    summary[sym]['prices'].append(price)

#compute stats using price 
for sym,stats in summary.items():
    prices=stats['prices']
    avg_price = sum(prices) / len(prices)
    print(f"{sym}: min={min(prices)} max={max(prices)}, avg={avg_price:,.2f}")

