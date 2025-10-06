import os 
from dotenv import load_dotenv
import requests, logging
load_dotenv()
WEBHOOK = os.getenv("discord_visual_hook")

def send_discord(content: str, webhook: str, timeout: int = 10):
    if not webhook:
        return 
    r = requests.get(
        webhook = webhook,
        json = {"content": content}, 
        timeout = timeout
    )
    if r.status_code not in (200,204):
        logging.error(f"Discord error {r.status_code}: {r.text}")
