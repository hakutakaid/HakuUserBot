#Created By HakutakaID # TELEGRAM t.me/hakutakaid
from pyrogram import Client

hai = Client(
    name="HakuBot",
    api_id=26522923,
    api_hash="d3fb3a6e5c23345409a5e100175fca84",
)

async def main():
    await hai.start()
    janckk = await hai.export_session_string()
    print(janckk)
    await hai.stop()

import asyncio
asyncio.run(main())