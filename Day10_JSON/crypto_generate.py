import json 
from datetime import datetime 

crypto_data = [
    {
        "symbol": 'BTC',
        'price_usd': 70000,
        'ts': datetime.now().isoformat(timespec='seconds')
    },
    {
        "symbol": 'BTC',
        'price_usd': 58000,
        'ts': datetime.now().isoformat(timespec='seconds')
    },
    {
        "symbol": 'ETH',
        'price_usd': 4000,
        'ts': datetime.now().isoformat(timespec='seconds')
    },
    {
        "symbol": 'ETH',
        'price_usd': 3000,
        'ts': datetime.now().isoformat(timespec='seconds')
    },
    {
        "symbol": 'ADA',
        'price_usd': 20,
        'ts': datetime.now().isoformat(timespec='seconds')
    },
    {
        "symbol": 'ADA',
        'price_usd': 10,
        'ts': datetime.now().isoformat(timespec='seconds')
    },
    ]

#Save the above to json 
with open('crypto_log.json', 'w') as f:
    json.dump(crypto_data, f, indent=4)

print("✅ Saved to fake crypto logs")