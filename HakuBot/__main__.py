#Created By HakutakaID # TELEGRAM t.me/hakutakaid
import asyncio
import importlib
import logging
from pyrogram import idle
from HakuBot import ubot
from HakuBot.modules import ALL_MODULES
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("HakuBot.modules." + all_module)
        logger.info(f"Module {all_module} imported")
        
    await ubot.start()
    await idle()
    logger.info("Bot is idle")

if __name__ == "__main__":
    logger.info("Starting bot")
    asyncio.get_event_loop().run_until_complete(start_bot())
    logger.info("Bot stopped")