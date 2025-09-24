"""
Discord test of webhook
Warm-up

Create a small function that sends a message to a Discord webhook
"""

from dotenv import load_dotenv
import os 

load_dotenv()
WEBHOOK = os.getenv("discord_visual_hook")
import requests

def discord_send(content: str, webhook: str, timeout: int = 10):
    if not webhook:
        raise ValueError("Missing Discord webhook URL")

    resp = requests.post(
        webhook,
        json={"content": content},
        timeout=timeout,
    )
    # Discord returns 204 No Content on success
    if resp.status_code not in (200, 204):
        raise RuntimeError(f"Discord error {resp.status_code}: {resp.text}")

discord_send("hello, i sent a message using python and visual studio", WEBHOOK)