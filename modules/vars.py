import os

API_ID    = os.environ.get("API_ID", "25030447")
API_HASH  = os.environ.get("API_HASH", "4fa50720e0d5194c515d1586ddfc0b20")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
