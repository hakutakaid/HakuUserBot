#Created By HakutakaID # TELEGRAM t.me/hakutakaid
import logging
import time
from datetime import datetime
from pyrogram import Client as mecha
from pyrogram import filters as indri
from pyrogram.handlers import CallbackQueryHandler, MessageHandler
from config import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

START_TIME = datetime.now()

StartTime = time.time()

class Ubot(mecha):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_message(self, filters=None, group=-1):
        def decorator(func):
            self.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    async def start(self):
        await super().start()
        logger.info("Bot started")

ubot = Ubot(
    name="sange",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION,
    in_memory=True,
)

from HakuBot.helpers import *
