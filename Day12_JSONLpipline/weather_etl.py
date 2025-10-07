"""
Day 12: - Weather ETL (JSONL)

The purpose of this script is to 
- append weather events to json logs 
- Read and filter logs (today only)
- summarize min/max/avg per city 
- save summary to json and print a report 

"""

import json
from datetime import datetime
from statistics import mean 

def append_jsonl(path, obj):
    with open(path, 'a', encoding='utf-8') as f:
        json.dump(obj,f)
        f.write("\n") #seprates JSON object by line
#reading back a jsonl file 
def read_jsonl(path):
    rows = []
    with open(path, 'r', encoding="utf-8") as f:
        for line in f: #for line in file 
            line = line.strip() #clean the line 
            if line: #if line is valid
                try:
                    rows.append(json.loads(line)) #append line to rows 
                except json.JSONDecodeError:
                    print(f"Skipping invalid line")
    return rows 
#sav json file 
def save_json(path,obj):
    with open(path, 'w', encoding="utf-8") as f:
        json.dump(obj, f, indent=2)
    print(f"Saved summary to {path}")

#event logging
def log_weather_event(city,temp,desc, path="weather_log.jsonl"):
    event = {
        "type": 'weather',
        "ts": datetime.now().isoformat(timespec="seconds"),
        "city": city,
        "temp": temp, 
        "desc": desc
    }
    append_jsonl(path, event)
    print(f"Logged weather {city} | {temp} | {desc}")

#filter for rainy events 
def filter_rain(rows):
    rainy = [r for r in rows if "rain" in r["desc"].lower()]
    return rainy

def filter_today(rows):
    #keep entry that starts where ts starts with today dates
    today = datetime.now().date().isoformat()
    return [r for r in rows if str(r.get("ts", "")).startswith(today)]

def summarize_weather(rows):
    groups = {}
    for row in rows:
        city = row["city"]
        temp = float(row["temp"])
        if city is None or temp is None:
            continue
        groups.setdefault(city, []).append(float(temp))

    report = {}
    for city, temps in groups.items():
        report[city] = {
            "min": min(temps),
            "max": max(temps),
            "avg": round(mean(temps), 2),
            "count": len(temps)
        }
    return report

#print in terminal
def print_summary(summary):
    print("\n weather summary")
    print("-------------------")
    for city,stats, in summary.items():
        print(f"{city}: min{stats['min']} | max = {stats['max']} avg = {stats['avg']}")


def run_daily_summary(jsonl_path="weather_log.jsonl", summary_path="weather_summary.json"):
    #read json file
    rows = read_jsonl(jsonl_path)
    #filter for today entrys
    rows_today = filter_today(rows)
    #summarise the entry
    summary = summarize_weather(rows_today)
    #print in terminal
    print_summary(summary)
    #save to file
    save_json(summary_path, summary)

if __name__ == "__main__":
    run_daily_summary()