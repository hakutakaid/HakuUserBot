#Created By HakutakaID # TELEGRAM t.me/hakutakaid
import os
from dotenv import load_dotenv

load_dotenv(".env")

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")
prefix = [".", "", "-"]
DEVS = [1831850761]

if not all([API_ID, API_HASH, SESSION]):
    raise ValueError("Missing one or more environment variables: API_ID, API_HASH, SESSION")