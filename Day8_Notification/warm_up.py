"""
27/09/2025

Warm up drill 
- Write a tiny function 


"""
import os 
from dotenv import load_dotenv
import requests
load_dotenv()
WEBHOOK = os.getenv("discord_visual_hook")


def discord_send(content: str, webhook:str, timeout: int = 10):
    if not webhook:
        raise ValueError("Missing discord webhook url")
    r = requests.post(
        webhook,
        json={"content": content},
        timeout = timeout
    )
    if r.status_code not in (200,204):
        #request havs failed 
        raise RuntimeError(f"Discord error {r.status_code}: {r.text}")
    
discord_send("**BTC ALERT 🚨**\nPrice dropped below $60k", WEBHOOK)

#function to send alert  

def send_alert(msg, use_console = True, use_discord=False): #default values, unless changed
    if use_console:
        print(f"[ALERT]{msg}")
    if use_discord:
        discord_send(msg, WEBHOOK)

send_alert("testing message", use_console = False, use_discord=True)