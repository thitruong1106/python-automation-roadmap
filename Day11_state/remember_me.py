"""
remember_me.py - Day 11: State and presistence
Date: 06/10/2025

This python script demonstrates basic state persistence using JSON configuration files. 

Features include 
- Remembers a user's name and their favourite pokemon between runs.
- Creates a config.py on first run, and updates when needed 
- safely loads and save JSON data. 

"""

import json, os 

CONFIG_PATH = "config.json" 

def load_config(path=CONFIG_PATH):
    if os.path.exists(path): #If file exists 
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("config.json is corrupt.")
            return {} #nothing has been saved 
    return{}#if file doesnt exisits, return empty dict instead of none
def save_config(cfg, path=CONFIG_PATH):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(cfg, f, indent=2)

def ask_nonempty(prompt):
    #Ask user to type something
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("Please enter something non-empty.")

def main(): 
    cfg = load_config()
    if "name" in cfg and 'pokemon' in cfg:
        #returning users 
        print(f"welcome back{cfg['name']} your fav pokemon is {cfg['pokemon']}")
        #optional: letting user update 
        choice = input("Do you want to update your favourite pokemon").strip().lower()
        if choice == "y":
            name = input("Enter your name: \n").strip()
            pokemon = input("Enter your favrouite pokemon: \n").strip()
            #keep old value if users just presses enter to skip
            cfg[name] = name or cfg["name"]
            cfg[pokemon] = pokemon or cfg["pokemon"]
            save_config(cfg)
            print("Updated !")
    else: #if name or pokemon not in config / First run 
        print("Hi, i dont know this user yet")
        name = input("Enter your name").strip()
        pokemon = input("Enter your favuorite pokemon").strip() 

        cfg = {
            "name": name.title(),
            "pokemon": pokemon.title(),
            }
        save_config(cfg)
        print(f"Nice to meet you, {name}! i will remember your favourite pokemon is {pokemon}")

if __name__ == "__main__":
    main()

 